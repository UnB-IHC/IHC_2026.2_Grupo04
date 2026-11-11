"""Gera o PDF do relatório de acessibilidade a partir dos textos em conteudo/*.md,
do checklist preenchido (CSV) e das evidências (JSON e capturas).

Uso, a partir da raiz do repositório:

    pip install -r requirements.txt
    python relatorio/gerar.py

Requer Google Chrome, Chromium ou Microsoft Edge (variável CHROME para outro caminho).
O pdftotext (poppler), se instalado, é usado para pôr os números de página no sumário.
"""

import base64
import csv
import html
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import markdown
import yaml

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent
DADOS = RAIZ / "docs/referencia/dados"
EVIDENCIAS = RAIZ / "docs/avaliacao-site/evidencias"
FONTES = RAIZ / "docs/assets/fonts"

SEVERIDADES = ["Bloqueante", "Alta", "Média", "Baixa"]
RESULTADOS = {"❌": "Não conforme", "⚠️": "Parcial", "✅": "Conforme", "⚪": "N/A"}
CLASSE = {"Não conforme": "nc", "Parcial": "parcial", "Conforme": "conforme", "N/A": "na",
          "Bloqueante": "bloqueante", "Alta": "alta", "Média": "media", "Baixa": "baixa"}
VERIFICADO = {"🤖 Agente": "Agente de IA", "🤝 Agente + Humano": "Agente de IA e integrante"}
ONDAS = [("Onda 1", "até 30 dias", ["Bloqueante", "Alta"]),
         ("Onda 2", "30 a 90 dias", ["Média"]),
         ("Onda 3", "90 a 180 dias", ["Baixa"])]
FLUXOS = ["Página inicial", "Rastreamento", "Busca CEP", "Preços e Prazos / Login"]
SECOES = {"5.1": "Teclado e foco", "5.2": "Imagens", "5.3": "Cabeçalhos", "5.4": "Regiões",
          "5.5": "Listas", "5.6": "Tabelas", "5.7": "Links e navegação", "5.8": "Botões e controles",
          "5.9": "Formulários", "5.10": "Apresentação", "5.11": "Cores", "5.12": "Conteúdo textual",
          "5.13": "Codificação semântica", "5.14": "Áudio e vídeo", "5.15": "Animação",
          "Anexo": "Anexo — itens críticos"}

e = html.escape


def sem_emoji(texto):
    return texto.split(" ", 1)[1].strip() if texto and " " in texto else texto.strip()


def carregar_criterios():
    with open(DADOS / "checklist-unificado.csv", encoding="utf-8-sig") as arquivo:
        linhas = [l for l in csv.DictReader(arquivo) if l["Resultado"][:1] in "❌⚠✅⚪"]
    criterios = {}
    for l in linhas:
        nbr = l["Cód. NBR"]
        secao = "Anexo" if nbr.startswith("Anexo") else ".".join(nbr.split(".")[:2])
        criterios[l["Critério"]] = {
            "nome": l["Critério"], "nbr": nbr, "wcag": l["Cód. WCAG"], "secao": secao,
            "nivel": sem_emoji(l["Nível"]), "principio": l["Princípio WCAG"],
            "resultado": next(v for k, v in RESULTADOS.items() if l["Resultado"].startswith(k)),
            "severidade": sem_emoji(l["Severidade da Falha"]),
            "verificado": VERIFICADO[l["Verificado por"]],
        }
    return criterios


def ler_fichas(texto, criterios, evidencias):
    intro, *partes = re.split(r"^## ", texto, flags=re.M)
    fichas = []
    for parte in partes:
        titulo, resto = parte.split("\n", 1)
        meta = re.search(r"<!--\s*criterio:(.*?)\|\s*fluxos:(.*?)\|\s*captura:(.*?)-->", resto)
        assert meta, f"ficha sem metadados: {titulo}"
        nome, fluxos, captura = (m.strip() for m in meta.groups())
        criterio = criterios[nome]
        legendas = dict(evidencias[nome]["imagens"])
        assert captura in legendas, f"{captura} não está nas evidências de {nome}"
        fluxos = [f.strip() for f in fluxos.split(",")]
        assert set(fluxos) <= set(FLUXOS), f"fluxo desconhecido em {titulo}: {fluxos}"
        assert criterio["resultado"] in ("Não conforme", "Parcial"), nome
        fichas.append({**criterio, "titulo": titulo.strip(), "fluxos": fluxos, "captura": captura,
                       "legenda": legendas[captura], "corpo": resto[meta.end():]})
    fichas.sort(key=lambda f: (SEVERIDADES.index(f["severidade"]), f["resultado"] != "Não conforme"))
    for i, ficha in enumerate(fichas, 1):
        ficha["codigo"] = f"AC-{i:02d}"
    com_falha = [c for c in criterios.values() if c["resultado"] in ("Não conforme", "Parcial")]
    assert len(fichas) == len(com_falha), "todo critério não conforme ou parcial precisa de uma ficha"
    return intro, fichas


def imagem(caminho, legenda, codigo=""):
    rotulo = f'<span class="fig-cod">{codigo}</span> ' if codigo else ""
    return (f'<figure><img src="{(EVIDENCIAS / caminho).as_uri()}" alt="{e(legenda)}">'
            f"<figcaption>{rotulo}{e(legenda)}</figcaption></figure>")


def selo(texto):
    return f'<span class="selo {CLASSE[texto]}">{e(texto)}</span>'


def tabela(cabecalho, linhas, classe=""):
    cab = "".join(f"<th scope=\"col\">{c}</th>" for c in cabecalho)
    celula = lambda c: f'<td class="n">{c}</td>' if str(c).isdigit() or c == "—" else f"<td>{c}</td>"
    corpo = "".join("<tr>" + "".join(map(celula, linha)) + "</tr>" for linha in linhas)
    classe += " curta" if len(linhas) <= 6 else ""
    return f'<table class="{classe}"><thead><tr>{cab}</tr></thead><tbody>{corpo}</tbody></table>'


def contagem(lista):
    return [sum(c["resultado"] == r for c in lista) for r in ("Conforme", "Parcial", "Não conforme", "N/A")]


def pior(lista):
    sev = [c["severidade"] for c in lista if c["severidade"]]
    return selo(min(sev, key=SEVERIDADES.index)) if sev else "—"


def numero(n):
    return str(n) if n else "—"


def blocos(criterios, fichas, evidencias, dados):
    todos = list(criterios.values())
    aplicaveis = [c for c in todos if c["resultado"] != "N/A"]
    conf, parc, nc, na = contagem(todos)
    pct = lambda n: f"{round(100 * n / len(aplicaveis))}%"
    sev = {s: sum(c["severidade"] == s for c in todos) for s in SEVERIDADES}
    valores = {
        "total": len(todos), "aplicaveis": len(aplicaveis), "conforme": conf, "parcial": parc,
        "nc": nc, "na": na, "achados": len(fichas), "pct_conforme": pct(conf),
        "pct_parcial": pct(parc), "pct_nc": pct(nc), "alta": sev["Alta"], "media": sev["Média"],
        "baixa": sev["Baixa"], "bloqueante": sev["Bloqueante"],
        "requisitos": sum(c["nivel"].startswith("Requisito") for c in aplicaveis),
        "recomendacoes": sum(c["nivel"].startswith("Recomendação") for c in aplicaveis),
        "data_coleta": dados["data_coleta"], "checklist": dados["checklist"],
    }

    painel = [(len(todos), "critérios avaliados", ""), (nc, "não conformes", "nc"),
              (parc, "parciais", "parcial"), (conf, "conformes", "conforme"),
              (sev["Bloqueante"], "falha bloqueante", "bloqueante")]
    valores["painel"] = '<div class="painel">' + "".join(
        f'<div class="kpi {c}"><strong>{n}</strong><span>{t}</span></div>' for n, t, c in painel) + "</div>"

    partes = [("Conforme", conf), ("Parcial", parc), ("Não conforme", nc), ("N/A", na)]
    barra = "".join(f'<span class="{CLASSE[r]}" style="width:{100 * n / len(todos):.2f}%">{n}</span>'
                    for r, n in partes if n)
    legenda = "".join(f'<li><i class="{CLASSE[r]}"></i>{r}: {n}</li>' for r, n in partes)
    valores["grafico_resultados"] = (f'<div class="grafico" role="img" aria-label="Resultados: '
                                     f'{conf} conformes, {parc} parciais, {nc} não conformes e {na} N/A">'
                                     f'<div class="barra">{barra}</div><ul>{legenda}</ul></div>')

    definicao = {"Bloqueante": "impede concluir a tarefa",
                 "Alta": "a tarefa só é concluída com muito esforço ou ajuda",
                 "Média": "causa confusão ou atraso, mas há contorno", "Baixa": "incômodo pontual"}
    valores["tabela_severidade"] = tabela(
        ["Severidade", "Significado", "Não conformes", "Parciais", "Total"],
        [[selo(s), definicao[s], numero(sum(f["severidade"] == s and f["resultado"] == "Não conforme" for f in fichas)),
          numero(sum(f["severidade"] == s and f["resultado"] == "Parcial" for f in fichas)), sev[s]]
         for s in SEVERIDADES], "num")

    por_secao = {}
    for c in todos:
        por_secao.setdefault(c["secao"], []).append(c)
    ordem = sorted(por_secao, key=lambda s: (-contagem(por_secao[s])[2], s == "Anexo", [int(p) for p in s.split(".") if p.isdigit()]))
    valores["tabela_secoes"] = tabela(
        ["Seção da NBR 17225", "Critérios", "Conformes", "Parciais", "Não conformes", "N/A"],
        [[f"{s if s != 'Anexo' else ''} {SECOES[s]}".strip(), len(por_secao[s]),
          *map(numero, contagem(por_secao[s]))] for s in ordem], "num")

    principios = sorted({c["principio"] for c in todos})
    valores["tabela_principios"] = tabela(
        ["Princípio da WCAG", "Critérios", "Conformes", "Parciais", "Não conformes", "N/A", "Pior severidade"],
        [[p.split(". ", 1)[1], len(grupo), *map(numero, contagem(grupo)), pior(grupo)]
         for p in principios for grupo in [[c for c in todos if c["principio"] == p]]], "num")

    valores["tabela_fluxos"] = tabela(
        ["Fluxo", "Achados", "Não conformes", "Parciais", "Pior severidade", "Fichas"],
        [[f, len(grupo), numero(contagem(grupo)[2]), numero(contagem(grupo)[1]), pior(grupo),
          ", ".join(x["codigo"] for x in grupo)]
         for f in FLUXOS for grupo in [[x for x in fichas if f in x["fluxos"]]]], "num")

    valores["tabela_plano"] = tabela(
        ["Onda", "Prazo", "Severidade", "Achados"],
        [[f"<strong>{onda}</strong>", prazo, " ".join(selo(s) for s in faixa),
          "<ul>" + "".join(f'<li><span class="cod">{x["codigo"]}</span> {e(x["titulo"])}</li>'
                           for x in fichas if x["severidade"] in faixa) + "</ul>"]
         for onda, prazo, faixa in ONDAS], "plano")

    valores["indice_achados"] = tabela(
        ["Ficha", "Achado", "Fluxos", "Resultado", "Severidade"],
        [[f'<span class="cod">{x["codigo"]}</span>', e(x["titulo"]), ", ".join(x["fluxos"]),
          selo(x["resultado"]), selo(x["severidade"])] for x in fichas], "indice")

    humanos = [c["nome"] for c in todos if c["verificado"] != "Agente de IA"]
    valores["tabela_verificacao"] = tabela(
        ["Verificado por", "Critérios", "Quais"],
        [["Agente de IA, com revisão do grupo", len(todos) - len(humanos), "os demais"],
         ["Agente de IA e integrante do grupo", len(humanos), "; ".join(map(e, humanos))]], "num")

    codigo_de = {x["nome"]: x["codigo"] for x in fichas}
    ordem_inv = [x["nome"] for x in fichas] + sorted(
        (c["nome"] for c in todos if c["nome"] not in codigo_de), key=lambda n: criterios[n]["resultado"] == "N/A")
    valores["inventario"] = tabela(
        ["Critério", "NBR", "WCAG", "Nível", "Resultado", "Severidade", "Verificado por", "Achado"],
        [[e(c["nome"]), e(c["nbr"]), e(c["wcag"]), e(c["nivel"]), selo(c["resultado"]),
          selo(c["severidade"]) if c["severidade"] else "—", c["verificado"], codigo_de.get(c["nome"], "—")]
         for c in map(criterios.get, ordem_inv)], "inventario")

    mostradas = {x["captura"] for x in fichas}
    figuras = []
    for x in fichas:
        for caminho, legenda in evidencias[x["nome"]]["imagens"]:
            if caminho not in mostradas:
                mostradas.add(caminho)
                figuras.append(imagem(caminho, legenda, x["codigo"]))
    valores["capturas"] = '<div class="galeria">' + "".join(figuras) + "</div>"
    return valores


def preencher(texto, valores):
    return re.sub(r"\{\{\s*(\w+)\s*\}\}", lambda m: str(valores[m.group(1)]), texto)


def md(texto):
    return markdown.markdown(texto, extensions=["tables", "fenced_code", "sane_lists"])


CAMPOS = ["O que foi observado", "Medição registrada", "Onde", "Quem é afetado",
          "Correção recomendada", "Como verificar a correção"]


def ficha_html(x):
    partes = re.split(r"<p><strong>([^<]+)</strong></p>", md(x["corpo"]))[1:]
    campos = dict(zip(partes[::2], partes[1::2]))
    assert list(campos) == CAMPOS, f"campos fora do padrão em {x['titulo']}: {list(campos)}"
    campo = lambda nome: f'<div class="campo"><p class="rotulo">{nome}</p>{campos[nome]}</div>'
    corpo = "".join(map(campo, CAMPOS[:3])) + '<div class="trio">' + "".join(map(campo, CAMPOS[3:])) + "</div>"
    meta = [("Critério", e(x["nome"])), ("Fluxos", ", ".join(x["fluxos"])), ("Verificado por", x["verificado"])]
    return (f'<section class="achado {CLASSE[x["severidade"]]}" id="{x["codigo"].lower()}">'
            f'<header><p class="achado-selos">{selo(x["resultado"])} {selo(x["severidade"])}</p>'
            f'<h2><span class="cod">{x["codigo"]}</span> {e(x["titulo"])}</h2>'
            f'<p class="achado-ref">NBR 17225 {e(x["nbr"])} · WCAG {e(x["wcag"])} · {e(x["nivel"])}</p>'
            f'<dl>{"".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in meta)}</dl></header>'
            f'{imagem(x["captura"], x["legenda"])}<div class="achado-corpo">{corpo}</div></section>')


def capitulos(valores, intro_achados, fichas):
    saida, sumario = [], []
    arquivos = sorted((AQUI / "conteudo").glob("*.md"))
    anexos = iter("ABCDEFG")
    numero_cap = 0
    for arquivo in arquivos:
        texto = intro_achados if arquivo.name.endswith("achados.md") else arquivo.read_text(encoding="utf-8")
        texto = preencher(texto, valores)
        titulo = re.search(r"^# (.+)$", texto, flags=re.M).group(1)
        corpo = md(texto.replace(f"# {titulo}", "", 1))
        if arquivo.name.startswith("9"):
            rotulo = f"Anexo {next(anexos)}"
        else:
            numero_cap += 1
            rotulo = str(numero_cap)
        ancora = f"cap-{rotulo.lower().replace(' ', '-')}"
        sumario.append((rotulo, titulo, ancora, 1))
        if arquivo.name.endswith("achados.md"):
            corpo += "".join(map(ficha_html, fichas))
            sumario += [(x["codigo"], x["titulo"], x["codigo"].lower(), 2) for x in fichas]
        saida.append(f'<section class="capitulo"><h1 id="{ancora}"><span class="num">{e(rotulo)}</span> '
                     f"{e(titulo)}</h1>{corpo}</section>")
    return "".join(saida), sumario


def capa(d):
    logo = (AQUI / "assets/unb.svg").read_text(encoding="utf-8")
    equipe = "".join(f"<li>{e(n)}</li>" for n in d["equipe"])
    return f"""
<section class="capa">
  <header class="capa-topo">{logo}<p>{e(d["instituicao"])}<br>{e(d["campus"])}</p></header>
  <div class="capa-titulo">
    <p class="sobre">Relatório técnico</p>
    <h1 class="titulo-doc">{e(d["objeto"])}</h1>
    <p class="subtitulo">{e(d["subtitulo"])}</p>
  </div>
  <dl class="capa-meta">
    <div><dt>Destinatário</dt><dd>{e(d["destinatario"])}<br>{e(d["destinatario_area"])}</dd></div>
    <div><dt>Elaboração</dt><dd>{e(d["grupo"])} · {e(d["disciplina"])} ({e(d["codigo_disciplina"])}), {e(d["semestre"])}</dd></div>
    <div><dt>Data da coleta</dt><dd>{e(d["data_coleta"])}</dd></div>
  </dl>
  <footer class="capa-rodape">{e(d["local"])}, {e(d["data_extenso"])}</footer>
</section>
<section class="identificacao">
  <h2 class="sem-numero">Identificação</h2>
  <dl class="ficha-tecnica">
    <div><dt>Instituição</dt><dd>{e(d["instituicao"])} - {e(d["campus"])}</dd></div>
    <div><dt>Disciplina</dt><dd>{e(d["disciplina"])} ({e(d["codigo_disciplina"])}) - semestre {e(d["semestre"])}</dd></div>
    <div><dt>Docente</dt><dd>{e(d["docente"])}</dd></div>
    <div><dt>Equipe</dt><dd>{e(d["grupo"])}<ul class="equipe">{equipe}</ul></dd></div>
    <div><dt>Objeto</dt><dd>{e(d["objeto"])}</dd></div>
    <div><dt>Referências</dt><dd>ABNT NBR 17225:2025<br>WCAG 2.2 (W3C)<br>Lei nº 13.146/2015, art. 63</dd></div>
    <div><dt>Coleta</dt><dd>{e(d["data_coleta"])}</dd></div>
    <div><dt>Evidências</dt><dd>Checklist público com medições, capturas e passo a passo de cada teste:<br><a href="{e(d["checklist"])}">{e(d["checklist"])}</a></dd></div>
  </dl>
</section>"""


def sumario_html(itens, paginas):
    linhas = "".join(
        f'<li class="n{nivel}"><a href="#{ancora}"><span class="num">{e(rotulo)}</span>'
        f'<span class="tit">{e(titulo)}</span><span class="pag">{paginas.get(ancora, "00")}</span></a></li>'
        for rotulo, titulo, ancora, nivel in itens)
    return f'<section class="sumario"><h2 class="sem-numero">Sumário</h2><ol>{linhas}</ol></section>'


def documento(d, miolo, itens, paginas):
    fontes = {n: base64.b64encode((FONTES / f"manrope-{n}.ttf").read_bytes()).decode() for n in ("regular", "bold")}
    css = (AQUI / "estilo.css").read_text(encoding="utf-8")
    css = css.replace("{{fonte_regular}}", fontes["regular"]).replace("{{fonte_bold}}", fontes["bold"])
    css = css.replace("{{cabecalho}}", f'{d["titulo"]} - {d["objeto"]}')
    css = css.replace("{{rodape}}", f'{d["instituicao"]} · {d["disciplina"]} {d["semestre"]} · {d["grupo"]}')
    return (f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
            f'<title>{e(d["titulo"])} - {e(d["objeto"])}</title><style>{css}</style></head>'
            f"<body>{capa(d)}{sumario_html(itens, paginas)}{miolo}</body></html>")


def navegador():
    candidatos = [os.environ.get("CHROME"), "google-chrome", "google-chrome-stable", "chromium",
                  "chromium-browser", "msedge", "microsoft-edge",
                  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
                  "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
                  r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                  r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"]
    for c in filter(None, candidatos):
        if shutil.which(c) or Path(c).exists():
            return shutil.which(c) or c
    sys.exit("Chrome, Chromium ou Edge não encontrado. Defina CHROME com o caminho do navegador.")


def imprimir(html_doc, pdf, pasta):
    pagina = Path(pasta) / "relatorio.html"
    pagina.write_text(html_doc, encoding="utf-8")
    subprocess.run([navegador(), "--headless", "--disable-gpu", "--no-pdf-header-footer",
                    "--generate-pdf-document-outline", f"--user-data-dir={Path(pasta) / 'perfil'}",
                    f"--print-to-pdf={pdf}", pagina.as_uri()],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def numeros_de_pagina(pdf, itens):
    if not shutil.which("pdftotext"):
        print("pdftotext não encontrado: sumário sem números de página.")
        return {}
    texto = subprocess.run(["pdftotext", "-layout", str(pdf), "-"], capture_output=True, text=True, check=True).stdout
    paginas = [[l.strip() for l in p.splitlines()] for p in texto.split("\f")]
    resultado, inicio = {}, 0
    for rotulo, titulo, ancora, nivel in itens:
        # fichas (nível 2) são achadas pelo código, porque o título pode quebrar em duas linhas
        alvo = re.compile(rf"{re.escape(rotulo)} .*" if nivel == 2 else rf"(?:{re.escape(rotulo)}\s+)?{re.escape(titulo)}")
        for i in range(inicio, len(paginas)):
            if nivel == 2 and "OQUEFOIOBSERVADO" not in re.sub(r"\s", "", "".join(paginas[i])):
                continue  # pula o índice de achados, que também lista os códigos
            if any(alvo.fullmatch(re.sub(r"\s+", " ", l)) for l in paginas[i]):
                resultado[ancora], inicio = i + 1, i
                break
    faltando = [t for _, t, a, _ in itens if a not in resultado]
    if faltando:
        print("Sem número de página no sumário para:", "; ".join(faltando))
    return resultado


def main():
    dados = yaml.safe_load((AQUI / "relatorio.yml").read_text(encoding="utf-8"))
    criterios = carregar_criterios()
    evidencias = json.loads((DADOS / "evidencias-correios.json").read_text(encoding="utf-8"))
    achados = next((AQUI / "conteudo").glob("*achados.md")).read_text(encoding="utf-8")
    intro, fichas = ler_fichas(achados, criterios, evidencias)
    valores = blocos(criterios, fichas, evidencias, dados)
    miolo, itens = capitulos(valores, intro, fichas)
    saida = RAIZ / dados["saida"]
    saida.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as pasta:
        rascunho = Path(pasta) / "rascunho.pdf"
        imprimir(documento(dados, miolo, itens, {}), rascunho, pasta)
        paginas = numeros_de_pagina(rascunho, itens)
        imprimir(documento(dados, miolo, itens, paginas), saida, pasta)
    print(f"PDF gerado: {saida.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()

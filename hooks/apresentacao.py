"""Adapta a apresentação do conteúdo sem modificar os documentos de origem."""

import csv
import html
import re
from pathlib import Path
from mkdocs.structure.toc import AnchorLink

ARROW = '<svg class="portal-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M5 12h14m-6-6 6 6-6 6"/></svg>'


def on_nav(nav, config, files):
    sections = {item.title: item for item in nav.items if getattr(item, "children", None)}
    for file in files.documentation_pages():
        page = file.page
        if page is None or page in nav.pages:
            continue
        source = file.src_uri
        if source.startswith(("avaliacao-site/", "referencia/criterios/")) or source == "guia/checklist.md":
            parent = "Correios"
        elif source.startswith("guia/"):
            parent = "Guia"
        else:
            parent = "Projeto"
        page.parent = sections[parent]
    return nav


def _page_context(page):
    source = page.file.src_uri
    groups = [
        ("fundamentos", "Fundamentos", ["necessidades-de-acessibilidade", "principios-pour", "niveis-de-conformidade", "tecnologia-assistiva", "leitor-de-tela", "pilares"]),
        ("normas", "Normas e contexto", ["nbr-abnt", "wcag", "introducao", "nbr-17225"]),
        ("interface", "Interface e implementação", ["semantica-html", "nome-acessivel", "arvore-de-acessibilidade", "aria", "landmarks", "foco-do-teclado", "contraste-de-cores", "texto-alternativo", "refluxo-e-zoom", "linguagem-simples", "captcha"]),
        ("experiencia", "Experiência do usuário", ["ux-design-empatico", "personas-jornadas", "blueprint-canvas", "heuristicas-nielsen"]),
        ("consulta", "Ferramentas e consulta", ["kit-de-ferramentas", "ferramentas", "glossario-az", "checklist-modelo"]),
    ]
    trail = []
    if source.startswith("referencia/criterios/"):
        trail = [("Correios", "avaliacao-site/"), ("Checklist", "avaliacao-site/checklist-correios/")]
    elif source.startswith("avaliacao-site/") or source in [
        "referencia/auditoria-site-dos-correios.md",
        "referencia/human-in-the-loop.md", "referencia/auditoria-assistida.md",
        "referencia/procedimento-de-auditoria.md", "guia/checklist.md",
    ]:
        trail = [("Correios", "avaliacao-site/")]
    elif source.startswith("teste-usabilidade/"):
        trail = [("Usabilidade", "teste-usabilidade/")]
    elif source == "guia/index.md":
        trail = [("Guia", "guia/")]
    else:
        stem = Path(source).stem
        for slug, label, names in groups:
            if (stem in names and source.startswith(("guia/", "referencia/"))) or source == f"guia/{slug}/index.md":
                trail = [("Guia", "guia/"), (label, f"guia/{slug}/")]
                break
        if not trail and source != "index.md":
            trail = [("Projeto", "gestao/")]
            if not source.startswith("gestao/"):
                trail.append(("Acervo", "materiais/"))
    page.meta["portal_trail"] = [
        {"title": title, "url": url} for title, url in trail if url != getattr(page, "url", "")
    ]
    complements = {
        "referencia/nbr-abnt.md": ("Notas sobre a NBR 17225", "guia/nbr-17225/"),
        "referencia/principios-pour.md": ("Pilares da acessibilidade", "guia/pilares/"),
        "referencia/kit-de-ferramentas.md": ("Pesquisa de ferramentas", "guia/ferramentas/"),
    }
    if source in complements:
        title, url = complements[source]
        page.meta["portal_complement"] = {"title": title, "url": url}
    notices = {
        "avaliacao-site/site-escolhido.md": "Registro inicial ainda por atualizar. O roteiro disponível no projeto já trata do site dos Correios.",
        "avaliacao-site/relatorio-inspecao.md": "Estrutura de relatório em preparação. Este documento ainda não contém achados de uma inspeção concluída.",
        "avaliacao-site/recomendacoes.md": "Estrutura em preparação. As recomendações ainda precisam ser preenchidas a partir dos achados da avaliação.",
    }
    if source.startswith("teste-usabilidade/") and not source.endswith("index.md"):
        page.meta["portal_notice"] = "Documento de trabalho em preparação. O material disponível ainda não registra a execução do teste nem resultados com participantes."
    elif source in notices:
        page.meta["portal_notice"] = notices[source]


def on_page_markdown(markdown, page, config, files):
    source = page.file.src_uri
    _page_context(page)
    if source == "gestao/equipe.md":
        return (Path(config["docs_dir"]) / "index.md").read_text(encoding="utf-8")
    if source == "design/design.md":
        markdown = re.sub(r'(<a\s+id="[^"]+")(?=href=)', r'\1 ', markdown)
    if source == "index.md":
        page.meta["portal_home"] = True
        page.meta["hide"] = ["toc"]
        return re.sub(r"^# ", "## ", markdown, count=1)
    if source.startswith("referencia/"):
        fenced = False
        first_title = True
        lines = []
        for line in markdown.splitlines(keepends=True):
            if line.lstrip().startswith("```"):
                fenced = not fenced
            if not fenced and line.startswith("# "):
                if first_title:
                    first_title = False
                else:
                    line = "#" + line
            lines.append(line)
        return "".join(lines)
    return markdown


def _criterion_details(content):
    blocks = list(re.finditer(r"<p>([^<\n]+?): (.*?)</p>", content, re.S))
    if not blocks:
        return content
    fields = []
    for block in blocks:
        label, value = block.groups()
        wide = ' class="criterion-details__wide"' if label == "Como Testar" else ""
        fields.append(f"<div{wide}><dt>{label}:</dt><dd>{value}</dd></div>")
    details = '<dl class="criterion-details">' + "".join(fields) + "</dl>"
    return content[:blocks[0].start()] + details + content[blocks[-1].end():]


CHECKLIST_SLOT = '<div data-checklist-slot></div>'
CHECKLISTS = {
    "guia/checklist-modelo.md": {"csv": "checklist-modelo.csv", "filled": False},
    "avaliacao-site/checklist-correios.md": {"csv": "checklist-unificado.csv", "filled": True},
}
ANSWERS = ["Conforme", "Parcialmente conforme", "Não conforme", "Não se aplica"]


def _esc(value):
    return html.escape(value or "", quote=True)


def _criterion_links(page, files):
    """Associa o título de cada ficha de critério ao link relativo à página atual."""
    links = {}
    for file in files.documentation_pages():
        if not file.src_uri.startswith("referencia/criterios/"):
            continue
        text = Path(file.abs_src_path).read_text(encoding="utf-8")
        title = re.search(r"^# (.+)$", text, re.M)
        if title:
            links[html.unescape(title[1].strip())] = file.url_relative_to(page.file)
    return links


def _filter_select(key, label, values, everything):
    options = f'<option value="">{everything}</option>' + "".join(
        f'<option value="{_esc(v)}">{html.escape(v)}</option>' for v in values
    )
    return f'''<label for="criterion-{key}">{label}
          <select id="criterion-{key}" data-filter="{key}" aria-controls="checklist-table">{options}</select>
        </label>'''


def _checklist(page, config, files):
    settings = CHECKLISTS[page.file.src_uri]
    filled = settings["filled"]
    file = Path(config["docs_dir"]) / "referencia/dados" / settings["csv"]
    with file.open(encoding="utf-8-sig", newline="") as stream:
        rows = [r for r in csv.DictReader(stream) if r["Cód. NBR"]]
    links = _criterion_links(page, files)
    missing = [r["Critério"] for r in rows if r["Critério"] not in links]
    assert not missing, f"Critérios sem ficha correspondente: {missing}"

    filters = _filter_select("principle", "Princípio WCAG", sorted({r["Princípio WCAG"] for r in rows}), "Todos os princípios")
    if filled:
        filters += _filter_select("result", "Resultado", sorted({r["Resultado"] or "Sem registro" for r in rows}), "Todos os resultados")
    tools = f'''<div class="checklist-tools" data-checklist-tools hidden>
      <div class="checklist-tools__fields">
        <label for="criterion-query">Buscar no checklist
          <input type="search" id="criterion-query" placeholder="Critério, código ou palavra-chave" autocomplete="off" aria-controls="checklist-table">
        </label>
        {filters}
        <button type="button" class="filter-reset" data-filter-reset>Limpar filtros</button>
      </div>
      <p class="checklist-count" role="status" aria-live="polite" aria-atomic="true" data-checklist-count>{len(rows)} critérios</p>
    </div>'''

    if filled:
        headers = ["Critério", "Cód. NBR", "Cód. WCAG", "Camada de teste", "Resultado", "Severidade", "Observações / Evidências", "Verificado por"]
    else:
        headers = ["Critério", "Cód. NBR", "Cód. WCAG", "Como testar", "Resultado", "Observações"]
        tools = '''<div class="checklist-answers" data-checklist-answers hidden>
      <label for="checklist-site">Site ou página avaliada
        <input type="url" id="checklist-site" data-answer="site" placeholder="https://" autocomplete="url">
      </label>
      <div class="checklist-answers__actions">
        <button type="button" class="checklist-export" data-checklist-export>Exportar respostas (CSV)</button>
        <button type="button" class="filter-reset" data-checklist-clear>Apagar respostas</button>
      </div>
      <p class="checklist-count" role="status" aria-live="polite" aria-atomic="true" data-checklist-progress>0 de ''' + str(len(rows)) + ''' critérios avaliados</p>
    </div>''' + tools

    body = []
    for record in rows:
        name = record["Critério"]
        slug = Path(links[name].rstrip("/")).name
        cells = [
            f'<td><a href="{_esc(links[name])}">{html.escape(name)}</a></td>',
            f'<td>{html.escape(record["Cód. NBR"])}</td>',
            f'<td>{html.escape(record["Cód. WCAG"])}</td>',
        ]
        if filled:
            result = record["Resultado"] or "Sem registro"
            cells += [f'<td>{html.escape(record[c] or "—")}</td>' for c in ("Camada de Teste", "Resultado", "Severidade da Falha", "Observações / Evidências", "Verificado por")]
            data = f' data-result="{_esc(result)}"'
        else:
            options = '<option value="">Não avaliado</option>' + "".join(f'<option>{a}</option>' for a in ANSWERS)
            cells += [
                f'<td>{html.escape(record["Como Testar"])}</td>',
                f'<td><select data-answer="{slug}:resultado" aria-label="Resultado: {_esc(name)}">{options}</select></td>',
                f'<td><textarea data-answer="{slug}:observacoes" rows="2" aria-label="Observações: {_esc(name)}"></textarea></td>',
            ]
            data = f' data-criterion="{_esc(slug)}" data-name="{_esc(name)}" data-nbr="{_esc(record["Cód. NBR"])}" data-wcag="{_esc(record["Cód. WCAG"])}"'
        search = " ".join(record.values())
        body.append(
            f'<tr data-criterion-row data-principle="{_esc(record["Princípio WCAG"])}"{data} data-search="{_esc(search)}">'
            + "".join(cells) + "</tr>"
        )
    head = "".join(f'<th scope="col">{h}</th>' for h in headers)
    label = "Checklist preenchido dos Correios" if filled else "Checklist para preencher"
    return (
        tools
        + f'<div class="table-scroll {"checklist-filled" if filled else "checklist-blank"}" role="region" aria-label="{label}" tabindex="0">'
        + '<table id="checklist-table">'
        + f"<thead><tr>{head}</tr></thead><tbody>{''.join(body)}</tbody></table></div>"
        + '<p class="checklist-empty" data-checklist-empty hidden>Nenhum critério encontrado. Tente outra palavra ou limpe os filtros.</p>'
    )


def on_page_content(content, page, config, files):
    source = page.file.src_uri
    if source == "index.md" and hasattr(page, "toc"):
        page.toc.items[:] = [AnchorLink("Guia de acessibilidade", "portal-title", 1)]
    if source == "index.md":
        team = re.search(r"<table>.*?</table>", content, flags=re.S)
        if team:
            page.meta["portal_team"] = team[0]
    if source == "guia/index.md":
        def topic(match):
            anchor, url, title, description = match.groups()
            return f'<a class="topic-entry" href="{url}" aria-labelledby="{anchor}"><h2 id="{anchor}">{title}</h2><p>{description}</p>{ARROW}</a>'

        content = re.sub(r'<h2 id="([^"]+)"><a href="([^"]+)">(.*?)</a></h2>\s*<p>(.*?)</p>', topic, content, flags=re.S)
    content = content.replace("<aside>", '<section class="reading-note">').replace("</aside>", "</section>")
    if source.startswith("referencia/"):
        content = re.sub(r"<p>(📖 .*?)</p>", r'<p class="source-navigation" hidden>\1</p>', content, count=1, flags=re.S)
    content = re.sub(r"<p>(Owner: [^<]+)</p>", r'<p class="source-byline">\1</p>', content)
    if source.startswith("referencia/criterios/"):
        content = _criterion_details(content)
    if source in CHECKLISTS:
        assert CHECKLIST_SLOT in content, f"{source} precisa do marcador {CHECKLIST_SLOT}"
        content = content.replace(CHECKLIST_SLOT, _checklist(page, config, files), 1)
    if source == "devWeb/non_text_content.md":
        heading = '<h2 id="dispositivo-movel-e-tocavel">'
        content = content.replace(heading, '<span id="TEC14"></span>' + heading, 1)
    if source == "geracaoConteudo/conteudo.md":
        content = content.replace('<p>', '<span id="TEC1"></span><p>', 1)
    return content

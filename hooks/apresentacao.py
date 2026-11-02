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
        ("consulta", "Ferramentas e consulta", ["kit-de-ferramentas", "ferramentas", "glossario-az"]),
    ]
    trail = []
    if source.startswith("referencia/criterios/"):
        trail = [("Correios", "avaliacao-site/"), ("Checklist", "referencia/checklist-unificado/")]
    elif source.startswith("avaliacao-site/") or source in [
        "referencia/auditoria-site-dos-correios.md", "referencia/checklist-unificado.md",
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
    if source == "referencia/checklist-unificado.md":
        page.meta["hide"] = ["toc"]
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


def _checklist(content, config):
    file = Path(config["docs_dir"]) / "referencia/dados/checklist-unificado.csv"
    with file.open(encoding="utf-8-sig", newline="") as stream:
        rows = [r for r in csv.DictReader(stream) if r["Cód. NBR"]]
    principles = sorted({r["Princípio WCAG"] for r in rows})
    options = '<option value="">Todos os princípios</option>' + "".join(
        f'<option value="{html.escape(p, quote=True)}">{html.escape(p)}</option>'
        for p in principles
    )
    controls = f'''<div class="checklist-tools" data-checklist-tools hidden>
      <div class="checklist-tools__fields">
        <label for="criterion-query">Buscar no checklist
          <input type="search" id="criterion-query" placeholder="Critério, código ou palavra-chave" autocomplete="off" aria-controls="checklist-table">
        </label>
        <label for="criterion-principle">Princípio WCAG
          <select id="criterion-principle" aria-controls="checklist-table">{options}</select>
        </label>
        <button type="button" class="filter-reset" data-filter-reset>Limpar filtros</button>
      </div>
      <p class="checklist-count" role="status" aria-live="polite" aria-atomic="true" data-checklist-count>{len(rows)} critérios</p>
    </div>'''
    row_index = 0

    def tag_row(match):
        nonlocal row_index
        record = rows[row_index]
        row_index += 1
        search = " ".join(record.values())
        return (
            '<tr data-criterion-row data-principle="'
            + html.escape(record["Princípio WCAG"], quote=True)
            + '" data-search="' + html.escape(search, quote=True) + '">'
            + match[1] + "</tr>"
        )

    body = re.search(r"<tbody>(.*?)</tbody>", content, re.S)
    if body:
        tagged = re.sub(r"<tr>(.*?)</tr>", tag_row, body[1], flags=re.S)
        assert row_index == len(rows), "O checklist deve corresponder às linhas do CSV."
        content = content[:body.start(1)] + tagged + content[body.end(1):]
    content = content.replace("<table>", controls + '<div class="table-scroll" role="region" aria-label="Checklist de acessibilidade" tabindex="0"><table id="checklist-table">', 1)
    content = content.replace("</table>", '</table></div><p class="checklist-empty" data-checklist-empty hidden>Nenhum critério encontrado. Tente outra palavra ou limpe os filtros.</p>', 1)
    return content


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
    if source == "referencia/checklist-unificado.md":
        content = _checklist(content, config)
    if source == "devWeb/non_text_content.md":
        heading = '<h2 id="dispositivo-movel-e-tocavel">'
        content = content.replace(heading, '<span id="TEC14"></span>' + heading, 1)
    if source == "geracaoConteudo/conteudo.md":
        content = content.replace('<p>', '<span id="TEC1"></span><p>', 1)
    return content

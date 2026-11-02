"""Adapta a apresentação do conteúdo sem modificar os documentos de origem."""

import csv
import html
import re
from pathlib import Path


def on_page_markdown(markdown, page, config, files):
    source = page.file.src_uri
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


def _group_callouts(content):
    blocks = list(re.finditer(r"<aside>.*?</aside>", content, flags=re.S))
    groups = []
    for block in blocks:
        if groups and not content[groups[-1][-1].end():block.start()].strip():
            groups[-1].append(block)
        else:
            groups.append([block])
    for group in reversed(groups):
        if len(group) < 2:
            continue
        start, end = group[0].start(), group[-1].end()
        content = content[:start] + '<div class="callout-grid">' + content[start:end] + "</div>" + content[end:]
    return content


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
    content = _group_callouts(content)
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

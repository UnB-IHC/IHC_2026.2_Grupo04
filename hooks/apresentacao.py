"""Adapta a apresentação do conteúdo sem modificar os documentos de origem."""

import csv
import html
import json
import re
import unicodedata
from collections import Counter
from pathlib import Path
from mkdocs.structure.toc import AnchorLink
from mkdocs.utils import get_relative_url

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
    if source == "guia/heuristicas-nielsen.md":
        markdown = re.sub(
            r'^(\?\?\?\+ note "(10|[1-9])\..*)$',
            r'<span class="heuristic-anchor" id="heuristica-\2"></span>\n\n\1',
            markdown,
            flags=re.M,
        )
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


def _criterion_details(content, result, checklist_url):
    blocks = list(re.finditer(r"<p>([^<\n]+?): (.*?)</p>", content, re.S))
    if not blocks:
        return content
    fields = []
    for block in blocks:
        label, value = block.groups()
        wide = ' class="criterion-details__wide"' if label == "Como Testar" else ""
        if label == "Resultado" and result:
            value = _esc(result["Resultado"] or "Sem registro")
            severity = result["Severidade da Falha"]
            if severity:
                value += f' <span class="audit-severity">{_esc(severity)}</span>'
            value += f'<br><a href="{_esc(checklist_url)}">Ver critério no checklist dos Correios</a>'
        fields.append(f"<div{wide}><dt>{label}:</dt><dd>{value}</dd></div>")
    details = '<dl class="criterion-details">' + "".join(fields) + "</dl>"
    return content[:blocks[0].start()] + details + content[blocks[-1].end():]


CHECKLIST_SLOT = '<div data-checklist-slot></div>'
AUDIT_SUMMARY_SLOT = '<div data-audit-summary=""></div>'
AUDIT_REPORT_SLOT = '<div data-audit-report=""></div>'
CORREIOS_CHECKLIST = "avaliacao-site/checklist-correios.md"
REPORT_FILE = "assets/relatorios/relatorio-acessibilidade-correios-2026-11.pdf"
CHECKLISTS = {
    "guia/checklist-modelo.md": {"csv": "checklist-modelo.csv", "filled": False},
    CORREIOS_CHECKLIST: {"csv": "checklist-unificado.csv", "filled": True},
}
ANSWERS = ["Conforme", "Parcialmente conforme", "Não conforme", "Não se aplica"]


def _esc(value):
    return html.escape(value or "", quote=True)


def _checklist_rows(file):
    with file.open(encoding="utf-8-sig", newline="") as stream:
        return [row for row in csv.DictReader(stream) if row["Cód. NBR"]]


def on_files(files, config):
    checklist = Path(config["docs_dir"]) / "referencia/dados" / CHECKLISTS[CORREIOS_CHECKLIST]["csv"]
    rows = _checklist_rows(checklist)
    counts = Counter(_result_tone(row["Resultado"]) for row in rows)
    config.extra["correios_audit"] = {
        "rows": {row["Critério"]: row for row in rows},
        "total": len(rows),
        "recorded": sum(counts[tone] for tone in RESULT_TONE.values()),
        "counts": counts,
    }


def _audit_summary(audit):
    labels = [("fail", "Não conformes"), ("partial", "Parciais"), ("pass", "Conformes"), ("na", "Não se aplica")]
    counts = audit["counts"]
    if counts["pending"]:
        labels.append(("pending", "Sem resultado"))
    entries = "".join(
        f'<div><dt>{label}</dt><dd>{counts[key]}</dd></div>' for key, label in labels
    )
    return f'<dl class="audit-summary">{entries}</dl>'


def _audit_report(page, files):
    report = files.get_file_from_path(REPORT_FILE)
    if not report:
        return '<p class="audit-report-note">O relatório consolidado está em revisão. As evidências já estão disponíveis no checklist.</p>'
    url = _esc(report.url_relative_to(page.file))
    return f'<p><a class="portal-text-link" href="{url}" download>Baixar relatório técnico (PDF) {ARROW}</a></p>'


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


EVIDENCE_DIR = "avaliacao-site/evidencias/"
ACTORS = {
    "auto": ("🤖", "Script automático", "Código JavaScript executado na própria página. Mede, conta e lê atributos do HTML, sem interpretar o resultado."),
    "agente": ("🧠", "Agente de IA", "Opera o navegador como uma pessoa faria (Tab, Enter, mouse, zoom), captura telas e interpreta o que vê. Nunca resolve CAPTCHA nem digita senhas."),
    "humano": ("🙋", "Pessoa do grupo", "Faz o que exige julgamento ou identidade: resolve CAPTCHA, digita credenciais, ouve áudio, avalia linguagem e qualidade de textos alternativos e confirma vereditos duvidosos."),
}
VERIFIED = [
    ("🤖 Agente", "Veredito tirado só das medições e da interação do agente."),
    ("🤝 Agente + Humano", "O agente coletou a evidência e uma pessoa do grupo testou junto ou decidiu o veredito."),
]
RESULT_TONE = {"❌": "fail", "⚠️": "partial", "✅": "pass", "⚪": "na"}


def _result_tone(result):
    return RESULT_TONE.get(result.split(maxsplit=1)[0], "pending") if result.strip() else "pending"


def _slug(text):
    plain = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", plain.lower()).strip("-")


def _evidence_legend():
    actors = "".join(
        f'<li class="evidence-actor-card evidence-actor-card--{key}"><span class="evidence-actor" aria-hidden="true">{icon}</span>'
        f"<strong>{label}</strong><span>{text}</span></li>"
        for key, (icon, label, text) in ACTORS.items()
    )
    verified = "".join(f"<li><strong>{html.escape(label)}</strong>: {text}</li>" for label, text in VERIFIED)
    return (
        '<section class="evidence-legend" aria-labelledby="como-testamos">'
        '<h2 id="como-testamos">Como os testes foram feitos</h2>'
        "<p>Cada critério foi testado no navegador por até três participantes. Em <strong>Ver evidências</strong> você encontra o passo a passo de cada um, as capturas de tela e as medições que sustentam o resultado.</p>"
        f'<ul class="evidence-actors">{actors}</ul>'
        f'<p class="evidence-legend__label">A coluna <strong>Verificado por</strong> resume quem decidiu o resultado:</p><ul class="evidence-verified">{verified}</ul>'
        "</section>"
    )


def _evidence_dialog(record, evidence, page):
    name = record["Critério"]
    dialog_id = "ev-" + _slug(name)
    tone = next((v for k, v in RESULT_TONE.items() if record["Resultado"].startswith(k)), "na")
    summary = "".join(
        f'<div><dt>{label}</dt><dd{extra}>{html.escape(value or "—")}</dd></div>'
        for label, value, extra in [
            ("Resultado", record["Resultado"], f' class="evidence-result evidence-result--{tone}"'),
            ("Severidade", record["Severidade da Falha"], ""),
            ("Verificado por", record["Verificado por"], ""),
            ("Camada prevista", record["Camada de Teste"], ""),
        ]
    )
    steps = "".join(
        f'<li class="evidence-step evidence-step--{actor}"><span class="evidence-step__who">'
        f'<span class="evidence-actor" aria-hidden="true">{ACTORS[actor][0]}</span>{ACTORS[actor][1]}</span>'
        f"<p>{html.escape(text)}</p></li>"
        for actor, text in evidence["como"]
    )
    findings = []
    for segment in record["Observações / Evidências"].split(" || "):
        match = re.match(r"\[([^\]]+)\]\s*(.*)", segment, re.S)
        where, text = match.groups() if match else ("", segment)
        parts = [p.strip() for p in text.split(" · ") if p.strip()]
        rest = "".join(
            f"<li><strong>{html.escape(label)}:</strong> {html.escape(value)}</li>" if label else f"<li>{html.escape(p)}</li>"
            for p in parts[1:]
            for label, value in [re.match(r"(?:(Onde|Regra|Correção|Sugestão):\s*)?(.*)", p, re.S).groups()]
        )
        findings.append(
            '<article class="evidence-finding">'
            + (f'<p class="evidence-finding__where">{html.escape(where)}</p>' if where else "")
            + f"<p>{html.escape(parts[0] if parts else text)}</p>"
            + (f"<ul>{rest}</ul>" if rest else "")
            + "</article>"
        )
    images = "".join(
        f'<figure class="evidence-shot"><a href="{_esc(get_relative_url(EVIDENCE_DIR + src, page.url))}" target="_blank" rel="noopener">'
        f'<img src="{_esc(get_relative_url(EVIDENCE_DIR + src, page.url))}" alt="" loading="lazy">'
        f'<span class="visually-hidden">Ampliar captura: {html.escape(caption)} (abre em nova aba)</span></a>'
        f"<figcaption>{html.escape(caption)}</figcaption></figure>"
        for src, caption in evidence.get("imagens", [])
    )
    code = "".join(
        f'<figure class="evidence-code"><figcaption>{html.escape(title)}</figcaption><pre><code>{html.escape(text)}</code></pre></figure>'
        for title, text in evidence.get("codigo", [])
    )
    meta = " · ".join(filter(None, [f'NBR {record["Cód. NBR"]}', f'WCAG {record["Cód. WCAG"]}', record["Fluxo Correios (Foco)"]]))
    return f'''<dialog id="{dialog_id}" class="evidence-dialog" aria-labelledby="{dialog_id}-title" closedby="any">
  <div class="evidence-dialog__head">
    <div><p class="evidence-dialog__meta">{html.escape(meta)}</p><h2 id="{dialog_id}-title">{html.escape(name)}</h2></div>
    <form method="dialog"><button class="evidence-close">Fechar<span class="visually-hidden"> evidências</span></button></form>
  </div>
  <div class="evidence-dialog__body">
    <dl class="evidence-summary">{summary}</dl>
    <section><h3>Como foi testado</h3><ol class="evidence-steps">{steps}</ol></section>
    <section><h3>Resultado</h3>{"".join(findings)}</section>
    {f'<section><h3>Capturas de tela</h3><div class="evidence-gallery">{images}</div></section>' if images else ""}
    {f'<section><h3>Código e medições</h3>{code}</section>' if code else ""}
  </div>
</dialog>'''


def _checklist(page, config, files):
    settings = CHECKLISTS[page.file.src_uri]
    filled = settings["filled"]
    file = Path(config["docs_dir"]) / "referencia/dados" / settings["csv"]
    rows = _checklist_rows(file)
    links = _criterion_links(page, files)
    missing = [r["Critério"] for r in rows if r["Critério"] not in links]
    assert not missing, f"Critérios sem ficha correspondente: {missing}"

    filters = _filter_select("principle", "Princípio WCAG", sorted({r["Princípio WCAG"] for r in rows}), "Todos" if filled else "Todos os princípios")
    if filled:
        filters += _filter_select("result", "Resultado", sorted({r["Resultado"] or "Sem registro" for r in rows}), "Todos")
    display_toggle = (
        '<button type="button" class="checklist-view" data-checklist-view aria-pressed="false" '
        'aria-controls="checklist-table">Mostrar colunas técnicas</button>'
        if filled else ""
    )
    tools = f'''<div class="checklist-tools" data-checklist-tools hidden>
      <div class="checklist-tools__fields">
        <label for="criterion-query">Buscar no checklist
          <input type="search" id="criterion-query" placeholder="Critério, código ou palavra-chave" autocomplete="off" aria-controls="checklist-table">
        </label>
        {filters}
        <button type="button" class="filter-reset" data-filter-reset>Limpar filtros</button>
      </div>
      <div class="checklist-tools__footer">
        <p class="checklist-count" role="status" aria-live="polite" aria-atomic="true" data-checklist-count>{len(rows)} critérios</p>
        {display_toggle}
      </div>
    </div>'''

    dialogs = []
    if filled:
        evidences = json.loads((file.parent / "evidencias-correios.json").read_text(encoding="utf-8"))
        missing = [r["Critério"] for r in rows if r["Critério"] not in evidences]
        assert not missing, f"Critérios sem evidência: {missing}"
        shots = [src for e in evidences.values() if isinstance(e, dict) for src, _ in e.get("imagens", [])]
        absent = [s for s in shots if not (Path(config["docs_dir"]) / EVIDENCE_DIR / s).is_file()]
        assert not absent, f"Capturas inexistentes: {absent}"
        headers = ["Critério", "Resultado", "Evidências", "Cód. NBR", "Cód. WCAG", "Camada de teste", "Severidade", "Verificado por"]
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
        cells = [f'<th scope="row"><a href="{_esc(links[name])}">{html.escape(name)}</a></th>'] if filled else [
            f'<td><a href="{_esc(links[name])}">{html.escape(name)}</a></td>',
            f'<td>{html.escape(record["Cód. NBR"])}</td>',
            f'<td>{html.escape(record["Cód. WCAG"])}</td>',
        ]
        if filled:
            result = record["Resultado"] or "Sem registro"
            slug = _slug(name)
            dialog_id = "ev-" + slug
            tone = _result_tone(result)
            severity = record["Severidade da Falha"]
            compact_severity = f'<span class="checklist-compact-severity">{_esc(severity)}</span>' if severity else ""
            label = result.split(maxsplit=1)[-1] if tone != "pending" else result
            cells += [
                f'<td class="checklist-verdict"><span class="checklist-result" data-tone="{tone}">{_esc(label)}</span>{compact_severity}</td>',
                f'<td><button type="button" class="evidence-open" commandfor="{dialog_id}" command="show-modal" aria-haspopup="dialog">'
                f'Ver evidências<span class="visually-hidden">: {html.escape(name)}</span></button></td>',
            ]
            cells += [
                f'<td class="checklist-technical">{_esc(record[key] or "—")}</td>'
                for key in ("Cód. NBR", "Cód. WCAG", "Camada de Teste", "Severidade da Falha", "Verificado por")
            ]
            dialogs.append(_evidence_dialog(record, evidences[name], page))
            data = f' id="criterio-{slug}" data-result="{_esc(result)}"'
        else:
            slug = Path(links[name].rstrip("/")).name
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
    head = "".join(
        f'<th scope="col" class="checklist-technical">{header}</th>'
        if filled and index >= 3 else f'<th scope="col">{header}</th>'
        for index, header in enumerate(headers)
    )
    label = "Checklist preenchido dos Correios" if filled else "Checklist para preencher"
    compact = ' data-compact="true"' if filled else ""
    return (
        tools
        + f'<div class="table-scroll {"checklist-filled" if filled else "checklist-blank"}"{compact} role="region" aria-label="{label}" tabindex="0">'
        + '<table id="checklist-table">'
        + f"<thead><tr>{head}</tr></thead><tbody>{''.join(body)}</tbody></table></div>"
        + '<p class="checklist-empty" data-checklist-empty hidden>Nenhum critério encontrado. Tente outra palavra ou limpe os filtros.</p>'
        + "".join(dialogs)
        + (_evidence_legend() if filled else "")
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
    audit = config.extra["correios_audit"]
    if AUDIT_SUMMARY_SLOT in content:
        content = content.replace(AUDIT_SUMMARY_SLOT, _audit_summary(audit), 1)
    if AUDIT_REPORT_SLOT in content:
        content = content.replace(AUDIT_REPORT_SLOT, _audit_report(page, files), 1)
    if source.startswith("referencia/criterios/"):
        title = html.unescape(page.title)
        checklist = files.get_file_from_path(CORREIOS_CHECKLIST).url_relative_to(page.file)
        content = _criterion_details(content, audit["rows"].get(title), f"{checklist}#criterio-{_slug(title)}")
    if source in CHECKLISTS:
        assert CHECKLIST_SLOT in content, f"{source} precisa do marcador {CHECKLIST_SLOT}"
        content = content.replace(CHECKLIST_SLOT, _checklist(page, config, files), 1)
    if source == "devWeb/non_text_content.md":
        heading = '<h2 id="dispositivo-movel-e-tocavel">'
        content = content.replace(heading, '<span id="TEC14"></span>' + heading, 1)
    if source == "geracaoConteudo/conteudo.md":
        content = content.replace('<p>', '<span id="TEC1"></span><p>', 1)
    return content

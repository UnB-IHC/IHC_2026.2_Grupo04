(() => {
  "use strict";

  const normalize = (text) => text.normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLowerCase();

  function preparePage() {
    function enhanceToggle(id, openingLabel, closingLabel) {
      const toggle = document.getElementById(id);
      const control = document.querySelector(`.md-header__button[for="${id}"]`);
      if (!toggle || !control || control.dataset.ready) return;
      control.dataset.ready = "true";
      control.setAttribute("role", "button");
      control.setAttribute("tabindex", "0");
      const update = () => {
        control.setAttribute("aria-expanded", String(toggle.checked));
        control.setAttribute("aria-label", toggle.checked ? closingLabel : openingLabel);
      };
      control.addEventListener("keydown", (event) => {
        if (event.key !== "Enter" && event.key !== " ") return;
        event.preventDefault();
        event.stopPropagation();
        toggle.checked = !toggle.checked;
        toggle.dispatchEvent(new Event("change", { bubbles: true }));
        if (id === "__search" && toggle.checked) {
          const drawer = document.getElementById("__drawer");
          if (drawer?.checked) {
            drawer.checked = false;
            drawer.dispatchEvent(new Event("change", { bubbles: true }));
          }
          document.querySelector(".md-search__input")?.focus();
        }
      });
      toggle.addEventListener("change", update);
      update();
    }
    enhanceToggle("__drawer", "Abrir menu de navegação", "Fechar menu de navegação");
    enhanceToggle("__search", "Abrir busca do site", "Fechar busca do site");
    if (!document.documentElement.dataset.portalKeys) {
      document.documentElement.dataset.portalKeys = "true";
      document.addEventListener("keydown", (event) => {
        if (event.key !== "Escape") return;
        for (const id of ["__search", "__drawer"]) {
          const toggle = document.getElementById(id);
          if (!toggle?.checked) continue;
          toggle.checked = false;
          toggle.dispatchEvent(new Event("change", { bubbles: true }));
          document.querySelector(`.md-header__button[for="${id}"]`)?.focus();
        }
      });
    }
    const skip = document.querySelector(".md-skip");
    if (skip && document.querySelector("#portal-title")) skip.href = "#portal-title";

    document.querySelectorAll(".md-typeset table").forEach((table) => {
      if (table.closest(".table-scroll, .md-typeset__scrollwrap")) return;
      const region = document.createElement("div");
      region.className = "table-scroll";
      region.setAttribute("role", "region");
      region.setAttribute("aria-label", "Tabela de " + (document.querySelector("article h1")?.textContent || "conteúdo"));
      region.tabIndex = 0;
      table.before(region);
      region.append(table);
    });

    prepareAnswers();

    const tools = document.querySelector("[data-checklist-tools]");
    if (!tools || tools.dataset.ready) return;
    const query = tools.querySelector("input[type=search]");
    const filters = [...tools.querySelectorAll("select[data-filter]")];
    const reset = tools.querySelector("[data-filter-reset]");
    const count = tools.querySelector("[data-checklist-count]");
    const empty = document.querySelector("[data-checklist-empty]");
    const rows = [...document.querySelectorAll("[data-criterion-row]")];
    const searchable = rows.map((row) => normalize(row.dataset.search));

    function filter() {
      const terms = normalize(query.value.trim()).split(/\s+/).filter(Boolean);
      let visible = 0;
      rows.forEach((row, index) => {
        const matches = filters.every((select) => !select.value || row.dataset[select.dataset.filter] === select.value)
          && terms.every((term) => searchable[index].includes(term));
        row.hidden = !matches;
        if (matches) visible += 1;
      });
      count.textContent = visible === rows.length ? `${visible} critérios` : `${visible} de ${rows.length} critérios`;
      empty.hidden = visible !== 0;
      reset.disabled = !query.value && filters.every((select) => !select.value);
    }

    query.addEventListener("input", filter);
    filters.forEach((select) => select.addEventListener("change", filter));
    reset.addEventListener("click", () => {
      query.value = "";
      filters.forEach((select) => { select.value = ""; });
      filter();
      query.focus();
    });
    tools.dataset.ready = "true";
    tools.hidden = false;
    filter();
  }

  // Checklist em branco: respostas salvas só no navegador (localStorage) e exportáveis em CSV.
  function prepareAnswers() {
    const panel = document.querySelector("[data-checklist-answers]");
    if (!panel || panel.dataset.ready) return;
    const storageKey = "ihc-g04:checklist-modelo";
    const fields = [...document.querySelectorAll("[data-answer]")];
    const rows = [...document.querySelectorAll("[data-criterion-row][data-criterion]")];
    const progress = panel.querySelector("[data-checklist-progress]");
    let saved = {};
    try { saved = JSON.parse(localStorage.getItem(storageKey)) || {}; } catch { saved = {}; }

    const answer = (key) => document.querySelector(`[data-answer="${key}"]`)?.value || "";
    function update() {
      const done = rows.filter((row) => answer(`${row.dataset.criterion}:resultado`)).length;
      progress.textContent = `${done} de ${rows.length} critérios avaliados`;
    }
    function store() {
      saved = Object.fromEntries(fields.filter((field) => field.value).map((field) => [field.dataset.answer, field.value]));
      try { localStorage.setItem(storageKey, JSON.stringify(saved)); } catch { /* armazenamento indisponível */ }
    }

    fields.forEach((field) => {
      if (saved[field.dataset.answer]) field.value = saved[field.dataset.answer];
      field.addEventListener(field.tagName === "SELECT" ? "change" : "input", () => {
        store();
        update();
      });
    });

    panel.querySelector("[data-checklist-export]").addEventListener("click", () => {
      const cell = (value) => `"${String(value).replace(/"/g, '""')}"`;
      const site = answer("site");
      const lines = [["Critério", "Cód. NBR", "Cód. WCAG", "Resultado", "Observações / Evidências", "URL Testada"]];
      rows.forEach((row) => lines.push([
        row.dataset.name, row.dataset.nbr, row.dataset.wcag,
        answer(`${row.dataset.criterion}:resultado`) || "Não avaliado",
        answer(`${row.dataset.criterion}:observacoes`), site,
      ]));
      const blob = new Blob(["\ufeff" + lines.map((line) => line.map(cell).join(",")).join("\r\n")], { type: "text/csv;charset=utf-8" });
      const link = document.createElement("a");
      link.href = URL.createObjectURL(blob);
      link.download = "checklist-acessibilidade.csv";
      document.body.append(link);
      link.click();
      link.remove();
      setTimeout(() => URL.revokeObjectURL(link.href), 0);
    });

    panel.querySelector("[data-checklist-clear]").addEventListener("click", () => {
      if (!window.confirm("Apagar todas as respostas salvas neste navegador?")) return;
      fields.forEach((field) => { field.value = ""; });
      store();
      update();
      panel.querySelector("#checklist-site")?.focus();
    });

    panel.dataset.ready = "true";
    panel.hidden = false;
    update();
  }

  // Modais de evidência: <button commandfor> e <dialog closedby="any"> já funcionam sem JS nos navegadores atuais.
  // Este trecho só cobre navegadores sem esses recursos.
  if (!("commandForElement" in HTMLButtonElement.prototype)) {
    document.addEventListener("click", (event) => {
      const opener = event.target.closest("button[commandfor][command=show-modal]");
      document.getElementById(opener?.getAttribute("commandfor"))?.showModal();
    });
  }
  if (!("closedBy" in HTMLDialogElement.prototype)) {
    document.addEventListener("click", (event) => {
      if (event.target.matches?.("dialog.evidence-dialog[open]")) event.target.close();
    });
  }

  if (typeof document$ !== "undefined") document$.subscribe(preparePage);
  else if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", preparePage, { once: true });
  else preparePage();
})();

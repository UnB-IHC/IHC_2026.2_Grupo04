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

    const tools = document.querySelector("[data-checklist-tools]");
    if (!tools || tools.dataset.ready) return;
    const query = tools.querySelector("input[type=search]");
    const principle = tools.querySelector("select");
    const reset = tools.querySelector("[data-filter-reset]");
    const count = tools.querySelector("[data-checklist-count]");
    const empty = document.querySelector("[data-checklist-empty]");
    const rows = [...document.querySelectorAll("[data-criterion-row]")];
    const searchable = rows.map((row) => normalize(row.dataset.search));

    function filter() {
      const terms = normalize(query.value.trim()).split(/\s+/).filter(Boolean);
      let visible = 0;
      rows.forEach((row, index) => {
        const matches = (!principle.value || row.dataset.principle === principle.value)
          && terms.every((term) => searchable[index].includes(term));
        row.hidden = !matches;
        if (matches) visible += 1;
      });
      count.textContent = visible === rows.length ? `${visible} critérios` : `${visible} de ${rows.length} critérios`;
      empty.hidden = visible !== 0;
      reset.disabled = !query.value && !principle.value;
    }

    query.addEventListener("input", filter);
    principle.addEventListener("change", filter);
    reset.addEventListener("click", () => {
      query.value = "";
      principle.value = "";
      filter();
      query.focus();
    });
    tools.dataset.ready = "true";
    tools.hidden = false;
    filter();
  }

  if (typeof document$ !== "undefined") document$.subscribe(preparePage);
  else if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", preparePage, { once: true });
  else preparePage();
})();

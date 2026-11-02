# WCAG

Owner: osakareaper

<aside markdown="1">
🌍

A **WCAG 2.2** (*Web Content Accessibility Guidelines*) é a recomendação oficial do **W3C**, publicada pela **WAI** (*Web Accessibility Initiative*), que define como tornar conteúdos web acessíveis a pessoas com deficiência. Ela é a **base técnica direta da** [NBR/ABNT](nbr-abnt.md): os requisitos da norma brasileira correspondem aos critérios de sucesso da WCAG 2.2.

</aside>

# 🧭 Os 4 Princípios Fundamentais (POUR)

Resumo para memorizar em [Princípios POUR](principios-pour.md).

<aside markdown="1">
👁️

**1. Perceptível (*Perceivable*)**

A informação e os componentes da interface devem ser apresentados aos usuários de formas que eles possam perceber.

- [Texto Alternativo](texto-alternativo.md)
- Legendas e audiodescrição
- [Contraste de Cores](contraste-de-cores.md)
- [Refluxo e Zoom](refluxo-e-zoom.md)
</aside>

<aside markdown="1">
⌨️

**2. Operável (*Operable*)**

Os componentes de interface e a navegação devem ser operáveis por todos.

- [Foco do Teclado](foco-do-teclado.md)
- Tempo suficiente
- Sem convulsões/flashes
- Navegável ([Landmarks](landmarks.md))
- Modalidades de entrada
</aside>

<aside markdown="1">
🧠

**3. Compreensível (*Understandable*)**

A informação e a operação da interface devem ser compreensíveis.

- [Linguagem Simples](linguagem-simples.md)
- Interface previsível
- Assistência na entrada de dados
- Prevenção de erros
</aside>

<aside markdown="1">
⚙️

**4. Robusto (*Robust*)**

O conteúdo deve ser robusto o suficiente para ser interpretado de forma confiável por uma ampla variedade de agentes de usuário, incluindo tecnologias assistivas.

- [Semântica HTML](semantica-html.md)
- [Nome Acessível](nome-acessivel.md)
- Mensagens de status ([ARIA](aria.md))
</aside>

# 🎚️ Níveis de Conformidade

Equivalência completa com a NBR em [Níveis de Conformidade](niveis-de-conformidade.md).

<aside markdown="1">
🔴

**Nível A — Básico / Crítico**

Remove as barreiras mais graves, que impedem totalmente o acesso.

</aside>

<aside markdown="1">
🟠

**Nível AA — Padrão Global**

Padrão exigido internacionalmente e base dos **Requisitos** da NBR 17225 (Conformidade Regular).

</aside>

<aside markdown="1">
🔵

**Nível AAA — Excelência**

Nível máximo de acessibilidade especializada. Corresponde às **Recomendações** da NBR 17225.

</aside>

# 🌉 Ponte WCAG 2.2 ↔ ABNT NBR 17225

Enquanto a **WCAG** agrupa os critérios nos **4 princípios abstratos (POUR)**, a **ABNT NBR 17225** reorganiza exatamente os mesmos critérios em **16 seções de componentes reais de interface** (Teclado, Imagens, Cabeçalhos, Formulários, Cores etc.). Na prática, a WCAG responde "*qual princípio está sendo violado?*" e a NBR responde "*em qual componente da tela está o problema?*".

| Aspecto | WCAG 2.2 (W3C) | ABNT NBR 17225 |
| --- | --- | --- |
| Organização | 4 princípios (POUR) → diretrizes → critérios de sucesso | 16 seções temáticas por componente de interface |
| Níveis | A, AA e AAA | Requisitos (A + AA) e Recomendações (AAA) |
| Exemplo | 2.4.7 Foco Visível (Operável, AA) | 5.1.1 Indicador de foco visível (Teclado, Requisito) |
| Exemplo | 1.1.1 Conteúdo Não Textual (Perceptível, A) | 5.2.1 a 5.2.3 Texto alternativo (Imagens, Requisito) |
| Exemplo | 4.1.3 Mensagens de Status (Robusto, AA) | 5.13.11 Mensagens de status (Semântica, Requisito) |

<aside markdown="1">
✅

O checklist unificado com o mapeamento completo NBR ↔ WCAG de cada critério está na página [Auditoria: Site dos Correios](auditoria-site-dos-correios.md).

</aside>

# 🔗 Links Oficiais

- [W3C — WCAG 2.2 (Recomendação Oficial)](https://www.w3.org/TR/WCAG22/)
- [WebAIM — WCAG 2 Checklist](https://webaim.org/standards/wcag/checklist)
- [The A11Y Project — Checklist](https://www.a11yproject.com/checklist/)

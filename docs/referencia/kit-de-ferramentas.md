# Kit de Ferramentas

Owner: osakareaper

📖 [Guia de Acessibilidade](index.md) › 🛠️ Prática

<aside markdown="1">
💬

**Em uma frase:** as ferramentas que usamos para auditar. Automáticas acham cerca de 1/3 dos problemas — o resto exige teste manual (ver [Human-in-the-Loop](human-in-the-loop.md)).

</aside>

Automáticas

| Ferramenta | O que faz | Melhor para |
| --- | --- | --- |
| [axe DevTools](https://www.deque.com/axe/devtools/) | Extensão que varre a página e lista falhas com o trecho de código | Relatório técnico para devs |
| [WAVE](https://wave.webaim.org/) | Desenha ícones de erro e alerta direto sobre a página | Visualizar problemas no layout |
| Lighthouse | Já vem no Chrome (DevTools › Lighthouse) e dá uma nota de 0 a 100 | Visão geral rápida |
| Accessibility Insights | Extensão da Microsoft com testes guiados passo a passo | Roteiro manual assistido |

Teclado

Deixe o mouse de lado e use só o teclado. Detalhes em [Foco do Teclado](foco-do-teclado.md).

| Tecla | Ação |
| --- | --- |
| Tab / Shift + Tab | Avançar / voltar |
| Enter / Espaço | Acionar |
| Setas | Menus e opções |
| Esc | Fechar |

Leitor de Tela

| Leitor | Sistema | Como ligar |
| --- | --- | --- |
| [NVDA](https://www.nvaccess.org/) | Windows (gratuito) | Ctrl + Alt + N |
| VoiceOver | macOS | Cmd + F5 |
| TalkBack | Android | Configurações › Acessibilidade |

Atalhos e o que ouvir em [Leitor de Tela](leitor-de-tela.md).

Zoom e Contraste

- **Zoom 200% e 400%:** Ctrl/Cmd + até chegar lá → [Refluxo e Zoom](refluxo-e-zoom.md).
- **Colour Contrast Analyser (CCA):** app gratuito com conta-gotas que calcula a razão → [Contraste de Cores](contraste-de-cores.md).
- **Conta-gotas do DevTools:** mostra o contraste ao inspecionar uma cor de texto.
- **Bookmarklet Text Spacing:** força espaçamentos para testar se o texto corta.

Estrutura

- **HeadingsMap:** mostra a árvore de títulos h1–h6 → [Semântica HTML](semantica-html.md).
- **Landmarks:** lista e navega pelas regiões → [Landmarks](landmarks.md).
- **Painel Accessibility do DevTools:** mostra [Nome Acessível](nome-acessivel.md) e a [Árvore de Acessibilidade](arvore-de-acessibilidade.md).


---

🔗 **Relacionados:** [Auditoria: Site dos Correios](auditoria-site-dos-correios.md) · [Human-in-the-Loop](human-in-the-loop.md) · [Leitor de Tela](leitor-de-tela.md)

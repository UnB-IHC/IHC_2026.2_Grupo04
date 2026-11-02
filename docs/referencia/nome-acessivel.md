# Nome Acessível

Owner: osakareaper

📖 [Guia de Acessibilidade](index.md) › 💡 Conceitos › Código e Semântica

<aside markdown="1">
💬

**Em uma frase:** o texto que a [Tecnologia Assistiva](tecnologia-assistiva.md) anuncia para um botão, link ou campo. Sem ele, o elemento vira um "botão" mudo.

</aside>

## ✅ ❌ Na prática

<aside markdown="1">
✅

`<button aria-label="Fechar janela">✕</button>`

🔊 *"Fechar janela, botão"*

</aside>

<aside markdown="1">
❌

`<button>✕</button>`

🔊 *"vezes, botão"* ou só *"botão"*

</aside>

## 🔢 De onde o nome vem (por prioridade)

1. `aria-labelledby` — aponta para outro texto da página.
2. `aria-label` — texto definido direto no elemento (ver [ARIA](aria.md)).
3. Conteúdo nativo — texto do botão/link, `label` do campo ou `alt` da imagem (ver [Texto Alternativo](texto-alternativo.md)).
4. `title` — último recurso, evite depender dele.

## 📦 Onde costuma falhar nos Correios

Lupa de busca · setas e bolinhas do carrossel · botão de áudio do [CAPTCHA](captcha.md) · menu mobile.

## 🧪 Como testar

- Chrome DevTools › Elements › painel **Accessibility** › campo *Name*.
- Ouvir com o [Leitor de Tela](leitor-de-tela.md).
- Script pronto na [Skill: Auditar acessibilidade com agente + humano (NBR 17225 / WCAG 2.2)](procedimento-de-auditoria.md).

## 📏 Na norma

| NBR 17225 | WCAG 2.2 |
| --- | --- |
| 5.8.3 Botões · 5.2.2 Imagens funcionais · 5.9.1 Rótulos | 4.1.2 Nome, Função, Valor · 1.1.1 · 3.3.2 |

---

🔗 **Relacionados:** [ARIA](aria.md) · [Árvore de Acessibilidade](arvore-de-acessibilidade.md) · [Texto Alternativo](texto-alternativo.md) · [Leitor de Tela](leitor-de-tela.md)

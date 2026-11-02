# Foco do Teclado

Owner: osakareaper

📖 [Guia de Acessibilidade](index.md) › 💡 Conceitos › Interface

<aside markdown="1">
💬

**Em uma frase:** o indicador visual (geralmente um contorno) que mostra em qual elemento a pessoa está ao navegar pelo teclado.

</aside>

## ⌨️ As teclas da auditoria

| Tecla | Ação |
| --- | --- |
| **Tab** / **Shift + Tab** | Avança / volta entre elementos |
| **Enter** | Aciona links e botões |
| **Espaço** | Aciona botões, marca caixas |
| **Setas** | Navega em menus, abas e opções |
| **Esc** | Fecha menus e modais |

## 📐 As 4 regras do foco

<aside markdown="1">
👁️

**Visível**

Sempre dá pra ver onde está.

NBR 5.1.1 · WCAG 2.4.7

</aside>

<aside markdown="1">
🙈

**Não escondido**

Banner de cookies ou header fixo não cobre.

NBR 5.1.3 · WCAG 2.4.11

</aside>

<aside markdown="1">
🔢

**Em ordem**

Segue a leitura visual.

NBR 5.1.4 · WCAG 2.4.3

</aside>

<aside markdown="1">
🪤

**Sem armadilha**

Sempre dá pra sair.

NBR 5.1.12 · WCAG 2.1.2

</aside>

## ✅ ❌ Na prática

<aside markdown="1">
✅

`:focus-visible { outline: 3px solid #0B5FFF; }`

Contorno forte, com [Contraste de Cores](contraste-de-cores.md) de 3:1 contra o fundo.

</aside>

<aside markdown="1">
❌

`*:focus { outline: none; }`

Remove o foco de tudo: quem usa teclado fica perdido.

</aside>

---

🔗 **Relacionados:** [Contraste de Cores](contraste-de-cores.md) · [Landmarks](landmarks.md) · [Semântica HTML](semantica-html.md) · [Kit de Ferramentas](kit-de-ferramentas.md)

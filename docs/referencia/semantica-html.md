# Semântica HTML

Owner: osakareaper

📖 [Guia de Acessibilidade](index.md) › 💡 Conceitos › Código e Semântica

<aside markdown="1">
💬

**Em uma frase:** usar a tag HTML certa para cada coisa, de modo que a estrutura seja **"determinada programaticamente"** — compreendida por software, não apenas vista na tela.

</aside>

## ✅ ❌ Na prática

<aside markdown="1">
✅

**Certo**

`<button>Buscar</button>`

Recebe foco, funciona com Enter/Espaço e é anunciado como botão.

</aside>

<aside markdown="1">
❌

**Errado**

`<div onclick="buscar()">Buscar</div>`

Não recebe foco, não funciona no teclado e o [Leitor de Tela](leitor-de-tela.md) não sabe que é um botão.

</aside>

## 🧱 Qual tag usar

| O que aparece na tela | Tag correta |
| --- | --- |
| Título de seção | `h1` a `h6`, sem pular níveis |
| Lista de itens | `ul`, `ol` ou `dl` |
| Ação (enviar, abrir, fechar) | `button` |
| Navegação para outra página | `a href` |
| Tabela de dados | `table`  • `th scope` |
| Campo de formulário | `input`  • `label` |
| Regiões da página | `header`, `nav`, `main`, `footer` → [Landmarks](landmarks.md) |

<aside markdown="1">
🥇

**Regra de ouro:** primeiro HTML nativo. Só use [ARIA](aria.md) quando não existir uma tag que resolva.

</aside>

## 📏 Na norma

| NBR 17225 | WCAG 2.2 |
| --- | --- |
| 5.3 Cabeçalhos · 5.5 Listas · 5.6 Tabelas · 5.7 Links · 5.8 Botões · 5.13 Semântica | 1.3.1 Informações e Relações · 4.1.2 Nome, Função, Valor |

---

🔗 **Relacionados:** [ARIA](aria.md) · [Árvore de Acessibilidade](arvore-de-acessibilidade.md) · [Nome Acessível](nome-acessivel.md) · [Landmarks](landmarks.md)

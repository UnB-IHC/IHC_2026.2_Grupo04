# ARIA

Owner: osakareaper

📖 [Guia de Acessibilidade](index.md) › 💡 Conceitos › Código e Semântica

<aside markdown="1">
💬

**Em uma frase:** WAI-ARIA é um conjunto de atributos que acrescenta função, nome e estado aos elementos quando o HTML nativo não é suficiente.

</aside>

<aside markdown="1">
⚠️

**Regra nº 1 do ARIA:** se existe uma tag HTML nativa que faz o trabalho, use a tag. ARIA errado é pior do que nenhum ARIA. Veja [Semântica HTML](semantica-html.md).

</aside>

## 🧩 Atributos mais usados

| Atributo | Para que serve | Exemplo de uso |
| --- | --- | --- |
| `aria-label` | Dá um [Nome Acessível](nome-acessivel.md) | Botão só com ícone |
| `aria-describedby` | Liga um texto de ajuda ou erro ao campo | Mensagem "CEP inválido" |
| `aria-expanded` | Informa se algo está aberto ou fechado | Mega menu |
| `aria-hidden="true"` | Esconde da TA | Ícone decorativo |
| `aria-live` / `role="status"` | Anuncia mudanças sem mover o foco | "Nenhum CEP encontrado" |
| `role` | Define a função | `role="dialog"` em modais |

## ✅ ❌ Na prática

<aside markdown="1">
✅

`<button aria-expanded="false">Menu</button>`

Botão nativo + estado informado.

</aside>

<aside markdown="1">
❌

`<div role="button">Menu</div>`

Sem `tabindex` nem tratamento de teclado: parece botão, mas não funciona como um.

</aside>

## 📏 Na norma

| NBR 17225 | WCAG 2.2 |
| --- | --- |
| 5.8.3 Botões · 5.13.11 Mensagens de status | 4.1.2 Nome, Função, Valor · 4.1.3 Mensagens de Status |

---

🔗 **Relacionados:** [Semântica HTML](semantica-html.md) · [Nome Acessível](nome-acessivel.md) · [Árvore de Acessibilidade](arvore-de-acessibilidade.md)

# Contraste de Cores

Owner: osakareaper

📖 [Guia de Acessibilidade](index.md) › 💡 Conceitos › Interface

<aside markdown="1">
💬

**Em uma frase:** a diferença de luminosidade entre um texto (ou ícone) e o fundo, medida como uma razão que vai de **1:1** (invisível) a **21:1** (preto no branco).

</aside>

## 📏 Os mínimos

| O quê | Mínimo | Nível | NBR 17225 · WCAG |
| --- | --- | --- | --- |
| Texto normal | **4,5:1** | AA | 5.11.3 · 1.4.3 |
| Texto grande (≥ 18pt ou ≥ 14pt negrito) | **3:1** | AA | 5.11.3 · 1.4.3 |
| Bordas de campos, ícones, contorno de [Foco do Teclado](foco-do-teclado.md) | **3:1** | AA | 5.11.4 · 1.4.11 |
| Texto normal (excelência) | **7:1** | AAA | Recomendação · 1.4.6 |

## 🎨 Cor nunca sozinha

<aside markdown="1">
✅

Campo com erro: borda vermelha **+** ícone ⚠️ **+** texto "CEP inválido".

</aside>

<aside markdown="1">
❌

Campo com erro: só a borda fica vermelha. Quem não distingue vermelho não percebe.

</aside>

<aside markdown="1">
📦

**Nos Correios:** o amarelo da marca é claro. Texto branco sobre amarelo tende a reprovar; texto escuro sobre amarelo tende a passar. **Meça sempre** — o olho engana.

</aside>

## 🧪 Como testar

Colour Contrast Analyser, conta-gotas do Chrome DevTools ou axe DevTools (ver [Kit de Ferramentas](kit-de-ferramentas.md)).

---

🔗 **Relacionados:** [Foco do Teclado](foco-do-teclado.md) · [Necessidades de Acessibilidade](necessidades-de-acessibilidade.md) · [Kit de Ferramentas](kit-de-ferramentas.md)

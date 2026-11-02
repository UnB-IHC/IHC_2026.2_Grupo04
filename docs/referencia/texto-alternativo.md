# Texto Alternativo

Owner: osakareaper

📖 [Guia de Acessibilidade](index.md) › 💡 Conceitos › Interface

<aside markdown="1">
💬

**Em uma frase:** a descrição em texto de uma imagem (atributo `alt`), lida pelo [Leitor de Tela](leitor-de-tela.md) no lugar dela.

</aside>

## 🌳 Que alt escrever?

| Tipo de imagem | O que fazer | Exemplo |
| --- | --- | --- |
| 📷 **Informativa** | Descrever o conteúdo relevante | `alt="Carteiro entregando encomenda"` |
| 🔘 **Funcional** (link/botão) | Descrever a ação ou destino | `alt="Página inicial dos Correios"` |
| ✨ **Decorativa** | Deixar vazio | `alt=""` |
| 📢 **Com texto** (banner) | Repetir o texto — ou melhor, usar HTML | `alt="Frete grátis até sexta"` |
| 📊 **Complexa** (gráfico) | Resumo curto + descrição longa na página | `alt="Entregas cresceram 12% em 2025"` |

## ✅ ❌ Na prática

<aside markdown="1">
✅

`<img src="lupa.svg" alt="Buscar">`

</aside>

<aside markdown="1">
❌

`<img src="lupa.svg" alt="lupa.png">` ou `alt="imagem"`

</aside>

<aside markdown="1">
🙋

**Camada humana:** ferramentas detectam *se* existe alt, mas só uma pessoa julga *se ele faz sentido*. Por isso é um item de [Human-in-the-Loop](human-in-the-loop.md).

</aside>

## 📏 Na norma

| NBR 17225 | WCAG 2.2 |
| --- | --- |
| 5.2.1 Conteúdo · 5.2.2 Funcionais · 5.2.3 Decorativas · 5.2.5 Imagens de texto | 1.1.1 Conteúdo Não Textual · 1.4.5 Imagens de Texto |

---

🔗 **Relacionados:** [Nome Acessível](nome-acessivel.md) · [Leitor de Tela](leitor-de-tela.md) · [Human-in-the-Loop](human-in-the-loop.md)

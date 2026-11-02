# Landmarks

Owner: osakareaper

📖 [Guia de Acessibilidade](index.md) › 💡 Conceitos › Código e Semântica

<aside markdown="1">
💬

**Em uma frase:** regiões da página (cabeçalho, navegação, conteúdo principal, rodapé) marcadas no código para que quem usa [Leitor de Tela](leitor-de-tela.md) pule direto para elas.

</aside>

## 🗺️ O mapa da página

| `header` — banner |
| --- |
| `nav` — navegação (menu principal) |
| `main` — conteúdo principal (um por página) |
| `aside` — conteúdo complementar |
| `footer` — rodapé (contentinfo) |

<aside markdown="1">
💡

**Duas `nav` na página?** Diferencie com `aria-label` — por exemplo "Menu principal" e "Links do rodapé".

</aside>

## ⏭️ Parente próximo: link de salto

O link *"Pular para o conteúdo principal"* (primeiro Tab da página) leva o [Foco do Teclado](foco-do-teclado.md) direto ao `main`.

## 🧪 Como testar

- No NVDA, tecla **D** pula de região em região.
- WAVE mostra os landmarks como ícones na página (ver [Kit de Ferramentas](kit-de-ferramentas.md)).

## 📏 Na norma

| NBR 17225 | WCAG 2.2 |
| --- | --- |
| 5.4.1 Regiões · 5.4.5 Regiões únicas · 5.7.12 Link de salto | 1.3.1 · 2.4.1 Ignorar Blocos |

---

🔗 **Relacionados:** [Semântica HTML](semantica-html.md) · [Leitor de Tela](leitor-de-tela.md) · [Foco do Teclado](foco-do-teclado.md)

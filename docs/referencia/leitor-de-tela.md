# Leitor de Tela

Owner: osakareaper

📖 [Guia de Acessibilidade](index.md) › 💡 Conceitos › Fundamentos

<aside markdown="1">
💬

**Em uma frase:** software que lê em voz alta (ou em braille) o conteúdo da tela e permite navegar só pelo teclado ou por gestos. É a [Tecnologia Assistiva](tecnologia-assistiva.md) mais usada por pessoas cegas.

</aside>

## 🔊 Os mais usados

| Leitor | Sistema | Custo | Como ligar |
| --- | --- | --- | --- |
| **NVDA** | Windows | Gratuito | Ctrl + Alt + N |
| **VoiceOver** | macOS | Nativo | Cmd + F5 |
| **VoiceOver** | iOS | Nativo | Ajustes › Acessibilidade |
| **TalkBack** | Android | Nativo | Configurações › Acessibilidade |
| **JAWS** | Windows | Pago | — |

## 🗣️ O que ele anuncia

Para cada elemento, o leitor fala o [Nome Acessível](nome-acessivel.md), a **função** e o **estado**:

<aside markdown="1">
✅

`<button aria-label="Buscar">🔍</button>`

🔊 *"Buscar, botão"*

</aside>

<aside markdown="1">
❌

`<div onclick="buscar()">🔍</div>`

🔊 *(silêncio — nem é anunciado como botão)*

</aside>

## ⌨️ Atalhos do NVDA para auditar

| Tecla | Vai para |
| --- | --- |
| **H** | Próximo título (h1–h6) |
| **D** | Próxima região ([Landmarks](landmarks.md)) |
| **K** | Próximo link |
| **F** | Próximo campo de formulário |
| **B** | Próximo botão |
| **Insert + F7** | Lista de todos os elementos |

---

🔗 **Relacionados:** [Tecnologia Assistiva](tecnologia-assistiva.md) · [Nome Acessível](nome-acessivel.md) · [Árvore de Acessibilidade](arvore-de-acessibilidade.md) · [Kit de Ferramentas](kit-de-ferramentas.md)

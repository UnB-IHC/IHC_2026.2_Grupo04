# CAPTCHA

Owner: osakareaper

📖 [Guia de Acessibilidade](index.md) › 💡 Conceitos › Auditoria

<aside markdown="1">
💬

**Em uma frase:** teste para distinguir humanos de robôs — e um dos **itens críticos** do Anexo da [NBR/ABNT](nbr-abnt.md), porque frequentemente bloqueia pessoas com deficiência.

</aside>

## 🚧 Quem fica de fora

| Tipo de CAPTCHA | Quem é excluído |
| --- | --- |
| 🖼️ Imagem distorcida / "clique nos semáforos" | Pessoas cegas ou com baixa visão |
| 🔊 Áudio | Pessoas surdas e surdocegas; áudio confuso exclui muita gente |
| ⏱️ Com tempo limite | Limitações motoras e cognitivas |
| 🧩 Quebra-cabeça de arrastar | Quem usa teclado ou acionadores |

## ✅ Alternativas melhores

- CAPTCHA invisível ou comportamental (ex: Cloudflare Turnstile, reCAPTCHA v3).
- Campo "pote de mel" (honeypot) escondido de humanos.
- Limite de tentativas por IP ou sessão.
- Se precisar de desafio: alternativa em áudio **e** em lógica, operável por teclado, com [Nome Acessível](nome-acessivel.md) nos botões.

<aside markdown="1">
📦

**Nos Correios:** o Rastreamento e a Busca CEP exibem desafio de segurança. Na auditoria, verifique se existe alternativa acessível em português e se ela funciona com teclado e leitor de tela.

</aside>

<aside markdown="1">
🔐

**Regra da auditoria:** quem testa e resolve o CAPTCHA é a pessoa auditora. O agente de IA só identifica a barreira e documenta — nunca contorna. Veja [Human-in-the-Loop](human-in-the-loop.md).

</aside>

## 📏 Na norma

| NBR 17225 | WCAG 2.2 |
| --- | --- |
| Anexo de Itens Críticos · 5.2.1 | 1.1.1 Conteúdo Não Textual · 3.3.8 Autenticação Acessível |

---

🔗 **Relacionados:** [Human-in-the-Loop](human-in-the-loop.md) · [Texto Alternativo](texto-alternativo.md) · [Necessidades de Acessibilidade](necessidades-de-acessibilidade.md)

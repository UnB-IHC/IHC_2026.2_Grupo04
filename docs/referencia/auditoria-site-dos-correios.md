# Auditoria: Site dos Correios

Owner: osakareaper

<aside markdown="1">
📦

**Objetivo:** avaliar a acessibilidade do site dos Correios ([correios.com.br](http://correios.com.br)) com base na **ABNT NBR 17225:2025** e na **WCAG 2.2**, usando uma amostra de 4 fluxos críticos para o cidadão.

Cada linha do checklist abaixo é um critério unificado (NBR + WCAG). Durante o teste, atualize **Resultado**, **Severidade da Falha** e **Observações / Evidências**.

</aside>

## 🎯 Escopo da Auditoria — Fluxos Avaliados

<aside markdown="1">
🏠

**Fluxo 1 — Página Inicial e Navegação Global**

`correios.com.br`

- Mega menu
- Busca rápida
- Carrossel de banners
- Contraste da paleta amarelo/azul
- Rodapé
</aside>

<aside markdown="1">
📮

**Fluxo 3 — Busca CEP / Endereço**

`buscacepinter.correios.com.br`

- Formulário de consulta
- Filtros
- Tabelas de resultados
- Paginação
</aside>

<aside markdown="1">
🔍

**Fluxo 2 — Rastreamento de Objetos**

`rastreamento.correios.com.br`

- Campo de código de objeto
- Desafio de segurança [CAPTCHA](captcha.md)
- Mensagens de erro
- Linha do tempo de status do objeto
</aside>

<aside markdown="1">
💰

**Fluxo 4 — Preços e Prazos / Meus Correios (Login)**

- Autenticação
- Máscaras de entrada
- Modais
- Widgets flutuantes (VLibras / Chat)
</aside>

## 🧭 Roteiro de Teste

1. **Varredura automática:** rode axe DevTools, WAVE e Lighthouse em cada fluxo e anote os alertas como ponto de partida.
2. [Foco do Teclado](foco-do-teclado.md): percorra cada fluxo apenas com Tab, Shift+Tab, Enter, Espaço, Setas e Esc.
3. [Leitor de Tela](leitor-de-tela.md): repita os fluxos com NVDA (Windows) ou VoiceOver (macOS/iOS).
4. **Zoom e contraste:** aplique zoom de 200% e 400% e meça cores com o Colour Contrast Analyser (ver [Refluxo e Zoom](refluxo-e-zoom.md), [Contraste de Cores](contraste-de-cores.md) e [Kit de Ferramentas](kit-de-ferramentas.md)).
5. **Registro:** para cada falha, anote a URL exata, o elemento HTML e a sugestão de correção.

## 📊 Legenda

**Resultado**

- ⏳ **Pendente:** ainda não testado.
- ✅ **Conforme:** atende ao critério em todas as páginas da amostra.
- ⚠️ **Parcial:** atende em parte da amostra ou com ressalvas.
- ❌ **Não Conforme:** há falha que gera barreira de acesso.
- ⚪ **N/A:** o elemento avaliado não existe no fluxo.

**Severidade da Falha**

- 🔥 **Bloqueante:** impede a conclusão da tarefa (ex: CAPTCHA sem alternativa).
- 🔴 **Alta:** tarefa só é concluída com muito esforço ou ajuda.
- 🟡 **Média:** causa confusão ou atraso, mas há contorno.
- 🟢 **Baixa:** incômodo pontual, sem impedir a tarefa.

<aside markdown="1">
🤖

Quer que um agente de IA execute este checklist no navegador e grave os resultados aqui? Veja [Auditoria Assistida por IA (Human-in-the-Loop)](auditoria-assistida.md). A coluna **Camada de Teste** indica o que é automático, o que exige IA com visão e o que exige você.

</aside>

## ✅ Checklist Unificado

[✅ Checklist Unificado: NBR 17225 + WCAG 2.2 (Auditoria Correios)](checklist-unificado.md)

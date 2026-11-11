---
title: Relatório e recomendações
portal_landing: true
---
# Relatório e recomendações

<div class="work-notice" markdown="1">

**Relatório concluído.** A avaliação dos quatro fluxos críticos do portal dos Correios foi encerrada em 7 de novembro de 2026. O documento técnico está disponível em PDF, para leitura e download.

[📄 Relatório de acessibilidade — Portal dos Correios (PDF, 43 páginas, 2,6 MB)](../assets/relatorios/relatorio-acessibilidade-correios-2026-11.pdf)

</div>

## O que foi avaliado

A amostra cobre os caminhos que o cidadão percorre com mais frequência, nas seguintes páginas:

| Fluxo | Endereço |
|---|---|
| Página inicial | `www.correios.com.br` |
| Rastreamento | `rastreamento.correios.com.br` |
| Busca CEP | `buscacepinter.correios.com.br` |
| Preços e Prazos / Login | `www2.correios.com.br/sistemas/precosPrazos` e `cas.correios.com.br` |

Critérios que valem para qualquer tela (título, idioma, foco, regiões, cabeçalhos) foram verificados em todas essas páginas.

## Como foi julgado

Cada um dos **32 critérios** unificados (NBR 17225:2025 + WCAG 2.2) recebeu um resultado — Conforme, Parcial, Não conforme ou N/A — e, quando havia falha, uma severidade: **Bloqueante** (impede a tarefa), **Alta** (só se conclui com muito esforço), **Média** (atrasa ou confunde, com contorno) ou **Baixa** (incômodo pontual). A legenda completa, com o critério de cada nível, está em [Escopo e roteiro](../referencia/auditoria-site-dos-correios.md).

A coleta foi feita no Google Chrome para computador, com um agente de IA operando o navegador sob supervisão do grupo. Não foi usado leitor de tela: os efeitos para quem usa leitor de tela foram deduzidos da árvore de acessibilidade e do código, e devem ser confirmados com NVDA ou VoiceOver.

## Resultados

Dos 32 critérios, **31 são aplicáveis** (a amostra não tem vídeo nem áudio). Seis são conformes (19%), cinco parciais (16%) e **vinte não conformes (65%)**. A única falha bloqueante é o CAPTCHA da busca de CEP.

| Resultado | Critérios | Percentual dos aplicáveis |
|---|---:|---:|
| ✅ Conforme | 6 | 19% |
| ⚠️ Parcial | 5 | 16% |
| ❌ Não conforme | 20 | 65% |
| ⚪ N/A | 1 | — |

**Por severidade:** 1 bloqueante · 2 alta · 18 média · 4 baixa.

**Por princípio WCAG:** 17 Perceptível · 9 Operável · 4 Compreensível · 2 Robusto.

**Por quem verificou:** 24 pelo agente de IA, com revisão do grupo · 8 pelo agente com um integrante do grupo (CAPTCHA, login, textos alternativos, texto em imagem, linguagem, refluxo e tabelas).

### Onde a norma é violada

| Seção da NBR 17225 | Critérios | Conformes | Parciais | Não conformes |
|---|---:|---:|---:|---:|
| 5.1 Teclado e foco | 5 | 0 | 1 | 4 |
| 5.2 Imagens | 4 | 0 | 0 | 4 |
| 5.8 Botões e controles | 2 | 0 | 0 | 2 |
| 5.9 Formulários | 3 | 1 | 0 | 2 |
| 5.11 Cores | 3 | 1 | 0 | 2 |
| 5.13 Codificação semântica | 2 | 0 | 0 | 2 |
| 5.3 Cabeçalhos | 1 | 0 | 0 | 1 |
| 5.7 Links e navegação | 2 | 1 | 0 | 1 |
| 5.15 Animação | 1 | 0 | 0 | 1 |
| Anexo — itens críticos | 1 | 0 | 0 | 1 |
| 5.4 Regiões | 1 | 0 | 1 | 0 |
| 5.5 Listas | 1 | 1 | 0 | 0 |
| 5.6 Tabelas | 1 | 0 | 1 | 0 |
| 5.10 Apresentação | 2 | 1 | 1 | 0 |
| 5.12 Conteúdo textual | 2 | 1 | 1 | 0 |
| 5.14 Áudio e vídeo | 1 | 0 | 0 | 0 |

O critério de áudio e vídeo é o único não aplicável.

## Achados prioritários

O PDF traz uma ficha para cada um dos 25 achados, com captura, medição, correção recomendada e forma de verificação. O [checklist preenchido](checklist-correios.md), em **Ver evidências**, traz o passo a passo de cada teste.

| Ficha | Achado | Fluxos | Severidade |
|---|---|---|---:|
| AC-01 | CAPTCHA da busca de CEP inacessível pelo teclado: o áudio existe, mas os botões não recebem foco e o de áudio não tem nome | Busca CEP | 🔥 Bloqueante |
| AC-02 | Mensagens de erro sem vínculo com o campo e sem orientação | Busca CEP, Rastreamento, Preços e Prazos / Login | 🔴 Alta |
| AC-03 | Linha do tempo do rastreamento, submenus e opções de formato do Preços e Prazos só respondem ao mouse | Rastreamento, Página inicial, Preços e Prazos | 🔴 Alta |
| AC-04 | Resultados e erros de busca sem anúncio para leitor de tela | Busca CEP, Rastreamento | 🟡 Média |
| AC-07 | Contraste insuficiente: menu principal em 4,27:1 e link "aqui" em 4,01:1 | Página inicial | 🟡 Média |
| AC-08 | Contorno de foco do botão Consultar com 1,84:1 | Rastreamento | 🟡 Média |
| AC-10 | Foco encoberto pelo aviso de cookies e pela assistente Carol | Página inicial | 🟡 Média |
| AC-11 | Logo e "Entrar" do Rastreamento sem indicador de foco | Rastreamento | 🟡 Média |
| AC-15 | Nenhuma página tem título H1 que identifique a tela | Todos | 🟡 Média |
| AC-17 | Logo, Entrar e menu sem nome acessível | Rastreamento, Busca CEP, Página inicial | 🟡 Média |

## Plano de correção

A priorização segue o impacto para o cidadão, e cada onda reúne uma faixa de severidade.

| Onda | Prazo | Severidade | O que entra |
|---|---|---|---|
| 1 | até 30 dias | Bloqueante e alta | CAPTCHA operável pelo teclado (botões com nome, sem `tabindex="-1"`, áudio mais limpo); linha do tempo, submenus e opções de formato pelo teclado; mensagens de erro ligadas aos campos |
| 2 | 30 a 90 dias | Média | Contraste de texto e de foco, um H1 por página, `alt` de banners e links de imagem, `role="status"` nos resultados, link para pular ao conteúdo, pausa nos carrosséis, Esc no mega menu, aviso de cookies e assistente sem encobrir conteúdo, linguagem das mensagens |
| 3 | 90 a 180 dias | Baixa | Regiões com rótulo, tabelas com legenda e `scope`, ícones decorativos com `alt=""`, área de clique dos indicadores do carrossel |

**O que preservar:** seis critérios já são conformes e não devem ser alterados na pressa da correção — listas semânticas, propósito dos links, instruções sem dependência sensorial, autenticação sem teste cognitivo, espaçamento de texto adaptável e uso da cor sem perda de informação.

## Parecer

Na amostra avaliada, o portal **não atende à conformidade regular da ABNT NBR 17225:2025 nem ao nível AA da WCAG 2.2**. O resultado não é homogêneo: a navegação básica funciona para quem usa mouse e enxerga; a barreira aparece para quem depende de teclado, leitor de tela ou ampliação. O parecer vale para a data da coleta e deve ser revalidado após cada correção.

## Documentos de trabalho

- [Checklist preenchido](checklist-correios.md): os 32 critérios com resultado, evidência e captura.
- [Inspeção inicial da busca de CEP](inspecao-busca-cep.md): dois achados individuais e limites da rodada.
- [Modelo de achado](modelo-achado.md): registro reproduzível para novas inspeções.
- [Recomendações técnicas](recomendacoes.md): organização das melhorias por impacto e prioridade.
- [Escopo e roteiro](../referencia/auditoria-site-dos-correios.md): os quatro fluxos e a legenda de julgamento.

---
title: Relatório e recomendações
portal_landing: true
---
# Relatório e recomendações

<div class="work-notice" markdown="1">

**Relatório concluído.** A avaliação dos quatro fluxos críticos do portal dos Correios foi encerrada em 7 de novembro de 2026. O documento técnico está disponível em PDF, para leitura e download.

[📄 Relatório de acessibilidade — Portal dos Correios (PDF, 44 páginas, 2,3 MB)](../assets/relatorios/relatorio-acessibilidade-correios-2026-11.pdf)

</div>

## O que foi avaliado

A amostra cobre os caminhos que o cidadão percorre com mais frequência, nas seguintes páginas:

| Fluxo | Endereço |
|---|---|
| Navegação global | `correios.com.br` |
| Rastreamento | `rastreamento.correios.com.br` |
| Busca CEP | `buscacepinter.correios.com.br` |
| Preços/Login | `www2.correios.com.br/sistemas/precosPrazos` e `cas.correios.com.br` |

## Como foi julgado

Cada um dos **32 critérios** unificados (NBR 17225:2025 + WCAG 2.2) recebeu um resultado — Conforme, Parcial, Não conforme ou N/A — e, quando havia falha, uma severidade: **Bloqueante** (impede a tarefa), **Alta** (só se conclui com muito esforço), **Média** (atrasa ou confunde, com contorno) ou **Baixa** (incômodo pontual). A legenda completa, com o critério de cada nível, está em [Escopo e roteiro](../referencia/auditoria-site-dos-correios.md).

## Resultados

Dos 32 critérios, **31 são aplicáveis** (a Home não publica vídeos). Seis são conformes (19%), cinco parciais (16%) e **vinte não conformes (65%)**. A única falha bloqueante é o CAPTCHA da busca de CEP.

| Resultado | Critérios | Percentual dos aplicáveis |
|---|---:|---:|
| ✅ Conforme | 6 | 19% |
| ⚠️ Parcial | 5 | 16% |
| ❌ Não conforme | 20 | 65% |
| ⚪ N/A | 1 | — |

**Por severidade:** 1 bloqueante · 2 alta · 18 média · 4 baixa.

**Por princípio WCAG:** 17 Perceptível · 9 Operável · 4 Compreensível · 2 Robusto.

**Por camada de teste:** 11 automática · 15 IA com visão · 6 humano no loop.

### Onde a norma é violada

| Seção da NBR 17225 | Critérios | Conformes | Parciais | Não conformes |
|---|---:|---:|---:|---:|
| 5.1 Teclado | 5 | 0 | 1 | 4 |
| 5.2 Imagens | 4 | 0 | 0 | 4 |
| 5.11 Cores | 3 | 1 | 0 | 2 |
| 5.9 Formulários | 3 | 1 | 0 | 2 |
| 5.10 Apresentação | 2 | 1 | 1 | 0 |
| 5.12 Texto | 2 | 1 | 1 | 0 |
| 5.13 Semântica | 2 | 0 | 0 | 2 |
| 5.7 Links | 2 | 1 | 0 | 1 |
| 5.8 Botões e Controles | 2 | 0 | 0 | 2 |
| 5.14 Multimídia | 1 | 0 | 0 | 0 |
| 5.15 Animação | 1 | 0 | 0 | 1 |
| 5.3 Cabeçalhos | 1 | 0 | 0 | 1 |
| 5.4 Regiões | 1 | 0 | 1 | 0 |
| 5.5 Listas | 1 | 1 | 0 | 0 |
| 5.6 Tabelas | 1 | 0 | 1 | 0 |
| Anexo Crítico NBR | 1 | 0 | 0 | 1 |

## Achados prioritários

A lista completa, com medição, captura de tela e correção, está no [checklist preenchido](checklist-correios.md), em **Ver evidências**, e no PDF.

| # | Achado | Severidade |
|---|---|---:|
| 1 | CAPTCHA Acessível (Item Crítico NBR) — áudio existe, mas os botões não recebem foco e o de áudio não tem nome | 🔥 Bloqueante |
| 2 | Identificação e sugestão em erros de formulário — mensagem longe do campo, sem vínculo e sem anúncio | 🔴 Alta |
| 3 | Operação plena por teclado e sem armadilhas — submenus e controles da linha do tempo só respondem ao mouse | 🔴 Alta |
| 4 | Semântica e hierarquia de cabeçalhos — nenhuma página tem H1 com o nome da tela | 🟡 Média |
| 5 | Texto alternativo em imagens funcionais — logo, Entrar e menu sem nome acessível | 🟡 Média |
| 6 | Contraste mínimo para texto — menu principal em 4,27:1 e link “aqui” em 4,01:1 | 🟡 Média |
| 7 | Indicador de foco visível — logo e “Entrar” do Rastreamento sem contorno | 🟡 Média |
| 8 | Ordem lógica de foco — slides ocultos recebem foco e o resultado da busca não é alcançado | 🟡 Média |
| 9 | Elemento em foco não obscurecido — cookies cobrem o rodapé e a Carol cobre atalhos | 🟡 Média |
| 10 | Anúncio automático de mensagens de status — resultado e erros sem `aria-live` | 🟡 Média |

## Plano de correção

A priorização segue o custo para o cidadão, não a contagem de achados.

| Onda | Prazo | O que entra |
|---|---|---|
| 1 | 0–30 dias | CAPTCHA (botões com nome, sem `tabindex="-1"`, áudio limpo), mega menu por teclado com Esc, controles da linha do tempo |
| 2 | 30–90 dias | Contraste de texto e de indicadores, um H1 por página, `alt` de banners e ícones, mensagens de erro associadas, `aria-live` nos resultados |
| 3 | 90–180 dias | Landmarks, tabelas com `caption`/`scope`, hierarquia de títulos, carrossel com pausa, linguagem das mensagens |

**O que preservar:** seis critérios já são conformes e não devem ser alterados na pressa da correção — listas semânticas, propósito dos links, instruções sem dependência sensorial, autenticação sem teste cognitivo, espaçamento de texto adaptável e uso da cor sem perda de informação.

## Parecer

Na amostra avaliada, o portal **não atende à conformidade regular da ABNT NBR 17225:2025 nem ao nível AA da WCAG 2.2**. O resultado não é homogêneo: a navegação básica funciona para quem usa mouse e enxerga; a barreira aparece para quem depende de teclado, leitor de tela ou ampliação. O parecer vale para a data da coleta e deve ser revalidado após cada correção.

## Documentos de trabalho

- [Checklist preenchido](checklist-correios.md): os 32 critérios com resultado, evidência e captura.
- [Inspeção inicial da busca de CEP](inspecao-busca-cep.md): dois achados individuais e limites da rodada.
- [Modelo de achado](modelo-achado.md): registro reproduzível para novas inspeções.
- [Recomendações técnicas](recomendacoes.md): organização das melhorias por impacto e prioridade.
- [Escopo e roteiro](../referencia/auditoria-site-dos-correios.md): os quatro fluxos e a legenda de julgamento.

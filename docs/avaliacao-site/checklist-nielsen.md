---
title: Checklist de Nielsen
---
# Checklist de Nielsen

Perguntas para aplicar as [dez heurísticas do guia](../guia/heuristicas-nielsen.md) aos fluxos dos Correios. Este roteiro complementa o [checklist de acessibilidade NBR/WCAG](checklist-correios.md).

## Como registrar

Escolha uma tarefa e registre a URL, a data, o dispositivo e as condições da inspeção. Percorra o fluxo para conhecer a interface e depois examine as perguntas abaixo. Para cada problema, use o [modelo de achado](modelo-achado.md) e anexe a evidência correspondente.

Use os seguintes estados no registro de cada rodada:

- **Problema observado:** há um comportamento reproduzível e uma justificativa ligada à heurística.
- **Sem problema observado no trecho:** a inspeção daquele trecho não encontrou um problema. Não significa aprovação do site inteiro.
- **Não verificado:** o cenário ainda não foi executado ou houve uma limitação.
- **Não aplicável:** a funcionalidade não existe no recorte; explique o motivo.

A [inspeção inicial da busca de CEP](inspecao-busca-cep.md) exemplifica o preenchimento. Os resultados dessa rodada ficam separados do roteiro reutilizável.

Exemplos no CEP: [H3, botões do CAPTCHA fora da sequência de Tab](inspecao-busca-cep.md#cep-h03-02-alternativas-do-captcha-fora-da-sequencia-de-tab) e [H6, instrução que some ao digitar](inspecao-busca-cep.md#cep-h06-01-orientacao-disponivel-apenas-no-campo-vazio).

## Perguntas de inspeção

| ID | Heurística | O que observar nos Correios | Como verificar |
| --- | --- | --- | --- |
| H1 | Visibilidade do status | A consulta informa processamento, conclusão ou ausência de resultados? | Realizar uma busca e acompanhar as transições. |
| H2 | Correspondência com o mundo real | As instruções e os filtros usam termos compreensíveis para quem consulta o serviço? | Ler os rótulos, as opções e as mensagens no contexto da tarefa. |
| H3 | Controle e liberdade | É possível corrigir a consulta e acessar as alternativas disponíveis? | Experimentar retorno, edição e nova busca, inclusive pelo teclado. |
| H4 | Consistência e padrões | Campos, ações e mensagens mantêm nomes e comportamentos coerentes? | Comparar as etapas do mesmo fluxo. |
| H5 | Prevenção de erros | A página explica as entradas esperadas antes do envio? | Inspecionar orientações e testar campos vazios ou formatos inadequados. |
| H6 | Reconhecimento em vez de memorização | As orientações necessárias continuam disponíveis durante o preenchimento? | Comparar o formulário vazio e preenchido. |
| H7 | Flexibilidade e eficiência | Há meios de repetir a consulta sem esforço desnecessário? | Repetir uma tarefa e examinar filtros e navegação por teclado. |
| H8 | Estética e minimalismo | A hierarquia destaca os campos, a ação principal e o resultado? | Observar o percurso de leitura e possíveis distrações. |
| H9 | Reconhecimento e recuperação de erros | A mensagem identifica o problema e orienta a próxima tentativa? | Provocar validações e examinar o retorno sem dados. |
| H10 | Ajuda e documentação | As regras de preenchimento e os recursos de ajuda são fáceis de localizar? | Procurar exemplos, instruções persistentes e ajuda contextual. |

## Severidade proposta

Use a escala apresentada no [guia de Nielsen](../guia/heuristicas-nielsen.md#etapa-4-classificacao-de-severidade): **0** sem problema reconhecido; **1** cosmético; **2** pequeno; **3** grande; **4** catastrófico. Não use zero para um cenário que não foi testado.

Justifique a nota pelo impacto, pela repetição do obstáculo e pela possibilidade de contorno. Em uma inspeção individual, registre a severidade como **proposta**, para revisão na consolidação do grupo. A severidade heurística não substitui os níveis de conformidade WCAG nem a classificação usada no checklist NBR/WCAG.

## Relação com a avaliação de acessibilidade

Um mesmo achado pode motivar testes nos dois roteiros. Por exemplo, controles fora da sequência de Tab merecem investigação no [critério de operação por teclado](../referencia/criterios/operacao-plena-por-teclado-e-sem-armadilhas.md). Registre a relação quando houver evidência; a associação não comprova equivalência entre uma heurística e um requisito normativo.

Mantenha os achados individuais identificados por rodada. A síntese do grupo deve reconciliar duplicações, revisar as severidades e distinguir inspeção heurística de teste com participantes.

## Referências

- NIELSEN, Jakob. [10 Usability Heuristics for User Interface Design](https://www.nngroup.com/articles/ten-usability-heuristics/). 1994, revisão de 2024. Acesso em 04/11/2026.
- MORAN, Kate; GORDON, Kelley. [How to Conduct a Heuristic Evaluation](https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/). 2023. Acesso em 04/11/2026.
- NIELSEN, Jakob. [Severity Ratings for Usability Problems](https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/). 1994. Acesso em 04/11/2026.

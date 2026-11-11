# Plano de correção

A ordem de correção segue o impacto para o cidadão, e não a quantidade de achados: primeiro o que impede a tarefa, depois o que a torna penosa e, por último, o que causa desconforto. Cada onda reúne os achados de uma faixa de severidade.

{{tabela_plano}}

## Como executar

**Onda 1 (até 30 dias).** Tornar o CAPTCHA da busca de CEP operável pelo teclado: botões com nome acessível, sem `tabindex="-1"`, e áudio mais limpo. No mesmo ciclo, levar ao teclado os controles da linha do tempo do Rastreamento, os submenus do menu principal e as opções de formato do Preços e Prazos, e associar as mensagens de erro aos campos.

**Onda 2 (30 a 90 dias).** Corrigir contraste de texto e de indicadores de foco, definir um H1 por página, revisar textos alternativos de banners e links de imagem, anunciar resultados com `role="status"`, adicionar link para pular ao conteúdo, pausa nos carrosséis e Esc no mega menu, e ajustar aviso de cookies e assistente virtual para não encobrir o foco nem o conteúdo ampliado. São, em sua maioria, ajustes de conteúdo, CSS e atributos, com amplo alcance e baixo risco.

**Onda 3 (90 a 180 dias).** Ajustes de semântica fina: regiões com rótulo, tabelas com legenda e `scope`, ícones decorativos com `alt=""` e área de clique dos indicadores do carrossel.

## O que preservar

Seis critérios já estão conformes e não devem ser afetados pelas correções: listas semânticas, propósito dos links, instruções sem dependência de características sensoriais, autenticação sem teste cognitivo, espaçamento de texto adaptável e uso da cor sem perda de informação.

## Recomendações de processo

1. **Verificar acessibilidade na entrega, não no fim.** Incluir verificação automática no processo de publicação e um teste de teclado obrigatório antes de publicar uma tela nova.
2. **Testar com tecnologia assistiva.** Fazer sessões periódicas com leitor de tela (NVDA no Windows e VoiceOver no macOS e iOS) nos fluxos críticos, de preferência com pessoas com deficiência.
3. **Tratar conteúdo como parte da acessibilidade.** Textos alternativos, títulos, mensagens de erro e linguagem mudam a cada campanha. Sem revisão editorial, a conformidade conquistada se perde na campanha seguinte.
4. **Exigir acessibilidade de terceiros.** Componentes incorporados, como a assistente virtual, o aviso de cookies e a verificação anti-robô, respondem por parte dos achados e precisam de exigência contratual.
5. **Publicar uma declaração de acessibilidade**, com o nível alcançado, os recursos disponíveis e um canal para relatar barreiras.

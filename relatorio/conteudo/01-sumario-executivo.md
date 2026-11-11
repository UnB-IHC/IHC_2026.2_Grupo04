# Sumário executivo

Este relatório apresenta a avaliação de acessibilidade digital do Portal dos Correios realizada em {{data_coleta}}. Foram avaliados quatro fluxos de uso frequente: página inicial, rastreamento de objetos, busca de CEP e cálculo de preços e prazos com login. A referência é a ABNT NBR 17225:2025, com a correspondência para os critérios de sucesso da WCAG 2.2.

{{painel}}

**Conclusão.** Na amostra avaliada, o portal não atende à conformidade regular da ABNT NBR 17225:2025 nem ao nível AA da WCAG 2.2. Dos {{aplicaveis}} critérios aplicáveis, {{nc}} são não conformes, {{parcial}} são parcialmente conformes e {{conforme}} são conformes. Quem enxerga e usa mouse consegue concluir as tarefas. As barreiras recaem sobre quem navega pelo teclado, usa leitor de tela ou amplia a tela.

## Principais barreiras

1. **CAPTCHA da busca de CEP (bloqueante).** Os botões de áudio e de nova imagem não recebem foco pelo teclado, e o botão de áudio não tem nome acessível. Quem não usa mouse não alcança a alternativa sonora e não conclui a busca.
2. **Operação por teclado (alta).** No rastreamento, "Mais informações" e "Compartilhar" não recebem foco, e metade dos eventos do objeto só aparece com o mouse. Os submenus da página inicial e as opções de formato do Preços e Prazos também ficam fora do teclado.
3. **Mensagens de erro (alta).** Os erros aparecem longe do campo, sem vínculo programático com ele e sem anúncio para leitor de tela. Algumas não dizem como corrigir, como "Captcha Inválido!" e "Período inválido".

Também se repetem nos quatro fluxos: controles de ícone sem nome acessível, nenhuma página com título de nível 1 (H1) que identifique a tela, foco encoberto pelo aviso de cookies e pela assistente virtual, e contraste insuficiente no menu principal.

## O que já funciona

Seis critérios estão conformes: listas semânticas, propósito dos links, instruções sem dependência de características sensoriais, autenticação sem teste cognitivo, espaçamento de texto adaptável e uso da cor sem perda de informação. Esses pontos devem ser preservados durante as correções.

## Recomendação

Corrigir em três ondas definidas pela severidade: em até 30 dias, o item bloqueante e os {{alta}} de severidade alta; de 30 a 90 dias, os {{media}} de severidade média; de 90 a 180 dias, os {{baixa}} de severidade baixa. O plano está no capítulo 6, e cada achado tem uma ficha no capítulo 5 com evidência, correção recomendada e forma de verificação.

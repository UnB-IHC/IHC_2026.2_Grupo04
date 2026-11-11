# Escopo e método

## Objeto avaliado

A amostra cobre os caminhos que o cidadão percorre com mais frequência no portal.

| Fluxo | Endereço | Elementos avaliados |
|---|---|---|
| Página inicial | `www.correios.com.br` | cabeçalho, menu principal, busca rápida, carrosséis, rodapé, aviso de cookies e assistente virtual Carol |
| Rastreamento | `rastreamento.correios.com.br` | campo de consulta, mensagens de erro, linha do tempo do objeto e carrossel |
| Busca CEP | `buscacepinter.correios.com.br` | formulário, CAPTCHA, tabela de resultados e paginação |
| Preços e Prazos / Login | `www2.correios.com.br/sistemas/precosPrazos` e `cas.correios.com.br` | formulário de cálculo, tabela de resultado e autenticação |

Os critérios que valem para qualquer tela, como título, idioma, foco, regiões e cabeçalhos, foram verificados em todas as páginas acima. No inventário do Anexo A eles aparecem com o fluxo "Global".

## Período e ambiente

A coleta foi feita em {{data_coleta}}, no navegador Google Chrome para computador. O refluxo foi verificado com a página exibida em 320 px de largura, o equivalente a 400% de zoom numa tela de 1280 px, como define a WCAG 1.4.10. O portal muda com frequência (banners, campanhas e ofertas), e os achados descrevem o estado observado na data da coleta.

## Procedimento

Foram aplicados os {{total}} critérios do checklist unificado do grupo, que reúne itens da NBR 17225:2025 e os critérios de sucesso correspondentes da WCAG 2.2. Para cada critério, a verificação combinou as técnicas abaixo, conforme a natureza do item:

- **Varredura no navegador:** estrutura da página (listas, cabeçalhos, regiões, `alt`, `lang`, `title`), nome acessível de botões e links, contraste calculado pela fórmula da WCAG e tamanho das áreas de clique.
- **Percurso pelo teclado:** Tab, Shift+Tab, Enter, Espaço e Esc. A cada tecla, foram registrados o elemento focado, sua posição e se estava visível ou encoberto.
- **Formulários com dados vazios e inválidos:** foram observados a mensagem exibida, o vínculo dela com o campo e a existência de região de anúncio para leitor de tela.
- **Inspeção das capturas de tela:** indicador de foco, sobreposição de elementos e texto dentro de imagens.

A coleta foi conduzida com um agente de IA operando o navegador, sob supervisão de integrantes do grupo. Os integrantes atuaram onde era necessário julgamento humano ou ação pessoal: ouvir e resolver o CAPTCHA, entrar com conta própria no login e julgar texto alternativo, texto em imagem, clareza da linguagem e refluxo. Todos os resultados foram revisados pelo grupo.

{{tabela_verificacao}}

Cada critério tem ao menos uma medição e uma captura de tela registradas no checklist público do grupo, que traz também o passo a passo de cada teste: {{checklist}}.

## Critérios de julgamento

**Resultado.** *Conforme*: atende em toda a amostra. *Parcial*: atende em parte da amostra ou com ressalva. *Não conforme*: há barreira em ao menos um fluxo. *N/A*: o elemento não existe na amostra, como ocorreu com vídeos.

**Severidade**, atribuída aos itens não conformes e parciais. *Bloqueante*: impede concluir a tarefa. *Alta*: a tarefa só é concluída com muito esforço ou ajuda. *Média*: causa confusão ou atraso, mas há contorno. *Baixa*: incômodo pontual.

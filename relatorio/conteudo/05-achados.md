# Achados

Os {{achados}} achados estão em ordem de severidade: primeiro o que bloqueia a tarefa, depois o que a torna muito difícil e, por fim, o que atrapalha sem impedir. Dentro de cada severidade, os não conformes vêm antes dos parciais.

Cada ficha traz o critério da NBR e da WCAG, os fluxos em que a barreira foi observada, uma captura de tela, o que foi observado, a medição registrada, quem é afetado, a correção recomendada e como verificar a correção. As demais capturas de cada achado estão no Anexo B.

{{indice_achados}}

<!--
Formato de cada ficha, lido por gerar.py: título em nível 2 e, na linha seguinte, um comentário
com "criterio" (nome exato no checklist), "fluxos" e "captura" (caminho em evidencias/).
Os campos vêm em negrito, cada um em linha própria, seguidos do texto.
Numeração AC-xx, resultado, severidade e referências saem do checklist.
-->

## CAPTCHA da busca de CEP inacessível pelo teclado
<!-- criterio: CAPTCHA Acessível (Item Crítico NBR) | fluxos: Busca CEP | captura: busca-cep/01-estado-inicial.jpg -->

**O que foi observado**

O CAPTCHA de imagem oferece áudio, mas o botão de áudio e o de gerar nova imagem têm `tabindex="-1"` e nunca recebem foco pelo teclado. O botão de áudio também não tem nome acessível. Ouvido com o mouse, o áudio está em português, mas com muito ruído de fundo. No Rastreamento não há desafio visível: a verificação (Cloudflare Turnstile) é invisível e não pediu interação.

**Medição registrada**

```text
<a tabindex="-1" class="captcha_play_button">
  <i class="fa fa-volume-up" aria-hidden="true"></i>      ← sem nome
</a>
<a tabindex="-1" title="Refresh Image" id="captcha_refresh_btn">

Tab: INPUT#endereco → SELECT#tipoCEP → INPUT#captcha → BUTTON "Buscar"
(áudio e nova imagem nunca recebem foco)
```

**Onde**

`a.captcha_play_button` e `a#captcha_refresh_btn`, no formulário do Busca CEP.

**Quem é afetado**

Pessoas cegas ou com baixa visão que não leem a imagem distorcida e navegam pelo teclado, e pessoas com deficiência motora que não usam mouse. A alternativa em áudio existe, mas não pode ser alcançada. Sem resolver o CAPTCHA, a busca não é feita.

**Correção recomendada**

Trocar os dois links por `<button>` com nome em português ("Ouvir código" e "Gerar nova imagem"), sem `tabindex="-1"`, e reduzir o ruído do áudio. Avaliar uma verificação sem desafio para a pessoa, como a já usada no Rastreamento.

**Como verificar a correção**

Usando só o teclado, alcançar e acionar "Ouvir código" e "Gerar nova imagem": os dois devem receber foco visível, ter nome acessível e produzir áudio inteligível. Repetir com leitor de tela.

## Mensagens de erro sem vínculo com o campo e sem orientação
<!-- criterio: Identificação e sugestão em erros de formulário | fluxos: Busca CEP, Rastreamento, Preços e Prazos / Login | captura: busca-cep/04-captcha-invalido.jpg -->

**O que foi observado**

No Busca CEP, o envio vazio mostra "Informe o Endereço com no mínimo 2 (dois) caracteres!" e o CAPTCHA errado mostra "Captcha Inválido!", numa faixa abaixo do botão, sem ligação com o campo e sem anúncio para leitor de tela. "Captcha Inválido!" não diz o que fazer. No Rastreamento, a mensagem do campo vazio fica abaixo do campo, mas também sem ligação nem anúncio, e um código inexistente gera "Período inválido". No Preços e Prazos, o alerta do navegador leva o foco ao campo, mas mostra um erro por vez. No login, a senha errada gera uma mensagem em inglês e sem sugestão.

**Medição registrada**

```text
Busca CEP     DIV#alerta  role=null  aria-live=null   "Captcha Inválido!"
              #captcha    aria-invalid=null  aria-describedby=null
              regiões live na página: 0
Rastreamento  DIV.mensagem  role=null  aria-live=null
              #objeto       aria-invalid=null  aria-describedby=null
```

**Onde**

`#alerta`, `#endereco` e `#captcha` (Busca CEP); `div.mensagem` e `#objeto` (Rastreamento); mensagem de erro da tela de login.

**Quem é afetado**

Usuários de leitor de tela não são avisados do erro nem sabem a que campo ele se refere. Pessoas com deficiência intelectual ou pouca familiaridade com sistemas recebem mensagens que não dizem como corrigir.

**Correção recomendada**

Mostrar a mensagem junto ao campo, ligada por `aria-describedby`, com `aria-invalid="true"` no campo e `role="alert"`. Dizer o que corrigir: "Código incorreto. Digite os caracteres da imagem ou ouça o áudio."

**Como verificar a correção**

Enviar cada formulário vazio e com dado inválido: a mensagem deve aparecer junto ao campo, estar ligada a ele, ser anunciada pelo leitor de tela e dizer como corrigir.

## Funções do rastreamento, do menu e do Preços e Prazos fora do teclado
<!-- criterio: Operação plena por teclado e sem armadilhas | fluxos: Rastreamento, Página inicial, Preços e Prazos / Login | captura: rastreamento/07-linha-do-tempo-expandida-mouse.jpg -->

**O que foi observado**

No Rastreamento, "Mais informações" (+) e "Compartilhar" são links sem `href` e não recebem foco: 3 dos 6 eventos do objeto só aparecem com o mouse. Na página inicial, os submenus do menu principal só abrem com o mouse. No Preços e Prazos, as opções de formato (Caixa, Envelope e Rolo) não recebem foco.

**Medição registrada**

```text
a#a-ver-mais ("+", Mais informações)   sem href
a.btn[title=Compartilhar]              sem href
Tab: Consultar → "Ver cupons"          (pula a linha do tempo)
```

**Onde**

`a#a-ver-mais` e `a[title=Compartilhar]` (Rastreamento); menu principal (página inicial); campo "Formato" (Preços e Prazos).

**Quem é afetado**

Pessoas que não usam mouse, por deficiência motora, cegueira ou lesão por esforço repetitivo. Elas não veem o histórico completo do objeto, não chegam aos submenus e não escolhem o formato da encomenda.

**Correção recomendada**

Usar `<button>` em "Mais informações", com `aria-expanded`, e em "Compartilhar". Abrir os submenus com Enter e Espaço. Tornar as opções de formato focáveis, por exemplo com `input type="radio"` e rótulo.

**Como verificar a correção**

Rastrear um objeto e ver o histórico completo, navegar pelo menu principal e calcular um preço usando só Tab, Shift+Tab, setas, Enter, Espaço e Esc.

## Resultados e erros de busca sem anúncio para leitor de tela
<!-- criterio: Anúncio automático de mensagens de status | fluxos: Busca CEP, Rastreamento | captura: busca-cep/07-paginacao-proximo-teclado.jpg -->

**O que foi observado**

No Busca CEP, o resultado e cada página da paginação são inseridos sem região de anúncio (a página não tem nenhuma região `aria-live`), e o foco volta ao início da página depois da busca. No Rastreamento existe uma região `role="status"`, mas ela fica vazia: "Buscando..." e as mensagens de erro aparecem fora dela.

**Medição registrada**

```text
Busca CEP  +H5 em DIV#mensagem-resultado   live=false
           +TR em TBODY                    live=false   (50 por página)
           regiões live na página: 0  |  foco após o resultado: BODY
```

**Onde**

`#mensagem-resultado` e tabela de resultado (Busca CEP); região `role="status"` (Rastreamento).

**Quem é afetado**

Usuários de leitor de tela não sabem que a busca terminou, quantos resultados existem nem que a página mudou ao avançar a paginação.

**Correção recomendada**

Colocar a contagem de resultados e as mensagens numa região `role="status"` e levar o foco ao título do resultado depois da busca.

**Como verificar a correção**

Com leitor de tela, buscar um CEP, avançar a paginação e consultar um código inválido: o resultado, a nova página e o erro devem ser anunciados.

## Texto de campanhas publicado só como imagem
<!-- criterio: Ausência de imagens de texto | fluxos: Página inicial | captura: home-global/01-estado-inicial-cookies-carol.jpg -->

**O que foi observado**

Banners e cards de campanha trazem o texto dentro da imagem, e o texto alternativo não o reproduz. O banner "O mês virou e os preços caíram! Vem pro Novembro de Ofertas…" tem `alt="Mais Correios"`. O card do prêmio Reclame Aqui também tem o texto principal só na imagem.

**Medição registrada**

```text
1351×312  alt="Mais Correios"
          imagem: "O mês virou e os preços caíram! Vem pro Novembro de Ofertas…"
 473×420  alt="Correios Celular no prêmio Reclame Aqui"
          imagem continua: "Estamos concorrendo… Vote…"
```

**Onde**

Banners `.banner-home` e cards da página inicial.

**Quem é afetado**

Pessoas com baixa visão que ampliam a tela ou alteram cores, porque o texto da imagem perde nitidez e não se adapta, e usuários de leitor de tela, que não recebem o conteúdo da campanha.

**Correção recomendada**

Publicar o texto da campanha em HTML sobre a imagem. Quando não for possível, reproduzir o texto completo no `alt`.

**Como verificar a correção**

Com as imagens desativadas ou com leitor de tela, o conteúdo de cada banner deve continuar disponível em texto.

## Mega menu não fecha com Esc nem abre pelo teclado
<!-- criterio: Conteúdo adicional em hover ou foco | fluxos: Página inicial | captura: home-global/13-megamenu-apos-esc.jpg -->

**O que foi observado**

O mega menu do menu principal abre ao passar o mouse, continua aberto depois de Esc e não abre com Enter. O item "Enviar" é um link `href="#"` sem `aria-expanded` nem `aria-haspopup`.

**Medição registrada**

```text
ativo: A "Enviar"  href="#"  aria-expanded=null  aria-haspopup=null
link "Nacional"    visível=false
próximo Tab:       "Receber"
```

**Onde**

Menu principal (Enviar, Receber, Comprar e demais itens).

**Quem é afetado**

Pessoas que navegam pelo teclado não chegam aos submenus. Pessoas com baixa visão que usam ampliação ficam com o conteúdo encoberto pelo menu, sem como dispensá-lo.

**Correção recomendada**

Fechar o menu com Esc. Transformar os itens em botões com `aria-expanded`, que abram com Enter e Espaço. Manter o menu aberto enquanto o ponteiro estiver sobre ele.

**Como verificar a correção**

Abrir cada submenu só com o teclado, percorrer os itens e fechar com Esc. Com o mouse, abrir o menu e fechá-lo com Esc sem mover o ponteiro.

## Contraste insuficiente no menu principal e em links
<!-- criterio: Contraste mínimo para texto (4,5:1 / 3:1) | fluxos: Página inicial | captura: home-global/03-foco-menu-enviar.png -->

**O que foi observado**

Quatro combinações de texto e fundo ficam abaixo de 4,5:1: o menu principal (4,27:1), o link "aqui" (4,01:1), um título de notícia (4,49:1) e "Confira os eletrônicos" sobre amarelo (3,70:1). No Busca CEP e no Rastreamento não houve falha de contraste de texto.

**Medição registrada**

```text
4,27:1  rgb(0,123,179) sobre rgb(243,245,240)   "Enviar" (menu)
4,01:1  rgb(0,123,179) sobre rgb(239,237,234)   "aqui"
4,49:1  rgb(0,123,179) sobre rgb(250,250,250)   título de notícia
3,70:1  rgb(0,113,173) sobre rgb(255,212,0)     "Confira os eletrônicos"
```

**Onde**

Menu principal, link "Simule aqui outros serviços", títulos de notícia e card de ofertas da página inicial.

**Quem é afetado**

Pessoas com baixa visão, idosos e qualquer pessoa usando o celular sob luz forte.

**Correção recomendada**

Escurecer o azul dos links e do menu até atingir pelo menos 4,5:1 sobre os fundos usados (3:1 para texto grande).

**Como verificar a correção**

Medir as quatro combinações com um analisador de contraste: todas devem ter 4,5:1 ou mais.

## Contorno de foco do botão Consultar quase invisível
<!-- criterio: Contraste não textual (3:1 em bordas e ícones) | fluxos: Rastreamento | captura: rastreamento/03-foco-botao-consultar.png -->

**O que foi observado**

O contorno de foco do botão "Consultar", azul translúcido, tem 1,84:1 contra o fundo e 2,43:1 contra o botão, abaixo do mínimo de 3:1. Nos demais pontos medidos o contraste é suficiente: no Busca CEP, bordas dos campos (4,50:1), foco (5,30:1) e ícones (5,30:1); no Rastreamento, o foco do campo de consulta.

**Medição registrada**

```text
Rastreamento  contorno de foco do "Consultar": rgba(0,123,255,.5)
              1,84:1 contra o fundo  ·  2,43:1 contra o botão   (mínimo 3:1)
Busca CEP     borda 4,50:1  ·  foco 5,30:1  ·  ícones 5,30:1   (atende)
```

**Onde**

`button#b-pesquisar`, no Rastreamento.

**Quem é afetado**

Pessoas com baixa visão que navegam pelo teclado não percebem que o foco está no botão.

**Correção recomendada**

Contorno de foco sólido e escuro, com pelo menos 3:1 contra o botão e contra o fundo, por exemplo 2 px sólido na cor do texto.

**Como verificar a correção**

Focar "Consultar" com Tab e medir o contorno contra o botão e contra o fundo: os dois valores devem ser 3:1 ou mais.

## Carrosséis giram sozinhos e não têm botão de pausa
<!-- criterio: Controle de carrosséis/animações e Limite de tempo | fluxos: Página inicial, Rastreamento | captura: rastreamento/08-carrossel.jpg -->

**O que foi observado**

O carrossel do Rastreamento troca de banner sozinho a cada 10 segundos e só tem os controles "anterior" e "próximo". Na página inicial, o carrossel principal e o bloco "Correios Aqui" também giram sem opção de pausa. Não há sessão com tempo limite nos fluxos sem login.

**Medição registrada**

```text
Rastreamento    div#carouselExampleControls  data-ride="carousel"  data-interval="10000"
                slide ativo a cada 4 s: 2 → 2 → 0 → 0 → 1
Página inicial  slide visível a cada 3 s: Papai Noel → Papai Noel → Mais Correios → …
Botão de pausar: não existe
```

**Onde**

`div#carouselExampleControls` (Rastreamento) e `.bannerPrincipal` (página inicial).

**Quem é afetado**

Pessoas com déficit de atenção, dislexia ou baixa visão, que precisam de mais tempo para ler, e pessoas sensíveis a movimento.

**Correção recomendada**

Botão "Pausar" visível e operável pelo teclado. Pausar também quando o carrossel recebe o foco ou o ponteiro.

**Como verificar a correção**

Pausar cada carrossel pelo teclado e confirmar que a rotação só recomeça por ação da pessoa.

## Foco encoberto pelo aviso de cookies e pela assistente virtual
<!-- criterio: Elemento em foco não obscurecido | fluxos: Página inicial | captura: home-global/10-foco-rodape-coberto-cookies.jpg -->

**O que foi observado**

Na primeira visita, com o aviso de cookies aberto, os links do rodapé ficam totalmente escondidos quando recebem foco. O atalho "Correios Empresas" fica atrás da imagem da assistente Carol.

**Medição registrada**

```text
19. "Correios Empresas"            encoberto (3 de 3 pontos) por IMG#carol-corpo-img
29. "Soluções para o seu negócio"  encoberto (3 de 3) pelo aviso de cookies
31. "Ouvidoria"  ·  32. "Denúncia"  ·  33. "Segurança"   encobertos (3 de 3)
```

**Onde**

`div.cookiesCorreios` e `img#carol-corpo-img`, na página inicial.

**Quem é afetado**

Pessoas que navegam pelo teclado perdem de vista onde está o foco.

**Correção recomendada**

Reservar espaço para o aviso com `scroll-padding-bottom` e permitir fechá-lo sem aceitar. Não sobrepor a imagem da assistente ao conteúdo.

**Como verificar a correção**

Percorrer a página com Tab, com o aviso de cookies e a assistente abertos: nenhum elemento focado pode ficar totalmente encoberto.

## Logo e "Entrar" do Rastreamento sem indicador de foco
<!-- criterio: Indicador de foco visível | fluxos: Rastreamento, Página inicial | captura: home-global/22-rastreamento-foco-entrar-invisivel.png -->

**O que foi observado**

No Rastreamento, o logo e o link "Entrar" não mostram nenhum indicador quando recebem foco. Na página inicial, o botão "Busca" tem um indicador fraco, em que só muda a cor de fundo. Menu, banners e rodapé da página inicial mostram o foco corretamente.

**Medição registrada**

```text
A.logo    focusVisible=true   outline=none   box-shadow=rgba(0,0,0,0)
A.entrar  focusVisible=true   outline=none   box-shadow=rgba(0,0,0,0)
```

**Onde**

`a.logo` e `a.entrar` (Rastreamento); botão "Busca" (página inicial).

**Quem é afetado**

Pessoas que navegam pelo teclado não sabem qual elemento será acionado.

**Correção recomendada**

Aplicar um contorno de foco visível a todos os controles, por exemplo `:focus-visible { outline: 3px solid; outline-offset: 2px }`.

**Como verificar a correção**

Focar o logo, "Entrar" e "Busca" com Tab: o contorno deve aparecer em cada um.

## Falta link para pular ao conteúdo principal
<!-- criterio: Link de salto ("Pular para o conteúdo principal") | fluxos: Página inicial, Rastreamento, Busca CEP | captura: home-global/14-menu-acessibilidade-sem-salto.jpg -->

**O que foi observado**

A página inicial não tem link de salto, e o menu "Acessibilidade" oferece apenas "Alto Contraste" e "Saiba mais". No Rastreamento e no Busca CEP o link "Ir para o conteúdo" existe, mas tem largura zero e não aparece ao receber foco.

**Medição registrada**

```text
Página inicial  nenhum link de salto
Rastreamento    "Ir para o conteúdo"          largura=0, não recebe foco no Tab
Busca CEP       "Ir para o conteúdo (alt+1)"  largura=0
```

**Onde**

Início de cada página.

**Quem é afetado**

Pessoas que navegam pelo teclado ou com leitor de tela precisam percorrer todo o cabeçalho e o menu em cada página.

**Correção recomendada**

Incluir como primeiro elemento focável de cada página um link "Ir para o conteúdo principal", visível ao receber foco, que leve ao `main`.

**Como verificar a correção**

Ao carregar a página, o primeiro Tab deve mostrar o link, e Enter deve levar o foco ao conteúdo principal.

## Campos sem rótulo recebem foco no Preços e Prazos
<!-- criterio: Rótulos (labels) visíveis e associados aos campos | fluxos: Preços e Prazos / Login | captura: precos-login/03-precos-formulario-expandido-sedex.jpg -->

**O que foi observado**

No formulário do Preços e Prazos, cinco campos de texto sem rótulo, posicionados fora da tela, recebem foco pelo Tab entre os campos do formulário. Os campos do Busca CEP, do Rastreamento e do login têm rótulo visível e associado.

**Medição registrada**

```text
Preços e Prazos  campos visíveis=16  ·  sem rótulo=6
                 text  tabIndex=0  @x=-9564  (fora da tela)
                 Tab: "Comparar…" → INPUT "" (fora da tela) → "Embalagem" → INPUT "" (fora da tela)
```

**Onde**

Campos `name="Format…"` e `name="TipoEm…"` do formulário do Preços e Prazos.

**Quem é afetado**

Quem usa leitor de tela ouve "campo de edição" sem nome e perde a referência do formulário. Quem usa teclado vê o foco desaparecer.

**Correção recomendada**

Usar `type="hidden"` nesses campos ou retirá-los da ordem de foco com `tabindex="-1"`, se não forem preenchidos pela pessoa.

**Como verificar a correção**

Percorrer o formulário com Tab: todo campo que recebe foco deve estar visível e ter rótulo associado.

## Botões de ícone sem nome acessível
<!-- criterio: Semântica e Nome Acessível em botões | fluxos: Rastreamento, Página inicial, Busca CEP | captura: home-global/08-foco-botao-lupa-sem-nome.png -->

**O que foi observado**

Três controles de ícone não têm nome acessível: imprimir, no Rastreamento; a lupa do campo de rastreio, na página inicial; e o áudio do CAPTCHA, no Busca CEP, que também não recebe foco (ver AC-01).

**Medição registrada**

```text
Rastreamento    A#print > i.fa-print[aria-hidden]    nome ""
Página inicial  BUTTON.bt-link-ic > I.ic-busca-out    nome ""
Busca CEP       a.captcha_play_button                nome ""
```

**Onde**

`a#print`, `button.bt-link-ic` e `a.captcha_play_button`.

**Quem é afetado**

Usuários de leitor de tela ouvem apenas "botão" ou "link", sem saber a ação.

**Correção recomendada**

Incluir `aria-label` com a ação: "Imprimir", "Rastrear" e "Ouvir código".

**Como verificar a correção**

Na árvore de acessibilidade do navegador, cada controle deve ter nome em português que descreva a ação.

## Nenhuma página tem título H1 que identifique a tela
<!-- criterio: Semântica e hierarquia de cabeçalhos (H1-H6) | fluxos: Página inicial, Rastreamento, Busca CEP, Preços e Prazos / Login | captura: busca-cep/05-resultado-cep-unico.jpg -->

**O que foi observado**

Na página inicial, o H1 contém só o logo, e o nível seguinte é H3. O Rastreamento não tem H1, e o título "Rastreamento" é H3. O Busca CEP não tem H1: o título é H2, e "Resultado da Busca" é H5. O Preços e Prazos tem H1 vazio, e o login não tem cabeçalhos.

**Medição registrada**

```text
Página inicial   H1 = só o logo (img)  →  H3 "Correios Aqui"  (salto)
Rastreamento     sem H1; título "Rastreamento" em H3
Busca CEP        sem H1; título em H2, resultado em H5
Preços e Prazos  H1 vazio      |      Login: nenhum h1–h3
```

**Onde**

Estrutura de cabeçalhos das cinco páginas.

**Quem é afetado**

Usuários de leitor de tela que navegam por títulos não identificam a tela nem a estrutura do conteúdo.

**Correção recomendada**

Um H1 por página com o nome da tela e os demais níveis em sequência, sem saltos.

**Como verificar a correção**

Listar os cabeçalhos de cada página: deve haver um H1 com o nome da tela e níveis sem saltos.

## Texto alternativo que não descreve a imagem
<!-- criterio: Texto alternativo em imagens de conteúdo | fluxos: Página inicial, Rastreamento, Preços e Prazos / Login | captura: rastreamento/08-carrossel.jpg -->

**O que foi observado**

Na página inicial, o banner de ofertas tem `alt="Mais Correios"`, e outra imagem tem `alt="Indexes all content in the site"`, texto-padrão do sistema de gestão de conteúdo, em inglês. No Rastreamento, os banners têm textos alternativos de outras campanhas ("Sua entrega está a caminho!", "Mês do cliente"), que não correspondem ao banner exibido. No resultado do Preços e Prazos, o logo do SEDEX, único identificador do serviço, tem `alt=""`.

**Medição registrada**

```text
alt="Mais Correios"                     → banner de ofertas inteiro
alt="Indexes all content in the site"   → texto-padrão do sistema, em inglês
Rastreamento: "Sua entrega está a caminho!", "Mês do cliente"…  ≠ banner exibido
Preços e Prazos: logo SEDEX do resultado com alt=""
```

**Onde**

Banners da página inicial e do Rastreamento; tabela de resultado do Preços e Prazos.

**Quem é afetado**

Pessoas cegas recebem uma descrição errada ou nenhuma descrição.

**Correção recomendada**

Revisar o `alt` a cada troca de campanha. No Preços e Prazos, usar `alt="SEDEX"` ou o nome do serviço em texto.

**Como verificar a correção**

Comparar cada imagem de conteúdo com seu `alt`: o texto deve transmitir a mesma informação.

## Links de imagem sem nome ou com nome que descreve a imagem
<!-- criterio: Texto alternativo em imagens funcionais | fluxos: Rastreamento, Busca CEP, Página inicial | captura: home-global/23-rastreamento-foco-logo-invisivel.png -->

**O que foi observado**

No Rastreamento, os links do logo, de "Entrar" e do menu não têm texto, `aria-label` nem `title`. No Busca CEP, o link do logo também não tem nome. Na página inicial, o logo tem `alt="Imagem com o logo dos Correios"`, que descreve a imagem e não o destino.

**Medição registrada**

```text
Rastreamento    a.logo, a.entrar, a.hamburger  → sem texto, aria-label ou title
Busca CEP       link do logo sem nome
Página inicial  logo  alt="Imagem com o logo dos Correios"
```

**Onde**

Cabeçalho do Rastreamento, do Busca CEP e da página inicial.

**Quem é afetado**

Usuários de leitor de tela ouvem "link" sem saber o destino.

**Correção recomendada**

Usar `alt="Correios — página inicial"` no logo, `aria-label="Entrar"` e `aria-label="Abrir menu"`.

**Como verificar a correção**

Cada link de imagem deve ter um nome que descreva o destino ou a ação.

## Idioma não declarado e título genérico em páginas do fluxo
<!-- criterio: Título descritivo da página (<title>) e Idioma (<html lang>) | fluxos: Rastreamento, Preços e Prazos / Login | captura: precos-login/05-meucorreios-ingles.jpg -->

**O que foi observado**

O Rastreamento e o login declaram `<html lang="">` vazio. O Preços e Prazos tem o título "home". Depois do login, o Meu Correios aparece em inglês com `lang="pt-BR"`. A página inicial ("Correios") e o Busca CEP ("Busca CEP") estão corretos.

**Medição registrada**

```text
Página inicial   title="Correios"        lang="pt-br"
Busca CEP        title="Busca CEP"       lang="pt-br"
Rastreamento     title="Rastreamento"    lang=""        ← vazio
Preços e Prazos  title="home"            lang="pt-br"   ← título genérico
Login            title="Login - CAS…"    lang=""        ← vazio
```

**Onde**

`<html lang>` e `<title>` de cada página.

**Quem é afetado**

Leitores de tela podem pronunciar o texto com a voz de outro idioma. Quem usa várias abas ou leitor de tela não identifica a página pelo título.

**Correção recomendada**

Declarar `lang="pt-BR"` em todas as páginas, com `lang="en"` apenas em trechos em inglês, e usar títulos no formato "Nome da tela — Correios".

**Como verificar a correção**

Conferir `lang` e `title` de cada página.

## Ícones decorativos lidos pelo leitor de tela
<!-- criterio: Imagens decorativas ocultas | fluxos: Página inicial, Rastreamento | captura: home-global/04-foco-login.png -->

**O que foi observado**

Nos atalhos da página inicial, os ícones ao lado do texto têm `alt` igual ao rótulo, e o leitor de tela lê duas vezes ("Preços e Prazos Preços e Prazos"). O ícone de "Faça Login" tem `alt` que descreve uma porta. No Rastreamento, os ícones da linha do tempo não têm o atributo `alt`.

**Medição registrada**

```text
Página inicial  "Preços e Prazos" (alt) + "Preços e Prazos" (texto)  → lido duas vezes
Rastreamento    IMG.circle-img sem alt  (caminhao-correndo-stroke.svg …)
```

**Onde**

Atalhos da página inicial e `img.circle-img` da linha do tempo do Rastreamento.

**Quem é afetado**

Usuários de leitor de tela ouvem informação repetida ou sem sentido.

**Correção recomendada**

Usar `alt=""` nos ícones decorativos que acompanham um texto.

**Como verificar a correção**

Inspecionar os ícones: os decorativos devem ter `alt=""` e não ser anunciados.

## Indicadores do carrossel pequenos e próximos demais
<!-- criterio: Tamanho mínimo da área de clique/toque (24x24px) | fluxos: Página inicial | captura: home-global/06-foco-banner.jpg -->

**O que foi observado**

Os indicadores do carrossel principal medem 10×10 px, e os centros estão a 20 px um do outro, abaixo do mínimo de 24 px. Eles também não recebem foco e não têm nome. No Busca CEP, a paginação (63×23 px) e os botões do CAPTCHA (20×23 e 27×19 px) são menores que 24 px, mas têm espaço livre suficiente em volta, o que a regra aceita.

**Medição registrada**

```text
<div class="circulo">  10×10  @656,394
<div class="circulo">  10×10  @676,394
<div class="circulo">  10×10  @696,394
centros a 20 px (< 24 px)  ·  tabIndex=-1  ·  sem nome
```

**Onde**

`div.circulo`, no carrossel principal da página inicial.

**Quem é afetado**

Pessoas com tremor ou dificuldade motora e quem usa tela sensível ao toque.

**Correção recomendada**

Área clicável de pelo menos 24×24 px, ou centros a pelo menos 24 px de distância.

**Como verificar a correção**

Medir a área clicável dos indicadores: deve ter 24×24 px ou centros a 24 px ou mais.

## Mensagens que não orientam a próxima ação
<!-- criterio: Linguagem simples e clareza textual | fluxos: Rastreamento, Preços e Prazos / Login | captura: rastreamento/05-codigo-ficticio-periodo-invalido.jpg -->

**O que foi observado**

Para um código inexistente, o Rastreamento mostra "Período inválido". O evento "Informações prestadas pelo cliente em análise" não diz o que a pessoa deve fazer, e "Previsão de Entrega:" aparece sem data. No login, o erro está em inglês. No Preços e Prazos, o alerta sobre dimensões da caixa é longo e técnico. Os rótulos e instruções dos formulários são diretos.

**Medição registrada**

```text
resposta para código inexistente: {"erro": true, "mensagem": "Período inválido"}
"Informações prestadas pelo cliente em análise."
"Previsão de Entrega:"   (sem valor)
"Your account is not recognized and cannot login at this time."
```

**Onde**

Mensagens de erro e linha do tempo do Rastreamento; tela de login; alertas do Preços e Prazos.

**Quem é afetado**

Pessoas com deficiência intelectual, baixa escolaridade ou pouca familiaridade com o português.

**Correção recomendada**

Usar "Código não encontrado. Confira as letras e os números."; explicar a pendência e a ação esperada; ocultar a previsão quando não houver data; escrever as mensagens de login em português, dizendo o que fazer.

**Como verificar a correção**

Ler as mensagens com uma pessoa de fora do projeto: cada uma deve dizer o que aconteceu e o que fazer.

## Foco se perde após a busca e passa por slides ocultos
<!-- criterio: Ordem lógica de foco | fluxos: Página inicial, Busca CEP, Rastreamento | captura: busca-cep/05-resultado-cep-unico.jpg -->

**O que foi observado**

Na página inicial, a ordem do Tab segue a ordem de leitura, mas slides fora da tela do carrossel "Acesso rápido" recebem foco. Depois de buscar um CEP ou rastrear um objeto, o foco volta ao início da página. No Rastreamento, o Tab pula os controles da linha do tempo (ver AC-03).

**Medição registrada**

```text
1. Acessibilidade → 2. logo → 3–8. menu → 9. Login → 10. Busca → 11–12. banners → 13. campo de rastreio …
25. "Central de Atendimento"  @1648,319  FORA DA TELA  (slide oculto)
Busca CEP e Rastreamento: após a busca, foco em BODY
```

**Onde**

Carrossel "Acesso rápido" da página inicial; resultados do Busca CEP e do Rastreamento.

**Quem é afetado**

Pessoas que navegam pelo teclado perdem o foco de vista e precisam percorrer a página de novo para chegar ao resultado.

**Correção recomendada**

Retirar do Tab os slides ocultos (com `inert` ou `tabindex="-1"`) e levar o foco ao título do resultado depois da busca.

**Como verificar a correção**

Percorrer a página do topo ao rodapé: nenhum foco fora da tela. Depois da busca, o foco deve estar no resultado.

## Em 320 px, aviso de cookies e assistente cobrem o conteúdo
<!-- criterio: Refluxo e Zoom de até 400% sem perda de conteúdo | fluxos: Página inicial | captura: home-global/20-refluxo-320px-carol-cobre-calcular.png -->

**O que foi observado**

Em 320 px de largura, equivalente a 400% de zoom, a página se reorganiza sem rolagem horizontal. Porém o aviso de cookies ocupa 47% da tela, e a assistente Carol, 30%, cobrindo o botão "Calcular Frete".

**Medição registrada**

```text
largura=316  scrollWidth=316  rolagem horizontal: não
elementos fixos: assistente Carol 164×405 = 30% da tela
                 aviso de cookies 301×341 = 47% da tela
```

**Onde**

`div#cookiesId` e `div#chat-correios`, na página inicial.

**Quem é afetado**

Pessoas com baixa visão que usam ampliação e quem acessa pelo celular.

**Correção recomendada**

Aviso de cookies compacto em telas estreitas, que possa ser fechado sem aceitar, e assistente recolhida em ícone.

**Como verificar a correção**

Em 320 px de largura, não deve haver rolagem horizontal nem conteúdo essencial encoberto.

## Regiões da página sem rótulo e menu fora de nav
<!-- criterio: Demarcação semântica de regiões (Landmarks) | fluxos: Página inicial, Rastreamento, Busca CEP | captura: home-global/03-foco-menu-enviar.png -->

**O que foi observado**

As páginas têm `main` e `footer`, mas o menu principal da página inicial não está em `nav`, nenhuma `nav` tem rótulo, e há mais de um `header` por página.

**Medição registrada**

```text
Página inicial  header=2  nav=5 (4 ocultas, nenhuma rotulada)  main=1  footer=2
Rastreamento    header=3  nav=1 ("breadcrumb")                  main=1  footer=1
Busca CEP       header=4  nav=1 (sem rótulo)                    main=1  footer=1
```

**Onde**

Estrutura de regiões das três páginas.

**Quem é afetado**

Usuários de leitor de tela que navegam por regiões não encontram o menu principal e encontram cabeçalhos repetidos.

**Correção recomendada**

Usar `<nav aria-label="Principal">` no menu e um único `header` de página.

**Como verificar a correção**

Na árvore de acessibilidade, cada página deve ter um cabeçalho, navegação rotulada, conteúdo principal e rodapé.

## Tabelas de resultado sem legenda acessível e sem escopo
<!-- criterio: Semântica de tabelas de dados | fluxos: Busca CEP, Preços e Prazos / Login | captura: precos-login/04-precos-resultado.jpg -->

**O que foi observado**

A tabela do Busca CEP usa `th` no cabeçalho e `td` no corpo, mas a legenda (`caption`) está oculta com `hidden`, o que a esconde também do leitor de tela. A tabela tem ainda o atributo obsoleto `summary`, e os `th` não têm `scope`. No Preços e Prazos, as linhas têm `th`, mas o serviço (SEDEX) só é identificado por um logo com `alt=""`.

**Medição registrada**

```text
Busca CEP        <table id="resultado-DNEC" summary="Resultado DNEC">
                   <caption hidden="true">Resultado da Busca…</caption>
                   <thead><tr><th>Logradouro/Nome</th>…   (sem scope)
Preços e Prazos  linha 0: <td> "" | <td> [img alt=""]   ← logo SEDEX
```

**Onde**

`table#resultado-DNEC` (Busca CEP) e `table.comparaResult` (Preços e Prazos).

**Quem é afetado**

Usuários de leitor de tela não ouvem o título da tabela e, no Preços e Prazos, não sabem a qual serviço os valores se referem.

**Correção recomendada**

Ocultar a legenda só visualmente (classe `sr-only` em vez de `hidden`), usar `scope="col"` e `scope="row"`, remover `summary` e identificar o serviço em texto no cabeçalho.

**Como verificar a correção**

Inspecionar as tabelas: legenda disponível ao leitor de tela, `scope` nos cabeçalhos e serviço identificado em texto.

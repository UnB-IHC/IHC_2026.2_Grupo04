# NBR/ABNT

Owner: osakareaper

<aside markdown="1">
💡

Esta seção do Guia segue a conformidade proposta pela **ABNT NBR 17225** (Acessibilidade em conteúdo e aplicações web — Requisitos), alinhada à [WCAG](wcag.md) e ao **Art. 63 da Lei Brasileira de Inclusão** (LBI - Lei nº 13.146/2015).

</aside>

# 🧩 O Ecossistema de Normas ABNT

A **ABNT NBR 17225** é a norma central para sites, mas ela faz referência normativa a outras normas brasileiras que complementam a acessibilidade digital:

<aside markdown="1">
🌐

**ABNT NBR 17225**

Acessibilidade em conteúdo e aplicações web — Requisitos.

</aside>

<aside markdown="1">
📱

**ABNT NBR 17060**

Acessibilidade em aplicativos de dispositivos móveis — Requisitos.

</aside>

<aside markdown="1">
✍️

**ABNT NBR ISO 24495-1**

Linguagem simples — Princípios norteadores e diretrizes (fundamental para acessibilidade cognitiva e textual).

</aside>

<aside markdown="1">
🎧

**ABNT NBR 16452**

Acessibilidade na comunicação — Audiodescrição.

</aside>

<aside markdown="1">
🤟

**ABNT NBR 15610-3**

Televisão digital e vídeo — Língua Brasileira de Sinais (Libras).

</aside>

# 📚 Conceitos Essenciais

Cada conceito tem sua própria nota. Leia a frase e clique para se aprofundar.

| Conceito | Em uma frase |
| --- | --- |
| [Necessidades de Acessibilidade](necessidades-de-acessibilidade.md) | Permanentes, temporárias ou situacionais — acessibilidade é para todos. |
| [Tecnologia Assistiva](tecnologia-assistiva.md) | Hardware ou software de apoio; inclui o conceito de agente de usuário. |
| [Leitor de Tela](leitor-de-tela.md) | Lê a tela em voz alta: NVDA, VoiceOver, TalkBack. |
| [Semântica HTML](semantica-html.md) | Estrutura "determinada programaticamente" no código. |
| [Nome Acessível](nome-acessivel.md) | O texto anunciado para botões, links e campos. |
| [Árvore de Acessibilidade](arvore-de-acessibilidade.md) | Função, nome e estado que chegam à tecnologia assistiva. |
| [Foco do Teclado](foco-do-teclado.md) | O contorno que mostra onde você está ao usar Tab. |
| [Níveis de Conformidade](niveis-de-conformidade.md) | 96 Requisitos (A + AA) e 50 Recomendações (AAA) em 16 seções. |
- **Requisitos vs. Recomendações** → [Níveis de Conformidade](niveis-de-conformidade.md)

    Diferente da WCAG (que agrupa os itens em 4 princípios abstratos: *Perceptível, Operável, Compreensível e Robusto*), a **ABNT NBR 17225** organiza tudo de forma prática em **16 seções temáticas** (Imagens, Teclado, Formulários, Cores etc.), totalizando **146 itens**:

    1. **96 Requisitos (obrigatórios — Conformidade Regular):** equivalem aos níveis **A e AA** da WCAG 2.2. Para um site ser considerado em conformidade com a norma, ele deve atender a **todos** os requisitos aplicáveis.
    2. **50 Recomendações (Conformidade Aprimorada):** equivalem ao nível **AAA** da WCAG 2.2. Elevam a qualidade da experiência, mas não são obrigatórias para a conformidade básica.
- **Itens Críticos / Problemáticos (Anexo da NBR 17225)**

    A norma destaca recursos que frequentemente bloqueiam pessoas com deficiência no Brasil:

    - 🤖 [CAPTCHA](captcha.md): desafios exclusivamente visuais (ex: "clique nos semáforos") sem alternativa em áudio ou validação não sensorial.
    - 🧑‍🦯 **Reconhecimento Facial / Biometria:** provas de vida (*liveness*) que exigem movimentos faciais complexos sem instrução por voz ou método alternativo.
    - 🧱 **Componentes Customizados:** menus, abas, carrosséis e modais feitos com &lt;div&gt; que não expõem função, nome e estado para tecnologias assistivas (ver [ARIA](aria.md)).
    - 📄 **PDFs e documentos para download:** arquivos escaneados como imagem, sem texto selecionável nem marcação (tags) de leitura.
    - 🔌 **Conteúdo de Terceiros:** widgets, chats, players, mapas e plug-ins incorporados, cuja acessibilidade continua sendo responsabilidade de quem publica o site.

# 🔗 Links Oficiais

- [Catálogo da ABNT](https://www.abnt.org.br) — aquisição e consulta oficial das normas.
- [Projeto da Norma ABNT no Ceweb.br](https://ceweb.br/projetos/norma-abnt/) — histórico e materiais do projeto da NBR 17225.
- [Plataforma Todos na Web](https://todosnaweb.ceweb.br/) — conteúdos e capacitação em acessibilidade web.
- [eMAG — Modelo de Acessibilidade em Governo Eletrônico (Gov.br)](https://emag.governoeletronico.gov.br/) — referência para sites públicos brasileiros.

# 📋 Referência Rápida por Seção

<aside markdown="1">
✅

O checklist operacional (com Resultado, Severidade e Evidências) fica na página [Auditoria: Site dos Correios](auditoria-site-dos-correios.md). As tabelas abaixo são a referência original por seção, mantida para consulta.

</aside>

### Seção 5.1 — Interação por Teclado e Foco

| Cód. NBR (WCAG) | Tipo | O que testa | Como testar na prática |
| --- | --- | --- | --- |
| **5.1.1** *(2.4.7 AA)* | Requisito | **Indicador de foco visível:** Todos os elementos interativos exibem contorno claro ao receber foco. | Pressione Tab repetidamente pela página. Verifique se você sempre sabe onde o cursor está posicionado visualmente. |
| **5.1.3** *(2.4.11 AA)* | Requisito | **Elemento em foco parcialmente visível (Não obscurecido):** O item focado não fica escondido atrás de banners fixos. | Navegue com Tab com o banner de cookies, botão de WhatsApp/chat ou menu fixo (*sticky header*) abertos. O elemento focado não pode ficar coberto por eles. |
| **5.1.4** *(2.4.3 A)* | Requisito | **Ordem de foco:** A navegação segue uma sequência lógica e previsível. | Use Tab do topo ao rodapé. O foco deve seguir a ordem visual de leitura (esquerda p/ direita, cima p/ baixo) sem pular erraticamente. |
| **5.1.8 / 5.1.9** *(1.4.13 AA)* | Requisito | **Conteúdo adicional em foco/hover:** Menus suspensos ou *tooltips* podem ser fechados com Esc e permitem mover o mouse sobre eles sem sumir. | Abra um submenu ou *tooltip* via teclado ou mouse. Pressione Esc para ver se fecha sem mover o foco e passe o mouse sobre o texto aberto. |
| **5.1.12 / 5.1.13** *(2.1.1 A / 2.1.2 A)* | Requisito | **Operação por teclado e Sem armadilhas:** Tudo funciona sem mouse e o foco nunca fica preso. | Tente usar carrosséis, modais, filtros e menus só com Tab, Enter, Espaço e Esc. Se abrir um modal, garanta que é possível sair dele pelo teclado. |

### Seção 5.2 — Imagens

| Cód. NBR (WCAG) | Tipo | O que testa | Como testar na prática |
| --- | --- | --- | --- |
| **5.2.1** *(1.1.1 A)* | Requisito | **Texto alternativo para imagens de conteúdo:** Imagens informativas possuem descrição equivalente. | Inspecione as tags &lt;img&gt; ou rode o WAVE. Verifique se o atributo alt transmite a mesma informação visual da imagem. |
| **5.2.2** *(1.1.1 A / 2.4.4 A)* | Requisito | **Texto alternativo para imagens funcionais:** Imagens que são links ou botões descrevem a ação/destino, não a aparência. | Em ícones de lupa, redes sociais ou logotipos clicáveis, verifique se o alt ou aria-label diz "Buscar" ou "Ir para página inicial" (e não "ícone lupa.png"). |
| **5.2.3** *(1.1.1 A)* | Requisito | **Imagens decorativas ocultas:** Imagens puramente estéticas devem ser ignoradas por leitores de tela. | Inspecione grafismos, divisores e fotos ilustrativas genéricas. Devem possuir alt="" (vazio) ou aria-hidden="true". |
| **5.2.5** *(1.4.5 AA)* | Requisito | **Imagens de texto:** Não utilizar imagens contendo textos embutidos (exceto logos). | Tente selecionar o texto dos banners promocionais com o mouse. Se não for selecionável (for um JPG/PNG com texto achatado), reprove o item. |

### Seções 5.3 e 5.4 — Cabeçalhos e Regiões (Estrutura)

| Cód. NBR (WCAG) | Tipo | O que testa | Como testar na prática |
| --- | --- | --- | --- |
| **5.3.1 / 5.3.2** *(1.3.1 A)* | Requisito | **Semântica e uso de cabeçalhos:** Títulos visuais utilizam tags &lt;h1&gt; a &lt;h6&gt; reais no código. | Use a extensão *HeadingsMap* ou WAVE. Verifique se textos grandes que dividem seções são realmente &lt;h1-h6&gt; e não apenas &lt;div/p&gt; estilizados. |
| **5.3.5** *(1.3.1 A / 2.4.6 AA)* | Requisito | **Estrutura hierárquica de cabeçalhos:** Os títulos seguem ordem lógica sem pular níveis. | Verifique a árvore de títulos: existe um &lt;h1&gt; principal? Os subtítulos seguem &lt;h2&gt;, &lt;h3&gt; sem saltar diretamente de &lt;h1&gt; para &lt;h4&gt;? |
| **5.4.1 / 5.4.2** *(1.3.1 A)* | Requisito | **Semântica de regiões (*Landmarks*):** Áreas da página estão demarcadas corretamente. | Inspecione o HTML procurando pelas tags semânticas: &lt;header&gt;, &lt;nav&gt;, &lt;main&gt;, &lt;aside&gt; e &lt;footer&gt;. |
| **5.4.5** *(1.3.1 A)* | Requisito | **Regiões identificadas unicamente:** Regiões repetidas possuem nomes diferenciados. | Se houver duas tags &lt;nav&gt; (ex: menu principal e menu do rodapé), verifique se possuem aria-label distintos distinguindo cada uma. |

### Seções 5.5 e 5.6 — Listas e Tabelas

| Cód. NBR (WCAG) | Tipo | O que testa | Como testar na prática |
| --- | --- | --- | --- |
| **5.5.1 / 5.5.2** *(1.3.1 A)* | Requisito | **Semântica e uso de listas:** Agrupamentos de itens usam tags de lista adequadas. | Verifique menus, rodapés e tópicos no texto: devem usar &lt;ul&gt; (não ordenada), &lt;ol&gt; (ordenada) ou &lt;dl&gt; (definições). |
| **5.6.1 / 5.6.2** *(1.3.1 A)* | Requisito | **Semântica e uso de tabelas:** Tabelas têm cabeçalhos (&lt;th&gt;) associados às células e não são usadas para layout. | Inspecione tabelas de dados. Confira se usam &lt;table&gt;, &lt;th&gt; (com scope="col" ou row) e &lt;td&gt;, e que não existem tabelas usadas apenas para alinhar layout. |

### Seções 5.7 e 5.8 — Links, Navegação, Botões e Controles

| Cód. NBR (WCAG) | Tipo | O que testa | Como testar na prática |
| --- | --- | --- | --- |
| **5.7.1 / 5.7.2** *(1.3.1 A)* | Requisito | **Semântica e uso de links:** Links usam tag &lt;a href="..."&gt; e servem para navegação (ir para outra página/âncora). | Inspecione os links: possuem atributo href válido? Não são &lt;span&gt; ou &lt;div&gt; com evento onclick? |
| **5.7.4** *(2.4.4 A)* | Requisito | **Propósito do link (em contexto):** O texto do link deixa claro para onde ele leva. | Procure por links vagos como *"Clique aqui"*, *"Saiba mais"* ou *"Leia mais"*. Eles devem ter contexto programático ou textos descritivos (ex: *"Saiba mais sobre nossos planos"*). |
| **5.7.12** *(2.4.1 A)* | Requisito | **Link de salto ("Pular para o conteúdo"):** Mecanismo para pular blocos repetidos de cabeçalho/menu. | Recarregue a página e aperte Tab uma ou duas vezes. Deve surgir um link visível *"Ir para o conteúdo principal"* que, ao apertar Enter, move o foco direto para o &lt;main&gt;. |
| **5.8.1 / 5.8.2** *(1.3.1 A)* | Requisito | **Semântica e uso de botões:** Elementos que executam ações usam &lt;button&gt;. | Verifique controles que abrem modais, enviam dados ou filtram itens. Devem ser &lt;button&gt; reais no HTML. |
| **5.8.3** *(4.1.2 A)* | Requisito | **Propósito do botão (Nome acessível):** Todo botão tem nome identificável pelo leitor de tela. | Verifique botões que só têm ícone (ex: "X" de fechar modal, seta de carrossel, menu hambúrguer). Inspecione se possuem aria-label em português (ex: aria-label="Fechar janela"). |
| **5.8.6** *(2.5.8 AA)* | Requisito | **Tamanho mínimo da área de clique/toque:** Alvos interativos têm pelo menos **24x24 pixels CSS** (ou espaçamento equivalente). | Inspecione botões pequenos, paginações e ícones próximos. Verifique no DevTools se a caixa do elemento tem no mínimo 24x24px. |

### Seção 5.9 — Formulários e Entrada de Dados

| Cód. NBR (WCAG) | Tipo | O que testa | Como testar na prática |
| --- | --- | --- | --- |
| **5.9.1 / 5.9.3** *(3.3.2 A / 1.3.1 A)* | Requisito | **Rótulo de campo visível e associado:** Todo &lt;input&gt;, &lt;select&gt; ou &lt;textarea&gt; tem um &lt;label&gt; fixo e vinculado no código. | Clique em cima do texto do rótulo (ex: "E-mail"): o cursor deve entrar automaticamente dentro do campo. *Atenção: placeholder que some ao digitar não substitui &lt;label&gt;!* |
| **5.9.6** *(1.3.1 A / 3.3.2 A)* | Requisito | **Identificação de campos obrigatórios e grupos:** Campos obrigatórios são claros e grupos de opções usam &lt;fieldset&gt;/&lt;legend&gt;. | Confira se campos obrigatórios estão sinalizados claramente (não apenas por cor) e se botões de rádio (ex: "Sim / Não") têm a pergunta agrupada via &lt;fieldset&gt;. |
| **5.9.9 / 5.9.11** *(3.3.1 A / 3.3.3 AA)* | Requisito | **Identificação e sugestão em erros:** Erros de preenchimento são descritos em texto e explicam como corrigir. | Tente enviar o formulário em branco ou com e-mail inválido. A mensagem de erro deve aparecer em texto claro, vinculada ao campo (aria-describedby) e ser lida pelo leitor de tela. |
| **5.9.16** *(3.3.8 AA)* | Requisito | **Autenticação acessível (Sem teste cognitivo):** O login não exige memorizar senhas sem permitir colar ou usar gerenciador. | Na tela de login/cadastro, tente colar (Ctrl+V) uma senha no campo de senha e verifique se gerenciadores de senha do navegador funcionam normalmente. |

### Seções 5.10 e 5.11 — Apresentação e Uso de Cores

| Cód. NBR (WCAG) | Tipo | O que testa | Como testar na prática |
| --- | --- | --- | --- |
| **5.10.1** *(1.3.3 A)* | Requisito | **Características sensoriais:** Instruções não dependem apenas de forma, tamanho, cor ou posição visual. | Procure textos como *"Clique no botão verde à direita"* ou *"Veja o quadro redondo"*. A instrução deve citar também o nome do elemento. |
| **5.10.2 / 5.10.4** *(1.3.4 AA / 1.4.10 AA)* | Requisito | **Orientação de tela e Refluxo (Zoom 400%):** O site funciona na vertical/horizontal e se adapta ao zoom sem barra de rolagem horizontal. | Dê zoom de **400%** no navegador (em resolução 1280px de largura). O conteúdo deve se reorganizar em uma única coluna sem cortar textos, sobrepor caixas ou exigir rolagem lateral. |
| **5.11.1** *(1.4.1 A)* | Requisito | **Uso de cores:** A cor nunca é o único meio de transmitir uma informação, erro ou link. | Links em meio a textos possuem sublinhado? Erros de formulário têm ícone/texto além da borda vermelha? Gráficos têm rótulos além das cores? |
| **5.11.3** *(1.4.3 AA)* | Requisito | **Contraste mínimo para texto:** Proporção mínima de **4,5:1** para texto normal e **3:1** para texto grande (≥18pt ou ≥14pt negrito). | Rode o WAVE/axe e use o *Colour Contrast Analyser* em textos cinza-claro, botões, *placeholders* e textos sobre imagens de fundo. |
| **5.11.4** *(1.4.11 AA)* | Requisito | **Contraste não textual:** Proporção mínima de **3:1** para bordas de inputs, ícones e indicadores de foco. | Meça o contraste da borda dos campos de formulário, de ícones informativos e do contorno de foco em relação ao fundo da página. |

### Seções 5.12 e 5.13 — Conteúdo Textual e Codificação Semântica

| Cód. NBR (WCAG) | Tipo | O que testa | Como testar na prática |
| --- | --- | --- | --- |
| **5.12.1 / 5.12.2** *(1.4.12 AA)* | Requisito | **Espaçamento de texto:** Entrelinhas de pelo menos 1,5x a fonte e espaço entre parágrafos de 2x (ou suporte à customização sem quebrar o layout). | Aplique o *bookmarklet* "Text Spacing" para forçar entrelinhas de 1.5x e espaçamento de letras de 0.12em. Veja se nenhum texto fica cortado dentro de botões ou cards. |
| **5.12.7** *(3.1.5 AAA)* | Recomendação | **Linguagem simples:** Textos claros, sem jargões desnecessários, siglas explicadas na primeira menção (ABNT NBR ISO 24495-1). | Leia textos institucionais, termos e avisos de erro: são diretos e compreensíveis por pessoas com diferentes níveis de escolaridade? |
| **5.13.1** *(2.4.2 A)* | Requisito | **Título da página (&lt;title&gt;):** Cada página possui um título único e descritivo na aba do navegador. | Olhe a aba do navegador em diferentes páginas (Home, Contato, Produto). O &lt;title&gt; descreve a página atual seguido do nome do site? |
| **5.13.2 / 5.13.3** *(3.1.1 A / 3.1.2 AA)* | Requisito | **Idioma da página e de trechos:** O idioma principal e expressões estrangeiras estão declarados no código. | Inspecione a tag raiz &lt;html lang="pt-BR"&gt;. Se houver parágrafos ou citações em outro idioma (ex: inglês), verifique se possuem lang="en" na tag do elemento. |
| **5.13.11** *(4.1.3 AA)* | Requisito | **Mensagens de status:** Avisos dinâmicos ("Item adicionado ao carrinho", "3 resultados encontrados") são anunciados sem mudar o foco. | Com o leitor de tela ligado, acione uma busca ou filtro dinâmico. O leitor deve ler o aviso automaticamente (uso de role="status", role="alert" ou aria-live). |

### Seções 5.14, 5.15 e 5.16 — Áudio/Vídeo, Animação e Tempo

| Cód. NBR (WCAG) | Tipo | O que testa | Como testar na prática |
| --- | --- | --- | --- |
| **5.14.1** *(1.2.1 A)* | Requisito | **Alternativa em texto para áudio:** Podcasts ou áudios gravados possuem transcrição textual completa. | Verifique se há um botão ou texto logo abaixo de players de áudio com a transcrição integral das falas. |
| **5.14.2 / 5.14.4** *(1.2.2 A / 1.2.5 AA)* | Requisito | **Legendas descritivas e Audiodescrição em vídeos:** Vídeos possuem legendas sincronizadas e descrição das informações visuais. | Assista ao vídeo sem som (as legendas cobrem falas e sons importantes?). Depois, ouça o vídeo sem olhar para a tela (tudo que aparece só em texto na tela é narrado ou há faixa de audiodescrição?). |
| **5.14.7** *(1.4.2 A)* | Requisito | **Controle de áudio automático:** Nenhum som inicia sozinho por mais de 3 segundos sem botão claro para pausar/silenciar. | Abra a página e observe se algum vídeo ou música começa a tocar com áudio ativo automaticamente. |
| **5.15.1 / 5.15.3** *(2.2.2 A / 2.3.1 A)* | Requisito | **Controle de animações e Limite de flashes:** Carrosséis automáticos (>5s) têm botão de pausa; nada pisca mais de 3 vezes por segundo. | Se houver banner rotativo ou animação contínua, verifique se existe botão "Pausar" operável por teclado e se não há efeitos estroboscópicos. |
| **5.16.2** *(2.2.1 A)* | Requisito | **Limite de tempo ajustável:** Sessões que expiram avisam o usuário antes e permitem estender o tempo com um comando simples. | Em áreas logadas ou checkouts com *timeout*, verifique se o sistema emite um alerta acessível permitindo renovar o tempo antes de desconectar. |

### Anexo Especial da NBR 17225 — Itens Críticos / Problemáticos

A norma brasileira destaca uma seção exclusiva para recursos que frequentemente bloqueiam pessoas com deficiência no Brasil:

| Item Crítico | O que testa | Como testar na prática |
| --- | --- | --- |
| **CAPTCHA** | Desafios de segurança não podem ser exclusivamente visuais (ex: clicar em semáforos) sem alternativa acessível. | Verifique se o CAPTCHA é invisível/comportamental (ex: Cloudflare Turnstile / reCAPTCHA v3) ou se oferece alternativa em áudio/lógica acessível por teclado e leitor de tela. |
| **Reconhecimento Facial / Biometria** | Sistemas de prova de vida (*liveness*) não podem exigir movimentos oculares/faciais complexos sem alternativa ou instrução por voz. | Se o site solicita selfie ou biometria, verifique se há guia sonoro claro para pessoas cegas e método alternativo caso a deficiência impeça o enquadramento padrão. |
| **Intérprete de Libras e Documentos PDF** | Arquivos disponíveis para download (PDFs, planilhas) também devem ser acessíveis (texto selecionável, tags de leitura). | Baixe um PDF do site: tente selecionar o texto (não pode ser imagem escaneada) e verifique as propriedades de marcação de acessibilidade do documento. |

### 🛠️ Ferramentas Indicadas (detalhado)

- **Varredura Automática (Extensões de Navegador):** instale o **axe DevTools**, **WAVE Evaluation Tool** ou use o **Google Lighthouse** (aba Inspecionar do Chrome).
- **Teste Manual de Teclado:** deixe o mouse de lado. Use Tab (avançar), Shift + Tab (voltar), Enter e Espaço (acionar botões/links), Setas (menus/radios) e Esc (fechar modais).
- **Teste de Leitor de Tela:** no Windows, utilize o **NVDA** (gratuito); no Mac/iPhone, use o **VoiceOver** (Cmd + F5); no Android, use o **TalkBack**.
- **Verificador de Contraste e Zoom:** utilize o **Colour Contrast Analyser (CCA)** ou o seletor de cores do Chrome DevTools. Teste a página aplicando zoom do navegador em **200%** e **400%**.

**Legenda usada nas tabelas:** ✅ C (Conforme), ❌ NC (Não Conforme), ⚪ N/A (Não se aplica).

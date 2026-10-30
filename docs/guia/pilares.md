# Os 4 Pilares da Acessibilidade Digital

O Guia divide a aplicação prática da acessibilidade digital em quatro frentes multidisciplinares essenciais:

---

## 1. Gestão de Projetos

A acessibilidade não pode ser tratada como um mero acessório ou etapa final de homologação. Ela exige maturidade gerencial e planejamento:

1. **Acessibilidade desde o Início (*Shift Left*):** Não deixar para aplicar acessibilidade no final da entrega como se fosse uma *feature* opcional ou uma correção de bugs. O custo de refazer uma aplicação inacessível é expressivamente maior do que planejar a arquitetura acessível desde a concepção.
2. **Cultura Multidisciplinar:** Acessibilidade não é responsabilidade exclusiva de quem coda. Ela envolve Gestão, Recursos Humanos, Design, Conteúdo, Testes de Qualidade (QA), Jurídico e Liderança.
3. **Alerta contra Plugins Mágicos ("Overlays"):** O guia condena fortemente a ideia de que instalar um botão flutuante ou um plugin milagroso resolve a acessibilidade de um website. A acessibilidade real reside na qualidade estrutural do código HTML, semântica e ergonomia do design, e não em scripts sobrepostos de terceiros.
4. **Testes com Usuários Reais:** Testes automatizados cobrem apenas uma fração dos erros (em torno de 30% a 40%). É indispensável realizar testes manuais de navegação por teclado e envolver pessoas com deficiência real na validação.

---

## 2. Design (UI / UX)

A interface deve ser ergonomicamente amigável e adaptável às mais diversas condições de visualização:

1. **Design Responsivo e Mobile First:** A interface deve se reorganizar fluidamente para telas de desktop e dispositivos móveis, suportando zoom de até **200%** sem quebrar o layout nem gerar barra de rolagem horizontal para leitura.
2. **Uso Consciente da Cor:** Nunca transmitir informação dependendo exclusivamente da cor (como usar apenas verde e vermelho para aprovação/reprovação, o que exclui daltônicos). A cor deve vir sempre acompanhada de texto explícito ou ícones de apoio.
3. **Contraste Mínimo:** Garantir contraste suficiente entre a cor do texto e a cor de fundo:
    * Proporção mínima de **4,5:1** para texto normal.
    * Proporção mínima de **3:1** para textos grandes (acima de 18pt ou 14pt negrito) e elementos gráficos funcionais.
4. **Área de Toque/Clique Ampla:** Elementos clicáveis precisam de área física confortável para facilitar o acionamento por pessoas com tremores ou limitações motoras:
    * Mínimo de **44x44 pixels** em interfaces desktop.
    * Mínimo de **48x48 pixels** em dispositivos móveis (*touchscreen*).
5. **Tipografia e Parágrafos:** Fontes limpas e legíveis, blocos de texto com média de até 80 caracteres por linha e alinhamento preferencialmente **à esquerda** (evitando texto justificado, que cria "rios brancos" e dispersa a leitura).

---

## 3. Desenvolvimento Web (Front-End)

A engenharia da página deve garantir que navegadores e tecnologias assistivas compreendam perfeitamente a árvore de acessibilidade:

1. **Semântica HTML Nativa:** O pilar mais importante da programação acessível. Usar elementos nativos (`<button>`, `<a>`, `<main>`, `<header>`, `<nav>`, `<section>`). Nunca transformar uma `<div>` genérica em botão se você já possui a tag `<button>` com comportamento acessível nativo.
2. **Navegação 100% por Teclado:** Todas as funcionalidades utilizáveis com o mouse precisam ser acionáveis com o teclado (`Tab`, `Shift+Tab`, `Enter`, `Espaço` e setas direcionais).
3. **Indicador de Foco Visível (`:focus`):** O elemento focado deve apresentar uma moldura ou contorno visual nítido para que o usuário saiba exatamente onde está na tela.
4. **Ordem Lógica e Previsível:** A sequência de foco e a leitura dos leitores de tela devem seguir uma ordem lógica natural (de cima para baixo, da esquerda para a direita).
5. **Cuidados com Modais (*Pop-ups*):** Evitar abrir janelas modais desnecessárias. Se forem indispensáveis:
    * Devem permitir fechamento pela tecla `Esc`.
    * O foco do teclado deve ficar retido ("preso") no modal enquanto aberto.
    * Ao fechar, o foco deve retornar ao elemento que disparou a abertura.
6. **Formulários e Tratamento de Erros:** Todo `<input>` precisa de uma `<label>` explicitamente associada via `for`/`id`. Mensagens de erro devem ser claras, próximas ao campo com falha e anunciadas por leitores de tela via atributos ARIA (`aria-describedby`, `aria-live`).
7. **Controle de Mídia e Movimento:** Carrosséis, vídeos e animações automáticas precisam fornecer controles visíveis para pausar, parar ou desativar o movimento, mitigando sobrecargas cognitivas e gatilhos vestibulares.

---

## 4. Produção de Conteúdo e Comunicação

A clareza e empatia na transmissão das mensagens são vitais para a compreensão universal:

1. **Terminologia Adequada:** Utilizar o termo consagrado **"Pessoa com Deficiência (PcD)"**. Evitar expressões ultrapassadas como "portador de deficiência", "deficiente" ou "pessoa especial".
2. **Linguagem Simples (*Plain Language*):** Redigir textos na ordem direta (*sujeito + verbo + predicado*), com períodos curtos (15 a 20 palavras), vocabulário acessível e sem jargões desnecessários.
3. **Descrição de Imagens (`alt`):** Imagens com valor informativo devem possuir texto alternativo descritivo e contextualizado. Imagens meramente decorativas devem receber `alt=""` para que sejam ignoradas por leitores de tela.
4. **Links Claros e Autoexplicativos:** Evitar textos genéricos como "clique aqui", "saiba mais" ou o endereço cru da URL. O texto do link deve descrever claramente o destino (exemplo: *"Consulte o Edital de Matrícula 2026.2"*).
5. **Multimídia Acessível:** Vídeos institucionais/educativos devem conter legendas descritivas (*Open* ou *Closed Caption*), janela de Libras (preferencialmente à direita da tela) e audiodescrição. Arquivos de áudio (como podcasts) necessitam de transcrição textual completa.
6. **Hashtags em CamelCase:** Em redes e artigos, utilizar letras maiúsculas no início de cada palavra composta (ex: `#AcessibilidadeParaTodos`), viabilizando a leitura individualizada por sintetizadores de voz.

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| `1.0` | 29/10/2026 | Consolidação dos 4 pilares práticos do Guia de Acessibilidade | Grupo 04 | Grupo 04 |

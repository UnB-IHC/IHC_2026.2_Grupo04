---
name: IHC · Grupo 04
description: Portal acadêmico de leitura e consulta da UnB, semestre 2026.2.
colors:
  ink: "#172f40"
  muted: "#526570"
  accent: "#006b83"
  accent-hover: "#004e63"
  paper: "#ffffff"
  ground: "#f5f8fa"
  soft: "#eaf4f7"
  line: "#dbe5ea"
  dark: "#12374d"
  focus: "#bd5a00"
  preview-detail: "#b6e5ed"
  preview-line: "#466576"
  slate-ink: "#e4edf3"
  slate-muted: "#adbdc7"
  slate-accent: "#83d7e8"
  slate-accent-hover: "#b9edf4"
  slate-paper: "#142630"
  slate-ground: "#101f28"
  slate-soft: "#1c3543"
  slate-line: "#324954"
  slate-focus: "#ffc77d"
typography:
  display:
    fontFamily: "Manrope, sans-serif"
    fontSize: "3.65rem"
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: "-.04em"
  headline:
    fontFamily: "Manrope, sans-serif"
    fontSize: "2.15rem"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "-.025em"
  title:
    fontFamily: "Manrope, sans-serif"
    fontSize: "1.4rem"
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: "-.025em"
  body:
    fontFamily: "Manrope, sans-serif"
    fontSize: ".85rem"
    lineHeight: 1.8
  label:
    fontFamily: "Manrope, sans-serif"
    fontSize: ".65rem"
    fontWeight: 700
rounded:
  inline-code: "4px"
  control: "6px"
  table: "8px"
  panel: "12px"
spacing:
  small: ".4rem"
  medium: ".8rem"
  content: "1rem"
  section: "1.5rem"
components:
  button-primary:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.paper}"
    rounded: "{rounded.control}"
    padding: ".8rem 1.1rem"
  button-primary-hover:
    backgroundColor: "{colors.accent-hover}"
  field:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.control}"
    padding: ".6rem .7rem"
  nav-active:
    backgroundColor: "{colors.soft}"
    textColor: "{colors.accent}"
    rounded: "{rounded.control}"
  preview:
    backgroundColor: "{colors.dark}"
    textColor: "{colors.paper}"
    rounded: "{rounded.panel}"
    padding: "1.8rem 2rem 1.4rem"
---

# Sistema visual: IHC · Grupo 04

## Overview

Portal acadêmico da disciplina de Interação Humano-Computador da Universidade de Brasília, Grupo 04, semestre 2026.2. A apresentação prioriza leitura, orientação e consulta: fundo branco, azul profundo, ciano e espaço entre blocos. A referência estrutural é o A11yG10 indicado pela monitoria; a identidade e a página inicial são próprias do grupo.

O sistema está em `mkdocs.yml`, `docs/stylesheets/portal.css`, `docs/javascripts/portal.js`, `overrides/main.html` e `hooks/apresentacao.py`. Este documento descreve a implementação atual; não representa uma auditoria completa de conformidade WCAG.

## Colors

Os tokens do frontmatter correspondem às propriedades `--portal-*` em `portal.css`. `ink` é texto principal; `muted`, informação secundária; `accent` e `accent-hover`, links e ações; `paper`, superfície principal; `ground`, áreas de apoio; `soft`, destaques; `line`, divisórias; `focus`, contorno de foco.

O tema claro usa os nomes sem prefixo. O tema escuro (`slate`) substitui esses papéis pelos tokens `slate-*`. `dark` permanece no painel de apresentação da home nos dois temas, acompanhado de branco, `preview-detail` e `preview-line`. Ao mudar uma cor, altere sua propriedade na folha de estilos e atualize este registro. Preserve as combinações de texto, fundo e foco em ambos os temas.

## Typography

Manrope é servida localmente por `docs/assets/fonts/manrope-regular.ttf` e `manrope-bold.ttf`, com licença em `docs/assets/fonts/OFL.txt`. O carregamento usa `font-display: swap` e fallback `sans-serif`. A configuração desativa a fonte remota do tema. O primeiro arquivo atende os pesos declarados 400–500; o segundo, 600–800. Código usa `Consolas, monospace`.

A escala não segue uma razão única. O frontmatter registra título da home, H1 de conteúdo, H2, corpo e rótulos. H3 usa 1.05rem, peso 700 e entrelinha 1.4. A navegação usa .7rem e entrelinha 1.55; tabelas, .72rem e 1.65. O texto introdutório da home limita-se a 41ch; a apresentação original, a 74ch. Mantenha os valores em rem, sem presumir uma conversão fixa para pixels, pois a base vem do tema.

## Layout

Há cinco entradas principais: **Início, Guia, Avaliação, Usabilidade e Projeto**. `mkdocs.yml` define seus rótulos, agrupamentos e arquivos. As páginas internas têm navegação lateral com grupos recolhíveis, conteúdo central e índice de títulos quando aplicável. O menu vira uma gaveta nas larguras menores. A home tem uma composição própria em `overrides/main.html`, sem índice lateral: introdução e painel POUR, caminhos do projeto e apresentação/equipe.

A grade geral limita-se a 72rem; a home, a 63rem; a apresentação original, a 50rem. A abertura usa duas colunas (1.15fr / 1fr) com intervalo de 4rem. Chamadas e fichas de critérios usam duas colunas. Equipe usa quatro colunas.

Os ajustes responsivos estão em 76.25em (home ampla), 76.234375em (gaveta e margens menores), 60em (compactação) e 40em (celular). Até 40em, abertura, caminhos, chamadas, fichas e campos ficam em uma coluna; a equipe passa a duas. O título da home usa `clamp(1.9rem, 10.6vw, 2.4rem)`; H1 interno passa a 1.65rem e corpo a .8rem. Tabelas extensas rolam em sua própria região. A impressão remove navegação, ações, filtros e painel de apresentação.

## Elevation & Depth

A separação vem de fundos suaves e linhas de 1px. Cabeçalho, títulos de navegação e avisos não usam sombra. Preserve essa apresentação plana; o destaque azul da home é um contraste de superfície, sem simular volume.

## Shapes

Os cantos seguem os quatro raios do frontmatter: código pequeno, controles, tabelas e painéis. Retratos são circulares. As divisórias organizam listas e metadados; não é necessário transformar cada link em um cartão.

## Components

- **Navegação:** seção ativa com linha ciano nas abas; página ativa com fundo suave e peso 700 no menu. Caminho de localização nas páginas internas e links anterior/próximo no rodapé. A busca global e a troca de tema são do tema base.
- **Ações:** botão ciano para entrar no guia e link textual para o checklist. O hover altera o fundo em 160ms, com `ease-out`. O foco visível global tem contorno de 3px e afastamento de 4px. Preserve rótulos textuais e não dependa só da cor.
- **Painel da home:** fundo azul profundo, identificação IHC 04 e quatro links para os princípios POUR. O painel mantém sua combinação própria nos dois temas.
- **Chamadas e fichas:** blocos `aside` consecutivos são agrupados em grade; fichas de critérios exibem pares de termo/descrição, com “Como Testar” em destaque. A autoria de origem continua visível quando presente.
- **Tabelas:** cabeçalho em fundo neutro, linhas divisórias e região de rolagem com nome e foco de teclado. O JavaScript envolve tabelas ainda não tratadas; o checklist já recebe a região no processamento da página.
- **Checklist:** busca local por texto, código ou palavra, filtro por princípio WCAG, contagem anunciada e botão “Limpar filtros”. A busca ignora maiúsculas e acentos, combina todas as palavras e atua apenas sobre as linhas da página. São 32 critérios registrados como pendentes, não resultados de uma avaliação concluída. Sem JavaScript, os filtros permanecem ocultos e a tabela completa continua disponível. Ao atualizar, mantenha o Markdown e `docs/referencia/dados/checklist-unificado.csv` correspondentes, na mesma ordem; o processamento verifica a quantidade de linhas.
- **Teclado e navegação instantânea:** os controles de menu e busca recebem rótulos, estado expandido e ativação por Enter/Espaço. Escape fecha a gaveta ou busca e devolve o foco ao controle. A preparação se repete após a troca instantânea de página, sem duplicar eventos. O link de salto da home aponta para seu título.
- **Movimento reduzido:** `prefers-reduced-motion: reduce` zera a duração das animações e transições e usa rolagem automática. Novos efeitos devem respeitar essa regra.

## Do's and Don'ts

- Preserve o conteúdo original de Marcus e João. As adaptações de hierarquia, agrupamento, metadados e âncoras acontecem na renderização, em `hooks/apresentacao.py`, sem reescrever os arquivos de origem.
- Acrescente páginas no grupo adequado de `mkdocs.yml` e reutilize os padrões existentes antes de criar novos estilos.
- Mantenha texto editorial no Markdown; a estrutura exclusiva da home fica em `overrides/main.html`. Use caminhos relativos e o filtro de URL do tema nos links do template para respeitar o subdiretório do site.
- Atualize este documento ao mudar os tokens. Confira a mesma alteração no modo claro, no escuro, no celular e com teclado.
- Mantenha as fontes e a licença locais, a hierarquia de títulos, o foco visível e a leitura das tabelas sem filtros.
- Não apresente critérios pendentes como testes aprovados nem atribua conformidade completa apenas à aparência da interface.
- Não copie a identidade da referência nem acrescente sombras, cores ou efeitos sem função de leitura ou orientação.

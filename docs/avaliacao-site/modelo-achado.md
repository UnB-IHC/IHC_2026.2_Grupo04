---
title: Registro de achados
---
# Registro de achados

Use um registro por problema. Quando o mesmo comportamento aparecer em várias páginas, reúna as ocorrências no mesmo achado e identifique as URLs. Consulte o [checklist de Nielsen](checklist-nielsen.md) e o [exemplo da busca de CEP](inspecao-busca-cep.md).

## Campos do registro

| Campo | Informação necessária |
| --- | --- |
| Identificação | Código único, título, data e responsável pelo registro. |
| Contexto | URL exata, tarefa, navegador, dispositivo e condições relevantes. |
| Reprodução | Entrada utilizada e passos para chegar ao comportamento. |
| Observação | O que a interface apresentou, sem atribuir uma causa que não foi investigada. |
| Comportamento esperado | O que permitiria realizar a tarefa com mais clareza ou controle. |
| Evidência | Captura da tela e, quando útil, trecho da estrutura da página. |
| Fundamentação | Heurística principal e explicação de sua relação com o problema. |
| Severidade proposta | Nota de 0 a 4, impacto, repetição e possibilidade de contorno. |
| Recomendação | Mudança que responde ao comportamento registrado. |
| Limites | Cenários não executados, dependências e pontos a confirmar. |
| Revisão | Situação da revisão, responsável e data, quando ocorrer. |

## Modelo para copiar

Substitua os campos entre colchetes antes de publicar um achado. Não inclua senhas, CPF, dados de participantes ou informações particulares de encomendas nas evidências.

```markdown
## [Código] - [Título do achado]

- Data e responsável pelo registro: [informar]
- URL: [endereço completo]
- Tarefa: [objetivo da navegação]
- Ambiente: [navegador, dispositivo e condições]
- Entrada usada: [dado público ou de teste]
- Estado: [observado individualmente / revisado pelo grupo]

### Passos para reproduzir

1. [Ação inicial]
2. [Ação seguinte]
3. [Ponto em que aparece o comportamento]

### Comportamento observado

[Descrever o que aconteceu.]

### Comportamento esperado e fundamentação

[Descrever a alternativa esperada e relacionar à heurística.]

- Heurística principal: [H1 a H10]
- Relações complementares: [informar somente se justificadas]

### Evidência

[Link para captura e descrição do que ela demonstra.]

### Severidade proposta e recomendação

- Nota: [0 a 4]
- Justificativa: [impacto, repetição e possibilidade de contorno]
- Recomendação: [mudança específica]
- Limites: [o que não foi verificado]
- Revisão: [pendente ou identificação de quem revisou e quando]
```

## Critérios de revisão

Confirme se outra pessoa consegue reproduzir o relato, se a captura sustenta a observação e se a recomendação responde ao problema. Um cenário não executado fica como **não verificado**, sem uma nota de severidade. Use a [escala e as referências do checklist](checklist-nielsen.md#severidade-proposta) para fundamentar a classificação.

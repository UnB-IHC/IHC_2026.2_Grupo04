# Resultados por Tarefa & Escore SUS

Esta seção consolida as métricas quantitativas e os desfechos observados durante a execução dos quatro cenários de uso com o participante **P1**, além da mensuração de usabilidade percebida através da **System Usability Scale (SUS)**.

???+ info "Nota Metodológica"
    Como o teste foi conduzido com um único participante representativo, os dados devem ser interpretados como **indicativos de usabilidade**, e não como generalizações estatísticas sobre todo o público dos Correios.

---

## 1. Métricas de Desempenho por Tarefa

A classificação dos desfechos adotou estritamente as categorias metodológicas definidas pela disciplina (Rubin & Chisnell, 2008; Nielsen & Budiu, 2001):

* **Sucesso sem ajuda:** O participante atinge o critério de sucesso sozinho, sem nenhuma intervenção.
* **Sucesso com ajuda:** O participante atinge o objetivo recebendo uma única dica/orientação da moderação.
* **Falha:** O participante desiste, excede o tempo-limite ou recebe mais de uma dica.

### Tabela Consolidada de Execução

| Tarefa / Cenário | Desfecho Observado | Tempo Estimado | Erros / Desvios | Dicas da Moderação |
| :--- | :---: | :---: | :---: | :---: |
| **Cenário 1:** Cálculo de Preço e Prazo | **Sucesso com ajuda** | ~2 min 40 s | Dificuldade com opções de caixa postal e validação por captcha visual. | 1 intervenção orientadora para prosseguir o fluxo. |
| **Cenário 2:** Busca de CEP por Endereço | **Sucesso com ajuda** | ~2 min 10 s | Navegação confusa entre ferramentas de endereço e menus redundantes. | 1 orientação inicial de direcionamento. |
| **Cenário 3:** Localização de Agência e Horário | **Sucesso sem ajuda** | ~3 min 15 s | Exploração errática de menus de atendimento/logística e ajuste de raio de 5 km. | Nenhuma (concluída autonomamente após longo percurso). |
| **Cenário 4:** Rastreamento de Encomenda | **Sucesso sem ajuda** | ~1 min 20 s | Leve hesitação visual inicial na localização do campo de busca. | Nenhuma. |

---

### Cálculo da Taxa de Sucesso

Conforme a fórmula padrão de Nielsen e Budiu (2001), calcula-se o percentual de tarefas completadas de forma totalmente autônoma:

> **Taxa de Sucesso sem ajuda** = (Tarefas com sucesso sem ajuda ÷ Total de tarefas) = **2 ÷ 4 = 50%**

* **Sucesso sem ajuda:** 50% (2 tarefas)
* **Sucesso com ajuda:** 50% (2 tarefas)
* **Falhas / Desistências:** 0% (0 tarefas)

---

## 2. Avaliação da Usabilidade Percebida (Escore SUS)

O questionário **SUS (System Usability Scale)** foi aplicado imediatamente após o término do Cenário 4, utilizando a versão transcultural em português validada por Lourenço, Carmona e Lopes (2022). O formulário é composto por 10 afirmações avaliadas em escala Likert de 1 (*Discordo totalmente*) a 5 (*Concordo totalmente*).

### Procedimento de Cálculo (Brooke, 1996; Sauro, 2011)

1. Para os **itens ímpares** (perguntas positivas: 1, 3, 5, 7, 9), subtrai-se 1 da pontuação:  
   **Contribuição = Resposta − 1**
2. Para os **itens pares** (perguntas negativas: 2, 4, 6, 8, 10), subtrai-se a pontuação de 5:  
   **Contribuição = 5 − Resposta**
3. Soma-se o resultado das 10 contribuições e multiplica-se por **2,5**, obtendo-se uma pontuação global na escala de **0 a 100**.

???+ warning "Atenção Metodológica sobre o Escore"
    O valor final da escala SUS **não representa porcentagem** nem taxa de acerto; trata-se de um índice de percentil padronizado de percepção de usabilidade (Sauro, 2011). A média histórica de mercado para sistemas aceitáveis gira em torno de 68 pontos.

### Resultados Obtidos pelo Participante P1

| Nº | Afirmação Avaliada | Resposta Bruta (1 a 5) | Cálculo da Contribuição |
| :---: | :--- | :---: | :---: |
| **1** | Eu acho que gostaria de usar esse sistema frequentemente. | 2 | 2 − 1 = **1** |
| **2** | Eu achei esse sistema desnecessariamente complexo. | 4 | 5 − 4 = **1** |
| **3** | Eu achei esse sistema fácil de usar. | 2 | 2 − 1 = **1** |
| **4** | Eu achei que precisaria de ajuda de uma pessoa técnica para ser capaz de usar esse sistema. | 3 | 5 − 3 = **2** |
| **5** | Eu achei que as várias funções desse sistema foram bem integradas. | 2 | 2 − 1 = **1** |
| **6** | Eu acho que o sistema apresenta muita inconsistência. | 4 | 5 − 4 = **1** |
| **7** | Eu imagino que a maioria das pessoas pode aprender a usar esse sistema rapidamente. | 3 | 3 − 1 = **2** |
| **8** | Eu achei esse sistema muito pesado para usar. | 4 | 5 − 4 = **1** |
| **9** | Eu me senti muito seguro usando o sistema. | 3 | 3 − 1 = **2** |
| **10** | Eu precisei aprender muitas coisas antes que pudesse utilizar esse sistema. | 3 | 5 − 3 = **2** |
| **Total** | **Soma das contribuições individuais** | — | **14** |

### Escore Final do Sistema

> **Escore SUS** = 14 × 2,5 = **35,0**

### Interpretação do Resultado

O escore de **35,0** situa o sítio dos Correios em um patamar classificado como **"Marginal / Baixo"** (Grau F na escala Sauro & Lewis), indicando sérios problemas de usabilidade, sobrecarga cognitiva e inconsistência percebida pelo usuário real, o que corrobora plenamente os relatos qualitativos de "interface contraintuitiva" e "excesso de poluição visual" colhidos na entrevista final.

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| `1.0` | 29/10/2026 | Estrutura de métricas do teste | Grupo 04 | Grupo 04 |
| `2.0` | 10/11/2026 | Registro de taxas de sucesso dos 4 cenários e cálculo detalhado do escore SUS | Grupo 04 | Grupo 04 |

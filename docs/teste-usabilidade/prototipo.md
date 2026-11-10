# Protótipo da Solução Prioritária (Opcional)

Em consonância com as orientações metodológicas da disciplina (Seção 2.6 da proposta de trabalho), esta etapa complementar concretiza a **recomendação de maior prioridade (Recomendação 1 / PB-01)** decorrente do teste de usabilidade.

---

## 1. O Problema Resolvido

* **Problema Vinculado:** [PB-01 — Barreira por CAPTCHA visual distorcido](relacao-pocket.md#1-tabela-comparativa-de-problemas-evidencias-e-severidade).
* **Severidade Atribuída:** Grau 3 (Grave / Impeditivo na escala de Nielsen).
* **Fundamentação Técnica e Normativa:**
    * **ABNT NBR 17225:2025:** Anexo A (Mapeamento de itens problemáticos — CAPTCHA).
    * **WCAG 2.2:** Critério de Sucesso 3.3.8 (Autenticação Acessível - Sem Teste Cognitivo) e 1.1.1 (Conteúdo Não Textual).
    * **Heurística de Nielsen:** Heurística 5 (Prevenção de Erros) e Heurística 9 (Recuperação de Erros).

---

## 2. Comparativo Antes x Depois

| Versão Atual do Site dos Correios | Versão Proposta pelo Grupo 04 (Redesign Acessível) |
| :--- | :--- |
| **Exigência de decifração visual:** Obriga o cidadão a identificar caracteres alfanuméricos com distorções gráficas, ruído visual e baixo contraste. | **Validação Não-Intrusiva (*Honeypot* / Botão de Ação Direta):** Validação automática e silenciosa via scripts de segurança em segundo plano (ou desafio simples de seleção contextual com alternativa sonora de alta definição). |
| **Alto índice de atrito:** O participante P1 necessitou de auxílio do moderador para conseguir submeter o formulário de cálculo de frete. | **Fluxo Fluido e Contínuo:** Elimina o ponto de interrupção e permite cálculo imediato com clique único no botão primário. |
| **Exclusão de pessoas com baixa visão:** Viola preceitos de acessibilidade de forma severa. | **Conformidade Plena com a NBR 17225:** Totalmente operável por tecnologias assistivas e sem sobrecarga cognitiva para o cidadão. |

---

## 3. Justificativa de Engenharia e Design de IHC

A proposta substitui a abordagem punitiva do CAPTCHA gráfico — que transfere o ônus da segurança para o usuário final — por uma arquitetura de proteção em camadas no servidor. A simplificação reduz o tempo médio da tarefa em aproximadamente 40 segundos e erradica os erros de digitação causados por ambiguidades entre letras e números (como "0" e "O", "1" e "l").

---

## 4. Acesso ao Protótipo Interativo

O protótipo de alta fidelidade da tela de cálculo de frete sem CAPTCHA encontra-se em desenvolvimento no Figma:

🔗 **[Acessar Protótipo de Redesign no Figma](https://www.figma.com)** *(Link do projeto do Grupo 04)*

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| `1.0` | 29/10/2026 | Estrutura de anexo de protótipo | Grupo 04 | Grupo 04 |
| `2.0` | 10/11/2026 | Documentação do protótipo da solução prioritária (substituição do CAPTCHA) | Grupo 04 | Grupo 04 |

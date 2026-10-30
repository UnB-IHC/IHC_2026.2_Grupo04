# IHC 2026.2 - Grupo 04

Repositório da disciplina de **Interação Humano-Computador (FGA0173)** da Universidade de Brasília (UnB - FGA).

Este repositório armazena a documentação oficial do projeto, desenvolvida em Markdown e publicada via **GitHub Pages** utilizando o **MkDocs Material**.

## Integrantes do Grupo

| Nome | Matrícula | GitHub |
| :--- | :---: | :---: |
| Bruna Vitória De Lima Liberal | 222021942 | [@](https://github.com/) |
| Daniel Ribeiro de Andrade | 241025612 | [@](https://github.com/) |
| João Pedro de Sousa Silva | 232003723 | [@joaoPedro-201](https://github.com/joaoPedro-201) |
| Luiz Henrique Pessato Da Mota | 232028428 | [@](https://github.com/) |
| Marcella Sousa Anderle | 221035040 | [@](https://github.com/) |
| Marcus Rogério Aguiar de Sousa | 211062203 | [@](https://github.com/) |
| Paulo Lucca | 170020339 | [@](https://github.com/) |
| Pedro Vieira Antunes | 232014155 | [@](https://github.com/) |

---

## Como Executar Localmente

### Pré-requisitos
* Python 3.10 ou superior
* Git

### Passo a Passo

1. **Clone o repositório:**
```bash
git clone https://github.com/joaoPedro-201/IHC-26.2-GP-04.git
cd IHC-26.2-GP-04
```

2. **Crie e ative um ambiente virtual (opcional, mas recomendado):**
```bash
python -m venv venv
# No Windows:
.\venv\Scripts\activate
# No Linux/macOS:
source venv/bin/activate
```

3. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

4. **Inicie o servidor de documentação:**
```bash
mkdocs serve
```

5. Acesse no navegador em `http://127.0.0.1:8000`.

Qualquer alteração feita nos arquivos `.md` dentro da pasta `docs/` será recarregada automaticamente no navegador (Live Reload).

---

## Deploy Contínuo (GitHub Pages)

O deploy é automatizado através do **GitHub Actions** configurado em `.github/workflows/deploy.yml`. 
Toda vez que uma alteração é enviada via `git push` para a branch `main`, a documentação é reconstruída e atualizada no GitHub Pages.

# Company Server 👔💼

Este é um projeto em Python que implementa uma API de cadastro de empresas, utilizando a metodologia TDD (Test-Driven Development) e seguindo os princípios da Clean Architecture.

## Pré-requisitos 📋

Antes de começar, certifique-se de ter os seguintes pré-requisitos instalados em sua máquina:

- Python na versão ^3.10 🐍
- [Poetry](https://python-poetry.org/) instalado para gerenciamento de dependências 🎵
- Um banco PostgreSQL em execução 🐘

## Como Iniciar o Projeto 🚀

1. Clone o repositório do GitHub:

```bash
git clone https://github.com/kelwinv/company-crud-with-tdd-backend.git
```

2. Crie um ambiente virtual e instale as dependências utilizando o Poetry:

```bash
cd company-crud-with-tdd-backend
poetry install
poetry shell
```

3. Configure o arquivo `.env` na raiz do projeto com as informações de conexão do banco de dados e a porta do servidor. Por exemplo:

```
DATABASE_NAME=app
DATABASE_USER=postgres
DATABASE_PASSWORD=docker
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_SCHEMA=company

PORT=3333 
```

Caso já tenha um banco PostgreSQL em execução e não queira criar um novo esquema, você pode remover a linha `DATABASE_SCHEMA=company`, pois o padrão será o esquema público.

Se desejar preencher o banco com algumas empresas de exemplo, execute:

```bash
seed_company 25
```

Onde `seed_company` é o comando e `25` é a quantidade de empresas que você deseja adicionar.

4. Com o banco de dados configurado, você pode rodar o servidor com o seguinte comando:

```bash
start
```

ou 

```bash
poetry run start
```

5. Para rodar o servidor em modo de desenvolvimento (modo de debug, reiniciando automaticamente em caso de mudanças no código), utilize o seguinte comando:

```bash
start_dev
```

ou

```bash
poetry run start_dev
```

## Executando os Testes 🧪

Os testes automatizados foram desenvolvidos seguindo a metodologia TDD e podem ser executados utilizando o pytest. Para rodar os testes em modo de debug, utilize o seguinte comando:

```bash
poetry run pytest-watch -c
```

## Estrutura do Repositório 📂

O projeto está organizado seguindo os princípios da Clean Architecture, o que facilita a manutenção e extensibilidade do código. A estrutura do repositório é a seguinte:

- **application**: Nesta pasta estão os casos de uso da aplicação, que representam as ações que podem ser executadas.
  - **controllers**: Contém o blueprint que define as rotas da API e os controladores para cada rota.
  - **exceptions**: Contém as classes de exceção personalizadas para tratamento de erros específicos.
  - **use_case**: Aqui estão os casos de uso da aplicação, cada um representando uma ação específica que pode ser executada.

- **domain**: Contém as entidades de domínio da aplicação, que representam os conceitos centrais do negócio.
  - **entities**: Contém as classes que definem as entidades de domínio, como a entidade Company e a classe CNPJ para validação de CNPJs.
  - **Repository**: Define a interface do repositório que será implementada pelas classes de infraestrutura.

- **infra**: Nesta pasta estão as classes que implementam os detalhes técnicos da aplicação.
  - **db**: Contém arquivos relacionados ao banco de dados, como a classe base_pg que define a conexão com o PostgreSQL e a classe company_seed_pg para popular a base de dados com dados de exemplo.
  - **repository**: Aqui estão as implementações concretas do repositório definido na camada de domínio, tanto em memória (in_memory) quanto no PostgreSQL (postgress_repository).

- **config**: Contém classes e utilitários relacionados à configuração da aplicação.

- **main.py**: Ponto de entrada da aplicação, onde o servidor é iniciado.

- **tests**: Contém os testes automatizados do projeto, separados em testes de unidade (unit) e testes de integração (integration).

## Dependências 📦

O projeto utiliza as seguintes dependências:

- peewee: ORM usado para conexão com o banco de dados e configuração de modelos.
- psycopg2: Usado junto com peewee para conexão com o banco PostgreSQL.
- flask: Util

izado para construir a API.
- waitress: Servidor WSGI para rodar a aplicação.

Dependências para testes:

- pytest: Framework para execução de testes.
- pytest-testmon: Plugin para execução de testes incrementais.
- pytest-watch: Plugin para executar os testes automaticamente quando houver mudanças no código.
- pytest-cov: Plugin para medir a cobertura dos testes.

Dependências de desenvolvimento:

- black: Ferramenta de formatação de código.
- faker: Biblioteca para geração de dados falsos.

## Autor 👨‍💻

- **Kelwin Vieira** - [GitHub](https://github.com/kelwinv)

## Licença 📜

Este projeto está licenciado sob a licença [CC0 1.0 Universal](LICENSE.md) da Creative Commons - consulte o arquivo [LICENSE.md](LICENSE.md) para mais detalhes.

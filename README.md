# climate-db

Ferramenta simples de visualização de banco de dados em interface de linha de comando.

## Índice

- [Recursos](#recursos)
- [Instalação](#instalação)
- [Como usar](#como-usar)
    - [Configurando a conexão](#configurando-a-conexão)
    - [Comandos](#comandos)
    - [Ajuda](#obtendo-ajuda-sobre-os-comandos)


## Recursos
- [x] Permitir a conexão a bancos de dados PostgreSQL e MySQL
- [x] Gravar dados de conexão
- [x] Mostrar graficamente (em árvore) as tabelas e views do banco de dados
- [x] Mostrar também os campos da tabela e seus tipos e tamanhos
- [ ] Apontar as chaves primárias de cada tabela
- [x] Consultar os dados da tabela
- [x] Dados mostrados em estrutura de tabela
- [x] Mostrar todos os dados (limitado a 1000 registros - configurável)
- [x] Permitir consultas gerais (digitando o SQL diretamente)
- [ ] Exportação de dados das tabelas e das consultas em CSV ou JSON

## Instalação

### Requisitos
- Python 3.7+
- Banco de dados MySQL ou PostgreSQL
- Bibliotecas necessárias:
    - mysql-connector-python
    - psycopg2
    - sqlalchemy
    - pandas
    - tabulate
    - rich
    - typer

### Clonando o repositório via HTTPS

    git clone https://github.com/lucasltarga/climate-db.git

### Instalando dependências com pip

Navegue até a pasta raiz do projeto e use o seguinte comando:


    pip install -r requirements.txt

## Como usar

### Configurando a conexão

**Para configurar o banco de dados:**

```
python climate.py configure --db_type TIPO_BANCO --host HOST --port PORTA --user USUARIO --password SENHA --database BANCO_DE_DADOS
```

ou 

```
python climate.py configure TIPO_BANCO HOST PORTA USUARIO SENHA BANCO_DE_DADOS
```

**Exemplos:**

```
python climate.py configure --db_type mysql --host localhost --port 3306 --user meu_usuario --password minhasenhaforte --database testeBD
```

ou

```
python climate.py configure postgresql 127.0.0.1 3306 meu_usuario minhasenhaforte testeDB
```

*As configurações serão salvas localmente em climate-db/src/config/db_config.json.*

**Para testar a conexão:**

    python climate.py test

### Comandos

#### **configure**

Salva as informações do banco de dados em um arquivo JSON para fazer a conexão posteriormente.

Argumentos esperados:

- db_type: tipo de banco de dados (mysql ou postgresql)
- host: hostname ou IP do banco de dados
- port: porta usada no servidor de banco de dados
- user: usuário a ser usado na conexão
- password: senha do usuário a ser usado na conexão
- database: nome do banco de dados

Exemplo: 

    python climate.py configure mysql 127.0.0.1 3306 meu_usuario minhasenhaforte meu_banco

#### **query**

Permite a execução de queries no banco de dados.

Exemplo:

    python climate.py query "select * from student where tot_cred > 50"

#### **show-table**

Mostra os dados na tabela determinada.
O limite padrão de resultados é 1000, mas pode ser configurado utilizando a _flag_ --limit

Exemplo:

    python climate.py show-table student --limit=10

#### **show-tree**

Mostra todo o banco de dados em uma estrutura de árvore, incluindo os tipos de dados e tamanho de cada campo.

Exemplo:

    python climate.py show-tree

#### **test**

Testa o sucesso de uma conexão usando os dados salvos em climate-db/src/config/db_config.json.

Exemplo:

    python climate.py test

### Obtendo ajuda sobre os comandos:

Mostrar todos os comandos disponíveis:
    
    python climate.py --help

Mostrar as opções e os argumentos de cada comando:

    python climate.py COMANDO --help


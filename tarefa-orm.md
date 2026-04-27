# Resumo Técnico: ODBC com Python
## O ODBC (Open Database Connectivity) atua como uma camada de abstração que permite ao Python comunicar-se com diversos Sistemas de Gerenciamento de Banco de Dados (SGBD) de forma padronizada.

## O Papel do ODBC no Ecossistema Python
**A principal função do ODBC é a interoperabilidade. Em vez de escrever um código específico para cada banco, o desenvolvedor utiliza uma biblioteca Python que conversa com o Gerenciador de Driver ODBC do sistema operacional.**

**Componentes da Arquitetura**
* Aplicação (Python)
  * Onde reside a lógica de negócio e as chamadas SQL.
* Biblioteca de Interface (pyodbc)
  * Implementa a especificação DB-API 2.0 do Python para o padrão ODBC.
* Gerenciador de Driver
  * Biblioteca de sistema (ex: odbc32.dll ou unixODBC) que carrega o driver correto.
* Driver ODBC
  * O tradutor específico fornecido pelo fabricante do banco (ex: ODBC Driver for SQL Server).

**Conceitos Chave**
1. DSN (Data Source Name)
  1. Um nome configurado no SO que agrupa informações de conexão (servidor, porta, driver).
2. Connection Strings (DSN-less)
  1. Strings que contêm todos os parâmetros necessários de forma explícita no código.
3. Cursores
  1. Objetos que permitem navegar e manipular os registros retornados.
4. Commit/Rollback
  1. Gestão de transações para garantir a integridade dos dados.



# O ORM (Object-Relational Mapper) do Django é uma das funcionalidades mais poderosas do framework. Ele permite que você interaja com o banco de dados utilizando sintaxe Python em vez de escrever SQL manualmente.

## O ORM atua como um tradutor entre o mundo da Orientação a Objetos (Python) e o mundo Relacional (Bancos de Dados como PostgreSQL, MySQL ou SQLite).


1. No Django, cada tabela do banco de dados é representada por uma classe Python que herda de django.db.models.Model.
  1. Classe: Representa a Tabela.
  2. Atributo: Representa a Coluna (campo).
  3. Instância da Classe: Representa uma Linha (registro) na tabela.

## Componentes da Arquitetura
  1. Models: Onde você define a estrutura dos dados.
  2. QuerySets: Uma coleção de objetos do banco de dados. Eles são "preguiçosos" (lazy), o que significa que a consulta só é executada no banco quando você realmente tenta acessar os dados.
  3. Managers (objects): A interface através da qual as consultas de banco de dados são fornecidas aos modelos Django (ex: User.objects.all()).
  4. Migrations: O sistema que propaga as alterações que você faz nos modelos para o esquema do banco de dados.

## Conceitos Chave
1. Abstração de Banco de Dados
  1. Você define seus modelos uma única vez. Se decidir trocar de SQLite para PostgreSQL, o Django ORM traduz automaticamente as operações para a nova sintaxe do banco de dados.
2. Relacionamento, o ORM facilita a criação de vínculos entre tabelas:
  1. `ForeignKey:` Relacionamento Um-para-Muitos.
  2. `ManyToManyField:` Relacionamento Muitos-para-Muitos.
  3. `OneToOneField:` Relacionamento Um-para-Um.
3. API de Consulta (Lookup), permite filtrar dados de forma intuitiva:
  1. `filter():` Filtra registros com base em critérios.
  2. `exclude():` Retorna objetos que não correspondem aos critérios.
  3.  `get():` Retorna um único objeto específico.
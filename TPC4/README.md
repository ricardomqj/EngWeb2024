# TPC4: Compositores e diversos períodos
## 10-03-2024

## Autor:
- A100066
- Ricardo Miguel Queirós de Jesus

## Resumo:

Este TPC concentrou-se no desenvolvimento de um sistema de gerenciamento de compositores e períodos musicais, com o propósito de facilitar a organização e visualização das informações relacionadas a esses artistas e as suas respetivas épocas históricas.

## Objetivos:

- Os objetivos deste TPC consiste na implementação de um dataset no JSON-server, carregando os dados sobre compositores e períodos musicais num servidor JSON de modo a fornecer acesso a estes dados pela aplicação web.
- Outro objetivo consiste na criação de um conjunto de rotas importantes como:
    - `/compositores:` listar os compositores.
    - `/compositores{id}:` informações detalhadas de um compositor.
    - `/compositores?periodo={periodo}:` listar compositores de um determinado período.
    - `/periodos:` listar todos os períodos musicais.
    - `/periodos/{id}:` informações detalhadas sobre um determinado período musical.

- Outro objetivo consiste na implementação de um serviço com operações CRUD(Create, Read, Update, Delete) para manipulação de dados sobre compositores e períodos musicais.

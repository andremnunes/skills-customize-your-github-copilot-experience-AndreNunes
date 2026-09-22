# 📘 Atividade: Building REST APIs with FastAPI

## 🎯 Objetivo

Construir uma API REST simples com FastAPI, aprender a definir rotas, validar dados com Pydantic e gerenciar uma pequena coleção em memória.

## 📝 Tarefas

### 🛠️ Configuração da API

#### Descrição
Crie uma aplicação FastAPI que exponha endpoints para consultar o status do serviço e listar itens.

#### Requisitos
O programa concluído deve:

- Criar uma aplicação FastAPI com título e descrição.
- Incluir um endpoint `GET /health` que retorne um JSON com status `ok`.
- Incluir um endpoint `GET /items` para listar itens em memória.
- Usar um modelo de dados com Pydantic para representar cada item.

### 🛠️ CRUD de Itens

#### Descrição
Implemente operações para criar, listar, atualizar e remover itens em uma API REST.

#### Requisitos
O programa concluído deve:

- Definir uma rota `POST /items` para criar um novo item.
- Definir uma rota `GET /items/{item_id}` para consultar um item específico.
- Definir uma rota `PUT /items/{item_id}` para atualizar um item existente.
- Definir uma rota `DELETE /items/{item_id}` para remover um item.
- Validar campos obrigatórios como `name`, `price` e `in_stock`.
- Usar respostas em JSON com códigos HTTP apropriados.

Exemplo de payload de criação:

```json
{
  "name": "Notebook",
  "price": 9.99,
  "in_stock": true
}
```

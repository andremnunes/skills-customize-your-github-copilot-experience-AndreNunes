# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Construir uma API REST para gerenciar tarefas usando FastAPI e Pydantic. Ao final, você saberá criar rotas, validar dados de requisições, filtrar resultados e retornar códigos HTTP apropriados.

## 📝 Tasks

### 🛠️ Criar a aplicação e as rotas de leitura

#### Descrição

Complete a aplicação inicial e crie os endpoints necessários para consultar tarefas. As tarefas devem permanecer armazenadas em memória enquanto a aplicação estiver em execução.

#### Requisitos

O programa concluído deve:

- Criar uma aplicação FastAPI com título e descrição.
- Incluir um endpoint `GET /health` que retorne `{ "status": "ok" }`.
- Incluir um endpoint `GET /tasks` que retorne todas as tarefas.
- Incluir um endpoint `GET /tasks/{task_id}` que retorne uma tarefa pelo ID.
- Retornar o código HTTP `404` quando o ID solicitado não existir.

### 🛠️ Validar dados e criar tarefas

#### Descrição

Defina modelos Pydantic para representar tarefas e o corpo usado na criação. Depois, implemente o endpoint que adiciona uma nova tarefa à coleção em memória.

#### Requisitos

O programa concluído deve:

- Representar uma tarefa com `id`, `title`, `description`, `completed` e `priority`.
- Exigir um título e uma descrição não vazios.
- Aceitar somente as prioridades `low`, `medium` ou `high`.
- Definir `completed` como `false` por padrão.
- Implementar `POST /tasks` e retornar o código HTTP `201` ao criar uma tarefa.
- Gerar um ID novo sem sobrescrever tarefas existentes.

Exemplo de payload:

```json
{
  "title": "Estudar FastAPI",
  "description": "Praticar rotas e modelos Pydantic",
  "priority": "high"
}
```

### 🛠️ Atualizar, remover e filtrar tarefas

#### Descrição

Complete o ciclo de operações da API e permita que clientes encontrem tarefas por status e prioridade usando query parameters.

#### Requisitos

O programa concluído deve:

- Implementar `PUT /tasks/{task_id}` para atualizar uma tarefa existente.
- Implementar `DELETE /tasks/{task_id}` para remover uma tarefa existente.
- Retornar `404` para atualizações ou remoções de IDs inexistentes.
- Implementar `GET /tasks?completed=true` para filtrar pelo status de conclusão.
- Implementar `GET /tasks?priority=high` para filtrar pela prioridade.
- Permitir combinar os filtros `completed` e `priority`.
- Documentar e testar os endpoints usando a documentação automática em `/docs`.

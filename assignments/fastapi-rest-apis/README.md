# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI to learn how to define routes, handle HTTP requests, and return JSON responses for a simple resource.

## 📝 Tasks

### 🛠️ Create the API App

#### Descrição
Create a FastAPI app that exposes a health endpoint and a list of sample items. The goal is to understand the basic structure of a FastAPI project and how request handlers return JSON.

#### Requisitos
O programa concluído deve:

- Import `FastAPI` and create an application instance
- Add a `GET /health` endpoint that returns a JSON message such as `{"status": "ok"}`
- Add a `GET /items` endpoint that returns a list of sample items
- Use Python dictionaries and lists to represent the data returned by the API

### 🛠️ Add CRUD Endpoints

#### Descrição
Extend the API to support creating, reading, updating, and deleting a simple item collection. This task focuses on request methods and resource modeling.

#### Requisitos
O programa concluído deve:

- Add a `GET /items/{item_id}` endpoint to return a single item by ID
- Add a `POST /items` endpoint to create a new item from a request body
- Add a `PUT /items/{item_id}` endpoint to update an existing item
- Add a `DELETE /items/{item_id}` endpoint to remove an item
- Return JSON responses with clear status information and item data

### 🛠️ Validate Input and Improve the API

#### Descrição
Improve the API by validating incoming data and organizing the code so it is easier to maintain and test. This task introduces realistic API design best practices.

#### Requisitos
O programa concluído deve:

- Use Pydantic models to validate item fields such as `id`, `name`, and `description`
- Require meaningful fields for item creation and update requests
- Handle invalid requests with FastAPI validation errors
- Keep the application logic organized in a clean, readable structure
- Demonstrate the app running successfully with a sample API call

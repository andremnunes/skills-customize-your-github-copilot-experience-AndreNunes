from fastapi import FastAPI

app = FastAPI(title="Sample FastAPI App")

items = [
    {"id": 1, "name": "Keyboard", "description": "Mechanical keyboard"},
    {"id": 2, "name": "Mouse", "description": "Wireless mouse"},
]


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/items")
def get_items():
    return items


# TODO: Add endpoints for getting, creating, updating, and deleting items

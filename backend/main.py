from dotenv import dotenv_values
from deta import Deta
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

deta_key = dotenv_values(".env")["DETA_PROJECT_KEY"]
deta_base = dotenv_values(".env")["DETA_PROJECT_ID"]
deta = Deta(deta_key)
deta_db = deta.Base(deta_base)

app = FastAPI()


class PlaylistSchema(BaseModel):
    sentiment: str
    name: str
    url: str


@app.post("/")
async def create_item(item: PlaylistSchema):
    item = deta_db.put({"name": item.name, "url": item.url})
    return {"message": "Item created successfully"}


@app.get("/{key}")
async def get_item(key):
    item = deta_db.fetch({"sentiment?contains": key})
    if item:
        return item
    else:
        raise HTTPException(status_code=404, detail="Item not found")


@app.get("/sentiment/{key}")
async def get_sentiment(key):
    item = deta_db.get(key)
    if item:
        return item
    else:
        raise HTTPException(status_code=404, detail="Item not found")


@app.get("/")
async def get_items():
    items = deta_db.fetch()
    return items


@app.delete("/{key}")
async def delete_item(key):
    deta_db.delete(key)
    return {"message": f"Item with key {key} deleted successfully"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

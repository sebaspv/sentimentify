from dotenv import dotenv_values
from deta import Deta
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
from fer import FER
import cv2
import numpy as np
import base64

deta_key = dotenv_values(".env")["DETA_PROJECT_KEY"]
deta_base = dotenv_values(".env")["DETA_PROJECT_ID"]
deta = Deta(deta_key)
deta_db = deta.Base(deta_base)

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class PlaylistSchema(BaseModel):
    sentiment: str
    name: str
    url: str


class ImageSchema(BaseModel):
    msg: str


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


@app.post("/get-sentiment")
async def get_sentiment(msg: ImageSchema):
    encoded_data = msg.msg.split(',')[1]
    nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
    source = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    detector = FER()
    return detector.top_emotion(source)


@app.get("/")
async def get_items():
    items = deta_db.fetch()
    return items


@app.delete("/{key}")
async def delete_item(key):
    deta_db.delete(key)
    return {"message": f"Item with key {key} deleted successfully"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

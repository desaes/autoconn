import sys, os
from fastapi import FastAPI
from libraries.config import Config
import threading

lock = threading.RLock()

config = Config()

targets = [target for target in config.get_config()]



"""

app = FastAPI()


@app.get('/')
async def raiz():
    return {"msg": "xpto"}


@app.get('/api/v1/aranda/{instance}/projects')
async def projects(instance: str):
    return {"endpoint": f"{config.get_config()['itsm']['aranda'][instance]}"}



if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, 
                log_level="info", reload=True)
"""
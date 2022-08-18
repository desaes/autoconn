from fastapi import FastAPI
from config import Config
import threading

config = Config()
lock = threading.RLock()

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

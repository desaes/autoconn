from fastapi import FastAPI
from config import aranda_conf



app = FastAPI()


@app.get('/')
async def raiz():
    return {"msg": aranda_conf.Instance01.MainEndpoint}

@app.get('/api/v1/aranda/projects')
async def projects() -> None:
    return {"msg": "cfg"}
    


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, 
                log_level="info", reload=True)

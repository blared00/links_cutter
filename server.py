import uvicorn
from decouple import config
from fastapi import FastAPI

from apps.cutter.endpoints import router


app = FastAPI(title="Links Cutter")
app.include_router(router)


if __name__ == '__main__':
    uvicorn.run('server:app', port=int(config('PORT')), host=config("HOME_PAGE"), reload=True)

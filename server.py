import uvicorn
from decouple import config
from fastapi import FastAPI

from apps.cutter.endpoints import router as cutter
from apps.cutter.redirect import router as redirect
from db_apps.core import database


app = FastAPI(title="Links Cutter")
app.include_router(cutter)
app.include_router(redirect)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

if __name__ == '__main__':
    uvicorn.run('server:app', port=int(config('PORT')), host=config("HOME_PAGE"), reload=True)

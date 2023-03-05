from sqlalchemy.orm import Session

from . import models, schemas
from ..core import database


async def get_short_link_by_full(full_link):
    query = models.Link.__table__.select().where(models.Link.__table__.c.full_link == full_link)
    return await database.fetch_one(query)


async def get_full_link_by_short(short_link):
    query = models.Link.__table__.select().where(models.Link.__table__.c.short_link == short_link)
    return await database.fetch_one(query)


async def create_link(link: schemas.LinkCreate):
    query = models.Link.__table__.insert().values(**link.dict())
    last_record_id = await database.execute(query)
    return {**link.dict(), "id": last_record_id}


async def delete_link(link: schemas.Link):
    query = models.Link.__table__.delete().where(models.Link.__table__.c.short_link == link.short_link)
    await database.execute(query)
    return

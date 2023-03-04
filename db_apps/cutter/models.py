from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.sql import func

from ..core import Base


class Link(Base):
    __tablename__ = "links"

    id = Column(Integer, primary_key=True, index=True)
    full_link = Column(String, unique=True, index=True)
    short_link = Column(String, unique=True, index=True)
    created_at = Column(TIMESTAMP, server_default=func.now())

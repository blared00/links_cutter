from pydantic import BaseModel


class Link(BaseModel):
    short_link: str
    full_link: str

from pydantic import BaseModel


class LinkBase(BaseModel):
    short_link: str
    full_link: str


class LinkCreate(LinkBase):
    pass


class Link(LinkBase):
    id: int
    created_at: int

    class Config:
        orm_mode = True

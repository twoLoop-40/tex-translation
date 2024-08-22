from pydantic import BaseModel


class DocStyle(BaseModel):
    type: str
    settings: list[str | tuple]

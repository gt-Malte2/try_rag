from pydantic import BaseModel
import pydantic_settings


class Module(BaseModel):
    module_title: str
    ects: int
    optional: bool
    competencies: str
    content: str
    requirements: list["Module"] | None


class Document(BaseModel):
    modules: list[Module]

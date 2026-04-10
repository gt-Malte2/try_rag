from pydantic import BaseModel


class RawModule(BaseModel):
    module_tite: str | None
    ects: str | None
    optional: str


class Module(BaseModel):
    module_title: str
    ects: int
    optional: bool
    competencies: str
    content: str
    requirements: list[str] | None


class Document(BaseModel):
    modules: list[Module]

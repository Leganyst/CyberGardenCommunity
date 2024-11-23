from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List


class WorkspaceBase(BaseModel):
    """
    Базовая схема рабочего пространства.
    """
    name: str = Field(..., max_length=100, description="Название рабочего пространства")


class WorkspaceCreate(WorkspaceBase):
    """
    Схема для создания рабочего пространства.
    """
    created_by: int | None = None
    pass

class WorkspaceUpdate(BaseModel):
    """
    Схема для обновления рабочего пространства.
    """
    name: Optional[str] = Field(None, max_length=100, description="Новое название рабочего пространства")


class WorkspaceResponse(WorkspaceBase):
    """
    Схема для ответа с данными рабочего пространства.
    """
    id: int = Field(..., description="Уникальный идентификатор рабочего пространства")
    created_by: int = Field(..., description="ID пользователя, создавшего рабочее пространство")
    created_at: datetime = Field(..., description="Дата создания рабочего пространства")
    updated_at: datetime = Field(..., description="Дата последнего обновления рабочего пространства")

    class Config:
        from_attributes = True


class WorkspaceWithProjects(WorkspaceResponse):
    """
    Схема для ответа с данными рабочего пространства и связанных проектов.
    """
    projects: List[dict] = Field(..., description="Список проектов, связанных с рабочим пространством")

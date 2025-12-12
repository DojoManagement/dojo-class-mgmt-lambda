from dataclasses import dataclass
from datetime import date, time
from pydantic import BaseModel, Field

@dataclass
class ClassBase(BaseModel):
    name: str = Field(..., description="Nome completo da Aula")
    description: str = Field(..., description="Descrição da Aula")
    instructor: str = Field(..., description="Nome do Instrutor")
    day_of_week: str = Field(..., description="Dia da semana da Aula, ex: 'Monday', 'Tuesday'")
    start_time: time = Field(..., description="Hora de início da Aula")
    end_time: time = Field(..., description="Hora de término da Aula")
    max_students: int = Field(..., description="Número máximo de alunos na Aula")
    current_students: int = Field(0, description="Número atual de alunos na Aula")
    is_active: bool = Field(True, description="Indica se a Aula está ativa")

class ClassCreate(ClassBase):
    """✅ Modelo para criação (sem ID)"""
    pass

class Class(ClassBase):
    """Modelo completo com ID"""
    id: Optional[int] = Field(None, description="ID único (gerado automaticamente)")

    class Config:
        from_attributes = True
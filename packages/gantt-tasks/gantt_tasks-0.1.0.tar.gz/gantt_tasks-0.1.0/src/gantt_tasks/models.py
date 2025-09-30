from dataclasses import dataclass, field
from datetime import date
from typing import Optional

@dataclass
class Task:
    """
    Representa uma tarefa.
    - id: identificador opcional
    - title: descrição curta
    - duration: duração em dias (inteiro >=1)
    - priority: inteiro (maior = mais prioridade)
    - sequence: ordem relativa (menor = executa antes)
    - start: data de início opcional (se None, será agendado pelo TaskManager)
    - assigned_start: data atribuída pelo scheduler (após agendamento)
    """
    title: str
    duration: int = 1
    priority: int = 1
    sequence: int = 0
    start: Optional[date] = None
    assigned_start: Optional[date] = field(default=None, repr=False)

    def __post_init__(self):
        if self.duration < 1:
            raise ValueError("duration must be >= 1")

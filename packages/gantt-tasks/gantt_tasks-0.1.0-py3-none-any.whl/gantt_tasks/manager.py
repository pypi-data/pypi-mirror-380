from datetime import date, timedelta
from typing import List, Optional, Tuple
from .models import Task
import calendar

class TaskManager:
    """
    Garante CRUD simples em memória (podes ligar a BD depois).
    Fornece uma função de agendamento mensal por prioridade e sequência.
    """

    def __init__(self, tasks: Optional[List[Task]] = None):
        self.tasks = tasks[:] if tasks else []

    # CRUD básico
    def add(self, task: Task):
        self.tasks.append(task)

    def remove(self, task_index: int):
        del self.tasks[task_index]

    def list(self) -> List[Task]:
        return self.tasks[:]

    def find_by_title(self, title: str) -> List[Task]:
        return [t for t in self.tasks if title.lower() in t.title.lower()]

    # --- Scheduler simples ---
    def schedule_month(self, year: int, month: int) -> List[Task]:
        """
        Agenda as tarefas dentro do mês especificado.
        Regras:
            - Ordena por (sequence asc, priority desc).
            - Se task.start foi fornecido e cai no mês, respeita esse start.
            - Caso contrário, coloca as tarefas disponíveis ocupando dias disponíveis do mês
              respeitando sequência e prioridade (greedy).
        Retorna lista de tarefas com `assigned_start` preenchido (ou None se não coube).
        """
        # criar mapa de dias ocupados (booleans)
        _, ndays = calendar.monthrange(year, month)
        month_start = date(year, month, 1)
        occupied = [False] * ndays  # index 0 => day 1

        # ordena por sequence asc, priority desc (higher priority first when same sequence)
        order = sorted(self.tasks, key=lambda t: (t.sequence, -t.priority))

        # primeiro, marcar tarefas com start fixo dentro do mês
        for t in order:
            if t.start and t.start.year == year and t.start.month == month:
                sday = t.start.day
                end_day = sday + t.duration - 1
                if end_day <= ndays:
                    # marcar ocupados
                    for d in range(sday-1, end_day):
                        occupied[d] = True
                    t.assigned_start = t.start
                else:
                    # start fornecido mas não cabe — assigned_start stays None
                    t.assigned_start = None

        # agora agendar restantes greedy: para cada task na ordem, encontrar primeiro bloco contínuo disponível
        for t in order:
            if t.assigned_start is not None:
                continue  # já marcou
            # procurar primeiro bloco de tamanho duration livre entre day 1..ndays
            placed = False
            for day_idx in range(0, ndays - t.duration + 1):
                # verificar se bloco livre
                if all(not occupied[d] for d in range(day_idx, day_idx + t.duration)):
                    # colocar
                    for d in range(day_idx, day_idx + t.duration):
                        occupied[d] = True
                    t.assigned_start = date(year, month, day_idx + 1)
                    placed = True
                    break
            if not placed:
                t.assigned_start = None  # não coube

        return order

    def clear_assigned(self):
        for t in self.tasks:
            t.assigned_start = None

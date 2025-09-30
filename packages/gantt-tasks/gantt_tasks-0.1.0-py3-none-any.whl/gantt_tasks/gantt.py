from datetime import date, timedelta
from typing import List, Optional
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import calendar
from .models import Task
from .manager import TaskManager

def _day_to_datetime(dt: date):
    # convert date to matplotlib date number
    import datetime
    return mdates.date2num(datetime.date(dt.year, dt.month, dt.day))

def generate_month_gantt(tasks: List[Task], year: int, month: int, filename: str = "gantt_month.png", figsize=(10,6)):
    """
    Gera um gráfico de Gantt para o mês dado, a partir de tasks (já com assigned_start preferencialmente).
    Se uma tarefa não tiver assigned_start, será ignorada no gráfico.
    Salva em filename e retorna o filename.
    """
    # filtrar apenas tasks com assigned_start no mês pedido
    tasks_in_month = [t for t in tasks if t.assigned_start and t.assigned_start.year == year and t.assigned_start.month == month]

    # ordenar por assigned_start (asc) e priority (desc)
    tasks_sorted = sorted(tasks_in_month, key=lambda t: (t.assigned_start, -t.priority, t.sequence))

    if not tasks_sorted:
        # criar figura vazia com título
        fig, ax = plt.subplots(figsize=figsize)
        ax.set_title(f"Gantt - {calendar.month_name[month]} {year}\n(nenhuma tarefa agendada)")
        ax.axis('off')
        fig.savefig(filename, bbox_inches="tight")
        plt.close(fig)
        return filename

    # y positions
    y_pos = list(range(len(tasks_sorted)))
    labels = [f"{t.title} (P{t.priority} S{t.sequence})" for t in tasks_sorted]

    # build bars: left = assigned_start, width = duration days
    lefts = [_day_to_datetime(t.assigned_start) for t in tasks_sorted]
    widths = [t.duration for t in tasks_sorted]

    fig, ax = plt.subplots(figsize=figsize)
    ax.barh(y_pos, widths, left=lefts, height=0.6, align='center')

    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels)
    ax.invert_yaxis()

    # x axis: day ticks of month
    import datetime as _dt
    month_first = _dt.date(year, month, 1)
    _, ndays = calendar.monthrange(year, month)
    month_last = _dt.date(year, month, ndays)
    ax.set_xlim(_day_to_datetime(month_first) - 0.5, _day_to_datetime(month_last) + 0.5)

    # format x-axis as day numbers
    locator = mdates.DayLocator()
    formatter = mdates.DateFormatter('%d')
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)

    ax.set_xlabel("Dia do mês")
    ax.set_title(f"Gantt - {calendar.month_name[month]} {year}")
    plt.tight_layout()
    fig.savefig(filename, bbox_inches="tight")
    plt.close(fig)
    return filename

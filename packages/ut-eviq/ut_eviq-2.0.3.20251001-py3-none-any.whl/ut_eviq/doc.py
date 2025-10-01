"""
This module provides utility classes for the management of OmniTracker
EcoVadis NHRR (Nachhaltigkeits Risiko Rating) processing for Department UMH
"""
from ut_eviq.rst.taskioc import TaskIoc as EviqRstTaskIoc
from ut_eviq.xls.taskioc import TaskIoc as EviqXlsTaskIoc

from typing import Any, Callable
TyCallable = Callable[..., Any]
TyDoC = dict[str, TyCallable]
TyDoDoC = dict[str, TyDoC]


DoDoC: TyDoDoC = {
    'xls': {
        'evupadm': EviqXlsTaskIoc.evupadm,
        'evupdel': EviqXlsTaskIoc.evupdel,
        'evupreg': EviqXlsTaskIoc.evupreg,
        'evdomap': EviqXlsTaskIoc.evdomap,
    },
    'rst': {
        'evupadm': EviqRstTaskIoc.evupadm,
        'evupdel': EviqRstTaskIoc.evupdel,
        'evupreg': EviqRstTaskIoc.evupreg,
        'evdoexp': EviqRstTaskIoc.evdoexp,
        'evdomap': EviqRstTaskIoc.evdomap,
    },
}

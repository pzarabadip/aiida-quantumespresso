# -*- coding: utf-8 -*-
import click
from aiida_quantumespresso.utils.click import command
from aiida_quantumespresso.utils.click import options


@command()
@options.code()
@options.parent_calc()
@options.kpoint_mesh()
@options.max_num_machines()
@options.max_wallclock_seconds()
def launch(
    code, parent_calc, kpoints, max_num_machines, max_wallclock_seconds):
    """
    Run the PhBaseWorkChain for a previously completed PwCalculation
    """
    from aiida.orm.data.parameter import ParameterData
    from aiida.orm.utils import CalculationFactory, WorkflowFactory
    from aiida.work.run import run
    from aiida_quantumespresso.utils.resources import get_default_options

    PwCalculation = CalculationFactory('quantumespresso.pw')
    PhBaseWorkChain = WorkflowFactory('quantumespresso.ph.base')

    parameters = {
        'INPUTPH': {
        }
    }

    options = get_default_options(max_num_machines, max_wallclock_seconds)

    inputs = {
        'code': code,
        'qpoints': kpoints,
        'parent_calc': parent_calc,
        'parameters': ParameterData(dict=parameters),
        'options': ParameterData(dict=options),
    }

    run(PhBaseWorkChain, **inputs)
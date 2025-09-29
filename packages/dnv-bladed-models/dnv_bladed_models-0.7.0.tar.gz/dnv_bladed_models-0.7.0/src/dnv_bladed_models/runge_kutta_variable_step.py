# *********************************************************************#
# Bladed Python Models API                                             #
# Copyright (c) DNV Services UK Limited (c) 2025. All rights reserved. #
# MIT License (see license file)                                       #
# *********************************************************************#


# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401
from enum import Enum, IntEnum

import os
import re  # noqa: F401
from typing import Annotated, Any, Dict, List, Literal, Optional, Set, Type, Union, Callable, Iterable  # noqa: F401
from pathlib import Path
from typing import TypeVar
Model = TypeVar('Model', bound='BaseModel')
StrBytes = Union[str, bytes]

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator, root_validator, Extra,PrivateAttr  # noqa: F401
from pydantic import ValidationError
from pydantic.error_wrappers import ErrorWrapper
from pydantic.utils import ROOT_KEY
from json import encoder
from dnv_bladed_models.integrator import Integrator

from .schema_helper import SchemaHelper
from .models_impl import *


class RungeKuttaVariableStep(Integrator):
    r"""
    Settings for the Runge Kutta Variable Step integrator.
    
    Attributes
    ----------
    IntegratorType : Literal['RungeKuttaVariableStep'], default='RungeKuttaVariableStep'
        Defines the specific type of Integrator model in use.  For a `RungeKuttaVariableStep` object, this must always be set to a value of `RungeKuttaVariableStep`.
    
    InitialStep : float, default=0
        The recommended value is zero: the minimum time step will in fact be used.  A value larger than the minimum time step will speed up the initialisation of the simulation, but there is a risk of numerical problems if too large a value is used.
    
    Tolerance : float, default=0.005
        The tolerance for the variable step integrator: This parameter defines the precision of the simulation. All states are integrated to an error within the integration tolerance multiplied by the state magnitude at that step. A higher value can increase simulation speed but lower precision.  Fixed step integrators: When the \"Maximum number of iterations\" > 1, the integrator relative tolerance is used to control how many iterations are carried out when integrating the first order and prescribed second order states. Iterations are carried out until the maximum number of iterations is reached, or until the change in all first order and prescribed state derivatives between successive iterations is less than the relative tolerance multiplied by the state derivative absolute value.
    
    MinimumTimeStep : float, default=1.0E-7
        The minimum time step.  The simulation uses a 4/5th order Runge-Kutta variable time step method.  The time step will be reduced automatically if the specified tolerance is exceeded, until this minimum value is reached.
    
    MaximumTimeStep : float, default=1
        The maximum time step.  This should normally be the same as the output time step, although a smaller value might be useful in some cases if the output time step is particularly long.  A very small value for the minimum time step is recommended, such as 10^-8 s, to ensure that the accuracy of simulation is not constrained by this.  In special cases, increasing the minimum time step may speed up the simulation with little loss of accuracy, but it is advisable to check that the results are not significantly altered by doing this.  This situation may arise for example with a dynamic mode which is inactive because it is heavily damped.  It may be better to remove the mode completely.
    
    Notes
    -----
    
    """
    IntegratorType: Literal['RungeKuttaVariableStep'] = Field(alias="IntegratorType", default='RungeKuttaVariableStep', allow_mutation=False, const=True) # type: ignore
    InitialStep: float = Field(alias="InitialStep", default=None)
    Tolerance: float = Field(alias="Tolerance", default=None)
    MinimumTimeStep: float = Field(alias="MinimumTimeStep", default=None)
    MaximumTimeStep: float = Field(alias="MaximumTimeStep", default=None)

    _relative_schema_path = 'Settings/SolverSettings/Integrator/RungeKuttaVariableStep.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'IntegratorType').merge(Integrator._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


RungeKuttaVariableStep.update_forward_refs()

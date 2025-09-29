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
from dnv_bladed_models.bladed_model import BladedModel

from .schema_helper import SchemaHelper
from .models_impl import *


class EquilibriumStateSolverSettings(BladedModel):
    r"""
    The settings pertaining to the determination of equilibrium conditions, used for steady calculations or initial conditions.
    
    Attributes
    ----------
    ModalStatesRelaxationFactor : float, default=0.4
        The relaxation factor applied to modal states during iterations to find the equilibrium conditions, to improve numerical stability.  This is used to calculate the initial conditions for time domain calculations, and the steady state in steady calculations.
    
    FloatingPlatformStatesRelaxationFactor : float, default=0.4
        The relaxation factor applied to floating platform positional states during iterations to find the equilibrium conditions, to improve numerical stability.  This is used to calculate the initial conditions for time domain calculations, and the steady state in steady calculations.
    
    Notes
    -----
    
    """
    ModalStatesRelaxationFactor: float = Field(alias="ModalStatesRelaxationFactor", default=None)
    FloatingPlatformStatesRelaxationFactor: float = Field(alias="FloatingPlatformStatesRelaxationFactor", default=None)

    _relative_schema_path = 'Settings/SolverSettings/EquilibriumStateSolverSettings/EquilibriumStateSolverSettings.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        None).merge(BladedModel._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


EquilibriumStateSolverSettings.update_forward_refs()

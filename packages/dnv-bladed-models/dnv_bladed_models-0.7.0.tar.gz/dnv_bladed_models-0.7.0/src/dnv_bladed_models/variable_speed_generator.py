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
from dnv_bladed_models.generator import Generator

from .schema_helper import SchemaHelper
from .models_impl import *


class VariableSpeedGenerator(Generator):
    r"""
    A variable speed generator where the torque is actively controlled by the controller.
    
    Attributes
    ----------
    ComponentType : Literal['VariableSpeedGenerator'], default='VariableSpeedGenerator'
        Defines the specific type of Component model in use.  For a `VariableSpeedGenerator` object, this must always be set to a value of `VariableSpeedGenerator`.
    
    GeneratorTimeConstant : float, default=0
        Time constant of generator torque response to demanded torque
    
    PowerFactor : float, default=1
        Turbine power factor
    
    MaximumTorqueDemand : float
        The upper limit for the torque demand.
    
    MinimumTorqueDemand : float, default=0
        The lower limit for the torque demand.
    
    Notes
    -----
    
    """
    ComponentType: Literal['VariableSpeedGenerator'] = Field(alias="ComponentType", default='VariableSpeedGenerator', allow_mutation=False, const=True) # type: ignore
    GeneratorTimeConstant: float = Field(alias="GeneratorTimeConstant", default=None)
    PowerFactor: float = Field(alias="PowerFactor", default=None)
    MaximumTorqueDemand: float = Field(alias="MaximumTorqueDemand", default=None)
    MinimumTorqueDemand: float = Field(alias="MinimumTorqueDemand", default=None)

    _relative_schema_path = 'Components/Generator/VariableSpeedGenerator.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'ComponentType').merge(Generator._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


VariableSpeedGenerator.update_forward_refs()

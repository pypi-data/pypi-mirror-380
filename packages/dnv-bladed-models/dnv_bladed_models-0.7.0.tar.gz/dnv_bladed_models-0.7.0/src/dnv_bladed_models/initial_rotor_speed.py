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
from dnv_bladed_models.initial_condition import InitialCondition

from .schema_helper import SchemaHelper
from .models_impl import *


class InitialRotorSpeed(InitialCondition):
    r"""
    The rotor speed.  If there is only one rotor or all rotors have the same initial speed, then AssemblyReference can be omitted.
    
    Attributes
    ----------
    InitialConditionType : Literal['InitialRotorSpeed'], default='InitialRotorSpeed'
        Defines the specific type of InitialCondition model in use.  For a `InitialRotorSpeed` object, this must always be set to a value of `InitialRotorSpeed`.
    
    RotorSpeed : float
        The rotor speed to use during initial conditions.  If omitted, Bladed will attempt to determine a combination of generator torque and pitch angle that would result in the rotor operating at a constant speed.  Once the simulation begins, environmental and control changes can result in this speed changing unless MaintainInitialValueThroughoutSimulation is true.
    
    MaintainInitialValueThroughoutSimulation : bool, default=False
        If true, the rotor speed will be prescribed to maintain whatever speed was determined during initial conditions.  This cannot be overcome by aerodynamic loads or other physical forces, and the generator torque will become irrelevant.
    
    Notes
    -----
    
    """
    InitialConditionType: Literal['InitialRotorSpeed'] = Field(alias="InitialConditionType", default='InitialRotorSpeed', allow_mutation=False, const=True) # type: ignore
    RotorSpeed: float = Field(alias="RotorSpeed", default=None)
    MaintainInitialValueThroughoutSimulation: bool = Field(alias="MaintainInitialValueThroughoutSimulation", default=None)

    _relative_schema_path = 'TimeDomainSimulation/InitialCondition/InitialRotorSpeed.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'InitialConditionType').merge(InitialCondition._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


InitialRotorSpeed.update_forward_refs()

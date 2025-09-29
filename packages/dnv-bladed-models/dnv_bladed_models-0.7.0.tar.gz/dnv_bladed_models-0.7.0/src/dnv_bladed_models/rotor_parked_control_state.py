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
from dnv_bladed_models.initial_control_state import InitialControlState

from .schema_helper import SchemaHelper
from .models_impl import *


class RotorParkedControlState(InitialControlState):
    r"""
    The initial condition of the rotor or turbine being parked.  The external controller is still able to change the state of the turbine during the simulation.
    
    Attributes
    ----------
    InitialConditionType : Literal['RotorParked'], default='RotorParked'
        Defines the specific type of InitialCondition model in use.  For a `RotorParked` object, this must always be set to a value of `RotorParked`.
    
    IsControllerActive : bool
        If true, the controller is active and can change the state of the turbine.
    
    Notes
    -----
    
    """
    InitialConditionType: Literal['RotorParked'] = Field(alias="InitialConditionType", default='RotorParked', allow_mutation=False, const=True) # type: ignore
    IsControllerActive: bool = Field(alias="IsControllerActive", default=None)

    _relative_schema_path = 'TimeDomainSimulation/InitialCondition/RotorParkedControlState.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'InitialConditionType').merge(InitialControlState._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


RotorParkedControlState.update_forward_refs()

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
from dnv_bladed_models.initial_position import InitialPosition

from .schema_helper import SchemaHelper
from .models_impl import *


class InitialPitchPosition(InitialPosition):
    r"""
    The initial pitch angle of a pitch system.  If all pitch systems have the same initial position, then AssemblyReference can be omitted.
    
    Attributes
    ----------
    InitialConditionType : Literal['InitialPitchPosition'], default='InitialPitchPosition'
        Defines the specific type of InitialCondition model in use.  For a `InitialPitchPosition` object, this must always be set to a value of `InitialPitchPosition`.
    
    PitchAngle : float
        The pitch angle to use during initial conditions.  If omitted, Bladed will attempt to determine a pitch angle that would achieve equilibrium.  Once initial conditions have been determined and the simulation begins, this angle is subject to control changes.
    
    MaintainInitialValueThroughoutSimulation : bool, default=False
        If true, the pitch system will be prescribed to maintain whatever pitch angle was determined during initial conditions.  This cannot be overcome by aerodynamic loads or other physical forces.
    
    Notes
    -----
    
    """
    InitialConditionType: Literal['InitialPitchPosition'] = Field(alias="InitialConditionType", default='InitialPitchPosition', allow_mutation=False, const=True) # type: ignore
    PitchAngle: float = Field(alias="PitchAngle", default=None)
    MaintainInitialValueThroughoutSimulation: bool = Field(alias="MaintainInitialValueThroughoutSimulation", default=None)

    _relative_schema_path = 'TimeDomainSimulation/InitialCondition/InitialPitchPosition.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'InitialConditionType').merge(InitialPosition._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


InitialPitchPosition.update_forward_refs()

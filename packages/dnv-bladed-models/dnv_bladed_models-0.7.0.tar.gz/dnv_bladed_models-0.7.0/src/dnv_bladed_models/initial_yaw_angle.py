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


class InitialYawAngle(InitialPosition):
    r"""
    The initial position of the yaw system.
    
    Attributes
    ----------
    InitialConditionType : Literal['InitialYawAngle'], default='InitialYawAngle'
        Defines the specific type of InitialCondition model in use.  For a `InitialYawAngle` object, this must always be set to a value of `InitialYawAngle`.
    
    YawAngle : float
        The yaw angle of the yaw system.
    
    MaintainInitialValueThroughoutSimulation : bool, default=False
        If true, the yaw system will be prescribed to maintain whatever yaw angle was determined during initial conditions.  This cannot be overcome by aerodynamic loads or other physical forces.
    
    Notes
    -----
    
    """
    InitialConditionType: Literal['InitialYawAngle'] = Field(alias="InitialConditionType", default='InitialYawAngle', allow_mutation=False, const=True) # type: ignore
    YawAngle: float = Field(alias="YawAngle", default=None)
    MaintainInitialValueThroughoutSimulation: bool = Field(alias="MaintainInitialValueThroughoutSimulation", default=None)

    _relative_schema_path = 'TimeDomainSimulation/InitialCondition/InitialYawAngle.json'
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


InitialYawAngle.update_forward_refs()

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
from dnv_bladed_models.dynamic_stall import DynamicStall

from .schema_helper import SchemaHelper
from .models_impl import *


class IAGModel(DynamicStall):
    r"""
    The IAG dynamic stall model.
    
    Attributes
    ----------
    DynamicStallType : Literal['IAGModel'], default='IAGModel'
        Defines the specific type of DynamicStall model in use.  For a `IAGModel` object, this must always be set to a value of `IAGModel`.
    
    UseImpulsiveContributions : bool, default=True
        Enabling the impulsive contributions in lift and moment coefficient.
    
    PressureLagTimeConstant : float, default=1.7
        The lag between the pressure and the lift.
    
    VortexLiftTimeConstant : float, default=6
        The rate of decay of the vortex induced lift that is generated when aerofoils undergo a rapid change in angle of attack towards positive or negative stall.
    
    VortexTravelTimeConstant : float, default=6
        The time constant that controls the duration of the vortex induced lift that is generated when aerofoils undergo a rapid change in angle of attack towards positive or negative stall.
    
    AttachedFlowConstantA1 : float, default=0.3
        The constant A1 for the IAG dynamic stall model to control the attached flow states.
    
    AttachedFlowConstantA2 : float, default=0.7
        The constant A2 for the IAG dynamic stall model to control the attached flow states.
    
    AttachedFlowConstantB1 : float, default=0.7
        The constant B1 for the IAG dynamic stall model to control the attached flow states.
    
    AttachedFlowConstantB2 : float, default=0.53
        The constant B2 for the IAG dynamic stall model to control the attached flow states.
    
    Notes
    -----
    
    """
    DynamicStallType: Literal['IAGModel'] = Field(alias="DynamicStallType", default='IAGModel', allow_mutation=False, const=True) # type: ignore
    UseImpulsiveContributions: bool = Field(alias="UseImpulsiveContributions", default=None)
    PressureLagTimeConstant: float = Field(alias="PressureLagTimeConstant", default=None)
    VortexLiftTimeConstant: float = Field(alias="VortexLiftTimeConstant", default=None)
    VortexTravelTimeConstant: float = Field(alias="VortexTravelTimeConstant", default=None)
    AttachedFlowConstantA1: float = Field(alias="AttachedFlowConstantA1", default=None)
    AttachedFlowConstantA2: float = Field(alias="AttachedFlowConstantA2", default=None)
    AttachedFlowConstantB1: float = Field(alias="AttachedFlowConstantB1", default=None)
    AttachedFlowConstantB2: float = Field(alias="AttachedFlowConstantB2", default=None)

    _relative_schema_path = 'Settings/AerodynamicSettings/DynamicStall/IAGModel.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'DynamicStallType').merge(DynamicStall._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


IAGModel.update_forward_refs()

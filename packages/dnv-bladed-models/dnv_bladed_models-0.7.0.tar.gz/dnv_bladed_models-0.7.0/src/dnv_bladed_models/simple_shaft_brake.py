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
from dnv_bladed_models.brake import Brake

from .schema_helper import SchemaHelper
from .models_impl import *


class SimpleShaftBrake(Brake):
    r"""
    The definition of a simple shaft brake whose retarding torque will increase linearly over a set time.
    
    Attributes
    ----------
    BrakeType : Literal['SimpleShaftBrake'], default='SimpleShaftBrake'
        Defines the specific type of Brake model in use.  For a `SimpleShaftBrake` object, this must always be set to a value of `SimpleShaftBrake`.
    
    MaximumTorque : float
        The maximum retarding torque to apply to the shaft.
    
    RampTime : float
        The amount of time following the brake's activation to reach maximum torque.
    
    Notes
    -----
    
    """
    BrakeType: Literal['SimpleShaftBrake'] = Field(alias="BrakeType", default='SimpleShaftBrake', allow_mutation=False, const=True) # type: ignore
    MaximumTorque: float = Field(alias="MaximumTorque", default=None)
    RampTime: float = Field(alias="RampTime", default=None)

    _relative_schema_path = 'Components/DrivetrainAndNacelle/Brake/SimpleShaftBrake.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'BrakeType').merge(Brake._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


SimpleShaftBrake.update_forward_refs()

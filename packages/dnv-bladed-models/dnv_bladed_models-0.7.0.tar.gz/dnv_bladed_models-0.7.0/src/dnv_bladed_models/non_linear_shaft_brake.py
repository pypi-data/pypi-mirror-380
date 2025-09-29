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
from dnv_bladed_models.time_vs_torque import TimeVsTorque

from .schema_helper import SchemaHelper
from .models_impl import *


class NonLinearShaftBrake(Brake):
    r"""
    The definition of a shaft brake whose applied torque varies with time.
    
    Attributes
    ----------
    BrakeType : Literal['NonLinearShaftBrake'], default='NonLinearShaftBrake'
        Defines the specific type of Brake model in use.  For a `NonLinearShaftBrake` object, this must always be set to a value of `NonLinearShaftBrake`.
    
    TimeVsTorque : List[TimeVsTorque]
        The relationship between the time following the brake's activation, and the retarding torque it applies to the shaft.
    
    Notes
    -----
    
    """
    BrakeType: Literal['NonLinearShaftBrake'] = Field(alias="BrakeType", default='NonLinearShaftBrake', allow_mutation=False, const=True) # type: ignore
    TimeVsTorque: List[TimeVsTorque] = Field(alias="TimeVsTorque", default=list())

    _relative_schema_path = 'Components/DrivetrainAndNacelle/Brake/NonLinearShaftBrake.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set(['TimeVsTorque',]),
        'BrakeType').merge(Brake._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


NonLinearShaftBrake.update_forward_refs()

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


class LoadBank(BladedModel):
    r"""
    The properties of a load bank.
    
    Attributes
    ----------
    HighSpeedShaftStiffness : float
        The stiffness of the high speed shaft. Obmiting this will be it rigid. If omitted, the shaft will be rigid.
    
    HighSpeedShaftDamping : float
        The coefficient of damping for the high speed shaft. If omitted, the shaft will be rigid.
    
    MomentOfInertiaOfMotor : float
        The inertia of the motor/actuator connected to this HSS.
    
    Notes
    -----
    
    """
    HighSpeedShaftStiffness: float = Field(alias="HighSpeedShaftStiffness", default=None)
    HighSpeedShaftDamping: float = Field(alias="HighSpeedShaftDamping", default=None)
    MomentOfInertiaOfMotor: float = Field(alias="MomentOfInertiaOfMotor", default=None)

    _relative_schema_path = 'Components/YawSystem/YawActuation/LoadBank/LoadBank.json'
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


LoadBank.update_forward_refs()

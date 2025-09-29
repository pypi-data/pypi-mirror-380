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
from dnv_bladed_models.yaw_fault import YawFault

from .schema_helper import SchemaHelper
from .models_impl import *


class YawFaultConstantRate(YawFault):
    r"""
    A fault in the yaw system where the yaw system moves at a constant rate until it reaches an end stop.
    
    Not supported yet.
    
    Attributes
    ----------
    EventType : Literal['YawFaultConstantRate'], default='YawFaultConstantRate', Not supported yet
        Defines the specific type of Event model in use.  For a `YawFaultConstantRate` object, this must always be set to a value of `YawFaultConstantRate`.
    
    FaultYawRate : float, Not supported yet
        The rate at which the yaw system will move until it reaches an end stop.
    
    YawEndStop : float, Not supported yet
        The angle at which the yaw system's end stop is placed.  The movement will cease once the yaw bearing has reached this angle.
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    EventType: Literal['YawFaultConstantRate'] = Field(alias="EventType", default='YawFaultConstantRate', allow_mutation=False, const=True) # Not supported yet # type: ignore
    FaultYawRate: float = Field(alias="FaultYawRate", default=None) # Not supported yet
    YawEndStop: float = Field(alias="YawEndStop", default=None) # Not supported yet

    _relative_schema_path = 'TimeDomainSimulation/Event/YawFaultConstantRate.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'EventType').merge(YawFault._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


YawFaultConstantRate.update_forward_refs()

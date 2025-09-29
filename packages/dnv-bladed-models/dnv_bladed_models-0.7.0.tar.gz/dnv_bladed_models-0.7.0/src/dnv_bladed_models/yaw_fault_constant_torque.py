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


class YawFaultConstantTorque(YawFault):
    r"""
    A fault in the yaw system where the actuator applies a constant torque.
    
    Not supported yet.
    
    Attributes
    ----------
    EventType : Literal['YawFaultConstantTorque'], default='YawFaultConstantTorque', Not supported yet
        Defines the specific type of Event model in use.  For a `YawFaultConstantTorque` object, this must always be set to a value of `YawFaultConstantTorque`.
    
    Torque : float, Not supported yet
        The torque applied by the actuator in its failed state.
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    EventType: Literal['YawFaultConstantTorque'] = Field(alias="EventType", default='YawFaultConstantTorque', allow_mutation=False, const=True) # Not supported yet # type: ignore
    Torque: float = Field(alias="Torque", default=None) # Not supported yet

    _relative_schema_path = 'TimeDomainSimulation/Event/YawFaultConstantTorque.json'
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


YawFaultConstantTorque.update_forward_refs()

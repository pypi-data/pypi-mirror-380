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
from dnv_bladed_models.fault import Fault

from .schema_helper import SchemaHelper
from .models_impl import *


class ControllerFault(Fault):
    r"""
    A controller fault occuring at a specified time.  A signal will be sent to the controller, and the controller will be expected to implement the fault behaviour.
    
    Attributes
    ----------
    EventType : Literal['ControllerFault'], default='ControllerFault'
        Defines the specific type of Event model in use.  For a `ControllerFault` object, this must always be set to a value of `ControllerFault`.
    
    FaultCode : int
        A fault number that will be provided to the controller.  It is for the controller to decide how to react to this number.
    
    FaultParametersAsString : str
        A string and passed to the external controller at the time the fault occurs.
    
    FaultParametersAsJson : Dict[str, Any]
        A JSON object that will be serialised as a string and passed to the external controller at the time the fault occurs.
    
    Notes
    -----
    
    """
    EventType: Literal['ControllerFault'] = Field(alias="EventType", default='ControllerFault', allow_mutation=False, const=True) # type: ignore
    FaultCode: int = Field(alias="FaultCode", default=None)
    FaultParametersAsString: str = Field(alias="FaultParametersAsString", default=None)
    FaultParametersAsJson: Dict[str, Any] = Field(alias="FaultParametersAsJson", default=None)

    _relative_schema_path = 'TimeDomainSimulation/Event/ControllerFault.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'EventType').merge(Fault._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


ControllerFault.update_forward_refs()

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
from dnv_bladed_models.actuator_response import ActuatorResponse

from .schema_helper import SchemaHelper
from .models_impl import *


class SecondOrderActuatorResponse(ActuatorResponse):
    r"""
    Defines a second-order response to the controller's demands.
    
    Attributes
    ----------
    ActuatorResponseType : Literal['SecondOrderActuatorResponse'], default='SecondOrderActuatorResponse'
        Defines the specific type of ActuatorResponse model in use.  For a `SecondOrderActuatorResponse` object, this must always be set to a value of `SecondOrderActuatorResponse`.
    
    Frequency : float, default=6.28318530717959
        The angular frequency of oscillation of response.
    
    Damping : float, default=0.8
        The fraction of critical damping.
    
    Notes
    -----
    
    """
    ActuatorResponseType: Literal['SecondOrderActuatorResponse'] = Field(alias="ActuatorResponseType", default='SecondOrderActuatorResponse', allow_mutation=False, const=True) # type: ignore
    Frequency: float = Field(alias="Frequency", default=None)
    Damping: float = Field(alias="Damping", default=None)

    _relative_schema_path = 'Components/PitchSystem/PitchActuator/ActuatorResponse/SecondOrderActuatorResponse.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'ActuatorResponseType').merge(ActuatorResponse._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


SecondOrderActuatorResponse.update_forward_refs()

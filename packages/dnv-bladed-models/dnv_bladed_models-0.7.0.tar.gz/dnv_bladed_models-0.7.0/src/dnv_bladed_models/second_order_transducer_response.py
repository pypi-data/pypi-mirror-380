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
from dnv_bladed_models.transducer_behaviour import TransducerBehaviour

from .schema_helper import SchemaHelper
from .models_impl import *


class SecondOrderTransducerResponse(TransducerBehaviour):
    r"""
    
    
    Not supported yet.
    
    Attributes
    ----------
    TransducerBehaviourType : Literal['SecondOrderTransducerResponse'], default='SecondOrderTransducerResponse', Not supported yet
        Defines the specific type of TransducerBehaviour model in use.  For a `SecondOrderTransducerResponse` object, this must always be set to a value of `SecondOrderTransducerResponse`.
    
    Frequency : float, default=6.28318530717959, Not supported yet
        The angular frequency of oscillation of response.
    
    Damping : float, default=0.8, Not supported yet
        The fraction of critical damping.
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    TransducerBehaviourType: Literal['SecondOrderTransducerResponse'] = Field(alias="TransducerBehaviourType", default='SecondOrderTransducerResponse', allow_mutation=False, const=True) # Not supported yet # type: ignore
    Frequency: float = Field(alias="Frequency", default=None) # Not supported yet
    Damping: float = Field(alias="Damping", default=None) # Not supported yet

    _relative_schema_path = 'Turbine/BladedControl/MeasuredSignalProperties/common/SecondOrderTransducerResponse.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'TransducerBehaviourType').merge(TransducerBehaviour._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


SecondOrderTransducerResponse.update_forward_refs()

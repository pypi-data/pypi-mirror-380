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


class PassiveTransducerResponse(TransducerBehaviour):
    r"""
    
    
    Not supported yet.
    
    Attributes
    ----------
    TransducerBehaviourType : Literal['PassiveTransducerResponse'], default='PassiveTransducerResponse', Not supported yet
        Defines the specific type of TransducerBehaviour model in use.  For a `PassiveTransducerResponse` object, this must always be set to a value of `PassiveTransducerResponse`.
    
    Numerators : List[float], Not supported yet
        The numerators of the transfer function. Transfer function must be at least second order.
    
    Denominators : List[float], Not supported yet
        The denominators of the transfer function. Transfer function must be at least second order.
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    TransducerBehaviourType: Literal['PassiveTransducerResponse'] = Field(alias="TransducerBehaviourType", default='PassiveTransducerResponse', allow_mutation=False, const=True) # Not supported yet # type: ignore
    Numerators: List[float] = Field(alias="Numerators", default=list()) # Not supported yet
    Denominators: List[float] = Field(alias="Denominators", default=list()) # Not supported yet

    _relative_schema_path = 'Turbine/BladedControl/MeasuredSignalProperties/common/PassiveTransducerResponse.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set(['Numerators','Denominators',]),
        'TransducerBehaviourType').merge(TransducerBehaviour._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


PassiveTransducerResponse.update_forward_refs()

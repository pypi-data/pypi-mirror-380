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
from dnv_bladed_models.wind_shear import WindShear

from .schema_helper import SchemaHelper
from .models_impl import *


class LogarithmicShearModel(WindShear):
    r"""
    The wind shear to apply to the wind field.
    
    Attributes
    ----------
    WindShearType : Literal['LogarithmicShearModel'], default='LogarithmicShearModel'
        Defines the specific type of WindShear model in use.  For a `LogarithmicShearModel` object, this must always be set to a value of `LogarithmicShearModel`.
    
    SurfaceRoughness : float
        The surface roughness, used to determine the shape of the wind shear variation.
    
    Notes
    -----
    
    """
    WindShearType: Literal['LogarithmicShearModel'] = Field(alias="WindShearType", default='LogarithmicShearModel', allow_mutation=False, const=True) # type: ignore
    SurfaceRoughness: float = Field(alias="SurfaceRoughness", default=None)

    _relative_schema_path = 'common/LogarithmicShearModel.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'WindShearType').merge(WindShear._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


LogarithmicShearModel.update_forward_refs()

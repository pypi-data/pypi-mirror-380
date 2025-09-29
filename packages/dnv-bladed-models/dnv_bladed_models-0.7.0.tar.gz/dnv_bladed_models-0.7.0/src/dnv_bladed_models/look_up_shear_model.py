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
from dnv_bladed_models.height_vs_shear_factor import HeightVsShearFactor
from dnv_bladed_models.wind_shear import WindShear

from .schema_helper import SchemaHelper
from .models_impl import *


class LookUpShearModel(WindShear):
    r"""
    The wind shear to apply to the wind field.
    
    Attributes
    ----------
    WindShearType : Literal['LookUpShearModel'], default='LookUpShearModel'
        Defines the specific type of WindShear model in use.  For a `LookUpShearModel` object, this must always be set to a value of `LookUpShearModel`.
    
    HeightVsShearFactor : List[HeightVsShearFactor]
        A series of height vs shear factors, including a point at the reference height (above which normal flow begins) and 0.0 (ground level).
    
    Notes
    -----
    
    """
    WindShearType: Literal['LookUpShearModel'] = Field(alias="WindShearType", default='LookUpShearModel', allow_mutation=False, const=True) # type: ignore
    HeightVsShearFactor: List[HeightVsShearFactor] = Field(alias="HeightVsShearFactor", default=list())

    _relative_schema_path = 'common/LookUpShearModel.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set(['HeightVsShearFactor',]),
        'WindShearType').merge(WindShear._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


LookUpShearModel.update_forward_refs()

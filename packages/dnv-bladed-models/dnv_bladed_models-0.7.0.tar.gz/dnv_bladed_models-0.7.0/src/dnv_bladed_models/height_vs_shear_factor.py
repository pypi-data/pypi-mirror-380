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


class HeightVsShearFactor(BladedModel):
    r"""
    A single height vs shear factor point.
    
    Attributes
    ----------
    Height : float
        The height above the ground.  This should vary from 0.0 up to the reference height, above which normal flow resumes.
    
    ShearFactor : float
        The shear factor, varying from 0.0 (no wind) up to 1.0 (full flow).
    
    Notes
    -----
    
    """
    Height: float = Field(alias="Height", default=None)
    ShearFactor: float = Field(alias="ShearFactor", default=None)

    _relative_schema_path = 'common/HeightVsShearFactor.json'
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


HeightVsShearFactor.update_forward_refs()

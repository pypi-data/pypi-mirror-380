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
from dnv_bladed_models.foundation import Foundation

from .schema_helper import SchemaHelper
from .models_impl import *


class SimplifiedLinearFoundation(Foundation):
    r"""
    Foundation type ?.  This *may* be a super-simple foundation.
    
    Attributes
    ----------
    FoundationType : Literal['SimplifiedLinearFoundation'], default='SimplifiedLinearFoundation'
        Defines the specific type of Foundation model in use.  For a `SimplifiedLinearFoundation` object, this must always be set to a value of `SimplifiedLinearFoundation`.
    
    TranslationalStiffness : float
        Translational stiffness of foundation;KTRANS   Nm/rad Transitional stiffness of fopundation  Omit if no translation permited (TRANDOF is null).
    
    Mass : float, default=24000
        Foundation mass;FMASS       kg  Mass of foundation
    
    RotationalStiffness : float
        Rotational stiffness of foundation;KROT       N/m  Rotational stiffness of foundation  Omit if no translation permited (ROTDOF is null).
    
    RotationalInertia : float, default=380000
        Moment of inertia of foundation;FOUNDI     kgmÂ² Inertia of foundation mass about a horizontal axis at tower base
    
    Notes
    -----
    
    """
    FoundationType: Literal['SimplifiedLinearFoundation'] = Field(alias="FoundationType", default='SimplifiedLinearFoundation', allow_mutation=False, const=True) # type: ignore
    TranslationalStiffness: float = Field(alias="TranslationalStiffness", default=None)
    Mass: float = Field(alias="Mass", default=None)
    RotationalStiffness: float = Field(alias="RotationalStiffness", default=None)
    RotationalInertia: float = Field(alias="RotationalInertia", default=None)

    _relative_schema_path = 'Components/Tower/Foundation/SimplifiedLinearFoundation.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'FoundationType').merge(Foundation._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


SimplifiedLinearFoundation.update_forward_refs()

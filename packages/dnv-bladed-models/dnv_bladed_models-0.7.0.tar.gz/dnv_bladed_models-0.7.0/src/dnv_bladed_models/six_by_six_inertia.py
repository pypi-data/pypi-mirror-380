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
from dnv_bladed_models.added_inertia import AddedInertia

from .schema_helper import SchemaHelper
from .models_impl import *


class SixBySixInertia(AddedInertia):
    r"""
    An inertia added to a structural component specified with a 6x6 inertia matrix.
    
    Attributes
    ----------
    AddedInertiaType : Literal['SixBySixInertia'], default='SixBySixInertia'
        Defines the specific type of AddedInertia model in use.  For a `SixBySixInertia` object, this must always be set to a value of `SixBySixInertia`.
    
    Inertia : List[List[float]]
        A 6x6 matrix of the linear and rotational inertias of an object.
    
    Notes
    -----
    
    """
    AddedInertiaType: Literal['SixBySixInertia'] = Field(alias="AddedInertiaType", default='SixBySixInertia', allow_mutation=False, const=True) # type: ignore
    Inertia: List[List[float]] = Field(alias="Inertia", default=list())

    _relative_schema_path = 'Components/Tower/AddedInertia/SixBySixInertia.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set(['Inertia',]),
        'AddedInertiaType').merge(AddedInertia._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


SixBySixInertia.update_forward_refs()

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
from dnv_bladed_models.standard_hub import StandardHub

from .schema_helper import SchemaHelper
from .models_impl import *


class IndependentPitchHub(StandardHub):
    r"""
    A standard hub with two or more blades, and one pitch system for each blade.
    
    Attributes
    ----------
    ComponentType : Literal['IndependentPitchHub'], default='IndependentPitchHub'
        Defines the specific type of Component model in use.  For a `IndependentPitchHub` object, this must always be set to a value of `IndependentPitchHub`.
    
    Notes
    -----
    
    """
    ComponentType: Literal['IndependentPitchHub'] = Field(alias="ComponentType", default='IndependentPitchHub', allow_mutation=False, const=True) # type: ignore

    _relative_schema_path = 'Components/Hub/IndependentPitchHub.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'ComponentType').merge(StandardHub._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


IndependentPitchHub.update_forward_refs()

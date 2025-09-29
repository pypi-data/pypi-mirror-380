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
from dnv_bladed_models.structural_modelling import StructuralModelling

from .schema_helper import SchemaHelper
from .models_impl import *


class RigidStructuralModelling(StructuralModelling):
    r"""
    The properties for modelling as being completely rigid.
    
    Attributes
    ----------
    StructuralModellingType : Literal['RigidStructuralModelling'], default='RigidStructuralModelling'
        Defines the specific type of StructuralModelling model in use.  For a `RigidStructuralModelling` object, this must always be set to a value of `RigidStructuralModelling`.
    
    Notes
    -----
    
    """
    StructuralModellingType: Literal['RigidStructuralModelling'] = Field(alias="StructuralModellingType", default='RigidStructuralModelling', allow_mutation=False, const=True) # type: ignore

    _relative_schema_path = 'Components/StructuralModelling/RigidStructuralModelling.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'StructuralModellingType').merge(StructuralModelling._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


RigidStructuralModelling.update_forward_refs()

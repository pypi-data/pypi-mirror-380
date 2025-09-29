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
from dnv_bladed_models.rigid_body_inertia import RigidBodyInertia

from .schema_helper import SchemaHelper
from .models_impl import *


class RigidBodySixbySixInertia(RigidBodyInertia):
    r"""
    An inertia component to the assembly tree, defined via a six-by-six matrix.
    
    Attributes
    ----------
    ComponentType : Literal['RigidBodySixbySixInertia'], default='RigidBodySixbySixInertia'
        Defines the specific type of Component model in use.  For a `RigidBodySixbySixInertia` object, this must always be set to a value of `RigidBodySixbySixInertia`.
    
    Inertia : List[List[float]]
        A 6x6 matrix of the linear and rotational inertias of an object.
    
    Notes
    -----
    
    """
    ComponentType: Literal['RigidBodySixbySixInertia'] = Field(alias="ComponentType", default='RigidBodySixbySixInertia', allow_mutation=False, const=True) # type: ignore
    Inertia: List[List[float]] = Field(alias="Inertia", default=list())

    _relative_schema_path = 'Components/RigidBodySixbySixInertia.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set(['Inertia',]),
        'ComponentType').merge(RigidBodyInertia._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


RigidBodySixbySixInertia.update_forward_refs()

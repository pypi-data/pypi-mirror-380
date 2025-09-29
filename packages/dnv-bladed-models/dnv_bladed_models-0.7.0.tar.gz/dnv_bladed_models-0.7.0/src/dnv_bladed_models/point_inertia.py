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
from dnv_bladed_models.vector3_d import Vector3D

from .schema_helper import SchemaHelper
from .models_impl import *


class PointInertia(AddedInertia):
    r"""
    An inertia added to a structural component.
    
    Attributes
    ----------
    AddedInertiaType : Literal['PointInertia'], default='PointInertia'
        Defines the specific type of AddedInertia model in use.  For a `PointInertia` object, this must always be set to a value of `PointInertia`.
    
    Mass : float, default=0
        The mass to be added.
    
    Offset : Vector3D
    
    MomentOfInertiaTensor : List[float], default=[0,0,0]
        Moment of inertia tensor acting about the centre of mass. This tensor is defined using the local coordinate system of the attachment node.
    
    CompleteInertiaTensor : float, default=0
        The symmetric inertia tensor acting about the attachment node. This tensor is defined using the local coordinate system of the attachment node.
    
    Notes
    -----
    
    """
    AddedInertiaType: Literal['PointInertia'] = Field(alias="AddedInertiaType", default='PointInertia', allow_mutation=False, const=True) # type: ignore
    Mass: float = Field(alias="Mass", default=None)
    Offset: Vector3D = Field(alias="Offset", default=None)
    MomentOfInertiaTensor: List[float] = Field(alias="MomentOfInertiaTensor", default=list())
    CompleteInertiaTensor: float = Field(alias="CompleteInertiaTensor", default=None)

    _relative_schema_path = 'Components/Tower/AddedInertia/PointInertia.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set(['MomentOfInertiaTensor',]),
        'AddedInertiaType').merge(AddedInertia._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


PointInertia.update_forward_refs()

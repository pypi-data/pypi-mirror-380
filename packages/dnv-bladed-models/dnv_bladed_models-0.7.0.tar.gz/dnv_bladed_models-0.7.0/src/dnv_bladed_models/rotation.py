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
from dnv_bladed_models.component import Component
from dnv_bladed_models.vector3_d import Vector3D

from .schema_helper import SchemaHelper
from .models_impl import *


class Rotation(Component):
    r"""
    A change in orientation between two components, or the origin - [0,0,0] - and the first component in the Assembly tree.  This will be modelled as completely rigid.
    
    Attributes
    ----------
    ComponentType : Literal['Rotation'], default='Rotation'
        Defines the specific type of Component model in use.  For a `Rotation` object, this must always be set to a value of `Rotation`.
    
    AxisOfRotation : Vector3D
    
    AngleOfRotation : float
        The angle to rotate around the AxisOfRotation, following the right-hand-rule.
    
    Notes
    -----
    
    """
    ComponentType: Literal['Rotation'] = Field(alias="ComponentType", default='Rotation', allow_mutation=False, const=True) # type: ignore
    AxisOfRotation: Vector3D = Field(alias="AxisOfRotation", default=None)
    AngleOfRotation: float = Field(alias="AngleOfRotation", default=None)

    _relative_schema_path = 'Components/Rotation.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'ComponentType').merge(Component._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


Rotation.update_forward_refs()

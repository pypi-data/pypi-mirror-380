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


class OffsetAndRotatedCoordinateSystem(BladedModel):
    r"""
    The X- and Y-offsets and a rotation, relative to the ReferenceCoordinateSystem, are used to position and orient a coordinate system.
    
    Attributes
    ----------
    OffsetInReferenceX : float, default=0
        The X-offset of the coordinate system origin along the reference X-axis, relative to the ReferenceCoordinateSystem.
    
    OffsetInReferenceY : float, default=0
        The Y-offset of the coordinate system origin along the reference Y-axis, relative to the ReferenceCoordinateSystem.
    
    RotationAboutReferenceZ : float, default=0
        The rotation of the coordinate system's X- and Y-axes around the reference Z-axis (the section plane normal).
    
    Notes
    -----
    
    """
    OffsetInReferenceX: float = Field(alias="OffsetInReferenceX", default=None)
    OffsetInReferenceY: float = Field(alias="OffsetInReferenceY", default=None)
    RotationAboutReferenceZ: float = Field(alias="RotationAboutReferenceZ", default=None)

    _relative_schema_path = 'Components/Blade/CrossSection/CoordinateSystems/OffsetAndRotatedCoordinateSystem/OffsetAndRotatedCoordinateSystem.json'
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


OffsetAndRotatedCoordinateSystem.update_forward_refs()

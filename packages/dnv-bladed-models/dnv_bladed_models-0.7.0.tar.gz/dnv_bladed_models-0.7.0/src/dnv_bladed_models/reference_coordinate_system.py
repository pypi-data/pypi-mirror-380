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
from dnv_bladed_models.point_on_span import PointOnSpan
from dnv_bladed_models.vector3_d import Vector3D

from .schema_helper import SchemaHelper
from .models_impl import *


class ReferenceCoordinateSystem(BladedModel):
    r"""
    The main coordinate system of the cross-section, from which all other coordinate systems are derived.  If a coordinate system is not specified, it defaults to the ReferenceCoordinateSystem.  Consequently, any coordinate system may serve as the reference coordinate system.
    
    Attributes
    ----------
    Origin : PointOnSpan
    
    ZAxis : Vector3D
    
    RotationAboutReferenceZ : float
        This specifies the ReferenceCoordinateSystem's local Y-axis direction.  A vector specifying the YAxis explicitly can be provided instead, or without either the Y-axis will lie on the component's YZ-plane.
    
    YAxis : Vector3D
    
    Notes
    -----
    
    """
    Origin: PointOnSpan = Field(alias="Origin", default=None)
    ZAxis: Vector3D = Field(alias="ZAxis", default=None)
    RotationAboutReferenceZ: float = Field(alias="RotationAboutReferenceZ", default=None)
    YAxis: Vector3D = Field(alias="YAxis", default=None)

    _relative_schema_path = 'Components/Blade/CrossSection/CoordinateSystems/ReferenceCoordinateSystem/ReferenceCoordinateSystem.json'
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


ReferenceCoordinateSystem.update_forward_refs()

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
from dnv_bladed_models.offset_and_rotated_coordinate_system import OffsetAndRotatedCoordinateSystem
from dnv_bladed_models.reference_coordinate_system import ReferenceCoordinateSystem

from .schema_helper import SchemaHelper
from .models_impl import *


class CoordinateSystems(BladedModel):
    r"""
    The coordinate systems of the blade cross-section.  If a coordinate system is not specified, it defaults to the ReferenceCoordinateSystem.  Consequently, any coordinate system may serve as the reference coordinate system.
    
    Attributes
    ----------
    ReferenceCoordinateSystem : ReferenceCoordinateSystem
    
    QuarterChordCoordinateSystem : OffsetAndRotatedCoordinateSystem
    
    PrincipalInertiaCoordinateSystem : OffsetAndRotatedCoordinateSystem
    
    PrincipalElasticCoordinateSystem : OffsetAndRotatedCoordinateSystem
    
    PrincipalShearCoordinateSystem : OffsetAndRotatedCoordinateSystem
    
    Notes
    -----
    
    """
    ReferenceCoordinateSystem: ReferenceCoordinateSystem = Field(alias="ReferenceCoordinateSystem", default=None)
    QuarterChordCoordinateSystem: OffsetAndRotatedCoordinateSystem = Field(alias="QuarterChordCoordinateSystem", default=None)
    PrincipalInertiaCoordinateSystem: OffsetAndRotatedCoordinateSystem = Field(alias="PrincipalInertiaCoordinateSystem", default=None)
    PrincipalElasticCoordinateSystem: OffsetAndRotatedCoordinateSystem = Field(alias="PrincipalElasticCoordinateSystem", default=None)
    PrincipalShearCoordinateSystem: OffsetAndRotatedCoordinateSystem = Field(alias="PrincipalShearCoordinateSystem", default=None)

    _relative_schema_path = 'Components/Blade/CrossSection/CoordinateSystems/CoordinateSystems.json'
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


CoordinateSystems.update_forward_refs()

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


class PointOnSpan(BladedModel):
    r"""
    A position along the span of the blade, defined either in full 3D, or as if the blade had been flattened into 2D (i.e. disregarding pre-bend and pre-sweep).
    
    Attributes
    ----------
    X : float, default=0
        The offset of the point from the blade's pitch axis (the z-axis) in the blade root's X direction.
    
    Y : float, default=0
        The offset of the point from the blade's pitch axis (the z- axis) in the blade root's Y direction.
    
    Z : float
        The spanwise location of the point along the blade's pitch axis (the blade root axes' z-axis).  This is the absolute 3D position, including any pre-bend or pre-sweep.
    
    DistanceAlongSpan : float
        The spanwise location of the point along the blade's pitch axis (the blade root z-axis), as measured along the blade's reference curve, which connects the origins of each blade cross-section.  This would be the distance along the undeformed blade, should it lie flat in a plane.  This is used when the pre-bend and pre-sweep has yet to be finalised, as the PlanformDistance will remain constant for any value of X and Y.
    
    Notes
    -----
    
    """
    X: float = Field(alias="X", default=None)
    Y: float = Field(alias="Y", default=None)
    Z: float = Field(alias="Z", default=None)
    DistanceAlongSpan: float = Field(alias="DistanceAlongSpan", default=None)

    _relative_schema_path = 'Components/Blade/CrossSection/CoordinateSystems/ReferenceCoordinateSystem/PointOnSpan/PointOnSpan.json'
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


PointOnSpan.update_forward_refs()

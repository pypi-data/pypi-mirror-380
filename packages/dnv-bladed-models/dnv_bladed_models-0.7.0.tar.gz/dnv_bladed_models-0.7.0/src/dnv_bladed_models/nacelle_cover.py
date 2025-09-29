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
from dnv_bladed_models.vector3_d import Vector3D

from .schema_helper import SchemaHelper
from .models_impl import *


class NacelleCover(BladedModel):
    r"""
    A nacelle cover best represented by a cuboid.
    
    Attributes
    ----------
    Width : float
        The width (Y dimension) of the nacelle cover.
    
    Length : float
        The length (X dimension) of the nacelle cover.
    
    Height : float
        The height (Z dimension) of the nacelle cover.
    
    CentreOfPressure : Vector3D
    
    CoefficientOfDrag : float
        The coefficient of drag for the nacelle.
    
    Notes
    -----
    
    """
    Width: float = Field(alias="Width", default=None)
    Length: float = Field(alias="Length", default=None)
    Height: float = Field(alias="Height", default=None)
    CentreOfPressure: Vector3D = Field(alias="CentreOfPressure", default=None)
    CoefficientOfDrag: float = Field(alias="CoefficientOfDrag", default=None)

    _relative_schema_path = 'Components/DrivetrainAndNacelle/NacelleCover/NacelleCover.json'
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


NacelleCover.update_forward_refs()

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
from dnv_bladed_models.lidar_focal_distance_control import LidarFocalDistanceControl

from .schema_helper import SchemaHelper
from .models_impl import *


class ControllerLidarSettings(LidarFocalDistanceControl):
    r"""
    The focal distance is controlled by the external controller.
    
    Not supported yet.
    
    Attributes
    ----------
    FocalDistanceControlType : Literal['Controller'], default='Controller', Not supported yet
        Defines the specific type of FocalDistanceControl model in use.  For a `Controller` object, this must always be set to a value of `Controller`.
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    FocalDistanceControlType: Literal['Controller'] = Field(alias="FocalDistanceControlType", default='Controller', allow_mutation=False, const=True) # Not supported yet # type: ignore

    _relative_schema_path = 'Components/Lidar/LidarFocalDistanceControl/ControllerLidarSettings.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'FocalDistanceControlType').merge(LidarFocalDistanceControl._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


ControllerLidarSettings.update_forward_refs()

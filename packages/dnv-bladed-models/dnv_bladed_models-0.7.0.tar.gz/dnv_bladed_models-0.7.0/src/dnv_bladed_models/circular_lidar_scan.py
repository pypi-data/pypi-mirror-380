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
from dnv_bladed_models.preset_lidar_scan import PresetLidarScan

from .schema_helper import SchemaHelper
from .models_impl import *


class CircularLidarScan(PresetLidarScan):
    r"""
    A simple circular scan pattern.
    
    Not supported yet.
    
    Attributes
    ----------
    ScanningPatternType : Literal['CircularScan'], default='CircularScan', Not supported yet
        Defines the specific type of ScanningPattern model in use.  For a `CircularScan` object, this must always be set to a value of `CircularScan`.
    
    HalfAngle : float, Not supported yet
        The half-angle between centre of scan and scanning position.
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    ScanningPatternType: Literal['CircularScan'] = Field(alias="ScanningPatternType", default='CircularScan', allow_mutation=False, const=True) # Not supported yet # type: ignore
    HalfAngle: float = Field(alias="HalfAngle", default=None) # Not supported yet

    _relative_schema_path = 'Components/Lidar/LidarScanningPattern/CircularLidarScan.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'ScanningPatternType').merge(PresetLidarScan._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


CircularLidarScan.update_forward_refs()

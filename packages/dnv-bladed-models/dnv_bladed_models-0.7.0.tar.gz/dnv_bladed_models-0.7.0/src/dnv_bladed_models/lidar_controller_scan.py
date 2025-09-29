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
from dnv_bladed_models.lidar_scanning_pattern import LidarScanningPattern

from .schema_helper import SchemaHelper
from .models_impl import *


class LidarControllerScan(LidarScanningPattern):
    r"""
    Where the scan pattern is controlled by the turbine's controller.  The controller API will provide functions with which to move the beam.
    
    Not supported yet.
    
    Attributes
    ----------
    ScanningPatternType : Literal['ControllerScan'], default='ControllerScan', Not supported yet
        Defines the specific type of ScanningPattern model in use.  For a `ControllerScan` object, this must always be set to a value of `ControllerScan`.
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    ScanningPatternType: Literal['ControllerScan'] = Field(alias="ScanningPatternType", default='ControllerScan', allow_mutation=False, const=True) # Not supported yet # type: ignore

    _relative_schema_path = 'Components/Lidar/LidarScanningPattern/LidarControllerScan.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'ScanningPatternType').merge(LidarScanningPattern._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


LidarControllerScan.update_forward_refs()

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


class MultipleLidarFocalDistances(LidarFocalDistanceControl):
    r"""
    A set number of focal distances at which the Lidar samples.
    
    Not supported yet.
    
    Attributes
    ----------
    FocalDistanceControlType : Literal['MultipleFocalDistances'], default='MultipleFocalDistances', Not supported yet
        Defines the specific type of FocalDistanceControl model in use.  For a `MultipleFocalDistances` object, this must always be set to a value of `MultipleFocalDistances`.
    
    FocalDistances : List[float], Not supported yet
        A list of fixed focal distances.
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    FocalDistanceControlType: Literal['MultipleFocalDistances'] = Field(alias="FocalDistanceControlType", default='MultipleFocalDistances', allow_mutation=False, const=True) # Not supported yet # type: ignore
    FocalDistances: List[float] = Field(alias="FocalDistances", default=list()) # Not supported yet

    _relative_schema_path = 'Components/Lidar/LidarFocalDistanceControl/MultipleLidarFocalDistances.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set(['FocalDistances',]),
        'FocalDistanceControlType').merge(LidarFocalDistanceControl._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


MultipleLidarFocalDistances.update_forward_refs()

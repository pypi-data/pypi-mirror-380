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


class RotorImbalances(BladedModel):
    r"""
    The definition of any imbalances on the hub.
    
    Attributes
    ----------
    OutOfBalanceMass : float
        A mass to add off the centreline of the hub to represent the various mass imbalances and assymetries in the rotor.
    
    RadiusOfMass : float
        The radial location of the mass to add off the centreline of the hub to represent the various mass imbalances and assymetries in the rotor.
    
    AzimuthalPositionOfMass : float
        The angular location of the mass to add off the centreline of the hub to represent the various mass imbalances and assymetries in the rotor.
    
    ErrorsInSetAngle : List[float]
        The manufacturing or assembly errors in the angle the pitch bearings or blades are attached to the hub.
    
    ErrorsInAzimuthAngle : List[float]
        The manufacturing or assembly errors in the azimuth angle for each blade mounting point.
    
    Notes
    -----
    
    """
    OutOfBalanceMass: float = Field(alias="OutOfBalanceMass", default=None)
    RadiusOfMass: float = Field(alias="RadiusOfMass", default=None)
    AzimuthalPositionOfMass: float = Field(alias="AzimuthalPositionOfMass", default=None)
    ErrorsInSetAngle: List[float] = Field(alias="ErrorsInSetAngle", default=list())
    ErrorsInAzimuthAngle: List[float] = Field(alias="ErrorsInAzimuthAngle", default=list())

    _relative_schema_path = 'Components/Hub/RotorImbalances/RotorImbalances.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set(['ErrorsInSetAngle','ErrorsInAzimuthAngle',]),
        None).merge(BladedModel._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


RotorImbalances.update_forward_refs()

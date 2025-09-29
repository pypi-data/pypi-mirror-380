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


class PositionOfHubCentre(BladedModel):
    r"""
    The positioning of the hub centre.  The hub centre is the nominal point where all of the pitch axes intercept the axis of rotation, if any sweep is ignored.
    
    Attributes
    ----------
    RotorTilt : float
        The angle of the main bearing and low speed shaft to the horizontal.  A positive value will tilt the rotor upwards to face the sky.
    
    Overhang : float
        The distance of the hub centre upwind from the `DrivetrainAndNacelle`'s origin (where the nacelle is attached to the yaw bearing or support structure). This will be considered as the vector component parallel to the `DrivetrainAndNacelle`'s x-axis if the `DrivetrainAndNacelle`'s axis system is not aligned with global X.
    
    HeightOffset : float
        The distance in the `DrivetrainAndNacelle`'s Z direction between the `DrivetrainAndNacelle`'s origin (where the nacelle is attached to the yaw system or support structure) and the hub centre.
    
    SideOffset : float, default=0
        The distance in the `DrivetrainAndNacelle`'s Y direction between the `DrivetrainAndNacelle`'s origin (where the nacelle is attached to the yaw system or support structure) and the hub centre.  This is often zero or very small.
    
    Notes
    -----
    
    """
    RotorTilt: float = Field(alias="RotorTilt", default=None)
    Overhang: float = Field(alias="Overhang", default=None)
    HeightOffset: float = Field(alias="HeightOffset", default=None)
    SideOffset: float = Field(alias="SideOffset", default=None)

    _relative_schema_path = 'Components/DrivetrainAndNacelle/PositionOfHubCentre/PositionOfHubCentre.json'
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


PositionOfHubCentre.update_forward_refs()

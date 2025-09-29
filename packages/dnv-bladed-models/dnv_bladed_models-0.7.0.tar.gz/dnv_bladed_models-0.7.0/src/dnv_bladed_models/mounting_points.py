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


class MountingPoints(BladedModel):
    r"""
    The properties defining where the blades or pitch systems attach to the hub.  All of the angles described are for INSIDE of the pitch bearing - the blade has its own values for sweep and cone outside of the pitch bearing.
    
    Attributes
    ----------
    RadiusOfBladeConnection : float
        The radius (measured from the hub's axis of rotation) that the extension piece terminates and the blade will commence.
    
    ConingAngle : float, default=0
        The coning angle of the hub itself.  A positive value for ConingAngle will result in the blade tips moving away from the nacelle, whether an upwind or downwind turbine.
    
    SetAngle : float, default=0
        The angle at which the pitch bearings or blades are mounted onto the pitch bearing or hub.  When the set angle is 0, the blade root Y-axis (which is broadly aligned with the chord-line) will lie in the plane of the rotor (when cone angle is ignored).  More positive values of set angle push the leading edge further upstream.
    
    Notes
    -----
    
    """
    RadiusOfBladeConnection: float = Field(alias="RadiusOfBladeConnection", default=None)
    ConingAngle: float = Field(alias="ConingAngle", default=None)
    SetAngle: float = Field(alias="SetAngle", default=None)

    _relative_schema_path = 'Components/Hub/MountingPoints/MountingPoints.json'
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


MountingPoints.update_forward_refs()

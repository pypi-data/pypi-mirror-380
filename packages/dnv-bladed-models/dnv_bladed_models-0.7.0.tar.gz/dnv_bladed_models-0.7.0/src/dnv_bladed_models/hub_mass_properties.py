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


class HubMassProperties(BladedModel):
    r"""
    The mass properties of the hub.
    
    Attributes
    ----------
    Mass : float
        The total mass of hub including the pitch system, but excluding contribution from the blades connected to it.
    
    AxialPositionOfCentreOfGravity : float
        The hub centre of gravity, relative to intercept of blade pitch axis and drivetrain axis (the hub centre), positive direction being along drivetrain axis towards the hub.
    
    MomentOfInertiaAboutShaft : float
        The total moment of inertia of hub about the low speed shaft, including the pitch system but excluding contribution from the blades connected to it.
    
    MomentOfInertiaPerpendicularToShaft : float
        The total moment of inertia of hub perpendicular to the low speed shaft, including the pitch system but excluding contribution from the blades connected to it.
    
    Notes
    -----
    
    """
    Mass: float = Field(alias="Mass", default=None)
    AxialPositionOfCentreOfGravity: float = Field(alias="AxialPositionOfCentreOfGravity", default=None)
    MomentOfInertiaAboutShaft: float = Field(alias="MomentOfInertiaAboutShaft", default=None)
    MomentOfInertiaPerpendicularToShaft: float = Field(alias="MomentOfInertiaPerpendicularToShaft", default=None)

    _relative_schema_path = 'Components/Hub/HubMassProperties/HubMassProperties.json'
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


HubMassProperties.update_forward_refs()

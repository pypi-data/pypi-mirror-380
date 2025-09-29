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


class PositionOfUpwindTurbine(BladedModel):
    r"""
    
    
    Attributes
    ----------
    DistanceUpwind : float
        The distance of turbine generating the wake relative to the simulated turbine in the North direction (negative global X).
    
    OffsetY : float
        The distance of turbine generating the wake relative to the simulated turbine in the West (global Y) direction.
    
    RelativeHubHeight : float, default=0
        The relative difference in height between the upwind and the simulated turbines.  A positive value indicates that the hub of the turbine generating the wake is higher than the hub of the turbine being simulated.
    
    Notes
    -----
    
    """
    DistanceUpwind: float = Field(alias="DistanceUpwind", default=None)
    OffsetY: float = Field(alias="OffsetY", default=None)
    RelativeHubHeight: float = Field(alias="RelativeHubHeight", default=None)

    _relative_schema_path = 'TimeDomainSimulation/Environment/Wind/DynamicUpstreamWake/PositionOfUpwindTurbine/PositionOfUpwindTurbine.json'
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


PositionOfUpwindTurbine.update_forward_refs()

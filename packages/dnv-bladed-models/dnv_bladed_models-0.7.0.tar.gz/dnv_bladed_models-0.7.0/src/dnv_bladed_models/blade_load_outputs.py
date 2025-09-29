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


class BladeLoadOutputs(BladedModel):
    r"""
    Loads selected
    
    Not supported yet.
    
    Attributes
    ----------
    FlapwiseBendingLoads : bool, default=False, Not supported yet
        Output blade bending moments for the flapwise direction (0=no, 1=yes).
    
    EdgewiseBendingLoads : bool, default=False, Not supported yet
        Output blade bending moments for the edgewise direction (0=no, 1=yes).
    
    FlapwiseShearLoads : bool, default=False, Not supported yet
        Output blade shear forces for the flapwise direction (0=no, 1=yes).
    
    EdgewiseShearLoads : bool, default=False, Not supported yet
        Output blade shear forces for the edgewise direction (0=no, 1=yes).
    
    OutOfPlaneBendingLoads : bool, default=False, Not supported yet
        Output blade bending moments for out of plane direction (0=no, 1=yes).
    
    InPlaneBendingLoads : bool, default=False, Not supported yet
        Output blade bending moments for in plane direction (0=no, 1=yes).
    
    OutOfPlaneShearLoads : bool, default=False, Not supported yet
        Output blade shear forces for out of plane direction (0=no, 1=yes).
    
    InPlaneShearLoads : bool, default=False, Not supported yet
        Output blade shear forces for in plane direction (0=no, 1=yes).
    
    RadialForces : bool, default=False, Not supported yet
        Output blade radial forces (0=no, 1=yes).
    
    LoadsInRootAxisSystem : bool, default=False, Not supported yet
        Output blade loads about the root axes system (0=no, 1=yes).
    
    LoadsInAeroAxisSystem : bool, default=False, Not supported yet
        Output blade loads about the aero axes system (0=no, 1=yes).
    
    LoadsInUserAxisSystem : bool, default=False, Not supported yet
        Output blade loads about the user defined axes system (0=no, 1=yes).
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    FlapwiseBendingLoads: bool = Field(alias="FlapwiseBendingLoads", default=None) # Not supported yet
    EdgewiseBendingLoads: bool = Field(alias="EdgewiseBendingLoads", default=None) # Not supported yet
    FlapwiseShearLoads: bool = Field(alias="FlapwiseShearLoads", default=None) # Not supported yet
    EdgewiseShearLoads: bool = Field(alias="EdgewiseShearLoads", default=None) # Not supported yet
    OutOfPlaneBendingLoads: bool = Field(alias="OutOfPlaneBendingLoads", default=None) # Not supported yet
    InPlaneBendingLoads: bool = Field(alias="InPlaneBendingLoads", default=None) # Not supported yet
    OutOfPlaneShearLoads: bool = Field(alias="OutOfPlaneShearLoads", default=None) # Not supported yet
    InPlaneShearLoads: bool = Field(alias="InPlaneShearLoads", default=None) # Not supported yet
    RadialForces: bool = Field(alias="RadialForces", default=None) # Not supported yet
    LoadsInRootAxisSystem: bool = Field(alias="LoadsInRootAxisSystem", default=None) # Not supported yet
    LoadsInAeroAxisSystem: bool = Field(alias="LoadsInAeroAxisSystem", default=None) # Not supported yet
    LoadsInUserAxisSystem: bool = Field(alias="LoadsInUserAxisSystem", default=None) # Not supported yet

    _relative_schema_path = 'Components/Blade/BladeOutputGroupLibrary/BladeOutputGroup/BladeLoadOutputs/BladeLoadOutputs.json'
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


BladeLoadOutputs.update_forward_refs()

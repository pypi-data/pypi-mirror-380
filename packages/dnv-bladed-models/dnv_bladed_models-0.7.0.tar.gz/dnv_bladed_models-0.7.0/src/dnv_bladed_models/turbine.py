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
from dnv_bladed_models.assembly import Assembly
from dnv_bladed_models.bladed_control import BladedControl
from dnv_bladed_models.bladed_model import BladedModel
from dnv_bladed_models.component_library import ComponentLibrary
from dnv_bladed_models.electrical_grid import ElectricalGrid
from dnv_bladed_models.external_module import ExternalModule
from dnv_bladed_models.turbine_operational_parameters import TurbineOperationalParameters

from .schema_helper import SchemaHelper
from .models_impl import *


class Turbine(BladedModel):
    r"""
    The definition of the turbine and its installation that is to be modelled.
    
    Attributes
    ----------
    ElectricalGrid : ElectricalGrid, Not supported yet
    
    TurbineOperationalParameters : TurbineOperationalParameters
    
    Control : BladedControl
    
    GlobalExternalModules : List[ExternalModule], Not supported yet
        A list of any external modules that will be run with the time domain simulations.  It is expected that external modules defined here will interact with more than one area of the turbine, such as to apply additional aerodynamics loads to the entire structure.  Any external modules that represent a single component should be added to the Assembly tree.
    
    MeanSeaLevel : float, default=0, Not supported yet
        The mean sea depth at the turbine location.  If omited, the Turbine will be considered an on-shore turbine and any sea states will be ignored.
    
    Assembly : Assembly
    
    ComponentLibrary : ComponentLibrary
    
    Notes
    -----
    
    """
    ElectricalGrid: ElectricalGrid = Field(alias="ElectricalGrid", default=None) # Not supported yet
    TurbineOperationalParameters: TurbineOperationalParameters = Field(alias="TurbineOperationalParameters", default=None)
    Control: BladedControl = Field(alias="Control", default=None)
    GlobalExternalModules: List[ExternalModule] = Field(alias="GlobalExternalModules", default=list()) # Not supported yet
    MeanSeaLevel: float = Field(alias="MeanSeaLevel", default=None) # Not supported yet
    Assembly: Assembly = Field(alias="Assembly", default=Assembly())
    ComponentLibrary: ComponentLibrary = Field(alias="ComponentLibrary", default=ComponentLibrary())

    _relative_schema_path = 'Turbine/Turbine.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set(['GlobalExternalModules','Assembly','ComponentLibrary',]),
        None).merge(BladedModel._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


Turbine.update_forward_refs()

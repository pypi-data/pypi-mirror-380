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
from dnv_bladed_models.campbell_diagram_mode_of_operation import CampbellDiagramModeOfOperation
from dnv_bladed_models.velocity_range import VelocityRange

from .schema_helper import SchemaHelper
from .models_impl import *


class CampbellPowerProduction(CampbellDiagramModeOfOperation):
    r"""
    The properties for generating a Campbell diagram for a turbine in power production mode.  This will use the steady-state operating parameters defined in the TurbineOperationalParameters section to determine the operating point for the specified wind speeds.
    
    Not supported yet.
    
    Attributes
    ----------
    CampbellDiagramModeOfOperationType : Literal['PowerProduction'], default='PowerProduction', Not supported yet
        Defines the specific type of CampbellDiagramModeOfOperation model in use.  For a `PowerProduction` object, this must always be set to a value of `PowerProduction`.
    
    WindSpeedRange : VelocityRange
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    CampbellDiagramModeOfOperationType: Literal['PowerProduction'] = Field(alias="CampbellDiagramModeOfOperationType", default='PowerProduction', allow_mutation=False, const=True) # Not supported yet # type: ignore
    WindSpeedRange: VelocityRange = Field(alias="WindSpeedRange", default=None)

    _relative_schema_path = 'SteadyCalculation/CampbellDiagramModeOfOperation/CampbellPowerProduction.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'CampbellDiagramModeOfOperationType').merge(CampbellDiagramModeOfOperation._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


CampbellPowerProduction.update_forward_refs()

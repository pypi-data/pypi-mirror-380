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
from dnv_bladed_models.aerodynamic_settings import AerodynamicSettings
from dnv_bladed_models.bladed_model import BladedModel
from dnv_bladed_models.hydrodynamic_calculation import HydrodynamicCalculation
from dnv_bladed_models.logging import Logging
from dnv_bladed_models.solver_settings import SolverSettings

from .schema_helper import SchemaHelper
from .models_impl import *


class Settings(BladedModel):
    r"""
    The settings for both time domain simulations and steady calculations.  These are typically calculation options which have reliable defaults, but offer the users other options to control the analysis.
    
    Attributes
    ----------
    Solver : SolverSettings
    
    Aerodynamics : AerodynamicSettings
    
    Hydrodynamics : HydrodynamicCalculation, Not supported yet
    
    Logging : Logging
    
    Notes
    -----
    
    """
    Solver: SolverSettings = Field(alias="Solver", default=None)
    Aerodynamics: AerodynamicSettings = Field(alias="Aerodynamics", default=None)
    Hydrodynamics: HydrodynamicCalculation = Field(alias="Hydrodynamics", default=None) # Not supported yet
    Logging: Logging = Field(alias="Logging", default=None)

    _relative_schema_path = 'Settings/Settings.json'
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


Settings.update_forward_refs()

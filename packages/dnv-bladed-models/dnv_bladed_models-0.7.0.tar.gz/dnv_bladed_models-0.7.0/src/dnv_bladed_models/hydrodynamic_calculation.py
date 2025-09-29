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
class HydrodynamicCalculation_HydrostaticsMorisonMethodEnum(str, Enum):
    VARIABLE_INTERFACE = "VARIABLE_INTERFACE"
    EQUALLY_SPACED_INTERFACE = "EQUALLY_SPACED_INTERFACE"
    NOT_USED = "NOT_USED"

from .schema_helper import SchemaHelper
from .models_impl import *


class HydrodynamicCalculation(BladedModel):
    r"""
    Settings for the hydrodynamic modelling within Bladed.  Note that many hydrodynamic modelling options are specific to the components.  These options can be found within the componentss definitions themselves.
    
    Not supported yet.
    
    Attributes
    ----------
    MinimumExcitationForceTimeStep : float, default=0.1, Not supported yet
        The timestep for calculating excitation forces for BEM bodies.  If omitted, the excitation force will be calculated on every integrator timestep.
    
    HydrostaticsMorisonMethod : HydrodynamicCalculation_HydrostaticsMorisonMethodEnum, default='NOT_USED', Not supported yet
        The method to use for the hydrostatics Morison calculations.
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    MinimumExcitationForceTimeStep: float = Field(alias="MinimumExcitationForceTimeStep", default=None) # Not supported yet
    HydrostaticsMorisonMethod: HydrodynamicCalculation_HydrostaticsMorisonMethodEnum = Field(alias="HydrostaticsMorisonMethod", default=None) # Not supported yet

    _relative_schema_path = 'Settings/HydrodynamicCalculation/HydrodynamicCalculation.json'
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


HydrodynamicCalculation.update_forward_refs()

# *********************************************************************#
# Bladed Python Models API                                             #
# Copyright (c) DNV Services UK Limited (c) 2025. All rights reserved. #
# MIT License (see license file)                                       #
# *********************************************************************#


# coding: utf-8

from __future__ import annotations

from abc import ABC

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
class SteadyCalculation_SteadyCalculationTypeEnum(str, Enum):
    AERODYNAMIC_INFORMATION = "AerodynamicInformation"
    BLADE_STABILITY_ANALYSIS = "BladeStabilityAnalysis"
    CAMPBELL_DIAGRAM = "CampbellDiagram"
    MODAL_ANALYSIS = "ModalAnalysis"
    MODEL_LINEARISATION = "ModelLinearisation"
    PERFORMANCE_COEFFICIENTS = "PerformanceCoefficients"
    STEADY_OPERATIONAL_LOADS = "SteadyOperationalLoads"
    STEADY_PARKED_LOADS = "SteadyParkedLoads"
    STEADY_POWER_CURVE = "SteadyPowerCurve"
    INSERT = "Insert"

from .schema_helper import SchemaHelper
from .models_impl import *


class SteadyCalculation(BladedModel, ABC):
    r"""
    The common properties of the steady calculations in Bladed.
    
    Attributes
    ----------
    SteadyCalculationType : SteadyCalculation_SteadyCalculationTypeEnum
        Defines the specific type of model in use.
    
    Notes
    -----
    
    This class is an abstraction, with the following concrete implementations:
        - AerodynamicInformationCalculation
        - BladeStabilityAnalysis
        - CampbellDiagram
        - SteadyCalculationInsert
        - ModalAnalysisCalculation
        - ModelLinearisation
        - PerformanceCoefficientsCalculation
        - SteadyOperationalLoadsCalculation
        - SteadyParkedLoadsCalculation
        - SteadyPowerCurveCalculation
    
    """
    SteadyCalculationType: SteadyCalculation_SteadyCalculationTypeEnum = Field(alias="SteadyCalculationType", default=None)

    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        None).merge(BladedModel._type_info)


SteadyCalculation.update_forward_refs()

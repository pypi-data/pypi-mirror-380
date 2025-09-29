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
from dnv_bladed_models.blade_stability_perturbations import BladeStabilityPerturbations
from dnv_bladed_models.custom_linear_model_dll import CustomLinearModelDll
from dnv_bladed_models.linearisation_calculation import LinearisationCalculation

from .schema_helper import SchemaHelper
from .models_impl import *


class BladeStabilityAnalysisCalculation(LinearisationCalculation, ABC):
    r"""
    
    
    Not supported yet.
    
    Attributes
    ----------
    AzimuthAngle : float, default=0, Not supported yet
        The fixed azimuth angle of the rotor (zero azimuth indicates blade 1 pointing upwards).
    
    MaximumPlotFrequency : float, default=125.663706144, Not supported yet
        The maximum frequency for modes to be shown in the Campbell diagram plot. The default value is 20 * 2 * 3.14159265358979323
    
    CustomLinearModelDll : CustomLinearModelDll, Not supported yet
    
    Perturbations : BladeStabilityPerturbations, Not supported yet
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    AzimuthAngle: float = Field(alias="AzimuthAngle", default=None) # Not supported yet
    MaximumPlotFrequency: float = Field(alias="MaximumPlotFrequency", default=None) # Not supported yet
    CustomLinearModelDll: CustomLinearModelDll = Field(alias="CustomLinearModelDll", default=None) # Not supported yet
    Perturbations: BladeStabilityPerturbations = Field(alias="Perturbations", default=None) # Not supported yet

    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        None).merge(LinearisationCalculation._type_info)


BladeStabilityAnalysisCalculation.update_forward_refs()

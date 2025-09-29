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
from dnv_bladed_models.angle_range import AngleRange
from dnv_bladed_models.linearisation_calculation import LinearisationCalculation
from dnv_bladed_models.model_linearisation_perturbations import ModelLinearisationPerturbations
from dnv_bladed_models.velocity_range import VelocityRange

from .schema_helper import SchemaHelper
from .models_impl import *


class ModelLinearisation(LinearisationCalculation):
    r"""
    Defines a calculation which produces a linear model.  This can be post-processed into a linearised model of the turbine in state-space form.  This is of particular value in the design of controllers.
    
    Not supported yet.
    
    Attributes
    ----------
    SteadyCalculationType : Literal['ModelLinearisation'], default='ModelLinearisation', Not supported yet
        Defines the specific type of SteadyCalculation model in use.  For a `ModelLinearisation` object, this must always be set to a value of `ModelLinearisation`.
    
    Perturbations : ModelLinearisationPerturbations, Not supported yet
    
    WindSpeed : VelocityRange
    
    Azimuth : AngleRange
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    SteadyCalculationType: Literal['ModelLinearisation'] = Field(alias="SteadyCalculationType", default='ModelLinearisation', allow_mutation=False, const=True) # Not supported yet # type: ignore
    Perturbations: ModelLinearisationPerturbations = Field(alias="Perturbations", default=None) # Not supported yet
    WindSpeed: VelocityRange = Field(alias="WindSpeed", default=None)
    Azimuth: AngleRange = Field(alias="Azimuth", default=None)

    _relative_schema_path = 'SteadyCalculation/ModelLinearisation.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'SteadyCalculationType').merge(LinearisationCalculation._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


ModelLinearisation.update_forward_refs()

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
from dnv_bladed_models.perturbation_settings import PerturbationSettings

from .schema_helper import SchemaHelper
from .models_impl import *


class ModelLinearisationPerturbations(PerturbationSettings):
    r"""
    
    
    Not supported yet.
    
    Attributes
    ----------
    WindSpeedPerturbation : float, Not supported yet
        The magnitude of perturbation of the wind speed around the equilibrium value.  It should be small so that the analysis stays in the linear region  Omit keyword in order to let Bladed calculate a default perturbation.
    
    PitchPerturbation : float, Not supported yet
        The magnitude of perturbation of the pitch angle around the equilibrium value.  It should be small so that the analysis stays in the linear region.  Omit keyword in order to let Bladed calculate a default perturbation.
    
    GeneratorTorquePerturbation : float, Not supported yet
        The magnitude of perturbation of the generator torque around the equilibrium value.  It should be small so that the analysis stays in the linear region.  Omit keyword in order to let Bladed calculate a default perturbation.
    
    WindShearPerturbation : float, default=0, Not supported yet
        The magnitude of both horizontal and vertical shear perturbations   The default is to have no perturbation on the wind shear.
    
    ApplyPitchPerturbationToEachBlade : bool, default=False, Not supported yet
        If true, the pitch angle will be perturbed in turn for each blade as well as collectively for all blades
    
    YawActuatorTorquePerturbation : float, Not supported yet
        Yaw actuator torque perturbation. The torque perturbation is evenly distributed across the actuator banks.
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    WindSpeedPerturbation: float = Field(alias="WindSpeedPerturbation", default=None) # Not supported yet
    PitchPerturbation: float = Field(alias="PitchPerturbation", default=None) # Not supported yet
    GeneratorTorquePerturbation: float = Field(alias="GeneratorTorquePerturbation", default=None) # Not supported yet
    WindShearPerturbation: float = Field(alias="WindShearPerturbation", default=None) # Not supported yet
    ApplyPitchPerturbationToEachBlade: bool = Field(alias="ApplyPitchPerturbationToEachBlade", default=None) # Not supported yet
    YawActuatorTorquePerturbation: float = Field(alias="YawActuatorTorquePerturbation", default=None) # Not supported yet

    _relative_schema_path = 'SteadyCalculation/ModelLinearisationPerturbations/ModelLinearisationPerturbations.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        None).merge(PerturbationSettings._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


ModelLinearisationPerturbations.update_forward_refs()

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
from dnv_bladed_models.aerodynamic_model import AerodynamicModel
class VortexLine_WakeTypeEnum(str, Enum):
    FREE_WAKE = "FreeWake"
    FIXED_WAKE = "FixedWake"
class VortexLine_CoreGrowthModelEnum(str, Enum):
    RL_MODEL = "RL_Model"
    LO_MODEL = "LO_Model"
    FIXED = "Fixed"
class VortexLine_InitialVortexCoreSizeModelEnum(str, Enum):
    RL_MODEL = "RL_Model"
    LO_MODEL = "LO_Model"
    FIXED = "Fixed"

from .schema_helper import SchemaHelper
from .models_impl import *


class VortexLine(AerodynamicModel):
    r"""
    The Vortex Line aerodynamic model.
    
    Not supported yet.
    
    Attributes
    ----------
    AerodynamicModelType : Literal['VortexLine'], default='VortexLine', Not supported yet
        Defines the specific type of AerodynamicModel model in use.  For a `VortexLine` object, this must always be set to a value of `VortexLine`.
    
    MaximumNumberofFreeWakeSteps : int, default=200, Not supported yet
        Each free wake node that is emitted from the trailing edge will be allowed a maximum number of free wake steps after it will be no longer considered in the free wake solution and convected with local wind speed and last computed induction.
    
    MaximumNumberofWakeSteps : int, default=10000, Not supported yet
        Each wake node will be allowed a maximum number of steps before it is removed. This option puts an upper bound on the number of wake nodes.
    
    NumberOfThreads : int, default=1, Not supported yet
        The number of parallel CPU threads used in evaluation of the Biot-Savart law.  This option is only relevant when the wake type is set to \"Free Wake\".
    
    VortexWakeTimeStep : float, default=0.05, Not supported yet
        The time step used to update the vortex wake.  It is recommended to select a time step such that at least 60 vortex wake steps are taken each rotor revolution.
    
    WakeType : VortexLine_WakeTypeEnum, default='FreeWake', Not supported yet
        The \"Free Wake\" option will calculate the mutual influence of all wake elements on all wake nodes during each time step.  The \"Fixed Wake\" option will assume that the induced velocity in all wake nodes is equal to the average wake induced velocity at 70% blade radius.  The \"Free Wake\" option requires substantially more calculations to be performed, and is likely to significantly slow the analysis.
    
    CoreGrowthModel : VortexLine_CoreGrowthModelEnum, default='RL_Model', Not supported yet
        The Core Growth Model.
    
    InitialVortexCoreSizeModel : VortexLine_InitialVortexCoreSizeModelEnum, default='RL_Model', Not supported yet
        The intial vortex core size Model.
    
    FilamentStrain : bool, default=True, Not supported yet
        The filament strain.
    
    LambOseenCoreGrowthConstant : float, default=1.234, Not supported yet
        The Lamb-Oseen core growth constant,
    
    CoreGrowthConstant : float, default=50, Not supported yet
        The core growth constant.
    
    RamasamyLeishmanConstant : float, default=0.000065, Not supported yet
        The Ramasamy-Leishman constant.
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    AerodynamicModelType: Literal['VortexLine'] = Field(alias="AerodynamicModelType", default='VortexLine', allow_mutation=False, const=True) # Not supported yet # type: ignore
    MaximumNumberofFreeWakeSteps: int = Field(alias="MaximumNumberofFreeWakeSteps", default=None) # Not supported yet
    MaximumNumberofWakeSteps: int = Field(alias="MaximumNumberofWakeSteps", default=None) # Not supported yet
    NumberOfThreads: int = Field(alias="NumberOfThreads", default=None) # Not supported yet
    VortexWakeTimeStep: float = Field(alias="VortexWakeTimeStep", default=None) # Not supported yet
    WakeType: VortexLine_WakeTypeEnum = Field(alias="WakeType", default=None) # Not supported yet
    CoreGrowthModel: VortexLine_CoreGrowthModelEnum = Field(alias="CoreGrowthModel", default=None) # Not supported yet
    InitialVortexCoreSizeModel: VortexLine_InitialVortexCoreSizeModelEnum = Field(alias="InitialVortexCoreSizeModel", default=None) # Not supported yet
    FilamentStrain: bool = Field(alias="FilamentStrain", default=None) # Not supported yet
    LambOseenCoreGrowthConstant: float = Field(alias="LambOseenCoreGrowthConstant", default=None) # Not supported yet
    CoreGrowthConstant: float = Field(alias="CoreGrowthConstant", default=None) # Not supported yet
    RamasamyLeishmanConstant: float = Field(alias="RamasamyLeishmanConstant", default=None) # Not supported yet

    _relative_schema_path = 'Settings/AerodynamicSettings/AerodynamicModel/VortexLine.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'AerodynamicModelType').merge(AerodynamicModel._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


VortexLine.update_forward_refs()

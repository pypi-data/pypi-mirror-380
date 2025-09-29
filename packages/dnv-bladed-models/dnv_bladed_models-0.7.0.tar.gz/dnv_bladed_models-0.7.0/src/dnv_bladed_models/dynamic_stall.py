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
class DynamicStall_DynamicStallTypeEnum(str, Enum):
    COMPRESSIBLE_BEDDOES_LEISHMAN_MODEL = "CompressibleBeddoesLeishmanModel"
    IAG_MODEL = "IAGModel"
    INCOMPRESSIBLE_BEDDOES_LEISHMAN_MODEL = "IncompressibleBeddoesLeishmanModel"
    OYE_MODEL = "OyeModel"
    INSERT = "Insert"

from .schema_helper import SchemaHelper
from .models_impl import *


class DynamicStall(BladedModel, ABC):
    r"""
    The common properties of all of the dynamic stall models.
    
    Attributes
    ----------
    DynamicStallType : DynamicStall_DynamicStallTypeEnum
        Defines the specific type of model in use.
    
    UseDynamicPitchingMomentCoefficient : bool, default=True
        If true, the dynamic pitching moment coefficient will be used.  This option is enabled by default.  It is not recommended to disable this option for blades with a torsional degree of freedom because the so-called 'pitch- rate damping' term of the moment coefficient is typically important to keep the blade torsional mode stable.
    
    StartingRadius : float, default=0
        The fraction of the radius outboard of which the dynamic stall model will be used. A value of 0.0 means that dynamic stall is applied from the blade root.
    
    EndingRadius : float, default=0.95
        The fraction of the radius outboard of which the dynamic stall model will be switched off. A value of 1.0 means that dynamic stall is applied until the blade tip.
    
    SeparationTimeConstant : float, default=3
        A dimensionless time constant, given in terms of the time taken to travel half a chord. It defines the lag in the movement of the separation point due to unsteady pressure and boundary layer response.
    
    UseLinearFitGradientMethod : bool, default=True
        If true, the linear fit polar gradient is used to reconstruct the inviscid polar data. The fit is performed only within the linear polar regime that is searched automatically between the zero lift AoA to AoA = 7 deg. This approach is more suitable for polar data sets where the lift coefficient slope is not straight around 0 deg angle of attack. It is recommended to activate this option for more accurate computations. This option is turned on by default.
    
    Notes
    -----
    
    This class is an abstraction, with the following concrete implementations:
        - CompressibleBeddoesLeishmanModel
        - IAGModel
        - IncompressibleBeddoesLeishmanModel
        - DynamicStallInsert
        - OyeModel
    
    """
    DynamicStallType: DynamicStall_DynamicStallTypeEnum = Field(alias="DynamicStallType", default=None)
    UseDynamicPitchingMomentCoefficient: bool = Field(alias="UseDynamicPitchingMomentCoefficient", default=None)
    StartingRadius: float = Field(alias="StartingRadius", default=None)
    EndingRadius: float = Field(alias="EndingRadius", default=None)
    SeparationTimeConstant: float = Field(alias="SeparationTimeConstant", default=None)
    UseLinearFitGradientMethod: bool = Field(alias="UseLinearFitGradientMethod", default=None)

    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        None).merge(BladedModel._type_info)


DynamicStall.update_forward_refs()

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
from dnv_bladed_models.nominal_hub_wind_speed_vs_rotor_speed_and_pitch_angle import NominalHubWindSpeedVsRotorSpeedAndPitchAngle
from dnv_bladed_models.variable_speed_pitch_regulated_control_model import VariableSpeedPitchRegulatedControlModel

from .schema_helper import SchemaHelper
from .models_impl import *


class TurbineOperationalParameters(BladedModel):
    r"""
    The general operational parameters for the turbine. These are used to calculate steady state conditions for steady calculation types or initial conditions for time-domain calculation types.
    
    Attributes
    ----------
    NominalHubWindSpeedVsRotorSpeedAndPitchAngle : List[NominalHubWindSpeedVsRotorSpeedAndPitchAngle]
        User defined look-up table to define the steady state conditions of rotor speed and pitch angle over wind speed. If defined Bladed will use these values instead of trying to determine them.
    
    VariableSpeedPitchRegulatedControlModel : VariableSpeedPitchRegulatedControlModel
    
    PitchAngleWhilstIdling : float, default=1.570796326794
        The pitch angle of the blades when the turbine is idling.  The default is 90 degrees.
    
    PitchAngleWhilstParked : float, default=1.570796326794
        The pitch angle of the blades when the turbine is parked.  The default is 90 degrees.
    
    Notes
    -----
    
    """
    NominalHubWindSpeedVsRotorSpeedAndPitchAngle: List[NominalHubWindSpeedVsRotorSpeedAndPitchAngle] = Field(alias="NominalHubWindSpeedVsRotorSpeedAndPitchAngle", default=list())
    VariableSpeedPitchRegulatedControlModel: VariableSpeedPitchRegulatedControlModel = Field(alias="VariableSpeedPitchRegulatedControlModel", default=None)
    PitchAngleWhilstIdling: float = Field(alias="PitchAngleWhilstIdling", default=None)
    PitchAngleWhilstParked: float = Field(alias="PitchAngleWhilstParked", default=None)

    _relative_schema_path = 'Turbine/TurbineOperationalParameters/TurbineOperationalParameters.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set(['NominalHubWindSpeedVsRotorSpeedAndPitchAngle',]),
        None).merge(BladedModel._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


TurbineOperationalParameters.update_forward_refs()

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
from dnv_bladed_models.shaft_input_power_vs_power_loss import ShaftInputPowerVsPowerLoss
from dnv_bladed_models.shaft_input_torque_vs_resisting_torque import ShaftInputTorqueVsResistingTorque
from dnv_bladed_models.shaft_speed_vs_shaft_input_power_vs_power_loss import ShaftSpeedVsShaftInputPowerVsPowerLoss
from dnv_bladed_models.shaft_speed_vs_shaft_input_torque_vs_resisting_torque import ShaftSpeedVsShaftInputTorqueVsResistingTorque

from .schema_helper import SchemaHelper
from .models_impl import *


class MechanicalLosses(BladedModel):
    r"""
    The common properties for the mechanical losses in the drivetrain.
    
    Attributes
    ----------
    ShaftSpeedVsShaftInputTorqueVsResistingTorque : List[ShaftSpeedVsShaftInputTorqueVsResistingTorque]
        A series of look-up tables for the losses, each valid for the specified shaft speed.
    
    ShaftInputTorqueVsResistingTorque : List[ShaftInputTorqueVsResistingTorque]
        A look-up table for the losses, each valid for the specified input torque.
    
    ShaftSpeedVsShaftInputPowerVsPowerLoss : List[ShaftSpeedVsShaftInputPowerVsPowerLoss]
        A series of look-up tables for the losses, each valid for the specified shaft rotational speed.
    
    ShaftInputPowerVsPowerLoss : List[ShaftInputPowerVsPowerLoss]
        A series of look-up tables for the losses, each valid for the specified shaft rotational speed.
    
    Notes
    -----
    
    """
    ShaftSpeedVsShaftInputTorqueVsResistingTorque: List[ShaftSpeedVsShaftInputTorqueVsResistingTorque] = Field(alias="ShaftSpeedVsShaftInputTorqueVsResistingTorque", default=list())
    ShaftInputTorqueVsResistingTorque: List[ShaftInputTorqueVsResistingTorque] = Field(alias="ShaftInputTorqueVsResistingTorque", default=list())
    ShaftSpeedVsShaftInputPowerVsPowerLoss: List[ShaftSpeedVsShaftInputPowerVsPowerLoss] = Field(alias="ShaftSpeedVsShaftInputPowerVsPowerLoss", default=list())
    ShaftInputPowerVsPowerLoss: List[ShaftInputPowerVsPowerLoss] = Field(alias="ShaftInputPowerVsPowerLoss", default=list())

    _relative_schema_path = 'Components/DrivetrainAndNacelle/MechanicalLosses/MechanicalLosses.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set(['ShaftSpeedVsShaftInputTorqueVsResistingTorque','ShaftInputTorqueVsResistingTorque','ShaftSpeedVsShaftInputPowerVsPowerLoss','ShaftInputPowerVsPowerLoss',]),
        None).merge(BladedModel._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


MechanicalLosses.update_forward_refs()

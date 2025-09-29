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
from dnv_bladed_models.signal_properties_acceleration import SignalPropertiesAcceleration
from dnv_bladed_models.signal_properties_angle import SignalPropertiesAngle
from dnv_bladed_models.signal_properties_angular_acceleration import SignalPropertiesAngularAcceleration
from dnv_bladed_models.signal_properties_angular_velocity import SignalPropertiesAngularVelocity
from dnv_bladed_models.signal_properties_force import SignalPropertiesForce
from dnv_bladed_models.signal_properties_length import SignalPropertiesLength
from dnv_bladed_models.signal_properties_moment import SignalPropertiesMoment
from dnv_bladed_models.signal_properties_power import SignalPropertiesPower
from dnv_bladed_models.signal_properties_velocity import SignalPropertiesVelocity

from .schema_helper import SchemaHelper
from .models_impl import *


class MeasuredSignalProperties(BladedModel):
    r"""
    The noise and transducer properties for those signals representing values coming from a physical sensor.
    
    Not supported yet.
    
    Attributes
    ----------
    RandomNumberSeed : int, default=0, Not supported yet
        A seed for the random number generator to ensure that subsequent runs have identical noise signatures.
    
    TurnOffNoise : bool, default=False, Not supported yet
        This allows the noise to be turned off globally.  Note: this turns off noise, but keeps discretisation, sampling time, faults and transducer behaviour.
    
    ShaftPowerSignals : SignalPropertiesPower, Not supported yet
    
    RotorSpeedSignals : SignalPropertiesAngularVelocity, Not supported yet
    
    ElectricalPowerOutputSignals : SignalPropertiesPower, Not supported yet
    
    GeneratorSpeedSignals : SignalPropertiesAngularVelocity, Not supported yet
    
    GeneratorTorqueSignals : SignalPropertiesMoment, Not supported yet
    
    YawBearingAngularPositionSignals : SignalPropertiesAngle, Not supported yet
    
    YawBearingAngularVelocitySignals : SignalPropertiesAngularVelocity, Not supported yet
    
    YawBearingAngularAccelerationSignals : SignalPropertiesAngularAcceleration, Not supported yet
    
    YawMotorRateSignals : SignalPropertiesAngularVelocity, Not supported yet
    
    YawErrorSignals : SignalPropertiesAngle, Not supported yet
    
    NacelleAngleFromNorthSignals : SignalPropertiesAngle, Not supported yet
    
    TowerTopForeAftAccelerationSignals : SignalPropertiesAcceleration, Not supported yet
    
    TowerTopSideSideAccelerationSignals : SignalPropertiesAcceleration, Not supported yet
    
    ShaftTorqueSignals : SignalPropertiesMoment, Not supported yet
    
    YawBearingMySignals : SignalPropertiesMoment, Not supported yet
    
    YawBearingMzSignals : SignalPropertiesMoment, Not supported yet
    
    NacelleRollAngleSignals : SignalPropertiesAngle, Not supported yet
    
    NacelleNoddingAngleSignals : SignalPropertiesAngle, Not supported yet
    
    NacelleRollAccelerationSignals : SignalPropertiesAngularAcceleration, Not supported yet
    
    NacelleNoddingAccelerationSignals : SignalPropertiesAngularAcceleration, Not supported yet
    
    NacelleYawAccelerationSignals : SignalPropertiesAngularAcceleration, Not supported yet
    
    RotorAzimuthAngleSignals : SignalPropertiesAngle, Not supported yet
    
    NominalHubFlowSpeedSignals : SignalPropertiesVelocity, Not supported yet
    
    RotatingHubMySignals : SignalPropertiesMoment, Not supported yet
    
    RotatingHubMzSignals : SignalPropertiesMoment, Not supported yet
    
    FixedHubMySignals : SignalPropertiesMoment, Not supported yet
    
    FixedHubMzSignals : SignalPropertiesMoment, Not supported yet
    
    FixedHubFxSignals : SignalPropertiesForce, Not supported yet
    
    FixedHubFySignals : SignalPropertiesForce, Not supported yet
    
    FixedHubFzSignals : SignalPropertiesForce, Not supported yet
    
    PitchAngleSignals : SignalPropertiesAngle, Not supported yet
    
    PitchRateSignals : SignalPropertiesAngularVelocity, Not supported yet
    
    PitchActuatorTorqueSignals : SignalPropertiesMoment, Not supported yet
    
    PitchBearingFrictionSignals : SignalPropertiesMoment, Not supported yet
    
    PitchBearingStictionSignals : SignalPropertiesMoment, Not supported yet
    
    BladeOutOfPlaneBendingMomentSignals : SignalPropertiesMoment, Not supported yet
    
    BladeInPlaneBendingMomentSignals : SignalPropertiesMoment, Not supported yet
    
    PitchBearingMxSignals : SignalPropertiesMoment, Not supported yet
    
    PitchBearingMySignals : SignalPropertiesMoment, Not supported yet
    
    PitchBearingMzSignals : SignalPropertiesMoment, Not supported yet
    
    PitchBearingRadialForceSignals : SignalPropertiesForce, Not supported yet
    
    PitchBearingAxialForceSignals : SignalPropertiesForce, Not supported yet
    
    PitchBearingFxSignals : SignalPropertiesForce, Not supported yet
    
    PitchBearingFySignals : SignalPropertiesForce, Not supported yet
    
    BladeStationWindSpeedSignals : SignalPropertiesVelocity, Not supported yet
    
    BladeStationAngleOfAttackSignals : SignalPropertiesAngle, Not supported yet
    
    AileronAngleSignals : SignalPropertiesAngle, Not supported yet
    
    AileronRateSignals : SignalPropertiesAngularVelocity, Not supported yet
    
    BladeStationPositionXSignals : SignalPropertiesLength, Not supported yet
    
    BladeStationPositionYSignals : SignalPropertiesLength, Not supported yet
    
    BladeStationPositionZSignals : SignalPropertiesLength, Not supported yet
    
    BladeStationPositionXRotationSignals : SignalPropertiesAngle, Not supported yet
    
    BladeStationPositionYRotationSignals : SignalPropertiesAngle, Not supported yet
    
    BladeStationPositionZRotationSignals : SignalPropertiesAngle, Not supported yet
    
    LidarBeamFocalPointVelocitySignals : SignalPropertiesVelocity, Not supported yet
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    RandomNumberSeed: int = Field(alias="RandomNumberSeed", default=None) # Not supported yet
    TurnOffNoise: bool = Field(alias="TurnOffNoise", default=None) # Not supported yet
    ShaftPowerSignals: SignalPropertiesPower = Field(alias="ShaftPowerSignals", default=None) # Not supported yet
    RotorSpeedSignals: SignalPropertiesAngularVelocity = Field(alias="RotorSpeedSignals", default=None) # Not supported yet
    ElectricalPowerOutputSignals: SignalPropertiesPower = Field(alias="ElectricalPowerOutputSignals", default=None) # Not supported yet
    GeneratorSpeedSignals: SignalPropertiesAngularVelocity = Field(alias="GeneratorSpeedSignals", default=None) # Not supported yet
    GeneratorTorqueSignals: SignalPropertiesMoment = Field(alias="GeneratorTorqueSignals", default=None) # Not supported yet
    YawBearingAngularPositionSignals: SignalPropertiesAngle = Field(alias="YawBearingAngularPositionSignals", default=None) # Not supported yet
    YawBearingAngularVelocitySignals: SignalPropertiesAngularVelocity = Field(alias="YawBearingAngularVelocitySignals", default=None) # Not supported yet
    YawBearingAngularAccelerationSignals: SignalPropertiesAngularAcceleration = Field(alias="YawBearingAngularAccelerationSignals", default=None) # Not supported yet
    YawMotorRateSignals: SignalPropertiesAngularVelocity = Field(alias="YawMotorRateSignals", default=None) # Not supported yet
    YawErrorSignals: SignalPropertiesAngle = Field(alias="YawErrorSignals", default=None) # Not supported yet
    NacelleAngleFromNorthSignals: SignalPropertiesAngle = Field(alias="NacelleAngleFromNorthSignals", default=None) # Not supported yet
    TowerTopForeAftAccelerationSignals: SignalPropertiesAcceleration = Field(alias="TowerTopForeAftAccelerationSignals", default=None) # Not supported yet
    TowerTopSideSideAccelerationSignals: SignalPropertiesAcceleration = Field(alias="TowerTopSideSideAccelerationSignals", default=None) # Not supported yet
    ShaftTorqueSignals: SignalPropertiesMoment = Field(alias="ShaftTorqueSignals", default=None) # Not supported yet
    YawBearingMySignals: SignalPropertiesMoment = Field(alias="YawBearingMySignals", default=None) # Not supported yet
    YawBearingMzSignals: SignalPropertiesMoment = Field(alias="YawBearingMzSignals", default=None) # Not supported yet
    NacelleRollAngleSignals: SignalPropertiesAngle = Field(alias="NacelleRollAngleSignals", default=None) # Not supported yet
    NacelleNoddingAngleSignals: SignalPropertiesAngle = Field(alias="NacelleNoddingAngleSignals", default=None) # Not supported yet
    NacelleRollAccelerationSignals: SignalPropertiesAngularAcceleration = Field(alias="NacelleRollAccelerationSignals", default=None) # Not supported yet
    NacelleNoddingAccelerationSignals: SignalPropertiesAngularAcceleration = Field(alias="NacelleNoddingAccelerationSignals", default=None) # Not supported yet
    NacelleYawAccelerationSignals: SignalPropertiesAngularAcceleration = Field(alias="NacelleYawAccelerationSignals", default=None) # Not supported yet
    RotorAzimuthAngleSignals: SignalPropertiesAngle = Field(alias="RotorAzimuthAngleSignals", default=None) # Not supported yet
    NominalHubFlowSpeedSignals: SignalPropertiesVelocity = Field(alias="NominalHubFlowSpeedSignals", default=None) # Not supported yet
    RotatingHubMySignals: SignalPropertiesMoment = Field(alias="RotatingHubMySignals", default=None) # Not supported yet
    RotatingHubMzSignals: SignalPropertiesMoment = Field(alias="RotatingHubMzSignals", default=None) # Not supported yet
    FixedHubMySignals: SignalPropertiesMoment = Field(alias="FixedHubMySignals", default=None) # Not supported yet
    FixedHubMzSignals: SignalPropertiesMoment = Field(alias="FixedHubMzSignals", default=None) # Not supported yet
    FixedHubFxSignals: SignalPropertiesForce = Field(alias="FixedHubFxSignals", default=None) # Not supported yet
    FixedHubFySignals: SignalPropertiesForce = Field(alias="FixedHubFySignals", default=None) # Not supported yet
    FixedHubFzSignals: SignalPropertiesForce = Field(alias="FixedHubFzSignals", default=None) # Not supported yet
    PitchAngleSignals: SignalPropertiesAngle = Field(alias="PitchAngleSignals", default=None) # Not supported yet
    PitchRateSignals: SignalPropertiesAngularVelocity = Field(alias="PitchRateSignals", default=None) # Not supported yet
    PitchActuatorTorqueSignals: SignalPropertiesMoment = Field(alias="PitchActuatorTorqueSignals", default=None) # Not supported yet
    PitchBearingFrictionSignals: SignalPropertiesMoment = Field(alias="PitchBearingFrictionSignals", default=None) # Not supported yet
    PitchBearingStictionSignals: SignalPropertiesMoment = Field(alias="PitchBearingStictionSignals", default=None) # Not supported yet
    BladeOutOfPlaneBendingMomentSignals: SignalPropertiesMoment = Field(alias="BladeOutOfPlaneBendingMomentSignals", default=None) # Not supported yet
    BladeInPlaneBendingMomentSignals: SignalPropertiesMoment = Field(alias="BladeInPlaneBendingMomentSignals", default=None) # Not supported yet
    PitchBearingMxSignals: SignalPropertiesMoment = Field(alias="PitchBearingMxSignals", default=None) # Not supported yet
    PitchBearingMySignals: SignalPropertiesMoment = Field(alias="PitchBearingMySignals", default=None) # Not supported yet
    PitchBearingMzSignals: SignalPropertiesMoment = Field(alias="PitchBearingMzSignals", default=None) # Not supported yet
    PitchBearingRadialForceSignals: SignalPropertiesForce = Field(alias="PitchBearingRadialForceSignals", default=None) # Not supported yet
    PitchBearingAxialForceSignals: SignalPropertiesForce = Field(alias="PitchBearingAxialForceSignals", default=None) # Not supported yet
    PitchBearingFxSignals: SignalPropertiesForce = Field(alias="PitchBearingFxSignals", default=None) # Not supported yet
    PitchBearingFySignals: SignalPropertiesForce = Field(alias="PitchBearingFySignals", default=None) # Not supported yet
    BladeStationWindSpeedSignals: SignalPropertiesVelocity = Field(alias="BladeStationWindSpeedSignals", default=None) # Not supported yet
    BladeStationAngleOfAttackSignals: SignalPropertiesAngle = Field(alias="BladeStationAngleOfAttackSignals", default=None) # Not supported yet
    AileronAngleSignals: SignalPropertiesAngle = Field(alias="AileronAngleSignals", default=None) # Not supported yet
    AileronRateSignals: SignalPropertiesAngularVelocity = Field(alias="AileronRateSignals", default=None) # Not supported yet
    BladeStationPositionXSignals: SignalPropertiesLength = Field(alias="BladeStationPositionXSignals", default=None) # Not supported yet
    BladeStationPositionYSignals: SignalPropertiesLength = Field(alias="BladeStationPositionYSignals", default=None) # Not supported yet
    BladeStationPositionZSignals: SignalPropertiesLength = Field(alias="BladeStationPositionZSignals", default=None) # Not supported yet
    BladeStationPositionXRotationSignals: SignalPropertiesAngle = Field(alias="BladeStationPositionXRotationSignals", default=None) # Not supported yet
    BladeStationPositionYRotationSignals: SignalPropertiesAngle = Field(alias="BladeStationPositionYRotationSignals", default=None) # Not supported yet
    BladeStationPositionZRotationSignals: SignalPropertiesAngle = Field(alias="BladeStationPositionZRotationSignals", default=None) # Not supported yet
    LidarBeamFocalPointVelocitySignals: SignalPropertiesVelocity = Field(alias="LidarBeamFocalPointVelocitySignals", default=None) # Not supported yet

    _relative_schema_path = 'Turbine/BladedControl/MeasuredSignalProperties/MeasuredSignalProperties.json'
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


MeasuredSignalProperties.update_forward_refs()

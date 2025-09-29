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
from dnv_bladed_models.angle_vs_stiffness_torque import AngleVsStiffnessTorque
from dnv_bladed_models.damper import Damper
from dnv_bladed_models.pendulum_damper_mounting_position import PendulumDamperMountingPosition
from dnv_bladed_models.velocity_vs_damping_torque import VelocityVsDampingTorque

from .schema_helper import SchemaHelper
from .models_impl import *


class PendulumDamper(Damper):
    r"""
    A \"pendulum\" or \"tuned mass\" damper, which uses a suspended mass to damp oscillations in a tower.
    
    Not supported yet.
    
    Attributes
    ----------
    ComponentType : Literal['PendulumDamper'], default='PendulumDamper', Not supported yet
        Defines the specific type of Component model in use.  For a `PendulumDamper` object, this must always be set to a value of `PendulumDamper`.
    
    Length : float, Not supported yet
        The length of the (rigid) pendulum arm.
    
    Mass : float, Not supported yet
        The mass suspended at the end of the pendulum arm.
    
    Inertia : float, Not supported yet
        Any added inertia for the pendulum.
    
    Stiffness : float, Not supported yet
        The constant stiffness term for the hinge of the pendulum.  This is in addition to the non-linear terms defined in the AngleVsStiffnessTorque parameter.
    
    Damping : float, Not supported yet
        The constant damping term for the hinge of the pendulum.  This is in addition to the non-linear terms defined in the VelocityVsDampingTorque parameter.
    
    InitialAngle : float, Not supported yet
        The initial angle of the pendulum at the beginning of the simulation.
    
    ConstantFriction : float, Not supported yet
        The constant friction torque applied to rotational hinge.  Any other friction contributions will be in addition to this.
    
    AngleVsStiffnessTorque : List[AngleVsStiffnessTorque], Not supported yet
        A look-up table of additional stiffnesses that vary with the pendulum's position.
    
    VelocityVsDampingTorque : List[VelocityVsDampingTorque], Not supported yet
        A look-up table of additional damping that vary with the pendulum's velocity.
    
    MountingPosition : PendulumDamperMountingPosition, Not supported yet
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    ComponentType: Literal['PendulumDamper'] = Field(alias="ComponentType", default='PendulumDamper', allow_mutation=False, const=True) # Not supported yet # type: ignore
    Length: float = Field(alias="Length", default=None) # Not supported yet
    Mass: float = Field(alias="Mass", default=None) # Not supported yet
    Inertia: float = Field(alias="Inertia", default=None) # Not supported yet
    Stiffness: float = Field(alias="Stiffness", default=None) # Not supported yet
    Damping: float = Field(alias="Damping", default=None) # Not supported yet
    InitialAngle: float = Field(alias="InitialAngle", default=None) # Not supported yet
    ConstantFriction: float = Field(alias="ConstantFriction", default=None) # Not supported yet
    AngleVsStiffnessTorque: List[AngleVsStiffnessTorque] = Field(alias="AngleVsStiffnessTorque", default=list()) # Not supported yet
    VelocityVsDampingTorque: List[VelocityVsDampingTorque] = Field(alias="VelocityVsDampingTorque", default=list()) # Not supported yet
    MountingPosition: PendulumDamperMountingPosition = Field(alias="MountingPosition", default=None) # Not supported yet

    _relative_schema_path = 'Components/Damper/PendulumDamper.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set(['AngleVsStiffnessTorque','VelocityVsDampingTorque',]),
        'ComponentType').merge(Damper._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


PendulumDamper.update_forward_refs()

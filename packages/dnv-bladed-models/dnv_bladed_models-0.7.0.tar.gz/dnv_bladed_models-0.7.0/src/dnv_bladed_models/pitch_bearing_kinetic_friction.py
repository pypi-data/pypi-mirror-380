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
from dnv_bladed_models.pitch_bearing_friction_rate_relationship import PitchBearingFrictionRateRelationship
from dnv_bladed_models.pitch_bearing_friction_xy_force_relationship import PitchBearingFrictionXYForceRelationship
from dnv_bladed_models.pitch_bearing_friction_xy_moment_relationship import PitchBearingFrictionXYMomentRelationship
from dnv_bladed_models.pitch_bearing_friction_z_force_relationship import PitchBearingFrictionZForceRelationship

from .schema_helper import SchemaHelper
from .models_impl import *


class PitchBearingKineticFriction(BladedModel):
    r"""
    The torque resisting movement, once the bearing is in motion.
    
    Attributes
    ----------
    ConstantFriction : float, default=0
        The constant friction opposing the movement of the bearing.
    
    RelationshipWithXYMoment : PitchBearingFrictionXYMomentRelationship
    
    RelationshipWithXYForce : PitchBearingFrictionXYForceRelationship
    
    RelationshipWithZForce : PitchBearingFrictionZForceRelationship
    
    RelationshipWithRate : PitchBearingFrictionRateRelationship
    
    Notes
    -----
    
    """
    ConstantFriction: float = Field(alias="ConstantFriction", default=None)
    RelationshipWithXYMoment: PitchBearingFrictionXYMomentRelationship = Field(alias="RelationshipWithXYMoment", default=None)
    RelationshipWithXYForce: PitchBearingFrictionXYForceRelationship = Field(alias="RelationshipWithXYForce", default=None)
    RelationshipWithZForce: PitchBearingFrictionZForceRelationship = Field(alias="RelationshipWithZForce", default=None)
    RelationshipWithRate: PitchBearingFrictionRateRelationship = Field(alias="RelationshipWithRate", default=None)

    _relative_schema_path = 'Components/PitchSystem/Friction/PitchBearingKineticFriction/PitchBearingKineticFriction.json'
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


PitchBearingKineticFriction.update_forward_refs()

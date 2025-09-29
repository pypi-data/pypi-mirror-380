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
from dnv_bladed_models.applied_moment_vs_friction_torque import AppliedMomentVsFrictionTorque
from dnv_bladed_models.bladed_model import BladedModel

from .schema_helper import SchemaHelper
from .models_impl import *


class PitchBearingFrictionXYMomentRelationship(BladedModel):
    r"""
    The relationship between the Coulomb friction and the bending moment over the bearing.
    
    Attributes
    ----------
    FrictionTorquePerUnitAppliedMoment : float
        A fixed ratio between the bending moment over the bearing and the friction opposing the motion.
    
    AppliedMomentVsFrictionTorque : List[AppliedMomentVsFrictionTorque]
        A look-up table describing a non-linear relationship between the bending moment over the bearing and the corresponding friction.
    
    Notes
    -----
    
    """
    FrictionTorquePerUnitAppliedMoment: float = Field(alias="FrictionTorquePerUnitAppliedMoment", default=None)
    AppliedMomentVsFrictionTorque: List[AppliedMomentVsFrictionTorque] = Field(alias="AppliedMomentVsFrictionTorque", default=list())

    _relative_schema_path = 'Components/PitchSystem/Friction/PitchBearingKineticFriction/PitchBearingFrictionXYMomentRelationship/PitchBearingFrictionXYMomentRelationship.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set(['AppliedMomentVsFrictionTorque',]),
        None).merge(BladedModel._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


PitchBearingFrictionXYMomentRelationship.update_forward_refs()

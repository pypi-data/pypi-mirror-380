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
from dnv_bladed_models.applied_z_force_vs_friction_torque import AppliedZForceVsFrictionTorque
from dnv_bladed_models.bladed_model import BladedModel

from .schema_helper import SchemaHelper
from .models_impl import *


class PitchBearingFrictionZForceRelationship(BladedModel):
    r"""
    The relationship between the Coulomb friction and the axial force on the bearing.
    
    Attributes
    ----------
    FrictionTorquePerUnitAppliedForce : float
        A fixed ratio between the axial force on the bearing and the friction opposing the motion.
    
    AppliedForceVsFrictionTorque : List[AppliedZForceVsFrictionTorque]
        A look-up table describing a non-linear relationship between the axial force on the bearing and the corresponding friction.
    
    Notes
    -----
    
    """
    FrictionTorquePerUnitAppliedForce: float = Field(alias="FrictionTorquePerUnitAppliedForce", default=None)
    AppliedForceVsFrictionTorque: List[AppliedZForceVsFrictionTorque] = Field(alias="AppliedForceVsFrictionTorque", default=list())

    _relative_schema_path = 'Components/PitchSystem/Friction/PitchBearingKineticFriction/PitchBearingFrictionZForceRelationship/PitchBearingFrictionZForceRelationship.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set(['AppliedForceVsFrictionTorque',]),
        None).merge(BladedModel._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


PitchBearingFrictionZForceRelationship.update_forward_refs()

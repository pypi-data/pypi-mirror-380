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
from dnv_bladed_models.drivetrain_and_nacelle_moment_of_inertia import DrivetrainAndNacelleMomentOfInertia
from dnv_bladed_models.vector3_d import Vector3D

from .schema_helper import SchemaHelper
from .models_impl import *


class DrivetrainAndNacelleMassProperties(BladedModel):
    r"""
    The mass properties of the nacelle and all of its contents, such as the generator or drivetrain.
    
    Attributes
    ----------
    TotalMass : float
        The total mass of the nacelle and all of its contents, such as the generator or drivetrain.
    
    CentreOfGravity : Vector3D
    
    MomentOfInertia : DrivetrainAndNacelleMomentOfInertia
    
    Notes
    -----
    
    """
    TotalMass: float = Field(alias="TotalMass", default=None)
    CentreOfGravity: Vector3D = Field(alias="CentreOfGravity", default=None)
    MomentOfInertia: DrivetrainAndNacelleMomentOfInertia = Field(alias="MomentOfInertia", default=None)

    _relative_schema_path = 'Components/DrivetrainAndNacelle/DrivetrainAndNacelleMassProperties/DrivetrainAndNacelleMassProperties.json'
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


DrivetrainAndNacelleMassProperties.update_forward_refs()

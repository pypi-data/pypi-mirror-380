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
from dnv_bladed_models.pitch_controller_torque_safety_system import PitchControllerTorqueSafetySystem

from .schema_helper import SchemaHelper
from .models_impl import *


class PitchTorqueSetByExternalController(PitchControllerTorqueSafetySystem):
    r"""
    A pitch safety system where the torque is specified by the main controller.
    
    Attributes
    ----------
    PitchSafetySystemType : Literal['TorqueSetByExternalController'], default='TorqueSetByExternalController'
        Defines the specific type of PitchSafetySystem model in use.  For a `TorqueSetByExternalController` object, this must always be set to a value of `TorqueSetByExternalController`.
    
    Notes
    -----
    
    """
    PitchSafetySystemType: Literal['TorqueSetByExternalController'] = Field(alias="PitchSafetySystemType", default='TorqueSetByExternalController', allow_mutation=False, const=True) # type: ignore

    _relative_schema_path = 'Components/PitchSystem/PitchController/PitchSafetySystem/PitchTorqueSetByExternalController.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'PitchSafetySystemType').merge(PitchControllerTorqueSafetySystem._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


PitchTorqueSetByExternalController.update_forward_refs()

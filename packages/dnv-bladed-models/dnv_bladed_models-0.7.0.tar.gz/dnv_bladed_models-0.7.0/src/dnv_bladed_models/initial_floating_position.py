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
from dnv_bladed_models.initial_position import InitialPosition
from dnv_bladed_models.vector3_d import Vector3D

from .schema_helper import SchemaHelper
from .models_impl import *


class InitialFloatingPosition(InitialPosition):
    r"""
    Initial mooring position.  This can be provided where the equilibrium position of a floating position is time-consuming to calculate.
    
    Not supported yet.
    
    Attributes
    ----------
    InitialConditionType : Literal['InitialFloatingPosition'], default='InitialFloatingPosition', Not supported yet
        Defines the specific type of InitialCondition model in use.  For a `InitialFloatingPosition` object, this must always be set to a value of `InitialFloatingPosition`.
    
    PositionOfOrigin : Vector3D
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    InitialConditionType: Literal['InitialFloatingPosition'] = Field(alias="InitialConditionType", default='InitialFloatingPosition', allow_mutation=False, const=True) # Not supported yet # type: ignore
    PositionOfOrigin: Vector3D = Field(alias="PositionOfOrigin", default=None)

    _relative_schema_path = 'TimeDomainSimulation/InitialCondition/InitialFloatingPosition.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'InitialConditionType').merge(InitialPosition._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


InitialFloatingPosition.update_forward_refs()

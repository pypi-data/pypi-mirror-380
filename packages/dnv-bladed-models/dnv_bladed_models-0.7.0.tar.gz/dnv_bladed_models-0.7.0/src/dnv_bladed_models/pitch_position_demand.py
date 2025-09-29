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
from dnv_bladed_models.pitch_system_demand import PitchSystemDemand

from .schema_helper import SchemaHelper
from .models_impl import *


class PitchPositionDemand(PitchSystemDemand):
    r"""
    A position response, where the pitch controller receives a pitch angle to achieve from the main controller.
    
    Attributes
    ----------
    PitchSystemDemandType : Literal['Position'], default='Position'
        Defines the specific type of PitchSystemDemand model in use.  For a `Position` object, this must always be set to a value of `Position`.
    
    Notes
    -----
    
    """
    PitchSystemDemandType: Literal['Position'] = Field(alias="PitchSystemDemandType", default='Position', allow_mutation=False, const=True) # type: ignore

    _relative_schema_path = 'Components/PitchSystem/PitchController/PitchSystemDemand/PitchPositionDemand.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'PitchSystemDemandType').merge(PitchSystemDemand._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


PitchPositionDemand.update_forward_refs()

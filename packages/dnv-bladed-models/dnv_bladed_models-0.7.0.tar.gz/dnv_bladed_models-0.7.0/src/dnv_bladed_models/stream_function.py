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
from dnv_bladed_models.regular_waves import RegularWaves

from .schema_helper import SchemaHelper
from .models_impl import *


class StreamFunction(RegularWaves):
    r"""
    The definition of Stream Function waves.
    
    Not supported yet.
    
    Attributes
    ----------
    WavesType : Literal['StreamFunction'], default='StreamFunction', Not supported yet
        Defines the specific type of Waves model in use.  For a `StreamFunction` object, this must always be set to a value of `StreamFunction`.
    
    UseTotalAcceleration : bool, Not supported yet
        If true, total acceleration (convective and time derivative) will be used for Morison loading when using the stream function.  The water particle accelerations in Bladed only include the time derivative terms. The convective terms of the water particles can be added when using the stream function for the water particle acceleration calculations.  If irregular waves and additional constrained waves are applied, where the constrained wave is defined by a stream function and total acceleration is turned on, the water particle acceleration will be calculated using local derivatives for the irregular waves and substantive derivatives for the constrained waves and will therefore be inconsistent.
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    WavesType: Literal['StreamFunction'] = Field(alias="WavesType", default='StreamFunction', allow_mutation=False, const=True) # Not supported yet # type: ignore
    UseTotalAcceleration: bool = Field(alias="UseTotalAcceleration", default=None) # Not supported yet

    _relative_schema_path = 'TimeDomainSimulation/Environment/SeaState/Waves/StreamFunction.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'WavesType').merge(RegularWaves._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


StreamFunction.update_forward_refs()

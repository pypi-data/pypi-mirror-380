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

from .schema_helper import SchemaHelper
from .models_impl import *


class SequentialTimestepAdaptation(BladedModel):
    r"""
    Parameters for the Sequential Timestep Adaptation (STA) technique.
    
    Not supported yet.
    
    Attributes
    ----------
    FineTimeStepStart : float, default=0, Not supported yet
        The time at which the fine time step will start being used.  It is recommended to select a sufficient time buffer to allow wake to develop before evaluating the results.  A value of 0.0 (default) means that the fine time starts right away (no STA technique in use); a value greater than zero means that the STA technique in use.  Consider setting it to be a value such that it starts during the transient initial simulation period.
    
    MaximumTimestepCoarseningLevel : float, default=1, Not supported yet
        The maximum multiplier of the time step for updating vortex wake time step.  A value of 1.0 (default) means the Vortex wake time step is constant (no STA technique in use).  A value greater than 1.0 means the STA technique in use, and the vortex wake time step is multiplied at maximum by this number.
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    FineTimeStepStart: float = Field(alias="FineTimeStepStart", default=None) # Not supported yet
    MaximumTimestepCoarseningLevel: float = Field(alias="MaximumTimestepCoarseningLevel", default=None) # Not supported yet

    _relative_schema_path = 'Settings/AerodynamicSettings/AerodynamicModel/SequentialTimestepAdaptation/SequentialTimestepAdaptation.json'
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


SequentialTimestepAdaptation.update_forward_refs()

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
from dnv_bladed_models.pitch_fault import PitchFault

from .schema_helper import SchemaHelper
from .models_impl import *


class PitchFaultLimp(PitchFault):
    r"""
    The failure of a blade's pitch system at a specified time that leaves it without actuation and free to move.
    
    Not supported yet.
    
    Attributes
    ----------
    EventType : Literal['PitchFaultLimp'], default='PitchFaultLimp', Not supported yet
        Defines the specific type of Event model in use.  For a `PitchFaultLimp` object, this must always be set to a value of `PitchFaultLimp`.
    
    IncludePitchFriction : bool, Not supported yet
        If true, the friction defined in the pitch system will be applied to the joint.
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    EventType: Literal['PitchFaultLimp'] = Field(alias="EventType", default='PitchFaultLimp', allow_mutation=False, const=True) # Not supported yet # type: ignore
    IncludePitchFriction: bool = Field(alias="IncludePitchFriction", default=None) # Not supported yet

    _relative_schema_path = 'TimeDomainSimulation/Event/PitchFaultLimp.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'EventType').merge(PitchFault._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


PitchFaultLimp.update_forward_refs()

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
from dnv_bladed_models.conditional_event import ConditionalEvent

from .schema_helper import SchemaHelper
from .models_impl import *


class PitchFaultSeizureAtAngle(ConditionalEvent):
    r"""
    The failure of a blade's pitch system when it passes through a specified angle that leaves it without actuation and free to move.  If the pitch system never passes through the specified angle, no seizure will occur.
    
    Not supported yet.
    
    Attributes
    ----------
    EventType : Literal['PitchFaultSeizureAtAngle'], default='PitchFaultSeizureAtAngle', Not supported yet
        Defines the specific type of Event model in use.  For a `PitchFaultSeizureAtAngle` object, this must always be set to a value of `PitchFaultSeizureAtAngle`.
    
    OnComponentInAssembly : str, regex=^Assembly.(.+)$, Not supported yet
        A qualified, dot-separated path to a component in the assembly tree to which this applies.  e.g. `Assembly.Hub.PitchSystem1`
    
    SeizesAsItPassesAngle : float, Not supported yet
        The angle of the pitch system at which it will seize.  If the pitch system never passes through the specified angle, no seizure will occur.
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    EventType: Literal['PitchFaultSeizureAtAngle'] = Field(alias="EventType", default='PitchFaultSeizureAtAngle', allow_mutation=False, const=True) # Not supported yet # type: ignore
    OnComponentInAssembly: str = Field(alias="@OnComponentInAssembly", default=None, regex='^Assembly.(.+)$') # Not supported yet
    SeizesAsItPassesAngle: float = Field(alias="SeizesAsItPassesAngle", default=None) # Not supported yet

    _relative_schema_path = 'TimeDomainSimulation/Event/PitchFaultSeizureAtAngle.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'EventType').merge(ConditionalEvent._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


PitchFaultSeizureAtAngle.update_forward_refs()

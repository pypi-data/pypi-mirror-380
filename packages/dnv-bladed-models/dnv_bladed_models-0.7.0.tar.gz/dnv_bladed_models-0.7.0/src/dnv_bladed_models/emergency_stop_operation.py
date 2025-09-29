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
from dnv_bladed_models.controlled_stop import ControlledStop

from .schema_helper import SchemaHelper
from .models_impl import *


class EmergencyStopOperation(ControlledStop):
    r"""
    A request for the controller to stop the turbine or rotor at a specified time in the simulation.  The stop will be performed by the safety system.
    
    Attributes
    ----------
    EventType : Literal['EmergencyStopOperation'], default='EmergencyStopOperation'
        Defines the specific type of Event model in use.  For a `EmergencyStopOperation` object, this must always be set to a value of `EmergencyStopOperation`.
    
    Notes
    -----
    
    """
    EventType: Literal['EmergencyStopOperation'] = Field(alias="EventType", default='EmergencyStopOperation', allow_mutation=False, const=True) # type: ignore

    _relative_schema_path = 'TimeDomainSimulation/Event/EmergencyStopOperation.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'EventType').merge(ControlledStop._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


EmergencyStopOperation.update_forward_refs()

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
from dnv_bladed_models.controlled_operation import ControlledOperation
from dnv_bladed_models.idealised_yaw_manoeuvre import IdealisedYawManoeuvre

from .schema_helper import SchemaHelper
from .models_impl import *


class YawManoeuvre(ControlledOperation):
    r"""
    A prescribed yaw manoever, occuring at a specified time in the simulation.
    
    Not supported yet.
    
    Attributes
    ----------
    EventType : Literal['YawManoeuvre'], default='YawManoeuvre', Not supported yet
        Defines the specific type of Event model in use.  For a `YawManoeuvre` object, this must always be set to a value of `YawManoeuvre`.
    
    FinalYawAngle : float, Not supported yet
        The yaw angle at which to stop.
    
    Idealised : IdealisedYawManoeuvre, Not supported yet
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    EventType: Literal['YawManoeuvre'] = Field(alias="EventType", default='YawManoeuvre', allow_mutation=False, const=True) # Not supported yet # type: ignore
    FinalYawAngle: float = Field(alias="FinalYawAngle", default=None) # Not supported yet
    Idealised: IdealisedYawManoeuvre = Field(alias="Idealised", default=None) # Not supported yet

    _relative_schema_path = 'TimeDomainSimulation/Event/YawManoeuvre.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'EventType').merge(ControlledOperation._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


YawManoeuvre.update_forward_refs()

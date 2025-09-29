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
from dnv_bladed_models.yaw_fault import YawFault

from .schema_helper import SchemaHelper
from .models_impl import *


class YawFaultLimp(YawFault):
    r"""
    A fault in the yaw system where the yaw system is left without actuation.  The reaction torques are specified, and if these forces are overcome, the yaw bearing will move.
    
    Not supported yet.
    
    Attributes
    ----------
    EventType : Literal['YawFaultLimp'], default='YawFaultLimp', Not supported yet
        Defines the specific type of Event model in use.  For a `YawFaultLimp` object, this must always be set to a value of `YawFaultLimp`.
    
    Friction : float, Not supported yet
        The kinetic friction in the yaw bearing and any connected systems.
    
    Stiffness : float, Not supported yet
        The stiffness of the yaw system, if it has failed without actuation.
    
    Damping : float, Not supported yet
        The damping on the yaw system, if it has failed without actuation.
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    EventType: Literal['YawFaultLimp'] = Field(alias="EventType", default='YawFaultLimp', allow_mutation=False, const=True) # Not supported yet # type: ignore
    Friction: float = Field(alias="Friction", default=None) # Not supported yet
    Stiffness: float = Field(alias="Stiffness", default=None) # Not supported yet
    Damping: float = Field(alias="Damping", default=None) # Not supported yet

    _relative_schema_path = 'TimeDomainSimulation/Event/YawFaultLimp.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'EventType').merge(YawFault._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


YawFaultLimp.update_forward_refs()

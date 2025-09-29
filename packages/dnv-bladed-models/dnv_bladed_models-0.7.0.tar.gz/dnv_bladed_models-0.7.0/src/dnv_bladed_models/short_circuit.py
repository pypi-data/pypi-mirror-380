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
from dnv_bladed_models.fault import Fault

from .schema_helper import SchemaHelper
from .models_impl import *


class ShortCircuit(Fault):
    r"""
    A short circuit that occurs at a specified time in the simulation.
    
    Not supported yet.
    
    Attributes
    ----------
    EventType : Literal['ShortCircuit'], default='ShortCircuit', Not supported yet
        Defines the specific type of Event model in use.  For a `ShortCircuit` object, this must always be set to a value of `ShortCircuit`.
    
    Filepath : str, Not supported yet
        The filepath or URI of the short circuit data.
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    EventType: Literal['ShortCircuit'] = Field(alias="EventType", default='ShortCircuit', allow_mutation=False, const=True) # Not supported yet # type: ignore
    Filepath: str = Field(alias="Filepath", default=None) # Not supported yet

    _relative_schema_path = 'TimeDomainSimulation/Event/ShortCircuit.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'EventType').merge(Fault._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


ShortCircuit.update_forward_refs()

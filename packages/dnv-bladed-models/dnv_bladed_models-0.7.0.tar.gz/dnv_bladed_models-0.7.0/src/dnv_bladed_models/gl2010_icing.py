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
from dnv_bladed_models.iced_condition import IcedCondition

from .schema_helper import SchemaHelper
from .models_impl import *


class GL2010Icing(IcedCondition):
    r"""
    The initial condition of a blade being iced according to the GL2010 standards.  This will remain unchanged throughout the simulation.
    
    Not supported yet.
    
    Attributes
    ----------
    InitialConditionType : Literal['GL2010Icing'], default='GL2010Icing', Not supported yet
        Defines the specific type of InitialCondition model in use.  For a `GL2010Icing` object, this must always be set to a value of `GL2010Icing`.
    
    ReferenceTipChord : float, Not supported yet
        The blade tip chord  for the GL2010 ice model standards.
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    InitialConditionType: Literal['GL2010Icing'] = Field(alias="InitialConditionType", default='GL2010Icing', allow_mutation=False, const=True) # Not supported yet # type: ignore
    ReferenceTipChord: float = Field(alias="ReferenceTipChord", default=None) # Not supported yet

    _relative_schema_path = 'TimeDomainSimulation/InitialCondition/GL2010Icing.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'InitialConditionType').merge(IcedCondition._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


GL2010Icing.update_forward_refs()

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
from dnv_bladed_models.load_bank import LoadBank

from .schema_helper import SchemaHelper
from .models_impl import *


class YawActuation(BladedModel):
    r"""
    The properties related to the actuation of the yaw system.
    
    Attributes
    ----------
    ExternalLoadsFilepath : str
        The filepath to an External Loads DLL module that will apply the relevant actuator torque. This is optional and can also be applied in other specified External Loads DLLs.
    
    EffectiveGearRatio : float
        The effective total ratio for all load banks of the input high-speed shaft's rotations to the output low-speed shaft's rotations.
    
    LoadBanks : List[LoadBank]
        The properties of the load banks.
    
    Notes
    -----
    
    """
    ExternalLoadsFilepath: str = Field(alias="ExternalLoadsFilepath", default=None)
    EffectiveGearRatio: float = Field(alias="EffectiveGearRatio", default=None)
    LoadBanks: List[LoadBank] = Field(alias="LoadBanks", default=list())

    _relative_schema_path = 'Components/YawSystem/YawActuation/YawActuation.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set(['LoadBanks',]),
        None).merge(BladedModel._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


YawActuation.update_forward_refs()

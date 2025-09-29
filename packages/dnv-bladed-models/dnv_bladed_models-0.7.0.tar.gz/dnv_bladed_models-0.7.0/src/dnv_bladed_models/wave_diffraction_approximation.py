# *********************************************************************#
# Bladed Python Models API                                             #
# Copyright (c) DNV Services UK Limited (c) 2025. All rights reserved. #
# MIT License (see license file)                                       #
# *********************************************************************#


# coding: utf-8

from __future__ import annotations

from abc import ABC

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
class WaveDiffractionApproximation_WaveDiffractionApproximationTypeEnum(str, Enum):
    AUTOMATIC_MAC_CAMY_FUCHS = "AutomaticMacCamyFuchs"
    AUTOMATIC_SIMPLE_CUTOFF_FREQUENCY = "AutomaticSimpleCutoffFrequency"
    MAC_CAMY_FUCHS = "MacCamyFuchs"
    SIMPLE_CUTOFF_FREQUENCY = "SimpleCutoffFrequency"
    INSERT = "Insert"

from .schema_helper import SchemaHelper
from .models_impl import *


class WaveDiffractionApproximation(BladedModel, ABC):
    r"""
    The method used for wave diffraction approximation and the option for parameters to be auto-defined.
    
    Not supported yet.
    
    Attributes
    ----------
    WaveDiffractionApproximationType : WaveDiffractionApproximation_WaveDiffractionApproximationTypeEnum, Not supported yet
        Defines the specific type of model in use.
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    This class is an abstraction, with the following concrete implementations:
        - AutomaticMacCamyFuchs
        - AutomaticSimpleCutoffFrequency
        - WaveDiffractionApproximationInsert
        - MacCamyFuchs
        - SimpleCutoffFrequency
    
    """
    WaveDiffractionApproximationType: WaveDiffractionApproximation_WaveDiffractionApproximationTypeEnum = Field(alias="WaveDiffractionApproximationType", default=None) # Not supported yet

    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        None).merge(BladedModel._type_info)


WaveDiffractionApproximation.update_forward_refs()

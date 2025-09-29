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
class Integrator_IntegratorTypeEnum(str, Enum):
    EXPLICIT_NEWMARK_BETA_FIXED_STEP = "ExplicitNewmarkBetaFixedStep"
    GENERALISED_ALPHA_FIXED_STEP = "GeneralisedAlphaFixedStep"
    IMPLICIT_NEWMARK_BETA_FIXED_STEP = "ImplicitNewmarkBetaFixedStep"
    RUNGE_KUTTA_VARIABLE_STEP = "RungeKuttaVariableStep"
    INSERT = "Insert"

from .schema_helper import SchemaHelper
from .models_impl import *


class Integrator(BladedModel, ABC):
    r"""
    The settings for the integrator, used for all time domain simulations.
    
    Attributes
    ----------
    IntegratorType : Integrator_IntegratorTypeEnum
        Defines the specific type of model in use.
    
    Notes
    -----
    
    This class is an abstraction, with the following concrete implementations:
        - ExplicitNewmarkBetaFixedStep
        - GeneralisedAlphaFixedStep
        - ImplicitNewmarkBetaFixedStep
        - IntegratorInsert
        - RungeKuttaVariableStep
    
    """
    IntegratorType: Integrator_IntegratorTypeEnum = Field(alias="IntegratorType", default=None)

    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        None).merge(BladedModel._type_info)


Integrator.update_forward_refs()

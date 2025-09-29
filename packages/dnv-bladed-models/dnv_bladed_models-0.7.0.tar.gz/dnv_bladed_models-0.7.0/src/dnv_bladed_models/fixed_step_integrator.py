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
from dnv_bladed_models.integrator import Integrator

from .schema_helper import SchemaHelper
from .models_impl import *


class FixedStepIntegrator(Integrator, ABC):
    r"""
    Common settings for the fixed step integrators.
    
    Attributes
    ----------
    TimeStep : float
        The fixed time step used by the integrator.  It must be set as a divisor of the output time-step and external controller communication interval.
    
    Tolerance : float, default=0.005
        When the \"Maximum number of iterations\" > 1, the integrator relative tolerance is used to control how many iterations are carried out when integrating the first order and prescribed second order states.  Iterations are carried out until the maximum number of iterations is reached, or until the change in all first order and prescribed state derivatives between successive iterations is less than the relative tolerance multiplied by the state derivative absolute value.
    
    Notes
    -----
    
    """
    TimeStep: float = Field(alias="TimeStep", default=None)
    Tolerance: float = Field(alias="Tolerance", default=None)

    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        None).merge(Integrator._type_info)


FixedStepIntegrator.update_forward_refs()

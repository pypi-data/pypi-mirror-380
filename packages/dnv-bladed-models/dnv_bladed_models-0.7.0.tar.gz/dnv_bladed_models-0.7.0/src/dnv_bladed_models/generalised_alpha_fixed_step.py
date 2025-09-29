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
from dnv_bladed_models.fixed_step_integrator import FixedStepIntegrator

from .schema_helper import SchemaHelper
from .models_impl import *


class GeneralisedAlphaFixedStep(FixedStepIntegrator):
    r"""
    Settings for the Generalised Alpha Fixed Step integrator.
    
    Attributes
    ----------
    IntegratorType : Literal['GeneralisedAlphaFixedStep'], default='GeneralisedAlphaFixedStep'
        Defines the specific type of Integrator model in use.  For a `GeneralisedAlphaFixedStep` object, this must always be set to a value of `GeneralisedAlphaFixedStep`.
    
    MaximumNumberOfIterations : int, default=1
        The maximum number of iterations for prescribed freedoms and first order states (e.g. dynamic stall & wake).  A value of 1 may sometimes inprecisely integrate first order states
    
    SpectralRadiusAtInfiniteFrequency : float, default=0.8
        This determines the numerical damping of high-frequency modes.  A value of 1 provides no numerical damping and a low value provides heavy numerical damping on high-frequency modes which can improve stability but decrease precision.
    
    Notes
    -----
    
    """
    IntegratorType: Literal['GeneralisedAlphaFixedStep'] = Field(alias="IntegratorType", default='GeneralisedAlphaFixedStep', allow_mutation=False, const=True) # type: ignore
    MaximumNumberOfIterations: int = Field(alias="MaximumNumberOfIterations", default=None)
    SpectralRadiusAtInfiniteFrequency: float = Field(alias="SpectralRadiusAtInfiniteFrequency", default=None)

    _relative_schema_path = 'Settings/SolverSettings/Integrator/GeneralisedAlphaFixedStep.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'IntegratorType').merge(FixedStepIntegrator._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


GeneralisedAlphaFixedStep.update_forward_refs()

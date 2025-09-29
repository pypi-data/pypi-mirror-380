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


class ExplicitNewmarkBetaFixedStep(FixedStepIntegrator):
    r"""
    Settings for the Explicit Newmark Beta Fixed Step integrator.
    
    Attributes
    ----------
    IntegratorType : Literal['ExplicitNewmarkBetaFixedStep'], default='ExplicitNewmarkBetaFixedStep'
        Defines the specific type of Integrator model in use.  For a `ExplicitNewmarkBetaFixedStep` object, this must always be set to a value of `ExplicitNewmarkBetaFixedStep`.
    
    MaximumNumberOfIterations : int, default=1
        The maximum number of iterations for prescribed freedoms and first order states (e.g. dynamic stall & wake).  A value of 1 may sometimes inprecisely integrate first order states
    
    Beta : float, default=0.25
        The β parameter for the Newmark-β integration method.  The recommended value of 0.25 (with a γ value of 0.50) results in the constant average acceleration method that is unconditionally stable for linear systems.  A value of 0.26 (with a γ value of 0.52) results in a method that is close to the constant average acceleration method but includes a small amount of numerical damping to reduce unwanted vibrations of high-frequency modes. Note that the numerical damping increases with the step size.
    
    Gamma : float, default=0.5
        The γ parameter for the Newmark-β integration method.  The recommended value depends on the β parameter and given by the formula γ = 2.sqrt(β) - 0.5.  Values higher than 0.5 introduce positive numerical damping, whereas lower values introduce negative numerical damping.
    
    Notes
    -----
    
    """
    IntegratorType: Literal['ExplicitNewmarkBetaFixedStep'] = Field(alias="IntegratorType", default='ExplicitNewmarkBetaFixedStep', allow_mutation=False, const=True) # type: ignore
    MaximumNumberOfIterations: int = Field(alias="MaximumNumberOfIterations", default=None)
    Beta: float = Field(alias="Beta", default=None)
    Gamma: float = Field(alias="Gamma", default=None)

    _relative_schema_path = 'Settings/SolverSettings/Integrator/ExplicitNewmarkBetaFixedStep.json'
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


ExplicitNewmarkBetaFixedStep.update_forward_refs()

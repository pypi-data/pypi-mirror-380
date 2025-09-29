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
class ExternalController_CallingConventionEnum(str, Enum):
    CDECL = "__cdecl"
    STDCALL = "__stdcall"
class ExternalController_TimeStepMultiplierEnum(str, Enum):
    EVERY = "Every"
    SECOND = "Second"
    THIRD = "Third"
    FOURTH = "Fourth"
    FIFTH = "Fifth"
    SIXTH = "Sixth"
    SEVENTH = "Seventh"
    EIGTH = "Eigth"
    NINTH = "Ninth"
    TENTH = "Tenth"

from .schema_helper import SchemaHelper
from .models_impl import *


class ExternalController(BladedModel):
    r"""
    A definition of a single controller for the turbine.
    
    Attributes
    ----------
    Filepath : str
        The location of the external controller dll.
    
    CallingConvention : ExternalController_CallingConventionEnum, default='__cdecl'
        The calling convention to be used when calling the external controller.  The default for all C-family languages is '__cdecl'.  The default for FORTRAN is '__stdcall' unless the [C] qualifier is specfied immediately after the function name.  Specifying the wrong calling convention can lead to unexplained system exceptions when attempting to call the external controller.
    
    FunctionName : str, default='ExternalController'
        The name of the function in the dll to run.  This must satisfy the standard external controller typedef, found in the ExternalControllerApi.h.
    
    PassParametersByFile : bool, default=False
        If true, a file will be written containing the parameters in the above box.  The location of this file can be obtained in the external controller using the function GetInfileFilepath.  The name of this file will be \"DISCON.IN\" if there is only one controller, or of the pattern \"DISCONn.IN\", where 'n' is the number of the controller.  If not checked (the default), this string will be directly available using the function GetUserParameters.
    
    ForceLegacy : bool, default=False
        If true, only the old-style 'DISCON' function will be looked for in the controller, and raise an error if it cannot be found.  This is only used for testing legacy controllers where both CONTROLLER and DISCON functions are both defined, but the DISCON function is required.
    
    TimeStepMultiplier : ExternalController_TimeStepMultiplierEnum, default='Every'
        Whether the controller should be called on every discrete timestep, set above.
    
    ParametersAsString : str
        A string that will be passed to the external controller.
    
    ParametersAsJson : Dict[str, Any]
        A JSON object that will be serialised as a string and passed to the external controller.
    
    UseFloatingPointProtection : bool, default=True
        If true, this will apply floating point protection when calling the external controllers.  When the protection is on, any floating point errors are trapped and reported.  When this is switched off, the behaviour will default to that of the computer's floating point machine, but this can often be to not report the error, and to use a semi-random (but often very large) number instead of the correct result.  This can lead to unrepeatable results and numeric errors.
    
    Notes
    -----
    
    """
    Filepath: str = Field(alias="Filepath", default=None)
    CallingConvention: ExternalController_CallingConventionEnum = Field(alias="CallingConvention", default=None)
    FunctionName: str = Field(alias="FunctionName", default=None)
    PassParametersByFile: bool = Field(alias="PassParametersByFile", default=None)
    ForceLegacy: bool = Field(alias="ForceLegacy", default=None)
    TimeStepMultiplier: ExternalController_TimeStepMultiplierEnum = Field(alias="TimeStepMultiplier", default=None)
    ParametersAsString: str = Field(alias="ParametersAsString", default=None)
    ParametersAsJson: Dict[str, Any] = Field(alias="ParametersAsJson", default=None)
    UseFloatingPointProtection: bool = Field(alias="UseFloatingPointProtection", default=None)

    _relative_schema_path = 'Turbine/BladedControl/ExternalController/ExternalController.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        None).merge(BladedModel._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


ExternalController.update_forward_refs()

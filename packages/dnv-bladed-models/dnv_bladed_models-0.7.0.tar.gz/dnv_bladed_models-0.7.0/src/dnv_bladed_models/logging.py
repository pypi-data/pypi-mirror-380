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
class Logging_ConsoleLoggingLevelEnum(str, Enum):
    SILENT = "SILENT"
    EXCEPTIONS = "EXCEPTIONS"
    WARNINGS = "WARNINGS"
    INFORMATION = "INFORMATION"
    DIAGNOSTIC = "DIAGNOSTIC"
class Logging_MessageFileLoggingLevelEnum(str, Enum):
    EXCEPTIONS = "EXCEPTIONS"
    WARNINGS = "WARNINGS"
    INFORMATION = "INFORMATION"
    DIAGNOSTIC = "DIAGNOSTIC"
class Logging_SupportingFilesEnum(str, Enum):
    BASIC = "BASIC"
    VERIFICATION = "VERIFICATION"
    DIAGNOSTIC = "DIAGNOSTIC"
class Logging_VisualisationEnum(str, Enum):
    NONE = "NONE"
    MODEL = "MODEL"
    ANIMATION = "ANIMATION"

from .schema_helper import SchemaHelper
from .models_impl import *


class Logging(BladedModel):
    r"""
    Default settings for the logging of the supporting data, such as verification or progress data.  Many of these settings can be overridden for individual analyses using command line options.
    
    Attributes
    ----------
    ConsoleLoggingLevel : Logging_ConsoleLoggingLevelEnum, default='WARNINGS'
        The level of detail to report to stdout and stderr:   'SILENT': there will be no messages written to the console.   'EXCEPTIONS': only error messages will be written to the console.   'WARNING': error messages plus warning messages.   'INFORMATION': additional notes describing the simulation.   'DIAGNOSTIC': includes additional details which would might help explain more subtle simulation behaviour.
    
    MessageFileLoggingLevel : Logging_MessageFileLoggingLevelEnum, default='INFORMATION'
        The level of detail to report to the $ME message file:   'EXCEPTIONS': only error messages will be written to the file.   'WARNING': error messages plus warning messages.   'INFORMATION': additional notes describing the simulation.   'DIAGNOSTIC': includes additional details which would might help explain more subtle simulation behaviour.
    
    SupportingFiles : Logging_SupportingFilesEnum, default='BASIC'
        The level of supporting files to be written to the output directory during the analysis:   'BASIC' includes .$ME and .$TE files.   'VERIFICATION' produces additional reports summarising the inputs with minimal processing, such as inertia properties and basic mode data.   'DIAGNOSTIC' will output any data during the analysis that may assist in diagnosing problems. This may impair the performance. These options are cumulative, with DIAGNOSTIC including all VERIFICATION outputs; VERIFICATION indluding all CONSOLIDATED_INPUTS; and CONSOLIDATED_INPUTS including all BASIC outputs.
    
    ProgressFile : bool, default=True
        If true, a .$PR file containing a single number detailing the progree will be written to the working directory and updated throughout the analysis.  This can be read by the calling process such as a GUI or batch manager.
    
    Visualisation : Logging_VisualisationEnum, default='NONE'
        The level of additional visualisation files to produce during an analysis:   'MODEL' produces additional files to allow external software to produce a static 3D model of the turbine.   'ANIMATION' produces additional files and time-series to allow external software to animate the movement of the turbine.
    
    Notes
    -----
    
    """
    ConsoleLoggingLevel: Logging_ConsoleLoggingLevelEnum = Field(alias="ConsoleLoggingLevel", default=None)
    MessageFileLoggingLevel: Logging_MessageFileLoggingLevelEnum = Field(alias="MessageFileLoggingLevel", default=None)
    SupportingFiles: Logging_SupportingFilesEnum = Field(alias="SupportingFiles", default=None)
    ProgressFile: bool = Field(alias="ProgressFile", default=None)
    Visualisation: Logging_VisualisationEnum = Field(alias="Visualisation", default=None)

    _relative_schema_path = 'Settings/Logging/Logging.json'
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


Logging.update_forward_refs()

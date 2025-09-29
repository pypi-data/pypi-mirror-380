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
from dnv_bladed_models.outputs import Outputs
from dnv_bladed_models.selected_component_output_group import SelectedComponentOutputGroup

from .schema_helper import SchemaHelper
from .models_impl import *


class TimeDomainOutputs(Outputs):
    r"""
    The definition outputs to write for this simulation.
    
    Attributes
    ----------
    TimeStepForOutputs : float
        The output time step for the simulation.
    
    LengthOfOutputBuffer : float
        The length of time to buffer the output logs.
    
    OutputSummaryInformation : bool, default=True
        If true, the summary information output group will be created.
    
    OutputExternalControllers : bool, default=True
        If true, the controller output group will be created.
    
    OutputBuoyancyInformation : bool, default=False
        If true, the buoyancy output group will be created.
    
    OutputFiniteElementMatrices : bool, default=False
        If true, the finite element output group will be created, providing far more detail about the finite element matrices.
    
    OutputSignalProperties : bool, default=False
        If true, the signal properties output group will be created.  This records the properties provided to the controller, with and without noise and other distortions.
    
    OutputWakePropagation : bool, default=False
        If true, the eddy viscosity propagation of the wake is output as a 2D table of relative velocity against radial position and distance traveled to a \".wake\" file in the output folder.
    
    OutputSoftwarePerformance : bool, default=False
        If true, the software performance output group will be created.
    
    OutputStateInformation : bool, default=False
        If true, the integrator state output group will be created.  This can be used to help understand how efficiently the integrator is coping with the simulation.
    
    OutputExternalControllerExchangeObject : bool, default=False
        If true, this will output all of the values contained in the external controller interface before and after each external controller call.  This is intended to assist debugging external controllers.
    
    OutputExternalControllerLegacySwapArray : bool, default=False
        If true, the contents of the swap array passed to a legacy controller will be logged.  This is used only when trying to debug legacy controllers, and will not produce useful results if there is more than one legacy controller being run.
    
    SelectedComponentOutputGroups : List[SelectedComponentOutputGroup], Not supported yet
        A list of references to the OutputGroup of specific components to output.  This allows the outputs of individual components to be switched off, or chosen from an available list of output regimes.  If a component is not mentioned, it will produce outputs according to its default output group, if there is one available.
    
    Notes
    -----
    
    """
    TimeStepForOutputs: float = Field(alias="TimeStepForOutputs", default=None)
    LengthOfOutputBuffer: float = Field(alias="LengthOfOutputBuffer", default=None)
    OutputSummaryInformation: bool = Field(alias="OutputSummaryInformation", default=None)
    OutputExternalControllers: bool = Field(alias="OutputExternalControllers", default=None)
    OutputBuoyancyInformation: bool = Field(alias="OutputBuoyancyInformation", default=None)
    OutputFiniteElementMatrices: bool = Field(alias="OutputFiniteElementMatrices", default=None)
    OutputSignalProperties: bool = Field(alias="OutputSignalProperties", default=None)
    OutputWakePropagation: bool = Field(alias="OutputWakePropagation", default=None)
    OutputSoftwarePerformance: bool = Field(alias="OutputSoftwarePerformance", default=None)
    OutputStateInformation: bool = Field(alias="OutputStateInformation", default=None)
    OutputExternalControllerExchangeObject: bool = Field(alias="OutputExternalControllerExchangeObject", default=None)
    OutputExternalControllerLegacySwapArray: bool = Field(alias="OutputExternalControllerLegacySwapArray", default=None)
    SelectedComponentOutputGroups: List[SelectedComponentOutputGroup] = Field(alias="SelectedComponentOutputGroups", default=list()) # Not supported yet

    _relative_schema_path = 'TimeDomainSimulation/TimeDomainOutputs/TimeDomainOutputs.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set(['SelectedComponentOutputGroups',]),
        None).merge(Outputs._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


TimeDomainOutputs.update_forward_refs()

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
from dnv_bladed_models.blade_stability_analysis_calculation import BladeStabilityAnalysisCalculation
from dnv_bladed_models.blade_stability_analysis_idling import BladeStabilityAnalysisIdling
from dnv_bladed_models.blade_stability_analysis_mode_of_operation import BladeStabilityAnalysisModeOfOperation
from dnv_bladed_models.blade_stability_analysis_mode_of_operation_insert import BladeStabilityAnalysisModeOfOperationInsert
from dnv_bladed_models.blade_stability_analysis_parked import BladeStabilityAnalysisParked

from .schema_helper import SchemaHelper
from .models_impl import *

TBladeStabilityAnalysisModeOfOperationOptions = TypeVar('TBladeStabilityAnalysisModeOfOperationOptions', BladeStabilityAnalysisIdling, BladeStabilityAnalysisModeOfOperationInsert, BladeStabilityAnalysisParked, BladeStabilityAnalysisModeOfOperation, )

class BladeStabilityAnalysis(BladeStabilityAnalysisCalculation):
    r"""
    Defines a calculation which produces the damping and frequency of all the coupled rotor or blade modes plotted against wind speed for a single rotor.  This calculation allows analysis over a wider range of inflow conditions than the Cambell diagram calculation, rather than being constrained to normal operating conditions.
    
    Not supported yet.
    
    Attributes
    ----------
    SteadyCalculationType : Literal['BladeStabilityAnalysis'], default='BladeStabilityAnalysis', Not supported yet
        Defines the specific type of SteadyCalculation model in use.  For a `BladeStabilityAnalysis` object, this must always be set to a value of `BladeStabilityAnalysis`.
    
    ModeOfOperation : Union[BladeStabilityAnalysisIdling, BladeStabilityAnalysisModeOfOperationInsert, BladeStabilityAnalysisParked], Not supported yet
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    SteadyCalculationType: Literal['BladeStabilityAnalysis'] = Field(alias="SteadyCalculationType", default='BladeStabilityAnalysis', allow_mutation=False, const=True) # Not supported yet # type: ignore
    ModeOfOperation: Union[BladeStabilityAnalysisIdling, BladeStabilityAnalysisModeOfOperationInsert, BladeStabilityAnalysisParked] = Field(alias="ModeOfOperation", default=None, discriminator='BladeStabilityAnalysisModeOfOperationType') # Not supported yet

    _relative_schema_path = 'SteadyCalculation/BladeStabilityAnalysis.json'
    _type_info = TypeInfo(
        set([('ModeOfOperation', 'BladeStabilityAnalysisModeOfOperationType'),]),
        set([]),
        set([]),
        'SteadyCalculationType').merge(BladeStabilityAnalysisCalculation._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    @property
    def ModeOfOperation_as_BladeStabilityAnalysisIdling(self) -> BladeStabilityAnalysisIdling:
        """
        Retrieves the value of ModeOfOperation guaranteeing it is a BladeStabilityAnalysisIdling; if it is not, an error is raised.

        Useful when using type-checking development tools, as it provides a concise way to retrieve a value and assign a variable with the correct type.

        Returns
        -------
        BladeStabilityAnalysisIdling
            A model object, guaranteed to be a BladeStabilityAnalysisIdling.

        Raises
        ------
        TypeError
            If the value is not a BladeStabilityAnalysisIdling.
        """
        return self.ModeOfOperation_as(BladeStabilityAnalysisIdling)


    @property
    def ModeOfOperation_as_BladeStabilityAnalysisParked(self) -> BladeStabilityAnalysisParked:
        """
        Retrieves the value of ModeOfOperation guaranteeing it is a BladeStabilityAnalysisParked; if it is not, an error is raised.

        Useful when using type-checking development tools, as it provides a concise way to retrieve a value and assign a variable with the correct type.

        Returns
        -------
        BladeStabilityAnalysisParked
            A model object, guaranteed to be a BladeStabilityAnalysisParked.

        Raises
        ------
        TypeError
            If the value is not a BladeStabilityAnalysisParked.
        """
        return self.ModeOfOperation_as(BladeStabilityAnalysisParked)


    @property
    def ModeOfOperation_as_inline(self) -> Union[BladeStabilityAnalysisIdling, BladeStabilityAnalysisParked]:
        """
        Retrieves the value of ModeOfOperation as a model object; if the value is specified with a '$insert', an error is raised.

        Returns
        -------
        Union[BladeStabilityAnalysisIdling, BladeStabilityAnalysisParked]
            A model object at the specified index, guaranteed to not be a '$insert'.

        Raises
        ------
        TypeError
            If the value is not one of the concrete types of BladeStabilityAnalysisModeOfOperation; i.e. it is specified with a '$insert'.
        """
        if isinstance(self.ModeOfOperation, BladeStabilityAnalysisModeOfOperationInsert) or self.ModeOfOperation.is_insert:
            raise TypeError(f"Expected ModeOfOperation value to be an in-line object, but it is currently in the '$insert' state.")
        return self.ModeOfOperation


    def ModeOfOperation_as(self, cls: Type[TBladeStabilityAnalysisModeOfOperationOptions])-> TBladeStabilityAnalysisModeOfOperationOptions:
        """
        Retrieves the value of ModeOfOperation, ensuring it is of the specified type.
        The specified type must be one of the valid concrete types of BladeStabilityAnalysisModeOfOperation, or the '$insert' type
        (in the case the model is defined to be inserted from an external resource).

        Useful when using type-checking development tools, as it provides a concise way to access a value with the correct type.

        Parameters
        ----------
        cls: Type[Union[BladeStabilityAnalysisIdling, BladeStabilityAnalysisModeOfOperationInsert, BladeStabilityAnalysisParked]]
            One of the valid concrete types of BladeStabilityAnalysisModeOfOperation, or the '$insert' type
            (in the case the model is defined to be inserted from an external resource).

        Returns
        -------
        TBladeStabilityAnalysisModeOfOperationOptions
            A model object of the specified type.

        Raises
        ------
        TypeError
            If the value is not of the specified type.

        Examples
        --------
        Get a reference to the value when it is one of the types of BladeStabilityAnalysisModeOfOperation:
        >>> val_obj = model_obj.ModeOfOperation_as(models.BladeStabilityAnalysisIdling)
        >>> val_obj = model_obj.ModeOfOperation_as(models.BladeStabilityAnalysisParked)

        Get a reference to the value, when it was specified with a '$insert' and read in from a file:
        >>> insert_obj = model_obj.ModeOfOperation_as(models.BladeStabilityAnalysisModeOfOperationInsert)
        """
        if not isinstance(self.ModeOfOperation, cls):
            raise TypeError(f"Expected ModeOfOperation of type '{cls.__name__}' but was type '{type(self.ModeOfOperation).__name__}'")
        return self.ModeOfOperation


    def _entity(self) -> bool:
        return True


BladeStabilityAnalysis.update_forward_refs()

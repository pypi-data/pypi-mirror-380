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
from dnv_bladed_models.aerodynamic_information_calculation import AerodynamicInformationCalculation
from dnv_bladed_models.blade_stability_analysis import BladeStabilityAnalysis
from dnv_bladed_models.bladed_model import BladedModel
from dnv_bladed_models.campbell_diagram import CampbellDiagram
from dnv_bladed_models.constants import Constants
from dnv_bladed_models.modal_analysis_calculation import ModalAnalysisCalculation
from dnv_bladed_models.model_linearisation import ModelLinearisation
from dnv_bladed_models.performance_coefficients_calculation import PerformanceCoefficientsCalculation
from dnv_bladed_models.settings import Settings
from dnv_bladed_models.steady_calculation import SteadyCalculation
from dnv_bladed_models.steady_calculation_insert import SteadyCalculationInsert
from dnv_bladed_models.steady_operational_loads_calculation import SteadyOperationalLoadsCalculation
from dnv_bladed_models.steady_parked_loads_calculation import SteadyParkedLoadsCalculation
from dnv_bladed_models.steady_power_curve_calculation import SteadyPowerCurveCalculation
from dnv_bladed_models.time_domain_simulation import TimeDomainSimulation
from dnv_bladed_models.turbine import Turbine

from .schema_helper import SchemaHelper
from .models_impl import *

TSteadyCalculationOptions = TypeVar('TSteadyCalculationOptions', AerodynamicInformationCalculation, BladeStabilityAnalysis, CampbellDiagram, SteadyCalculationInsert, ModalAnalysisCalculation, ModelLinearisation, PerformanceCoefficientsCalculation, SteadyOperationalLoadsCalculation, SteadyParkedLoadsCalculation, SteadyPowerCurveCalculation, SteadyCalculation, )

class BladedAnalysis(BladedModel):
    r"""
    The definition of a single Bladed analysis.
    
    Attributes
    ----------
    TimeDomainSimulation : TimeDomainSimulation
    
    SteadyCalculation : Union[AerodynamicInformationCalculation, BladeStabilityAnalysis, CampbellDiagram, SteadyCalculationInsert, ModalAnalysisCalculation, ModelLinearisation, PerformanceCoefficientsCalculation, SteadyOperationalLoadsCalculation, SteadyParkedLoadsCalculation, SteadyPowerCurveCalculation]
    
    Settings : Settings
    
    Constants : Constants
    
    Turbine : Turbine
    
    Notes
    -----
    
    """
    TimeDomainSimulation: TimeDomainSimulation = Field(alias="TimeDomainSimulation", default=None)
    SteadyCalculation: Union[AerodynamicInformationCalculation, BladeStabilityAnalysis, CampbellDiagram, SteadyCalculationInsert, ModalAnalysisCalculation, ModelLinearisation, PerformanceCoefficientsCalculation, SteadyOperationalLoadsCalculation, SteadyParkedLoadsCalculation, SteadyPowerCurveCalculation] = Field(alias="SteadyCalculation", default=None, discriminator='SteadyCalculationType')
    Settings: Settings = Field(alias="Settings", default=None)
    Constants: Constants = Field(alias="Constants", default=None)
    Turbine: Turbine = Field(alias="Turbine", default=None)

    _relative_schema_path = 'BladedAnalysis.json'
    _type_info = TypeInfo(
        set([('SteadyCalculation', 'SteadyCalculationType'),]),
        set([]),
        set([]),
        None).merge(BladedModel._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    @property
    def SteadyCalculation_as_AerodynamicInformationCalculation(self) -> AerodynamicInformationCalculation:
        """
        Retrieves the value of SteadyCalculation guaranteeing it is a AerodynamicInformationCalculation; if it is not, an error is raised.

        Useful when using type-checking development tools, as it provides a concise way to retrieve a value and assign a variable with the correct type.

        Returns
        -------
        AerodynamicInformationCalculation
            A model object, guaranteed to be a AerodynamicInformationCalculation.

        Raises
        ------
        TypeError
            If the value is not a AerodynamicInformationCalculation.
        """
        return self.SteadyCalculation_as(AerodynamicInformationCalculation)


    @property
    def SteadyCalculation_as_BladeStabilityAnalysis(self) -> BladeStabilityAnalysis:
        """
        Retrieves the value of SteadyCalculation guaranteeing it is a BladeStabilityAnalysis; if it is not, an error is raised.

        Useful when using type-checking development tools, as it provides a concise way to retrieve a value and assign a variable with the correct type.

        Returns
        -------
        BladeStabilityAnalysis
            A model object, guaranteed to be a BladeStabilityAnalysis.

        Raises
        ------
        TypeError
            If the value is not a BladeStabilityAnalysis.
        """
        return self.SteadyCalculation_as(BladeStabilityAnalysis)


    @property
    def SteadyCalculation_as_CampbellDiagram(self) -> CampbellDiagram:
        """
        Retrieves the value of SteadyCalculation guaranteeing it is a CampbellDiagram; if it is not, an error is raised.

        Useful when using type-checking development tools, as it provides a concise way to retrieve a value and assign a variable with the correct type.

        Returns
        -------
        CampbellDiagram
            A model object, guaranteed to be a CampbellDiagram.

        Raises
        ------
        TypeError
            If the value is not a CampbellDiagram.
        """
        return self.SteadyCalculation_as(CampbellDiagram)


    @property
    def SteadyCalculation_as_ModalAnalysisCalculation(self) -> ModalAnalysisCalculation:
        """
        Retrieves the value of SteadyCalculation guaranteeing it is a ModalAnalysisCalculation; if it is not, an error is raised.

        Useful when using type-checking development tools, as it provides a concise way to retrieve a value and assign a variable with the correct type.

        Returns
        -------
        ModalAnalysisCalculation
            A model object, guaranteed to be a ModalAnalysisCalculation.

        Raises
        ------
        TypeError
            If the value is not a ModalAnalysisCalculation.
        """
        return self.SteadyCalculation_as(ModalAnalysisCalculation)


    @property
    def SteadyCalculation_as_ModelLinearisation(self) -> ModelLinearisation:
        """
        Retrieves the value of SteadyCalculation guaranteeing it is a ModelLinearisation; if it is not, an error is raised.

        Useful when using type-checking development tools, as it provides a concise way to retrieve a value and assign a variable with the correct type.

        Returns
        -------
        ModelLinearisation
            A model object, guaranteed to be a ModelLinearisation.

        Raises
        ------
        TypeError
            If the value is not a ModelLinearisation.
        """
        return self.SteadyCalculation_as(ModelLinearisation)


    @property
    def SteadyCalculation_as_PerformanceCoefficientsCalculation(self) -> PerformanceCoefficientsCalculation:
        """
        Retrieves the value of SteadyCalculation guaranteeing it is a PerformanceCoefficientsCalculation; if it is not, an error is raised.

        Useful when using type-checking development tools, as it provides a concise way to retrieve a value and assign a variable with the correct type.

        Returns
        -------
        PerformanceCoefficientsCalculation
            A model object, guaranteed to be a PerformanceCoefficientsCalculation.

        Raises
        ------
        TypeError
            If the value is not a PerformanceCoefficientsCalculation.
        """
        return self.SteadyCalculation_as(PerformanceCoefficientsCalculation)


    @property
    def SteadyCalculation_as_SteadyOperationalLoadsCalculation(self) -> SteadyOperationalLoadsCalculation:
        """
        Retrieves the value of SteadyCalculation guaranteeing it is a SteadyOperationalLoadsCalculation; if it is not, an error is raised.

        Useful when using type-checking development tools, as it provides a concise way to retrieve a value and assign a variable with the correct type.

        Returns
        -------
        SteadyOperationalLoadsCalculation
            A model object, guaranteed to be a SteadyOperationalLoadsCalculation.

        Raises
        ------
        TypeError
            If the value is not a SteadyOperationalLoadsCalculation.
        """
        return self.SteadyCalculation_as(SteadyOperationalLoadsCalculation)


    @property
    def SteadyCalculation_as_SteadyParkedLoadsCalculation(self) -> SteadyParkedLoadsCalculation:
        """
        Retrieves the value of SteadyCalculation guaranteeing it is a SteadyParkedLoadsCalculation; if it is not, an error is raised.

        Useful when using type-checking development tools, as it provides a concise way to retrieve a value and assign a variable with the correct type.

        Returns
        -------
        SteadyParkedLoadsCalculation
            A model object, guaranteed to be a SteadyParkedLoadsCalculation.

        Raises
        ------
        TypeError
            If the value is not a SteadyParkedLoadsCalculation.
        """
        return self.SteadyCalculation_as(SteadyParkedLoadsCalculation)


    @property
    def SteadyCalculation_as_SteadyPowerCurveCalculation(self) -> SteadyPowerCurveCalculation:
        """
        Retrieves the value of SteadyCalculation guaranteeing it is a SteadyPowerCurveCalculation; if it is not, an error is raised.

        Useful when using type-checking development tools, as it provides a concise way to retrieve a value and assign a variable with the correct type.

        Returns
        -------
        SteadyPowerCurveCalculation
            A model object, guaranteed to be a SteadyPowerCurveCalculation.

        Raises
        ------
        TypeError
            If the value is not a SteadyPowerCurveCalculation.
        """
        return self.SteadyCalculation_as(SteadyPowerCurveCalculation)


    @property
    def SteadyCalculation_as_inline(self) -> Union[AerodynamicInformationCalculation, BladeStabilityAnalysis, CampbellDiagram, ModalAnalysisCalculation, ModelLinearisation, PerformanceCoefficientsCalculation, SteadyOperationalLoadsCalculation, SteadyParkedLoadsCalculation, SteadyPowerCurveCalculation]:
        """
        Retrieves the value of SteadyCalculation as a model object; if the value is specified with a '$insert', an error is raised.

        Returns
        -------
        Union[AerodynamicInformationCalculation, BladeStabilityAnalysis, CampbellDiagram, ModalAnalysisCalculation, ModelLinearisation, PerformanceCoefficientsCalculation, SteadyOperationalLoadsCalculation, SteadyParkedLoadsCalculation, SteadyPowerCurveCalculation]
            A model object at the specified index, guaranteed to not be a '$insert'.

        Raises
        ------
        TypeError
            If the value is not one of the concrete types of SteadyCalculation; i.e. it is specified with a '$insert'.
        """
        if isinstance(self.SteadyCalculation, SteadyCalculationInsert) or self.SteadyCalculation.is_insert:
            raise TypeError(f"Expected SteadyCalculation value to be an in-line object, but it is currently in the '$insert' state.")
        return self.SteadyCalculation


    def SteadyCalculation_as(self, cls: Type[TSteadyCalculationOptions])-> TSteadyCalculationOptions:
        """
        Retrieves the value of SteadyCalculation, ensuring it is of the specified type.
        The specified type must be one of the valid concrete types of SteadyCalculation, or the '$insert' type
        (in the case the model is defined to be inserted from an external resource).

        Useful when using type-checking development tools, as it provides a concise way to access a value with the correct type.

        Parameters
        ----------
        cls: Type[Union[AerodynamicInformationCalculation, BladeStabilityAnalysis, CampbellDiagram, SteadyCalculationInsert, ModalAnalysisCalculation, ModelLinearisation, PerformanceCoefficientsCalculation, SteadyOperationalLoadsCalculation, SteadyParkedLoadsCalculation, SteadyPowerCurveCalculation]]
            One of the valid concrete types of SteadyCalculation, or the '$insert' type
            (in the case the model is defined to be inserted from an external resource).

        Returns
        -------
        TSteadyCalculationOptions
            A model object of the specified type.

        Raises
        ------
        TypeError
            If the value is not of the specified type.

        Examples
        --------
        Get a reference to the value when it is one of the types of SteadyCalculation:
        >>> val_obj = model_obj.SteadyCalculation_as(models.AerodynamicInformationCalculation)
        >>> val_obj = model_obj.SteadyCalculation_as(models.BladeStabilityAnalysis)
        >>> val_obj = model_obj.SteadyCalculation_as(models.CampbellDiagram)
        >>> val_obj = model_obj.SteadyCalculation_as(models.ModalAnalysisCalculation)
        >>> val_obj = model_obj.SteadyCalculation_as(models.ModelLinearisation)
        >>> val_obj = model_obj.SteadyCalculation_as(models.PerformanceCoefficientsCalculation)
        >>> val_obj = model_obj.SteadyCalculation_as(models.SteadyOperationalLoadsCalculation)
        >>> val_obj = model_obj.SteadyCalculation_as(models.SteadyParkedLoadsCalculation)
        >>> val_obj = model_obj.SteadyCalculation_as(models.SteadyPowerCurveCalculation)

        Get a reference to the value, when it was specified with a '$insert' and read in from a file:
        >>> insert_obj = model_obj.SteadyCalculation_as(models.SteadyCalculationInsert)
        """
        if not isinstance(self.SteadyCalculation, cls):
            raise TypeError(f"Expected SteadyCalculation of type '{cls.__name__}' but was type '{type(self.SteadyCalculation).__name__}'")
        return self.SteadyCalculation


    def _entity(self) -> bool:
        return True


BladedAnalysis.update_forward_refs()

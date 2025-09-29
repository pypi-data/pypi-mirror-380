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
from dnv_bladed_models.first_order_transducer_response import FirstOrderTransducerResponse
from dnv_bladed_models.instantaneous_transducer_response import InstantaneousTransducerResponse
from dnv_bladed_models.passive_transducer_response import PassiveTransducerResponse
from dnv_bladed_models.position_proportional_integral_deriviative import PositionProportionalIntegralDeriviative
from dnv_bladed_models.rate_proportional_integral_deriviative import RateProportionalIntegralDeriviative
from dnv_bladed_models.second_order_transducer_response import SecondOrderTransducerResponse
from dnv_bladed_models.transducer_behaviour import TransducerBehaviour
from dnv_bladed_models.transducer_behaviour_insert import TransducerBehaviourInsert
from dnv_bladed_models.use_setpoint_trajectory_planning import UseSetpointTrajectoryPlanning
class SignalProperties_SignalQualityEnum(str, Enum):
    RAW = "Raw"
    TRANSDUCER = "Transducer"
    MEASURED = "Measured"
class SignalProperties_SignalNoiseEnum(str, Enum):
    NONE = "None"
    UNIFORM = "Uniform"
    GAUSSIAN = "Gaussian"

from .schema_helper import SchemaHelper
from .models_impl import *

TTransducerBehaviourOptions = TypeVar('TTransducerBehaviourOptions', FirstOrderTransducerResponse, TransducerBehaviourInsert, InstantaneousTransducerResponse, PassiveTransducerResponse, PositionProportionalIntegralDeriviative, RateProportionalIntegralDeriviative, SecondOrderTransducerResponse, UseSetpointTrajectoryPlanning, TransducerBehaviour, )

class SignalProperties(BladedModel, ABC):
    r"""
    
    
    Not supported yet.
    
    Attributes
    ----------
    SignalQuality : SignalProperties_SignalQualityEnum, default='Raw', Not supported yet
        The representation of the signal quality - whether it has transducer lag and signal noise.
    
    SignalNoise : SignalProperties_SignalNoiseEnum, default='None', Not supported yet
        The type of noise on the measured signal.
    
    NoiseMagnitude : float, default=0, Not supported yet
        The magnitude of the signal noise.
    
    SamplingPeriod : float, default=0, Not supported yet
        The time step at which the input (continuous) signal is discretised at.
    
    DiscretisationStep : float, default=0, Not supported yet
        The intervals at which values can be represented.
    
    Transducer : Union[FirstOrderTransducerResponse, TransducerBehaviourInsert, InstantaneousTransducerResponse, PassiveTransducerResponse, PositionProportionalIntegralDeriviative, RateProportionalIntegralDeriviative, SecondOrderTransducerResponse, UseSetpointTrajectoryPlanning], Not supported yet
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    SignalQuality: SignalProperties_SignalQualityEnum = Field(alias="SignalQuality", default=None) # Not supported yet
    SignalNoise: SignalProperties_SignalNoiseEnum = Field(alias="SignalNoise", default=None) # Not supported yet
    NoiseMagnitude: float = Field(alias="NoiseMagnitude", default=None) # Not supported yet
    SamplingPeriod: float = Field(alias="SamplingPeriod", default=None) # Not supported yet
    DiscretisationStep: float = Field(alias="DiscretisationStep", default=None) # Not supported yet
    Transducer: Union[FirstOrderTransducerResponse, TransducerBehaviourInsert, InstantaneousTransducerResponse, PassiveTransducerResponse, PositionProportionalIntegralDeriviative, RateProportionalIntegralDeriviative, SecondOrderTransducerResponse, UseSetpointTrajectoryPlanning] = Field(alias="Transducer", default=None, discriminator='TransducerBehaviourType') # Not supported yet

    _type_info = TypeInfo(
        set([('Transducer', 'TransducerBehaviourType'),]),
        set([]),
        set([]),
        None).merge(BladedModel._type_info)


    @property
    def Transducer_as_FirstOrderTransducerResponse(self) -> FirstOrderTransducerResponse:
        """
        Retrieves the value of Transducer guaranteeing it is a FirstOrderTransducerResponse; if it is not, an error is raised.

        Useful when using type-checking development tools, as it provides a concise way to retrieve a value and assign a variable with the correct type.

        Returns
        -------
        FirstOrderTransducerResponse
            A model object, guaranteed to be a FirstOrderTransducerResponse.

        Raises
        ------
        TypeError
            If the value is not a FirstOrderTransducerResponse.
        """
        return self.Transducer_as(FirstOrderTransducerResponse)


    @property
    def Transducer_as_InstantaneousTransducerResponse(self) -> InstantaneousTransducerResponse:
        """
        Retrieves the value of Transducer guaranteeing it is a InstantaneousTransducerResponse; if it is not, an error is raised.

        Useful when using type-checking development tools, as it provides a concise way to retrieve a value and assign a variable with the correct type.

        Returns
        -------
        InstantaneousTransducerResponse
            A model object, guaranteed to be a InstantaneousTransducerResponse.

        Raises
        ------
        TypeError
            If the value is not a InstantaneousTransducerResponse.
        """
        return self.Transducer_as(InstantaneousTransducerResponse)


    @property
    def Transducer_as_PassiveTransducerResponse(self) -> PassiveTransducerResponse:
        """
        Retrieves the value of Transducer guaranteeing it is a PassiveTransducerResponse; if it is not, an error is raised.

        Useful when using type-checking development tools, as it provides a concise way to retrieve a value and assign a variable with the correct type.

        Returns
        -------
        PassiveTransducerResponse
            A model object, guaranteed to be a PassiveTransducerResponse.

        Raises
        ------
        TypeError
            If the value is not a PassiveTransducerResponse.
        """
        return self.Transducer_as(PassiveTransducerResponse)


    @property
    def Transducer_as_PositionProportionalIntegralDeriviative(self) -> PositionProportionalIntegralDeriviative:
        """
        Retrieves the value of Transducer guaranteeing it is a PositionProportionalIntegralDeriviative; if it is not, an error is raised.

        Useful when using type-checking development tools, as it provides a concise way to retrieve a value and assign a variable with the correct type.

        Returns
        -------
        PositionProportionalIntegralDeriviative
            A model object, guaranteed to be a PositionProportionalIntegralDeriviative.

        Raises
        ------
        TypeError
            If the value is not a PositionProportionalIntegralDeriviative.
        """
        return self.Transducer_as(PositionProportionalIntegralDeriviative)


    @property
    def Transducer_as_RateProportionalIntegralDeriviative(self) -> RateProportionalIntegralDeriviative:
        """
        Retrieves the value of Transducer guaranteeing it is a RateProportionalIntegralDeriviative; if it is not, an error is raised.

        Useful when using type-checking development tools, as it provides a concise way to retrieve a value and assign a variable with the correct type.

        Returns
        -------
        RateProportionalIntegralDeriviative
            A model object, guaranteed to be a RateProportionalIntegralDeriviative.

        Raises
        ------
        TypeError
            If the value is not a RateProportionalIntegralDeriviative.
        """
        return self.Transducer_as(RateProportionalIntegralDeriviative)


    @property
    def Transducer_as_SecondOrderTransducerResponse(self) -> SecondOrderTransducerResponse:
        """
        Retrieves the value of Transducer guaranteeing it is a SecondOrderTransducerResponse; if it is not, an error is raised.

        Useful when using type-checking development tools, as it provides a concise way to retrieve a value and assign a variable with the correct type.

        Returns
        -------
        SecondOrderTransducerResponse
            A model object, guaranteed to be a SecondOrderTransducerResponse.

        Raises
        ------
        TypeError
            If the value is not a SecondOrderTransducerResponse.
        """
        return self.Transducer_as(SecondOrderTransducerResponse)


    @property
    def Transducer_as_UseSetpointTrajectoryPlanning(self) -> UseSetpointTrajectoryPlanning:
        """
        Retrieves the value of Transducer guaranteeing it is a UseSetpointTrajectoryPlanning; if it is not, an error is raised.

        Useful when using type-checking development tools, as it provides a concise way to retrieve a value and assign a variable with the correct type.

        Returns
        -------
        UseSetpointTrajectoryPlanning
            A model object, guaranteed to be a UseSetpointTrajectoryPlanning.

        Raises
        ------
        TypeError
            If the value is not a UseSetpointTrajectoryPlanning.
        """
        return self.Transducer_as(UseSetpointTrajectoryPlanning)


    @property
    def Transducer_as_inline(self) -> Union[FirstOrderTransducerResponse, InstantaneousTransducerResponse, PassiveTransducerResponse, PositionProportionalIntegralDeriviative, RateProportionalIntegralDeriviative, SecondOrderTransducerResponse, UseSetpointTrajectoryPlanning]:
        """
        Retrieves the value of Transducer as a model object; if the value is specified with a '$insert', an error is raised.

        Returns
        -------
        Union[FirstOrderTransducerResponse, InstantaneousTransducerResponse, PassiveTransducerResponse, PositionProportionalIntegralDeriviative, RateProportionalIntegralDeriviative, SecondOrderTransducerResponse, UseSetpointTrajectoryPlanning]
            A model object at the specified index, guaranteed to not be a '$insert'.

        Raises
        ------
        TypeError
            If the value is not one of the concrete types of TransducerBehaviour; i.e. it is specified with a '$insert'.
        """
        if isinstance(self.Transducer, TransducerBehaviourInsert) or self.Transducer.is_insert:
            raise TypeError(f"Expected Transducer value to be an in-line object, but it is currently in the '$insert' state.")
        return self.Transducer


    def Transducer_as(self, cls: Type[TTransducerBehaviourOptions])-> TTransducerBehaviourOptions:
        """
        Retrieves the value of Transducer, ensuring it is of the specified type.
        The specified type must be one of the valid concrete types of TransducerBehaviour, or the '$insert' type
        (in the case the model is defined to be inserted from an external resource).

        Useful when using type-checking development tools, as it provides a concise way to access a value with the correct type.

        Parameters
        ----------
        cls: Type[Union[FirstOrderTransducerResponse, TransducerBehaviourInsert, InstantaneousTransducerResponse, PassiveTransducerResponse, PositionProportionalIntegralDeriviative, RateProportionalIntegralDeriviative, SecondOrderTransducerResponse, UseSetpointTrajectoryPlanning]]
            One of the valid concrete types of TransducerBehaviour, or the '$insert' type
            (in the case the model is defined to be inserted from an external resource).

        Returns
        -------
        TTransducerBehaviourOptions
            A model object of the specified type.

        Raises
        ------
        TypeError
            If the value is not of the specified type.

        Examples
        --------
        Get a reference to the value when it is one of the types of TransducerBehaviour:
        >>> val_obj = model_obj.Transducer_as(models.FirstOrderTransducerResponse)
        >>> val_obj = model_obj.Transducer_as(models.InstantaneousTransducerResponse)
        >>> val_obj = model_obj.Transducer_as(models.PassiveTransducerResponse)
        >>> val_obj = model_obj.Transducer_as(models.PositionProportionalIntegralDeriviative)
        >>> val_obj = model_obj.Transducer_as(models.RateProportionalIntegralDeriviative)
        >>> val_obj = model_obj.Transducer_as(models.SecondOrderTransducerResponse)
        >>> val_obj = model_obj.Transducer_as(models.UseSetpointTrajectoryPlanning)

        Get a reference to the value, when it was specified with a '$insert' and read in from a file:
        >>> insert_obj = model_obj.Transducer_as(models.TransducerBehaviourInsert)
        """
        if not isinstance(self.Transducer, cls):
            raise TypeError(f"Expected Transducer of type '{cls.__name__}' but was type '{type(self.Transducer).__name__}'")
        return self.Transducer


SignalProperties.update_forward_refs()

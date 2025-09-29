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
from dnv_bladed_models.component import Component
from dnv_bladed_models.friction import Friction
from dnv_bladed_models.idealised_pitch_actuator import IdealisedPitchActuator
from dnv_bladed_models.linear_pitch_actuator import LinearPitchActuator
from dnv_bladed_models.pitch_actuator import PitchActuator
from dnv_bladed_models.pitch_actuator_insert import PitchActuatorInsert
from dnv_bladed_models.pitch_controller import PitchController
from dnv_bladed_models.pitch_end_stops import PitchEndStops
from dnv_bladed_models.pitch_limit_switches import PitchLimitSwitches
from dnv_bladed_models.pitch_system_connectable_nodes import PitchSystemConnectableNodes
from dnv_bladed_models.pitch_system_output_group_library import PitchSystemOutputGroupLibrary
from dnv_bladed_models.pitch_system_rotary_drive import PitchSystemRotaryDrive

from .schema_helper import SchemaHelper
from .models_impl import *

TPitchActuatorOptions = TypeVar('TPitchActuatorOptions', IdealisedPitchActuator, PitchActuatorInsert, LinearPitchActuator, PitchSystemRotaryDrive, PitchActuator, )

class PitchSystem(Component):
    r"""
    A pitch system, including bearing, actuation, and independent control system.
    
    Attributes
    ----------
    ComponentType : Literal['PitchSystem'], default='PitchSystem'
        Defines the specific type of Component model in use.  For a `PitchSystem` object, this must always be set to a value of `PitchSystem`.
    
    PitchController : PitchController
    
    LimitSwitches : PitchLimitSwitches
    
    EndStops : PitchEndStops
    
    Bearing : Friction
    
    Actuator : Union[IdealisedPitchActuator, PitchActuatorInsert, LinearPitchActuator, PitchSystemRotaryDrive]
    
    OutputGroups : PitchSystemOutputGroupLibrary, Not supported yet
    
    ConnectableNodes : PitchSystemConnectableNodes, Not supported yet
    
    Notes
    -----
    
    """
    ComponentType: Literal['PitchSystem'] = Field(alias="ComponentType", default='PitchSystem', allow_mutation=False, const=True) # type: ignore
    PitchController: PitchController = Field(alias="PitchController", default=None)
    LimitSwitches: PitchLimitSwitches = Field(alias="LimitSwitches", default=None)
    EndStops: PitchEndStops = Field(alias="EndStops", default=None)
    Bearing: Friction = Field(alias="Bearing", default=None)
    Actuator: Union[IdealisedPitchActuator, PitchActuatorInsert, LinearPitchActuator, PitchSystemRotaryDrive] = Field(alias="Actuator", default=None, discriminator='ActuatorDriveType')
    OutputGroups: PitchSystemOutputGroupLibrary = Field(alias="OutputGroups", default=PitchSystemOutputGroupLibrary()) # Not supported yet
    ConnectableNodes: PitchSystemConnectableNodes = Field(alias="ConnectableNodes", default=PitchSystemConnectableNodes()) # Not supported yet

    _relative_schema_path = 'Components/PitchSystem/PitchSystem.json'
    _type_info = TypeInfo(
        set([('Actuator', 'ActuatorDriveType'),]),
        set([]),
        set(['OutputGroups','ConnectableNodes',]),
        'ComponentType').merge(Component._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    @property
    def Actuator_as_IdealisedPitchActuator(self) -> IdealisedPitchActuator:
        """
        Retrieves the value of Actuator guaranteeing it is a IdealisedPitchActuator; if it is not, an error is raised.

        Useful when using type-checking development tools, as it provides a concise way to retrieve a value and assign a variable with the correct type.

        Returns
        -------
        IdealisedPitchActuator
            A model object, guaranteed to be a IdealisedPitchActuator.

        Raises
        ------
        TypeError
            If the value is not a IdealisedPitchActuator.
        """
        return self.Actuator_as(IdealisedPitchActuator)


    @property
    def Actuator_as_LinearPitchActuator(self) -> LinearPitchActuator:
        """
        Retrieves the value of Actuator guaranteeing it is a LinearPitchActuator; if it is not, an error is raised.

        Useful when using type-checking development tools, as it provides a concise way to retrieve a value and assign a variable with the correct type.

        Returns
        -------
        LinearPitchActuator
            A model object, guaranteed to be a LinearPitchActuator.

        Raises
        ------
        TypeError
            If the value is not a LinearPitchActuator.
        """
        return self.Actuator_as(LinearPitchActuator)


    @property
    def Actuator_as_PitchSystemRotaryDrive(self) -> PitchSystemRotaryDrive:
        """
        Retrieves the value of Actuator guaranteeing it is a PitchSystemRotaryDrive; if it is not, an error is raised.

        Useful when using type-checking development tools, as it provides a concise way to retrieve a value and assign a variable with the correct type.

        Returns
        -------
        PitchSystemRotaryDrive
            A model object, guaranteed to be a PitchSystemRotaryDrive.

        Raises
        ------
        TypeError
            If the value is not a PitchSystemRotaryDrive.
        """
        return self.Actuator_as(PitchSystemRotaryDrive)


    @property
    def Actuator_as_inline(self) -> Union[IdealisedPitchActuator, LinearPitchActuator, PitchSystemRotaryDrive]:
        """
        Retrieves the value of Actuator as a model object; if the value is specified with a '$insert', an error is raised.

        Returns
        -------
        Union[IdealisedPitchActuator, LinearPitchActuator, PitchSystemRotaryDrive]
            A model object at the specified index, guaranteed to not be a '$insert'.

        Raises
        ------
        TypeError
            If the value is not one of the concrete types of PitchActuator; i.e. it is specified with a '$insert'.
        """
        if isinstance(self.Actuator, PitchActuatorInsert) or self.Actuator.is_insert:
            raise TypeError(f"Expected Actuator value to be an in-line object, but it is currently in the '$insert' state.")
        return self.Actuator


    def Actuator_as(self, cls: Type[TPitchActuatorOptions])-> TPitchActuatorOptions:
        """
        Retrieves the value of Actuator, ensuring it is of the specified type.
        The specified type must be one of the valid concrete types of PitchActuator, or the '$insert' type
        (in the case the model is defined to be inserted from an external resource).

        Useful when using type-checking development tools, as it provides a concise way to access a value with the correct type.

        Parameters
        ----------
        cls: Type[Union[IdealisedPitchActuator, PitchActuatorInsert, LinearPitchActuator, PitchSystemRotaryDrive]]
            One of the valid concrete types of PitchActuator, or the '$insert' type
            (in the case the model is defined to be inserted from an external resource).

        Returns
        -------
        TPitchActuatorOptions
            A model object of the specified type.

        Raises
        ------
        TypeError
            If the value is not of the specified type.

        Examples
        --------
        Get a reference to the value when it is one of the types of PitchActuator:
        >>> val_obj = model_obj.Actuator_as(models.IdealisedPitchActuator)
        >>> val_obj = model_obj.Actuator_as(models.LinearPitchActuator)
        >>> val_obj = model_obj.Actuator_as(models.PitchSystemRotaryDrive)

        Get a reference to the value, when it was specified with a '$insert' and read in from a file:
        >>> insert_obj = model_obj.Actuator_as(models.PitchActuatorInsert)
        """
        if not isinstance(self.Actuator, cls):
            raise TypeError(f"Expected Actuator of type '{cls.__name__}' but was type '{type(self.Actuator).__name__}'")
        return self.Actuator


    def _entity(self) -> bool:
        return True


PitchSystem.update_forward_refs()

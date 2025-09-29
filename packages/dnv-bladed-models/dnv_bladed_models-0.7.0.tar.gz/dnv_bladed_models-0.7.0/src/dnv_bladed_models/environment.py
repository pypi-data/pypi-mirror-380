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
from dnv_bladed_models.earthquake import Earthquake
from dnv_bladed_models.external_flow_source_for_wind import ExternalFlowSourceForWind
from dnv_bladed_models.laminar_flow_wind import LaminarFlowWind
from dnv_bladed_models.sea_state import SeaState
from dnv_bladed_models.turbulent_wind import TurbulentWind
from dnv_bladed_models.wind import Wind
from dnv_bladed_models.wind_insert import WindInsert

from .schema_helper import SchemaHelper
from .models_impl import *

TWindOptions = TypeVar('TWindOptions', ExternalFlowSourceForWind, WindInsert, LaminarFlowWind, TurbulentWind, Wind, )

class Environment(BladedModel):
    r"""
    The definition of the environment conditions affecting the turbine location during this simulation.
    
    Attributes
    ----------
    Wind : Union[ExternalFlowSourceForWind, WindInsert, LaminarFlowWind, TurbulentWind]
    
    SeaState : SeaState, Not supported yet
    
    Earthquake : Earthquake, Not supported yet
    
    Notes
    -----
    
    """
    Wind: Union[ExternalFlowSourceForWind, WindInsert, LaminarFlowWind, TurbulentWind] = Field(alias="Wind", default=None, discriminator='WindType')
    SeaState: SeaState = Field(alias="SeaState", default=None) # Not supported yet
    Earthquake: Earthquake = Field(alias="Earthquake", default=None) # Not supported yet

    _relative_schema_path = 'TimeDomainSimulation/Environment/Environment.json'
    _type_info = TypeInfo(
        set([('Wind', 'WindType'),]),
        set([]),
        set([]),
        None).merge(BladedModel._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    @property
    def Wind_as_ExternalFlowSourceForWind(self) -> ExternalFlowSourceForWind:
        """
        Retrieves the value of Wind guaranteeing it is a ExternalFlowSourceForWind; if it is not, an error is raised.

        Useful when using type-checking development tools, as it provides a concise way to retrieve a value and assign a variable with the correct type.

        Returns
        -------
        ExternalFlowSourceForWind
            A model object, guaranteed to be a ExternalFlowSourceForWind.

        Raises
        ------
        TypeError
            If the value is not a ExternalFlowSourceForWind.
        """
        return self.Wind_as(ExternalFlowSourceForWind)


    @property
    def Wind_as_LaminarFlowWind(self) -> LaminarFlowWind:
        """
        Retrieves the value of Wind guaranteeing it is a LaminarFlowWind; if it is not, an error is raised.

        Useful when using type-checking development tools, as it provides a concise way to retrieve a value and assign a variable with the correct type.

        Returns
        -------
        LaminarFlowWind
            A model object, guaranteed to be a LaminarFlowWind.

        Raises
        ------
        TypeError
            If the value is not a LaminarFlowWind.
        """
        return self.Wind_as(LaminarFlowWind)


    @property
    def Wind_as_TurbulentWind(self) -> TurbulentWind:
        """
        Retrieves the value of Wind guaranteeing it is a TurbulentWind; if it is not, an error is raised.

        Useful when using type-checking development tools, as it provides a concise way to retrieve a value and assign a variable with the correct type.

        Returns
        -------
        TurbulentWind
            A model object, guaranteed to be a TurbulentWind.

        Raises
        ------
        TypeError
            If the value is not a TurbulentWind.
        """
        return self.Wind_as(TurbulentWind)


    @property
    def Wind_as_inline(self) -> Union[ExternalFlowSourceForWind, LaminarFlowWind, TurbulentWind]:
        """
        Retrieves the value of Wind as a model object; if the value is specified with a '$insert', an error is raised.

        Returns
        -------
        Union[ExternalFlowSourceForWind, LaminarFlowWind, TurbulentWind]
            A model object at the specified index, guaranteed to not be a '$insert'.

        Raises
        ------
        TypeError
            If the value is not one of the concrete types of Wind; i.e. it is specified with a '$insert'.
        """
        if isinstance(self.Wind, WindInsert) or self.Wind.is_insert:
            raise TypeError(f"Expected Wind value to be an in-line object, but it is currently in the '$insert' state.")
        return self.Wind


    def Wind_as(self, cls: Type[TWindOptions])-> TWindOptions:
        """
        Retrieves the value of Wind, ensuring it is of the specified type.
        The specified type must be one of the valid concrete types of Wind, or the '$insert' type
        (in the case the model is defined to be inserted from an external resource).

        Useful when using type-checking development tools, as it provides a concise way to access a value with the correct type.

        Parameters
        ----------
        cls: Type[Union[ExternalFlowSourceForWind, WindInsert, LaminarFlowWind, TurbulentWind]]
            One of the valid concrete types of Wind, or the '$insert' type
            (in the case the model is defined to be inserted from an external resource).

        Returns
        -------
        TWindOptions
            A model object of the specified type.

        Raises
        ------
        TypeError
            If the value is not of the specified type.

        Examples
        --------
        Get a reference to the value when it is one of the types of Wind:
        >>> val_obj = model_obj.Wind_as(models.ExternalFlowSourceForWind)
        >>> val_obj = model_obj.Wind_as(models.LaminarFlowWind)
        >>> val_obj = model_obj.Wind_as(models.TurbulentWind)

        Get a reference to the value, when it was specified with a '$insert' and read in from a file:
        >>> insert_obj = model_obj.Wind_as(models.WindInsert)
        """
        if not isinstance(self.Wind, cls):
            raise TypeError(f"Expected Wind of type '{cls.__name__}' but was type '{type(self.Wind).__name__}'")
        return self.Wind


    def _entity(self) -> bool:
        return True


Environment.update_forward_refs()

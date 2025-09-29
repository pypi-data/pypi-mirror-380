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
from dnv_bladed_models.current_direction_shear_time_history import CurrentDirectionShearTimeHistory
from dnv_bladed_models.current_direction_shear_variation import CurrentDirectionShearVariation
from dnv_bladed_models.current_direction_shear_variation_insert import CurrentDirectionShearVariationInsert
from dnv_bladed_models.current_horizontal_shear_time_history import CurrentHorizontalShearTimeHistory
from dnv_bladed_models.current_horizontal_shear_variation import CurrentHorizontalShearVariation
from dnv_bladed_models.current_horizontal_shear_variation_insert import CurrentHorizontalShearVariationInsert
from dnv_bladed_models.current_mean_speed_time_history import CurrentMeanSpeedTimeHistory
from dnv_bladed_models.current_mean_speed_variation import CurrentMeanSpeedVariation
from dnv_bladed_models.current_mean_speed_variation_insert import CurrentMeanSpeedVariationInsert
from dnv_bladed_models.current_vertical_shear_time_history import CurrentVerticalShearTimeHistory
from dnv_bladed_models.current_vertical_shear_variation import CurrentVerticalShearVariation
from dnv_bladed_models.current_vertical_shear_variation_insert import CurrentVerticalShearVariationInsert
from dnv_bladed_models.preset_current_direction_shear_transient import PresetCurrentDirectionShearTransient
from dnv_bladed_models.preset_current_horizontal_shear_transient import PresetCurrentHorizontalShearTransient
from dnv_bladed_models.preset_current_mean_speed_transient import PresetCurrentMeanSpeedTransient
from dnv_bladed_models.preset_current_vertical_shear_transient import PresetCurrentVerticalShearTransient
from dnv_bladed_models.time_domain_current import TimeDomainCurrent

from .schema_helper import SchemaHelper
from .models_impl import *

TCurrentMeanSpeedVariationOptions = TypeVar('TCurrentMeanSpeedVariationOptions', CurrentMeanSpeedVariationInsert, PresetCurrentMeanSpeedTransient, CurrentMeanSpeedTimeHistory, CurrentMeanSpeedVariation, )
TCurrentVerticalShearVariationOptions = TypeVar('TCurrentVerticalShearVariationOptions', CurrentVerticalShearVariationInsert, PresetCurrentVerticalShearTransient, CurrentVerticalShearTimeHistory, CurrentVerticalShearVariation, )
TCurrentHorizontalShearVariationOptions = TypeVar('TCurrentHorizontalShearVariationOptions', CurrentHorizontalShearVariationInsert, PresetCurrentHorizontalShearTransient, CurrentHorizontalShearTimeHistory, CurrentHorizontalShearVariation, )
TCurrentDirectionShearVariationOptions = TypeVar('TCurrentDirectionShearVariationOptions', CurrentDirectionShearVariationInsert, PresetCurrentDirectionShearTransient, CurrentDirectionShearTimeHistory, CurrentDirectionShearVariation, )

class LaminarFlowCurrent(TimeDomainCurrent):
    r"""
    The definition of a current that varies throughout a time domain simulation, but does not have turbulence.
    
    Not supported yet.
    
    Attributes
    ----------
    CurrentType : Literal['LaminarFlow'], default='LaminarFlow', Not supported yet
        Defines the specific type of Current model in use.  For a `LaminarFlow` object, this must always be set to a value of `LaminarFlow`.
    
    MeanSpeed : float, Not supported yet
        The (constant) mean speed of the current for the duration of the simulation.
    
    MeanSpeedVariation : Union[CurrentMeanSpeedVariationInsert, PresetCurrentMeanSpeedTransient, CurrentMeanSpeedTimeHistory], Not supported yet
    
    VerticalShearVariation : Union[CurrentVerticalShearVariationInsert, PresetCurrentVerticalShearTransient, CurrentVerticalShearTimeHistory], Not supported yet
    
    HorizontalShearVariation : Union[CurrentHorizontalShearVariationInsert, PresetCurrentHorizontalShearTransient, CurrentHorizontalShearTimeHistory], Not supported yet
    
    DirectionShearVariation : Union[CurrentDirectionShearVariationInsert, PresetCurrentDirectionShearTransient, CurrentDirectionShearTimeHistory], Not supported yet
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    CurrentType: Literal['LaminarFlow'] = Field(alias="CurrentType", default='LaminarFlow', allow_mutation=False, const=True) # Not supported yet # type: ignore
    MeanSpeed: float = Field(alias="MeanSpeed", default=None) # Not supported yet
    MeanSpeedVariation: Union[CurrentMeanSpeedVariationInsert, PresetCurrentMeanSpeedTransient, CurrentMeanSpeedTimeHistory] = Field(alias="MeanSpeedVariation", default=None, discriminator='MeanSpeedVariationType') # Not supported yet
    VerticalShearVariation: Union[CurrentVerticalShearVariationInsert, PresetCurrentVerticalShearTransient, CurrentVerticalShearTimeHistory] = Field(alias="VerticalShearVariation", default=None, discriminator='VerticalShearVariationType') # Not supported yet
    HorizontalShearVariation: Union[CurrentHorizontalShearVariationInsert, PresetCurrentHorizontalShearTransient, CurrentHorizontalShearTimeHistory] = Field(alias="HorizontalShearVariation", default=None, discriminator='HorizontalShearVariationType') # Not supported yet
    DirectionShearVariation: Union[CurrentDirectionShearVariationInsert, PresetCurrentDirectionShearTransient, CurrentDirectionShearTimeHistory] = Field(alias="DirectionShearVariation", default=None, discriminator='DirectionShearVariationType') # Not supported yet

    _relative_schema_path = 'TimeDomainSimulation/Environment/SeaState/Current/LaminarFlowCurrent.json'
    _type_info = TypeInfo(
        set([('MeanSpeedVariation', 'MeanSpeedVariationType'),('VerticalShearVariation', 'VerticalShearVariationType'),('HorizontalShearVariation', 'HorizontalShearVariationType'),('DirectionShearVariation', 'DirectionShearVariationType'),]),
        set([]),
        set([]),
        'CurrentType').merge(TimeDomainCurrent._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    @property
    def MeanSpeedVariation_as_PresetCurrentMeanSpeedTransient(self) -> PresetCurrentMeanSpeedTransient:
        """
        Retrieves the value of MeanSpeedVariation guaranteeing it is a PresetCurrentMeanSpeedTransient; if it is not, an error is raised.

        Useful when using type-checking development tools, as it provides a concise way to retrieve a value and assign a variable with the correct type.

        Returns
        -------
        PresetCurrentMeanSpeedTransient
            A model object, guaranteed to be a PresetCurrentMeanSpeedTransient.

        Raises
        ------
        TypeError
            If the value is not a PresetCurrentMeanSpeedTransient.
        """
        return self.MeanSpeedVariation_as(PresetCurrentMeanSpeedTransient)


    @property
    def MeanSpeedVariation_as_CurrentMeanSpeedTimeHistory(self) -> CurrentMeanSpeedTimeHistory:
        """
        Retrieves the value of MeanSpeedVariation guaranteeing it is a CurrentMeanSpeedTimeHistory; if it is not, an error is raised.

        Useful when using type-checking development tools, as it provides a concise way to retrieve a value and assign a variable with the correct type.

        Returns
        -------
        CurrentMeanSpeedTimeHistory
            A model object, guaranteed to be a CurrentMeanSpeedTimeHistory.

        Raises
        ------
        TypeError
            If the value is not a CurrentMeanSpeedTimeHistory.
        """
        return self.MeanSpeedVariation_as(CurrentMeanSpeedTimeHistory)


    @property
    def MeanSpeedVariation_as_inline(self) -> Union[PresetCurrentMeanSpeedTransient, CurrentMeanSpeedTimeHistory]:
        """
        Retrieves the value of MeanSpeedVariation as a model object; if the value is specified with a '$insert', an error is raised.

        Returns
        -------
        Union[PresetCurrentMeanSpeedTransient, CurrentMeanSpeedTimeHistory]
            A model object at the specified index, guaranteed to not be a '$insert'.

        Raises
        ------
        TypeError
            If the value is not one of the concrete types of CurrentMeanSpeedVariation; i.e. it is specified with a '$insert'.
        """
        if isinstance(self.MeanSpeedVariation, CurrentMeanSpeedVariationInsert) or self.MeanSpeedVariation.is_insert:
            raise TypeError(f"Expected MeanSpeedVariation value to be an in-line object, but it is currently in the '$insert' state.")
        return self.MeanSpeedVariation


    def MeanSpeedVariation_as(self, cls: Type[TCurrentMeanSpeedVariationOptions])-> TCurrentMeanSpeedVariationOptions:
        """
        Retrieves the value of MeanSpeedVariation, ensuring it is of the specified type.
        The specified type must be one of the valid concrete types of CurrentMeanSpeedVariation, or the '$insert' type
        (in the case the model is defined to be inserted from an external resource).

        Useful when using type-checking development tools, as it provides a concise way to access a value with the correct type.

        Parameters
        ----------
        cls: Type[Union[CurrentMeanSpeedVariationInsert, PresetCurrentMeanSpeedTransient, CurrentMeanSpeedTimeHistory]]
            One of the valid concrete types of CurrentMeanSpeedVariation, or the '$insert' type
            (in the case the model is defined to be inserted from an external resource).

        Returns
        -------
        TCurrentMeanSpeedVariationOptions
            A model object of the specified type.

        Raises
        ------
        TypeError
            If the value is not of the specified type.

        Examples
        --------
        Get a reference to the value when it is one of the types of CurrentMeanSpeedVariation:
        >>> val_obj = model_obj.MeanSpeedVariation_as(models.PresetCurrentMeanSpeedTransient)
        >>> val_obj = model_obj.MeanSpeedVariation_as(models.CurrentMeanSpeedTimeHistory)

        Get a reference to the value, when it was specified with a '$insert' and read in from a file:
        >>> insert_obj = model_obj.MeanSpeedVariation_as(models.CurrentMeanSpeedVariationInsert)
        """
        if not isinstance(self.MeanSpeedVariation, cls):
            raise TypeError(f"Expected MeanSpeedVariation of type '{cls.__name__}' but was type '{type(self.MeanSpeedVariation).__name__}'")
        return self.MeanSpeedVariation


    @property
    def VerticalShearVariation_as_PresetCurrentVerticalShearTransient(self) -> PresetCurrentVerticalShearTransient:
        """
        Retrieves the value of VerticalShearVariation guaranteeing it is a PresetCurrentVerticalShearTransient; if it is not, an error is raised.

        Useful when using type-checking development tools, as it provides a concise way to retrieve a value and assign a variable with the correct type.

        Returns
        -------
        PresetCurrentVerticalShearTransient
            A model object, guaranteed to be a PresetCurrentVerticalShearTransient.

        Raises
        ------
        TypeError
            If the value is not a PresetCurrentVerticalShearTransient.
        """
        return self.VerticalShearVariation_as(PresetCurrentVerticalShearTransient)


    @property
    def VerticalShearVariation_as_CurrentVerticalShearTimeHistory(self) -> CurrentVerticalShearTimeHistory:
        """
        Retrieves the value of VerticalShearVariation guaranteeing it is a CurrentVerticalShearTimeHistory; if it is not, an error is raised.

        Useful when using type-checking development tools, as it provides a concise way to retrieve a value and assign a variable with the correct type.

        Returns
        -------
        CurrentVerticalShearTimeHistory
            A model object, guaranteed to be a CurrentVerticalShearTimeHistory.

        Raises
        ------
        TypeError
            If the value is not a CurrentVerticalShearTimeHistory.
        """
        return self.VerticalShearVariation_as(CurrentVerticalShearTimeHistory)


    @property
    def VerticalShearVariation_as_inline(self) -> Union[PresetCurrentVerticalShearTransient, CurrentVerticalShearTimeHistory]:
        """
        Retrieves the value of VerticalShearVariation as a model object; if the value is specified with a '$insert', an error is raised.

        Returns
        -------
        Union[PresetCurrentVerticalShearTransient, CurrentVerticalShearTimeHistory]
            A model object at the specified index, guaranteed to not be a '$insert'.

        Raises
        ------
        TypeError
            If the value is not one of the concrete types of CurrentVerticalShearVariation; i.e. it is specified with a '$insert'.
        """
        if isinstance(self.VerticalShearVariation, CurrentVerticalShearVariationInsert) or self.VerticalShearVariation.is_insert:
            raise TypeError(f"Expected VerticalShearVariation value to be an in-line object, but it is currently in the '$insert' state.")
        return self.VerticalShearVariation


    def VerticalShearVariation_as(self, cls: Type[TCurrentVerticalShearVariationOptions])-> TCurrentVerticalShearVariationOptions:
        """
        Retrieves the value of VerticalShearVariation, ensuring it is of the specified type.
        The specified type must be one of the valid concrete types of CurrentVerticalShearVariation, or the '$insert' type
        (in the case the model is defined to be inserted from an external resource).

        Useful when using type-checking development tools, as it provides a concise way to access a value with the correct type.

        Parameters
        ----------
        cls: Type[Union[CurrentVerticalShearVariationInsert, PresetCurrentVerticalShearTransient, CurrentVerticalShearTimeHistory]]
            One of the valid concrete types of CurrentVerticalShearVariation, or the '$insert' type
            (in the case the model is defined to be inserted from an external resource).

        Returns
        -------
        TCurrentVerticalShearVariationOptions
            A model object of the specified type.

        Raises
        ------
        TypeError
            If the value is not of the specified type.

        Examples
        --------
        Get a reference to the value when it is one of the types of CurrentVerticalShearVariation:
        >>> val_obj = model_obj.VerticalShearVariation_as(models.PresetCurrentVerticalShearTransient)
        >>> val_obj = model_obj.VerticalShearVariation_as(models.CurrentVerticalShearTimeHistory)

        Get a reference to the value, when it was specified with a '$insert' and read in from a file:
        >>> insert_obj = model_obj.VerticalShearVariation_as(models.CurrentVerticalShearVariationInsert)
        """
        if not isinstance(self.VerticalShearVariation, cls):
            raise TypeError(f"Expected VerticalShearVariation of type '{cls.__name__}' but was type '{type(self.VerticalShearVariation).__name__}'")
        return self.VerticalShearVariation


    @property
    def HorizontalShearVariation_as_PresetCurrentHorizontalShearTransient(self) -> PresetCurrentHorizontalShearTransient:
        """
        Retrieves the value of HorizontalShearVariation guaranteeing it is a PresetCurrentHorizontalShearTransient; if it is not, an error is raised.

        Useful when using type-checking development tools, as it provides a concise way to retrieve a value and assign a variable with the correct type.

        Returns
        -------
        PresetCurrentHorizontalShearTransient
            A model object, guaranteed to be a PresetCurrentHorizontalShearTransient.

        Raises
        ------
        TypeError
            If the value is not a PresetCurrentHorizontalShearTransient.
        """
        return self.HorizontalShearVariation_as(PresetCurrentHorizontalShearTransient)


    @property
    def HorizontalShearVariation_as_CurrentHorizontalShearTimeHistory(self) -> CurrentHorizontalShearTimeHistory:
        """
        Retrieves the value of HorizontalShearVariation guaranteeing it is a CurrentHorizontalShearTimeHistory; if it is not, an error is raised.

        Useful when using type-checking development tools, as it provides a concise way to retrieve a value and assign a variable with the correct type.

        Returns
        -------
        CurrentHorizontalShearTimeHistory
            A model object, guaranteed to be a CurrentHorizontalShearTimeHistory.

        Raises
        ------
        TypeError
            If the value is not a CurrentHorizontalShearTimeHistory.
        """
        return self.HorizontalShearVariation_as(CurrentHorizontalShearTimeHistory)


    @property
    def HorizontalShearVariation_as_inline(self) -> Union[PresetCurrentHorizontalShearTransient, CurrentHorizontalShearTimeHistory]:
        """
        Retrieves the value of HorizontalShearVariation as a model object; if the value is specified with a '$insert', an error is raised.

        Returns
        -------
        Union[PresetCurrentHorizontalShearTransient, CurrentHorizontalShearTimeHistory]
            A model object at the specified index, guaranteed to not be a '$insert'.

        Raises
        ------
        TypeError
            If the value is not one of the concrete types of CurrentHorizontalShearVariation; i.e. it is specified with a '$insert'.
        """
        if isinstance(self.HorizontalShearVariation, CurrentHorizontalShearVariationInsert) or self.HorizontalShearVariation.is_insert:
            raise TypeError(f"Expected HorizontalShearVariation value to be an in-line object, but it is currently in the '$insert' state.")
        return self.HorizontalShearVariation


    def HorizontalShearVariation_as(self, cls: Type[TCurrentHorizontalShearVariationOptions])-> TCurrentHorizontalShearVariationOptions:
        """
        Retrieves the value of HorizontalShearVariation, ensuring it is of the specified type.
        The specified type must be one of the valid concrete types of CurrentHorizontalShearVariation, or the '$insert' type
        (in the case the model is defined to be inserted from an external resource).

        Useful when using type-checking development tools, as it provides a concise way to access a value with the correct type.

        Parameters
        ----------
        cls: Type[Union[CurrentHorizontalShearVariationInsert, PresetCurrentHorizontalShearTransient, CurrentHorizontalShearTimeHistory]]
            One of the valid concrete types of CurrentHorizontalShearVariation, or the '$insert' type
            (in the case the model is defined to be inserted from an external resource).

        Returns
        -------
        TCurrentHorizontalShearVariationOptions
            A model object of the specified type.

        Raises
        ------
        TypeError
            If the value is not of the specified type.

        Examples
        --------
        Get a reference to the value when it is one of the types of CurrentHorizontalShearVariation:
        >>> val_obj = model_obj.HorizontalShearVariation_as(models.PresetCurrentHorizontalShearTransient)
        >>> val_obj = model_obj.HorizontalShearVariation_as(models.CurrentHorizontalShearTimeHistory)

        Get a reference to the value, when it was specified with a '$insert' and read in from a file:
        >>> insert_obj = model_obj.HorizontalShearVariation_as(models.CurrentHorizontalShearVariationInsert)
        """
        if not isinstance(self.HorizontalShearVariation, cls):
            raise TypeError(f"Expected HorizontalShearVariation of type '{cls.__name__}' but was type '{type(self.HorizontalShearVariation).__name__}'")
        return self.HorizontalShearVariation


    @property
    def DirectionShearVariation_as_PresetCurrentDirectionShearTransient(self) -> PresetCurrentDirectionShearTransient:
        """
        Retrieves the value of DirectionShearVariation guaranteeing it is a PresetCurrentDirectionShearTransient; if it is not, an error is raised.

        Useful when using type-checking development tools, as it provides a concise way to retrieve a value and assign a variable with the correct type.

        Returns
        -------
        PresetCurrentDirectionShearTransient
            A model object, guaranteed to be a PresetCurrentDirectionShearTransient.

        Raises
        ------
        TypeError
            If the value is not a PresetCurrentDirectionShearTransient.
        """
        return self.DirectionShearVariation_as(PresetCurrentDirectionShearTransient)


    @property
    def DirectionShearVariation_as_CurrentDirectionShearTimeHistory(self) -> CurrentDirectionShearTimeHistory:
        """
        Retrieves the value of DirectionShearVariation guaranteeing it is a CurrentDirectionShearTimeHistory; if it is not, an error is raised.

        Useful when using type-checking development tools, as it provides a concise way to retrieve a value and assign a variable with the correct type.

        Returns
        -------
        CurrentDirectionShearTimeHistory
            A model object, guaranteed to be a CurrentDirectionShearTimeHistory.

        Raises
        ------
        TypeError
            If the value is not a CurrentDirectionShearTimeHistory.
        """
        return self.DirectionShearVariation_as(CurrentDirectionShearTimeHistory)


    @property
    def DirectionShearVariation_as_inline(self) -> Union[PresetCurrentDirectionShearTransient, CurrentDirectionShearTimeHistory]:
        """
        Retrieves the value of DirectionShearVariation as a model object; if the value is specified with a '$insert', an error is raised.

        Returns
        -------
        Union[PresetCurrentDirectionShearTransient, CurrentDirectionShearTimeHistory]
            A model object at the specified index, guaranteed to not be a '$insert'.

        Raises
        ------
        TypeError
            If the value is not one of the concrete types of CurrentDirectionShearVariation; i.e. it is specified with a '$insert'.
        """
        if isinstance(self.DirectionShearVariation, CurrentDirectionShearVariationInsert) or self.DirectionShearVariation.is_insert:
            raise TypeError(f"Expected DirectionShearVariation value to be an in-line object, but it is currently in the '$insert' state.")
        return self.DirectionShearVariation


    def DirectionShearVariation_as(self, cls: Type[TCurrentDirectionShearVariationOptions])-> TCurrentDirectionShearVariationOptions:
        """
        Retrieves the value of DirectionShearVariation, ensuring it is of the specified type.
        The specified type must be one of the valid concrete types of CurrentDirectionShearVariation, or the '$insert' type
        (in the case the model is defined to be inserted from an external resource).

        Useful when using type-checking development tools, as it provides a concise way to access a value with the correct type.

        Parameters
        ----------
        cls: Type[Union[CurrentDirectionShearVariationInsert, PresetCurrentDirectionShearTransient, CurrentDirectionShearTimeHistory]]
            One of the valid concrete types of CurrentDirectionShearVariation, or the '$insert' type
            (in the case the model is defined to be inserted from an external resource).

        Returns
        -------
        TCurrentDirectionShearVariationOptions
            A model object of the specified type.

        Raises
        ------
        TypeError
            If the value is not of the specified type.

        Examples
        --------
        Get a reference to the value when it is one of the types of CurrentDirectionShearVariation:
        >>> val_obj = model_obj.DirectionShearVariation_as(models.PresetCurrentDirectionShearTransient)
        >>> val_obj = model_obj.DirectionShearVariation_as(models.CurrentDirectionShearTimeHistory)

        Get a reference to the value, when it was specified with a '$insert' and read in from a file:
        >>> insert_obj = model_obj.DirectionShearVariation_as(models.CurrentDirectionShearVariationInsert)
        """
        if not isinstance(self.DirectionShearVariation, cls):
            raise TypeError(f"Expected DirectionShearVariation of type '{cls.__name__}' but was type '{type(self.DirectionShearVariation).__name__}'")
        return self.DirectionShearVariation


    def _entity(self) -> bool:
        return True


LaminarFlowCurrent.update_forward_refs()

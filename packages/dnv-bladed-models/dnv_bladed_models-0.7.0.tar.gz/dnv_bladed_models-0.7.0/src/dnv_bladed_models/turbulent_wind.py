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
from dnv_bladed_models.evolving_turbulence import EvolvingTurbulence
from dnv_bladed_models.evolving_turbulence_exponential import EvolvingTurbulenceExponential
from dnv_bladed_models.evolving_turbulence_insert import EvolvingTurbulenceInsert
from dnv_bladed_models.evolving_turbulence_kristensen import EvolvingTurbulenceKristensen
from dnv_bladed_models.time_domain_wind import TimeDomainWind
class TurbulentWind_CentreTurbulenceFileOnEnum(str, Enum):
    CENTRED_ON_HUB = "CENTRED_ON_HUB"
    BEST_FIT = "BEST_FIT"
class TurbulentWind_InterpolationMethodEnum(str, Enum):
    LINEAR = "LINEAR"
    CUBIC_IN_ROTOR_PLANE = "CUBIC_IN_ROTOR_PLANE"
    ALL_CUBIC = "ALL_CUBIC"

from .schema_helper import SchemaHelper
from .models_impl import *

TEvolvingTurbulenceOptions = TypeVar('TEvolvingTurbulenceOptions', EvolvingTurbulenceExponential, EvolvingTurbulenceKristensen, EvolvingTurbulenceInsert, EvolvingTurbulence, )

class TurbulentWind(TimeDomainWind):
    r"""
    The definition of a turbulent flow field, with the values for the turbulence defined in an external file.
    
    Attributes
    ----------
    WindType : Literal['TurbulentWind'], default='TurbulentWind'
        Defines the specific type of Wind model in use.  For a `TurbulentWind` object, this must always be set to a value of `TurbulentWind`.
    
    MeanSpeed : float
        The mean wind speed upon which the turbulence will be added.  This must correspond with the mean wind speed used to create the turbulence file.
    
    TurbulenceFilepath : str
        The filepath or URI of the turbulence file.
    
    TurbulenceIntensity : float
        The turbulence intensity in the longitudinal (global X) direction.  This is used to scale the turbulence provided in the file.
    
    TurbulenceIntensityLateral : float
        The turbulence intensity in the lateral (global Y) direction.  This is typically in the order of 80% of the longitudinal turbulence intensity.
    
    TurbulenceIntensityVertical : float
        The turbulence intensity in the vertical (global Z) direction.  This is typically in the order of 50% of the longitudinal turbulence intensity.
    
    CentreTurbulenceFileOn : TurbulentWind_CentreTurbulenceFileOnEnum
        The method used to position the data in the turbulence file relative to the turbine.  If any part of the rotor exceeds this box, the simulation will terminate with an exception.
    
    CentreTurbulenceFileAtHeight : float
        The height at which to centre the data in the turbulence file.  If any part of the rotor exceeds this box, the simulation will terminate with an exception.
    
    InterpolationMethod : TurbulentWind_InterpolationMethodEnum, default='ALL_CUBIC'
        The method used to interpolate the wind speed in between the provided turbulence locations.
    
    RepeatTurbulenceFile : bool, default=False
        If true, the turbulence file will be \"looped\".  If false, the turbulence will be 0 in all three components once the end of the file has been reached.  Using part of a turbulence file may invalidate its turbulence statistics, and no effort is made by Bladed to ensure coherence at the point when it transitions from the end of the wind file back to the beginning.
    
    EvolvingTurbulence : Union[EvolvingTurbulenceExponential, EvolvingTurbulenceKristensen, EvolvingTurbulenceInsert]
    
    TurbulenceFileStartTime : float, default=0
        The time into turbulent wind file at start of simulation.  This can be used to synchronise the wind file with simulation.
    
    DirectionShear : float, default=0
        The direction shear, otherwise known as \"wind veer\".  This models the case where the direction of the wind field varies as the height increases.
    
    Notes
    -----
    
    """
    WindType: Literal['TurbulentWind'] = Field(alias="WindType", default='TurbulentWind', allow_mutation=False, const=True) # type: ignore
    MeanSpeed: float = Field(alias="MeanSpeed", default=None)
    TurbulenceFilepath: str = Field(alias="TurbulenceFilepath", default=None)
    TurbulenceIntensity: float = Field(alias="TurbulenceIntensity", default=None)
    TurbulenceIntensityLateral: float = Field(alias="TurbulenceIntensityLateral", default=None)
    TurbulenceIntensityVertical: float = Field(alias="TurbulenceIntensityVertical", default=None)
    CentreTurbulenceFileOn: TurbulentWind_CentreTurbulenceFileOnEnum = Field(alias="CentreTurbulenceFileOn", default=None)
    CentreTurbulenceFileAtHeight: float = Field(alias="CentreTurbulenceFileAtHeight", default=None)
    InterpolationMethod: TurbulentWind_InterpolationMethodEnum = Field(alias="InterpolationMethod", default=None)
    RepeatTurbulenceFile: bool = Field(alias="RepeatTurbulenceFile", default=None)
    EvolvingTurbulence: Union[EvolvingTurbulenceExponential, EvolvingTurbulenceKristensen, EvolvingTurbulenceInsert] = Field(alias="EvolvingTurbulence", default=None, discriminator='EvolvingTurbulenceType')
    TurbulenceFileStartTime: float = Field(alias="TurbulenceFileStartTime", default=None)
    DirectionShear: float = Field(alias="DirectionShear", default=None)

    _relative_schema_path = 'TimeDomainSimulation/Environment/Wind/TurbulentWind.json'
    _type_info = TypeInfo(
        set([('EvolvingTurbulence', 'EvolvingTurbulenceType'),]),
        set([]),
        set([]),
        'WindType').merge(TimeDomainWind._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    @property
    def EvolvingTurbulence_as_EvolvingTurbulenceExponential(self) -> EvolvingTurbulenceExponential:
        """
        Retrieves the value of EvolvingTurbulence guaranteeing it is a EvolvingTurbulenceExponential; if it is not, an error is raised.

        Useful when using type-checking development tools, as it provides a concise way to retrieve a value and assign a variable with the correct type.

        Returns
        -------
        EvolvingTurbulenceExponential
            A model object, guaranteed to be a EvolvingTurbulenceExponential.

        Raises
        ------
        TypeError
            If the value is not a EvolvingTurbulenceExponential.
        """
        return self.EvolvingTurbulence_as(EvolvingTurbulenceExponential)


    @property
    def EvolvingTurbulence_as_EvolvingTurbulenceKristensen(self) -> EvolvingTurbulenceKristensen:
        """
        Retrieves the value of EvolvingTurbulence guaranteeing it is a EvolvingTurbulenceKristensen; if it is not, an error is raised.

        Useful when using type-checking development tools, as it provides a concise way to retrieve a value and assign a variable with the correct type.

        Returns
        -------
        EvolvingTurbulenceKristensen
            A model object, guaranteed to be a EvolvingTurbulenceKristensen.

        Raises
        ------
        TypeError
            If the value is not a EvolvingTurbulenceKristensen.
        """
        return self.EvolvingTurbulence_as(EvolvingTurbulenceKristensen)


    @property
    def EvolvingTurbulence_as_inline(self) -> Union[EvolvingTurbulenceExponential, EvolvingTurbulenceKristensen]:
        """
        Retrieves the value of EvolvingTurbulence as a model object; if the value is specified with a '$insert', an error is raised.

        Returns
        -------
        Union[EvolvingTurbulenceExponential, EvolvingTurbulenceKristensen]
            A model object at the specified index, guaranteed to not be a '$insert'.

        Raises
        ------
        TypeError
            If the value is not one of the concrete types of EvolvingTurbulence; i.e. it is specified with a '$insert'.
        """
        if isinstance(self.EvolvingTurbulence, EvolvingTurbulenceInsert) or self.EvolvingTurbulence.is_insert:
            raise TypeError(f"Expected EvolvingTurbulence value to be an in-line object, but it is currently in the '$insert' state.")
        return self.EvolvingTurbulence


    def EvolvingTurbulence_as(self, cls: Type[TEvolvingTurbulenceOptions])-> TEvolvingTurbulenceOptions:
        """
        Retrieves the value of EvolvingTurbulence, ensuring it is of the specified type.
        The specified type must be one of the valid concrete types of EvolvingTurbulence, or the '$insert' type
        (in the case the model is defined to be inserted from an external resource).

        Useful when using type-checking development tools, as it provides a concise way to access a value with the correct type.

        Parameters
        ----------
        cls: Type[Union[EvolvingTurbulenceExponential, EvolvingTurbulenceKristensen, EvolvingTurbulenceInsert]]
            One of the valid concrete types of EvolvingTurbulence, or the '$insert' type
            (in the case the model is defined to be inserted from an external resource).

        Returns
        -------
        TEvolvingTurbulenceOptions
            A model object of the specified type.

        Raises
        ------
        TypeError
            If the value is not of the specified type.

        Examples
        --------
        Get a reference to the value when it is one of the types of EvolvingTurbulence:
        >>> val_obj = model_obj.EvolvingTurbulence_as(models.EvolvingTurbulenceExponential)
        >>> val_obj = model_obj.EvolvingTurbulence_as(models.EvolvingTurbulenceKristensen)

        Get a reference to the value, when it was specified with a '$insert' and read in from a file:
        >>> insert_obj = model_obj.EvolvingTurbulence_as(models.EvolvingTurbulenceInsert)
        """
        if not isinstance(self.EvolvingTurbulence, cls):
            raise TypeError(f"Expected EvolvingTurbulence of type '{cls.__name__}' but was type '{type(self.EvolvingTurbulence).__name__}'")
        return self.EvolvingTurbulence


    def _entity(self) -> bool:
        return True


TurbulentWind.update_forward_refs()

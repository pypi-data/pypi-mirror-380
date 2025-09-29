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

from .schema_helper import SchemaHelper
from .models_impl import *
TBladedModel = TypeVar('TBladedModel', bound='BladedModel')


class BladedModel(BladedEntity, ABC):
    r"""
    The base schema for all Bladed schema objects.
    
    Attributes
    ----------
    Schema : str
        The location of the JSON schema used to validate this object and enable enhanced tooling support.
    
    insert : str
        A path to a resource from which a valid JSON model object can be resolved. All properties will be taken from the resolved object; no properties can be specified in-line.
    
    Notes
    -----
    
    """
    Schema: str = Field(alias="$schema", default=None)
    insert: str = Field(alias="$insert", default=None)

    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        None).merge(BladedEntity._type_info)


    def extract_to_insert_from_file(
            self, 
            insert_path: Union[str, Path], 
            relative_to: Optional[Union[str, Path]] = None,
            write_file: bool = True) -> Path:
        r"""
        Sets this model to be inserted from a file when read by the Bladed application, and optionally writes the model to the new file. 
        Subsequently, when the parent model is serialized to JSON, only the '$insert' field will then be rendered for this model object.

        Parameters
        ----------
        insert_path : str or Path
            The seed for the '$insert' value for the JSON file that will contain the model document. 
            This can be an absolute path or a relative path.
            If absolute, and relative_to is supplied, a relative path will be calculated and set as the '$insert' value.
            If it is a relative path, and no relative_to is supplied, it will be interpreted relative to the current working directory.
        
        relative_to : str or Path
            The path to the file or directory that will contain the parent or owning model document.
            If supplied, and insert_path is absolute, it is used to calculate a relative path value, which is then set as the $insert value.
            If it is a relative path, it will be relative to the current working directory.

        write_file : bool = True
            If True, a JSON file will be written to the calculated file location, and contain the JSON model for insertion.

        Returns
        -------
        Path
            The full path of the file that the extracted model will be written to.

        Raises
        ------
        ValueError
            If the insert_path is None or empty.
            If a relative_to is provided and it is not a valid sub-path.
            If the model is already set to insert, and write_file is True.

        Examples
        --------
        1. Set the model to insert from a relative directory, using a relative seed path:
           - writes a new file to `c:/absolute/path/sub-dir/ChildModel.json` containing the child model JSON document
           - sets the insert path to `sub-dir/ChildModel.json` on the parent property object
           - writes the parent model to file, now containing the 'insert' reference to the child model

        >>> child_model_path = ParentModel.ChildModel.extract_to_insert_from_file("sub-dir/ChildModel.json", relative_to="c:/absolute/path/ParentModel.json")
        >>> ParentModel.to_file("c:/absolute/path/ParentModel.json")

        2. Set the model to insert from a relative directory, using an absolute seed path:
           - writes a new file to 'c:/absolute/path/sub-dir/ChildModel.json' containing the child model JSON document
           - sets the insert path to `../sub-dir/ChildModel.json` on the parent property object
           - writes the parent model to file, now containing the 'insert' reference to the child model

        >>> ParentModel.ChildModel.extract_to_insert_from_file("c:/absolute/path/sub-dir/ChildModel.json", relative_to="c:/absolute/path/parent-dir/ParentModel.json")
        >>> ParentModel.to_file("c:/absolute/path/parent-dir/ParentModel.json")
        """
        if insert_path is None or insert_path == "": # type: ignore
            raise ValueError("insert_path is required")
        
        ip: Path = Path(insert_path) if not isinstance(insert_path, Path) else insert_path

        insert_loc: Path = ip

        # Calculate the relative path to the relative_to if required
        if relative_to is not None and str(relative_to) != "" and ip.is_absolute():
            relp: Path = Path(relative_to).resolve() if not isinstance(relative_to, Path) else relative_to.resolve()
            relp_d: Path = relp if relp.is_dir() else relp.parent
            insert_loc = Path(os.path.relpath(ip.resolve(), relp_d))
            
        if relative_to is not None and str(relative_to) != "" and not ip.is_absolute():
            relp: Path = Path(relative_to) if not isinstance(relative_to, Path) else relative_to
            relp_d: Path = relp if relp.is_dir() else relp.parent
            file_loc = relp_d.joinpath(insert_path).resolve()
        else:
            file_loc = ip if ip.is_absolute() else ip.resolve()
            
        if write_file:
            if self.is_insert:
                raise ValueError("Cannot extract a model to a new file when it has already been set as an insert.")
            
            if not file_loc.parent.exists():
                file_loc.parent.mkdir(parents=True, exist_ok=True)

            self.to_file(file_loc)
        
        # forward slashes render a little neater in JSON as they don't require escaping.
        # there's no functional difference either way, and the Bladed application will accept either.
        self.insert = insert_loc.as_posix()
        return file_loc



    def to_json(self, indent: Optional[int] = 2, **json_kwargs: Any) -> str:
        r"""
        Generates a JSON string representation of the model.

        Parameters
        ----------
        indent : int
            The whitespace indentation to use for formatting, as per json.dumps().

        Examples
        --------
        >>> model.to_json()
        Renders the full JSON representation of the model object.
        """

        json_kwargs['by_alias'] = True
        json_kwargs['exclude_unset'] = False
        json_kwargs['exclude_none'] = True
        if self.Schema is None:
            self.Schema = SchemaHelper.construct_schema_url(getattr(self, '_relative_schema_path'))
        
        return super().json(indent=indent, **json_kwargs)


    @classmethod
    def from_file(cls: Type[TBladedModel], path: Union[str, Path]) -> TBladedModel:
        r"""
        Loads a model from a given file path.

        Parameters
        ----------
        path : string
            The file path to the model.

        Returns
        -------
        
            The model object.

        Raises
        ------
        ValueError, ValidationError
            If the JSON document does not correctly describe the model according to the model schema.

        Examples
        --------
        >>> model = ModelClass.from_file('/path/to/file')
        """
        
        return super().parse_file(path=path)


    @classmethod
    def from_json(cls: Type[TBladedModel], b: StrBytes) -> TBladedModel:
        r"""
        Creates a model object from a JSON string.

        Parameters
        ----------
        b: StrBytes
            The JSON string describing the model.

        Returns
        -------
        
            The model object.

        Raises
        ------
        ValueError, ValidationError
            If the JSON document does not correctly describe the model according to the model schema.

        Examples
        --------
        >>> model = ModelClass.from_json('{ ... }')
        """

        return super().parse_raw(
            b=b,
            content_type='application/json')
        

    @classmethod
    def from_dict(cls: Type[TBladedModel], obj: Any) -> TBladedModel:
        r"""
        Creates a model object from a dict.
        
        Parameters
        ----------
        obj : Any
            The dictionary object describing the model.

        Returns
        -------
        
            The model object.

        Raises
        ------
        ValueError, ValidationError
            If the JSON document does not correctly describe the model according to the model schema.

        Examples
        --------
        >>> model = ModelClass.from_dict({ ... })
        """
        
        return cls.parse_obj(obj=obj)


    def to_file(self, path: Union[str, Path]) -> None:
        r"""
        Writes the model as a JSON document to a file with UTF8 encoding.

        Parameters
        ----------                
        path : string
            The file path to which the model will be written.

        Examples
        --------
        >>> model.to_file('/path/to/file')
        """

        with open(file=path, mode='w', encoding="utf8") as output_file:
            output_file.write(self.to_json())


BladedModel.update_forward_refs()

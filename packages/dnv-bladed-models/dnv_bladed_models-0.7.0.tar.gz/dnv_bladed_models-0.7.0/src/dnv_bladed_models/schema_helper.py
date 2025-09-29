# *********************************************************************#
# Bladed Python Models API                                             #
# Copyright (c) DNV Services UK Limited (c) 2025. All rights reserved. #
# MIT License (see license file)                                       #
# *********************************************************************#


class SchemaHelper:
    """
    Helper methods for constructing schema URLs and retrieving the schema version.
    """
    __schema_version__ = "0.7.0"
    __build_version__ = "0.7.0-rc.18+b.71.sha.68d8d40c"
    __Host__ = "https://bladednextgen.dnv.com/schema"

    @staticmethod
    def construct_schema_url(relative_schema_path: str) -> str:
        """
        Constructs a schema URL based on the provided path.

        Parameters
        ----------
        relative_schema_path: str
            The relative path to a schema file within the Bladed schema repository.

        Returns
        -------
        str
            The constructed schema URL.

        """
        return f"{SchemaHelper.__Host__}/{SchemaHelper.__schema_version__}/{relative_schema_path}"


    @staticmethod
    def get_schema_version() -> str:
        """
        Retrieves the schema version this Model API was generated for.
        """
        return SchemaHelper.__schema_version__
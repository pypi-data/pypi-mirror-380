# coding: utf-8

"""
    The Plane REST API

    The Plane REST API  Visit our quick start guide and full API documentation at [developers.plane.so](https://developers.plane.so/api-reference/introduction).

    The version of the API Spec: 0.0.2
    Contact: support@plane.so
    This class is auto generated.

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class NetworkEnum(int, Enum):
    """
    * `0` - Secret * `2` - Public
    """

    """
    allowed enum values
    """
    NUMBER_0 = 0
    NUMBER_2 = 2

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of NetworkEnum from a JSON string"""
        return cls(json.loads(json_str))



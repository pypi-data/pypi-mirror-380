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
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from plane.models.intake_work_item_status_enum import IntakeWorkItemStatusEnum
from plane.models.issue_expand import IssueExpand
from typing import Set
from typing_extensions import Self

class IntakeIssue(BaseModel):
    """
    Comprehensive serializer for intake work items with expanded issue details.  Provides full intake work item data including embedded issue information, status tracking, and triage metadata for issue queue management.
    """ # noqa: E501
    id: Optional[StrictStr] = None
    issue_detail: Optional[IssueExpand] = None
    inbox: Optional[StrictStr] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    status: Optional[IntakeWorkItemStatusEnum] = None
    snoozed_till: Optional[datetime] = None
    source: Optional[Annotated[str, Field(strict=True, max_length=255)]] = None
    source_email: Optional[StrictStr] = None
    external_source: Optional[Annotated[str, Field(strict=True, max_length=255)]] = None
    external_id: Optional[Annotated[str, Field(strict=True, max_length=255)]] = None
    extra: Optional[Any] = None
    created_by: Optional[StrictStr] = None
    updated_by: Optional[StrictStr] = None
    project: Optional[StrictStr] = None
    workspace: Optional[StrictStr] = None
    intake: StrictStr
    issue: Optional[StrictStr] = None
    duplicate_to: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["id", "issue_detail", "inbox", "created_at", "updated_at", "deleted_at", "status", "snoozed_till", "source", "source_email", "external_source", "external_id", "extra", "created_by", "updated_by", "project", "workspace", "intake", "issue", "duplicate_to"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of IntakeIssue from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "id",
            "issue_detail",
            "inbox",
            "created_at",
            "updated_at",
            "created_by",
            "updated_by",
            "project",
            "workspace",
            "issue",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of issue_detail
        if self.issue_detail:
            _dict['issue_detail'] = self.issue_detail.to_dict()
        # set to None if deleted_at (nullable) is None
        # and model_fields_set contains the field
        if self.deleted_at is None and "deleted_at" in self.model_fields_set:
            _dict['deleted_at'] = None

        # set to None if snoozed_till (nullable) is None
        # and model_fields_set contains the field
        if self.snoozed_till is None and "snoozed_till" in self.model_fields_set:
            _dict['snoozed_till'] = None

        # set to None if source (nullable) is None
        # and model_fields_set contains the field
        if self.source is None and "source" in self.model_fields_set:
            _dict['source'] = None

        # set to None if source_email (nullable) is None
        # and model_fields_set contains the field
        if self.source_email is None and "source_email" in self.model_fields_set:
            _dict['source_email'] = None

        # set to None if external_source (nullable) is None
        # and model_fields_set contains the field
        if self.external_source is None and "external_source" in self.model_fields_set:
            _dict['external_source'] = None

        # set to None if external_id (nullable) is None
        # and model_fields_set contains the field
        if self.external_id is None and "external_id" in self.model_fields_set:
            _dict['external_id'] = None

        # set to None if extra (nullable) is None
        # and model_fields_set contains the field
        if self.extra is None and "extra" in self.model_fields_set:
            _dict['extra'] = None

        # set to None if created_by (nullable) is None
        # and model_fields_set contains the field
        if self.created_by is None and "created_by" in self.model_fields_set:
            _dict['created_by'] = None

        # set to None if updated_by (nullable) is None
        # and model_fields_set contains the field
        if self.updated_by is None and "updated_by" in self.model_fields_set:
            _dict['updated_by'] = None

        # set to None if duplicate_to (nullable) is None
        # and model_fields_set contains the field
        if self.duplicate_to is None and "duplicate_to" in self.model_fields_set:
            _dict['duplicate_to'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IntakeIssue from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "issue_detail": IssueExpand.from_dict(obj["issue_detail"]) if obj.get("issue_detail") is not None else None,
            "inbox": obj.get("inbox"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "deleted_at": obj.get("deleted_at"),
            "status": obj.get("status"),
            "snoozed_till": obj.get("snoozed_till"),
            "source": obj.get("source"),
            "source_email": obj.get("source_email"),
            "external_source": obj.get("external_source"),
            "external_id": obj.get("external_id"),
            "extra": obj.get("extra"),
            "created_by": obj.get("created_by"),
            "updated_by": obj.get("updated_by"),
            "project": obj.get("project"),
            "workspace": obj.get("workspace"),
            "intake": obj.get("intake"),
            "issue": obj.get("issue"),
            "duplicate_to": obj.get("duplicate_to")
        })
        return _obj



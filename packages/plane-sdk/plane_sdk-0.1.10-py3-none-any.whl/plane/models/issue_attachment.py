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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from typing import Set
from typing_extensions import Self

class IssueAttachment(BaseModel):
    """
    Serializer for work item file attachments.  Manages file asset associations with work items including metadata, storage information, and access control for document management.
    """ # noqa: E501
    id: Optional[StrictStr] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    attributes: Optional[Any] = None
    asset: StrictStr
    entity_type: Optional[Annotated[str, Field(strict=True, max_length=255)]] = None
    entity_identifier: Optional[Annotated[str, Field(strict=True, max_length=255)]] = None
    is_deleted: Optional[StrictBool] = None
    is_archived: Optional[StrictBool] = None
    external_id: Optional[Annotated[str, Field(strict=True, max_length=255)]] = None
    external_source: Optional[Annotated[str, Field(strict=True, max_length=255)]] = None
    size: Optional[Union[StrictFloat, StrictInt]] = None
    is_uploaded: Optional[StrictBool] = None
    storage_metadata: Optional[Any] = None
    created_by: Optional[StrictStr] = None
    updated_by: Optional[StrictStr] = None
    user: Optional[StrictStr] = None
    workspace: Optional[StrictStr] = None
    draft_issue: Optional[StrictStr] = None
    project: Optional[StrictStr] = None
    issue: Optional[StrictStr] = None
    comment: Optional[StrictStr] = None
    page: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["id", "created_at", "updated_at", "deleted_at", "attributes", "asset", "entity_type", "entity_identifier", "is_deleted", "is_archived", "external_id", "external_source", "size", "is_uploaded", "storage_metadata", "created_by", "updated_by", "user", "workspace", "draft_issue", "project", "issue", "comment", "page"]

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
        """Create an instance of IssueAttachment from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "id",
            "created_at",
            "updated_at",
            "updated_by",
            "workspace",
            "project",
            "issue",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if deleted_at (nullable) is None
        # and model_fields_set contains the field
        if self.deleted_at is None and "deleted_at" in self.model_fields_set:
            _dict['deleted_at'] = None

        # set to None if attributes (nullable) is None
        # and model_fields_set contains the field
        if self.attributes is None and "attributes" in self.model_fields_set:
            _dict['attributes'] = None

        # set to None if entity_type (nullable) is None
        # and model_fields_set contains the field
        if self.entity_type is None and "entity_type" in self.model_fields_set:
            _dict['entity_type'] = None

        # set to None if entity_identifier (nullable) is None
        # and model_fields_set contains the field
        if self.entity_identifier is None and "entity_identifier" in self.model_fields_set:
            _dict['entity_identifier'] = None

        # set to None if external_id (nullable) is None
        # and model_fields_set contains the field
        if self.external_id is None and "external_id" in self.model_fields_set:
            _dict['external_id'] = None

        # set to None if external_source (nullable) is None
        # and model_fields_set contains the field
        if self.external_source is None and "external_source" in self.model_fields_set:
            _dict['external_source'] = None

        # set to None if storage_metadata (nullable) is None
        # and model_fields_set contains the field
        if self.storage_metadata is None and "storage_metadata" in self.model_fields_set:
            _dict['storage_metadata'] = None

        # set to None if created_by (nullable) is None
        # and model_fields_set contains the field
        if self.created_by is None and "created_by" in self.model_fields_set:
            _dict['created_by'] = None

        # set to None if updated_by (nullable) is None
        # and model_fields_set contains the field
        if self.updated_by is None and "updated_by" in self.model_fields_set:
            _dict['updated_by'] = None

        # set to None if user (nullable) is None
        # and model_fields_set contains the field
        if self.user is None and "user" in self.model_fields_set:
            _dict['user'] = None

        # set to None if workspace (nullable) is None
        # and model_fields_set contains the field
        if self.workspace is None and "workspace" in self.model_fields_set:
            _dict['workspace'] = None

        # set to None if draft_issue (nullable) is None
        # and model_fields_set contains the field
        if self.draft_issue is None and "draft_issue" in self.model_fields_set:
            _dict['draft_issue'] = None

        # set to None if project (nullable) is None
        # and model_fields_set contains the field
        if self.project is None and "project" in self.model_fields_set:
            _dict['project'] = None

        # set to None if issue (nullable) is None
        # and model_fields_set contains the field
        if self.issue is None and "issue" in self.model_fields_set:
            _dict['issue'] = None

        # set to None if comment (nullable) is None
        # and model_fields_set contains the field
        if self.comment is None and "comment" in self.model_fields_set:
            _dict['comment'] = None

        # set to None if page (nullable) is None
        # and model_fields_set contains the field
        if self.page is None and "page" in self.model_fields_set:
            _dict['page'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IssueAttachment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "deleted_at": obj.get("deleted_at"),
            "attributes": obj.get("attributes"),
            "asset": obj.get("asset"),
            "entity_type": obj.get("entity_type"),
            "entity_identifier": obj.get("entity_identifier"),
            "is_deleted": obj.get("is_deleted"),
            "is_archived": obj.get("is_archived"),
            "external_id": obj.get("external_id"),
            "external_source": obj.get("external_source"),
            "size": obj.get("size"),
            "is_uploaded": obj.get("is_uploaded"),
            "storage_metadata": obj.get("storage_metadata"),
            "created_by": obj.get("created_by"),
            "updated_by": obj.get("updated_by"),
            "user": obj.get("user"),
            "workspace": obj.get("workspace"),
            "draft_issue": obj.get("draft_issue"),
            "project": obj.get("project"),
            "issue": obj.get("issue"),
            "comment": obj.get("comment"),
            "page": obj.get("page")
        })
        return _obj



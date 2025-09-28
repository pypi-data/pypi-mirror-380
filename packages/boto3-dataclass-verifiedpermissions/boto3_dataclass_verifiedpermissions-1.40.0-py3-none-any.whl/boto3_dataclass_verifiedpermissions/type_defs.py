# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_verifiedpermissions import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class ActionIdentifier:
    boto3_raw_data: "type_defs.ActionIdentifierTypeDef" = dataclasses.field()

    actionType = field("actionType")
    actionId = field("actionId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActionIdentifierTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActionIdentifierTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EntityIdentifier:
    boto3_raw_data: "type_defs.EntityIdentifierTypeDef" = dataclasses.field()

    entityType = field("entityType")
    entityId = field("entityId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EntityIdentifierTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EntityIdentifierTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetPolicyErrorItem:
    boto3_raw_data: "type_defs.BatchGetPolicyErrorItemTypeDef" = dataclasses.field()

    code = field("code")
    policyStoreId = field("policyStoreId")
    policyId = field("policyId")
    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetPolicyErrorItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetPolicyErrorItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetPolicyInputItem:
    boto3_raw_data: "type_defs.BatchGetPolicyInputItemTypeDef" = dataclasses.field()

    policyStoreId = field("policyStoreId")
    policyId = field("policyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetPolicyInputItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetPolicyInputItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseMetadata:
    boto3_raw_data: "type_defs.ResponseMetadataTypeDef" = dataclasses.field()

    RequestId = field("RequestId")
    HTTPStatusCode = field("HTTPStatusCode")
    HTTPHeaders = field("HTTPHeaders")
    RetryAttempts = field("RetryAttempts")
    HostId = field("HostId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResponseMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponseMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeterminingPolicyItem:
    boto3_raw_data: "type_defs.DeterminingPolicyItemTypeDef" = dataclasses.field()

    policyId = field("policyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeterminingPolicyItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeterminingPolicyItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationErrorItem:
    boto3_raw_data: "type_defs.EvaluationErrorItemTypeDef" = dataclasses.field()

    errorDescription = field("errorDescription")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EvaluationErrorItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationErrorItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CognitoGroupConfigurationDetail:
    boto3_raw_data: "type_defs.CognitoGroupConfigurationDetailTypeDef" = (
        dataclasses.field()
    )

    groupEntityType = field("groupEntityType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CognitoGroupConfigurationDetailTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CognitoGroupConfigurationDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CognitoGroupConfigurationItem:
    boto3_raw_data: "type_defs.CognitoGroupConfigurationItemTypeDef" = (
        dataclasses.field()
    )

    groupEntityType = field("groupEntityType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CognitoGroupConfigurationItemTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CognitoGroupConfigurationItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CognitoGroupConfiguration:
    boto3_raw_data: "type_defs.CognitoGroupConfigurationTypeDef" = dataclasses.field()

    groupEntityType = field("groupEntityType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CognitoGroupConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CognitoGroupConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValidationSettings:
    boto3_raw_data: "type_defs.ValidationSettingsTypeDef" = dataclasses.field()

    mode = field("mode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ValidationSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValidationSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePolicyTemplateInput:
    boto3_raw_data: "type_defs.CreatePolicyTemplateInputTypeDef" = dataclasses.field()

    policyStoreId = field("policyStoreId")
    statement = field("statement")
    clientToken = field("clientToken")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePolicyTemplateInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePolicyTemplateInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteIdentitySourceInput:
    boto3_raw_data: "type_defs.DeleteIdentitySourceInputTypeDef" = dataclasses.field()

    policyStoreId = field("policyStoreId")
    identitySourceId = field("identitySourceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteIdentitySourceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteIdentitySourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePolicyInput:
    boto3_raw_data: "type_defs.DeletePolicyInputTypeDef" = dataclasses.field()

    policyStoreId = field("policyStoreId")
    policyId = field("policyId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeletePolicyInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePolicyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePolicyStoreInput:
    boto3_raw_data: "type_defs.DeletePolicyStoreInputTypeDef" = dataclasses.field()

    policyStoreId = field("policyStoreId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePolicyStoreInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePolicyStoreInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePolicyTemplateInput:
    boto3_raw_data: "type_defs.DeletePolicyTemplateInputTypeDef" = dataclasses.field()

    policyStoreId = field("policyStoreId")
    policyTemplateId = field("policyTemplateId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePolicyTemplateInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePolicyTemplateInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIdentitySourceInput:
    boto3_raw_data: "type_defs.GetIdentitySourceInputTypeDef" = dataclasses.field()

    policyStoreId = field("policyStoreId")
    identitySourceId = field("identitySourceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetIdentitySourceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIdentitySourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdentitySourceDetails:
    boto3_raw_data: "type_defs.IdentitySourceDetailsTypeDef" = dataclasses.field()

    clientIds = field("clientIds")
    userPoolArn = field("userPoolArn")
    discoveryUrl = field("discoveryUrl")
    openIdIssuer = field("openIdIssuer")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IdentitySourceDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdentitySourceDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPolicyInput:
    boto3_raw_data: "type_defs.GetPolicyInputTypeDef" = dataclasses.field()

    policyStoreId = field("policyStoreId")
    policyId = field("policyId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetPolicyInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetPolicyInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPolicyStoreInput:
    boto3_raw_data: "type_defs.GetPolicyStoreInputTypeDef" = dataclasses.field()

    policyStoreId = field("policyStoreId")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPolicyStoreInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPolicyStoreInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPolicyTemplateInput:
    boto3_raw_data: "type_defs.GetPolicyTemplateInputTypeDef" = dataclasses.field()

    policyStoreId = field("policyStoreId")
    policyTemplateId = field("policyTemplateId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPolicyTemplateInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPolicyTemplateInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSchemaInput:
    boto3_raw_data: "type_defs.GetSchemaInputTypeDef" = dataclasses.field()

    policyStoreId = field("policyStoreId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetSchemaInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetSchemaInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdentitySourceFilter:
    boto3_raw_data: "type_defs.IdentitySourceFilterTypeDef" = dataclasses.field()

    principalEntityType = field("principalEntityType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IdentitySourceFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdentitySourceFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdentitySourceItemDetails:
    boto3_raw_data: "type_defs.IdentitySourceItemDetailsTypeDef" = dataclasses.field()

    clientIds = field("clientIds")
    userPoolArn = field("userPoolArn")
    discoveryUrl = field("discoveryUrl")
    openIdIssuer = field("openIdIssuer")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IdentitySourceItemDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdentitySourceItemDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PaginatorConfig:
    boto3_raw_data: "type_defs.PaginatorConfigTypeDef" = dataclasses.field()

    MaxItems = field("MaxItems")
    PageSize = field("PageSize")
    StartingToken = field("StartingToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PaginatorConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PaginatorConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPolicyStoresInput:
    boto3_raw_data: "type_defs.ListPolicyStoresInputTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPolicyStoresInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPolicyStoresInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolicyStoreItem:
    boto3_raw_data: "type_defs.PolicyStoreItemTypeDef" = dataclasses.field()

    policyStoreId = field("policyStoreId")
    arn = field("arn")
    createdDate = field("createdDate")
    lastUpdatedDate = field("lastUpdatedDate")
    description = field("description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PolicyStoreItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PolicyStoreItemTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPolicyTemplatesInput:
    boto3_raw_data: "type_defs.ListPolicyTemplatesInputTypeDef" = dataclasses.field()

    policyStoreId = field("policyStoreId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPolicyTemplatesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPolicyTemplatesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolicyTemplateItem:
    boto3_raw_data: "type_defs.PolicyTemplateItemTypeDef" = dataclasses.field()

    policyStoreId = field("policyStoreId")
    policyTemplateId = field("policyTemplateId")
    createdDate = field("createdDate")
    lastUpdatedDate = field("lastUpdatedDate")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PolicyTemplateItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PolicyTemplateItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceInput:
    boto3_raw_data: "type_defs.ListTagsForResourceInputTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenIdConnectAccessTokenConfigurationDetail:
    boto3_raw_data: "type_defs.OpenIdConnectAccessTokenConfigurationDetailTypeDef" = (
        dataclasses.field()
    )

    principalIdClaim = field("principalIdClaim")
    audiences = field("audiences")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OpenIdConnectAccessTokenConfigurationDetailTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpenIdConnectAccessTokenConfigurationDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenIdConnectAccessTokenConfigurationItem:
    boto3_raw_data: "type_defs.OpenIdConnectAccessTokenConfigurationItemTypeDef" = (
        dataclasses.field()
    )

    principalIdClaim = field("principalIdClaim")
    audiences = field("audiences")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OpenIdConnectAccessTokenConfigurationItemTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpenIdConnectAccessTokenConfigurationItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenIdConnectAccessTokenConfiguration:
    boto3_raw_data: "type_defs.OpenIdConnectAccessTokenConfigurationTypeDef" = (
        dataclasses.field()
    )

    principalIdClaim = field("principalIdClaim")
    audiences = field("audiences")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OpenIdConnectAccessTokenConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpenIdConnectAccessTokenConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenIdConnectGroupConfigurationDetail:
    boto3_raw_data: "type_defs.OpenIdConnectGroupConfigurationDetailTypeDef" = (
        dataclasses.field()
    )

    groupClaim = field("groupClaim")
    groupEntityType = field("groupEntityType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OpenIdConnectGroupConfigurationDetailTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpenIdConnectGroupConfigurationDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenIdConnectGroupConfigurationItem:
    boto3_raw_data: "type_defs.OpenIdConnectGroupConfigurationItemTypeDef" = (
        dataclasses.field()
    )

    groupClaim = field("groupClaim")
    groupEntityType = field("groupEntityType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OpenIdConnectGroupConfigurationItemTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpenIdConnectGroupConfigurationItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenIdConnectGroupConfiguration:
    boto3_raw_data: "type_defs.OpenIdConnectGroupConfigurationTypeDef" = (
        dataclasses.field()
    )

    groupClaim = field("groupClaim")
    groupEntityType = field("groupEntityType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.OpenIdConnectGroupConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpenIdConnectGroupConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenIdConnectIdentityTokenConfigurationDetail:
    boto3_raw_data: "type_defs.OpenIdConnectIdentityTokenConfigurationDetailTypeDef" = (
        dataclasses.field()
    )

    principalIdClaim = field("principalIdClaim")
    clientIds = field("clientIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OpenIdConnectIdentityTokenConfigurationDetailTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpenIdConnectIdentityTokenConfigurationDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenIdConnectIdentityTokenConfigurationItem:
    boto3_raw_data: "type_defs.OpenIdConnectIdentityTokenConfigurationItemTypeDef" = (
        dataclasses.field()
    )

    principalIdClaim = field("principalIdClaim")
    clientIds = field("clientIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OpenIdConnectIdentityTokenConfigurationItemTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpenIdConnectIdentityTokenConfigurationItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenIdConnectIdentityTokenConfiguration:
    boto3_raw_data: "type_defs.OpenIdConnectIdentityTokenConfigurationTypeDef" = (
        dataclasses.field()
    )

    principalIdClaim = field("principalIdClaim")
    clientIds = field("clientIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OpenIdConnectIdentityTokenConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpenIdConnectIdentityTokenConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StaticPolicyDefinitionDetail:
    boto3_raw_data: "type_defs.StaticPolicyDefinitionDetailTypeDef" = (
        dataclasses.field()
    )

    statement = field("statement")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StaticPolicyDefinitionDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StaticPolicyDefinitionDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StaticPolicyDefinitionItem:
    boto3_raw_data: "type_defs.StaticPolicyDefinitionItemTypeDef" = dataclasses.field()

    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StaticPolicyDefinitionItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StaticPolicyDefinitionItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StaticPolicyDefinition:
    boto3_raw_data: "type_defs.StaticPolicyDefinitionTypeDef" = dataclasses.field()

    statement = field("statement")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StaticPolicyDefinitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StaticPolicyDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SchemaDefinition:
    boto3_raw_data: "type_defs.SchemaDefinitionTypeDef" = dataclasses.field()

    cedarJson = field("cedarJson")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SchemaDefinitionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SchemaDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagResourceInput:
    boto3_raw_data: "type_defs.TagResourceInputTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")
    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagResourceInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagResourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagResourceInput:
    boto3_raw_data: "type_defs.UntagResourceInputTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")
    tagKeys = field("tagKeys")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UntagResourceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UntagResourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCognitoGroupConfiguration:
    boto3_raw_data: "type_defs.UpdateCognitoGroupConfigurationTypeDef" = (
        dataclasses.field()
    )

    groupEntityType = field("groupEntityType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateCognitoGroupConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCognitoGroupConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateOpenIdConnectAccessTokenConfiguration:
    boto3_raw_data: "type_defs.UpdateOpenIdConnectAccessTokenConfigurationTypeDef" = (
        dataclasses.field()
    )

    principalIdClaim = field("principalIdClaim")
    audiences = field("audiences")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateOpenIdConnectAccessTokenConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateOpenIdConnectAccessTokenConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateOpenIdConnectGroupConfiguration:
    boto3_raw_data: "type_defs.UpdateOpenIdConnectGroupConfigurationTypeDef" = (
        dataclasses.field()
    )

    groupClaim = field("groupClaim")
    groupEntityType = field("groupEntityType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateOpenIdConnectGroupConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateOpenIdConnectGroupConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateOpenIdConnectIdentityTokenConfiguration:
    boto3_raw_data: "type_defs.UpdateOpenIdConnectIdentityTokenConfigurationTypeDef" = (
        dataclasses.field()
    )

    principalIdClaim = field("principalIdClaim")
    clientIds = field("clientIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateOpenIdConnectIdentityTokenConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateOpenIdConnectIdentityTokenConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateStaticPolicyDefinition:
    boto3_raw_data: "type_defs.UpdateStaticPolicyDefinitionTypeDef" = (
        dataclasses.field()
    )

    statement = field("statement")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateStaticPolicyDefinitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateStaticPolicyDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePolicyTemplateInput:
    boto3_raw_data: "type_defs.UpdatePolicyTemplateInputTypeDef" = dataclasses.field()

    policyStoreId = field("policyStoreId")
    policyTemplateId = field("policyTemplateId")
    statement = field("statement")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePolicyTemplateInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePolicyTemplateInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttributeValueOutput:
    boto3_raw_data: "type_defs.AttributeValueOutputTypeDef" = dataclasses.field()

    boolean = field("boolean")

    @cached_property
    def entityIdentifier(self):  # pragma: no cover
        return EntityIdentifier.make_one(self.boto3_raw_data["entityIdentifier"])

    long = field("long")
    string = field("string")
    set = field("set")
    record = field("record")
    ipaddr = field("ipaddr")
    decimal = field("decimal")
    datetime = field("datetime")
    duration = field("duration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttributeValueOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttributeValueOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttributeValue:
    boto3_raw_data: "type_defs.AttributeValueTypeDef" = dataclasses.field()

    boolean = field("boolean")

    @cached_property
    def entityIdentifier(self):  # pragma: no cover
        return EntityIdentifier.make_one(self.boto3_raw_data["entityIdentifier"])

    long = field("long")
    string = field("string")
    set = field("set")
    record = field("record")
    ipaddr = field("ipaddr")
    decimal = field("decimal")
    datetime = field("datetime")
    duration = field("duration")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AttributeValueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AttributeValueTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EntityReference:
    boto3_raw_data: "type_defs.EntityReferenceTypeDef" = dataclasses.field()

    unspecified = field("unspecified")

    @cached_property
    def identifier(self):  # pragma: no cover
        return EntityIdentifier.make_one(self.boto3_raw_data["identifier"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EntityReferenceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EntityReferenceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TemplateLinkedPolicyDefinitionDetail:
    boto3_raw_data: "type_defs.TemplateLinkedPolicyDefinitionDetailTypeDef" = (
        dataclasses.field()
    )

    policyTemplateId = field("policyTemplateId")

    @cached_property
    def principal(self):  # pragma: no cover
        return EntityIdentifier.make_one(self.boto3_raw_data["principal"])

    @cached_property
    def resource(self):  # pragma: no cover
        return EntityIdentifier.make_one(self.boto3_raw_data["resource"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TemplateLinkedPolicyDefinitionDetailTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TemplateLinkedPolicyDefinitionDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TemplateLinkedPolicyDefinitionItem:
    boto3_raw_data: "type_defs.TemplateLinkedPolicyDefinitionItemTypeDef" = (
        dataclasses.field()
    )

    policyTemplateId = field("policyTemplateId")

    @cached_property
    def principal(self):  # pragma: no cover
        return EntityIdentifier.make_one(self.boto3_raw_data["principal"])

    @cached_property
    def resource(self):  # pragma: no cover
        return EntityIdentifier.make_one(self.boto3_raw_data["resource"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TemplateLinkedPolicyDefinitionItemTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TemplateLinkedPolicyDefinitionItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TemplateLinkedPolicyDefinition:
    boto3_raw_data: "type_defs.TemplateLinkedPolicyDefinitionTypeDef" = (
        dataclasses.field()
    )

    policyTemplateId = field("policyTemplateId")

    @cached_property
    def principal(self):  # pragma: no cover
        return EntityIdentifier.make_one(self.boto3_raw_data["principal"])

    @cached_property
    def resource(self):  # pragma: no cover
        return EntityIdentifier.make_one(self.boto3_raw_data["resource"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TemplateLinkedPolicyDefinitionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TemplateLinkedPolicyDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetPolicyInput:
    boto3_raw_data: "type_defs.BatchGetPolicyInputTypeDef" = dataclasses.field()

    @cached_property
    def requests(self):  # pragma: no cover
        return BatchGetPolicyInputItem.make_many(self.boto3_raw_data["requests"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetPolicyInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetPolicyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateIdentitySourceOutput:
    boto3_raw_data: "type_defs.CreateIdentitySourceOutputTypeDef" = dataclasses.field()

    createdDate = field("createdDate")
    identitySourceId = field("identitySourceId")
    lastUpdatedDate = field("lastUpdatedDate")
    policyStoreId = field("policyStoreId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateIdentitySourceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateIdentitySourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePolicyOutput:
    boto3_raw_data: "type_defs.CreatePolicyOutputTypeDef" = dataclasses.field()

    policyStoreId = field("policyStoreId")
    policyId = field("policyId")
    policyType = field("policyType")

    @cached_property
    def principal(self):  # pragma: no cover
        return EntityIdentifier.make_one(self.boto3_raw_data["principal"])

    @cached_property
    def resource(self):  # pragma: no cover
        return EntityIdentifier.make_one(self.boto3_raw_data["resource"])

    @cached_property
    def actions(self):  # pragma: no cover
        return ActionIdentifier.make_many(self.boto3_raw_data["actions"])

    createdDate = field("createdDate")
    lastUpdatedDate = field("lastUpdatedDate")
    effect = field("effect")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePolicyOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePolicyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePolicyStoreOutput:
    boto3_raw_data: "type_defs.CreatePolicyStoreOutputTypeDef" = dataclasses.field()

    policyStoreId = field("policyStoreId")
    arn = field("arn")
    createdDate = field("createdDate")
    lastUpdatedDate = field("lastUpdatedDate")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePolicyStoreOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePolicyStoreOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePolicyTemplateOutput:
    boto3_raw_data: "type_defs.CreatePolicyTemplateOutputTypeDef" = dataclasses.field()

    policyStoreId = field("policyStoreId")
    policyTemplateId = field("policyTemplateId")
    createdDate = field("createdDate")
    lastUpdatedDate = field("lastUpdatedDate")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePolicyTemplateOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePolicyTemplateOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPolicyTemplateOutput:
    boto3_raw_data: "type_defs.GetPolicyTemplateOutputTypeDef" = dataclasses.field()

    policyStoreId = field("policyStoreId")
    policyTemplateId = field("policyTemplateId")
    description = field("description")
    statement = field("statement")
    createdDate = field("createdDate")
    lastUpdatedDate = field("lastUpdatedDate")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPolicyTemplateOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPolicyTemplateOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSchemaOutput:
    boto3_raw_data: "type_defs.GetSchemaOutputTypeDef" = dataclasses.field()

    policyStoreId = field("policyStoreId")
    schema = field("schema")
    createdDate = field("createdDate")
    lastUpdatedDate = field("lastUpdatedDate")
    namespaces = field("namespaces")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetSchemaOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetSchemaOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceOutput:
    boto3_raw_data: "type_defs.ListTagsForResourceOutputTypeDef" = dataclasses.field()

    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutSchemaOutput:
    boto3_raw_data: "type_defs.PutSchemaOutputTypeDef" = dataclasses.field()

    policyStoreId = field("policyStoreId")
    namespaces = field("namespaces")
    createdDate = field("createdDate")
    lastUpdatedDate = field("lastUpdatedDate")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutSchemaOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PutSchemaOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateIdentitySourceOutput:
    boto3_raw_data: "type_defs.UpdateIdentitySourceOutputTypeDef" = dataclasses.field()

    createdDate = field("createdDate")
    identitySourceId = field("identitySourceId")
    lastUpdatedDate = field("lastUpdatedDate")
    policyStoreId = field("policyStoreId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateIdentitySourceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateIdentitySourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePolicyOutput:
    boto3_raw_data: "type_defs.UpdatePolicyOutputTypeDef" = dataclasses.field()

    policyStoreId = field("policyStoreId")
    policyId = field("policyId")
    policyType = field("policyType")

    @cached_property
    def principal(self):  # pragma: no cover
        return EntityIdentifier.make_one(self.boto3_raw_data["principal"])

    @cached_property
    def resource(self):  # pragma: no cover
        return EntityIdentifier.make_one(self.boto3_raw_data["resource"])

    @cached_property
    def actions(self):  # pragma: no cover
        return ActionIdentifier.make_many(self.boto3_raw_data["actions"])

    createdDate = field("createdDate")
    lastUpdatedDate = field("lastUpdatedDate")
    effect = field("effect")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePolicyOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePolicyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePolicyStoreOutput:
    boto3_raw_data: "type_defs.UpdatePolicyStoreOutputTypeDef" = dataclasses.field()

    policyStoreId = field("policyStoreId")
    arn = field("arn")
    createdDate = field("createdDate")
    lastUpdatedDate = field("lastUpdatedDate")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePolicyStoreOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePolicyStoreOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePolicyTemplateOutput:
    boto3_raw_data: "type_defs.UpdatePolicyTemplateOutputTypeDef" = dataclasses.field()

    policyStoreId = field("policyStoreId")
    policyTemplateId = field("policyTemplateId")
    createdDate = field("createdDate")
    lastUpdatedDate = field("lastUpdatedDate")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePolicyTemplateOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePolicyTemplateOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IsAuthorizedOutput:
    boto3_raw_data: "type_defs.IsAuthorizedOutputTypeDef" = dataclasses.field()

    decision = field("decision")

    @cached_property
    def determiningPolicies(self):  # pragma: no cover
        return DeterminingPolicyItem.make_many(
            self.boto3_raw_data["determiningPolicies"]
        )

    @cached_property
    def errors(self):  # pragma: no cover
        return EvaluationErrorItem.make_many(self.boto3_raw_data["errors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IsAuthorizedOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IsAuthorizedOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IsAuthorizedWithTokenOutput:
    boto3_raw_data: "type_defs.IsAuthorizedWithTokenOutputTypeDef" = dataclasses.field()

    decision = field("decision")

    @cached_property
    def determiningPolicies(self):  # pragma: no cover
        return DeterminingPolicyItem.make_many(
            self.boto3_raw_data["determiningPolicies"]
        )

    @cached_property
    def errors(self):  # pragma: no cover
        return EvaluationErrorItem.make_many(self.boto3_raw_data["errors"])

    @cached_property
    def principal(self):  # pragma: no cover
        return EntityIdentifier.make_one(self.boto3_raw_data["principal"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IsAuthorizedWithTokenOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IsAuthorizedWithTokenOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CognitoUserPoolConfigurationDetail:
    boto3_raw_data: "type_defs.CognitoUserPoolConfigurationDetailTypeDef" = (
        dataclasses.field()
    )

    userPoolArn = field("userPoolArn")
    clientIds = field("clientIds")
    issuer = field("issuer")

    @cached_property
    def groupConfiguration(self):  # pragma: no cover
        return CognitoGroupConfigurationDetail.make_one(
            self.boto3_raw_data["groupConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CognitoUserPoolConfigurationDetailTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CognitoUserPoolConfigurationDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CognitoUserPoolConfigurationItem:
    boto3_raw_data: "type_defs.CognitoUserPoolConfigurationItemTypeDef" = (
        dataclasses.field()
    )

    userPoolArn = field("userPoolArn")
    clientIds = field("clientIds")
    issuer = field("issuer")

    @cached_property
    def groupConfiguration(self):  # pragma: no cover
        return CognitoGroupConfigurationItem.make_one(
            self.boto3_raw_data["groupConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CognitoUserPoolConfigurationItemTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CognitoUserPoolConfigurationItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CognitoUserPoolConfiguration:
    boto3_raw_data: "type_defs.CognitoUserPoolConfigurationTypeDef" = (
        dataclasses.field()
    )

    userPoolArn = field("userPoolArn")
    clientIds = field("clientIds")

    @cached_property
    def groupConfiguration(self):  # pragma: no cover
        return CognitoGroupConfiguration.make_one(
            self.boto3_raw_data["groupConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CognitoUserPoolConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CognitoUserPoolConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePolicyStoreInput:
    boto3_raw_data: "type_defs.CreatePolicyStoreInputTypeDef" = dataclasses.field()

    @cached_property
    def validationSettings(self):  # pragma: no cover
        return ValidationSettings.make_one(self.boto3_raw_data["validationSettings"])

    clientToken = field("clientToken")
    description = field("description")
    deletionProtection = field("deletionProtection")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePolicyStoreInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePolicyStoreInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPolicyStoreOutput:
    boto3_raw_data: "type_defs.GetPolicyStoreOutputTypeDef" = dataclasses.field()

    policyStoreId = field("policyStoreId")
    arn = field("arn")

    @cached_property
    def validationSettings(self):  # pragma: no cover
        return ValidationSettings.make_one(self.boto3_raw_data["validationSettings"])

    createdDate = field("createdDate")
    lastUpdatedDate = field("lastUpdatedDate")
    description = field("description")
    deletionProtection = field("deletionProtection")
    cedarVersion = field("cedarVersion")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPolicyStoreOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPolicyStoreOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePolicyStoreInput:
    boto3_raw_data: "type_defs.UpdatePolicyStoreInputTypeDef" = dataclasses.field()

    policyStoreId = field("policyStoreId")

    @cached_property
    def validationSettings(self):  # pragma: no cover
        return ValidationSettings.make_one(self.boto3_raw_data["validationSettings"])

    deletionProtection = field("deletionProtection")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePolicyStoreInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePolicyStoreInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIdentitySourcesInput:
    boto3_raw_data: "type_defs.ListIdentitySourcesInputTypeDef" = dataclasses.field()

    policyStoreId = field("policyStoreId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @cached_property
    def filters(self):  # pragma: no cover
        return IdentitySourceFilter.make_many(self.boto3_raw_data["filters"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIdentitySourcesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIdentitySourcesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIdentitySourcesInputPaginate:
    boto3_raw_data: "type_defs.ListIdentitySourcesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    policyStoreId = field("policyStoreId")

    @cached_property
    def filters(self):  # pragma: no cover
        return IdentitySourceFilter.make_many(self.boto3_raw_data["filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListIdentitySourcesInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIdentitySourcesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPolicyStoresInputPaginate:
    boto3_raw_data: "type_defs.ListPolicyStoresInputPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListPolicyStoresInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPolicyStoresInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPolicyTemplatesInputPaginate:
    boto3_raw_data: "type_defs.ListPolicyTemplatesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    policyStoreId = field("policyStoreId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListPolicyTemplatesInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPolicyTemplatesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPolicyStoresOutput:
    boto3_raw_data: "type_defs.ListPolicyStoresOutputTypeDef" = dataclasses.field()

    @cached_property
    def policyStores(self):  # pragma: no cover
        return PolicyStoreItem.make_many(self.boto3_raw_data["policyStores"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPolicyStoresOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPolicyStoresOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPolicyTemplatesOutput:
    boto3_raw_data: "type_defs.ListPolicyTemplatesOutputTypeDef" = dataclasses.field()

    @cached_property
    def policyTemplates(self):  # pragma: no cover
        return PolicyTemplateItem.make_many(self.boto3_raw_data["policyTemplates"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPolicyTemplatesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPolicyTemplatesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenIdConnectTokenSelectionDetail:
    boto3_raw_data: "type_defs.OpenIdConnectTokenSelectionDetailTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def accessTokenOnly(self):  # pragma: no cover
        return OpenIdConnectAccessTokenConfigurationDetail.make_one(
            self.boto3_raw_data["accessTokenOnly"]
        )

    @cached_property
    def identityTokenOnly(self):  # pragma: no cover
        return OpenIdConnectIdentityTokenConfigurationDetail.make_one(
            self.boto3_raw_data["identityTokenOnly"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OpenIdConnectTokenSelectionDetailTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpenIdConnectTokenSelectionDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenIdConnectTokenSelectionItem:
    boto3_raw_data: "type_defs.OpenIdConnectTokenSelectionItemTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def accessTokenOnly(self):  # pragma: no cover
        return OpenIdConnectAccessTokenConfigurationItem.make_one(
            self.boto3_raw_data["accessTokenOnly"]
        )

    @cached_property
    def identityTokenOnly(self):  # pragma: no cover
        return OpenIdConnectIdentityTokenConfigurationItem.make_one(
            self.boto3_raw_data["identityTokenOnly"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.OpenIdConnectTokenSelectionItemTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpenIdConnectTokenSelectionItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenIdConnectTokenSelection:
    boto3_raw_data: "type_defs.OpenIdConnectTokenSelectionTypeDef" = dataclasses.field()

    @cached_property
    def accessTokenOnly(self):  # pragma: no cover
        return OpenIdConnectAccessTokenConfiguration.make_one(
            self.boto3_raw_data["accessTokenOnly"]
        )

    @cached_property
    def identityTokenOnly(self):  # pragma: no cover
        return OpenIdConnectIdentityTokenConfiguration.make_one(
            self.boto3_raw_data["identityTokenOnly"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OpenIdConnectTokenSelectionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpenIdConnectTokenSelectionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutSchemaInput:
    boto3_raw_data: "type_defs.PutSchemaInputTypeDef" = dataclasses.field()

    policyStoreId = field("policyStoreId")

    @cached_property
    def definition(self):  # pragma: no cover
        return SchemaDefinition.make_one(self.boto3_raw_data["definition"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutSchemaInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PutSchemaInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCognitoUserPoolConfiguration:
    boto3_raw_data: "type_defs.UpdateCognitoUserPoolConfigurationTypeDef" = (
        dataclasses.field()
    )

    userPoolArn = field("userPoolArn")
    clientIds = field("clientIds")

    @cached_property
    def groupConfiguration(self):  # pragma: no cover
        return UpdateCognitoGroupConfiguration.make_one(
            self.boto3_raw_data["groupConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateCognitoUserPoolConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCognitoUserPoolConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateOpenIdConnectTokenSelection:
    boto3_raw_data: "type_defs.UpdateOpenIdConnectTokenSelectionTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def accessTokenOnly(self):  # pragma: no cover
        return UpdateOpenIdConnectAccessTokenConfiguration.make_one(
            self.boto3_raw_data["accessTokenOnly"]
        )

    @cached_property
    def identityTokenOnly(self):  # pragma: no cover
        return UpdateOpenIdConnectIdentityTokenConfiguration.make_one(
            self.boto3_raw_data["identityTokenOnly"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateOpenIdConnectTokenSelectionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateOpenIdConnectTokenSelectionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePolicyDefinition:
    boto3_raw_data: "type_defs.UpdatePolicyDefinitionTypeDef" = dataclasses.field()

    @cached_property
    def static(self):  # pragma: no cover
        return UpdateStaticPolicyDefinition.make_one(self.boto3_raw_data["static"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePolicyDefinitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePolicyDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContextDefinitionOutput:
    boto3_raw_data: "type_defs.ContextDefinitionOutputTypeDef" = dataclasses.field()

    contextMap = field("contextMap")
    cedarJson = field("cedarJson")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContextDefinitionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContextDefinitionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolicyFilter:
    boto3_raw_data: "type_defs.PolicyFilterTypeDef" = dataclasses.field()

    @cached_property
    def principal(self):  # pragma: no cover
        return EntityReference.make_one(self.boto3_raw_data["principal"])

    @cached_property
    def resource(self):  # pragma: no cover
        return EntityReference.make_one(self.boto3_raw_data["resource"])

    policyType = field("policyType")
    policyTemplateId = field("policyTemplateId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PolicyFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PolicyFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolicyDefinitionDetail:
    boto3_raw_data: "type_defs.PolicyDefinitionDetailTypeDef" = dataclasses.field()

    @cached_property
    def static(self):  # pragma: no cover
        return StaticPolicyDefinitionDetail.make_one(self.boto3_raw_data["static"])

    @cached_property
    def templateLinked(self):  # pragma: no cover
        return TemplateLinkedPolicyDefinitionDetail.make_one(
            self.boto3_raw_data["templateLinked"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PolicyDefinitionDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PolicyDefinitionDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolicyDefinitionItem:
    boto3_raw_data: "type_defs.PolicyDefinitionItemTypeDef" = dataclasses.field()

    @cached_property
    def static(self):  # pragma: no cover
        return StaticPolicyDefinitionItem.make_one(self.boto3_raw_data["static"])

    @cached_property
    def templateLinked(self):  # pragma: no cover
        return TemplateLinkedPolicyDefinitionItem.make_one(
            self.boto3_raw_data["templateLinked"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PolicyDefinitionItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PolicyDefinitionItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolicyDefinition:
    boto3_raw_data: "type_defs.PolicyDefinitionTypeDef" = dataclasses.field()

    @cached_property
    def static(self):  # pragma: no cover
        return StaticPolicyDefinition.make_one(self.boto3_raw_data["static"])

    @cached_property
    def templateLinked(self):  # pragma: no cover
        return TemplateLinkedPolicyDefinition.make_one(
            self.boto3_raw_data["templateLinked"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PolicyDefinitionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PolicyDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenIdConnectConfigurationDetail:
    boto3_raw_data: "type_defs.OpenIdConnectConfigurationDetailTypeDef" = (
        dataclasses.field()
    )

    issuer = field("issuer")

    @cached_property
    def tokenSelection(self):  # pragma: no cover
        return OpenIdConnectTokenSelectionDetail.make_one(
            self.boto3_raw_data["tokenSelection"]
        )

    entityIdPrefix = field("entityIdPrefix")

    @cached_property
    def groupConfiguration(self):  # pragma: no cover
        return OpenIdConnectGroupConfigurationDetail.make_one(
            self.boto3_raw_data["groupConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.OpenIdConnectConfigurationDetailTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpenIdConnectConfigurationDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenIdConnectConfigurationItem:
    boto3_raw_data: "type_defs.OpenIdConnectConfigurationItemTypeDef" = (
        dataclasses.field()
    )

    issuer = field("issuer")

    @cached_property
    def tokenSelection(self):  # pragma: no cover
        return OpenIdConnectTokenSelectionItem.make_one(
            self.boto3_raw_data["tokenSelection"]
        )

    entityIdPrefix = field("entityIdPrefix")

    @cached_property
    def groupConfiguration(self):  # pragma: no cover
        return OpenIdConnectGroupConfigurationItem.make_one(
            self.boto3_raw_data["groupConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.OpenIdConnectConfigurationItemTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpenIdConnectConfigurationItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenIdConnectConfiguration:
    boto3_raw_data: "type_defs.OpenIdConnectConfigurationTypeDef" = dataclasses.field()

    issuer = field("issuer")

    @cached_property
    def tokenSelection(self):  # pragma: no cover
        return OpenIdConnectTokenSelection.make_one(
            self.boto3_raw_data["tokenSelection"]
        )

    entityIdPrefix = field("entityIdPrefix")

    @cached_property
    def groupConfiguration(self):  # pragma: no cover
        return OpenIdConnectGroupConfiguration.make_one(
            self.boto3_raw_data["groupConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OpenIdConnectConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpenIdConnectConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateOpenIdConnectConfiguration:
    boto3_raw_data: "type_defs.UpdateOpenIdConnectConfigurationTypeDef" = (
        dataclasses.field()
    )

    issuer = field("issuer")

    @cached_property
    def tokenSelection(self):  # pragma: no cover
        return UpdateOpenIdConnectTokenSelection.make_one(
            self.boto3_raw_data["tokenSelection"]
        )

    entityIdPrefix = field("entityIdPrefix")

    @cached_property
    def groupConfiguration(self):  # pragma: no cover
        return UpdateOpenIdConnectGroupConfiguration.make_one(
            self.boto3_raw_data["groupConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateOpenIdConnectConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateOpenIdConnectConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePolicyInput:
    boto3_raw_data: "type_defs.UpdatePolicyInputTypeDef" = dataclasses.field()

    policyStoreId = field("policyStoreId")
    policyId = field("policyId")

    @cached_property
    def definition(self):  # pragma: no cover
        return UpdatePolicyDefinition.make_one(self.boto3_raw_data["definition"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdatePolicyInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePolicyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchIsAuthorizedInputItemOutput:
    boto3_raw_data: "type_defs.BatchIsAuthorizedInputItemOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def principal(self):  # pragma: no cover
        return EntityIdentifier.make_one(self.boto3_raw_data["principal"])

    @cached_property
    def action(self):  # pragma: no cover
        return ActionIdentifier.make_one(self.boto3_raw_data["action"])

    @cached_property
    def resource(self):  # pragma: no cover
        return EntityIdentifier.make_one(self.boto3_raw_data["resource"])

    @cached_property
    def context(self):  # pragma: no cover
        return ContextDefinitionOutput.make_one(self.boto3_raw_data["context"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchIsAuthorizedInputItemOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchIsAuthorizedInputItemOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchIsAuthorizedWithTokenInputItemOutput:
    boto3_raw_data: "type_defs.BatchIsAuthorizedWithTokenInputItemOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def action(self):  # pragma: no cover
        return ActionIdentifier.make_one(self.boto3_raw_data["action"])

    @cached_property
    def resource(self):  # pragma: no cover
        return EntityIdentifier.make_one(self.boto3_raw_data["resource"])

    @cached_property
    def context(self):  # pragma: no cover
        return ContextDefinitionOutput.make_one(self.boto3_raw_data["context"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchIsAuthorizedWithTokenInputItemOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchIsAuthorizedWithTokenInputItemOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContextDefinition:
    boto3_raw_data: "type_defs.ContextDefinitionTypeDef" = dataclasses.field()

    contextMap = field("contextMap")
    cedarJson = field("cedarJson")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContextDefinitionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContextDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EntityItem:
    boto3_raw_data: "type_defs.EntityItemTypeDef" = dataclasses.field()

    @cached_property
    def identifier(self):  # pragma: no cover
        return EntityIdentifier.make_one(self.boto3_raw_data["identifier"])

    attributes = field("attributes")

    @cached_property
    def parents(self):  # pragma: no cover
        return EntityIdentifier.make_many(self.boto3_raw_data["parents"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EntityItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EntityItemTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPoliciesInputPaginate:
    boto3_raw_data: "type_defs.ListPoliciesInputPaginateTypeDef" = dataclasses.field()

    policyStoreId = field("policyStoreId")

    @cached_property
    def filter(self):  # pragma: no cover
        return PolicyFilter.make_one(self.boto3_raw_data["filter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPoliciesInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPoliciesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPoliciesInput:
    boto3_raw_data: "type_defs.ListPoliciesInputTypeDef" = dataclasses.field()

    policyStoreId = field("policyStoreId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @cached_property
    def filter(self):  # pragma: no cover
        return PolicyFilter.make_one(self.boto3_raw_data["filter"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListPoliciesInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPoliciesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetPolicyOutputItem:
    boto3_raw_data: "type_defs.BatchGetPolicyOutputItemTypeDef" = dataclasses.field()

    policyStoreId = field("policyStoreId")
    policyId = field("policyId")
    policyType = field("policyType")

    @cached_property
    def definition(self):  # pragma: no cover
        return PolicyDefinitionDetail.make_one(self.boto3_raw_data["definition"])

    createdDate = field("createdDate")
    lastUpdatedDate = field("lastUpdatedDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetPolicyOutputItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetPolicyOutputItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPolicyOutput:
    boto3_raw_data: "type_defs.GetPolicyOutputTypeDef" = dataclasses.field()

    policyStoreId = field("policyStoreId")
    policyId = field("policyId")
    policyType = field("policyType")

    @cached_property
    def principal(self):  # pragma: no cover
        return EntityIdentifier.make_one(self.boto3_raw_data["principal"])

    @cached_property
    def resource(self):  # pragma: no cover
        return EntityIdentifier.make_one(self.boto3_raw_data["resource"])

    @cached_property
    def actions(self):  # pragma: no cover
        return ActionIdentifier.make_many(self.boto3_raw_data["actions"])

    @cached_property
    def definition(self):  # pragma: no cover
        return PolicyDefinitionDetail.make_one(self.boto3_raw_data["definition"])

    createdDate = field("createdDate")
    lastUpdatedDate = field("lastUpdatedDate")
    effect = field("effect")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetPolicyOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetPolicyOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolicyItem:
    boto3_raw_data: "type_defs.PolicyItemTypeDef" = dataclasses.field()

    policyStoreId = field("policyStoreId")
    policyId = field("policyId")
    policyType = field("policyType")

    @cached_property
    def definition(self):  # pragma: no cover
        return PolicyDefinitionItem.make_one(self.boto3_raw_data["definition"])

    createdDate = field("createdDate")
    lastUpdatedDate = field("lastUpdatedDate")

    @cached_property
    def principal(self):  # pragma: no cover
        return EntityIdentifier.make_one(self.boto3_raw_data["principal"])

    @cached_property
    def resource(self):  # pragma: no cover
        return EntityIdentifier.make_one(self.boto3_raw_data["resource"])

    @cached_property
    def actions(self):  # pragma: no cover
        return ActionIdentifier.make_many(self.boto3_raw_data["actions"])

    effect = field("effect")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PolicyItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PolicyItemTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePolicyInput:
    boto3_raw_data: "type_defs.CreatePolicyInputTypeDef" = dataclasses.field()

    policyStoreId = field("policyStoreId")

    @cached_property
    def definition(self):  # pragma: no cover
        return PolicyDefinition.make_one(self.boto3_raw_data["definition"])

    clientToken = field("clientToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreatePolicyInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePolicyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigurationDetail:
    boto3_raw_data: "type_defs.ConfigurationDetailTypeDef" = dataclasses.field()

    @cached_property
    def cognitoUserPoolConfiguration(self):  # pragma: no cover
        return CognitoUserPoolConfigurationDetail.make_one(
            self.boto3_raw_data["cognitoUserPoolConfiguration"]
        )

    @cached_property
    def openIdConnectConfiguration(self):  # pragma: no cover
        return OpenIdConnectConfigurationDetail.make_one(
            self.boto3_raw_data["openIdConnectConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfigurationDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigurationDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigurationItem:
    boto3_raw_data: "type_defs.ConfigurationItemTypeDef" = dataclasses.field()

    @cached_property
    def cognitoUserPoolConfiguration(self):  # pragma: no cover
        return CognitoUserPoolConfigurationItem.make_one(
            self.boto3_raw_data["cognitoUserPoolConfiguration"]
        )

    @cached_property
    def openIdConnectConfiguration(self):  # pragma: no cover
        return OpenIdConnectConfigurationItem.make_one(
            self.boto3_raw_data["openIdConnectConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConfigurationItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigurationItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Configuration:
    boto3_raw_data: "type_defs.ConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def cognitoUserPoolConfiguration(self):  # pragma: no cover
        return CognitoUserPoolConfiguration.make_one(
            self.boto3_raw_data["cognitoUserPoolConfiguration"]
        )

    @cached_property
    def openIdConnectConfiguration(self):  # pragma: no cover
        return OpenIdConnectConfiguration.make_one(
            self.boto3_raw_data["openIdConnectConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConfigurationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateConfiguration:
    boto3_raw_data: "type_defs.UpdateConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def cognitoUserPoolConfiguration(self):  # pragma: no cover
        return UpdateCognitoUserPoolConfiguration.make_one(
            self.boto3_raw_data["cognitoUserPoolConfiguration"]
        )

    @cached_property
    def openIdConnectConfiguration(self):  # pragma: no cover
        return UpdateOpenIdConnectConfiguration.make_one(
            self.boto3_raw_data["openIdConnectConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchIsAuthorizedOutputItem:
    boto3_raw_data: "type_defs.BatchIsAuthorizedOutputItemTypeDef" = dataclasses.field()

    @cached_property
    def request(self):  # pragma: no cover
        return BatchIsAuthorizedInputItemOutput.make_one(self.boto3_raw_data["request"])

    decision = field("decision")

    @cached_property
    def determiningPolicies(self):  # pragma: no cover
        return DeterminingPolicyItem.make_many(
            self.boto3_raw_data["determiningPolicies"]
        )

    @cached_property
    def errors(self):  # pragma: no cover
        return EvaluationErrorItem.make_many(self.boto3_raw_data["errors"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchIsAuthorizedOutputItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchIsAuthorizedOutputItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchIsAuthorizedWithTokenOutputItem:
    boto3_raw_data: "type_defs.BatchIsAuthorizedWithTokenOutputItemTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def request(self):  # pragma: no cover
        return BatchIsAuthorizedWithTokenInputItemOutput.make_one(
            self.boto3_raw_data["request"]
        )

    decision = field("decision")

    @cached_property
    def determiningPolicies(self):  # pragma: no cover
        return DeterminingPolicyItem.make_many(
            self.boto3_raw_data["determiningPolicies"]
        )

    @cached_property
    def errors(self):  # pragma: no cover
        return EvaluationErrorItem.make_many(self.boto3_raw_data["errors"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchIsAuthorizedWithTokenOutputItemTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchIsAuthorizedWithTokenOutputItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EntitiesDefinition:
    boto3_raw_data: "type_defs.EntitiesDefinitionTypeDef" = dataclasses.field()

    @cached_property
    def entityList(self):  # pragma: no cover
        return EntityItem.make_many(self.boto3_raw_data["entityList"])

    cedarJson = field("cedarJson")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EntitiesDefinitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EntitiesDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetPolicyOutput:
    boto3_raw_data: "type_defs.BatchGetPolicyOutputTypeDef" = dataclasses.field()

    @cached_property
    def results(self):  # pragma: no cover
        return BatchGetPolicyOutputItem.make_many(self.boto3_raw_data["results"])

    @cached_property
    def errors(self):  # pragma: no cover
        return BatchGetPolicyErrorItem.make_many(self.boto3_raw_data["errors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetPolicyOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetPolicyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPoliciesOutput:
    boto3_raw_data: "type_defs.ListPoliciesOutputTypeDef" = dataclasses.field()

    @cached_property
    def policies(self):  # pragma: no cover
        return PolicyItem.make_many(self.boto3_raw_data["policies"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPoliciesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPoliciesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIdentitySourceOutput:
    boto3_raw_data: "type_defs.GetIdentitySourceOutputTypeDef" = dataclasses.field()

    createdDate = field("createdDate")

    @cached_property
    def details(self):  # pragma: no cover
        return IdentitySourceDetails.make_one(self.boto3_raw_data["details"])

    identitySourceId = field("identitySourceId")
    lastUpdatedDate = field("lastUpdatedDate")
    policyStoreId = field("policyStoreId")
    principalEntityType = field("principalEntityType")

    @cached_property
    def configuration(self):  # pragma: no cover
        return ConfigurationDetail.make_one(self.boto3_raw_data["configuration"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetIdentitySourceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIdentitySourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdentitySourceItem:
    boto3_raw_data: "type_defs.IdentitySourceItemTypeDef" = dataclasses.field()

    createdDate = field("createdDate")
    identitySourceId = field("identitySourceId")
    lastUpdatedDate = field("lastUpdatedDate")
    policyStoreId = field("policyStoreId")
    principalEntityType = field("principalEntityType")

    @cached_property
    def details(self):  # pragma: no cover
        return IdentitySourceItemDetails.make_one(self.boto3_raw_data["details"])

    @cached_property
    def configuration(self):  # pragma: no cover
        return ConfigurationItem.make_one(self.boto3_raw_data["configuration"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IdentitySourceItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdentitySourceItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateIdentitySourceInput:
    boto3_raw_data: "type_defs.CreateIdentitySourceInputTypeDef" = dataclasses.field()

    policyStoreId = field("policyStoreId")

    @cached_property
    def configuration(self):  # pragma: no cover
        return Configuration.make_one(self.boto3_raw_data["configuration"])

    clientToken = field("clientToken")
    principalEntityType = field("principalEntityType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateIdentitySourceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateIdentitySourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateIdentitySourceInput:
    boto3_raw_data: "type_defs.UpdateIdentitySourceInputTypeDef" = dataclasses.field()

    policyStoreId = field("policyStoreId")
    identitySourceId = field("identitySourceId")

    @cached_property
    def updateConfiguration(self):  # pragma: no cover
        return UpdateConfiguration.make_one(self.boto3_raw_data["updateConfiguration"])

    principalEntityType = field("principalEntityType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateIdentitySourceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateIdentitySourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchIsAuthorizedOutput:
    boto3_raw_data: "type_defs.BatchIsAuthorizedOutputTypeDef" = dataclasses.field()

    @cached_property
    def results(self):  # pragma: no cover
        return BatchIsAuthorizedOutputItem.make_many(self.boto3_raw_data["results"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchIsAuthorizedOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchIsAuthorizedOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchIsAuthorizedWithTokenOutput:
    boto3_raw_data: "type_defs.BatchIsAuthorizedWithTokenOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def principal(self):  # pragma: no cover
        return EntityIdentifier.make_one(self.boto3_raw_data["principal"])

    @cached_property
    def results(self):  # pragma: no cover
        return BatchIsAuthorizedWithTokenOutputItem.make_many(
            self.boto3_raw_data["results"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchIsAuthorizedWithTokenOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchIsAuthorizedWithTokenOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchIsAuthorizedInputItem:
    boto3_raw_data: "type_defs.BatchIsAuthorizedInputItemTypeDef" = dataclasses.field()

    @cached_property
    def principal(self):  # pragma: no cover
        return EntityIdentifier.make_one(self.boto3_raw_data["principal"])

    @cached_property
    def action(self):  # pragma: no cover
        return ActionIdentifier.make_one(self.boto3_raw_data["action"])

    @cached_property
    def resource(self):  # pragma: no cover
        return EntityIdentifier.make_one(self.boto3_raw_data["resource"])

    context = field("context")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchIsAuthorizedInputItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchIsAuthorizedInputItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchIsAuthorizedWithTokenInputItem:
    boto3_raw_data: "type_defs.BatchIsAuthorizedWithTokenInputItemTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def action(self):  # pragma: no cover
        return ActionIdentifier.make_one(self.boto3_raw_data["action"])

    @cached_property
    def resource(self):  # pragma: no cover
        return EntityIdentifier.make_one(self.boto3_raw_data["resource"])

    context = field("context")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchIsAuthorizedWithTokenInputItemTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchIsAuthorizedWithTokenInputItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IsAuthorizedInput:
    boto3_raw_data: "type_defs.IsAuthorizedInputTypeDef" = dataclasses.field()

    policyStoreId = field("policyStoreId")

    @cached_property
    def principal(self):  # pragma: no cover
        return EntityIdentifier.make_one(self.boto3_raw_data["principal"])

    @cached_property
    def action(self):  # pragma: no cover
        return ActionIdentifier.make_one(self.boto3_raw_data["action"])

    @cached_property
    def resource(self):  # pragma: no cover
        return EntityIdentifier.make_one(self.boto3_raw_data["resource"])

    context = field("context")

    @cached_property
    def entities(self):  # pragma: no cover
        return EntitiesDefinition.make_one(self.boto3_raw_data["entities"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IsAuthorizedInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IsAuthorizedInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IsAuthorizedWithTokenInput:
    boto3_raw_data: "type_defs.IsAuthorizedWithTokenInputTypeDef" = dataclasses.field()

    policyStoreId = field("policyStoreId")
    identityToken = field("identityToken")
    accessToken = field("accessToken")

    @cached_property
    def action(self):  # pragma: no cover
        return ActionIdentifier.make_one(self.boto3_raw_data["action"])

    @cached_property
    def resource(self):  # pragma: no cover
        return EntityIdentifier.make_one(self.boto3_raw_data["resource"])

    context = field("context")

    @cached_property
    def entities(self):  # pragma: no cover
        return EntitiesDefinition.make_one(self.boto3_raw_data["entities"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IsAuthorizedWithTokenInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IsAuthorizedWithTokenInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIdentitySourcesOutput:
    boto3_raw_data: "type_defs.ListIdentitySourcesOutputTypeDef" = dataclasses.field()

    @cached_property
    def identitySources(self):  # pragma: no cover
        return IdentitySourceItem.make_many(self.boto3_raw_data["identitySources"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIdentitySourcesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIdentitySourcesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchIsAuthorizedInput:
    boto3_raw_data: "type_defs.BatchIsAuthorizedInputTypeDef" = dataclasses.field()

    policyStoreId = field("policyStoreId")
    requests = field("requests")

    @cached_property
    def entities(self):  # pragma: no cover
        return EntitiesDefinition.make_one(self.boto3_raw_data["entities"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchIsAuthorizedInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchIsAuthorizedInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchIsAuthorizedWithTokenInput:
    boto3_raw_data: "type_defs.BatchIsAuthorizedWithTokenInputTypeDef" = (
        dataclasses.field()
    )

    policyStoreId = field("policyStoreId")
    requests = field("requests")
    identityToken = field("identityToken")
    accessToken = field("accessToken")

    @cached_property
    def entities(self):  # pragma: no cover
        return EntitiesDefinition.make_one(self.boto3_raw_data["entities"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchIsAuthorizedWithTokenInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchIsAuthorizedWithTokenInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]

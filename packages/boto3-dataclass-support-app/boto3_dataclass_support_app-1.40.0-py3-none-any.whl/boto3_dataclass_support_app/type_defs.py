# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_support_app import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class CreateSlackChannelConfigurationRequest:
    boto3_raw_data: "type_defs.CreateSlackChannelConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    channelId = field("channelId")
    channelRoleArn = field("channelRoleArn")
    notifyOnCaseSeverity = field("notifyOnCaseSeverity")
    teamId = field("teamId")
    channelName = field("channelName")
    notifyOnAddCorrespondenceToCase = field("notifyOnAddCorrespondenceToCase")
    notifyOnCreateOrReopenCase = field("notifyOnCreateOrReopenCase")
    notifyOnResolveCase = field("notifyOnResolveCase")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateSlackChannelConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSlackChannelConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSlackChannelConfigurationRequest:
    boto3_raw_data: "type_defs.DeleteSlackChannelConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    channelId = field("channelId")
    teamId = field("teamId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteSlackChannelConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSlackChannelConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSlackWorkspaceConfigurationRequest:
    boto3_raw_data: "type_defs.DeleteSlackWorkspaceConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    teamId = field("teamId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteSlackWorkspaceConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSlackWorkspaceConfigurationRequestTypeDef"]
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
class ListSlackChannelConfigurationsRequest:
    boto3_raw_data: "type_defs.ListSlackChannelConfigurationsRequestTypeDef" = (
        dataclasses.field()
    )

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSlackChannelConfigurationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSlackChannelConfigurationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SlackChannelConfiguration:
    boto3_raw_data: "type_defs.SlackChannelConfigurationTypeDef" = dataclasses.field()

    channelId = field("channelId")
    teamId = field("teamId")
    channelName = field("channelName")
    channelRoleArn = field("channelRoleArn")
    notifyOnAddCorrespondenceToCase = field("notifyOnAddCorrespondenceToCase")
    notifyOnCaseSeverity = field("notifyOnCaseSeverity")
    notifyOnCreateOrReopenCase = field("notifyOnCreateOrReopenCase")
    notifyOnResolveCase = field("notifyOnResolveCase")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SlackChannelConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SlackChannelConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSlackWorkspaceConfigurationsRequest:
    boto3_raw_data: "type_defs.ListSlackWorkspaceConfigurationsRequestTypeDef" = (
        dataclasses.field()
    )

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSlackWorkspaceConfigurationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSlackWorkspaceConfigurationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SlackWorkspaceConfiguration:
    boto3_raw_data: "type_defs.SlackWorkspaceConfigurationTypeDef" = dataclasses.field()

    teamId = field("teamId")
    allowOrganizationMemberAccount = field("allowOrganizationMemberAccount")
    teamName = field("teamName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SlackWorkspaceConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SlackWorkspaceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutAccountAliasRequest:
    boto3_raw_data: "type_defs.PutAccountAliasRequestTypeDef" = dataclasses.field()

    accountAlias = field("accountAlias")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutAccountAliasRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutAccountAliasRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterSlackWorkspaceForOrganizationRequest:
    boto3_raw_data: "type_defs.RegisterSlackWorkspaceForOrganizationRequestTypeDef" = (
        dataclasses.field()
    )

    teamId = field("teamId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RegisterSlackWorkspaceForOrganizationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterSlackWorkspaceForOrganizationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSlackChannelConfigurationRequest:
    boto3_raw_data: "type_defs.UpdateSlackChannelConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    channelId = field("channelId")
    teamId = field("teamId")
    channelName = field("channelName")
    channelRoleArn = field("channelRoleArn")
    notifyOnAddCorrespondenceToCase = field("notifyOnAddCorrespondenceToCase")
    notifyOnCaseSeverity = field("notifyOnCaseSeverity")
    notifyOnCreateOrReopenCase = field("notifyOnCreateOrReopenCase")
    notifyOnResolveCase = field("notifyOnResolveCase")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateSlackChannelConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSlackChannelConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccountAliasResult:
    boto3_raw_data: "type_defs.GetAccountAliasResultTypeDef" = dataclasses.field()

    accountAlias = field("accountAlias")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAccountAliasResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccountAliasResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterSlackWorkspaceForOrganizationResult:
    boto3_raw_data: "type_defs.RegisterSlackWorkspaceForOrganizationResultTypeDef" = (
        dataclasses.field()
    )

    accountType = field("accountType")
    teamId = field("teamId")
    teamName = field("teamName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RegisterSlackWorkspaceForOrganizationResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterSlackWorkspaceForOrganizationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSlackChannelConfigurationResult:
    boto3_raw_data: "type_defs.UpdateSlackChannelConfigurationResultTypeDef" = (
        dataclasses.field()
    )

    channelId = field("channelId")
    channelName = field("channelName")
    channelRoleArn = field("channelRoleArn")
    notifyOnAddCorrespondenceToCase = field("notifyOnAddCorrespondenceToCase")
    notifyOnCaseSeverity = field("notifyOnCaseSeverity")
    notifyOnCreateOrReopenCase = field("notifyOnCreateOrReopenCase")
    notifyOnResolveCase = field("notifyOnResolveCase")
    teamId = field("teamId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateSlackChannelConfigurationResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSlackChannelConfigurationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSlackChannelConfigurationsResult:
    boto3_raw_data: "type_defs.ListSlackChannelConfigurationsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def slackChannelConfigurations(self):  # pragma: no cover
        return SlackChannelConfiguration.make_many(
            self.boto3_raw_data["slackChannelConfigurations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSlackChannelConfigurationsResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSlackChannelConfigurationsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSlackWorkspaceConfigurationsResult:
    boto3_raw_data: "type_defs.ListSlackWorkspaceConfigurationsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def slackWorkspaceConfigurations(self):  # pragma: no cover
        return SlackWorkspaceConfiguration.make_many(
            self.boto3_raw_data["slackWorkspaceConfigurations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSlackWorkspaceConfigurationsResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSlackWorkspaceConfigurationsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]

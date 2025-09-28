# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_mq import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class ActionRequired:
    boto3_raw_data: "type_defs.ActionRequiredTypeDef" = dataclasses.field()

    ActionRequiredCode = field("ActionRequiredCode")
    ActionRequiredInfo = field("ActionRequiredInfo")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActionRequiredTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ActionRequiredTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AvailabilityZone:
    boto3_raw_data: "type_defs.AvailabilityZoneTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AvailabilityZoneTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AvailabilityZoneTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EngineVersion:
    boto3_raw_data: "type_defs.EngineVersionTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EngineVersionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EngineVersionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BrokerInstance:
    boto3_raw_data: "type_defs.BrokerInstanceTypeDef" = dataclasses.field()

    ConsoleURL = field("ConsoleURL")
    Endpoints = field("Endpoints")
    IpAddress = field("IpAddress")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BrokerInstanceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BrokerInstanceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BrokerSummary:
    boto3_raw_data: "type_defs.BrokerSummaryTypeDef" = dataclasses.field()

    DeploymentMode = field("DeploymentMode")
    EngineType = field("EngineType")
    BrokerArn = field("BrokerArn")
    BrokerId = field("BrokerId")
    BrokerName = field("BrokerName")
    BrokerState = field("BrokerState")
    Created = field("Created")
    HostInstanceType = field("HostInstanceType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BrokerSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BrokerSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigurationId:
    boto3_raw_data: "type_defs.ConfigurationIdTypeDef" = dataclasses.field()

    Id = field("Id")
    Revision = field("Revision")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConfigurationIdTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConfigurationIdTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigurationRevision:
    boto3_raw_data: "type_defs.ConfigurationRevisionTypeDef" = dataclasses.field()

    Created = field("Created")
    Revision = field("Revision")
    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfigurationRevisionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigurationRevisionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EncryptionOptions:
    boto3_raw_data: "type_defs.EncryptionOptionsTypeDef" = dataclasses.field()

    UseAwsOwnedKey = field("UseAwsOwnedKey")
    KmsKeyId = field("KmsKeyId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EncryptionOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EncryptionOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LdapServerMetadataInput:
    boto3_raw_data: "type_defs.LdapServerMetadataInputTypeDef" = dataclasses.field()

    Hosts = field("Hosts")
    RoleBase = field("RoleBase")
    RoleSearchMatching = field("RoleSearchMatching")
    ServiceAccountPassword = field("ServiceAccountPassword")
    ServiceAccountUsername = field("ServiceAccountUsername")
    UserBase = field("UserBase")
    UserSearchMatching = field("UserSearchMatching")
    RoleName = field("RoleName")
    RoleSearchSubtree = field("RoleSearchSubtree")
    UserRoleName = field("UserRoleName")
    UserSearchSubtree = field("UserSearchSubtree")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LdapServerMetadataInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LdapServerMetadataInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Logs:
    boto3_raw_data: "type_defs.LogsTypeDef" = dataclasses.field()

    Audit = field("Audit")
    General = field("General")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LogsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LogsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class User:
    boto3_raw_data: "type_defs.UserTypeDef" = dataclasses.field()

    Password = field("Password")
    Username = field("Username")
    ConsoleAccess = field("ConsoleAccess")
    Groups = field("Groups")
    ReplicationUser = field("ReplicationUser")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UserTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UserTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WeeklyStartTime:
    boto3_raw_data: "type_defs.WeeklyStartTimeTypeDef" = dataclasses.field()

    DayOfWeek = field("DayOfWeek")
    TimeOfDay = field("TimeOfDay")
    TimeZone = field("TimeZone")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WeeklyStartTimeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WeeklyStartTimeTypeDef"]],
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
class CreateConfigurationRequest:
    boto3_raw_data: "type_defs.CreateConfigurationRequestTypeDef" = dataclasses.field()

    EngineType = field("EngineType")
    Name = field("Name")
    AuthenticationStrategy = field("AuthenticationStrategy")
    EngineVersion = field("EngineVersion")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateConfigurationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTagsRequest:
    boto3_raw_data: "type_defs.CreateTagsRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    Tags = field("Tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateTagsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTagsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateUserRequest:
    boto3_raw_data: "type_defs.CreateUserRequestTypeDef" = dataclasses.field()

    BrokerId = field("BrokerId")
    Password = field("Password")
    Username = field("Username")
    ConsoleAccess = field("ConsoleAccess")
    Groups = field("Groups")
    ReplicationUser = field("ReplicationUser")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateUserRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataReplicationCounterpart:
    boto3_raw_data: "type_defs.DataReplicationCounterpartTypeDef" = dataclasses.field()

    BrokerId = field("BrokerId")
    Region = field("Region")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataReplicationCounterpartTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataReplicationCounterpartTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBrokerRequest:
    boto3_raw_data: "type_defs.DeleteBrokerRequestTypeDef" = dataclasses.field()

    BrokerId = field("BrokerId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBrokerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBrokerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteConfigurationRequest:
    boto3_raw_data: "type_defs.DeleteConfigurationRequestTypeDef" = dataclasses.field()

    ConfigurationId = field("ConfigurationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteConfigurationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTagsRequest:
    boto3_raw_data: "type_defs.DeleteTagsRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    TagKeys = field("TagKeys")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteTagsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTagsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteUserRequest:
    boto3_raw_data: "type_defs.DeleteUserRequestTypeDef" = dataclasses.field()

    BrokerId = field("BrokerId")
    Username = field("Username")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteUserRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBrokerEngineTypesRequest:
    boto3_raw_data: "type_defs.DescribeBrokerEngineTypesRequestTypeDef" = (
        dataclasses.field()
    )

    EngineType = field("EngineType")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeBrokerEngineTypesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBrokerEngineTypesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBrokerInstanceOptionsRequest:
    boto3_raw_data: "type_defs.DescribeBrokerInstanceOptionsRequestTypeDef" = (
        dataclasses.field()
    )

    EngineType = field("EngineType")
    HostInstanceType = field("HostInstanceType")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    StorageType = field("StorageType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeBrokerInstanceOptionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBrokerInstanceOptionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBrokerRequest:
    boto3_raw_data: "type_defs.DescribeBrokerRequestTypeDef" = dataclasses.field()

    BrokerId = field("BrokerId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeBrokerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBrokerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LdapServerMetadataOutput:
    boto3_raw_data: "type_defs.LdapServerMetadataOutputTypeDef" = dataclasses.field()

    Hosts = field("Hosts")
    RoleBase = field("RoleBase")
    RoleSearchMatching = field("RoleSearchMatching")
    ServiceAccountUsername = field("ServiceAccountUsername")
    UserBase = field("UserBase")
    UserSearchMatching = field("UserSearchMatching")
    RoleName = field("RoleName")
    RoleSearchSubtree = field("RoleSearchSubtree")
    UserRoleName = field("UserRoleName")
    UserSearchSubtree = field("UserSearchSubtree")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LdapServerMetadataOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LdapServerMetadataOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserSummary:
    boto3_raw_data: "type_defs.UserSummaryTypeDef" = dataclasses.field()

    Username = field("Username")
    PendingChange = field("PendingChange")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UserSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UserSummaryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConfigurationRequest:
    boto3_raw_data: "type_defs.DescribeConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigurationId = field("ConfigurationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeConfigurationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConfigurationRevisionRequest:
    boto3_raw_data: "type_defs.DescribeConfigurationRevisionRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigurationId = field("ConfigurationId")
    ConfigurationRevision = field("ConfigurationRevision")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeConfigurationRevisionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConfigurationRevisionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeUserRequest:
    boto3_raw_data: "type_defs.DescribeUserRequestTypeDef" = dataclasses.field()

    BrokerId = field("BrokerId")
    Username = field("Username")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeUserRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserPendingChanges:
    boto3_raw_data: "type_defs.UserPendingChangesTypeDef" = dataclasses.field()

    PendingChange = field("PendingChange")
    ConsoleAccess = field("ConsoleAccess")
    Groups = field("Groups")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UserPendingChangesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UserPendingChangesTypeDef"]
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
class ListBrokersRequest:
    boto3_raw_data: "type_defs.ListBrokersRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBrokersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBrokersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConfigurationRevisionsRequest:
    boto3_raw_data: "type_defs.ListConfigurationRevisionsRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigurationId = field("ConfigurationId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListConfigurationRevisionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConfigurationRevisionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConfigurationsRequest:
    boto3_raw_data: "type_defs.ListConfigurationsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListConfigurationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConfigurationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsRequest:
    boto3_raw_data: "type_defs.ListTagsRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListTagsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListTagsRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUsersRequest:
    boto3_raw_data: "type_defs.ListUsersRequestTypeDef" = dataclasses.field()

    BrokerId = field("BrokerId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListUsersRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUsersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PendingLogs:
    boto3_raw_data: "type_defs.PendingLogsTypeDef" = dataclasses.field()

    Audit = field("Audit")
    General = field("General")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PendingLogsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PendingLogsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PromoteRequest:
    boto3_raw_data: "type_defs.PromoteRequestTypeDef" = dataclasses.field()

    BrokerId = field("BrokerId")
    Mode = field("Mode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PromoteRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PromoteRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RebootBrokerRequest:
    boto3_raw_data: "type_defs.RebootBrokerRequestTypeDef" = dataclasses.field()

    BrokerId = field("BrokerId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RebootBrokerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RebootBrokerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SanitizationWarning:
    boto3_raw_data: "type_defs.SanitizationWarningTypeDef" = dataclasses.field()

    Reason = field("Reason")
    AttributeName = field("AttributeName")
    ElementName = field("ElementName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SanitizationWarningTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SanitizationWarningTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateConfigurationRequest:
    boto3_raw_data: "type_defs.UpdateConfigurationRequestTypeDef" = dataclasses.field()

    ConfigurationId = field("ConfigurationId")
    Data = field("Data")
    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateConfigurationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateUserRequest:
    boto3_raw_data: "type_defs.UpdateUserRequestTypeDef" = dataclasses.field()

    BrokerId = field("BrokerId")
    Username = field("Username")
    ConsoleAccess = field("ConsoleAccess")
    Groups = field("Groups")
    Password = field("Password")
    ReplicationUser = field("ReplicationUser")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateUserRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BrokerInstanceOption:
    boto3_raw_data: "type_defs.BrokerInstanceOptionTypeDef" = dataclasses.field()

    @cached_property
    def AvailabilityZones(self):  # pragma: no cover
        return AvailabilityZone.make_many(self.boto3_raw_data["AvailabilityZones"])

    EngineType = field("EngineType")
    HostInstanceType = field("HostInstanceType")
    StorageType = field("StorageType")
    SupportedDeploymentModes = field("SupportedDeploymentModes")
    SupportedEngineVersions = field("SupportedEngineVersions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BrokerInstanceOptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BrokerInstanceOptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BrokerEngineType:
    boto3_raw_data: "type_defs.BrokerEngineTypeTypeDef" = dataclasses.field()

    EngineType = field("EngineType")

    @cached_property
    def EngineVersions(self):  # pragma: no cover
        return EngineVersion.make_many(self.boto3_raw_data["EngineVersions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BrokerEngineTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BrokerEngineTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Configurations:
    boto3_raw_data: "type_defs.ConfigurationsTypeDef" = dataclasses.field()

    @cached_property
    def Current(self):  # pragma: no cover
        return ConfigurationId.make_one(self.boto3_raw_data["Current"])

    @cached_property
    def History(self):  # pragma: no cover
        return ConfigurationId.make_many(self.boto3_raw_data["History"])

    @cached_property
    def Pending(self):  # pragma: no cover
        return ConfigurationId.make_one(self.boto3_raw_data["Pending"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConfigurationsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConfigurationsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Configuration:
    boto3_raw_data: "type_defs.ConfigurationTypeDef" = dataclasses.field()

    Arn = field("Arn")
    AuthenticationStrategy = field("AuthenticationStrategy")
    Created = field("Created")
    Description = field("Description")
    EngineType = field("EngineType")
    EngineVersion = field("EngineVersion")
    Id = field("Id")

    @cached_property
    def LatestRevision(self):  # pragma: no cover
        return ConfigurationRevision.make_one(self.boto3_raw_data["LatestRevision"])

    Name = field("Name")
    Tags = field("Tags")

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
class CreateBrokerRequest:
    boto3_raw_data: "type_defs.CreateBrokerRequestTypeDef" = dataclasses.field()

    BrokerName = field("BrokerName")
    DeploymentMode = field("DeploymentMode")
    EngineType = field("EngineType")
    HostInstanceType = field("HostInstanceType")
    PubliclyAccessible = field("PubliclyAccessible")
    AuthenticationStrategy = field("AuthenticationStrategy")
    AutoMinorVersionUpgrade = field("AutoMinorVersionUpgrade")

    @cached_property
    def Configuration(self):  # pragma: no cover
        return ConfigurationId.make_one(self.boto3_raw_data["Configuration"])

    CreatorRequestId = field("CreatorRequestId")

    @cached_property
    def EncryptionOptions(self):  # pragma: no cover
        return EncryptionOptions.make_one(self.boto3_raw_data["EncryptionOptions"])

    EngineVersion = field("EngineVersion")

    @cached_property
    def LdapServerMetadata(self):  # pragma: no cover
        return LdapServerMetadataInput.make_one(
            self.boto3_raw_data["LdapServerMetadata"]
        )

    @cached_property
    def Logs(self):  # pragma: no cover
        return Logs.make_one(self.boto3_raw_data["Logs"])

    @cached_property
    def MaintenanceWindowStartTime(self):  # pragma: no cover
        return WeeklyStartTime.make_one(
            self.boto3_raw_data["MaintenanceWindowStartTime"]
        )

    SecurityGroups = field("SecurityGroups")
    StorageType = field("StorageType")
    SubnetIds = field("SubnetIds")
    Tags = field("Tags")

    @cached_property
    def Users(self):  # pragma: no cover
        return User.make_many(self.boto3_raw_data["Users"])

    DataReplicationMode = field("DataReplicationMode")
    DataReplicationPrimaryBrokerArn = field("DataReplicationPrimaryBrokerArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBrokerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBrokerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBrokerRequest:
    boto3_raw_data: "type_defs.UpdateBrokerRequestTypeDef" = dataclasses.field()

    BrokerId = field("BrokerId")
    AuthenticationStrategy = field("AuthenticationStrategy")
    AutoMinorVersionUpgrade = field("AutoMinorVersionUpgrade")

    @cached_property
    def Configuration(self):  # pragma: no cover
        return ConfigurationId.make_one(self.boto3_raw_data["Configuration"])

    EngineVersion = field("EngineVersion")
    HostInstanceType = field("HostInstanceType")

    @cached_property
    def LdapServerMetadata(self):  # pragma: no cover
        return LdapServerMetadataInput.make_one(
            self.boto3_raw_data["LdapServerMetadata"]
        )

    @cached_property
    def Logs(self):  # pragma: no cover
        return Logs.make_one(self.boto3_raw_data["Logs"])

    @cached_property
    def MaintenanceWindowStartTime(self):  # pragma: no cover
        return WeeklyStartTime.make_one(
            self.boto3_raw_data["MaintenanceWindowStartTime"]
        )

    SecurityGroups = field("SecurityGroups")
    DataReplicationMode = field("DataReplicationMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBrokerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBrokerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBrokerResponse:
    boto3_raw_data: "type_defs.CreateBrokerResponseTypeDef" = dataclasses.field()

    BrokerArn = field("BrokerArn")
    BrokerId = field("BrokerId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBrokerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBrokerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConfigurationResponse:
    boto3_raw_data: "type_defs.CreateConfigurationResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    AuthenticationStrategy = field("AuthenticationStrategy")
    Created = field("Created")
    Id = field("Id")

    @cached_property
    def LatestRevision(self):  # pragma: no cover
        return ConfigurationRevision.make_one(self.boto3_raw_data["LatestRevision"])

    Name = field("Name")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateConfigurationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBrokerResponse:
    boto3_raw_data: "type_defs.DeleteBrokerResponseTypeDef" = dataclasses.field()

    BrokerId = field("BrokerId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBrokerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBrokerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteConfigurationResponse:
    boto3_raw_data: "type_defs.DeleteConfigurationResponseTypeDef" = dataclasses.field()

    ConfigurationId = field("ConfigurationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteConfigurationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConfigurationResponse:
    boto3_raw_data: "type_defs.DescribeConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    AuthenticationStrategy = field("AuthenticationStrategy")
    Created = field("Created")
    Description = field("Description")
    EngineType = field("EngineType")
    EngineVersion = field("EngineVersion")
    Id = field("Id")

    @cached_property
    def LatestRevision(self):  # pragma: no cover
        return ConfigurationRevision.make_one(self.boto3_raw_data["LatestRevision"])

    Name = field("Name")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeConfigurationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConfigurationRevisionResponse:
    boto3_raw_data: "type_defs.DescribeConfigurationRevisionResponseTypeDef" = (
        dataclasses.field()
    )

    ConfigurationId = field("ConfigurationId")
    Created = field("Created")
    Data = field("Data")
    Description = field("Description")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeConfigurationRevisionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConfigurationRevisionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmptyResponseMetadata:
    boto3_raw_data: "type_defs.EmptyResponseMetadataTypeDef" = dataclasses.field()

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EmptyResponseMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmptyResponseMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBrokersResponse:
    boto3_raw_data: "type_defs.ListBrokersResponseTypeDef" = dataclasses.field()

    @cached_property
    def BrokerSummaries(self):  # pragma: no cover
        return BrokerSummary.make_many(self.boto3_raw_data["BrokerSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBrokersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBrokersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConfigurationRevisionsResponse:
    boto3_raw_data: "type_defs.ListConfigurationRevisionsResponseTypeDef" = (
        dataclasses.field()
    )

    ConfigurationId = field("ConfigurationId")
    MaxResults = field("MaxResults")

    @cached_property
    def Revisions(self):  # pragma: no cover
        return ConfigurationRevision.make_many(self.boto3_raw_data["Revisions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListConfigurationRevisionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConfigurationRevisionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsResponse:
    boto3_raw_data: "type_defs.ListTagsResponseTypeDef" = dataclasses.field()

    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListTagsResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PromoteResponse:
    boto3_raw_data: "type_defs.PromoteResponseTypeDef" = dataclasses.field()

    BrokerId = field("BrokerId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PromoteResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PromoteResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataReplicationMetadataOutput:
    boto3_raw_data: "type_defs.DataReplicationMetadataOutputTypeDef" = (
        dataclasses.field()
    )

    DataReplicationRole = field("DataReplicationRole")

    @cached_property
    def DataReplicationCounterpart(self):  # pragma: no cover
        return DataReplicationCounterpart.make_one(
            self.boto3_raw_data["DataReplicationCounterpart"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DataReplicationMetadataOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataReplicationMetadataOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUsersResponse:
    boto3_raw_data: "type_defs.ListUsersResponseTypeDef" = dataclasses.field()

    BrokerId = field("BrokerId")
    MaxResults = field("MaxResults")

    @cached_property
    def Users(self):  # pragma: no cover
        return UserSummary.make_many(self.boto3_raw_data["Users"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListUsersResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUsersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeUserResponse:
    boto3_raw_data: "type_defs.DescribeUserResponseTypeDef" = dataclasses.field()

    BrokerId = field("BrokerId")
    ConsoleAccess = field("ConsoleAccess")
    Groups = field("Groups")

    @cached_property
    def Pending(self):  # pragma: no cover
        return UserPendingChanges.make_one(self.boto3_raw_data["Pending"])

    Username = field("Username")
    ReplicationUser = field("ReplicationUser")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeUserResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeUserResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBrokersRequestPaginate:
    boto3_raw_data: "type_defs.ListBrokersRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBrokersRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBrokersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LogsSummary:
    boto3_raw_data: "type_defs.LogsSummaryTypeDef" = dataclasses.field()

    General = field("General")
    GeneralLogGroup = field("GeneralLogGroup")
    Audit = field("Audit")
    AuditLogGroup = field("AuditLogGroup")

    @cached_property
    def Pending(self):  # pragma: no cover
        return PendingLogs.make_one(self.boto3_raw_data["Pending"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LogsSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LogsSummaryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateConfigurationResponse:
    boto3_raw_data: "type_defs.UpdateConfigurationResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Created = field("Created")
    Id = field("Id")

    @cached_property
    def LatestRevision(self):  # pragma: no cover
        return ConfigurationRevision.make_one(self.boto3_raw_data["LatestRevision"])

    Name = field("Name")

    @cached_property
    def Warnings(self):  # pragma: no cover
        return SanitizationWarning.make_many(self.boto3_raw_data["Warnings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateConfigurationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBrokerInstanceOptionsResponse:
    boto3_raw_data: "type_defs.DescribeBrokerInstanceOptionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def BrokerInstanceOptions(self):  # pragma: no cover
        return BrokerInstanceOption.make_many(
            self.boto3_raw_data["BrokerInstanceOptions"]
        )

    MaxResults = field("MaxResults")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeBrokerInstanceOptionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBrokerInstanceOptionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBrokerEngineTypesResponse:
    boto3_raw_data: "type_defs.DescribeBrokerEngineTypesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def BrokerEngineTypes(self):  # pragma: no cover
        return BrokerEngineType.make_many(self.boto3_raw_data["BrokerEngineTypes"])

    MaxResults = field("MaxResults")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeBrokerEngineTypesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBrokerEngineTypesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConfigurationsResponse:
    boto3_raw_data: "type_defs.ListConfigurationsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Configurations(self):  # pragma: no cover
        return Configuration.make_many(self.boto3_raw_data["Configurations"])

    MaxResults = field("MaxResults")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListConfigurationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConfigurationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBrokerResponse:
    boto3_raw_data: "type_defs.UpdateBrokerResponseTypeDef" = dataclasses.field()

    AuthenticationStrategy = field("AuthenticationStrategy")
    AutoMinorVersionUpgrade = field("AutoMinorVersionUpgrade")
    BrokerId = field("BrokerId")

    @cached_property
    def Configuration(self):  # pragma: no cover
        return ConfigurationId.make_one(self.boto3_raw_data["Configuration"])

    EngineVersion = field("EngineVersion")
    HostInstanceType = field("HostInstanceType")

    @cached_property
    def LdapServerMetadata(self):  # pragma: no cover
        return LdapServerMetadataOutput.make_one(
            self.boto3_raw_data["LdapServerMetadata"]
        )

    @cached_property
    def Logs(self):  # pragma: no cover
        return Logs.make_one(self.boto3_raw_data["Logs"])

    @cached_property
    def MaintenanceWindowStartTime(self):  # pragma: no cover
        return WeeklyStartTime.make_one(
            self.boto3_raw_data["MaintenanceWindowStartTime"]
        )

    SecurityGroups = field("SecurityGroups")

    @cached_property
    def DataReplicationMetadata(self):  # pragma: no cover
        return DataReplicationMetadataOutput.make_one(
            self.boto3_raw_data["DataReplicationMetadata"]
        )

    DataReplicationMode = field("DataReplicationMode")

    @cached_property
    def PendingDataReplicationMetadata(self):  # pragma: no cover
        return DataReplicationMetadataOutput.make_one(
            self.boto3_raw_data["PendingDataReplicationMetadata"]
        )

    PendingDataReplicationMode = field("PendingDataReplicationMode")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBrokerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBrokerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBrokerResponse:
    boto3_raw_data: "type_defs.DescribeBrokerResponseTypeDef" = dataclasses.field()

    @cached_property
    def ActionsRequired(self):  # pragma: no cover
        return ActionRequired.make_many(self.boto3_raw_data["ActionsRequired"])

    AuthenticationStrategy = field("AuthenticationStrategy")
    AutoMinorVersionUpgrade = field("AutoMinorVersionUpgrade")
    BrokerArn = field("BrokerArn")
    BrokerId = field("BrokerId")

    @cached_property
    def BrokerInstances(self):  # pragma: no cover
        return BrokerInstance.make_many(self.boto3_raw_data["BrokerInstances"])

    BrokerName = field("BrokerName")
    BrokerState = field("BrokerState")

    @cached_property
    def Configurations(self):  # pragma: no cover
        return Configurations.make_one(self.boto3_raw_data["Configurations"])

    Created = field("Created")
    DeploymentMode = field("DeploymentMode")

    @cached_property
    def EncryptionOptions(self):  # pragma: no cover
        return EncryptionOptions.make_one(self.boto3_raw_data["EncryptionOptions"])

    EngineType = field("EngineType")
    EngineVersion = field("EngineVersion")
    HostInstanceType = field("HostInstanceType")

    @cached_property
    def LdapServerMetadata(self):  # pragma: no cover
        return LdapServerMetadataOutput.make_one(
            self.boto3_raw_data["LdapServerMetadata"]
        )

    @cached_property
    def Logs(self):  # pragma: no cover
        return LogsSummary.make_one(self.boto3_raw_data["Logs"])

    @cached_property
    def MaintenanceWindowStartTime(self):  # pragma: no cover
        return WeeklyStartTime.make_one(
            self.boto3_raw_data["MaintenanceWindowStartTime"]
        )

    PendingAuthenticationStrategy = field("PendingAuthenticationStrategy")
    PendingEngineVersion = field("PendingEngineVersion")
    PendingHostInstanceType = field("PendingHostInstanceType")

    @cached_property
    def PendingLdapServerMetadata(self):  # pragma: no cover
        return LdapServerMetadataOutput.make_one(
            self.boto3_raw_data["PendingLdapServerMetadata"]
        )

    PendingSecurityGroups = field("PendingSecurityGroups")
    PubliclyAccessible = field("PubliclyAccessible")
    SecurityGroups = field("SecurityGroups")
    StorageType = field("StorageType")
    SubnetIds = field("SubnetIds")
    Tags = field("Tags")

    @cached_property
    def Users(self):  # pragma: no cover
        return UserSummary.make_many(self.boto3_raw_data["Users"])

    @cached_property
    def DataReplicationMetadata(self):  # pragma: no cover
        return DataReplicationMetadataOutput.make_one(
            self.boto3_raw_data["DataReplicationMetadata"]
        )

    DataReplicationMode = field("DataReplicationMode")

    @cached_property
    def PendingDataReplicationMetadata(self):  # pragma: no cover
        return DataReplicationMetadataOutput.make_one(
            self.boto3_raw_data["PendingDataReplicationMetadata"]
        )

    PendingDataReplicationMode = field("PendingDataReplicationMode")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeBrokerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBrokerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]

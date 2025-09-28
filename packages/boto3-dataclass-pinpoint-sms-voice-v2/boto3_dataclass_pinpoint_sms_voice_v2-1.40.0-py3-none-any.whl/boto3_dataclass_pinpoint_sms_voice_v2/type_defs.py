# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_pinpoint_sms_voice_v2 import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AccountAttribute:
    boto3_raw_data: "type_defs.AccountAttributeTypeDef" = dataclasses.field()

    Name = field("Name")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccountAttributeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccountAttributeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccountLimit:
    boto3_raw_data: "type_defs.AccountLimitTypeDef" = dataclasses.field()

    Name = field("Name")
    Used = field("Used")
    Max = field("Max")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccountLimitTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccountLimitTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateOriginationIdentityRequest:
    boto3_raw_data: "type_defs.AssociateOriginationIdentityRequestTypeDef" = (
        dataclasses.field()
    )

    PoolId = field("PoolId")
    OriginationIdentity = field("OriginationIdentity")
    IsoCountryCode = field("IsoCountryCode")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateOriginationIdentityRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateOriginationIdentityRequestTypeDef"]
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
class AssociateProtectConfigurationRequest:
    boto3_raw_data: "type_defs.AssociateProtectConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    ProtectConfigurationId = field("ProtectConfigurationId")
    ConfigurationSetName = field("ConfigurationSetName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateProtectConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateProtectConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudWatchLogsDestination:
    boto3_raw_data: "type_defs.CloudWatchLogsDestinationTypeDef" = dataclasses.field()

    IamRoleArn = field("IamRoleArn")
    LogGroupArn = field("LogGroupArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CloudWatchLogsDestinationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudWatchLogsDestinationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigurationSetFilter:
    boto3_raw_data: "type_defs.ConfigurationSetFilterTypeDef" = dataclasses.field()

    Name = field("Name")
    Values = field("Values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfigurationSetFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigurationSetFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Tag:
    boto3_raw_data: "type_defs.TagTypeDef" = dataclasses.field()

    Key = field("Key")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KinesisFirehoseDestination:
    boto3_raw_data: "type_defs.KinesisFirehoseDestinationTypeDef" = dataclasses.field()

    IamRoleArn = field("IamRoleArn")
    DeliveryStreamArn = field("DeliveryStreamArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KinesisFirehoseDestinationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KinesisFirehoseDestinationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SnsDestination:
    boto3_raw_data: "type_defs.SnsDestinationTypeDef" = dataclasses.field()

    TopicArn = field("TopicArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SnsDestinationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SnsDestinationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRegistrationAssociationRequest:
    boto3_raw_data: "type_defs.CreateRegistrationAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    RegistrationId = field("RegistrationId")
    ResourceId = field("ResourceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateRegistrationAssociationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRegistrationAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRegistrationVersionRequest:
    boto3_raw_data: "type_defs.CreateRegistrationVersionRequestTypeDef" = (
        dataclasses.field()
    )

    RegistrationId = field("RegistrationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateRegistrationVersionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRegistrationVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegistrationVersionStatusHistory:
    boto3_raw_data: "type_defs.RegistrationVersionStatusHistoryTypeDef" = (
        dataclasses.field()
    )

    DraftTimestamp = field("DraftTimestamp")
    SubmittedTimestamp = field("SubmittedTimestamp")
    ReviewingTimestamp = field("ReviewingTimestamp")
    RequiresAuthenticationTimestamp = field("RequiresAuthenticationTimestamp")
    ApprovedTimestamp = field("ApprovedTimestamp")
    DiscardedTimestamp = field("DiscardedTimestamp")
    DeniedTimestamp = field("DeniedTimestamp")
    RevokedTimestamp = field("RevokedTimestamp")
    ArchivedTimestamp = field("ArchivedTimestamp")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RegistrationVersionStatusHistoryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegistrationVersionStatusHistoryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteConfigurationSetRequest:
    boto3_raw_data: "type_defs.DeleteConfigurationSetRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigurationSetName = field("ConfigurationSetName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteConfigurationSetRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteConfigurationSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDefaultMessageTypeRequest:
    boto3_raw_data: "type_defs.DeleteDefaultMessageTypeRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigurationSetName = field("ConfigurationSetName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteDefaultMessageTypeRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDefaultMessageTypeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDefaultSenderIdRequest:
    boto3_raw_data: "type_defs.DeleteDefaultSenderIdRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigurationSetName = field("ConfigurationSetName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDefaultSenderIdRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDefaultSenderIdRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEventDestinationRequest:
    boto3_raw_data: "type_defs.DeleteEventDestinationRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigurationSetName = field("ConfigurationSetName")
    EventDestinationName = field("EventDestinationName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteEventDestinationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEventDestinationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteKeywordRequest:
    boto3_raw_data: "type_defs.DeleteKeywordRequestTypeDef" = dataclasses.field()

    OriginationIdentity = field("OriginationIdentity")
    Keyword = field("Keyword")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteKeywordRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteKeywordRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteOptOutListRequest:
    boto3_raw_data: "type_defs.DeleteOptOutListRequestTypeDef" = dataclasses.field()

    OptOutListName = field("OptOutListName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteOptOutListRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteOptOutListRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteOptedOutNumberRequest:
    boto3_raw_data: "type_defs.DeleteOptedOutNumberRequestTypeDef" = dataclasses.field()

    OptOutListName = field("OptOutListName")
    OptedOutNumber = field("OptedOutNumber")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteOptedOutNumberRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteOptedOutNumberRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePoolRequest:
    boto3_raw_data: "type_defs.DeletePoolRequestTypeDef" = dataclasses.field()

    PoolId = field("PoolId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeletePoolRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePoolRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteProtectConfigurationRequest:
    boto3_raw_data: "type_defs.DeleteProtectConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    ProtectConfigurationId = field("ProtectConfigurationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteProtectConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteProtectConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteProtectConfigurationRuleSetNumberOverrideRequest:
    boto3_raw_data: (
        "type_defs.DeleteProtectConfigurationRuleSetNumberOverrideRequestTypeDef"
    ) = dataclasses.field()

    ProtectConfigurationId = field("ProtectConfigurationId")
    DestinationPhoneNumber = field("DestinationPhoneNumber")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteProtectConfigurationRuleSetNumberOverrideRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.DeleteProtectConfigurationRuleSetNumberOverrideRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRegistrationAttachmentRequest:
    boto3_raw_data: "type_defs.DeleteRegistrationAttachmentRequestTypeDef" = (
        dataclasses.field()
    )

    RegistrationAttachmentId = field("RegistrationAttachmentId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteRegistrationAttachmentRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRegistrationAttachmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRegistrationFieldValueRequest:
    boto3_raw_data: "type_defs.DeleteRegistrationFieldValueRequestTypeDef" = (
        dataclasses.field()
    )

    RegistrationId = field("RegistrationId")
    FieldPath = field("FieldPath")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteRegistrationFieldValueRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRegistrationFieldValueRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRegistrationRequest:
    boto3_raw_data: "type_defs.DeleteRegistrationRequestTypeDef" = dataclasses.field()

    RegistrationId = field("RegistrationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteRegistrationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRegistrationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteResourcePolicyRequest:
    boto3_raw_data: "type_defs.DeleteResourcePolicyRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteResourcePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteResourcePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVerifiedDestinationNumberRequest:
    boto3_raw_data: "type_defs.DeleteVerifiedDestinationNumberRequestTypeDef" = (
        dataclasses.field()
    )

    VerifiedDestinationNumberId = field("VerifiedDestinationNumberId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteVerifiedDestinationNumberRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVerifiedDestinationNumberRequestTypeDef"]
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
class DescribeAccountAttributesRequest:
    boto3_raw_data: "type_defs.DescribeAccountAttributesRequestTypeDef" = (
        dataclasses.field()
    )

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeAccountAttributesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAccountAttributesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAccountLimitsRequest:
    boto3_raw_data: "type_defs.DescribeAccountLimitsRequestTypeDef" = (
        dataclasses.field()
    )

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAccountLimitsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAccountLimitsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KeywordFilter:
    boto3_raw_data: "type_defs.KeywordFilterTypeDef" = dataclasses.field()

    Name = field("Name")
    Values = field("Values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KeywordFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.KeywordFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KeywordInformation:
    boto3_raw_data: "type_defs.KeywordInformationTypeDef" = dataclasses.field()

    Keyword = field("Keyword")
    KeywordMessage = field("KeywordMessage")
    KeywordAction = field("KeywordAction")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KeywordInformationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KeywordInformationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOptOutListsRequest:
    boto3_raw_data: "type_defs.DescribeOptOutListsRequestTypeDef" = dataclasses.field()

    OptOutListNames = field("OptOutListNames")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    Owner = field("Owner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeOptOutListsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeOptOutListsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OptOutListInformation:
    boto3_raw_data: "type_defs.OptOutListInformationTypeDef" = dataclasses.field()

    OptOutListArn = field("OptOutListArn")
    OptOutListName = field("OptOutListName")
    CreatedTimestamp = field("CreatedTimestamp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OptOutListInformationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OptOutListInformationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OptedOutFilter:
    boto3_raw_data: "type_defs.OptedOutFilterTypeDef" = dataclasses.field()

    Name = field("Name")
    Values = field("Values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OptedOutFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OptedOutFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OptedOutNumberInformation:
    boto3_raw_data: "type_defs.OptedOutNumberInformationTypeDef" = dataclasses.field()

    OptedOutNumber = field("OptedOutNumber")
    OptedOutTimestamp = field("OptedOutTimestamp")
    EndUserOptedOut = field("EndUserOptedOut")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OptedOutNumberInformationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OptedOutNumberInformationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PhoneNumberFilter:
    boto3_raw_data: "type_defs.PhoneNumberFilterTypeDef" = dataclasses.field()

    Name = field("Name")
    Values = field("Values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PhoneNumberFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PhoneNumberFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PhoneNumberInformation:
    boto3_raw_data: "type_defs.PhoneNumberInformationTypeDef" = dataclasses.field()

    PhoneNumberArn = field("PhoneNumberArn")
    PhoneNumber = field("PhoneNumber")
    Status = field("Status")
    IsoCountryCode = field("IsoCountryCode")
    MessageType = field("MessageType")
    NumberCapabilities = field("NumberCapabilities")
    NumberType = field("NumberType")
    MonthlyLeasingPrice = field("MonthlyLeasingPrice")
    TwoWayEnabled = field("TwoWayEnabled")
    SelfManagedOptOutsEnabled = field("SelfManagedOptOutsEnabled")
    OptOutListName = field("OptOutListName")
    DeletionProtectionEnabled = field("DeletionProtectionEnabled")
    CreatedTimestamp = field("CreatedTimestamp")
    PhoneNumberId = field("PhoneNumberId")
    TwoWayChannelArn = field("TwoWayChannelArn")
    TwoWayChannelRole = field("TwoWayChannelRole")
    InternationalSendingEnabled = field("InternationalSendingEnabled")
    PoolId = field("PoolId")
    RegistrationId = field("RegistrationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PhoneNumberInformationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PhoneNumberInformationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PoolFilter:
    boto3_raw_data: "type_defs.PoolFilterTypeDef" = dataclasses.field()

    Name = field("Name")
    Values = field("Values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PoolFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PoolFilterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PoolInformation:
    boto3_raw_data: "type_defs.PoolInformationTypeDef" = dataclasses.field()

    PoolArn = field("PoolArn")
    PoolId = field("PoolId")
    Status = field("Status")
    MessageType = field("MessageType")
    TwoWayEnabled = field("TwoWayEnabled")
    SelfManagedOptOutsEnabled = field("SelfManagedOptOutsEnabled")
    OptOutListName = field("OptOutListName")
    SharedRoutesEnabled = field("SharedRoutesEnabled")
    DeletionProtectionEnabled = field("DeletionProtectionEnabled")
    CreatedTimestamp = field("CreatedTimestamp")
    TwoWayChannelArn = field("TwoWayChannelArn")
    TwoWayChannelRole = field("TwoWayChannelRole")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PoolInformationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PoolInformationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectConfigurationFilter:
    boto3_raw_data: "type_defs.ProtectConfigurationFilterTypeDef" = dataclasses.field()

    Name = field("Name")
    Values = field("Values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProtectConfigurationFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtectConfigurationFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectConfigurationInformation:
    boto3_raw_data: "type_defs.ProtectConfigurationInformationTypeDef" = (
        dataclasses.field()
    )

    ProtectConfigurationArn = field("ProtectConfigurationArn")
    ProtectConfigurationId = field("ProtectConfigurationId")
    CreatedTimestamp = field("CreatedTimestamp")
    AccountDefault = field("AccountDefault")
    DeletionProtectionEnabled = field("DeletionProtectionEnabled")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ProtectConfigurationInformationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtectConfigurationInformationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegistrationAttachmentFilter:
    boto3_raw_data: "type_defs.RegistrationAttachmentFilterTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Values = field("Values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegistrationAttachmentFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegistrationAttachmentFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegistrationAttachmentsInformation:
    boto3_raw_data: "type_defs.RegistrationAttachmentsInformationTypeDef" = (
        dataclasses.field()
    )

    RegistrationAttachmentArn = field("RegistrationAttachmentArn")
    RegistrationAttachmentId = field("RegistrationAttachmentId")
    AttachmentStatus = field("AttachmentStatus")
    CreatedTimestamp = field("CreatedTimestamp")
    AttachmentUploadErrorReason = field("AttachmentUploadErrorReason")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RegistrationAttachmentsInformationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegistrationAttachmentsInformationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRegistrationFieldDefinitionsRequest:
    boto3_raw_data: "type_defs.DescribeRegistrationFieldDefinitionsRequestTypeDef" = (
        dataclasses.field()
    )

    RegistrationType = field("RegistrationType")
    SectionPath = field("SectionPath")
    FieldPaths = field("FieldPaths")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRegistrationFieldDefinitionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRegistrationFieldDefinitionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRegistrationFieldValuesRequest:
    boto3_raw_data: "type_defs.DescribeRegistrationFieldValuesRequestTypeDef" = (
        dataclasses.field()
    )

    RegistrationId = field("RegistrationId")
    VersionNumber = field("VersionNumber")
    SectionPath = field("SectionPath")
    FieldPaths = field("FieldPaths")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRegistrationFieldValuesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRegistrationFieldValuesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegistrationFieldValueInformation:
    boto3_raw_data: "type_defs.RegistrationFieldValueInformationTypeDef" = (
        dataclasses.field()
    )

    FieldPath = field("FieldPath")
    SelectChoices = field("SelectChoices")
    TextValue = field("TextValue")
    RegistrationAttachmentId = field("RegistrationAttachmentId")
    DeniedReason = field("DeniedReason")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RegistrationFieldValueInformationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegistrationFieldValueInformationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRegistrationSectionDefinitionsRequest:
    boto3_raw_data: "type_defs.DescribeRegistrationSectionDefinitionsRequestTypeDef" = (
        dataclasses.field()
    )

    RegistrationType = field("RegistrationType")
    SectionPaths = field("SectionPaths")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRegistrationSectionDefinitionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRegistrationSectionDefinitionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegistrationTypeFilter:
    boto3_raw_data: "type_defs.RegistrationTypeFilterTypeDef" = dataclasses.field()

    Name = field("Name")
    Values = field("Values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegistrationTypeFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegistrationTypeFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegistrationVersionFilter:
    boto3_raw_data: "type_defs.RegistrationVersionFilterTypeDef" = dataclasses.field()

    Name = field("Name")
    Values = field("Values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegistrationVersionFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegistrationVersionFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegistrationFilter:
    boto3_raw_data: "type_defs.RegistrationFilterTypeDef" = dataclasses.field()

    Name = field("Name")
    Values = field("Values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegistrationFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegistrationFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegistrationInformation:
    boto3_raw_data: "type_defs.RegistrationInformationTypeDef" = dataclasses.field()

    RegistrationArn = field("RegistrationArn")
    RegistrationId = field("RegistrationId")
    RegistrationType = field("RegistrationType")
    RegistrationStatus = field("RegistrationStatus")
    CurrentVersionNumber = field("CurrentVersionNumber")
    CreatedTimestamp = field("CreatedTimestamp")
    ApprovedVersionNumber = field("ApprovedVersionNumber")
    LatestDeniedVersionNumber = field("LatestDeniedVersionNumber")
    AdditionalAttributes = field("AdditionalAttributes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegistrationInformationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegistrationInformationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SenderIdAndCountry:
    boto3_raw_data: "type_defs.SenderIdAndCountryTypeDef" = dataclasses.field()

    SenderId = field("SenderId")
    IsoCountryCode = field("IsoCountryCode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SenderIdAndCountryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SenderIdAndCountryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SenderIdFilter:
    boto3_raw_data: "type_defs.SenderIdFilterTypeDef" = dataclasses.field()

    Name = field("Name")
    Values = field("Values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SenderIdFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SenderIdFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SenderIdInformation:
    boto3_raw_data: "type_defs.SenderIdInformationTypeDef" = dataclasses.field()

    SenderIdArn = field("SenderIdArn")
    SenderId = field("SenderId")
    IsoCountryCode = field("IsoCountryCode")
    MessageTypes = field("MessageTypes")
    MonthlyLeasingPrice = field("MonthlyLeasingPrice")
    DeletionProtectionEnabled = field("DeletionProtectionEnabled")
    Registered = field("Registered")
    RegistrationId = field("RegistrationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SenderIdInformationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SenderIdInformationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSpendLimitsRequest:
    boto3_raw_data: "type_defs.DescribeSpendLimitsRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeSpendLimitsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSpendLimitsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SpendLimit:
    boto3_raw_data: "type_defs.SpendLimitTypeDef" = dataclasses.field()

    Name = field("Name")
    EnforcedLimit = field("EnforcedLimit")
    MaxLimit = field("MaxLimit")
    Overridden = field("Overridden")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SpendLimitTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SpendLimitTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VerifiedDestinationNumberFilter:
    boto3_raw_data: "type_defs.VerifiedDestinationNumberFilterTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Values = field("Values")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.VerifiedDestinationNumberFilterTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VerifiedDestinationNumberFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VerifiedDestinationNumberInformation:
    boto3_raw_data: "type_defs.VerifiedDestinationNumberInformationTypeDef" = (
        dataclasses.field()
    )

    VerifiedDestinationNumberArn = field("VerifiedDestinationNumberArn")
    VerifiedDestinationNumberId = field("VerifiedDestinationNumberId")
    DestinationPhoneNumber = field("DestinationPhoneNumber")
    Status = field("Status")
    CreatedTimestamp = field("CreatedTimestamp")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.VerifiedDestinationNumberInformationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VerifiedDestinationNumberInformationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateOriginationIdentityRequest:
    boto3_raw_data: "type_defs.DisassociateOriginationIdentityRequestTypeDef" = (
        dataclasses.field()
    )

    PoolId = field("PoolId")
    OriginationIdentity = field("OriginationIdentity")
    IsoCountryCode = field("IsoCountryCode")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateOriginationIdentityRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateOriginationIdentityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateProtectConfigurationRequest:
    boto3_raw_data: "type_defs.DisassociateProtectConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    ProtectConfigurationId = field("ProtectConfigurationId")
    ConfigurationSetName = field("ConfigurationSetName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateProtectConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateProtectConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DiscardRegistrationVersionRequest:
    boto3_raw_data: "type_defs.DiscardRegistrationVersionRequestTypeDef" = (
        dataclasses.field()
    )

    RegistrationId = field("RegistrationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DiscardRegistrationVersionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DiscardRegistrationVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetProtectConfigurationCountryRuleSetRequest:
    boto3_raw_data: "type_defs.GetProtectConfigurationCountryRuleSetRequestTypeDef" = (
        dataclasses.field()
    )

    ProtectConfigurationId = field("ProtectConfigurationId")
    NumberCapability = field("NumberCapability")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetProtectConfigurationCountryRuleSetRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetProtectConfigurationCountryRuleSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectConfigurationCountryRuleSetInformation:
    boto3_raw_data: "type_defs.ProtectConfigurationCountryRuleSetInformationTypeDef" = (
        dataclasses.field()
    )

    ProtectStatus = field("ProtectStatus")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ProtectConfigurationCountryRuleSetInformationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtectConfigurationCountryRuleSetInformationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourcePolicyRequest:
    boto3_raw_data: "type_defs.GetResourcePolicyRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourcePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourcePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PoolOriginationIdentitiesFilter:
    boto3_raw_data: "type_defs.PoolOriginationIdentitiesFilterTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Values = field("Values")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PoolOriginationIdentitiesFilterTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PoolOriginationIdentitiesFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OriginationIdentityMetadata:
    boto3_raw_data: "type_defs.OriginationIdentityMetadataTypeDef" = dataclasses.field()

    OriginationIdentityArn = field("OriginationIdentityArn")
    OriginationIdentity = field("OriginationIdentity")
    IsoCountryCode = field("IsoCountryCode")
    NumberCapabilities = field("NumberCapabilities")
    PhoneNumber = field("PhoneNumber")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OriginationIdentityMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OriginationIdentityMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectConfigurationRuleSetNumberOverrideFilterItem:
    boto3_raw_data: (
        "type_defs.ProtectConfigurationRuleSetNumberOverrideFilterItemTypeDef"
    ) = dataclasses.field()

    Name = field("Name")
    Values = field("Values")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ProtectConfigurationRuleSetNumberOverrideFilterItemTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.ProtectConfigurationRuleSetNumberOverrideFilterItemTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectConfigurationRuleSetNumberOverride:
    boto3_raw_data: "type_defs.ProtectConfigurationRuleSetNumberOverrideTypeDef" = (
        dataclasses.field()
    )

    DestinationPhoneNumber = field("DestinationPhoneNumber")
    CreatedTimestamp = field("CreatedTimestamp")
    Action = field("Action")
    IsoCountryCode = field("IsoCountryCode")
    ExpirationTimestamp = field("ExpirationTimestamp")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ProtectConfigurationRuleSetNumberOverrideTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtectConfigurationRuleSetNumberOverrideTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegistrationAssociationFilter:
    boto3_raw_data: "type_defs.RegistrationAssociationFilterTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Values = field("Values")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RegistrationAssociationFilterTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegistrationAssociationFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegistrationAssociationMetadata:
    boto3_raw_data: "type_defs.RegistrationAssociationMetadataTypeDef" = (
        dataclasses.field()
    )

    ResourceArn = field("ResourceArn")
    ResourceId = field("ResourceId")
    ResourceType = field("ResourceType")
    IsoCountryCode = field("IsoCountryCode")
    PhoneNumber = field("PhoneNumber")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RegistrationAssociationMetadataTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegistrationAssociationMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceRequest:
    boto3_raw_data: "type_defs.ListTagsForResourceRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutKeywordRequest:
    boto3_raw_data: "type_defs.PutKeywordRequestTypeDef" = dataclasses.field()

    OriginationIdentity = field("OriginationIdentity")
    Keyword = field("Keyword")
    KeywordMessage = field("KeywordMessage")
    KeywordAction = field("KeywordAction")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutKeywordRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutKeywordRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutMessageFeedbackRequest:
    boto3_raw_data: "type_defs.PutMessageFeedbackRequestTypeDef" = dataclasses.field()

    MessageId = field("MessageId")
    MessageFeedbackStatus = field("MessageFeedbackStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutMessageFeedbackRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutMessageFeedbackRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutOptedOutNumberRequest:
    boto3_raw_data: "type_defs.PutOptedOutNumberRequestTypeDef" = dataclasses.field()

    OptOutListName = field("OptOutListName")
    OptedOutNumber = field("OptedOutNumber")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutOptedOutNumberRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutOptedOutNumberRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutRegistrationFieldValueRequest:
    boto3_raw_data: "type_defs.PutRegistrationFieldValueRequestTypeDef" = (
        dataclasses.field()
    )

    RegistrationId = field("RegistrationId")
    FieldPath = field("FieldPath")
    SelectChoices = field("SelectChoices")
    TextValue = field("TextValue")
    RegistrationAttachmentId = field("RegistrationAttachmentId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutRegistrationFieldValueRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutRegistrationFieldValueRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutResourcePolicyRequest:
    boto3_raw_data: "type_defs.PutResourcePolicyRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    Policy = field("Policy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutResourcePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutResourcePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegistrationDeniedReasonInformation:
    boto3_raw_data: "type_defs.RegistrationDeniedReasonInformationTypeDef" = (
        dataclasses.field()
    )

    Reason = field("Reason")
    ShortDescription = field("ShortDescription")
    LongDescription = field("LongDescription")
    DocumentationTitle = field("DocumentationTitle")
    DocumentationLink = field("DocumentationLink")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RegistrationDeniedReasonInformationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegistrationDeniedReasonInformationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SelectValidation:
    boto3_raw_data: "type_defs.SelectValidationTypeDef" = dataclasses.field()

    MinChoices = field("MinChoices")
    MaxChoices = field("MaxChoices")
    Options = field("Options")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SelectValidationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SelectValidationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TextValidation:
    boto3_raw_data: "type_defs.TextValidationTypeDef" = dataclasses.field()

    MinLength = field("MinLength")
    MaxLength = field("MaxLength")
    Pattern = field("Pattern")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TextValidationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TextValidationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SelectOptionDescription:
    boto3_raw_data: "type_defs.SelectOptionDescriptionTypeDef" = dataclasses.field()

    Option = field("Option")
    Title = field("Title")
    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SelectOptionDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SelectOptionDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegistrationSectionDisplayHints:
    boto3_raw_data: "type_defs.RegistrationSectionDisplayHintsTypeDef" = (
        dataclasses.field()
    )

    Title = field("Title")
    ShortDescription = field("ShortDescription")
    LongDescription = field("LongDescription")
    DocumentationTitle = field("DocumentationTitle")
    DocumentationLink = field("DocumentationLink")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RegistrationSectionDisplayHintsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegistrationSectionDisplayHintsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegistrationTypeDisplayHints:
    boto3_raw_data: "type_defs.RegistrationTypeDisplayHintsTypeDef" = (
        dataclasses.field()
    )

    Title = field("Title")
    ShortDescription = field("ShortDescription")
    LongDescription = field("LongDescription")
    DocumentationTitle = field("DocumentationTitle")
    DocumentationLink = field("DocumentationLink")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegistrationTypeDisplayHintsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegistrationTypeDisplayHintsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SupportedAssociation:
    boto3_raw_data: "type_defs.SupportedAssociationTypeDef" = dataclasses.field()

    ResourceType = field("ResourceType")
    AssociationBehavior = field("AssociationBehavior")
    DisassociationBehavior = field("DisassociationBehavior")
    IsoCountryCode = field("IsoCountryCode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SupportedAssociationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SupportedAssociationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReleasePhoneNumberRequest:
    boto3_raw_data: "type_defs.ReleasePhoneNumberRequestTypeDef" = dataclasses.field()

    PhoneNumberId = field("PhoneNumberId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReleasePhoneNumberRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReleasePhoneNumberRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReleaseSenderIdRequest:
    boto3_raw_data: "type_defs.ReleaseSenderIdRequestTypeDef" = dataclasses.field()

    SenderId = field("SenderId")
    IsoCountryCode = field("IsoCountryCode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReleaseSenderIdRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReleaseSenderIdRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendDestinationNumberVerificationCodeRequest:
    boto3_raw_data: "type_defs.SendDestinationNumberVerificationCodeRequestTypeDef" = (
        dataclasses.field()
    )

    VerifiedDestinationNumberId = field("VerifiedDestinationNumberId")
    VerificationChannel = field("VerificationChannel")
    LanguageCode = field("LanguageCode")
    OriginationIdentity = field("OriginationIdentity")
    ConfigurationSetName = field("ConfigurationSetName")
    Context = field("Context")
    DestinationCountryParameters = field("DestinationCountryParameters")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SendDestinationNumberVerificationCodeRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendDestinationNumberVerificationCodeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendMediaMessageRequest:
    boto3_raw_data: "type_defs.SendMediaMessageRequestTypeDef" = dataclasses.field()

    DestinationPhoneNumber = field("DestinationPhoneNumber")
    OriginationIdentity = field("OriginationIdentity")
    MessageBody = field("MessageBody")
    MediaUrls = field("MediaUrls")
    ConfigurationSetName = field("ConfigurationSetName")
    MaxPrice = field("MaxPrice")
    TimeToLive = field("TimeToLive")
    Context = field("Context")
    DryRun = field("DryRun")
    ProtectConfigurationId = field("ProtectConfigurationId")
    MessageFeedbackEnabled = field("MessageFeedbackEnabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SendMediaMessageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendMediaMessageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendTextMessageRequest:
    boto3_raw_data: "type_defs.SendTextMessageRequestTypeDef" = dataclasses.field()

    DestinationPhoneNumber = field("DestinationPhoneNumber")
    OriginationIdentity = field("OriginationIdentity")
    MessageBody = field("MessageBody")
    MessageType = field("MessageType")
    Keyword = field("Keyword")
    ConfigurationSetName = field("ConfigurationSetName")
    MaxPrice = field("MaxPrice")
    TimeToLive = field("TimeToLive")
    Context = field("Context")
    DestinationCountryParameters = field("DestinationCountryParameters")
    DryRun = field("DryRun")
    ProtectConfigurationId = field("ProtectConfigurationId")
    MessageFeedbackEnabled = field("MessageFeedbackEnabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SendTextMessageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendTextMessageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendVoiceMessageRequest:
    boto3_raw_data: "type_defs.SendVoiceMessageRequestTypeDef" = dataclasses.field()

    DestinationPhoneNumber = field("DestinationPhoneNumber")
    OriginationIdentity = field("OriginationIdentity")
    MessageBody = field("MessageBody")
    MessageBodyTextType = field("MessageBodyTextType")
    VoiceId = field("VoiceId")
    ConfigurationSetName = field("ConfigurationSetName")
    MaxPricePerMinute = field("MaxPricePerMinute")
    TimeToLive = field("TimeToLive")
    Context = field("Context")
    DryRun = field("DryRun")
    ProtectConfigurationId = field("ProtectConfigurationId")
    MessageFeedbackEnabled = field("MessageFeedbackEnabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SendVoiceMessageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendVoiceMessageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetAccountDefaultProtectConfigurationRequest:
    boto3_raw_data: "type_defs.SetAccountDefaultProtectConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    ProtectConfigurationId = field("ProtectConfigurationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SetAccountDefaultProtectConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetAccountDefaultProtectConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetDefaultMessageFeedbackEnabledRequest:
    boto3_raw_data: "type_defs.SetDefaultMessageFeedbackEnabledRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigurationSetName = field("ConfigurationSetName")
    MessageFeedbackEnabled = field("MessageFeedbackEnabled")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SetDefaultMessageFeedbackEnabledRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetDefaultMessageFeedbackEnabledRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetDefaultMessageTypeRequest:
    boto3_raw_data: "type_defs.SetDefaultMessageTypeRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigurationSetName = field("ConfigurationSetName")
    MessageType = field("MessageType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SetDefaultMessageTypeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetDefaultMessageTypeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetDefaultSenderIdRequest:
    boto3_raw_data: "type_defs.SetDefaultSenderIdRequestTypeDef" = dataclasses.field()

    ConfigurationSetName = field("ConfigurationSetName")
    SenderId = field("SenderId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SetDefaultSenderIdRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetDefaultSenderIdRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetMediaMessageSpendLimitOverrideRequest:
    boto3_raw_data: "type_defs.SetMediaMessageSpendLimitOverrideRequestTypeDef" = (
        dataclasses.field()
    )

    MonthlyLimit = field("MonthlyLimit")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SetMediaMessageSpendLimitOverrideRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetMediaMessageSpendLimitOverrideRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetTextMessageSpendLimitOverrideRequest:
    boto3_raw_data: "type_defs.SetTextMessageSpendLimitOverrideRequestTypeDef" = (
        dataclasses.field()
    )

    MonthlyLimit = field("MonthlyLimit")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SetTextMessageSpendLimitOverrideRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetTextMessageSpendLimitOverrideRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetVoiceMessageSpendLimitOverrideRequest:
    boto3_raw_data: "type_defs.SetVoiceMessageSpendLimitOverrideRequestTypeDef" = (
        dataclasses.field()
    )

    MonthlyLimit = field("MonthlyLimit")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SetVoiceMessageSpendLimitOverrideRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetVoiceMessageSpendLimitOverrideRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubmitRegistrationVersionRequest:
    boto3_raw_data: "type_defs.SubmitRegistrationVersionRequestTypeDef" = (
        dataclasses.field()
    )

    RegistrationId = field("RegistrationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SubmitRegistrationVersionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubmitRegistrationVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagResourceRequest:
    boto3_raw_data: "type_defs.UntagResourceRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    TagKeys = field("TagKeys")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UntagResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UntagResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePhoneNumberRequest:
    boto3_raw_data: "type_defs.UpdatePhoneNumberRequestTypeDef" = dataclasses.field()

    PhoneNumberId = field("PhoneNumberId")
    TwoWayEnabled = field("TwoWayEnabled")
    TwoWayChannelArn = field("TwoWayChannelArn")
    TwoWayChannelRole = field("TwoWayChannelRole")
    SelfManagedOptOutsEnabled = field("SelfManagedOptOutsEnabled")
    OptOutListName = field("OptOutListName")
    InternationalSendingEnabled = field("InternationalSendingEnabled")
    DeletionProtectionEnabled = field("DeletionProtectionEnabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePhoneNumberRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePhoneNumberRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePoolRequest:
    boto3_raw_data: "type_defs.UpdatePoolRequestTypeDef" = dataclasses.field()

    PoolId = field("PoolId")
    TwoWayEnabled = field("TwoWayEnabled")
    TwoWayChannelArn = field("TwoWayChannelArn")
    TwoWayChannelRole = field("TwoWayChannelRole")
    SelfManagedOptOutsEnabled = field("SelfManagedOptOutsEnabled")
    OptOutListName = field("OptOutListName")
    SharedRoutesEnabled = field("SharedRoutesEnabled")
    DeletionProtectionEnabled = field("DeletionProtectionEnabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdatePoolRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePoolRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateProtectConfigurationRequest:
    boto3_raw_data: "type_defs.UpdateProtectConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    ProtectConfigurationId = field("ProtectConfigurationId")
    DeletionProtectionEnabled = field("DeletionProtectionEnabled")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateProtectConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateProtectConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSenderIdRequest:
    boto3_raw_data: "type_defs.UpdateSenderIdRequestTypeDef" = dataclasses.field()

    SenderId = field("SenderId")
    IsoCountryCode = field("IsoCountryCode")
    DeletionProtectionEnabled = field("DeletionProtectionEnabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSenderIdRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSenderIdRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VerifyDestinationNumberRequest:
    boto3_raw_data: "type_defs.VerifyDestinationNumberRequestTypeDef" = (
        dataclasses.field()
    )

    VerifiedDestinationNumberId = field("VerifiedDestinationNumberId")
    VerificationCode = field("VerificationCode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.VerifyDestinationNumberRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VerifyDestinationNumberRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateOriginationIdentityResult:
    boto3_raw_data: "type_defs.AssociateOriginationIdentityResultTypeDef" = (
        dataclasses.field()
    )

    PoolArn = field("PoolArn")
    PoolId = field("PoolId")
    OriginationIdentityArn = field("OriginationIdentityArn")
    OriginationIdentity = field("OriginationIdentity")
    IsoCountryCode = field("IsoCountryCode")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateOriginationIdentityResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateOriginationIdentityResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateProtectConfigurationResult:
    boto3_raw_data: "type_defs.AssociateProtectConfigurationResultTypeDef" = (
        dataclasses.field()
    )

    ConfigurationSetArn = field("ConfigurationSetArn")
    ConfigurationSetName = field("ConfigurationSetName")
    ProtectConfigurationArn = field("ProtectConfigurationArn")
    ProtectConfigurationId = field("ProtectConfigurationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateProtectConfigurationResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateProtectConfigurationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRegistrationAssociationResult:
    boto3_raw_data: "type_defs.CreateRegistrationAssociationResultTypeDef" = (
        dataclasses.field()
    )

    RegistrationArn = field("RegistrationArn")
    RegistrationId = field("RegistrationId")
    RegistrationType = field("RegistrationType")
    ResourceArn = field("ResourceArn")
    ResourceId = field("ResourceId")
    ResourceType = field("ResourceType")
    IsoCountryCode = field("IsoCountryCode")
    PhoneNumber = field("PhoneNumber")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateRegistrationAssociationResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRegistrationAssociationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAccountDefaultProtectConfigurationResult:
    boto3_raw_data: (
        "type_defs.DeleteAccountDefaultProtectConfigurationResultTypeDef"
    ) = dataclasses.field()

    DefaultProtectConfigurationArn = field("DefaultProtectConfigurationArn")
    DefaultProtectConfigurationId = field("DefaultProtectConfigurationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteAccountDefaultProtectConfigurationResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.DeleteAccountDefaultProtectConfigurationResultTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDefaultMessageTypeResult:
    boto3_raw_data: "type_defs.DeleteDefaultMessageTypeResultTypeDef" = (
        dataclasses.field()
    )

    ConfigurationSetArn = field("ConfigurationSetArn")
    ConfigurationSetName = field("ConfigurationSetName")
    MessageType = field("MessageType")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteDefaultMessageTypeResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDefaultMessageTypeResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDefaultSenderIdResult:
    boto3_raw_data: "type_defs.DeleteDefaultSenderIdResultTypeDef" = dataclasses.field()

    ConfigurationSetArn = field("ConfigurationSetArn")
    ConfigurationSetName = field("ConfigurationSetName")
    SenderId = field("SenderId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDefaultSenderIdResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDefaultSenderIdResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteKeywordResult:
    boto3_raw_data: "type_defs.DeleteKeywordResultTypeDef" = dataclasses.field()

    OriginationIdentityArn = field("OriginationIdentityArn")
    OriginationIdentity = field("OriginationIdentity")
    Keyword = field("Keyword")
    KeywordMessage = field("KeywordMessage")
    KeywordAction = field("KeywordAction")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteKeywordResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteKeywordResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMediaMessageSpendLimitOverrideResult:
    boto3_raw_data: "type_defs.DeleteMediaMessageSpendLimitOverrideResultTypeDef" = (
        dataclasses.field()
    )

    MonthlyLimit = field("MonthlyLimit")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteMediaMessageSpendLimitOverrideResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMediaMessageSpendLimitOverrideResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteOptOutListResult:
    boto3_raw_data: "type_defs.DeleteOptOutListResultTypeDef" = dataclasses.field()

    OptOutListArn = field("OptOutListArn")
    OptOutListName = field("OptOutListName")
    CreatedTimestamp = field("CreatedTimestamp")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteOptOutListResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteOptOutListResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteOptedOutNumberResult:
    boto3_raw_data: "type_defs.DeleteOptedOutNumberResultTypeDef" = dataclasses.field()

    OptOutListArn = field("OptOutListArn")
    OptOutListName = field("OptOutListName")
    OptedOutNumber = field("OptedOutNumber")
    OptedOutTimestamp = field("OptedOutTimestamp")
    EndUserOptedOut = field("EndUserOptedOut")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteOptedOutNumberResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteOptedOutNumberResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePoolResult:
    boto3_raw_data: "type_defs.DeletePoolResultTypeDef" = dataclasses.field()

    PoolArn = field("PoolArn")
    PoolId = field("PoolId")
    Status = field("Status")
    MessageType = field("MessageType")
    TwoWayEnabled = field("TwoWayEnabled")
    TwoWayChannelArn = field("TwoWayChannelArn")
    TwoWayChannelRole = field("TwoWayChannelRole")
    SelfManagedOptOutsEnabled = field("SelfManagedOptOutsEnabled")
    OptOutListName = field("OptOutListName")
    SharedRoutesEnabled = field("SharedRoutesEnabled")
    CreatedTimestamp = field("CreatedTimestamp")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeletePoolResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePoolResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteProtectConfigurationResult:
    boto3_raw_data: "type_defs.DeleteProtectConfigurationResultTypeDef" = (
        dataclasses.field()
    )

    ProtectConfigurationArn = field("ProtectConfigurationArn")
    ProtectConfigurationId = field("ProtectConfigurationId")
    CreatedTimestamp = field("CreatedTimestamp")
    AccountDefault = field("AccountDefault")
    DeletionProtectionEnabled = field("DeletionProtectionEnabled")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteProtectConfigurationResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteProtectConfigurationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteProtectConfigurationRuleSetNumberOverrideResult:
    boto3_raw_data: (
        "type_defs.DeleteProtectConfigurationRuleSetNumberOverrideResultTypeDef"
    ) = dataclasses.field()

    ProtectConfigurationArn = field("ProtectConfigurationArn")
    ProtectConfigurationId = field("ProtectConfigurationId")
    DestinationPhoneNumber = field("DestinationPhoneNumber")
    CreatedTimestamp = field("CreatedTimestamp")
    Action = field("Action")
    IsoCountryCode = field("IsoCountryCode")
    ExpirationTimestamp = field("ExpirationTimestamp")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteProtectConfigurationRuleSetNumberOverrideResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.DeleteProtectConfigurationRuleSetNumberOverrideResultTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRegistrationAttachmentResult:
    boto3_raw_data: "type_defs.DeleteRegistrationAttachmentResultTypeDef" = (
        dataclasses.field()
    )

    RegistrationAttachmentArn = field("RegistrationAttachmentArn")
    RegistrationAttachmentId = field("RegistrationAttachmentId")
    AttachmentStatus = field("AttachmentStatus")
    AttachmentUploadErrorReason = field("AttachmentUploadErrorReason")
    CreatedTimestamp = field("CreatedTimestamp")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteRegistrationAttachmentResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRegistrationAttachmentResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRegistrationFieldValueResult:
    boto3_raw_data: "type_defs.DeleteRegistrationFieldValueResultTypeDef" = (
        dataclasses.field()
    )

    RegistrationArn = field("RegistrationArn")
    RegistrationId = field("RegistrationId")
    VersionNumber = field("VersionNumber")
    FieldPath = field("FieldPath")
    SelectChoices = field("SelectChoices")
    TextValue = field("TextValue")
    RegistrationAttachmentId = field("RegistrationAttachmentId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteRegistrationFieldValueResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRegistrationFieldValueResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRegistrationResult:
    boto3_raw_data: "type_defs.DeleteRegistrationResultTypeDef" = dataclasses.field()

    RegistrationArn = field("RegistrationArn")
    RegistrationId = field("RegistrationId")
    RegistrationType = field("RegistrationType")
    RegistrationStatus = field("RegistrationStatus")
    CurrentVersionNumber = field("CurrentVersionNumber")
    ApprovedVersionNumber = field("ApprovedVersionNumber")
    LatestDeniedVersionNumber = field("LatestDeniedVersionNumber")
    AdditionalAttributes = field("AdditionalAttributes")
    CreatedTimestamp = field("CreatedTimestamp")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteRegistrationResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRegistrationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteResourcePolicyResult:
    boto3_raw_data: "type_defs.DeleteResourcePolicyResultTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    Policy = field("Policy")
    CreatedTimestamp = field("CreatedTimestamp")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteResourcePolicyResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteResourcePolicyResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTextMessageSpendLimitOverrideResult:
    boto3_raw_data: "type_defs.DeleteTextMessageSpendLimitOverrideResultTypeDef" = (
        dataclasses.field()
    )

    MonthlyLimit = field("MonthlyLimit")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteTextMessageSpendLimitOverrideResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTextMessageSpendLimitOverrideResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVerifiedDestinationNumberResult:
    boto3_raw_data: "type_defs.DeleteVerifiedDestinationNumberResultTypeDef" = (
        dataclasses.field()
    )

    VerifiedDestinationNumberArn = field("VerifiedDestinationNumberArn")
    VerifiedDestinationNumberId = field("VerifiedDestinationNumberId")
    DestinationPhoneNumber = field("DestinationPhoneNumber")
    CreatedTimestamp = field("CreatedTimestamp")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteVerifiedDestinationNumberResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVerifiedDestinationNumberResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVoiceMessageSpendLimitOverrideResult:
    boto3_raw_data: "type_defs.DeleteVoiceMessageSpendLimitOverrideResultTypeDef" = (
        dataclasses.field()
    )

    MonthlyLimit = field("MonthlyLimit")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteVoiceMessageSpendLimitOverrideResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVoiceMessageSpendLimitOverrideResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAccountAttributesResult:
    boto3_raw_data: "type_defs.DescribeAccountAttributesResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AccountAttributes(self):  # pragma: no cover
        return AccountAttribute.make_many(self.boto3_raw_data["AccountAttributes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeAccountAttributesResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAccountAttributesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAccountLimitsResult:
    boto3_raw_data: "type_defs.DescribeAccountLimitsResultTypeDef" = dataclasses.field()

    @cached_property
    def AccountLimits(self):  # pragma: no cover
        return AccountLimit.make_many(self.boto3_raw_data["AccountLimits"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAccountLimitsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAccountLimitsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateOriginationIdentityResult:
    boto3_raw_data: "type_defs.DisassociateOriginationIdentityResultTypeDef" = (
        dataclasses.field()
    )

    PoolArn = field("PoolArn")
    PoolId = field("PoolId")
    OriginationIdentityArn = field("OriginationIdentityArn")
    OriginationIdentity = field("OriginationIdentity")
    IsoCountryCode = field("IsoCountryCode")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateOriginationIdentityResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateOriginationIdentityResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateProtectConfigurationResult:
    boto3_raw_data: "type_defs.DisassociateProtectConfigurationResultTypeDef" = (
        dataclasses.field()
    )

    ConfigurationSetArn = field("ConfigurationSetArn")
    ConfigurationSetName = field("ConfigurationSetName")
    ProtectConfigurationArn = field("ProtectConfigurationArn")
    ProtectConfigurationId = field("ProtectConfigurationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateProtectConfigurationResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateProtectConfigurationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourcePolicyResult:
    boto3_raw_data: "type_defs.GetResourcePolicyResultTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    Policy = field("Policy")
    CreatedTimestamp = field("CreatedTimestamp")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourcePolicyResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourcePolicyResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutKeywordResult:
    boto3_raw_data: "type_defs.PutKeywordResultTypeDef" = dataclasses.field()

    OriginationIdentityArn = field("OriginationIdentityArn")
    OriginationIdentity = field("OriginationIdentity")
    Keyword = field("Keyword")
    KeywordMessage = field("KeywordMessage")
    KeywordAction = field("KeywordAction")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutKeywordResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutKeywordResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutMessageFeedbackResult:
    boto3_raw_data: "type_defs.PutMessageFeedbackResultTypeDef" = dataclasses.field()

    MessageId = field("MessageId")
    MessageFeedbackStatus = field("MessageFeedbackStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutMessageFeedbackResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutMessageFeedbackResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutOptedOutNumberResult:
    boto3_raw_data: "type_defs.PutOptedOutNumberResultTypeDef" = dataclasses.field()

    OptOutListArn = field("OptOutListArn")
    OptOutListName = field("OptOutListName")
    OptedOutNumber = field("OptedOutNumber")
    OptedOutTimestamp = field("OptedOutTimestamp")
    EndUserOptedOut = field("EndUserOptedOut")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutOptedOutNumberResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutOptedOutNumberResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutProtectConfigurationRuleSetNumberOverrideResult:
    boto3_raw_data: (
        "type_defs.PutProtectConfigurationRuleSetNumberOverrideResultTypeDef"
    ) = dataclasses.field()

    ProtectConfigurationArn = field("ProtectConfigurationArn")
    ProtectConfigurationId = field("ProtectConfigurationId")
    DestinationPhoneNumber = field("DestinationPhoneNumber")
    CreatedTimestamp = field("CreatedTimestamp")
    Action = field("Action")
    IsoCountryCode = field("IsoCountryCode")
    ExpirationTimestamp = field("ExpirationTimestamp")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutProtectConfigurationRuleSetNumberOverrideResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.PutProtectConfigurationRuleSetNumberOverrideResultTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutRegistrationFieldValueResult:
    boto3_raw_data: "type_defs.PutRegistrationFieldValueResultTypeDef" = (
        dataclasses.field()
    )

    RegistrationArn = field("RegistrationArn")
    RegistrationId = field("RegistrationId")
    VersionNumber = field("VersionNumber")
    FieldPath = field("FieldPath")
    SelectChoices = field("SelectChoices")
    TextValue = field("TextValue")
    RegistrationAttachmentId = field("RegistrationAttachmentId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutRegistrationFieldValueResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutRegistrationFieldValueResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutResourcePolicyResult:
    boto3_raw_data: "type_defs.PutResourcePolicyResultTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    Policy = field("Policy")
    CreatedTimestamp = field("CreatedTimestamp")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutResourcePolicyResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutResourcePolicyResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReleasePhoneNumberResult:
    boto3_raw_data: "type_defs.ReleasePhoneNumberResultTypeDef" = dataclasses.field()

    PhoneNumberArn = field("PhoneNumberArn")
    PhoneNumberId = field("PhoneNumberId")
    PhoneNumber = field("PhoneNumber")
    Status = field("Status")
    IsoCountryCode = field("IsoCountryCode")
    MessageType = field("MessageType")
    NumberCapabilities = field("NumberCapabilities")
    NumberType = field("NumberType")
    MonthlyLeasingPrice = field("MonthlyLeasingPrice")
    TwoWayEnabled = field("TwoWayEnabled")
    TwoWayChannelArn = field("TwoWayChannelArn")
    TwoWayChannelRole = field("TwoWayChannelRole")
    SelfManagedOptOutsEnabled = field("SelfManagedOptOutsEnabled")
    OptOutListName = field("OptOutListName")
    RegistrationId = field("RegistrationId")
    CreatedTimestamp = field("CreatedTimestamp")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReleasePhoneNumberResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReleasePhoneNumberResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReleaseSenderIdResult:
    boto3_raw_data: "type_defs.ReleaseSenderIdResultTypeDef" = dataclasses.field()

    SenderIdArn = field("SenderIdArn")
    SenderId = field("SenderId")
    IsoCountryCode = field("IsoCountryCode")
    MessageTypes = field("MessageTypes")
    MonthlyLeasingPrice = field("MonthlyLeasingPrice")
    Registered = field("Registered")
    RegistrationId = field("RegistrationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReleaseSenderIdResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReleaseSenderIdResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendDestinationNumberVerificationCodeResult:
    boto3_raw_data: "type_defs.SendDestinationNumberVerificationCodeResultTypeDef" = (
        dataclasses.field()
    )

    MessageId = field("MessageId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SendDestinationNumberVerificationCodeResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendDestinationNumberVerificationCodeResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendMediaMessageResult:
    boto3_raw_data: "type_defs.SendMediaMessageResultTypeDef" = dataclasses.field()

    MessageId = field("MessageId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SendMediaMessageResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendMediaMessageResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendTextMessageResult:
    boto3_raw_data: "type_defs.SendTextMessageResultTypeDef" = dataclasses.field()

    MessageId = field("MessageId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SendTextMessageResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendTextMessageResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendVoiceMessageResult:
    boto3_raw_data: "type_defs.SendVoiceMessageResultTypeDef" = dataclasses.field()

    MessageId = field("MessageId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SendVoiceMessageResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendVoiceMessageResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetAccountDefaultProtectConfigurationResult:
    boto3_raw_data: "type_defs.SetAccountDefaultProtectConfigurationResultTypeDef" = (
        dataclasses.field()
    )

    DefaultProtectConfigurationArn = field("DefaultProtectConfigurationArn")
    DefaultProtectConfigurationId = field("DefaultProtectConfigurationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SetAccountDefaultProtectConfigurationResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetAccountDefaultProtectConfigurationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetDefaultMessageFeedbackEnabledResult:
    boto3_raw_data: "type_defs.SetDefaultMessageFeedbackEnabledResultTypeDef" = (
        dataclasses.field()
    )

    ConfigurationSetArn = field("ConfigurationSetArn")
    ConfigurationSetName = field("ConfigurationSetName")
    MessageFeedbackEnabled = field("MessageFeedbackEnabled")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SetDefaultMessageFeedbackEnabledResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetDefaultMessageFeedbackEnabledResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetDefaultMessageTypeResult:
    boto3_raw_data: "type_defs.SetDefaultMessageTypeResultTypeDef" = dataclasses.field()

    ConfigurationSetArn = field("ConfigurationSetArn")
    ConfigurationSetName = field("ConfigurationSetName")
    MessageType = field("MessageType")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SetDefaultMessageTypeResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetDefaultMessageTypeResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetDefaultSenderIdResult:
    boto3_raw_data: "type_defs.SetDefaultSenderIdResultTypeDef" = dataclasses.field()

    ConfigurationSetArn = field("ConfigurationSetArn")
    ConfigurationSetName = field("ConfigurationSetName")
    SenderId = field("SenderId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SetDefaultSenderIdResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetDefaultSenderIdResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetMediaMessageSpendLimitOverrideResult:
    boto3_raw_data: "type_defs.SetMediaMessageSpendLimitOverrideResultTypeDef" = (
        dataclasses.field()
    )

    MonthlyLimit = field("MonthlyLimit")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SetMediaMessageSpendLimitOverrideResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetMediaMessageSpendLimitOverrideResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetTextMessageSpendLimitOverrideResult:
    boto3_raw_data: "type_defs.SetTextMessageSpendLimitOverrideResultTypeDef" = (
        dataclasses.field()
    )

    MonthlyLimit = field("MonthlyLimit")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SetTextMessageSpendLimitOverrideResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetTextMessageSpendLimitOverrideResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetVoiceMessageSpendLimitOverrideResult:
    boto3_raw_data: "type_defs.SetVoiceMessageSpendLimitOverrideResultTypeDef" = (
        dataclasses.field()
    )

    MonthlyLimit = field("MonthlyLimit")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SetVoiceMessageSpendLimitOverrideResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetVoiceMessageSpendLimitOverrideResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePhoneNumberResult:
    boto3_raw_data: "type_defs.UpdatePhoneNumberResultTypeDef" = dataclasses.field()

    PhoneNumberArn = field("PhoneNumberArn")
    PhoneNumberId = field("PhoneNumberId")
    PhoneNumber = field("PhoneNumber")
    Status = field("Status")
    IsoCountryCode = field("IsoCountryCode")
    MessageType = field("MessageType")
    NumberCapabilities = field("NumberCapabilities")
    NumberType = field("NumberType")
    MonthlyLeasingPrice = field("MonthlyLeasingPrice")
    TwoWayEnabled = field("TwoWayEnabled")
    TwoWayChannelArn = field("TwoWayChannelArn")
    TwoWayChannelRole = field("TwoWayChannelRole")
    SelfManagedOptOutsEnabled = field("SelfManagedOptOutsEnabled")
    OptOutListName = field("OptOutListName")
    InternationalSendingEnabled = field("InternationalSendingEnabled")
    DeletionProtectionEnabled = field("DeletionProtectionEnabled")
    RegistrationId = field("RegistrationId")
    CreatedTimestamp = field("CreatedTimestamp")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePhoneNumberResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePhoneNumberResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePoolResult:
    boto3_raw_data: "type_defs.UpdatePoolResultTypeDef" = dataclasses.field()

    PoolArn = field("PoolArn")
    PoolId = field("PoolId")
    Status = field("Status")
    MessageType = field("MessageType")
    TwoWayEnabled = field("TwoWayEnabled")
    TwoWayChannelArn = field("TwoWayChannelArn")
    TwoWayChannelRole = field("TwoWayChannelRole")
    SelfManagedOptOutsEnabled = field("SelfManagedOptOutsEnabled")
    OptOutListName = field("OptOutListName")
    SharedRoutesEnabled = field("SharedRoutesEnabled")
    DeletionProtectionEnabled = field("DeletionProtectionEnabled")
    CreatedTimestamp = field("CreatedTimestamp")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdatePoolResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePoolResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateProtectConfigurationResult:
    boto3_raw_data: "type_defs.UpdateProtectConfigurationResultTypeDef" = (
        dataclasses.field()
    )

    ProtectConfigurationArn = field("ProtectConfigurationArn")
    ProtectConfigurationId = field("ProtectConfigurationId")
    CreatedTimestamp = field("CreatedTimestamp")
    AccountDefault = field("AccountDefault")
    DeletionProtectionEnabled = field("DeletionProtectionEnabled")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateProtectConfigurationResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateProtectConfigurationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSenderIdResult:
    boto3_raw_data: "type_defs.UpdateSenderIdResultTypeDef" = dataclasses.field()

    SenderIdArn = field("SenderIdArn")
    SenderId = field("SenderId")
    IsoCountryCode = field("IsoCountryCode")
    MessageTypes = field("MessageTypes")
    MonthlyLeasingPrice = field("MonthlyLeasingPrice")
    DeletionProtectionEnabled = field("DeletionProtectionEnabled")
    Registered = field("Registered")
    RegistrationId = field("RegistrationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSenderIdResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSenderIdResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VerifyDestinationNumberResult:
    boto3_raw_data: "type_defs.VerifyDestinationNumberResultTypeDef" = (
        dataclasses.field()
    )

    VerifiedDestinationNumberArn = field("VerifiedDestinationNumberArn")
    VerifiedDestinationNumberId = field("VerifiedDestinationNumberId")
    DestinationPhoneNumber = field("DestinationPhoneNumber")
    Status = field("Status")
    CreatedTimestamp = field("CreatedTimestamp")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.VerifyDestinationNumberResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VerifyDestinationNumberResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConfigurationSetsRequest:
    boto3_raw_data: "type_defs.DescribeConfigurationSetsRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigurationSetNames = field("ConfigurationSetNames")

    @cached_property
    def Filters(self):  # pragma: no cover
        return ConfigurationSetFilter.make_many(self.boto3_raw_data["Filters"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeConfigurationSetsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConfigurationSetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConfigurationSetRequest:
    boto3_raw_data: "type_defs.CreateConfigurationSetRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigurationSetName = field("ConfigurationSetName")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateConfigurationSetRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConfigurationSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConfigurationSetResult:
    boto3_raw_data: "type_defs.CreateConfigurationSetResultTypeDef" = (
        dataclasses.field()
    )

    ConfigurationSetArn = field("ConfigurationSetArn")
    ConfigurationSetName = field("ConfigurationSetName")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    CreatedTimestamp = field("CreatedTimestamp")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateConfigurationSetResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConfigurationSetResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateOptOutListRequest:
    boto3_raw_data: "type_defs.CreateOptOutListRequestTypeDef" = dataclasses.field()

    OptOutListName = field("OptOutListName")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateOptOutListRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateOptOutListRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateOptOutListResult:
    boto3_raw_data: "type_defs.CreateOptOutListResultTypeDef" = dataclasses.field()

    OptOutListArn = field("OptOutListArn")
    OptOutListName = field("OptOutListName")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    CreatedTimestamp = field("CreatedTimestamp")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateOptOutListResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateOptOutListResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePoolRequest:
    boto3_raw_data: "type_defs.CreatePoolRequestTypeDef" = dataclasses.field()

    OriginationIdentity = field("OriginationIdentity")
    IsoCountryCode = field("IsoCountryCode")
    MessageType = field("MessageType")
    DeletionProtectionEnabled = field("DeletionProtectionEnabled")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    ClientToken = field("ClientToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreatePoolRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePoolRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePoolResult:
    boto3_raw_data: "type_defs.CreatePoolResultTypeDef" = dataclasses.field()

    PoolArn = field("PoolArn")
    PoolId = field("PoolId")
    Status = field("Status")
    MessageType = field("MessageType")
    TwoWayEnabled = field("TwoWayEnabled")
    TwoWayChannelArn = field("TwoWayChannelArn")
    TwoWayChannelRole = field("TwoWayChannelRole")
    SelfManagedOptOutsEnabled = field("SelfManagedOptOutsEnabled")
    OptOutListName = field("OptOutListName")
    SharedRoutesEnabled = field("SharedRoutesEnabled")
    DeletionProtectionEnabled = field("DeletionProtectionEnabled")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    CreatedTimestamp = field("CreatedTimestamp")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreatePoolResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePoolResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateProtectConfigurationRequest:
    boto3_raw_data: "type_defs.CreateProtectConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    ClientToken = field("ClientToken")
    DeletionProtectionEnabled = field("DeletionProtectionEnabled")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateProtectConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateProtectConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateProtectConfigurationResult:
    boto3_raw_data: "type_defs.CreateProtectConfigurationResultTypeDef" = (
        dataclasses.field()
    )

    ProtectConfigurationArn = field("ProtectConfigurationArn")
    ProtectConfigurationId = field("ProtectConfigurationId")
    CreatedTimestamp = field("CreatedTimestamp")
    AccountDefault = field("AccountDefault")
    DeletionProtectionEnabled = field("DeletionProtectionEnabled")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateProtectConfigurationResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateProtectConfigurationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRegistrationAttachmentRequest:
    boto3_raw_data: "type_defs.CreateRegistrationAttachmentRequestTypeDef" = (
        dataclasses.field()
    )

    AttachmentBody = field("AttachmentBody")
    AttachmentUrl = field("AttachmentUrl")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateRegistrationAttachmentRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRegistrationAttachmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRegistrationAttachmentResult:
    boto3_raw_data: "type_defs.CreateRegistrationAttachmentResultTypeDef" = (
        dataclasses.field()
    )

    RegistrationAttachmentArn = field("RegistrationAttachmentArn")
    RegistrationAttachmentId = field("RegistrationAttachmentId")
    AttachmentStatus = field("AttachmentStatus")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    CreatedTimestamp = field("CreatedTimestamp")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateRegistrationAttachmentResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRegistrationAttachmentResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRegistrationRequest:
    boto3_raw_data: "type_defs.CreateRegistrationRequestTypeDef" = dataclasses.field()

    RegistrationType = field("RegistrationType")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRegistrationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRegistrationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRegistrationResult:
    boto3_raw_data: "type_defs.CreateRegistrationResultTypeDef" = dataclasses.field()

    RegistrationArn = field("RegistrationArn")
    RegistrationId = field("RegistrationId")
    RegistrationType = field("RegistrationType")
    RegistrationStatus = field("RegistrationStatus")
    CurrentVersionNumber = field("CurrentVersionNumber")
    AdditionalAttributes = field("AdditionalAttributes")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    CreatedTimestamp = field("CreatedTimestamp")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRegistrationResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRegistrationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVerifiedDestinationNumberRequest:
    boto3_raw_data: "type_defs.CreateVerifiedDestinationNumberRequestTypeDef" = (
        dataclasses.field()
    )

    DestinationPhoneNumber = field("DestinationPhoneNumber")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateVerifiedDestinationNumberRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVerifiedDestinationNumberRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVerifiedDestinationNumberResult:
    boto3_raw_data: "type_defs.CreateVerifiedDestinationNumberResultTypeDef" = (
        dataclasses.field()
    )

    VerifiedDestinationNumberArn = field("VerifiedDestinationNumberArn")
    VerifiedDestinationNumberId = field("VerifiedDestinationNumberId")
    DestinationPhoneNumber = field("DestinationPhoneNumber")
    Status = field("Status")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    CreatedTimestamp = field("CreatedTimestamp")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateVerifiedDestinationNumberResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVerifiedDestinationNumberResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceResult:
    boto3_raw_data: "type_defs.ListTagsForResourceResultTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RequestPhoneNumberRequest:
    boto3_raw_data: "type_defs.RequestPhoneNumberRequestTypeDef" = dataclasses.field()

    IsoCountryCode = field("IsoCountryCode")
    MessageType = field("MessageType")
    NumberCapabilities = field("NumberCapabilities")
    NumberType = field("NumberType")
    OptOutListName = field("OptOutListName")
    PoolId = field("PoolId")
    RegistrationId = field("RegistrationId")
    InternationalSendingEnabled = field("InternationalSendingEnabled")
    DeletionProtectionEnabled = field("DeletionProtectionEnabled")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RequestPhoneNumberRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RequestPhoneNumberRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RequestPhoneNumberResult:
    boto3_raw_data: "type_defs.RequestPhoneNumberResultTypeDef" = dataclasses.field()

    PhoneNumberArn = field("PhoneNumberArn")
    PhoneNumberId = field("PhoneNumberId")
    PhoneNumber = field("PhoneNumber")
    Status = field("Status")
    IsoCountryCode = field("IsoCountryCode")
    MessageType = field("MessageType")
    NumberCapabilities = field("NumberCapabilities")
    NumberType = field("NumberType")
    MonthlyLeasingPrice = field("MonthlyLeasingPrice")
    TwoWayEnabled = field("TwoWayEnabled")
    TwoWayChannelArn = field("TwoWayChannelArn")
    TwoWayChannelRole = field("TwoWayChannelRole")
    SelfManagedOptOutsEnabled = field("SelfManagedOptOutsEnabled")
    OptOutListName = field("OptOutListName")
    InternationalSendingEnabled = field("InternationalSendingEnabled")
    DeletionProtectionEnabled = field("DeletionProtectionEnabled")
    PoolId = field("PoolId")
    RegistrationId = field("RegistrationId")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    CreatedTimestamp = field("CreatedTimestamp")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RequestPhoneNumberResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RequestPhoneNumberResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RequestSenderIdRequest:
    boto3_raw_data: "type_defs.RequestSenderIdRequestTypeDef" = dataclasses.field()

    SenderId = field("SenderId")
    IsoCountryCode = field("IsoCountryCode")
    MessageTypes = field("MessageTypes")
    DeletionProtectionEnabled = field("DeletionProtectionEnabled")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RequestSenderIdRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RequestSenderIdRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RequestSenderIdResult:
    boto3_raw_data: "type_defs.RequestSenderIdResultTypeDef" = dataclasses.field()

    SenderIdArn = field("SenderIdArn")
    SenderId = field("SenderId")
    IsoCountryCode = field("IsoCountryCode")
    MessageTypes = field("MessageTypes")
    MonthlyLeasingPrice = field("MonthlyLeasingPrice")
    DeletionProtectionEnabled = field("DeletionProtectionEnabled")
    Registered = field("Registered")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RequestSenderIdResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RequestSenderIdResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagResourceRequest:
    boto3_raw_data: "type_defs.TagResourceRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TagResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEventDestinationRequest:
    boto3_raw_data: "type_defs.CreateEventDestinationRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigurationSetName = field("ConfigurationSetName")
    EventDestinationName = field("EventDestinationName")
    MatchingEventTypes = field("MatchingEventTypes")

    @cached_property
    def CloudWatchLogsDestination(self):  # pragma: no cover
        return CloudWatchLogsDestination.make_one(
            self.boto3_raw_data["CloudWatchLogsDestination"]
        )

    @cached_property
    def KinesisFirehoseDestination(self):  # pragma: no cover
        return KinesisFirehoseDestination.make_one(
            self.boto3_raw_data["KinesisFirehoseDestination"]
        )

    @cached_property
    def SnsDestination(self):  # pragma: no cover
        return SnsDestination.make_one(self.boto3_raw_data["SnsDestination"])

    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateEventDestinationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEventDestinationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventDestination:
    boto3_raw_data: "type_defs.EventDestinationTypeDef" = dataclasses.field()

    EventDestinationName = field("EventDestinationName")
    Enabled = field("Enabled")
    MatchingEventTypes = field("MatchingEventTypes")

    @cached_property
    def CloudWatchLogsDestination(self):  # pragma: no cover
        return CloudWatchLogsDestination.make_one(
            self.boto3_raw_data["CloudWatchLogsDestination"]
        )

    @cached_property
    def KinesisFirehoseDestination(self):  # pragma: no cover
        return KinesisFirehoseDestination.make_one(
            self.boto3_raw_data["KinesisFirehoseDestination"]
        )

    @cached_property
    def SnsDestination(self):  # pragma: no cover
        return SnsDestination.make_one(self.boto3_raw_data["SnsDestination"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventDestinationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventDestinationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEventDestinationRequest:
    boto3_raw_data: "type_defs.UpdateEventDestinationRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigurationSetName = field("ConfigurationSetName")
    EventDestinationName = field("EventDestinationName")
    Enabled = field("Enabled")
    MatchingEventTypes = field("MatchingEventTypes")

    @cached_property
    def CloudWatchLogsDestination(self):  # pragma: no cover
        return CloudWatchLogsDestination.make_one(
            self.boto3_raw_data["CloudWatchLogsDestination"]
        )

    @cached_property
    def KinesisFirehoseDestination(self):  # pragma: no cover
        return KinesisFirehoseDestination.make_one(
            self.boto3_raw_data["KinesisFirehoseDestination"]
        )

    @cached_property
    def SnsDestination(self):  # pragma: no cover
        return SnsDestination.make_one(self.boto3_raw_data["SnsDestination"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateEventDestinationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEventDestinationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRegistrationVersionResult:
    boto3_raw_data: "type_defs.CreateRegistrationVersionResultTypeDef" = (
        dataclasses.field()
    )

    RegistrationArn = field("RegistrationArn")
    RegistrationId = field("RegistrationId")
    VersionNumber = field("VersionNumber")
    RegistrationVersionStatus = field("RegistrationVersionStatus")

    @cached_property
    def RegistrationVersionStatusHistory(self):  # pragma: no cover
        return RegistrationVersionStatusHistory.make_one(
            self.boto3_raw_data["RegistrationVersionStatusHistory"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateRegistrationVersionResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRegistrationVersionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DiscardRegistrationVersionResult:
    boto3_raw_data: "type_defs.DiscardRegistrationVersionResultTypeDef" = (
        dataclasses.field()
    )

    RegistrationArn = field("RegistrationArn")
    RegistrationId = field("RegistrationId")
    VersionNumber = field("VersionNumber")
    RegistrationVersionStatus = field("RegistrationVersionStatus")

    @cached_property
    def RegistrationVersionStatusHistory(self):  # pragma: no cover
        return RegistrationVersionStatusHistory.make_one(
            self.boto3_raw_data["RegistrationVersionStatusHistory"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DiscardRegistrationVersionResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DiscardRegistrationVersionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubmitRegistrationVersionResult:
    boto3_raw_data: "type_defs.SubmitRegistrationVersionResultTypeDef" = (
        dataclasses.field()
    )

    RegistrationArn = field("RegistrationArn")
    RegistrationId = field("RegistrationId")
    VersionNumber = field("VersionNumber")
    RegistrationVersionStatus = field("RegistrationVersionStatus")

    @cached_property
    def RegistrationVersionStatusHistory(self):  # pragma: no cover
        return RegistrationVersionStatusHistory.make_one(
            self.boto3_raw_data["RegistrationVersionStatusHistory"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SubmitRegistrationVersionResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubmitRegistrationVersionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAccountAttributesRequestPaginate:
    boto3_raw_data: "type_defs.DescribeAccountAttributesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAccountAttributesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAccountAttributesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAccountLimitsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeAccountLimitsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAccountLimitsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAccountLimitsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConfigurationSetsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeConfigurationSetsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ConfigurationSetNames = field("ConfigurationSetNames")

    @cached_property
    def Filters(self):  # pragma: no cover
        return ConfigurationSetFilter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeConfigurationSetsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConfigurationSetsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOptOutListsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeOptOutListsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    OptOutListNames = field("OptOutListNames")
    Owner = field("Owner")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeOptOutListsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeOptOutListsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRegistrationFieldDefinitionsRequestPaginate:
    boto3_raw_data: (
        "type_defs.DescribeRegistrationFieldDefinitionsRequestPaginateTypeDef"
    ) = dataclasses.field()

    RegistrationType = field("RegistrationType")
    SectionPath = field("SectionPath")
    FieldPaths = field("FieldPaths")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRegistrationFieldDefinitionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.DescribeRegistrationFieldDefinitionsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRegistrationFieldValuesRequestPaginate:
    boto3_raw_data: (
        "type_defs.DescribeRegistrationFieldValuesRequestPaginateTypeDef"
    ) = dataclasses.field()

    RegistrationId = field("RegistrationId")
    VersionNumber = field("VersionNumber")
    SectionPath = field("SectionPath")
    FieldPaths = field("FieldPaths")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRegistrationFieldValuesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.DescribeRegistrationFieldValuesRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRegistrationSectionDefinitionsRequestPaginate:
    boto3_raw_data: (
        "type_defs.DescribeRegistrationSectionDefinitionsRequestPaginateTypeDef"
    ) = dataclasses.field()

    RegistrationType = field("RegistrationType")
    SectionPaths = field("SectionPaths")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRegistrationSectionDefinitionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.DescribeRegistrationSectionDefinitionsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSpendLimitsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeSpendLimitsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeSpendLimitsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSpendLimitsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeKeywordsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeKeywordsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    OriginationIdentity = field("OriginationIdentity")
    Keywords = field("Keywords")

    @cached_property
    def Filters(self):  # pragma: no cover
        return KeywordFilter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeKeywordsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeKeywordsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeKeywordsRequest:
    boto3_raw_data: "type_defs.DescribeKeywordsRequestTypeDef" = dataclasses.field()

    OriginationIdentity = field("OriginationIdentity")
    Keywords = field("Keywords")

    @cached_property
    def Filters(self):  # pragma: no cover
        return KeywordFilter.make_many(self.boto3_raw_data["Filters"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeKeywordsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeKeywordsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeKeywordsResult:
    boto3_raw_data: "type_defs.DescribeKeywordsResultTypeDef" = dataclasses.field()

    OriginationIdentityArn = field("OriginationIdentityArn")
    OriginationIdentity = field("OriginationIdentity")

    @cached_property
    def Keywords(self):  # pragma: no cover
        return KeywordInformation.make_many(self.boto3_raw_data["Keywords"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeKeywordsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeKeywordsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOptOutListsResult:
    boto3_raw_data: "type_defs.DescribeOptOutListsResultTypeDef" = dataclasses.field()

    @cached_property
    def OptOutLists(self):  # pragma: no cover
        return OptOutListInformation.make_many(self.boto3_raw_data["OptOutLists"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeOptOutListsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeOptOutListsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOptedOutNumbersRequestPaginate:
    boto3_raw_data: "type_defs.DescribeOptedOutNumbersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    OptOutListName = field("OptOutListName")
    OptedOutNumbers = field("OptedOutNumbers")

    @cached_property
    def Filters(self):  # pragma: no cover
        return OptedOutFilter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeOptedOutNumbersRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeOptedOutNumbersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOptedOutNumbersRequest:
    boto3_raw_data: "type_defs.DescribeOptedOutNumbersRequestTypeDef" = (
        dataclasses.field()
    )

    OptOutListName = field("OptOutListName")
    OptedOutNumbers = field("OptedOutNumbers")

    @cached_property
    def Filters(self):  # pragma: no cover
        return OptedOutFilter.make_many(self.boto3_raw_data["Filters"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeOptedOutNumbersRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeOptedOutNumbersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOptedOutNumbersResult:
    boto3_raw_data: "type_defs.DescribeOptedOutNumbersResultTypeDef" = (
        dataclasses.field()
    )

    OptOutListArn = field("OptOutListArn")
    OptOutListName = field("OptOutListName")

    @cached_property
    def OptedOutNumbers(self):  # pragma: no cover
        return OptedOutNumberInformation.make_many(
            self.boto3_raw_data["OptedOutNumbers"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeOptedOutNumbersResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeOptedOutNumbersResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePhoneNumbersRequestPaginate:
    boto3_raw_data: "type_defs.DescribePhoneNumbersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    PhoneNumberIds = field("PhoneNumberIds")

    @cached_property
    def Filters(self):  # pragma: no cover
        return PhoneNumberFilter.make_many(self.boto3_raw_data["Filters"])

    Owner = field("Owner")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribePhoneNumbersRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePhoneNumbersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePhoneNumbersRequest:
    boto3_raw_data: "type_defs.DescribePhoneNumbersRequestTypeDef" = dataclasses.field()

    PhoneNumberIds = field("PhoneNumberIds")

    @cached_property
    def Filters(self):  # pragma: no cover
        return PhoneNumberFilter.make_many(self.boto3_raw_data["Filters"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    Owner = field("Owner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribePhoneNumbersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePhoneNumbersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePhoneNumbersResult:
    boto3_raw_data: "type_defs.DescribePhoneNumbersResultTypeDef" = dataclasses.field()

    @cached_property
    def PhoneNumbers(self):  # pragma: no cover
        return PhoneNumberInformation.make_many(self.boto3_raw_data["PhoneNumbers"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribePhoneNumbersResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePhoneNumbersResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePoolsRequestPaginate:
    boto3_raw_data: "type_defs.DescribePoolsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    PoolIds = field("PoolIds")

    @cached_property
    def Filters(self):  # pragma: no cover
        return PoolFilter.make_many(self.boto3_raw_data["Filters"])

    Owner = field("Owner")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribePoolsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePoolsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePoolsRequest:
    boto3_raw_data: "type_defs.DescribePoolsRequestTypeDef" = dataclasses.field()

    PoolIds = field("PoolIds")

    @cached_property
    def Filters(self):  # pragma: no cover
        return PoolFilter.make_many(self.boto3_raw_data["Filters"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    Owner = field("Owner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribePoolsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePoolsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePoolsResult:
    boto3_raw_data: "type_defs.DescribePoolsResultTypeDef" = dataclasses.field()

    @cached_property
    def Pools(self):  # pragma: no cover
        return PoolInformation.make_many(self.boto3_raw_data["Pools"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribePoolsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePoolsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeProtectConfigurationsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeProtectConfigurationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ProtectConfigurationIds = field("ProtectConfigurationIds")

    @cached_property
    def Filters(self):  # pragma: no cover
        return ProtectConfigurationFilter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeProtectConfigurationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeProtectConfigurationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeProtectConfigurationsRequest:
    boto3_raw_data: "type_defs.DescribeProtectConfigurationsRequestTypeDef" = (
        dataclasses.field()
    )

    ProtectConfigurationIds = field("ProtectConfigurationIds")

    @cached_property
    def Filters(self):  # pragma: no cover
        return ProtectConfigurationFilter.make_many(self.boto3_raw_data["Filters"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeProtectConfigurationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeProtectConfigurationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeProtectConfigurationsResult:
    boto3_raw_data: "type_defs.DescribeProtectConfigurationsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ProtectConfigurations(self):  # pragma: no cover
        return ProtectConfigurationInformation.make_many(
            self.boto3_raw_data["ProtectConfigurations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeProtectConfigurationsResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeProtectConfigurationsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRegistrationAttachmentsRequestPaginate:
    boto3_raw_data: (
        "type_defs.DescribeRegistrationAttachmentsRequestPaginateTypeDef"
    ) = dataclasses.field()

    RegistrationAttachmentIds = field("RegistrationAttachmentIds")

    @cached_property
    def Filters(self):  # pragma: no cover
        return RegistrationAttachmentFilter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRegistrationAttachmentsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.DescribeRegistrationAttachmentsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRegistrationAttachmentsRequest:
    boto3_raw_data: "type_defs.DescribeRegistrationAttachmentsRequestTypeDef" = (
        dataclasses.field()
    )

    RegistrationAttachmentIds = field("RegistrationAttachmentIds")

    @cached_property
    def Filters(self):  # pragma: no cover
        return RegistrationAttachmentFilter.make_many(self.boto3_raw_data["Filters"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRegistrationAttachmentsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRegistrationAttachmentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRegistrationAttachmentsResult:
    boto3_raw_data: "type_defs.DescribeRegistrationAttachmentsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RegistrationAttachments(self):  # pragma: no cover
        return RegistrationAttachmentsInformation.make_many(
            self.boto3_raw_data["RegistrationAttachments"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRegistrationAttachmentsResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRegistrationAttachmentsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRegistrationFieldValuesResult:
    boto3_raw_data: "type_defs.DescribeRegistrationFieldValuesResultTypeDef" = (
        dataclasses.field()
    )

    RegistrationArn = field("RegistrationArn")
    RegistrationId = field("RegistrationId")
    VersionNumber = field("VersionNumber")

    @cached_property
    def RegistrationFieldValues(self):  # pragma: no cover
        return RegistrationFieldValueInformation.make_many(
            self.boto3_raw_data["RegistrationFieldValues"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRegistrationFieldValuesResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRegistrationFieldValuesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRegistrationTypeDefinitionsRequestPaginate:
    boto3_raw_data: (
        "type_defs.DescribeRegistrationTypeDefinitionsRequestPaginateTypeDef"
    ) = dataclasses.field()

    RegistrationTypes = field("RegistrationTypes")

    @cached_property
    def Filters(self):  # pragma: no cover
        return RegistrationTypeFilter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRegistrationTypeDefinitionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.DescribeRegistrationTypeDefinitionsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRegistrationTypeDefinitionsRequest:
    boto3_raw_data: "type_defs.DescribeRegistrationTypeDefinitionsRequestTypeDef" = (
        dataclasses.field()
    )

    RegistrationTypes = field("RegistrationTypes")

    @cached_property
    def Filters(self):  # pragma: no cover
        return RegistrationTypeFilter.make_many(self.boto3_raw_data["Filters"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRegistrationTypeDefinitionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRegistrationTypeDefinitionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRegistrationVersionsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeRegistrationVersionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    RegistrationId = field("RegistrationId")
    VersionNumbers = field("VersionNumbers")

    @cached_property
    def Filters(self):  # pragma: no cover
        return RegistrationVersionFilter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRegistrationVersionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRegistrationVersionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRegistrationVersionsRequest:
    boto3_raw_data: "type_defs.DescribeRegistrationVersionsRequestTypeDef" = (
        dataclasses.field()
    )

    RegistrationId = field("RegistrationId")
    VersionNumbers = field("VersionNumbers")

    @cached_property
    def Filters(self):  # pragma: no cover
        return RegistrationVersionFilter.make_many(self.boto3_raw_data["Filters"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRegistrationVersionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRegistrationVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRegistrationsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeRegistrationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    RegistrationIds = field("RegistrationIds")

    @cached_property
    def Filters(self):  # pragma: no cover
        return RegistrationFilter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRegistrationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRegistrationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRegistrationsRequest:
    boto3_raw_data: "type_defs.DescribeRegistrationsRequestTypeDef" = (
        dataclasses.field()
    )

    RegistrationIds = field("RegistrationIds")

    @cached_property
    def Filters(self):  # pragma: no cover
        return RegistrationFilter.make_many(self.boto3_raw_data["Filters"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeRegistrationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRegistrationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRegistrationsResult:
    boto3_raw_data: "type_defs.DescribeRegistrationsResultTypeDef" = dataclasses.field()

    @cached_property
    def Registrations(self):  # pragma: no cover
        return RegistrationInformation.make_many(self.boto3_raw_data["Registrations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeRegistrationsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRegistrationsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSenderIdsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeSenderIdsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SenderIds(self):  # pragma: no cover
        return SenderIdAndCountry.make_many(self.boto3_raw_data["SenderIds"])

    @cached_property
    def Filters(self):  # pragma: no cover
        return SenderIdFilter.make_many(self.boto3_raw_data["Filters"])

    Owner = field("Owner")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeSenderIdsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSenderIdsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSenderIdsRequest:
    boto3_raw_data: "type_defs.DescribeSenderIdsRequestTypeDef" = dataclasses.field()

    @cached_property
    def SenderIds(self):  # pragma: no cover
        return SenderIdAndCountry.make_many(self.boto3_raw_data["SenderIds"])

    @cached_property
    def Filters(self):  # pragma: no cover
        return SenderIdFilter.make_many(self.boto3_raw_data["Filters"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    Owner = field("Owner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeSenderIdsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSenderIdsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSenderIdsResult:
    boto3_raw_data: "type_defs.DescribeSenderIdsResultTypeDef" = dataclasses.field()

    @cached_property
    def SenderIds(self):  # pragma: no cover
        return SenderIdInformation.make_many(self.boto3_raw_data["SenderIds"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeSenderIdsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSenderIdsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSpendLimitsResult:
    boto3_raw_data: "type_defs.DescribeSpendLimitsResultTypeDef" = dataclasses.field()

    @cached_property
    def SpendLimits(self):  # pragma: no cover
        return SpendLimit.make_many(self.boto3_raw_data["SpendLimits"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeSpendLimitsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSpendLimitsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeVerifiedDestinationNumbersRequestPaginate:
    boto3_raw_data: (
        "type_defs.DescribeVerifiedDestinationNumbersRequestPaginateTypeDef"
    ) = dataclasses.field()

    VerifiedDestinationNumberIds = field("VerifiedDestinationNumberIds")
    DestinationPhoneNumbers = field("DestinationPhoneNumbers")

    @cached_property
    def Filters(self):  # pragma: no cover
        return VerifiedDestinationNumberFilter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeVerifiedDestinationNumbersRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.DescribeVerifiedDestinationNumbersRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeVerifiedDestinationNumbersRequest:
    boto3_raw_data: "type_defs.DescribeVerifiedDestinationNumbersRequestTypeDef" = (
        dataclasses.field()
    )

    VerifiedDestinationNumberIds = field("VerifiedDestinationNumberIds")
    DestinationPhoneNumbers = field("DestinationPhoneNumbers")

    @cached_property
    def Filters(self):  # pragma: no cover
        return VerifiedDestinationNumberFilter.make_many(self.boto3_raw_data["Filters"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeVerifiedDestinationNumbersRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeVerifiedDestinationNumbersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeVerifiedDestinationNumbersResult:
    boto3_raw_data: "type_defs.DescribeVerifiedDestinationNumbersResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def VerifiedDestinationNumbers(self):  # pragma: no cover
        return VerifiedDestinationNumberInformation.make_many(
            self.boto3_raw_data["VerifiedDestinationNumbers"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeVerifiedDestinationNumbersResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeVerifiedDestinationNumbersResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetProtectConfigurationCountryRuleSetResult:
    boto3_raw_data: "type_defs.GetProtectConfigurationCountryRuleSetResultTypeDef" = (
        dataclasses.field()
    )

    ProtectConfigurationArn = field("ProtectConfigurationArn")
    ProtectConfigurationId = field("ProtectConfigurationId")
    NumberCapability = field("NumberCapability")
    CountryRuleSet = field("CountryRuleSet")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetProtectConfigurationCountryRuleSetResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetProtectConfigurationCountryRuleSetResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateProtectConfigurationCountryRuleSetRequest:
    boto3_raw_data: (
        "type_defs.UpdateProtectConfigurationCountryRuleSetRequestTypeDef"
    ) = dataclasses.field()

    ProtectConfigurationId = field("ProtectConfigurationId")
    NumberCapability = field("NumberCapability")
    CountryRuleSetUpdates = field("CountryRuleSetUpdates")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateProtectConfigurationCountryRuleSetRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.UpdateProtectConfigurationCountryRuleSetRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateProtectConfigurationCountryRuleSetResult:
    boto3_raw_data: (
        "type_defs.UpdateProtectConfigurationCountryRuleSetResultTypeDef"
    ) = dataclasses.field()

    ProtectConfigurationArn = field("ProtectConfigurationArn")
    ProtectConfigurationId = field("ProtectConfigurationId")
    NumberCapability = field("NumberCapability")
    CountryRuleSet = field("CountryRuleSet")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateProtectConfigurationCountryRuleSetResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.UpdateProtectConfigurationCountryRuleSetResultTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPoolOriginationIdentitiesRequestPaginate:
    boto3_raw_data: "type_defs.ListPoolOriginationIdentitiesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    PoolId = field("PoolId")

    @cached_property
    def Filters(self):  # pragma: no cover
        return PoolOriginationIdentitiesFilter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPoolOriginationIdentitiesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPoolOriginationIdentitiesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPoolOriginationIdentitiesRequest:
    boto3_raw_data: "type_defs.ListPoolOriginationIdentitiesRequestTypeDef" = (
        dataclasses.field()
    )

    PoolId = field("PoolId")

    @cached_property
    def Filters(self):  # pragma: no cover
        return PoolOriginationIdentitiesFilter.make_many(self.boto3_raw_data["Filters"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPoolOriginationIdentitiesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPoolOriginationIdentitiesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPoolOriginationIdentitiesResult:
    boto3_raw_data: "type_defs.ListPoolOriginationIdentitiesResultTypeDef" = (
        dataclasses.field()
    )

    PoolArn = field("PoolArn")
    PoolId = field("PoolId")

    @cached_property
    def OriginationIdentities(self):  # pragma: no cover
        return OriginationIdentityMetadata.make_many(
            self.boto3_raw_data["OriginationIdentities"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPoolOriginationIdentitiesResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPoolOriginationIdentitiesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProtectConfigurationRuleSetNumberOverridesRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListProtectConfigurationRuleSetNumberOverridesRequestPaginateTypeDef"
    ) = dataclasses.field()

    ProtectConfigurationId = field("ProtectConfigurationId")

    @cached_property
    def Filters(self):  # pragma: no cover
        return ProtectConfigurationRuleSetNumberOverrideFilterItem.make_many(
            self.boto3_raw_data["Filters"]
        )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListProtectConfigurationRuleSetNumberOverridesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.ListProtectConfigurationRuleSetNumberOverridesRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProtectConfigurationRuleSetNumberOverridesRequest:
    boto3_raw_data: (
        "type_defs.ListProtectConfigurationRuleSetNumberOverridesRequestTypeDef"
    ) = dataclasses.field()

    ProtectConfigurationId = field("ProtectConfigurationId")

    @cached_property
    def Filters(self):  # pragma: no cover
        return ProtectConfigurationRuleSetNumberOverrideFilterItem.make_many(
            self.boto3_raw_data["Filters"]
        )

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListProtectConfigurationRuleSetNumberOverridesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.ListProtectConfigurationRuleSetNumberOverridesRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProtectConfigurationRuleSetNumberOverridesResult:
    boto3_raw_data: (
        "type_defs.ListProtectConfigurationRuleSetNumberOverridesResultTypeDef"
    ) = dataclasses.field()

    ProtectConfigurationArn = field("ProtectConfigurationArn")
    ProtectConfigurationId = field("ProtectConfigurationId")

    @cached_property
    def RuleSetNumberOverrides(self):  # pragma: no cover
        return ProtectConfigurationRuleSetNumberOverride.make_many(
            self.boto3_raw_data["RuleSetNumberOverrides"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListProtectConfigurationRuleSetNumberOverridesResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.ListProtectConfigurationRuleSetNumberOverridesResultTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRegistrationAssociationsRequestPaginate:
    boto3_raw_data: "type_defs.ListRegistrationAssociationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    RegistrationId = field("RegistrationId")

    @cached_property
    def Filters(self):  # pragma: no cover
        return RegistrationAssociationFilter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRegistrationAssociationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRegistrationAssociationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRegistrationAssociationsRequest:
    boto3_raw_data: "type_defs.ListRegistrationAssociationsRequestTypeDef" = (
        dataclasses.field()
    )

    RegistrationId = field("RegistrationId")

    @cached_property
    def Filters(self):  # pragma: no cover
        return RegistrationAssociationFilter.make_many(self.boto3_raw_data["Filters"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRegistrationAssociationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRegistrationAssociationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRegistrationAssociationsResult:
    boto3_raw_data: "type_defs.ListRegistrationAssociationsResultTypeDef" = (
        dataclasses.field()
    )

    RegistrationArn = field("RegistrationArn")
    RegistrationId = field("RegistrationId")
    RegistrationType = field("RegistrationType")

    @cached_property
    def RegistrationAssociations(self):  # pragma: no cover
        return RegistrationAssociationMetadata.make_many(
            self.boto3_raw_data["RegistrationAssociations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRegistrationAssociationsResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRegistrationAssociationsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutProtectConfigurationRuleSetNumberOverrideRequest:
    boto3_raw_data: (
        "type_defs.PutProtectConfigurationRuleSetNumberOverrideRequestTypeDef"
    ) = dataclasses.field()

    ProtectConfigurationId = field("ProtectConfigurationId")
    DestinationPhoneNumber = field("DestinationPhoneNumber")
    Action = field("Action")
    ClientToken = field("ClientToken")
    ExpirationTimestamp = field("ExpirationTimestamp")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutProtectConfigurationRuleSetNumberOverrideRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.PutProtectConfigurationRuleSetNumberOverrideRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegistrationVersionInformation:
    boto3_raw_data: "type_defs.RegistrationVersionInformationTypeDef" = (
        dataclasses.field()
    )

    VersionNumber = field("VersionNumber")
    RegistrationVersionStatus = field("RegistrationVersionStatus")

    @cached_property
    def RegistrationVersionStatusHistory(self):  # pragma: no cover
        return RegistrationVersionStatusHistory.make_one(
            self.boto3_raw_data["RegistrationVersionStatusHistory"]
        )

    @cached_property
    def DeniedReasons(self):  # pragma: no cover
        return RegistrationDeniedReasonInformation.make_many(
            self.boto3_raw_data["DeniedReasons"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RegistrationVersionInformationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegistrationVersionInformationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegistrationFieldDisplayHints:
    boto3_raw_data: "type_defs.RegistrationFieldDisplayHintsTypeDef" = (
        dataclasses.field()
    )

    Title = field("Title")
    ShortDescription = field("ShortDescription")
    LongDescription = field("LongDescription")
    DocumentationTitle = field("DocumentationTitle")
    DocumentationLink = field("DocumentationLink")

    @cached_property
    def SelectOptionDescriptions(self):  # pragma: no cover
        return SelectOptionDescription.make_many(
            self.boto3_raw_data["SelectOptionDescriptions"]
        )

    TextValidationDescription = field("TextValidationDescription")
    ExampleTextValue = field("ExampleTextValue")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RegistrationFieldDisplayHintsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegistrationFieldDisplayHintsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegistrationSectionDefinition:
    boto3_raw_data: "type_defs.RegistrationSectionDefinitionTypeDef" = (
        dataclasses.field()
    )

    SectionPath = field("SectionPath")

    @cached_property
    def DisplayHints(self):  # pragma: no cover
        return RegistrationSectionDisplayHints.make_one(
            self.boto3_raw_data["DisplayHints"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RegistrationSectionDefinitionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegistrationSectionDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegistrationTypeDefinition:
    boto3_raw_data: "type_defs.RegistrationTypeDefinitionTypeDef" = dataclasses.field()

    RegistrationType = field("RegistrationType")

    @cached_property
    def DisplayHints(self):  # pragma: no cover
        return RegistrationTypeDisplayHints.make_one(
            self.boto3_raw_data["DisplayHints"]
        )

    @cached_property
    def SupportedAssociations(self):  # pragma: no cover
        return SupportedAssociation.make_many(
            self.boto3_raw_data["SupportedAssociations"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegistrationTypeDefinitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegistrationTypeDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigurationSetInformation:
    boto3_raw_data: "type_defs.ConfigurationSetInformationTypeDef" = dataclasses.field()

    ConfigurationSetArn = field("ConfigurationSetArn")
    ConfigurationSetName = field("ConfigurationSetName")

    @cached_property
    def EventDestinations(self):  # pragma: no cover
        return EventDestination.make_many(self.boto3_raw_data["EventDestinations"])

    CreatedTimestamp = field("CreatedTimestamp")
    DefaultMessageType = field("DefaultMessageType")
    DefaultSenderId = field("DefaultSenderId")
    DefaultMessageFeedbackEnabled = field("DefaultMessageFeedbackEnabled")
    ProtectConfigurationId = field("ProtectConfigurationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfigurationSetInformationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigurationSetInformationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEventDestinationResult:
    boto3_raw_data: "type_defs.CreateEventDestinationResultTypeDef" = (
        dataclasses.field()
    )

    ConfigurationSetArn = field("ConfigurationSetArn")
    ConfigurationSetName = field("ConfigurationSetName")

    @cached_property
    def EventDestination(self):  # pragma: no cover
        return EventDestination.make_one(self.boto3_raw_data["EventDestination"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEventDestinationResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEventDestinationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteConfigurationSetResult:
    boto3_raw_data: "type_defs.DeleteConfigurationSetResultTypeDef" = (
        dataclasses.field()
    )

    ConfigurationSetArn = field("ConfigurationSetArn")
    ConfigurationSetName = field("ConfigurationSetName")

    @cached_property
    def EventDestinations(self):  # pragma: no cover
        return EventDestination.make_many(self.boto3_raw_data["EventDestinations"])

    DefaultMessageType = field("DefaultMessageType")
    DefaultSenderId = field("DefaultSenderId")
    DefaultMessageFeedbackEnabled = field("DefaultMessageFeedbackEnabled")
    CreatedTimestamp = field("CreatedTimestamp")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteConfigurationSetResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteConfigurationSetResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEventDestinationResult:
    boto3_raw_data: "type_defs.DeleteEventDestinationResultTypeDef" = (
        dataclasses.field()
    )

    ConfigurationSetArn = field("ConfigurationSetArn")
    ConfigurationSetName = field("ConfigurationSetName")

    @cached_property
    def EventDestination(self):  # pragma: no cover
        return EventDestination.make_one(self.boto3_raw_data["EventDestination"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteEventDestinationResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEventDestinationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEventDestinationResult:
    boto3_raw_data: "type_defs.UpdateEventDestinationResultTypeDef" = (
        dataclasses.field()
    )

    ConfigurationSetArn = field("ConfigurationSetArn")
    ConfigurationSetName = field("ConfigurationSetName")

    @cached_property
    def EventDestination(self):  # pragma: no cover
        return EventDestination.make_one(self.boto3_raw_data["EventDestination"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateEventDestinationResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEventDestinationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRegistrationVersionsResult:
    boto3_raw_data: "type_defs.DescribeRegistrationVersionsResultTypeDef" = (
        dataclasses.field()
    )

    RegistrationArn = field("RegistrationArn")
    RegistrationId = field("RegistrationId")

    @cached_property
    def RegistrationVersions(self):  # pragma: no cover
        return RegistrationVersionInformation.make_many(
            self.boto3_raw_data["RegistrationVersions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRegistrationVersionsResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRegistrationVersionsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegistrationFieldDefinition:
    boto3_raw_data: "type_defs.RegistrationFieldDefinitionTypeDef" = dataclasses.field()

    SectionPath = field("SectionPath")
    FieldPath = field("FieldPath")
    FieldType = field("FieldType")
    FieldRequirement = field("FieldRequirement")

    @cached_property
    def DisplayHints(self):  # pragma: no cover
        return RegistrationFieldDisplayHints.make_one(
            self.boto3_raw_data["DisplayHints"]
        )

    @cached_property
    def SelectValidation(self):  # pragma: no cover
        return SelectValidation.make_one(self.boto3_raw_data["SelectValidation"])

    @cached_property
    def TextValidation(self):  # pragma: no cover
        return TextValidation.make_one(self.boto3_raw_data["TextValidation"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegistrationFieldDefinitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegistrationFieldDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRegistrationSectionDefinitionsResult:
    boto3_raw_data: "type_defs.DescribeRegistrationSectionDefinitionsResultTypeDef" = (
        dataclasses.field()
    )

    RegistrationType = field("RegistrationType")

    @cached_property
    def RegistrationSectionDefinitions(self):  # pragma: no cover
        return RegistrationSectionDefinition.make_many(
            self.boto3_raw_data["RegistrationSectionDefinitions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRegistrationSectionDefinitionsResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRegistrationSectionDefinitionsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRegistrationTypeDefinitionsResult:
    boto3_raw_data: "type_defs.DescribeRegistrationTypeDefinitionsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RegistrationTypeDefinitions(self):  # pragma: no cover
        return RegistrationTypeDefinition.make_many(
            self.boto3_raw_data["RegistrationTypeDefinitions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRegistrationTypeDefinitionsResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRegistrationTypeDefinitionsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConfigurationSetsResult:
    boto3_raw_data: "type_defs.DescribeConfigurationSetsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ConfigurationSets(self):  # pragma: no cover
        return ConfigurationSetInformation.make_many(
            self.boto3_raw_data["ConfigurationSets"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeConfigurationSetsResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConfigurationSetsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRegistrationFieldDefinitionsResult:
    boto3_raw_data: "type_defs.DescribeRegistrationFieldDefinitionsResultTypeDef" = (
        dataclasses.field()
    )

    RegistrationType = field("RegistrationType")

    @cached_property
    def RegistrationFieldDefinitions(self):  # pragma: no cover
        return RegistrationFieldDefinition.make_many(
            self.boto3_raw_data["RegistrationFieldDefinitions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRegistrationFieldDefinitionsResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRegistrationFieldDefinitionsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]

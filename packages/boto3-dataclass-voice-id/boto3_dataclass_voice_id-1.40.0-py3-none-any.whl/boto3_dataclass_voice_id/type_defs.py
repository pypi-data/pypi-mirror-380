# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_voice_id import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AssociateFraudsterRequest:
    boto3_raw_data: "type_defs.AssociateFraudsterRequestTypeDef" = dataclasses.field()

    DomainId = field("DomainId")
    FraudsterId = field("FraudsterId")
    WatchlistId = field("WatchlistId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateFraudsterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateFraudsterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Fraudster:
    boto3_raw_data: "type_defs.FraudsterTypeDef" = dataclasses.field()

    CreatedAt = field("CreatedAt")
    DomainId = field("DomainId")
    GeneratedFraudsterId = field("GeneratedFraudsterId")
    WatchlistIds = field("WatchlistIds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FraudsterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FraudsterTypeDef"]]
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
class AuthenticationConfiguration:
    boto3_raw_data: "type_defs.AuthenticationConfigurationTypeDef" = dataclasses.field()

    AcceptanceThreshold = field("AcceptanceThreshold")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AuthenticationConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthenticationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServerSideEncryptionConfiguration:
    boto3_raw_data: "type_defs.ServerSideEncryptionConfigurationTypeDef" = (
        dataclasses.field()
    )

    KmsKeyId = field("KmsKeyId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ServerSideEncryptionConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServerSideEncryptionConfigurationTypeDef"]
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
class CreateWatchlistRequest:
    boto3_raw_data: "type_defs.CreateWatchlistRequestTypeDef" = dataclasses.field()

    DomainId = field("DomainId")
    Name = field("Name")
    ClientToken = field("ClientToken")
    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWatchlistRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWatchlistRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Watchlist:
    boto3_raw_data: "type_defs.WatchlistTypeDef" = dataclasses.field()

    CreatedAt = field("CreatedAt")
    DefaultWatchlist = field("DefaultWatchlist")
    Description = field("Description")
    DomainId = field("DomainId")
    Name = field("Name")
    UpdatedAt = field("UpdatedAt")
    WatchlistId = field("WatchlistId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WatchlistTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WatchlistTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDomainRequest:
    boto3_raw_data: "type_defs.DeleteDomainRequestTypeDef" = dataclasses.field()

    DomainId = field("DomainId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDomainRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDomainRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFraudsterRequest:
    boto3_raw_data: "type_defs.DeleteFraudsterRequestTypeDef" = dataclasses.field()

    DomainId = field("DomainId")
    FraudsterId = field("FraudsterId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteFraudsterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFraudsterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSpeakerRequest:
    boto3_raw_data: "type_defs.DeleteSpeakerRequestTypeDef" = dataclasses.field()

    DomainId = field("DomainId")
    SpeakerId = field("SpeakerId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSpeakerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSpeakerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteWatchlistRequest:
    boto3_raw_data: "type_defs.DeleteWatchlistRequestTypeDef" = dataclasses.field()

    DomainId = field("DomainId")
    WatchlistId = field("WatchlistId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteWatchlistRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteWatchlistRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDomainRequest:
    boto3_raw_data: "type_defs.DescribeDomainRequestTypeDef" = dataclasses.field()

    DomainId = field("DomainId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDomainRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDomainRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFraudsterRegistrationJobRequest:
    boto3_raw_data: "type_defs.DescribeFraudsterRegistrationJobRequestTypeDef" = (
        dataclasses.field()
    )

    DomainId = field("DomainId")
    JobId = field("JobId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeFraudsterRegistrationJobRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFraudsterRegistrationJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFraudsterRequest:
    boto3_raw_data: "type_defs.DescribeFraudsterRequestTypeDef" = dataclasses.field()

    DomainId = field("DomainId")
    FraudsterId = field("FraudsterId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeFraudsterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFraudsterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSpeakerEnrollmentJobRequest:
    boto3_raw_data: "type_defs.DescribeSpeakerEnrollmentJobRequestTypeDef" = (
        dataclasses.field()
    )

    DomainId = field("DomainId")
    JobId = field("JobId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeSpeakerEnrollmentJobRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSpeakerEnrollmentJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSpeakerRequest:
    boto3_raw_data: "type_defs.DescribeSpeakerRequestTypeDef" = dataclasses.field()

    DomainId = field("DomainId")
    SpeakerId = field("SpeakerId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeSpeakerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSpeakerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Speaker:
    boto3_raw_data: "type_defs.SpeakerTypeDef" = dataclasses.field()

    CreatedAt = field("CreatedAt")
    CustomerSpeakerId = field("CustomerSpeakerId")
    DomainId = field("DomainId")
    GeneratedSpeakerId = field("GeneratedSpeakerId")
    LastAccessedAt = field("LastAccessedAt")
    Status = field("Status")
    UpdatedAt = field("UpdatedAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SpeakerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SpeakerTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWatchlistRequest:
    boto3_raw_data: "type_defs.DescribeWatchlistRequestTypeDef" = dataclasses.field()

    DomainId = field("DomainId")
    WatchlistId = field("WatchlistId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeWatchlistRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWatchlistRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateFraudsterRequest:
    boto3_raw_data: "type_defs.DisassociateFraudsterRequestTypeDef" = (
        dataclasses.field()
    )

    DomainId = field("DomainId")
    FraudsterId = field("FraudsterId")
    WatchlistId = field("WatchlistId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisassociateFraudsterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateFraudsterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServerSideEncryptionUpdateDetails:
    boto3_raw_data: "type_defs.ServerSideEncryptionUpdateDetailsTypeDef" = (
        dataclasses.field()
    )

    Message = field("Message")
    OldKmsKeyId = field("OldKmsKeyId")
    UpdateStatus = field("UpdateStatus")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ServerSideEncryptionUpdateDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServerSideEncryptionUpdateDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WatchlistDetails:
    boto3_raw_data: "type_defs.WatchlistDetailsTypeDef" = dataclasses.field()

    DefaultWatchlistId = field("DefaultWatchlistId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WatchlistDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WatchlistDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnrollmentJobFraudDetectionConfigOutput:
    boto3_raw_data: "type_defs.EnrollmentJobFraudDetectionConfigOutputTypeDef" = (
        dataclasses.field()
    )

    FraudDetectionAction = field("FraudDetectionAction")
    RiskThreshold = field("RiskThreshold")
    WatchlistIds = field("WatchlistIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EnrollmentJobFraudDetectionConfigOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnrollmentJobFraudDetectionConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnrollmentJobFraudDetectionConfig:
    boto3_raw_data: "type_defs.EnrollmentJobFraudDetectionConfigTypeDef" = (
        dataclasses.field()
    )

    FraudDetectionAction = field("FraudDetectionAction")
    RiskThreshold = field("RiskThreshold")
    WatchlistIds = field("WatchlistIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EnrollmentJobFraudDetectionConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnrollmentJobFraudDetectionConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluateSessionRequest:
    boto3_raw_data: "type_defs.EvaluateSessionRequestTypeDef" = dataclasses.field()

    DomainId = field("DomainId")
    SessionNameOrId = field("SessionNameOrId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EvaluateSessionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluateSessionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailureDetails:
    boto3_raw_data: "type_defs.FailureDetailsTypeDef" = dataclasses.field()

    Message = field("Message")
    StatusCode = field("StatusCode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FailureDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FailureDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FraudDetectionConfiguration:
    boto3_raw_data: "type_defs.FraudDetectionConfigurationTypeDef" = dataclasses.field()

    RiskThreshold = field("RiskThreshold")
    WatchlistId = field("WatchlistId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FraudDetectionConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FraudDetectionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KnownFraudsterRisk:
    boto3_raw_data: "type_defs.KnownFraudsterRiskTypeDef" = dataclasses.field()

    RiskScore = field("RiskScore")
    GeneratedFraudsterId = field("GeneratedFraudsterId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KnownFraudsterRiskTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KnownFraudsterRiskTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VoiceSpoofingRisk:
    boto3_raw_data: "type_defs.VoiceSpoofingRiskTypeDef" = dataclasses.field()

    RiskScore = field("RiskScore")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VoiceSpoofingRiskTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VoiceSpoofingRiskTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobProgress:
    boto3_raw_data: "type_defs.JobProgressTypeDef" = dataclasses.field()

    PercentComplete = field("PercentComplete")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobProgressTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobProgressTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputDataConfig:
    boto3_raw_data: "type_defs.InputDataConfigTypeDef" = dataclasses.field()

    S3Uri = field("S3Uri")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InputDataConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InputDataConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutputDataConfig:
    boto3_raw_data: "type_defs.OutputDataConfigTypeDef" = dataclasses.field()

    S3Uri = field("S3Uri")
    KmsKeyId = field("KmsKeyId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OutputDataConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OutputDataConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegistrationConfigOutput:
    boto3_raw_data: "type_defs.RegistrationConfigOutputTypeDef" = dataclasses.field()

    DuplicateRegistrationAction = field("DuplicateRegistrationAction")
    FraudsterSimilarityThreshold = field("FraudsterSimilarityThreshold")
    WatchlistIds = field("WatchlistIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegistrationConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegistrationConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FraudsterSummary:
    boto3_raw_data: "type_defs.FraudsterSummaryTypeDef" = dataclasses.field()

    CreatedAt = field("CreatedAt")
    DomainId = field("DomainId")
    GeneratedFraudsterId = field("GeneratedFraudsterId")
    WatchlistIds = field("WatchlistIds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FraudsterSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FraudsterSummaryTypeDef"]
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
class ListDomainsRequest:
    boto3_raw_data: "type_defs.ListDomainsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDomainsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDomainsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFraudsterRegistrationJobsRequest:
    boto3_raw_data: "type_defs.ListFraudsterRegistrationJobsRequestTypeDef" = (
        dataclasses.field()
    )

    DomainId = field("DomainId")
    JobStatus = field("JobStatus")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListFraudsterRegistrationJobsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFraudsterRegistrationJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFraudstersRequest:
    boto3_raw_data: "type_defs.ListFraudstersRequestTypeDef" = dataclasses.field()

    DomainId = field("DomainId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    WatchlistId = field("WatchlistId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFraudstersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFraudstersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSpeakerEnrollmentJobsRequest:
    boto3_raw_data: "type_defs.ListSpeakerEnrollmentJobsRequestTypeDef" = (
        dataclasses.field()
    )

    DomainId = field("DomainId")
    JobStatus = field("JobStatus")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSpeakerEnrollmentJobsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSpeakerEnrollmentJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSpeakersRequest:
    boto3_raw_data: "type_defs.ListSpeakersRequestTypeDef" = dataclasses.field()

    DomainId = field("DomainId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSpeakersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSpeakersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SpeakerSummary:
    boto3_raw_data: "type_defs.SpeakerSummaryTypeDef" = dataclasses.field()

    CreatedAt = field("CreatedAt")
    CustomerSpeakerId = field("CustomerSpeakerId")
    DomainId = field("DomainId")
    GeneratedSpeakerId = field("GeneratedSpeakerId")
    LastAccessedAt = field("LastAccessedAt")
    Status = field("Status")
    UpdatedAt = field("UpdatedAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SpeakerSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SpeakerSummaryTypeDef"]],
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
class ListWatchlistsRequest:
    boto3_raw_data: "type_defs.ListWatchlistsRequestTypeDef" = dataclasses.field()

    DomainId = field("DomainId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWatchlistsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWatchlistsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WatchlistSummary:
    boto3_raw_data: "type_defs.WatchlistSummaryTypeDef" = dataclasses.field()

    CreatedAt = field("CreatedAt")
    DefaultWatchlist = field("DefaultWatchlist")
    Description = field("Description")
    DomainId = field("DomainId")
    Name = field("Name")
    UpdatedAt = field("UpdatedAt")
    WatchlistId = field("WatchlistId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WatchlistSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WatchlistSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OptOutSpeakerRequest:
    boto3_raw_data: "type_defs.OptOutSpeakerRequestTypeDef" = dataclasses.field()

    DomainId = field("DomainId")
    SpeakerId = field("SpeakerId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OptOutSpeakerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OptOutSpeakerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegistrationConfig:
    boto3_raw_data: "type_defs.RegistrationConfigTypeDef" = dataclasses.field()

    DuplicateRegistrationAction = field("DuplicateRegistrationAction")
    FraudsterSimilarityThreshold = field("FraudsterSimilarityThreshold")
    WatchlistIds = field("WatchlistIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegistrationConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegistrationConfigTypeDef"]
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
class UpdateWatchlistRequest:
    boto3_raw_data: "type_defs.UpdateWatchlistRequestTypeDef" = dataclasses.field()

    DomainId = field("DomainId")
    WatchlistId = field("WatchlistId")
    Description = field("Description")
    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateWatchlistRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWatchlistRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateFraudsterResponse:
    boto3_raw_data: "type_defs.AssociateFraudsterResponseTypeDef" = dataclasses.field()

    @cached_property
    def Fraudster(self):  # pragma: no cover
        return Fraudster.make_one(self.boto3_raw_data["Fraudster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateFraudsterResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateFraudsterResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFraudsterResponse:
    boto3_raw_data: "type_defs.DescribeFraudsterResponseTypeDef" = dataclasses.field()

    @cached_property
    def Fraudster(self):  # pragma: no cover
        return Fraudster.make_one(self.boto3_raw_data["Fraudster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeFraudsterResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFraudsterResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateFraudsterResponse:
    boto3_raw_data: "type_defs.DisassociateFraudsterResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Fraudster(self):  # pragma: no cover
        return Fraudster.make_one(self.boto3_raw_data["Fraudster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DisassociateFraudsterResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateFraudsterResponseTypeDef"]
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
class AuthenticationResult:
    boto3_raw_data: "type_defs.AuthenticationResultTypeDef" = dataclasses.field()

    AudioAggregationEndedAt = field("AudioAggregationEndedAt")
    AudioAggregationStartedAt = field("AudioAggregationStartedAt")
    AuthenticationResultId = field("AuthenticationResultId")

    @cached_property
    def Configuration(self):  # pragma: no cover
        return AuthenticationConfiguration.make_one(
            self.boto3_raw_data["Configuration"]
        )

    CustomerSpeakerId = field("CustomerSpeakerId")
    Decision = field("Decision")
    GeneratedSpeakerId = field("GeneratedSpeakerId")
    Score = field("Score")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AuthenticationResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthenticationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDomainRequest:
    boto3_raw_data: "type_defs.UpdateDomainRequestTypeDef" = dataclasses.field()

    DomainId = field("DomainId")
    Name = field("Name")

    @cached_property
    def ServerSideEncryptionConfiguration(self):  # pragma: no cover
        return ServerSideEncryptionConfiguration.make_one(
            self.boto3_raw_data["ServerSideEncryptionConfiguration"]
        )

    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDomainRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDomainRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDomainRequest:
    boto3_raw_data: "type_defs.CreateDomainRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def ServerSideEncryptionConfiguration(self):  # pragma: no cover
        return ServerSideEncryptionConfiguration.make_one(
            self.boto3_raw_data["ServerSideEncryptionConfiguration"]
        )

    ClientToken = field("ClientToken")
    Description = field("Description")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDomainRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDomainRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceResponse:
    boto3_raw_data: "type_defs.ListTagsForResourceResponseTypeDef" = dataclasses.field()

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceResponseTypeDef"]
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
class CreateWatchlistResponse:
    boto3_raw_data: "type_defs.CreateWatchlistResponseTypeDef" = dataclasses.field()

    @cached_property
    def Watchlist(self):  # pragma: no cover
        return Watchlist.make_one(self.boto3_raw_data["Watchlist"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWatchlistResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWatchlistResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWatchlistResponse:
    boto3_raw_data: "type_defs.DescribeWatchlistResponseTypeDef" = dataclasses.field()

    @cached_property
    def Watchlist(self):  # pragma: no cover
        return Watchlist.make_one(self.boto3_raw_data["Watchlist"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeWatchlistResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWatchlistResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateWatchlistResponse:
    boto3_raw_data: "type_defs.UpdateWatchlistResponseTypeDef" = dataclasses.field()

    @cached_property
    def Watchlist(self):  # pragma: no cover
        return Watchlist.make_one(self.boto3_raw_data["Watchlist"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateWatchlistResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWatchlistResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSpeakerResponse:
    boto3_raw_data: "type_defs.DescribeSpeakerResponseTypeDef" = dataclasses.field()

    @cached_property
    def Speaker(self):  # pragma: no cover
        return Speaker.make_one(self.boto3_raw_data["Speaker"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeSpeakerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSpeakerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OptOutSpeakerResponse:
    boto3_raw_data: "type_defs.OptOutSpeakerResponseTypeDef" = dataclasses.field()

    @cached_property
    def Speaker(self):  # pragma: no cover
        return Speaker.make_one(self.boto3_raw_data["Speaker"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OptOutSpeakerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OptOutSpeakerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainSummary:
    boto3_raw_data: "type_defs.DomainSummaryTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CreatedAt = field("CreatedAt")
    Description = field("Description")
    DomainId = field("DomainId")
    DomainStatus = field("DomainStatus")
    Name = field("Name")

    @cached_property
    def ServerSideEncryptionConfiguration(self):  # pragma: no cover
        return ServerSideEncryptionConfiguration.make_one(
            self.boto3_raw_data["ServerSideEncryptionConfiguration"]
        )

    @cached_property
    def ServerSideEncryptionUpdateDetails(self):  # pragma: no cover
        return ServerSideEncryptionUpdateDetails.make_one(
            self.boto3_raw_data["ServerSideEncryptionUpdateDetails"]
        )

    UpdatedAt = field("UpdatedAt")

    @cached_property
    def WatchlistDetails(self):  # pragma: no cover
        return WatchlistDetails.make_one(self.boto3_raw_data["WatchlistDetails"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DomainSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DomainSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Domain:
    boto3_raw_data: "type_defs.DomainTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CreatedAt = field("CreatedAt")
    Description = field("Description")
    DomainId = field("DomainId")
    DomainStatus = field("DomainStatus")
    Name = field("Name")

    @cached_property
    def ServerSideEncryptionConfiguration(self):  # pragma: no cover
        return ServerSideEncryptionConfiguration.make_one(
            self.boto3_raw_data["ServerSideEncryptionConfiguration"]
        )

    @cached_property
    def ServerSideEncryptionUpdateDetails(self):  # pragma: no cover
        return ServerSideEncryptionUpdateDetails.make_one(
            self.boto3_raw_data["ServerSideEncryptionUpdateDetails"]
        )

    UpdatedAt = field("UpdatedAt")

    @cached_property
    def WatchlistDetails(self):  # pragma: no cover
        return WatchlistDetails.make_one(self.boto3_raw_data["WatchlistDetails"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DomainTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DomainTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnrollmentConfigOutput:
    boto3_raw_data: "type_defs.EnrollmentConfigOutputTypeDef" = dataclasses.field()

    ExistingEnrollmentAction = field("ExistingEnrollmentAction")

    @cached_property
    def FraudDetectionConfig(self):  # pragma: no cover
        return EnrollmentJobFraudDetectionConfigOutput.make_one(
            self.boto3_raw_data["FraudDetectionConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnrollmentConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnrollmentConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnrollmentConfig:
    boto3_raw_data: "type_defs.EnrollmentConfigTypeDef" = dataclasses.field()

    ExistingEnrollmentAction = field("ExistingEnrollmentAction")

    @cached_property
    def FraudDetectionConfig(self):  # pragma: no cover
        return EnrollmentJobFraudDetectionConfig.make_one(
            self.boto3_raw_data["FraudDetectionConfig"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EnrollmentConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnrollmentConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FraudRiskDetails:
    boto3_raw_data: "type_defs.FraudRiskDetailsTypeDef" = dataclasses.field()

    @cached_property
    def KnownFraudsterRisk(self):  # pragma: no cover
        return KnownFraudsterRisk.make_one(self.boto3_raw_data["KnownFraudsterRisk"])

    @cached_property
    def VoiceSpoofingRisk(self):  # pragma: no cover
        return VoiceSpoofingRisk.make_one(self.boto3_raw_data["VoiceSpoofingRisk"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FraudRiskDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FraudRiskDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FraudsterRegistrationJobSummary:
    boto3_raw_data: "type_defs.FraudsterRegistrationJobSummaryTypeDef" = (
        dataclasses.field()
    )

    CreatedAt = field("CreatedAt")
    DomainId = field("DomainId")
    EndedAt = field("EndedAt")

    @cached_property
    def FailureDetails(self):  # pragma: no cover
        return FailureDetails.make_one(self.boto3_raw_data["FailureDetails"])

    JobId = field("JobId")
    JobName = field("JobName")

    @cached_property
    def JobProgress(self):  # pragma: no cover
        return JobProgress.make_one(self.boto3_raw_data["JobProgress"])

    JobStatus = field("JobStatus")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.FraudsterRegistrationJobSummaryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FraudsterRegistrationJobSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SpeakerEnrollmentJobSummary:
    boto3_raw_data: "type_defs.SpeakerEnrollmentJobSummaryTypeDef" = dataclasses.field()

    CreatedAt = field("CreatedAt")
    DomainId = field("DomainId")
    EndedAt = field("EndedAt")

    @cached_property
    def FailureDetails(self):  # pragma: no cover
        return FailureDetails.make_one(self.boto3_raw_data["FailureDetails"])

    JobId = field("JobId")
    JobName = field("JobName")

    @cached_property
    def JobProgress(self):  # pragma: no cover
        return JobProgress.make_one(self.boto3_raw_data["JobProgress"])

    JobStatus = field("JobStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SpeakerEnrollmentJobSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SpeakerEnrollmentJobSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FraudsterRegistrationJob:
    boto3_raw_data: "type_defs.FraudsterRegistrationJobTypeDef" = dataclasses.field()

    CreatedAt = field("CreatedAt")
    DataAccessRoleArn = field("DataAccessRoleArn")
    DomainId = field("DomainId")
    EndedAt = field("EndedAt")

    @cached_property
    def FailureDetails(self):  # pragma: no cover
        return FailureDetails.make_one(self.boto3_raw_data["FailureDetails"])

    @cached_property
    def InputDataConfig(self):  # pragma: no cover
        return InputDataConfig.make_one(self.boto3_raw_data["InputDataConfig"])

    JobId = field("JobId")
    JobName = field("JobName")

    @cached_property
    def JobProgress(self):  # pragma: no cover
        return JobProgress.make_one(self.boto3_raw_data["JobProgress"])

    JobStatus = field("JobStatus")

    @cached_property
    def OutputDataConfig(self):  # pragma: no cover
        return OutputDataConfig.make_one(self.boto3_raw_data["OutputDataConfig"])

    @cached_property
    def RegistrationConfig(self):  # pragma: no cover
        return RegistrationConfigOutput.make_one(
            self.boto3_raw_data["RegistrationConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FraudsterRegistrationJobTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FraudsterRegistrationJobTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFraudstersResponse:
    boto3_raw_data: "type_defs.ListFraudstersResponseTypeDef" = dataclasses.field()

    @cached_property
    def FraudsterSummaries(self):  # pragma: no cover
        return FraudsterSummary.make_many(self.boto3_raw_data["FraudsterSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFraudstersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFraudstersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDomainsRequestPaginate:
    boto3_raw_data: "type_defs.ListDomainsRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDomainsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDomainsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFraudsterRegistrationJobsRequestPaginate:
    boto3_raw_data: "type_defs.ListFraudsterRegistrationJobsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DomainId = field("DomainId")
    JobStatus = field("JobStatus")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListFraudsterRegistrationJobsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFraudsterRegistrationJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFraudstersRequestPaginate:
    boto3_raw_data: "type_defs.ListFraudstersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DomainId = field("DomainId")
    WatchlistId = field("WatchlistId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListFraudstersRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFraudstersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSpeakerEnrollmentJobsRequestPaginate:
    boto3_raw_data: "type_defs.ListSpeakerEnrollmentJobsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DomainId = field("DomainId")
    JobStatus = field("JobStatus")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSpeakerEnrollmentJobsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSpeakerEnrollmentJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSpeakersRequestPaginate:
    boto3_raw_data: "type_defs.ListSpeakersRequestPaginateTypeDef" = dataclasses.field()

    DomainId = field("DomainId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSpeakersRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSpeakersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWatchlistsRequestPaginate:
    boto3_raw_data: "type_defs.ListWatchlistsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DomainId = field("DomainId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListWatchlistsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWatchlistsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSpeakersResponse:
    boto3_raw_data: "type_defs.ListSpeakersResponseTypeDef" = dataclasses.field()

    @cached_property
    def SpeakerSummaries(self):  # pragma: no cover
        return SpeakerSummary.make_many(self.boto3_raw_data["SpeakerSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSpeakersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSpeakersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWatchlistsResponse:
    boto3_raw_data: "type_defs.ListWatchlistsResponseTypeDef" = dataclasses.field()

    @cached_property
    def WatchlistSummaries(self):  # pragma: no cover
        return WatchlistSummary.make_many(self.boto3_raw_data["WatchlistSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWatchlistsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWatchlistsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDomainsResponse:
    boto3_raw_data: "type_defs.ListDomainsResponseTypeDef" = dataclasses.field()

    @cached_property
    def DomainSummaries(self):  # pragma: no cover
        return DomainSummary.make_many(self.boto3_raw_data["DomainSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDomainsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDomainsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDomainResponse:
    boto3_raw_data: "type_defs.CreateDomainResponseTypeDef" = dataclasses.field()

    @cached_property
    def Domain(self):  # pragma: no cover
        return Domain.make_one(self.boto3_raw_data["Domain"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDomainResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDomainResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDomainResponse:
    boto3_raw_data: "type_defs.DescribeDomainResponseTypeDef" = dataclasses.field()

    @cached_property
    def Domain(self):  # pragma: no cover
        return Domain.make_one(self.boto3_raw_data["Domain"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDomainResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDomainResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDomainResponse:
    boto3_raw_data: "type_defs.UpdateDomainResponseTypeDef" = dataclasses.field()

    @cached_property
    def Domain(self):  # pragma: no cover
        return Domain.make_one(self.boto3_raw_data["Domain"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDomainResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDomainResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SpeakerEnrollmentJob:
    boto3_raw_data: "type_defs.SpeakerEnrollmentJobTypeDef" = dataclasses.field()

    CreatedAt = field("CreatedAt")
    DataAccessRoleArn = field("DataAccessRoleArn")
    DomainId = field("DomainId")
    EndedAt = field("EndedAt")

    @cached_property
    def EnrollmentConfig(self):  # pragma: no cover
        return EnrollmentConfigOutput.make_one(self.boto3_raw_data["EnrollmentConfig"])

    @cached_property
    def FailureDetails(self):  # pragma: no cover
        return FailureDetails.make_one(self.boto3_raw_data["FailureDetails"])

    @cached_property
    def InputDataConfig(self):  # pragma: no cover
        return InputDataConfig.make_one(self.boto3_raw_data["InputDataConfig"])

    JobId = field("JobId")
    JobName = field("JobName")

    @cached_property
    def JobProgress(self):  # pragma: no cover
        return JobProgress.make_one(self.boto3_raw_data["JobProgress"])

    JobStatus = field("JobStatus")

    @cached_property
    def OutputDataConfig(self):  # pragma: no cover
        return OutputDataConfig.make_one(self.boto3_raw_data["OutputDataConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SpeakerEnrollmentJobTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SpeakerEnrollmentJobTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FraudDetectionResult:
    boto3_raw_data: "type_defs.FraudDetectionResultTypeDef" = dataclasses.field()

    AudioAggregationEndedAt = field("AudioAggregationEndedAt")
    AudioAggregationStartedAt = field("AudioAggregationStartedAt")

    @cached_property
    def Configuration(self):  # pragma: no cover
        return FraudDetectionConfiguration.make_one(
            self.boto3_raw_data["Configuration"]
        )

    Decision = field("Decision")
    FraudDetectionResultId = field("FraudDetectionResultId")
    Reasons = field("Reasons")

    @cached_property
    def RiskDetails(self):  # pragma: no cover
        return FraudRiskDetails.make_one(self.boto3_raw_data["RiskDetails"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FraudDetectionResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FraudDetectionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFraudsterRegistrationJobsResponse:
    boto3_raw_data: "type_defs.ListFraudsterRegistrationJobsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def JobSummaries(self):  # pragma: no cover
        return FraudsterRegistrationJobSummary.make_many(
            self.boto3_raw_data["JobSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListFraudsterRegistrationJobsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFraudsterRegistrationJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSpeakerEnrollmentJobsResponse:
    boto3_raw_data: "type_defs.ListSpeakerEnrollmentJobsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def JobSummaries(self):  # pragma: no cover
        return SpeakerEnrollmentJobSummary.make_many(
            self.boto3_raw_data["JobSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSpeakerEnrollmentJobsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSpeakerEnrollmentJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFraudsterRegistrationJobResponse:
    boto3_raw_data: "type_defs.DescribeFraudsterRegistrationJobResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Job(self):  # pragma: no cover
        return FraudsterRegistrationJob.make_one(self.boto3_raw_data["Job"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeFraudsterRegistrationJobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFraudsterRegistrationJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartFraudsterRegistrationJobResponse:
    boto3_raw_data: "type_defs.StartFraudsterRegistrationJobResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Job(self):  # pragma: no cover
        return FraudsterRegistrationJob.make_one(self.boto3_raw_data["Job"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartFraudsterRegistrationJobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartFraudsterRegistrationJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartFraudsterRegistrationJobRequest:
    boto3_raw_data: "type_defs.StartFraudsterRegistrationJobRequestTypeDef" = (
        dataclasses.field()
    )

    DataAccessRoleArn = field("DataAccessRoleArn")
    DomainId = field("DomainId")

    @cached_property
    def InputDataConfig(self):  # pragma: no cover
        return InputDataConfig.make_one(self.boto3_raw_data["InputDataConfig"])

    @cached_property
    def OutputDataConfig(self):  # pragma: no cover
        return OutputDataConfig.make_one(self.boto3_raw_data["OutputDataConfig"])

    ClientToken = field("ClientToken")
    JobName = field("JobName")
    RegistrationConfig = field("RegistrationConfig")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartFraudsterRegistrationJobRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartFraudsterRegistrationJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSpeakerEnrollmentJobResponse:
    boto3_raw_data: "type_defs.DescribeSpeakerEnrollmentJobResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Job(self):  # pragma: no cover
        return SpeakerEnrollmentJob.make_one(self.boto3_raw_data["Job"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeSpeakerEnrollmentJobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSpeakerEnrollmentJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartSpeakerEnrollmentJobResponse:
    boto3_raw_data: "type_defs.StartSpeakerEnrollmentJobResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Job(self):  # pragma: no cover
        return SpeakerEnrollmentJob.make_one(self.boto3_raw_data["Job"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartSpeakerEnrollmentJobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSpeakerEnrollmentJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartSpeakerEnrollmentJobRequest:
    boto3_raw_data: "type_defs.StartSpeakerEnrollmentJobRequestTypeDef" = (
        dataclasses.field()
    )

    DataAccessRoleArn = field("DataAccessRoleArn")
    DomainId = field("DomainId")

    @cached_property
    def InputDataConfig(self):  # pragma: no cover
        return InputDataConfig.make_one(self.boto3_raw_data["InputDataConfig"])

    @cached_property
    def OutputDataConfig(self):  # pragma: no cover
        return OutputDataConfig.make_one(self.boto3_raw_data["OutputDataConfig"])

    ClientToken = field("ClientToken")
    EnrollmentConfig = field("EnrollmentConfig")
    JobName = field("JobName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartSpeakerEnrollmentJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSpeakerEnrollmentJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluateSessionResponse:
    boto3_raw_data: "type_defs.EvaluateSessionResponseTypeDef" = dataclasses.field()

    @cached_property
    def AuthenticationResult(self):  # pragma: no cover
        return AuthenticationResult.make_one(
            self.boto3_raw_data["AuthenticationResult"]
        )

    DomainId = field("DomainId")

    @cached_property
    def FraudDetectionResult(self):  # pragma: no cover
        return FraudDetectionResult.make_one(
            self.boto3_raw_data["FraudDetectionResult"]
        )

    SessionId = field("SessionId")
    SessionName = field("SessionName")
    StreamingStatus = field("StreamingStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EvaluateSessionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluateSessionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]

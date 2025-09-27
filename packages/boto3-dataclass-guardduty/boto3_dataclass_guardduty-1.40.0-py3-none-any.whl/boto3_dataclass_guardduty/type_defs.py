# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_guardduty import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AcceptAdministratorInvitationRequest:
    boto3_raw_data: "type_defs.AcceptAdministratorInvitationRequestTypeDef" = (
        dataclasses.field()
    )

    DetectorId = field("DetectorId")
    AdministratorId = field("AdministratorId")
    InvitationId = field("InvitationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AcceptAdministratorInvitationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AcceptAdministratorInvitationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AcceptInvitationRequest:
    boto3_raw_data: "type_defs.AcceptInvitationRequestTypeDef" = dataclasses.field()

    DetectorId = field("DetectorId")
    MasterId = field("MasterId")
    InvitationId = field("InvitationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AcceptInvitationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AcceptInvitationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccessControlList:
    boto3_raw_data: "type_defs.AccessControlListTypeDef" = dataclasses.field()

    AllowsPublicReadAccess = field("AllowsPublicReadAccess")
    AllowsPublicWriteAccess = field("AllowsPublicWriteAccess")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccessControlListTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccessControlListTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccessKeyDetails:
    boto3_raw_data: "type_defs.AccessKeyDetailsTypeDef" = dataclasses.field()

    AccessKeyId = field("AccessKeyId")
    PrincipalId = field("PrincipalId")
    UserName = field("UserName")
    UserType = field("UserType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccessKeyDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccessKeyDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccessKey:
    boto3_raw_data: "type_defs.AccessKeyTypeDef" = dataclasses.field()

    PrincipalId = field("PrincipalId")
    UserName = field("UserName")
    UserType = field("UserType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccessKeyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccessKeyTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccountDetail:
    boto3_raw_data: "type_defs.AccountDetailTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    Email = field("Email")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccountDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccountDetailTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FreeTrialFeatureConfigurationResult:
    boto3_raw_data: "type_defs.FreeTrialFeatureConfigurationResultTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    FreeTrialDaysRemaining = field("FreeTrialDaysRemaining")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.FreeTrialFeatureConfigurationResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FreeTrialFeatureConfigurationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BlockPublicAccess:
    boto3_raw_data: "type_defs.BlockPublicAccessTypeDef" = dataclasses.field()

    IgnorePublicAcls = field("IgnorePublicAcls")
    RestrictPublicBuckets = field("RestrictPublicBuckets")
    BlockPublicAcls = field("BlockPublicAcls")
    BlockPublicPolicy = field("BlockPublicPolicy")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BlockPublicAccessTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BlockPublicAccessTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccountStatistics:
    boto3_raw_data: "type_defs.AccountStatisticsTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    LastGeneratedAt = field("LastGeneratedAt")
    TotalFindings = field("TotalFindings")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccountStatisticsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccountStatisticsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Account:
    boto3_raw_data: "type_defs.AccountTypeDef" = dataclasses.field()

    Uid = field("Uid")
    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccountTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccountTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DnsRequestAction:
    boto3_raw_data: "type_defs.DnsRequestActionTypeDef" = dataclasses.field()

    Domain = field("Domain")
    Protocol = field("Protocol")
    Blocked = field("Blocked")
    DomainWithSuffix = field("DomainWithSuffix")
    VpcOwnerAccountId = field("VpcOwnerAccountId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DnsRequestActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DnsRequestActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KubernetesPermissionCheckedDetails:
    boto3_raw_data: "type_defs.KubernetesPermissionCheckedDetailsTypeDef" = (
        dataclasses.field()
    )

    Verb = field("Verb")
    Resource = field("Resource")
    Namespace = field("Namespace")
    Allowed = field("Allowed")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.KubernetesPermissionCheckedDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KubernetesPermissionCheckedDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KubernetesRoleBindingDetails:
    boto3_raw_data: "type_defs.KubernetesRoleBindingDetailsTypeDef" = (
        dataclasses.field()
    )

    Kind = field("Kind")
    Name = field("Name")
    Uid = field("Uid")
    RoleRefName = field("RoleRefName")
    RoleRefKind = field("RoleRefKind")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KubernetesRoleBindingDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KubernetesRoleBindingDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KubernetesRoleDetails:
    boto3_raw_data: "type_defs.KubernetesRoleDetailsTypeDef" = dataclasses.field()

    Kind = field("Kind")
    Name = field("Name")
    Uid = field("Uid")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KubernetesRoleDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KubernetesRoleDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActorProcess:
    boto3_raw_data: "type_defs.ActorProcessTypeDef" = dataclasses.field()

    Name = field("Name")
    Path = field("Path")
    Sha256 = field("Sha256")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActorProcessTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ActorProcessTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Session:
    boto3_raw_data: "type_defs.SessionTypeDef" = dataclasses.field()

    Uid = field("Uid")
    MfaStatus = field("MfaStatus")
    CreatedTime = field("CreatedTime")
    Issuer = field("Issuer")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SessionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SessionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddonDetails:
    boto3_raw_data: "type_defs.AddonDetailsTypeDef" = dataclasses.field()

    AddonVersion = field("AddonVersion")
    AddonStatus = field("AddonStatus")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AddonDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AddonDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdminAccount:
    boto3_raw_data: "type_defs.AdminAccountTypeDef" = dataclasses.field()

    AdminAccountId = field("AdminAccountId")
    AdminStatus = field("AdminStatus")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AdminAccountTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AdminAccountTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Administrator:
    boto3_raw_data: "type_defs.AdministratorTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    InvitationId = field("InvitationId")
    RelationshipStatus = field("RelationshipStatus")
    InvitedAt = field("InvitedAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AdministratorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AdministratorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AgentDetails:
    boto3_raw_data: "type_defs.AgentDetailsTypeDef" = dataclasses.field()

    Version = field("Version")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AgentDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AgentDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Observations:
    boto3_raw_data: "type_defs.ObservationsTypeDef" = dataclasses.field()

    Text = field("Text")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ObservationsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ObservationsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ArchiveFindingsRequest:
    boto3_raw_data: "type_defs.ArchiveFindingsRequestTypeDef" = dataclasses.field()

    DetectorId = field("DetectorId")
    FindingIds = field("FindingIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ArchiveFindingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ArchiveFindingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutonomousSystem:
    boto3_raw_data: "type_defs.AutonomousSystemTypeDef" = dataclasses.field()

    Name = field("Name")
    Number = field("Number")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AutonomousSystemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutonomousSystemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainDetails:
    boto3_raw_data: "type_defs.DomainDetailsTypeDef" = dataclasses.field()

    Domain = field("Domain")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DomainDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DomainDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoteAccountDetails:
    boto3_raw_data: "type_defs.RemoteAccountDetailsTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    Affiliated = field("Affiliated")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RemoteAccountDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoteAccountDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BucketPolicy:
    boto3_raw_data: "type_defs.BucketPolicyTypeDef" = dataclasses.field()

    AllowsPublicReadAccess = field("AllowsPublicReadAccess")
    AllowsPublicWriteAccess = field("AllowsPublicWriteAccess")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BucketPolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BucketPolicyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class City:
    boto3_raw_data: "type_defs.CityTypeDef" = dataclasses.field()

    CityName = field("CityName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CityTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudTrailConfigurationResult:
    boto3_raw_data: "type_defs.CloudTrailConfigurationResultTypeDef" = (
        dataclasses.field()
    )

    Status = field("Status")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CloudTrailConfigurationResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudTrailConfigurationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConditionOutput:
    boto3_raw_data: "type_defs.ConditionOutputTypeDef" = dataclasses.field()

    Eq = field("Eq")
    Neq = field("Neq")
    Gt = field("Gt")
    Gte = field("Gte")
    Lt = field("Lt")
    Lte = field("Lte")
    Equals = field("Equals")
    NotEquals = field("NotEquals")
    GreaterThan = field("GreaterThan")
    GreaterThanOrEqual = field("GreaterThanOrEqual")
    LessThan = field("LessThan")
    LessThanOrEqual = field("LessThanOrEqual")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConditionOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConditionOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Condition:
    boto3_raw_data: "type_defs.ConditionTypeDef" = dataclasses.field()

    Eq = field("Eq")
    Neq = field("Neq")
    Gt = field("Gt")
    Gte = field("Gte")
    Lt = field("Lt")
    Lte = field("Lte")
    Equals = field("Equals")
    NotEquals = field("NotEquals")
    GreaterThan = field("GreaterThan")
    GreaterThanOrEqual = field("GreaterThanOrEqual")
    LessThan = field("LessThan")
    LessThanOrEqual = field("LessThanOrEqual")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConditionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConditionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerFindingResource:
    boto3_raw_data: "type_defs.ContainerFindingResourceTypeDef" = dataclasses.field()

    Image = field("Image")
    ImageUid = field("ImageUid")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContainerFindingResourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerFindingResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerInstanceDetails:
    boto3_raw_data: "type_defs.ContainerInstanceDetailsTypeDef" = dataclasses.field()

    CoveredContainerInstances = field("CoveredContainerInstances")
    CompatibleContainerInstances = field("CompatibleContainerInstances")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContainerInstanceDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerInstanceDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SecurityContext:
    boto3_raw_data: "type_defs.SecurityContextTypeDef" = dataclasses.field()

    Privileged = field("Privileged")
    AllowPrivilegeEscalation = field("AllowPrivilegeEscalation")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SecurityContextTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SecurityContextTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VolumeMount:
    boto3_raw_data: "type_defs.VolumeMountTypeDef" = dataclasses.field()

    Name = field("Name")
    MountPath = field("MountPath")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VolumeMountTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VolumeMountTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Country:
    boto3_raw_data: "type_defs.CountryTypeDef" = dataclasses.field()

    CountryCode = field("CountryCode")
    CountryName = field("CountryName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CountryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CountryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FargateDetails:
    boto3_raw_data: "type_defs.FargateDetailsTypeDef" = dataclasses.field()

    Issues = field("Issues")
    ManagementType = field("ManagementType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FargateDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FargateDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CoverageFilterCondition:
    boto3_raw_data: "type_defs.CoverageFilterConditionTypeDef" = dataclasses.field()

    Equals = field("Equals")
    NotEquals = field("NotEquals")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CoverageFilterConditionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CoverageFilterConditionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CoverageSortCriteria:
    boto3_raw_data: "type_defs.CoverageSortCriteriaTypeDef" = dataclasses.field()

    AttributeName = field("AttributeName")
    OrderBy = field("OrderBy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CoverageSortCriteriaTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CoverageSortCriteriaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CoverageStatistics:
    boto3_raw_data: "type_defs.CoverageStatisticsTypeDef" = dataclasses.field()

    CountByResourceType = field("CountByResourceType")
    CountByCoverageStatus = field("CountByCoverageStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CoverageStatisticsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CoverageStatisticsTypeDef"]
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
class CreateIPSetRequest:
    boto3_raw_data: "type_defs.CreateIPSetRequestTypeDef" = dataclasses.field()

    DetectorId = field("DetectorId")
    Name = field("Name")
    Format = field("Format")
    Location = field("Location")
    Activate = field("Activate")
    ClientToken = field("ClientToken")
    Tags = field("Tags")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateIPSetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateIPSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UnprocessedAccount:
    boto3_raw_data: "type_defs.UnprocessedAccountTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    Result = field("Result")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UnprocessedAccountTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UnprocessedAccountTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateS3BucketResourceOutput:
    boto3_raw_data: "type_defs.CreateS3BucketResourceOutputTypeDef" = (
        dataclasses.field()
    )

    BucketName = field("BucketName")
    ObjectPrefixes = field("ObjectPrefixes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateS3BucketResourceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateS3BucketResourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateS3BucketResource:
    boto3_raw_data: "type_defs.CreateS3BucketResourceTypeDef" = dataclasses.field()

    BucketName = field("BucketName")
    ObjectPrefixes = field("ObjectPrefixes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateS3BucketResourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateS3BucketResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DestinationProperties:
    boto3_raw_data: "type_defs.DestinationPropertiesTypeDef" = dataclasses.field()

    DestinationArn = field("DestinationArn")
    KmsKeyArn = field("KmsKeyArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DestinationPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DestinationPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSampleFindingsRequest:
    boto3_raw_data: "type_defs.CreateSampleFindingsRequestTypeDef" = dataclasses.field()

    DetectorId = field("DetectorId")
    FindingTypes = field("FindingTypes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSampleFindingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSampleFindingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateThreatEntitySetRequest:
    boto3_raw_data: "type_defs.CreateThreatEntitySetRequestTypeDef" = (
        dataclasses.field()
    )

    DetectorId = field("DetectorId")
    Name = field("Name")
    Format = field("Format")
    Location = field("Location")
    Activate = field("Activate")
    ExpectedBucketOwner = field("ExpectedBucketOwner")
    ClientToken = field("ClientToken")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateThreatEntitySetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateThreatEntitySetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateThreatIntelSetRequest:
    boto3_raw_data: "type_defs.CreateThreatIntelSetRequestTypeDef" = dataclasses.field()

    DetectorId = field("DetectorId")
    Name = field("Name")
    Format = field("Format")
    Location = field("Location")
    Activate = field("Activate")
    ClientToken = field("ClientToken")
    Tags = field("Tags")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateThreatIntelSetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateThreatIntelSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTrustedEntitySetRequest:
    boto3_raw_data: "type_defs.CreateTrustedEntitySetRequestTypeDef" = (
        dataclasses.field()
    )

    DetectorId = field("DetectorId")
    Name = field("Name")
    Format = field("Format")
    Location = field("Location")
    Activate = field("Activate")
    ExpectedBucketOwner = field("ExpectedBucketOwner")
    ClientToken = field("ClientToken")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateTrustedEntitySetRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTrustedEntitySetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DNSLogsConfigurationResult:
    boto3_raw_data: "type_defs.DNSLogsConfigurationResultTypeDef" = dataclasses.field()

    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DNSLogsConfigurationResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DNSLogsConfigurationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlowLogsConfigurationResult:
    boto3_raw_data: "type_defs.FlowLogsConfigurationResultTypeDef" = dataclasses.field()

    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FlowLogsConfigurationResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FlowLogsConfigurationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3LogsConfigurationResult:
    boto3_raw_data: "type_defs.S3LogsConfigurationResultTypeDef" = dataclasses.field()

    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3LogsConfigurationResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3LogsConfigurationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3LogsConfiguration:
    boto3_raw_data: "type_defs.S3LogsConfigurationTypeDef" = dataclasses.field()

    Enable = field("Enable")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3LogsConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3LogsConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSourceFreeTrial:
    boto3_raw_data: "type_defs.DataSourceFreeTrialTypeDef" = dataclasses.field()

    FreeTrialDaysRemaining = field("FreeTrialDaysRemaining")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataSourceFreeTrialTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataSourceFreeTrialTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DateStatistics:
    boto3_raw_data: "type_defs.DateStatisticsTypeDef" = dataclasses.field()

    Date = field("Date")
    LastGeneratedAt = field("LastGeneratedAt")
    Severity = field("Severity")
    TotalFindings = field("TotalFindings")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DateStatisticsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DateStatisticsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeclineInvitationsRequest:
    boto3_raw_data: "type_defs.DeclineInvitationsRequestTypeDef" = dataclasses.field()

    AccountIds = field("AccountIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeclineInvitationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeclineInvitationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DefaultServerSideEncryption:
    boto3_raw_data: "type_defs.DefaultServerSideEncryptionTypeDef" = dataclasses.field()

    EncryptionType = field("EncryptionType")
    KmsMasterKeyArn = field("KmsMasterKeyArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DefaultServerSideEncryptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DefaultServerSideEncryptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDetectorRequest:
    boto3_raw_data: "type_defs.DeleteDetectorRequestTypeDef" = dataclasses.field()

    DetectorId = field("DetectorId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDetectorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDetectorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFilterRequest:
    boto3_raw_data: "type_defs.DeleteFilterRequestTypeDef" = dataclasses.field()

    DetectorId = field("DetectorId")
    FilterName = field("FilterName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteFilterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFilterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteIPSetRequest:
    boto3_raw_data: "type_defs.DeleteIPSetRequestTypeDef" = dataclasses.field()

    DetectorId = field("DetectorId")
    IpSetId = field("IpSetId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteIPSetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteIPSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteInvitationsRequest:
    boto3_raw_data: "type_defs.DeleteInvitationsRequestTypeDef" = dataclasses.field()

    AccountIds = field("AccountIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteInvitationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteInvitationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMalwareProtectionPlanRequest:
    boto3_raw_data: "type_defs.DeleteMalwareProtectionPlanRequestTypeDef" = (
        dataclasses.field()
    )

    MalwareProtectionPlanId = field("MalwareProtectionPlanId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteMalwareProtectionPlanRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMalwareProtectionPlanRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMembersRequest:
    boto3_raw_data: "type_defs.DeleteMembersRequestTypeDef" = dataclasses.field()

    DetectorId = field("DetectorId")
    AccountIds = field("AccountIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteMembersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMembersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePublishingDestinationRequest:
    boto3_raw_data: "type_defs.DeletePublishingDestinationRequestTypeDef" = (
        dataclasses.field()
    )

    DetectorId = field("DetectorId")
    DestinationId = field("DestinationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeletePublishingDestinationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePublishingDestinationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteThreatEntitySetRequest:
    boto3_raw_data: "type_defs.DeleteThreatEntitySetRequestTypeDef" = (
        dataclasses.field()
    )

    DetectorId = field("DetectorId")
    ThreatEntitySetId = field("ThreatEntitySetId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteThreatEntitySetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteThreatEntitySetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteThreatIntelSetRequest:
    boto3_raw_data: "type_defs.DeleteThreatIntelSetRequestTypeDef" = dataclasses.field()

    DetectorId = field("DetectorId")
    ThreatIntelSetId = field("ThreatIntelSetId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteThreatIntelSetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteThreatIntelSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTrustedEntitySetRequest:
    boto3_raw_data: "type_defs.DeleteTrustedEntitySetRequestTypeDef" = (
        dataclasses.field()
    )

    DetectorId = field("DetectorId")
    TrustedEntitySetId = field("TrustedEntitySetId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteTrustedEntitySetRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTrustedEntitySetRequestTypeDef"]
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
class SortCriteria:
    boto3_raw_data: "type_defs.SortCriteriaTypeDef" = dataclasses.field()

    AttributeName = field("AttributeName")
    OrderBy = field("OrderBy")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SortCriteriaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SortCriteriaTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOrganizationConfigurationRequest:
    boto3_raw_data: "type_defs.DescribeOrganizationConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    DetectorId = field("DetectorId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeOrganizationConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeOrganizationConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePublishingDestinationRequest:
    boto3_raw_data: "type_defs.DescribePublishingDestinationRequestTypeDef" = (
        dataclasses.field()
    )

    DetectorId = field("DetectorId")
    DestinationId = field("DestinationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribePublishingDestinationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePublishingDestinationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Destination:
    boto3_raw_data: "type_defs.DestinationTypeDef" = dataclasses.field()

    DestinationId = field("DestinationId")
    DestinationType = field("DestinationType")
    Status = field("Status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DestinationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DestinationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectorAdditionalConfigurationResult:
    boto3_raw_data: "type_defs.DetectorAdditionalConfigurationResultTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Status = field("Status")
    UpdatedAt = field("UpdatedAt")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DetectorAdditionalConfigurationResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectorAdditionalConfigurationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectorAdditionalConfiguration:
    boto3_raw_data: "type_defs.DetectorAdditionalConfigurationTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Status = field("Status")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DetectorAdditionalConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectorAdditionalConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisableOrganizationAdminAccountRequest:
    boto3_raw_data: "type_defs.DisableOrganizationAdminAccountRequestTypeDef" = (
        dataclasses.field()
    )

    AdminAccountId = field("AdminAccountId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisableOrganizationAdminAccountRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisableOrganizationAdminAccountRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateFromAdministratorAccountRequest:
    boto3_raw_data: "type_defs.DisassociateFromAdministratorAccountRequestTypeDef" = (
        dataclasses.field()
    )

    DetectorId = field("DetectorId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateFromAdministratorAccountRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateFromAdministratorAccountRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateFromMasterAccountRequest:
    boto3_raw_data: "type_defs.DisassociateFromMasterAccountRequestTypeDef" = (
        dataclasses.field()
    )

    DetectorId = field("DetectorId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateFromMasterAccountRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateFromMasterAccountRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateMembersRequest:
    boto3_raw_data: "type_defs.DisassociateMembersRequestTypeDef" = dataclasses.field()

    DetectorId = field("DetectorId")
    AccountIds = field("AccountIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisassociateMembersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateMembersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VolumeDetail:
    boto3_raw_data: "type_defs.VolumeDetailTypeDef" = dataclasses.field()

    VolumeArn = field("VolumeArn")
    VolumeType = field("VolumeType")
    DeviceName = field("DeviceName")
    VolumeSizeInGB = field("VolumeSizeInGB")
    EncryptionType = field("EncryptionType")
    SnapshotArn = field("SnapshotArn")
    KmsKeyArn = field("KmsKeyArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VolumeDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VolumeDetailTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EbsVolumesResult:
    boto3_raw_data: "type_defs.EbsVolumesResultTypeDef" = dataclasses.field()

    Status = field("Status")
    Reason = field("Reason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EbsVolumesResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EbsVolumesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IamInstanceProfile:
    boto3_raw_data: "type_defs.IamInstanceProfileTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IamInstanceProfileTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IamInstanceProfileTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProductCode:
    boto3_raw_data: "type_defs.ProductCodeTypeDef" = dataclasses.field()

    Code = field("Code")
    ProductType = field("ProductType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProductCodeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProductCodeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PrivateIpAddressDetails:
    boto3_raw_data: "type_defs.PrivateIpAddressDetailsTypeDef" = dataclasses.field()

    PrivateDnsName = field("PrivateDnsName")
    PrivateIpAddress = field("PrivateIpAddress")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PrivateIpAddressDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PrivateIpAddressDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SecurityGroup:
    boto3_raw_data: "type_defs.SecurityGroupTypeDef" = dataclasses.field()

    GroupId = field("GroupId")
    GroupName = field("GroupName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SecurityGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SecurityGroupTypeDef"]],
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
class EksCluster:
    boto3_raw_data: "type_defs.EksClusterTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CreatedAt = field("CreatedAt")
    Status = field("Status")
    VpcId = field("VpcId")
    Ec2InstanceUids = field("Ec2InstanceUids")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EksClusterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EksClusterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnableOrganizationAdminAccountRequest:
    boto3_raw_data: "type_defs.EnableOrganizationAdminAccountRequestTypeDef" = (
        dataclasses.field()
    )

    AdminAccountId = field("AdminAccountId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EnableOrganizationAdminAccountRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnableOrganizationAdminAccountRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ThreatIntelligenceDetail:
    boto3_raw_data: "type_defs.ThreatIntelligenceDetailTypeDef" = dataclasses.field()

    ThreatListName = field("ThreatListName")
    ThreatNames = field("ThreatNames")
    ThreatFileSha256 = field("ThreatFileSha256")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ThreatIntelligenceDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ThreatIntelligenceDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FilterCondition:
    boto3_raw_data: "type_defs.FilterConditionTypeDef" = dataclasses.field()

    EqualsValue = field("EqualsValue")
    GreaterThan = field("GreaterThan")
    LessThan = field("LessThan")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FilterConditionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FilterConditionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FindingTypeStatistics:
    boto3_raw_data: "type_defs.FindingTypeStatisticsTypeDef" = dataclasses.field()

    FindingType = field("FindingType")
    LastGeneratedAt = field("LastGeneratedAt")
    TotalFindings = field("TotalFindings")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FindingTypeStatisticsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FindingTypeStatisticsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceStatistics:
    boto3_raw_data: "type_defs.ResourceStatisticsTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    LastGeneratedAt = field("LastGeneratedAt")
    ResourceId = field("ResourceId")
    ResourceType = field("ResourceType")
    TotalFindings = field("TotalFindings")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceStatisticsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceStatisticsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SeverityStatistics:
    boto3_raw_data: "type_defs.SeverityStatisticsTypeDef" = dataclasses.field()

    LastGeneratedAt = field("LastGeneratedAt")
    Severity = field("Severity")
    TotalFindings = field("TotalFindings")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SeverityStatisticsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SeverityStatisticsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GeoLocation:
    boto3_raw_data: "type_defs.GeoLocationTypeDef" = dataclasses.field()

    Lat = field("Lat")
    Lon = field("Lon")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GeoLocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GeoLocationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAdministratorAccountRequest:
    boto3_raw_data: "type_defs.GetAdministratorAccountRequestTypeDef" = (
        dataclasses.field()
    )

    DetectorId = field("DetectorId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetAdministratorAccountRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAdministratorAccountRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDetectorRequest:
    boto3_raw_data: "type_defs.GetDetectorRequestTypeDef" = dataclasses.field()

    DetectorId = field("DetectorId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDetectorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDetectorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFilterRequest:
    boto3_raw_data: "type_defs.GetFilterRequestTypeDef" = dataclasses.field()

    DetectorId = field("DetectorId")
    FilterName = field("FilterName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetFilterRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFilterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIPSetRequest:
    boto3_raw_data: "type_defs.GetIPSetRequestTypeDef" = dataclasses.field()

    DetectorId = field("DetectorId")
    IpSetId = field("IpSetId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetIPSetRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetIPSetRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMalwareProtectionPlanRequest:
    boto3_raw_data: "type_defs.GetMalwareProtectionPlanRequestTypeDef" = (
        dataclasses.field()
    )

    MalwareProtectionPlanId = field("MalwareProtectionPlanId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetMalwareProtectionPlanRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMalwareProtectionPlanRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MalwareProtectionPlanStatusReason:
    boto3_raw_data: "type_defs.MalwareProtectionPlanStatusReasonTypeDef" = (
        dataclasses.field()
    )

    Code = field("Code")
    Message = field("Message")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MalwareProtectionPlanStatusReasonTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MalwareProtectionPlanStatusReasonTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMalwareScanSettingsRequest:
    boto3_raw_data: "type_defs.GetMalwareScanSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    DetectorId = field("DetectorId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetMalwareScanSettingsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMalwareScanSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMasterAccountRequest:
    boto3_raw_data: "type_defs.GetMasterAccountRequestTypeDef" = dataclasses.field()

    DetectorId = field("DetectorId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMasterAccountRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMasterAccountRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Master:
    boto3_raw_data: "type_defs.MasterTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    InvitationId = field("InvitationId")
    RelationshipStatus = field("RelationshipStatus")
    InvitedAt = field("InvitedAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MasterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MasterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMemberDetectorsRequest:
    boto3_raw_data: "type_defs.GetMemberDetectorsRequestTypeDef" = dataclasses.field()

    DetectorId = field("DetectorId")
    AccountIds = field("AccountIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMemberDetectorsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMemberDetectorsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMembersRequest:
    boto3_raw_data: "type_defs.GetMembersRequestTypeDef" = dataclasses.field()

    DetectorId = field("DetectorId")
    AccountIds = field("AccountIds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetMembersRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMembersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Member:
    boto3_raw_data: "type_defs.MemberTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    MasterId = field("MasterId")
    Email = field("Email")
    RelationshipStatus = field("RelationshipStatus")
    UpdatedAt = field("UpdatedAt")
    DetectorId = field("DetectorId")
    InvitedAt = field("InvitedAt")
    AdministratorId = field("AdministratorId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MemberTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MemberTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRemainingFreeTrialDaysRequest:
    boto3_raw_data: "type_defs.GetRemainingFreeTrialDaysRequestTypeDef" = (
        dataclasses.field()
    )

    DetectorId = field("DetectorId")
    AccountIds = field("AccountIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetRemainingFreeTrialDaysRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRemainingFreeTrialDaysRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetThreatEntitySetRequest:
    boto3_raw_data: "type_defs.GetThreatEntitySetRequestTypeDef" = dataclasses.field()

    DetectorId = field("DetectorId")
    ThreatEntitySetId = field("ThreatEntitySetId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetThreatEntitySetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetThreatEntitySetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetThreatIntelSetRequest:
    boto3_raw_data: "type_defs.GetThreatIntelSetRequestTypeDef" = dataclasses.field()

    DetectorId = field("DetectorId")
    ThreatIntelSetId = field("ThreatIntelSetId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetThreatIntelSetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetThreatIntelSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTrustedEntitySetRequest:
    boto3_raw_data: "type_defs.GetTrustedEntitySetRequestTypeDef" = dataclasses.field()

    DetectorId = field("DetectorId")
    TrustedEntitySetId = field("TrustedEntitySetId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTrustedEntitySetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTrustedEntitySetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UsageCriteria:
    boto3_raw_data: "type_defs.UsageCriteriaTypeDef" = dataclasses.field()

    AccountIds = field("AccountIds")
    DataSources = field("DataSources")
    Resources = field("Resources")
    Features = field("Features")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UsageCriteriaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UsageCriteriaTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HighestSeverityThreatDetails:
    boto3_raw_data: "type_defs.HighestSeverityThreatDetailsTypeDef" = (
        dataclasses.field()
    )

    Severity = field("Severity")
    ThreatName = field("ThreatName")
    Count = field("Count")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HighestSeverityThreatDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HighestSeverityThreatDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HostPath:
    boto3_raw_data: "type_defs.HostPathTypeDef" = dataclasses.field()

    Path = field("Path")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HostPathTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HostPathTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImpersonatedUser:
    boto3_raw_data: "type_defs.ImpersonatedUserTypeDef" = dataclasses.field()

    Username = field("Username")
    Groups = field("Groups")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImpersonatedUserTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImpersonatedUserTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Indicator:
    boto3_raw_data: "type_defs.IndicatorTypeDef" = dataclasses.field()

    Key = field("Key")
    Values = field("Values")
    Title = field("Title")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IndicatorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IndicatorTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Invitation:
    boto3_raw_data: "type_defs.InvitationTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    InvitationId = field("InvitationId")
    RelationshipStatus = field("RelationshipStatus")
    InvitedAt = field("InvitedAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InvitationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InvitationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InviteMembersRequest:
    boto3_raw_data: "type_defs.InviteMembersRequestTypeDef" = dataclasses.field()

    DetectorId = field("DetectorId")
    AccountIds = field("AccountIds")
    DisableEmailNotification = field("DisableEmailNotification")
    Message = field("Message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InviteMembersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InviteMembersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ItemPath:
    boto3_raw_data: "type_defs.ItemPathTypeDef" = dataclasses.field()

    NestedItemPath = field("NestedItemPath")
    Hash = field("Hash")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ItemPathTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ItemPathTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KubernetesAuditLogsConfigurationResult:
    boto3_raw_data: "type_defs.KubernetesAuditLogsConfigurationResultTypeDef" = (
        dataclasses.field()
    )

    Status = field("Status")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.KubernetesAuditLogsConfigurationResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KubernetesAuditLogsConfigurationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KubernetesAuditLogsConfiguration:
    boto3_raw_data: "type_defs.KubernetesAuditLogsConfigurationTypeDef" = (
        dataclasses.field()
    )

    Enable = field("Enable")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.KubernetesAuditLogsConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KubernetesAuditLogsConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KubernetesWorkload:
    boto3_raw_data: "type_defs.KubernetesWorkloadTypeDef" = dataclasses.field()

    ContainerUids = field("ContainerUids")
    Namespace = field("Namespace")
    KubernetesResourcesTypes = field("KubernetesResourcesTypes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KubernetesWorkloadTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KubernetesWorkloadTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LineageObject:
    boto3_raw_data: "type_defs.LineageObjectTypeDef" = dataclasses.field()

    StartTime = field("StartTime")
    NamespacePid = field("NamespacePid")
    UserId = field("UserId")
    Name = field("Name")
    Pid = field("Pid")
    Uuid = field("Uuid")
    ExecutablePath = field("ExecutablePath")
    Euid = field("Euid")
    ParentUuid = field("ParentUuid")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LineageObjectTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LineageObjectTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDetectorsRequest:
    boto3_raw_data: "type_defs.ListDetectorsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDetectorsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDetectorsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFiltersRequest:
    boto3_raw_data: "type_defs.ListFiltersRequestTypeDef" = dataclasses.field()

    DetectorId = field("DetectorId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFiltersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFiltersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIPSetsRequest:
    boto3_raw_data: "type_defs.ListIPSetsRequestTypeDef" = dataclasses.field()

    DetectorId = field("DetectorId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListIPSetsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIPSetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInvitationsRequest:
    boto3_raw_data: "type_defs.ListInvitationsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInvitationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInvitationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMalwareProtectionPlansRequest:
    boto3_raw_data: "type_defs.ListMalwareProtectionPlansRequestTypeDef" = (
        dataclasses.field()
    )

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListMalwareProtectionPlansRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMalwareProtectionPlansRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MalwareProtectionPlanSummary:
    boto3_raw_data: "type_defs.MalwareProtectionPlanSummaryTypeDef" = (
        dataclasses.field()
    )

    MalwareProtectionPlanId = field("MalwareProtectionPlanId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MalwareProtectionPlanSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MalwareProtectionPlanSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMembersRequest:
    boto3_raw_data: "type_defs.ListMembersRequestTypeDef" = dataclasses.field()

    DetectorId = field("DetectorId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    OnlyAssociated = field("OnlyAssociated")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMembersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMembersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOrganizationAdminAccountsRequest:
    boto3_raw_data: "type_defs.ListOrganizationAdminAccountsRequestTypeDef" = (
        dataclasses.field()
    )

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListOrganizationAdminAccountsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOrganizationAdminAccountsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPublishingDestinationsRequest:
    boto3_raw_data: "type_defs.ListPublishingDestinationsRequestTypeDef" = (
        dataclasses.field()
    )

    DetectorId = field("DetectorId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPublishingDestinationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPublishingDestinationsRequestTypeDef"]
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
class ListThreatEntitySetsRequest:
    boto3_raw_data: "type_defs.ListThreatEntitySetsRequestTypeDef" = dataclasses.field()

    DetectorId = field("DetectorId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListThreatEntitySetsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListThreatEntitySetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListThreatIntelSetsRequest:
    boto3_raw_data: "type_defs.ListThreatIntelSetsRequestTypeDef" = dataclasses.field()

    DetectorId = field("DetectorId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListThreatIntelSetsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListThreatIntelSetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTrustedEntitySetsRequest:
    boto3_raw_data: "type_defs.ListTrustedEntitySetsRequestTypeDef" = (
        dataclasses.field()
    )

    DetectorId = field("DetectorId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTrustedEntitySetsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTrustedEntitySetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LocalIpDetails:
    boto3_raw_data: "type_defs.LocalIpDetailsTypeDef" = dataclasses.field()

    IpAddressV4 = field("IpAddressV4")
    IpAddressV6 = field("IpAddressV6")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LocalIpDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LocalIpDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LocalPortDetails:
    boto3_raw_data: "type_defs.LocalPortDetailsTypeDef" = dataclasses.field()

    Port = field("Port")
    PortName = field("PortName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LocalPortDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LocalPortDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoginAttribute:
    boto3_raw_data: "type_defs.LoginAttributeTypeDef" = dataclasses.field()

    User = field("User")
    Application = field("Application")
    FailedLoginAttempts = field("FailedLoginAttempts")
    SuccessfulLoginAttempts = field("SuccessfulLoginAttempts")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LoginAttributeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LoginAttributeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScanEc2InstanceWithFindings:
    boto3_raw_data: "type_defs.ScanEc2InstanceWithFindingsTypeDef" = dataclasses.field()

    EbsVolumes = field("EbsVolumes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScanEc2InstanceWithFindingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScanEc2InstanceWithFindingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MalwareProtectionPlanTaggingAction:
    boto3_raw_data: "type_defs.MalwareProtectionPlanTaggingActionTypeDef" = (
        dataclasses.field()
    )

    Status = field("Status")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MalwareProtectionPlanTaggingActionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MalwareProtectionPlanTaggingActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MemberAdditionalConfigurationResult:
    boto3_raw_data: "type_defs.MemberAdditionalConfigurationResultTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Status = field("Status")
    UpdatedAt = field("UpdatedAt")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MemberAdditionalConfigurationResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MemberAdditionalConfigurationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MemberAdditionalConfiguration:
    boto3_raw_data: "type_defs.MemberAdditionalConfigurationTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Status = field("Status")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.MemberAdditionalConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MemberAdditionalConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemotePortDetails:
    boto3_raw_data: "type_defs.RemotePortDetailsTypeDef" = dataclasses.field()

    Port = field("Port")
    PortName = field("PortName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RemotePortDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemotePortDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkConnection:
    boto3_raw_data: "type_defs.NetworkConnectionTypeDef" = dataclasses.field()

    Direction = field("Direction")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NetworkConnectionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkConnectionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkGeoLocation:
    boto3_raw_data: "type_defs.NetworkGeoLocationTypeDef" = dataclasses.field()

    City = field("City")
    Country = field("Country")
    Latitude = field("Latitude")
    Longitude = field("Longitude")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NetworkGeoLocationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkGeoLocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrganizationAdditionalConfigurationResult:
    boto3_raw_data: "type_defs.OrganizationAdditionalConfigurationResultTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    AutoEnable = field("AutoEnable")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OrganizationAdditionalConfigurationResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrganizationAdditionalConfigurationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrganizationAdditionalConfiguration:
    boto3_raw_data: "type_defs.OrganizationAdditionalConfigurationTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    AutoEnable = field("AutoEnable")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OrganizationAdditionalConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrganizationAdditionalConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrganizationS3LogsConfigurationResult:
    boto3_raw_data: "type_defs.OrganizationS3LogsConfigurationResultTypeDef" = (
        dataclasses.field()
    )

    AutoEnable = field("AutoEnable")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OrganizationS3LogsConfigurationResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrganizationS3LogsConfigurationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrganizationS3LogsConfiguration:
    boto3_raw_data: "type_defs.OrganizationS3LogsConfigurationTypeDef" = (
        dataclasses.field()
    )

    AutoEnable = field("AutoEnable")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.OrganizationS3LogsConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrganizationS3LogsConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrganizationEbsVolumesResult:
    boto3_raw_data: "type_defs.OrganizationEbsVolumesResultTypeDef" = (
        dataclasses.field()
    )

    AutoEnable = field("AutoEnable")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OrganizationEbsVolumesResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrganizationEbsVolumesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrganizationEbsVolumes:
    boto3_raw_data: "type_defs.OrganizationEbsVolumesTypeDef" = dataclasses.field()

    AutoEnable = field("AutoEnable")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OrganizationEbsVolumesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrganizationEbsVolumesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrganizationFeatureStatisticsAdditionalConfiguration:
    boto3_raw_data: (
        "type_defs.OrganizationFeatureStatisticsAdditionalConfigurationTypeDef"
    ) = dataclasses.field()

    Name = field("Name")
    EnabledAccountsCount = field("EnabledAccountsCount")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OrganizationFeatureStatisticsAdditionalConfigurationTypeDef"
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
                "type_defs.OrganizationFeatureStatisticsAdditionalConfigurationTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrganizationKubernetesAuditLogsConfigurationResult:
    boto3_raw_data: (
        "type_defs.OrganizationKubernetesAuditLogsConfigurationResultTypeDef"
    ) = dataclasses.field()

    AutoEnable = field("AutoEnable")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OrganizationKubernetesAuditLogsConfigurationResultTypeDef"
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
                "type_defs.OrganizationKubernetesAuditLogsConfigurationResultTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrganizationKubernetesAuditLogsConfiguration:
    boto3_raw_data: "type_defs.OrganizationKubernetesAuditLogsConfigurationTypeDef" = (
        dataclasses.field()
    )

    AutoEnable = field("AutoEnable")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OrganizationKubernetesAuditLogsConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrganizationKubernetesAuditLogsConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Organization:
    boto3_raw_data: "type_defs.OrganizationTypeDef" = dataclasses.field()

    Asn = field("Asn")
    AsnOrg = field("AsnOrg")
    Isp = field("Isp")
    Org = field("Org")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OrganizationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OrganizationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Owner:
    boto3_raw_data: "type_defs.OwnerTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OwnerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OwnerTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PublicAccessConfiguration:
    boto3_raw_data: "type_defs.PublicAccessConfigurationTypeDef" = dataclasses.field()

    PublicAclAccess = field("PublicAclAccess")
    PublicPolicyAccess = field("PublicPolicyAccess")
    PublicAclIgnoreBehavior = field("PublicAclIgnoreBehavior")
    PublicBucketRestrictBehavior = field("PublicBucketRestrictBehavior")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PublicAccessConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PublicAccessConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RdsDbUserDetails:
    boto3_raw_data: "type_defs.RdsDbUserDetailsTypeDef" = dataclasses.field()

    User = field("User")
    Application = field("Application")
    Database = field("Database")
    Ssl = field("Ssl")
    AuthMethod = field("AuthMethod")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RdsDbUserDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RdsDbUserDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Object:
    boto3_raw_data: "type_defs.S3ObjectTypeDef" = dataclasses.field()

    ETag = field("ETag")
    Key = field("Key")
    VersionId = field("VersionId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3ObjectTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3ObjectTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceDetails:
    boto3_raw_data: "type_defs.ResourceDetailsTypeDef" = dataclasses.field()

    InstanceArn = field("InstanceArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3ObjectDetail:
    boto3_raw_data: "type_defs.S3ObjectDetailTypeDef" = dataclasses.field()

    ObjectArn = field("ObjectArn")
    Key = field("Key")
    ETag = field("ETag")
    Hash = field("Hash")
    VersionId = field("VersionId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3ObjectDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3ObjectDetailTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScanConditionPair:
    boto3_raw_data: "type_defs.ScanConditionPairTypeDef" = dataclasses.field()

    Key = field("Key")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScanConditionPairTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScanConditionPairTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScannedItemCount:
    boto3_raw_data: "type_defs.ScannedItemCountTypeDef" = dataclasses.field()

    TotalGb = field("TotalGb")
    Files = field("Files")
    Volumes = field("Volumes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScannedItemCountTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScannedItemCountTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ThreatsDetectedItemCount:
    boto3_raw_data: "type_defs.ThreatsDetectedItemCountTypeDef" = dataclasses.field()

    Files = field("Files")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ThreatsDetectedItemCountTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ThreatsDetectedItemCountTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScanFilePath:
    boto3_raw_data: "type_defs.ScanFilePathTypeDef" = dataclasses.field()

    FilePath = field("FilePath")
    VolumeArn = field("VolumeArn")
    Hash = field("Hash")
    FileName = field("FileName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScanFilePathTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScanFilePathTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScanResultDetails:
    boto3_raw_data: "type_defs.ScanResultDetailsTypeDef" = dataclasses.field()

    ScanResult = field("ScanResult")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScanResultDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScanResultDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TriggerDetails:
    boto3_raw_data: "type_defs.TriggerDetailsTypeDef" = dataclasses.field()

    GuardDutyFindingId = field("GuardDutyFindingId")
    Description = field("Description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TriggerDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TriggerDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceAdditionalInfo:
    boto3_raw_data: "type_defs.ServiceAdditionalInfoTypeDef" = dataclasses.field()

    Value = field("Value")
    Type = field("Type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServiceAdditionalInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceAdditionalInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartMalwareScanRequest:
    boto3_raw_data: "type_defs.StartMalwareScanRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartMalwareScanRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartMalwareScanRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartMonitoringMembersRequest:
    boto3_raw_data: "type_defs.StartMonitoringMembersRequestTypeDef" = (
        dataclasses.field()
    )

    DetectorId = field("DetectorId")
    AccountIds = field("AccountIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartMonitoringMembersRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartMonitoringMembersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopMonitoringMembersRequest:
    boto3_raw_data: "type_defs.StopMonitoringMembersRequestTypeDef" = (
        dataclasses.field()
    )

    DetectorId = field("DetectorId")
    AccountIds = field("AccountIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopMonitoringMembersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopMonitoringMembersRequestTypeDef"]
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
    Tags = field("Tags")

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
class Total:
    boto3_raw_data: "type_defs.TotalTypeDef" = dataclasses.field()

    Amount = field("Amount")
    Unit = field("Unit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TotalTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TotalTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UnarchiveFindingsRequest:
    boto3_raw_data: "type_defs.UnarchiveFindingsRequestTypeDef" = dataclasses.field()

    DetectorId = field("DetectorId")
    FindingIds = field("FindingIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UnarchiveFindingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UnarchiveFindingsRequestTypeDef"]
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
class UpdateFindingsFeedbackRequest:
    boto3_raw_data: "type_defs.UpdateFindingsFeedbackRequestTypeDef" = (
        dataclasses.field()
    )

    DetectorId = field("DetectorId")
    FindingIds = field("FindingIds")
    Feedback = field("Feedback")
    Comments = field("Comments")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateFindingsFeedbackRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFindingsFeedbackRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateIPSetRequest:
    boto3_raw_data: "type_defs.UpdateIPSetRequestTypeDef" = dataclasses.field()

    DetectorId = field("DetectorId")
    IpSetId = field("IpSetId")
    Name = field("Name")
    Location = field("Location")
    Activate = field("Activate")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateIPSetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateIPSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateS3BucketResource:
    boto3_raw_data: "type_defs.UpdateS3BucketResourceTypeDef" = dataclasses.field()

    ObjectPrefixes = field("ObjectPrefixes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateS3BucketResourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateS3BucketResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateThreatEntitySetRequest:
    boto3_raw_data: "type_defs.UpdateThreatEntitySetRequestTypeDef" = (
        dataclasses.field()
    )

    DetectorId = field("DetectorId")
    ThreatEntitySetId = field("ThreatEntitySetId")
    Name = field("Name")
    Location = field("Location")
    ExpectedBucketOwner = field("ExpectedBucketOwner")
    Activate = field("Activate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateThreatEntitySetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateThreatEntitySetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateThreatIntelSetRequest:
    boto3_raw_data: "type_defs.UpdateThreatIntelSetRequestTypeDef" = dataclasses.field()

    DetectorId = field("DetectorId")
    ThreatIntelSetId = field("ThreatIntelSetId")
    Name = field("Name")
    Location = field("Location")
    Activate = field("Activate")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateThreatIntelSetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateThreatIntelSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTrustedEntitySetRequest:
    boto3_raw_data: "type_defs.UpdateTrustedEntitySetRequestTypeDef" = (
        dataclasses.field()
    )

    DetectorId = field("DetectorId")
    TrustedEntitySetId = field("TrustedEntitySetId")
    Name = field("Name")
    Location = field("Location")
    ExpectedBucketOwner = field("ExpectedBucketOwner")
    Activate = field("Activate")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateTrustedEntitySetRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTrustedEntitySetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMembersRequest:
    boto3_raw_data: "type_defs.CreateMembersRequestTypeDef" = dataclasses.field()

    DetectorId = field("DetectorId")

    @cached_property
    def AccountDetails(self):  # pragma: no cover
        return AccountDetail.make_many(self.boto3_raw_data["AccountDetails"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateMembersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMembersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccountLevelPermissions:
    boto3_raw_data: "type_defs.AccountLevelPermissionsTypeDef" = dataclasses.field()

    @cached_property
    def BlockPublicAccess(self):  # pragma: no cover
        return BlockPublicAccess.make_one(self.boto3_raw_data["BlockPublicAccess"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AccountLevelPermissionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccountLevelPermissionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class User:
    boto3_raw_data: "type_defs.UserTypeDef" = dataclasses.field()

    Name = field("Name")
    Uid = field("Uid")
    Type = field("Type")
    CredentialUid = field("CredentialUid")

    @cached_property
    def Account(self):  # pragma: no cover
        return Account.make_one(self.boto3_raw_data["Account"])

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
class CoverageEksClusterDetails:
    boto3_raw_data: "type_defs.CoverageEksClusterDetailsTypeDef" = dataclasses.field()

    ClusterName = field("ClusterName")
    CoveredNodes = field("CoveredNodes")
    CompatibleNodes = field("CompatibleNodes")

    @cached_property
    def AddonDetails(self):  # pragma: no cover
        return AddonDetails.make_one(self.boto3_raw_data["AddonDetails"])

    ManagementType = field("ManagementType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CoverageEksClusterDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CoverageEksClusterDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CoverageEc2InstanceDetails:
    boto3_raw_data: "type_defs.CoverageEc2InstanceDetailsTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    InstanceType = field("InstanceType")
    ClusterArn = field("ClusterArn")

    @cached_property
    def AgentDetails(self):  # pragma: no cover
        return AgentDetails.make_one(self.boto3_raw_data["AgentDetails"])

    ManagementType = field("ManagementType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CoverageEc2InstanceDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CoverageEc2InstanceDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnomalyObject:
    boto3_raw_data: "type_defs.AnomalyObjectTypeDef" = dataclasses.field()

    ProfileType = field("ProfileType")
    ProfileSubtype = field("ProfileSubtype")

    @cached_property
    def Observations(self):  # pragma: no cover
        return Observations.make_one(self.boto3_raw_data["Observations"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AnomalyObjectTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AnomalyObjectTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BucketLevelPermissions:
    boto3_raw_data: "type_defs.BucketLevelPermissionsTypeDef" = dataclasses.field()

    @cached_property
    def AccessControlList(self):  # pragma: no cover
        return AccessControlList.make_one(self.boto3_raw_data["AccessControlList"])

    @cached_property
    def BucketPolicy(self):  # pragma: no cover
        return BucketPolicy.make_one(self.boto3_raw_data["BucketPolicy"])

    @cached_property
    def BlockPublicAccess(self):  # pragma: no cover
        return BlockPublicAccess.make_one(self.boto3_raw_data["BlockPublicAccess"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BucketLevelPermissionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BucketLevelPermissionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FindingCriteriaOutput:
    boto3_raw_data: "type_defs.FindingCriteriaOutputTypeDef" = dataclasses.field()

    Criterion = field("Criterion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FindingCriteriaOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FindingCriteriaOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FindingCriteria:
    boto3_raw_data: "type_defs.FindingCriteriaTypeDef" = dataclasses.field()

    Criterion = field("Criterion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FindingCriteriaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FindingCriteriaTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Container:
    boto3_raw_data: "type_defs.ContainerTypeDef" = dataclasses.field()

    ContainerRuntime = field("ContainerRuntime")
    Id = field("Id")
    Name = field("Name")
    Image = field("Image")
    ImagePrefix = field("ImagePrefix")

    @cached_property
    def VolumeMounts(self):  # pragma: no cover
        return VolumeMount.make_many(self.boto3_raw_data["VolumeMounts"])

    @cached_property
    def SecurityContext(self):  # pragma: no cover
        return SecurityContext.make_one(self.boto3_raw_data["SecurityContext"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContainerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ContainerTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CoverageEcsClusterDetails:
    boto3_raw_data: "type_defs.CoverageEcsClusterDetailsTypeDef" = dataclasses.field()

    ClusterName = field("ClusterName")

    @cached_property
    def FargateDetails(self):  # pragma: no cover
        return FargateDetails.make_one(self.boto3_raw_data["FargateDetails"])

    @cached_property
    def ContainerInstanceDetails(self):  # pragma: no cover
        return ContainerInstanceDetails.make_one(
            self.boto3_raw_data["ContainerInstanceDetails"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CoverageEcsClusterDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CoverageEcsClusterDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CoverageFilterCriterion:
    boto3_raw_data: "type_defs.CoverageFilterCriterionTypeDef" = dataclasses.field()

    CriterionKey = field("CriterionKey")

    @cached_property
    def FilterCondition(self):  # pragma: no cover
        return CoverageFilterCondition.make_one(self.boto3_raw_data["FilterCondition"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CoverageFilterCriterionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CoverageFilterCriterionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFilterResponse:
    boto3_raw_data: "type_defs.CreateFilterResponseTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFilterResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFilterResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateIPSetResponse:
    boto3_raw_data: "type_defs.CreateIPSetResponseTypeDef" = dataclasses.field()

    IpSetId = field("IpSetId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateIPSetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateIPSetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMalwareProtectionPlanResponse:
    boto3_raw_data: "type_defs.CreateMalwareProtectionPlanResponseTypeDef" = (
        dataclasses.field()
    )

    MalwareProtectionPlanId = field("MalwareProtectionPlanId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateMalwareProtectionPlanResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMalwareProtectionPlanResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePublishingDestinationResponse:
    boto3_raw_data: "type_defs.CreatePublishingDestinationResponseTypeDef" = (
        dataclasses.field()
    )

    DestinationId = field("DestinationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreatePublishingDestinationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePublishingDestinationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateThreatEntitySetResponse:
    boto3_raw_data: "type_defs.CreateThreatEntitySetResponseTypeDef" = (
        dataclasses.field()
    )

    ThreatEntitySetId = field("ThreatEntitySetId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateThreatEntitySetResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateThreatEntitySetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateThreatIntelSetResponse:
    boto3_raw_data: "type_defs.CreateThreatIntelSetResponseTypeDef" = (
        dataclasses.field()
    )

    ThreatIntelSetId = field("ThreatIntelSetId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateThreatIntelSetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateThreatIntelSetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTrustedEntitySetResponse:
    boto3_raw_data: "type_defs.CreateTrustedEntitySetResponseTypeDef" = (
        dataclasses.field()
    )

    TrustedEntitySetId = field("TrustedEntitySetId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateTrustedEntitySetResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTrustedEntitySetResponseTypeDef"]
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
class GetAdministratorAccountResponse:
    boto3_raw_data: "type_defs.GetAdministratorAccountResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Administrator(self):  # pragma: no cover
        return Administrator.make_one(self.boto3_raw_data["Administrator"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetAdministratorAccountResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAdministratorAccountResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCoverageStatisticsResponse:
    boto3_raw_data: "type_defs.GetCoverageStatisticsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CoverageStatistics(self):  # pragma: no cover
        return CoverageStatistics.make_one(self.boto3_raw_data["CoverageStatistics"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetCoverageStatisticsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCoverageStatisticsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIPSetResponse:
    boto3_raw_data: "type_defs.GetIPSetResponseTypeDef" = dataclasses.field()

    Name = field("Name")
    Format = field("Format")
    Location = field("Location")
    Status = field("Status")
    Tags = field("Tags")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetIPSetResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIPSetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInvitationsCountResponse:
    boto3_raw_data: "type_defs.GetInvitationsCountResponseTypeDef" = dataclasses.field()

    InvitationsCount = field("InvitationsCount")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetInvitationsCountResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInvitationsCountResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetThreatEntitySetResponse:
    boto3_raw_data: "type_defs.GetThreatEntitySetResponseTypeDef" = dataclasses.field()

    Name = field("Name")
    Format = field("Format")
    Location = field("Location")
    ExpectedBucketOwner = field("ExpectedBucketOwner")
    Status = field("Status")
    Tags = field("Tags")
    CreatedAt = field("CreatedAt")
    UpdatedAt = field("UpdatedAt")
    ErrorDetails = field("ErrorDetails")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetThreatEntitySetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetThreatEntitySetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetThreatIntelSetResponse:
    boto3_raw_data: "type_defs.GetThreatIntelSetResponseTypeDef" = dataclasses.field()

    Name = field("Name")
    Format = field("Format")
    Location = field("Location")
    Status = field("Status")
    Tags = field("Tags")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetThreatIntelSetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetThreatIntelSetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTrustedEntitySetResponse:
    boto3_raw_data: "type_defs.GetTrustedEntitySetResponseTypeDef" = dataclasses.field()

    Name = field("Name")
    Format = field("Format")
    Location = field("Location")
    ExpectedBucketOwner = field("ExpectedBucketOwner")
    Status = field("Status")
    Tags = field("Tags")
    CreatedAt = field("CreatedAt")
    UpdatedAt = field("UpdatedAt")
    ErrorDetails = field("ErrorDetails")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTrustedEntitySetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTrustedEntitySetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDetectorsResponse:
    boto3_raw_data: "type_defs.ListDetectorsResponseTypeDef" = dataclasses.field()

    DetectorIds = field("DetectorIds")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDetectorsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDetectorsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFiltersResponse:
    boto3_raw_data: "type_defs.ListFiltersResponseTypeDef" = dataclasses.field()

    FilterNames = field("FilterNames")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFiltersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFiltersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFindingsResponse:
    boto3_raw_data: "type_defs.ListFindingsResponseTypeDef" = dataclasses.field()

    FindingIds = field("FindingIds")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFindingsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFindingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIPSetsResponse:
    boto3_raw_data: "type_defs.ListIPSetsResponseTypeDef" = dataclasses.field()

    IpSetIds = field("IpSetIds")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIPSetsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIPSetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOrganizationAdminAccountsResponse:
    boto3_raw_data: "type_defs.ListOrganizationAdminAccountsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AdminAccounts(self):  # pragma: no cover
        return AdminAccount.make_many(self.boto3_raw_data["AdminAccounts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListOrganizationAdminAccountsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOrganizationAdminAccountsResponseTypeDef"]
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

    Tags = field("Tags")

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
class ListThreatEntitySetsResponse:
    boto3_raw_data: "type_defs.ListThreatEntitySetsResponseTypeDef" = (
        dataclasses.field()
    )

    ThreatEntitySetIds = field("ThreatEntitySetIds")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListThreatEntitySetsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListThreatEntitySetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListThreatIntelSetsResponse:
    boto3_raw_data: "type_defs.ListThreatIntelSetsResponseTypeDef" = dataclasses.field()

    ThreatIntelSetIds = field("ThreatIntelSetIds")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListThreatIntelSetsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListThreatIntelSetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTrustedEntitySetsResponse:
    boto3_raw_data: "type_defs.ListTrustedEntitySetsResponseTypeDef" = (
        dataclasses.field()
    )

    TrustedEntitySetIds = field("TrustedEntitySetIds")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListTrustedEntitySetsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTrustedEntitySetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartMalwareScanResponse:
    boto3_raw_data: "type_defs.StartMalwareScanResponseTypeDef" = dataclasses.field()

    ScanId = field("ScanId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartMalwareScanResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartMalwareScanResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFilterResponse:
    boto3_raw_data: "type_defs.UpdateFilterResponseTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFilterResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFilterResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMembersResponse:
    boto3_raw_data: "type_defs.CreateMembersResponseTypeDef" = dataclasses.field()

    @cached_property
    def UnprocessedAccounts(self):  # pragma: no cover
        return UnprocessedAccount.make_many(self.boto3_raw_data["UnprocessedAccounts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateMembersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMembersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeclineInvitationsResponse:
    boto3_raw_data: "type_defs.DeclineInvitationsResponseTypeDef" = dataclasses.field()

    @cached_property
    def UnprocessedAccounts(self):  # pragma: no cover
        return UnprocessedAccount.make_many(self.boto3_raw_data["UnprocessedAccounts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeclineInvitationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeclineInvitationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteInvitationsResponse:
    boto3_raw_data: "type_defs.DeleteInvitationsResponseTypeDef" = dataclasses.field()

    @cached_property
    def UnprocessedAccounts(self):  # pragma: no cover
        return UnprocessedAccount.make_many(self.boto3_raw_data["UnprocessedAccounts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteInvitationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteInvitationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMembersResponse:
    boto3_raw_data: "type_defs.DeleteMembersResponseTypeDef" = dataclasses.field()

    @cached_property
    def UnprocessedAccounts(self):  # pragma: no cover
        return UnprocessedAccount.make_many(self.boto3_raw_data["UnprocessedAccounts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteMembersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMembersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateMembersResponse:
    boto3_raw_data: "type_defs.DisassociateMembersResponseTypeDef" = dataclasses.field()

    @cached_property
    def UnprocessedAccounts(self):  # pragma: no cover
        return UnprocessedAccount.make_many(self.boto3_raw_data["UnprocessedAccounts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisassociateMembersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateMembersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InviteMembersResponse:
    boto3_raw_data: "type_defs.InviteMembersResponseTypeDef" = dataclasses.field()

    @cached_property
    def UnprocessedAccounts(self):  # pragma: no cover
        return UnprocessedAccount.make_many(self.boto3_raw_data["UnprocessedAccounts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InviteMembersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InviteMembersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartMonitoringMembersResponse:
    boto3_raw_data: "type_defs.StartMonitoringMembersResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def UnprocessedAccounts(self):  # pragma: no cover
        return UnprocessedAccount.make_many(self.boto3_raw_data["UnprocessedAccounts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartMonitoringMembersResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartMonitoringMembersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopMonitoringMembersResponse:
    boto3_raw_data: "type_defs.StopMonitoringMembersResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def UnprocessedAccounts(self):  # pragma: no cover
        return UnprocessedAccount.make_many(self.boto3_raw_data["UnprocessedAccounts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StopMonitoringMembersResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopMonitoringMembersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMemberDetectorsResponse:
    boto3_raw_data: "type_defs.UpdateMemberDetectorsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def UnprocessedAccounts(self):  # pragma: no cover
        return UnprocessedAccount.make_many(self.boto3_raw_data["UnprocessedAccounts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateMemberDetectorsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMemberDetectorsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateProtectedResourceOutput:
    boto3_raw_data: "type_defs.CreateProtectedResourceOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def S3Bucket(self):  # pragma: no cover
        return CreateS3BucketResourceOutput.make_one(self.boto3_raw_data["S3Bucket"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateProtectedResourceOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateProtectedResourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateProtectedResource:
    boto3_raw_data: "type_defs.CreateProtectedResourceTypeDef" = dataclasses.field()

    @cached_property
    def S3Bucket(self):  # pragma: no cover
        return CreateS3BucketResource.make_one(self.boto3_raw_data["S3Bucket"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateProtectedResourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateProtectedResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePublishingDestinationRequest:
    boto3_raw_data: "type_defs.CreatePublishingDestinationRequestTypeDef" = (
        dataclasses.field()
    )

    DetectorId = field("DetectorId")
    DestinationType = field("DestinationType")

    @cached_property
    def DestinationProperties(self):  # pragma: no cover
        return DestinationProperties.make_one(
            self.boto3_raw_data["DestinationProperties"]
        )

    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreatePublishingDestinationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePublishingDestinationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePublishingDestinationResponse:
    boto3_raw_data: "type_defs.DescribePublishingDestinationResponseTypeDef" = (
        dataclasses.field()
    )

    DestinationId = field("DestinationId")
    DestinationType = field("DestinationType")
    Status = field("Status")
    PublishingFailureStartTimestamp = field("PublishingFailureStartTimestamp")

    @cached_property
    def DestinationProperties(self):  # pragma: no cover
        return DestinationProperties.make_one(
            self.boto3_raw_data["DestinationProperties"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribePublishingDestinationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePublishingDestinationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePublishingDestinationRequest:
    boto3_raw_data: "type_defs.UpdatePublishingDestinationRequestTypeDef" = (
        dataclasses.field()
    )

    DetectorId = field("DetectorId")
    DestinationId = field("DestinationId")

    @cached_property
    def DestinationProperties(self):  # pragma: no cover
        return DestinationProperties.make_one(
            self.boto3_raw_data["DestinationProperties"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdatePublishingDestinationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePublishingDestinationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KubernetesDataSourceFreeTrial:
    boto3_raw_data: "type_defs.KubernetesDataSourceFreeTrialTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AuditLogs(self):  # pragma: no cover
        return DataSourceFreeTrial.make_one(self.boto3_raw_data["AuditLogs"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.KubernetesDataSourceFreeTrialTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KubernetesDataSourceFreeTrialTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MalwareProtectionDataSourceFreeTrial:
    boto3_raw_data: "type_defs.MalwareProtectionDataSourceFreeTrialTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ScanEc2InstanceWithFindings(self):  # pragma: no cover
        return DataSourceFreeTrial.make_one(
            self.boto3_raw_data["ScanEc2InstanceWithFindings"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MalwareProtectionDataSourceFreeTrialTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MalwareProtectionDataSourceFreeTrialTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDetectorsRequestPaginate:
    boto3_raw_data: "type_defs.ListDetectorsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDetectorsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDetectorsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFiltersRequestPaginate:
    boto3_raw_data: "type_defs.ListFiltersRequestPaginateTypeDef" = dataclasses.field()

    DetectorId = field("DetectorId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFiltersRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFiltersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIPSetsRequestPaginate:
    boto3_raw_data: "type_defs.ListIPSetsRequestPaginateTypeDef" = dataclasses.field()

    DetectorId = field("DetectorId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIPSetsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIPSetsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInvitationsRequestPaginate:
    boto3_raw_data: "type_defs.ListInvitationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListInvitationsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInvitationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMembersRequestPaginate:
    boto3_raw_data: "type_defs.ListMembersRequestPaginateTypeDef" = dataclasses.field()

    DetectorId = field("DetectorId")
    OnlyAssociated = field("OnlyAssociated")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMembersRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMembersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOrganizationAdminAccountsRequestPaginate:
    boto3_raw_data: "type_defs.ListOrganizationAdminAccountsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListOrganizationAdminAccountsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOrganizationAdminAccountsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListThreatEntitySetsRequestPaginate:
    boto3_raw_data: "type_defs.ListThreatEntitySetsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DetectorId = field("DetectorId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListThreatEntitySetsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListThreatEntitySetsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListThreatIntelSetsRequestPaginate:
    boto3_raw_data: "type_defs.ListThreatIntelSetsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DetectorId = field("DetectorId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListThreatIntelSetsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListThreatIntelSetsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTrustedEntitySetsRequestPaginate:
    boto3_raw_data: "type_defs.ListTrustedEntitySetsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DetectorId = field("DetectorId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTrustedEntitySetsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTrustedEntitySetsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFindingsRequest:
    boto3_raw_data: "type_defs.GetFindingsRequestTypeDef" = dataclasses.field()

    DetectorId = field("DetectorId")
    FindingIds = field("FindingIds")

    @cached_property
    def SortCriteria(self):  # pragma: no cover
        return SortCriteria.make_one(self.boto3_raw_data["SortCriteria"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFindingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFindingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPublishingDestinationsResponse:
    boto3_raw_data: "type_defs.ListPublishingDestinationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Destinations(self):  # pragma: no cover
        return Destination.make_many(self.boto3_raw_data["Destinations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPublishingDestinationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPublishingDestinationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectorFeatureConfigurationResult:
    boto3_raw_data: "type_defs.DetectorFeatureConfigurationResultTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Status = field("Status")
    UpdatedAt = field("UpdatedAt")

    @cached_property
    def AdditionalConfiguration(self):  # pragma: no cover
        return DetectorAdditionalConfigurationResult.make_many(
            self.boto3_raw_data["AdditionalConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DetectorFeatureConfigurationResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectorFeatureConfigurationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectorFeatureConfiguration:
    boto3_raw_data: "type_defs.DetectorFeatureConfigurationTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Status = field("Status")

    @cached_property
    def AdditionalConfiguration(self):  # pragma: no cover
        return DetectorAdditionalConfiguration.make_many(
            self.boto3_raw_data["AdditionalConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetectorFeatureConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectorFeatureConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EbsVolumeDetails:
    boto3_raw_data: "type_defs.EbsVolumeDetailsTypeDef" = dataclasses.field()

    @cached_property
    def ScannedVolumeDetails(self):  # pragma: no cover
        return VolumeDetail.make_many(self.boto3_raw_data["ScannedVolumeDetails"])

    @cached_property
    def SkippedVolumeDetails(self):  # pragma: no cover
        return VolumeDetail.make_many(self.boto3_raw_data["SkippedVolumeDetails"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EbsVolumeDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EbsVolumeDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScanEc2InstanceWithFindingsResult:
    boto3_raw_data: "type_defs.ScanEc2InstanceWithFindingsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EbsVolumes(self):  # pragma: no cover
        return EbsVolumesResult.make_one(self.boto3_raw_data["EbsVolumes"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ScanEc2InstanceWithFindingsResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScanEc2InstanceWithFindingsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Ec2Instance:
    boto3_raw_data: "type_defs.Ec2InstanceTypeDef" = dataclasses.field()

    AvailabilityZone = field("AvailabilityZone")
    ImageDescription = field("ImageDescription")
    InstanceState = field("InstanceState")

    @cached_property
    def IamInstanceProfile(self):  # pragma: no cover
        return IamInstanceProfile.make_one(self.boto3_raw_data["IamInstanceProfile"])

    InstanceType = field("InstanceType")
    OutpostArn = field("OutpostArn")
    Platform = field("Platform")

    @cached_property
    def ProductCodes(self):  # pragma: no cover
        return ProductCode.make_many(self.boto3_raw_data["ProductCodes"])

    Ec2NetworkInterfaceUids = field("Ec2NetworkInterfaceUids")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.Ec2InstanceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.Ec2InstanceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Ec2NetworkInterface:
    boto3_raw_data: "type_defs.Ec2NetworkInterfaceTypeDef" = dataclasses.field()

    Ipv6Addresses = field("Ipv6Addresses")

    @cached_property
    def PrivateIpAddresses(self):  # pragma: no cover
        return PrivateIpAddressDetails.make_many(
            self.boto3_raw_data["PrivateIpAddresses"]
        )

    PublicIp = field("PublicIp")

    @cached_property
    def SecurityGroups(self):  # pragma: no cover
        return SecurityGroup.make_many(self.boto3_raw_data["SecurityGroups"])

    SubNetId = field("SubNetId")
    VpcId = field("VpcId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.Ec2NetworkInterfaceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Ec2NetworkInterfaceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkInterface:
    boto3_raw_data: "type_defs.NetworkInterfaceTypeDef" = dataclasses.field()

    Ipv6Addresses = field("Ipv6Addresses")
    NetworkInterfaceId = field("NetworkInterfaceId")
    PrivateDnsName = field("PrivateDnsName")
    PrivateIpAddress = field("PrivateIpAddress")

    @cached_property
    def PrivateIpAddresses(self):  # pragma: no cover
        return PrivateIpAddressDetails.make_many(
            self.boto3_raw_data["PrivateIpAddresses"]
        )

    PublicDnsName = field("PublicDnsName")
    PublicIp = field("PublicIp")

    @cached_property
    def SecurityGroups(self):  # pragma: no cover
        return SecurityGroup.make_many(self.boto3_raw_data["SecurityGroups"])

    SubnetId = field("SubnetId")
    VpcId = field("VpcId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NetworkInterfaceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkInterfaceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcConfig:
    boto3_raw_data: "type_defs.VpcConfigTypeDef" = dataclasses.field()

    SubnetIds = field("SubnetIds")
    VpcId = field("VpcId")

    @cached_property
    def SecurityGroups(self):  # pragma: no cover
        return SecurityGroup.make_many(self.boto3_raw_data["SecurityGroups"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VpcConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VpcConfigTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EksClusterDetails:
    boto3_raw_data: "type_defs.EksClusterDetailsTypeDef" = dataclasses.field()

    Name = field("Name")
    Arn = field("Arn")
    VpcId = field("VpcId")
    Status = field("Status")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    CreatedAt = field("CreatedAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EksClusterDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EksClusterDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RdsDbInstanceDetails:
    boto3_raw_data: "type_defs.RdsDbInstanceDetailsTypeDef" = dataclasses.field()

    DbInstanceIdentifier = field("DbInstanceIdentifier")
    Engine = field("Engine")
    EngineVersion = field("EngineVersion")
    DbClusterIdentifier = field("DbClusterIdentifier")
    DbInstanceArn = field("DbInstanceArn")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RdsDbInstanceDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RdsDbInstanceDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RdsLimitlessDbDetails:
    boto3_raw_data: "type_defs.RdsLimitlessDbDetailsTypeDef" = dataclasses.field()

    DbShardGroupIdentifier = field("DbShardGroupIdentifier")
    DbShardGroupResourceId = field("DbShardGroupResourceId")
    DbShardGroupArn = field("DbShardGroupArn")
    Engine = field("Engine")
    EngineVersion = field("EngineVersion")
    DbClusterIdentifier = field("DbClusterIdentifier")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RdsLimitlessDbDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RdsLimitlessDbDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Evidence:
    boto3_raw_data: "type_defs.EvidenceTypeDef" = dataclasses.field()

    @cached_property
    def ThreatIntelligenceDetails(self):  # pragma: no cover
        return ThreatIntelligenceDetail.make_many(
            self.boto3_raw_data["ThreatIntelligenceDetails"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EvidenceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EvidenceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FilterCriterion:
    boto3_raw_data: "type_defs.FilterCriterionTypeDef" = dataclasses.field()

    CriterionKey = field("CriterionKey")

    @cached_property
    def FilterCondition(self):  # pragma: no cover
        return FilterCondition.make_one(self.boto3_raw_data["FilterCondition"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FilterCriterionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FilterCriterionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FindingStatistics:
    boto3_raw_data: "type_defs.FindingStatisticsTypeDef" = dataclasses.field()

    CountBySeverity = field("CountBySeverity")

    @cached_property
    def GroupedByAccount(self):  # pragma: no cover
        return AccountStatistics.make_many(self.boto3_raw_data["GroupedByAccount"])

    @cached_property
    def GroupedByDate(self):  # pragma: no cover
        return DateStatistics.make_many(self.boto3_raw_data["GroupedByDate"])

    @cached_property
    def GroupedByFindingType(self):  # pragma: no cover
        return FindingTypeStatistics.make_many(
            self.boto3_raw_data["GroupedByFindingType"]
        )

    @cached_property
    def GroupedByResource(self):  # pragma: no cover
        return ResourceStatistics.make_many(self.boto3_raw_data["GroupedByResource"])

    @cached_property
    def GroupedBySeverity(self):  # pragma: no cover
        return SeverityStatistics.make_many(self.boto3_raw_data["GroupedBySeverity"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FindingStatisticsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FindingStatisticsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMasterAccountResponse:
    boto3_raw_data: "type_defs.GetMasterAccountResponseTypeDef" = dataclasses.field()

    @cached_property
    def Master(self):  # pragma: no cover
        return Master.make_one(self.boto3_raw_data["Master"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMasterAccountResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMasterAccountResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMembersResponse:
    boto3_raw_data: "type_defs.GetMembersResponseTypeDef" = dataclasses.field()

    @cached_property
    def Members(self):  # pragma: no cover
        return Member.make_many(self.boto3_raw_data["Members"])

    @cached_property
    def UnprocessedAccounts(self):  # pragma: no cover
        return UnprocessedAccount.make_many(self.boto3_raw_data["UnprocessedAccounts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMembersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMembersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMembersResponse:
    boto3_raw_data: "type_defs.ListMembersResponseTypeDef" = dataclasses.field()

    @cached_property
    def Members(self):  # pragma: no cover
        return Member.make_many(self.boto3_raw_data["Members"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMembersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMembersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUsageStatisticsRequest:
    boto3_raw_data: "type_defs.GetUsageStatisticsRequestTypeDef" = dataclasses.field()

    DetectorId = field("DetectorId")
    UsageStatisticType = field("UsageStatisticType")

    @cached_property
    def UsageCriteria(self):  # pragma: no cover
        return UsageCriteria.make_one(self.boto3_raw_data["UsageCriteria"])

    Unit = field("Unit")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetUsageStatisticsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetUsageStatisticsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Volume:
    boto3_raw_data: "type_defs.VolumeTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def HostPath(self):  # pragma: no cover
        return HostPath.make_one(self.boto3_raw_data["HostPath"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VolumeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VolumeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KubernetesUserDetails:
    boto3_raw_data: "type_defs.KubernetesUserDetailsTypeDef" = dataclasses.field()

    Username = field("Username")
    Uid = field("Uid")
    Groups = field("Groups")
    SessionName = field("SessionName")

    @cached_property
    def ImpersonatedUser(self):  # pragma: no cover
        return ImpersonatedUser.make_one(self.boto3_raw_data["ImpersonatedUser"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KubernetesUserDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KubernetesUserDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Signal:
    boto3_raw_data: "type_defs.SignalTypeDef" = dataclasses.field()

    Uid = field("Uid")
    Type = field("Type")
    Name = field("Name")
    CreatedAt = field("CreatedAt")
    UpdatedAt = field("UpdatedAt")
    FirstSeenAt = field("FirstSeenAt")
    LastSeenAt = field("LastSeenAt")
    Count = field("Count")
    Description = field("Description")
    Severity = field("Severity")
    ResourceUids = field("ResourceUids")
    ActorIds = field("ActorIds")
    EndpointIds = field("EndpointIds")

    @cached_property
    def SignalIndicators(self):  # pragma: no cover
        return Indicator.make_many(self.boto3_raw_data["SignalIndicators"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SignalTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SignalTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInvitationsResponse:
    boto3_raw_data: "type_defs.ListInvitationsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Invitations(self):  # pragma: no cover
        return Invitation.make_many(self.boto3_raw_data["Invitations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInvitationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInvitationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Threat:
    boto3_raw_data: "type_defs.ThreatTypeDef" = dataclasses.field()

    Name = field("Name")
    Source = field("Source")

    @cached_property
    def ItemPaths(self):  # pragma: no cover
        return ItemPath.make_many(self.boto3_raw_data["ItemPaths"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ThreatTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ThreatTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KubernetesConfigurationResult:
    boto3_raw_data: "type_defs.KubernetesConfigurationResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AuditLogs(self):  # pragma: no cover
        return KubernetesAuditLogsConfigurationResult.make_one(
            self.boto3_raw_data["AuditLogs"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.KubernetesConfigurationResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KubernetesConfigurationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KubernetesConfiguration:
    boto3_raw_data: "type_defs.KubernetesConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def AuditLogs(self):  # pragma: no cover
        return KubernetesAuditLogsConfiguration.make_one(
            self.boto3_raw_data["AuditLogs"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KubernetesConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KubernetesConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProcessDetails:
    boto3_raw_data: "type_defs.ProcessDetailsTypeDef" = dataclasses.field()

    Name = field("Name")
    ExecutablePath = field("ExecutablePath")
    ExecutableSha256 = field("ExecutableSha256")
    NamespacePid = field("NamespacePid")
    Pwd = field("Pwd")
    Pid = field("Pid")
    StartTime = field("StartTime")
    Uuid = field("Uuid")
    ParentUuid = field("ParentUuid")
    User = field("User")
    UserId = field("UserId")
    Euid = field("Euid")

    @cached_property
    def Lineage(self):  # pragma: no cover
        return LineageObject.make_many(self.boto3_raw_data["Lineage"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProcessDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProcessDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMalwareProtectionPlansResponse:
    boto3_raw_data: "type_defs.ListMalwareProtectionPlansResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MalwareProtectionPlans(self):  # pragma: no cover
        return MalwareProtectionPlanSummary.make_many(
            self.boto3_raw_data["MalwareProtectionPlans"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListMalwareProtectionPlansResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMalwareProtectionPlansResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MalwareProtectionConfiguration:
    boto3_raw_data: "type_defs.MalwareProtectionConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ScanEc2InstanceWithFindings(self):  # pragma: no cover
        return ScanEc2InstanceWithFindings.make_one(
            self.boto3_raw_data["ScanEc2InstanceWithFindings"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.MalwareProtectionConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MalwareProtectionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MalwareProtectionPlanActions:
    boto3_raw_data: "type_defs.MalwareProtectionPlanActionsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Tagging(self):  # pragma: no cover
        return MalwareProtectionPlanTaggingAction.make_one(
            self.boto3_raw_data["Tagging"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MalwareProtectionPlanActionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MalwareProtectionPlanActionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MemberFeaturesConfigurationResult:
    boto3_raw_data: "type_defs.MemberFeaturesConfigurationResultTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Status = field("Status")
    UpdatedAt = field("UpdatedAt")

    @cached_property
    def AdditionalConfiguration(self):  # pragma: no cover
        return MemberAdditionalConfigurationResult.make_many(
            self.boto3_raw_data["AdditionalConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MemberFeaturesConfigurationResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MemberFeaturesConfigurationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MemberFeaturesConfiguration:
    boto3_raw_data: "type_defs.MemberFeaturesConfigurationTypeDef" = dataclasses.field()

    Name = field("Name")
    Status = field("Status")

    @cached_property
    def AdditionalConfiguration(self):  # pragma: no cover
        return MemberAdditionalConfiguration.make_many(
            self.boto3_raw_data["AdditionalConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MemberFeaturesConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MemberFeaturesConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkEndpoint:
    boto3_raw_data: "type_defs.NetworkEndpointTypeDef" = dataclasses.field()

    Id = field("Id")
    Ip = field("Ip")
    Domain = field("Domain")
    Port = field("Port")

    @cached_property
    def Location(self):  # pragma: no cover
        return NetworkGeoLocation.make_one(self.boto3_raw_data["Location"])

    @cached_property
    def AutonomousSystem(self):  # pragma: no cover
        return AutonomousSystem.make_one(self.boto3_raw_data["AutonomousSystem"])

    @cached_property
    def Connection(self):  # pragma: no cover
        return NetworkConnection.make_one(self.boto3_raw_data["Connection"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NetworkEndpointTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NetworkEndpointTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrganizationFeatureConfigurationResult:
    boto3_raw_data: "type_defs.OrganizationFeatureConfigurationResultTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    AutoEnable = field("AutoEnable")

    @cached_property
    def AdditionalConfiguration(self):  # pragma: no cover
        return OrganizationAdditionalConfigurationResult.make_many(
            self.boto3_raw_data["AdditionalConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OrganizationFeatureConfigurationResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrganizationFeatureConfigurationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrganizationFeatureConfiguration:
    boto3_raw_data: "type_defs.OrganizationFeatureConfigurationTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    AutoEnable = field("AutoEnable")

    @cached_property
    def AdditionalConfiguration(self):  # pragma: no cover
        return OrganizationAdditionalConfiguration.make_many(
            self.boto3_raw_data["AdditionalConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.OrganizationFeatureConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrganizationFeatureConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrganizationScanEc2InstanceWithFindingsResult:
    boto3_raw_data: "type_defs.OrganizationScanEc2InstanceWithFindingsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EbsVolumes(self):  # pragma: no cover
        return OrganizationEbsVolumesResult.make_one(self.boto3_raw_data["EbsVolumes"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OrganizationScanEc2InstanceWithFindingsResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrganizationScanEc2InstanceWithFindingsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrganizationScanEc2InstanceWithFindings:
    boto3_raw_data: "type_defs.OrganizationScanEc2InstanceWithFindingsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EbsVolumes(self):  # pragma: no cover
        return OrganizationEbsVolumes.make_one(self.boto3_raw_data["EbsVolumes"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OrganizationScanEc2InstanceWithFindingsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrganizationScanEc2InstanceWithFindingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrganizationFeatureStatistics:
    boto3_raw_data: "type_defs.OrganizationFeatureStatisticsTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    EnabledAccountsCount = field("EnabledAccountsCount")

    @cached_property
    def AdditionalConfiguration(self):  # pragma: no cover
        return OrganizationFeatureStatisticsAdditionalConfiguration.make_many(
            self.boto3_raw_data["AdditionalConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.OrganizationFeatureStatisticsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrganizationFeatureStatisticsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrganizationKubernetesConfigurationResult:
    boto3_raw_data: "type_defs.OrganizationKubernetesConfigurationResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AuditLogs(self):  # pragma: no cover
        return OrganizationKubernetesAuditLogsConfigurationResult.make_one(
            self.boto3_raw_data["AuditLogs"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OrganizationKubernetesConfigurationResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrganizationKubernetesConfigurationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrganizationKubernetesConfiguration:
    boto3_raw_data: "type_defs.OrganizationKubernetesConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AuditLogs(self):  # pragma: no cover
        return OrganizationKubernetesAuditLogsConfiguration.make_one(
            self.boto3_raw_data["AuditLogs"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OrganizationKubernetesConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrganizationKubernetesConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoteIpDetails:
    boto3_raw_data: "type_defs.RemoteIpDetailsTypeDef" = dataclasses.field()

    @cached_property
    def City(self):  # pragma: no cover
        return City.make_one(self.boto3_raw_data["City"])

    @cached_property
    def Country(self):  # pragma: no cover
        return Country.make_one(self.boto3_raw_data["Country"])

    @cached_property
    def GeoLocation(self):  # pragma: no cover
        return GeoLocation.make_one(self.boto3_raw_data["GeoLocation"])

    IpAddressV4 = field("IpAddressV4")
    IpAddressV6 = field("IpAddressV6")

    @cached_property
    def Organization(self):  # pragma: no cover
        return Organization.make_one(self.boto3_raw_data["Organization"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RemoteIpDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RemoteIpDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Bucket:
    boto3_raw_data: "type_defs.S3BucketTypeDef" = dataclasses.field()

    OwnerId = field("OwnerId")
    CreatedAt = field("CreatedAt")
    EncryptionType = field("EncryptionType")
    EncryptionKeyArn = field("EncryptionKeyArn")
    EffectivePermission = field("EffectivePermission")
    PublicReadAccess = field("PublicReadAccess")
    PublicWriteAccess = field("PublicWriteAccess")

    @cached_property
    def AccountPublicAccess(self):  # pragma: no cover
        return PublicAccessConfiguration.make_one(
            self.boto3_raw_data["AccountPublicAccess"]
        )

    @cached_property
    def BucketPublicAccess(self):  # pragma: no cover
        return PublicAccessConfiguration.make_one(
            self.boto3_raw_data["BucketPublicAccess"]
        )

    S3ObjectUids = field("S3ObjectUids")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3BucketTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3BucketTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScanConditionOutput:
    boto3_raw_data: "type_defs.ScanConditionOutputTypeDef" = dataclasses.field()

    @cached_property
    def MapEquals(self):  # pragma: no cover
        return ScanConditionPair.make_many(self.boto3_raw_data["MapEquals"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScanConditionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScanConditionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScanCondition:
    boto3_raw_data: "type_defs.ScanConditionTypeDef" = dataclasses.field()

    @cached_property
    def MapEquals(self):  # pragma: no cover
        return ScanConditionPair.make_many(self.boto3_raw_data["MapEquals"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScanConditionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScanConditionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScanThreatName:
    boto3_raw_data: "type_defs.ScanThreatNameTypeDef" = dataclasses.field()

    Name = field("Name")
    Severity = field("Severity")
    ItemCount = field("ItemCount")

    @cached_property
    def FilePaths(self):  # pragma: no cover
        return ScanFilePath.make_many(self.boto3_raw_data["FilePaths"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScanThreatNameTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScanThreatNameTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Scan:
    boto3_raw_data: "type_defs.ScanTypeDef" = dataclasses.field()

    DetectorId = field("DetectorId")
    AdminDetectorId = field("AdminDetectorId")
    ScanId = field("ScanId")
    ScanStatus = field("ScanStatus")
    FailureReason = field("FailureReason")
    ScanStartTime = field("ScanStartTime")
    ScanEndTime = field("ScanEndTime")

    @cached_property
    def TriggerDetails(self):  # pragma: no cover
        return TriggerDetails.make_one(self.boto3_raw_data["TriggerDetails"])

    @cached_property
    def ResourceDetails(self):  # pragma: no cover
        return ResourceDetails.make_one(self.boto3_raw_data["ResourceDetails"])

    @cached_property
    def ScanResultDetails(self):  # pragma: no cover
        return ScanResultDetails.make_one(self.boto3_raw_data["ScanResultDetails"])

    AccountId = field("AccountId")
    TotalBytes = field("TotalBytes")
    FileCount = field("FileCount")

    @cached_property
    def AttachedVolumes(self):  # pragma: no cover
        return VolumeDetail.make_many(self.boto3_raw_data["AttachedVolumes"])

    ScanType = field("ScanType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScanTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScanTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UsageAccountResult:
    boto3_raw_data: "type_defs.UsageAccountResultTypeDef" = dataclasses.field()

    AccountId = field("AccountId")

    @cached_property
    def Total(self):  # pragma: no cover
        return Total.make_one(self.boto3_raw_data["Total"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UsageAccountResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UsageAccountResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UsageDataSourceResult:
    boto3_raw_data: "type_defs.UsageDataSourceResultTypeDef" = dataclasses.field()

    DataSource = field("DataSource")

    @cached_property
    def Total(self):  # pragma: no cover
        return Total.make_one(self.boto3_raw_data["Total"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UsageDataSourceResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UsageDataSourceResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UsageFeatureResult:
    boto3_raw_data: "type_defs.UsageFeatureResultTypeDef" = dataclasses.field()

    Feature = field("Feature")

    @cached_property
    def Total(self):  # pragma: no cover
        return Total.make_one(self.boto3_raw_data["Total"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UsageFeatureResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UsageFeatureResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UsageResourceResult:
    boto3_raw_data: "type_defs.UsageResourceResultTypeDef" = dataclasses.field()

    Resource = field("Resource")

    @cached_property
    def Total(self):  # pragma: no cover
        return Total.make_one(self.boto3_raw_data["Total"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UsageResourceResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UsageResourceResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UsageTopAccountResult:
    boto3_raw_data: "type_defs.UsageTopAccountResultTypeDef" = dataclasses.field()

    AccountId = field("AccountId")

    @cached_property
    def Total(self):  # pragma: no cover
        return Total.make_one(self.boto3_raw_data["Total"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UsageTopAccountResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UsageTopAccountResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateProtectedResource:
    boto3_raw_data: "type_defs.UpdateProtectedResourceTypeDef" = dataclasses.field()

    @cached_property
    def S3Bucket(self):  # pragma: no cover
        return UpdateS3BucketResource.make_one(self.boto3_raw_data["S3Bucket"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateProtectedResourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateProtectedResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Actor:
    boto3_raw_data: "type_defs.ActorTypeDef" = dataclasses.field()

    Id = field("Id")

    @cached_property
    def User(self):  # pragma: no cover
        return User.make_one(self.boto3_raw_data["User"])

    @cached_property
    def Session(self):  # pragma: no cover
        return Session.make_one(self.boto3_raw_data["Session"])

    @cached_property
    def Process(self):  # pragma: no cover
        return ActorProcess.make_one(self.boto3_raw_data["Process"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ActorTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnomalyUnusual:
    boto3_raw_data: "type_defs.AnomalyUnusualTypeDef" = dataclasses.field()

    Behavior = field("Behavior")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AnomalyUnusualTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AnomalyUnusualTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PermissionConfiguration:
    boto3_raw_data: "type_defs.PermissionConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def BucketLevelPermissions(self):  # pragma: no cover
        return BucketLevelPermissions.make_one(
            self.boto3_raw_data["BucketLevelPermissions"]
        )

    @cached_property
    def AccountLevelPermissions(self):  # pragma: no cover
        return AccountLevelPermissions.make_one(
            self.boto3_raw_data["AccountLevelPermissions"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PermissionConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PermissionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFilterResponse:
    boto3_raw_data: "type_defs.GetFilterResponseTypeDef" = dataclasses.field()

    Name = field("Name")
    Description = field("Description")
    Action = field("Action")
    Rank = field("Rank")

    @cached_property
    def FindingCriteria(self):  # pragma: no cover
        return FindingCriteriaOutput.make_one(self.boto3_raw_data["FindingCriteria"])

    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetFilterResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFilterResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CoverageResourceDetails:
    boto3_raw_data: "type_defs.CoverageResourceDetailsTypeDef" = dataclasses.field()

    @cached_property
    def EksClusterDetails(self):  # pragma: no cover
        return CoverageEksClusterDetails.make_one(
            self.boto3_raw_data["EksClusterDetails"]
        )

    ResourceType = field("ResourceType")

    @cached_property
    def EcsClusterDetails(self):  # pragma: no cover
        return CoverageEcsClusterDetails.make_one(
            self.boto3_raw_data["EcsClusterDetails"]
        )

    @cached_property
    def Ec2InstanceDetails(self):  # pragma: no cover
        return CoverageEc2InstanceDetails.make_one(
            self.boto3_raw_data["Ec2InstanceDetails"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CoverageResourceDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CoverageResourceDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CoverageFilterCriteria:
    boto3_raw_data: "type_defs.CoverageFilterCriteriaTypeDef" = dataclasses.field()

    @cached_property
    def FilterCriterion(self):  # pragma: no cover
        return CoverageFilterCriterion.make_many(self.boto3_raw_data["FilterCriterion"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CoverageFilterCriteriaTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CoverageFilterCriteriaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSourcesFreeTrial:
    boto3_raw_data: "type_defs.DataSourcesFreeTrialTypeDef" = dataclasses.field()

    @cached_property
    def CloudTrail(self):  # pragma: no cover
        return DataSourceFreeTrial.make_one(self.boto3_raw_data["CloudTrail"])

    @cached_property
    def DnsLogs(self):  # pragma: no cover
        return DataSourceFreeTrial.make_one(self.boto3_raw_data["DnsLogs"])

    @cached_property
    def FlowLogs(self):  # pragma: no cover
        return DataSourceFreeTrial.make_one(self.boto3_raw_data["FlowLogs"])

    @cached_property
    def S3Logs(self):  # pragma: no cover
        return DataSourceFreeTrial.make_one(self.boto3_raw_data["S3Logs"])

    @cached_property
    def Kubernetes(self):  # pragma: no cover
        return KubernetesDataSourceFreeTrial.make_one(self.boto3_raw_data["Kubernetes"])

    @cached_property
    def MalwareProtection(self):  # pragma: no cover
        return MalwareProtectionDataSourceFreeTrial.make_one(
            self.boto3_raw_data["MalwareProtection"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataSourcesFreeTrialTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataSourcesFreeTrialTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MalwareProtectionConfigurationResult:
    boto3_raw_data: "type_defs.MalwareProtectionConfigurationResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ScanEc2InstanceWithFindings(self):  # pragma: no cover
        return ScanEc2InstanceWithFindingsResult.make_one(
            self.boto3_raw_data["ScanEc2InstanceWithFindings"]
        )

    ServiceRole = field("ServiceRole")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MalwareProtectionConfigurationResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MalwareProtectionConfigurationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceDetails:
    boto3_raw_data: "type_defs.InstanceDetailsTypeDef" = dataclasses.field()

    AvailabilityZone = field("AvailabilityZone")

    @cached_property
    def IamInstanceProfile(self):  # pragma: no cover
        return IamInstanceProfile.make_one(self.boto3_raw_data["IamInstanceProfile"])

    ImageDescription = field("ImageDescription")
    ImageId = field("ImageId")
    InstanceId = field("InstanceId")
    InstanceState = field("InstanceState")
    InstanceType = field("InstanceType")
    OutpostArn = field("OutpostArn")
    LaunchTime = field("LaunchTime")

    @cached_property
    def NetworkInterfaces(self):  # pragma: no cover
        return NetworkInterface.make_many(self.boto3_raw_data["NetworkInterfaces"])

    Platform = field("Platform")

    @cached_property
    def ProductCodes(self):  # pragma: no cover
        return ProductCode.make_many(self.boto3_raw_data["ProductCodes"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InstanceDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InstanceDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaDetails:
    boto3_raw_data: "type_defs.LambdaDetailsTypeDef" = dataclasses.field()

    FunctionArn = field("FunctionArn")
    FunctionName = field("FunctionName")
    Description = field("Description")
    LastModifiedAt = field("LastModifiedAt")
    RevisionId = field("RevisionId")
    FunctionVersion = field("FunctionVersion")
    Role = field("Role")

    @cached_property
    def VpcConfig(self):  # pragma: no cover
        return VpcConfig.make_one(self.boto3_raw_data["VpcConfig"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LambdaDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LambdaDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FilterCriteria:
    boto3_raw_data: "type_defs.FilterCriteriaTypeDef" = dataclasses.field()

    @cached_property
    def FilterCriterion(self):  # pragma: no cover
        return FilterCriterion.make_many(self.boto3_raw_data["FilterCriterion"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FilterCriteriaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FilterCriteriaTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFindingsStatisticsResponse:
    boto3_raw_data: "type_defs.GetFindingsStatisticsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FindingStatistics(self):  # pragma: no cover
        return FindingStatistics.make_one(self.boto3_raw_data["FindingStatistics"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetFindingsStatisticsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFindingsStatisticsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EcsTaskDetails:
    boto3_raw_data: "type_defs.EcsTaskDetailsTypeDef" = dataclasses.field()

    Arn = field("Arn")
    DefinitionArn = field("DefinitionArn")
    Version = field("Version")
    TaskCreatedAt = field("TaskCreatedAt")
    StartedAt = field("StartedAt")
    StartedBy = field("StartedBy")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def Volumes(self):  # pragma: no cover
        return Volume.make_many(self.boto3_raw_data["Volumes"])

    @cached_property
    def Containers(self):  # pragma: no cover
        return Container.make_many(self.boto3_raw_data["Containers"])

    Group = field("Group")
    LaunchType = field("LaunchType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EcsTaskDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EcsTaskDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KubernetesWorkloadDetails:
    boto3_raw_data: "type_defs.KubernetesWorkloadDetailsTypeDef" = dataclasses.field()

    Name = field("Name")
    Type = field("Type")
    Uid = field("Uid")
    Namespace = field("Namespace")
    HostNetwork = field("HostNetwork")

    @cached_property
    def Containers(self):  # pragma: no cover
        return Container.make_many(self.boto3_raw_data["Containers"])

    @cached_property
    def Volumes(self):  # pragma: no cover
        return Volume.make_many(self.boto3_raw_data["Volumes"])

    ServiceAccountName = field("ServiceAccountName")
    HostIPC = field("HostIPC")
    HostPID = field("HostPID")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KubernetesWorkloadDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KubernetesWorkloadDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MalwareScanDetails:
    boto3_raw_data: "type_defs.MalwareScanDetailsTypeDef" = dataclasses.field()

    @cached_property
    def Threats(self):  # pragma: no cover
        return Threat.make_many(self.boto3_raw_data["Threats"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MalwareScanDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MalwareScanDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuntimeContext:
    boto3_raw_data: "type_defs.RuntimeContextTypeDef" = dataclasses.field()

    @cached_property
    def ModifyingProcess(self):  # pragma: no cover
        return ProcessDetails.make_one(self.boto3_raw_data["ModifyingProcess"])

    ModifiedAt = field("ModifiedAt")
    ScriptPath = field("ScriptPath")
    LibraryPath = field("LibraryPath")
    LdPreloadValue = field("LdPreloadValue")
    SocketPath = field("SocketPath")
    RuncBinaryPath = field("RuncBinaryPath")
    ReleaseAgentPath = field("ReleaseAgentPath")
    MountSource = field("MountSource")
    MountTarget = field("MountTarget")
    FileSystemType = field("FileSystemType")
    Flags = field("Flags")
    ModuleName = field("ModuleName")
    ModuleFilePath = field("ModuleFilePath")
    ModuleSha256 = field("ModuleSha256")
    ShellHistoryFilePath = field("ShellHistoryFilePath")

    @cached_property
    def TargetProcess(self):  # pragma: no cover
        return ProcessDetails.make_one(self.boto3_raw_data["TargetProcess"])

    AddressFamily = field("AddressFamily")
    IanaProtocolNumber = field("IanaProtocolNumber")
    MemoryRegions = field("MemoryRegions")
    ToolName = field("ToolName")
    ToolCategory = field("ToolCategory")
    ServiceName = field("ServiceName")
    CommandLineExample = field("CommandLineExample")
    ThreatFilePath = field("ThreatFilePath")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuntimeContextTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuntimeContextTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSourceConfigurations:
    boto3_raw_data: "type_defs.DataSourceConfigurationsTypeDef" = dataclasses.field()

    @cached_property
    def S3Logs(self):  # pragma: no cover
        return S3LogsConfiguration.make_one(self.boto3_raw_data["S3Logs"])

    @cached_property
    def Kubernetes(self):  # pragma: no cover
        return KubernetesConfiguration.make_one(self.boto3_raw_data["Kubernetes"])

    @cached_property
    def MalwareProtection(self):  # pragma: no cover
        return MalwareProtectionConfiguration.make_one(
            self.boto3_raw_data["MalwareProtection"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataSourceConfigurationsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataSourceConfigurationsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMalwareProtectionPlanResponse:
    boto3_raw_data: "type_defs.GetMalwareProtectionPlanResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    Role = field("Role")

    @cached_property
    def ProtectedResource(self):  # pragma: no cover
        return CreateProtectedResourceOutput.make_one(
            self.boto3_raw_data["ProtectedResource"]
        )

    @cached_property
    def Actions(self):  # pragma: no cover
        return MalwareProtectionPlanActions.make_one(self.boto3_raw_data["Actions"])

    CreatedAt = field("CreatedAt")
    Status = field("Status")

    @cached_property
    def StatusReasons(self):  # pragma: no cover
        return MalwareProtectionPlanStatusReason.make_many(
            self.boto3_raw_data["StatusReasons"]
        )

    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetMalwareProtectionPlanResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMalwareProtectionPlanResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrganizationMalwareProtectionConfigurationResult:
    boto3_raw_data: (
        "type_defs.OrganizationMalwareProtectionConfigurationResultTypeDef"
    ) = dataclasses.field()

    @cached_property
    def ScanEc2InstanceWithFindings(self):  # pragma: no cover
        return OrganizationScanEc2InstanceWithFindingsResult.make_one(
            self.boto3_raw_data["ScanEc2InstanceWithFindings"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OrganizationMalwareProtectionConfigurationResultTypeDef"
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
                "type_defs.OrganizationMalwareProtectionConfigurationResultTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrganizationMalwareProtectionConfiguration:
    boto3_raw_data: "type_defs.OrganizationMalwareProtectionConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ScanEc2InstanceWithFindings(self):  # pragma: no cover
        return OrganizationScanEc2InstanceWithFindings.make_one(
            self.boto3_raw_data["ScanEc2InstanceWithFindings"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OrganizationMalwareProtectionConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrganizationMalwareProtectionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrganizationStatistics:
    boto3_raw_data: "type_defs.OrganizationStatisticsTypeDef" = dataclasses.field()

    TotalAccountsCount = field("TotalAccountsCount")
    MemberAccountsCount = field("MemberAccountsCount")
    ActiveAccountsCount = field("ActiveAccountsCount")
    EnabledAccountsCount = field("EnabledAccountsCount")

    @cached_property
    def CountByFeature(self):  # pragma: no cover
        return OrganizationFeatureStatistics.make_many(
            self.boto3_raw_data["CountByFeature"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OrganizationStatisticsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrganizationStatisticsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AwsApiCallAction:
    boto3_raw_data: "type_defs.AwsApiCallActionTypeDef" = dataclasses.field()

    Api = field("Api")
    CallerType = field("CallerType")

    @cached_property
    def DomainDetails(self):  # pragma: no cover
        return DomainDetails.make_one(self.boto3_raw_data["DomainDetails"])

    ErrorCode = field("ErrorCode")
    UserAgent = field("UserAgent")

    @cached_property
    def RemoteIpDetails(self):  # pragma: no cover
        return RemoteIpDetails.make_one(self.boto3_raw_data["RemoteIpDetails"])

    ServiceName = field("ServiceName")

    @cached_property
    def RemoteAccountDetails(self):  # pragma: no cover
        return RemoteAccountDetails.make_one(
            self.boto3_raw_data["RemoteAccountDetails"]
        )

    AffectedResources = field("AffectedResources")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AwsApiCallActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AwsApiCallActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KubernetesApiCallAction:
    boto3_raw_data: "type_defs.KubernetesApiCallActionTypeDef" = dataclasses.field()

    RequestUri = field("RequestUri")
    Verb = field("Verb")
    SourceIps = field("SourceIps")
    UserAgent = field("UserAgent")

    @cached_property
    def RemoteIpDetails(self):  # pragma: no cover
        return RemoteIpDetails.make_one(self.boto3_raw_data["RemoteIpDetails"])

    StatusCode = field("StatusCode")
    Parameters = field("Parameters")
    Resource = field("Resource")
    Subresource = field("Subresource")
    Namespace = field("Namespace")
    ResourceName = field("ResourceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KubernetesApiCallActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KubernetesApiCallActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkConnectionAction:
    boto3_raw_data: "type_defs.NetworkConnectionActionTypeDef" = dataclasses.field()

    Blocked = field("Blocked")
    ConnectionDirection = field("ConnectionDirection")

    @cached_property
    def LocalPortDetails(self):  # pragma: no cover
        return LocalPortDetails.make_one(self.boto3_raw_data["LocalPortDetails"])

    Protocol = field("Protocol")

    @cached_property
    def LocalIpDetails(self):  # pragma: no cover
        return LocalIpDetails.make_one(self.boto3_raw_data["LocalIpDetails"])

    LocalNetworkInterface = field("LocalNetworkInterface")

    @cached_property
    def RemoteIpDetails(self):  # pragma: no cover
        return RemoteIpDetails.make_one(self.boto3_raw_data["RemoteIpDetails"])

    @cached_property
    def RemotePortDetails(self):  # pragma: no cover
        return RemotePortDetails.make_one(self.boto3_raw_data["RemotePortDetails"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NetworkConnectionActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkConnectionActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PortProbeDetail:
    boto3_raw_data: "type_defs.PortProbeDetailTypeDef" = dataclasses.field()

    @cached_property
    def LocalPortDetails(self):  # pragma: no cover
        return LocalPortDetails.make_one(self.boto3_raw_data["LocalPortDetails"])

    @cached_property
    def LocalIpDetails(self):  # pragma: no cover
        return LocalIpDetails.make_one(self.boto3_raw_data["LocalIpDetails"])

    @cached_property
    def RemoteIpDetails(self):  # pragma: no cover
        return RemoteIpDetails.make_one(self.boto3_raw_data["RemoteIpDetails"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PortProbeDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PortProbeDetailTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RdsLoginAttemptAction:
    boto3_raw_data: "type_defs.RdsLoginAttemptActionTypeDef" = dataclasses.field()

    @cached_property
    def RemoteIpDetails(self):  # pragma: no cover
        return RemoteIpDetails.make_one(self.boto3_raw_data["RemoteIpDetails"])

    @cached_property
    def LoginAttributes(self):  # pragma: no cover
        return LoginAttribute.make_many(self.boto3_raw_data["LoginAttributes"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RdsLoginAttemptActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RdsLoginAttemptActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceData:
    boto3_raw_data: "type_defs.ResourceDataTypeDef" = dataclasses.field()

    @cached_property
    def S3Bucket(self):  # pragma: no cover
        return S3Bucket.make_one(self.boto3_raw_data["S3Bucket"])

    @cached_property
    def Ec2Instance(self):  # pragma: no cover
        return Ec2Instance.make_one(self.boto3_raw_data["Ec2Instance"])

    @cached_property
    def AccessKey(self):  # pragma: no cover
        return AccessKey.make_one(self.boto3_raw_data["AccessKey"])

    @cached_property
    def Ec2NetworkInterface(self):  # pragma: no cover
        return Ec2NetworkInterface.make_one(self.boto3_raw_data["Ec2NetworkInterface"])

    @cached_property
    def S3Object(self):  # pragma: no cover
        return S3Object.make_one(self.boto3_raw_data["S3Object"])

    @cached_property
    def EksCluster(self):  # pragma: no cover
        return EksCluster.make_one(self.boto3_raw_data["EksCluster"])

    @cached_property
    def KubernetesWorkload(self):  # pragma: no cover
        return KubernetesWorkload.make_one(self.boto3_raw_data["KubernetesWorkload"])

    @cached_property
    def Container(self):  # pragma: no cover
        return ContainerFindingResource.make_one(self.boto3_raw_data["Container"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceDataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScanResourceCriteriaOutput:
    boto3_raw_data: "type_defs.ScanResourceCriteriaOutputTypeDef" = dataclasses.field()

    Include = field("Include")
    Exclude = field("Exclude")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScanResourceCriteriaOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScanResourceCriteriaOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScanResourceCriteria:
    boto3_raw_data: "type_defs.ScanResourceCriteriaTypeDef" = dataclasses.field()

    Include = field("Include")
    Exclude = field("Exclude")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScanResourceCriteriaTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScanResourceCriteriaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ThreatDetectedByName:
    boto3_raw_data: "type_defs.ThreatDetectedByNameTypeDef" = dataclasses.field()

    ItemCount = field("ItemCount")
    UniqueThreatNameCount = field("UniqueThreatNameCount")
    Shortened = field("Shortened")

    @cached_property
    def ThreatNames(self):  # pragma: no cover
        return ScanThreatName.make_many(self.boto3_raw_data["ThreatNames"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ThreatDetectedByNameTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ThreatDetectedByNameTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMalwareScansResponse:
    boto3_raw_data: "type_defs.DescribeMalwareScansResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Scans(self):  # pragma: no cover
        return Scan.make_many(self.boto3_raw_data["Scans"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeMalwareScansResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMalwareScansResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UsageTopAccountsResult:
    boto3_raw_data: "type_defs.UsageTopAccountsResultTypeDef" = dataclasses.field()

    Feature = field("Feature")

    @cached_property
    def Accounts(self):  # pragma: no cover
        return UsageTopAccountResult.make_many(self.boto3_raw_data["Accounts"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UsageTopAccountsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UsageTopAccountsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMalwareProtectionPlanRequest:
    boto3_raw_data: "type_defs.UpdateMalwareProtectionPlanRequestTypeDef" = (
        dataclasses.field()
    )

    MalwareProtectionPlanId = field("MalwareProtectionPlanId")
    Role = field("Role")

    @cached_property
    def Actions(self):  # pragma: no cover
        return MalwareProtectionPlanActions.make_one(self.boto3_raw_data["Actions"])

    @cached_property
    def ProtectedResource(self):  # pragma: no cover
        return UpdateProtectedResource.make_one(
            self.boto3_raw_data["ProtectedResource"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateMalwareProtectionPlanRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMalwareProtectionPlanRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Anomaly:
    boto3_raw_data: "type_defs.AnomalyTypeDef" = dataclasses.field()

    Profiles = field("Profiles")

    @cached_property
    def Unusual(self):  # pragma: no cover
        return AnomalyUnusual.make_one(self.boto3_raw_data["Unusual"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AnomalyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AnomalyTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PublicAccess:
    boto3_raw_data: "type_defs.PublicAccessTypeDef" = dataclasses.field()

    @cached_property
    def PermissionConfiguration(self):  # pragma: no cover
        return PermissionConfiguration.make_one(
            self.boto3_raw_data["PermissionConfiguration"]
        )

    EffectivePermission = field("EffectivePermission")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PublicAccessTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PublicAccessTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFilterRequest:
    boto3_raw_data: "type_defs.CreateFilterRequestTypeDef" = dataclasses.field()

    DetectorId = field("DetectorId")
    Name = field("Name")
    FindingCriteria = field("FindingCriteria")
    Description = field("Description")
    Action = field("Action")
    Rank = field("Rank")
    ClientToken = field("ClientToken")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFilterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFilterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFindingsStatisticsRequest:
    boto3_raw_data: "type_defs.GetFindingsStatisticsRequestTypeDef" = (
        dataclasses.field()
    )

    DetectorId = field("DetectorId")
    FindingStatisticTypes = field("FindingStatisticTypes")
    FindingCriteria = field("FindingCriteria")
    GroupBy = field("GroupBy")
    OrderBy = field("OrderBy")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFindingsStatisticsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFindingsStatisticsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFindingsRequestPaginate:
    boto3_raw_data: "type_defs.ListFindingsRequestPaginateTypeDef" = dataclasses.field()

    DetectorId = field("DetectorId")
    FindingCriteria = field("FindingCriteria")

    @cached_property
    def SortCriteria(self):  # pragma: no cover
        return SortCriteria.make_one(self.boto3_raw_data["SortCriteria"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFindingsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFindingsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFindingsRequest:
    boto3_raw_data: "type_defs.ListFindingsRequestTypeDef" = dataclasses.field()

    DetectorId = field("DetectorId")
    FindingCriteria = field("FindingCriteria")

    @cached_property
    def SortCriteria(self):  # pragma: no cover
        return SortCriteria.make_one(self.boto3_raw_data["SortCriteria"])

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFindingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFindingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFilterRequest:
    boto3_raw_data: "type_defs.UpdateFilterRequestTypeDef" = dataclasses.field()

    DetectorId = field("DetectorId")
    FilterName = field("FilterName")
    Description = field("Description")
    Action = field("Action")
    Rank = field("Rank")
    FindingCriteria = field("FindingCriteria")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFilterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFilterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CoverageResource:
    boto3_raw_data: "type_defs.CoverageResourceTypeDef" = dataclasses.field()

    ResourceId = field("ResourceId")
    DetectorId = field("DetectorId")
    AccountId = field("AccountId")

    @cached_property
    def ResourceDetails(self):  # pragma: no cover
        return CoverageResourceDetails.make_one(self.boto3_raw_data["ResourceDetails"])

    CoverageStatus = field("CoverageStatus")
    Issue = field("Issue")
    UpdatedAt = field("UpdatedAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CoverageResourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CoverageResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCoverageStatisticsRequest:
    boto3_raw_data: "type_defs.GetCoverageStatisticsRequestTypeDef" = (
        dataclasses.field()
    )

    DetectorId = field("DetectorId")
    StatisticsType = field("StatisticsType")

    @cached_property
    def FilterCriteria(self):  # pragma: no cover
        return CoverageFilterCriteria.make_one(self.boto3_raw_data["FilterCriteria"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCoverageStatisticsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCoverageStatisticsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCoverageRequestPaginate:
    boto3_raw_data: "type_defs.ListCoverageRequestPaginateTypeDef" = dataclasses.field()

    DetectorId = field("DetectorId")

    @cached_property
    def FilterCriteria(self):  # pragma: no cover
        return CoverageFilterCriteria.make_one(self.boto3_raw_data["FilterCriteria"])

    @cached_property
    def SortCriteria(self):  # pragma: no cover
        return CoverageSortCriteria.make_one(self.boto3_raw_data["SortCriteria"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCoverageRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCoverageRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCoverageRequest:
    boto3_raw_data: "type_defs.ListCoverageRequestTypeDef" = dataclasses.field()

    DetectorId = field("DetectorId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @cached_property
    def FilterCriteria(self):  # pragma: no cover
        return CoverageFilterCriteria.make_one(self.boto3_raw_data["FilterCriteria"])

    @cached_property
    def SortCriteria(self):  # pragma: no cover
        return CoverageSortCriteria.make_one(self.boto3_raw_data["SortCriteria"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCoverageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCoverageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMalwareProtectionPlanRequest:
    boto3_raw_data: "type_defs.CreateMalwareProtectionPlanRequestTypeDef" = (
        dataclasses.field()
    )

    Role = field("Role")
    ProtectedResource = field("ProtectedResource")
    ClientToken = field("ClientToken")

    @cached_property
    def Actions(self):  # pragma: no cover
        return MalwareProtectionPlanActions.make_one(self.boto3_raw_data["Actions"])

    Tags = field("Tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateMalwareProtectionPlanRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMalwareProtectionPlanRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccountFreeTrialInfo:
    boto3_raw_data: "type_defs.AccountFreeTrialInfoTypeDef" = dataclasses.field()

    AccountId = field("AccountId")

    @cached_property
    def DataSources(self):  # pragma: no cover
        return DataSourcesFreeTrial.make_one(self.boto3_raw_data["DataSources"])

    @cached_property
    def Features(self):  # pragma: no cover
        return FreeTrialFeatureConfigurationResult.make_many(
            self.boto3_raw_data["Features"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AccountFreeTrialInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccountFreeTrialInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSourceConfigurationsResult:
    boto3_raw_data: "type_defs.DataSourceConfigurationsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CloudTrail(self):  # pragma: no cover
        return CloudTrailConfigurationResult.make_one(self.boto3_raw_data["CloudTrail"])

    @cached_property
    def DNSLogs(self):  # pragma: no cover
        return DNSLogsConfigurationResult.make_one(self.boto3_raw_data["DNSLogs"])

    @cached_property
    def FlowLogs(self):  # pragma: no cover
        return FlowLogsConfigurationResult.make_one(self.boto3_raw_data["FlowLogs"])

    @cached_property
    def S3Logs(self):  # pragma: no cover
        return S3LogsConfigurationResult.make_one(self.boto3_raw_data["S3Logs"])

    @cached_property
    def Kubernetes(self):  # pragma: no cover
        return KubernetesConfigurationResult.make_one(self.boto3_raw_data["Kubernetes"])

    @cached_property
    def MalwareProtection(self):  # pragma: no cover
        return MalwareProtectionConfigurationResult.make_one(
            self.boto3_raw_data["MalwareProtection"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DataSourceConfigurationsResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataSourceConfigurationsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UnprocessedDataSourcesResult:
    boto3_raw_data: "type_defs.UnprocessedDataSourcesResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MalwareProtection(self):  # pragma: no cover
        return MalwareProtectionConfigurationResult.make_one(
            self.boto3_raw_data["MalwareProtection"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UnprocessedDataSourcesResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UnprocessedDataSourcesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMalwareScansRequestPaginate:
    boto3_raw_data: "type_defs.DescribeMalwareScansRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DetectorId = field("DetectorId")

    @cached_property
    def FilterCriteria(self):  # pragma: no cover
        return FilterCriteria.make_one(self.boto3_raw_data["FilterCriteria"])

    @cached_property
    def SortCriteria(self):  # pragma: no cover
        return SortCriteria.make_one(self.boto3_raw_data["SortCriteria"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMalwareScansRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMalwareScansRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMalwareScansRequest:
    boto3_raw_data: "type_defs.DescribeMalwareScansRequestTypeDef" = dataclasses.field()

    DetectorId = field("DetectorId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @cached_property
    def FilterCriteria(self):  # pragma: no cover
        return FilterCriteria.make_one(self.boto3_raw_data["FilterCriteria"])

    @cached_property
    def SortCriteria(self):  # pragma: no cover
        return SortCriteria.make_one(self.boto3_raw_data["SortCriteria"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeMalwareScansRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMalwareScansRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EcsClusterDetails:
    boto3_raw_data: "type_defs.EcsClusterDetailsTypeDef" = dataclasses.field()

    Name = field("Name")
    Arn = field("Arn")
    Status = field("Status")
    ActiveServicesCount = field("ActiveServicesCount")
    RegisteredContainerInstancesCount = field("RegisteredContainerInstancesCount")
    RunningTasksCount = field("RunningTasksCount")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def TaskDetails(self):  # pragma: no cover
        return EcsTaskDetails.make_one(self.boto3_raw_data["TaskDetails"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EcsClusterDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EcsClusterDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KubernetesDetails:
    boto3_raw_data: "type_defs.KubernetesDetailsTypeDef" = dataclasses.field()

    @cached_property
    def KubernetesUserDetails(self):  # pragma: no cover
        return KubernetesUserDetails.make_one(
            self.boto3_raw_data["KubernetesUserDetails"]
        )

    @cached_property
    def KubernetesWorkloadDetails(self):  # pragma: no cover
        return KubernetesWorkloadDetails.make_one(
            self.boto3_raw_data["KubernetesWorkloadDetails"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KubernetesDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KubernetesDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuntimeDetails:
    boto3_raw_data: "type_defs.RuntimeDetailsTypeDef" = dataclasses.field()

    @cached_property
    def Process(self):  # pragma: no cover
        return ProcessDetails.make_one(self.boto3_raw_data["Process"])

    @cached_property
    def Context(self):  # pragma: no cover
        return RuntimeContext.make_one(self.boto3_raw_data["Context"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuntimeDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuntimeDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDetectorRequest:
    boto3_raw_data: "type_defs.CreateDetectorRequestTypeDef" = dataclasses.field()

    Enable = field("Enable")
    ClientToken = field("ClientToken")
    FindingPublishingFrequency = field("FindingPublishingFrequency")

    @cached_property
    def DataSources(self):  # pragma: no cover
        return DataSourceConfigurations.make_one(self.boto3_raw_data["DataSources"])

    Tags = field("Tags")

    @cached_property
    def Features(self):  # pragma: no cover
        return DetectorFeatureConfiguration.make_many(self.boto3_raw_data["Features"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDetectorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDetectorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDetectorRequest:
    boto3_raw_data: "type_defs.UpdateDetectorRequestTypeDef" = dataclasses.field()

    DetectorId = field("DetectorId")
    Enable = field("Enable")
    FindingPublishingFrequency = field("FindingPublishingFrequency")

    @cached_property
    def DataSources(self):  # pragma: no cover
        return DataSourceConfigurations.make_one(self.boto3_raw_data["DataSources"])

    @cached_property
    def Features(self):  # pragma: no cover
        return DetectorFeatureConfiguration.make_many(self.boto3_raw_data["Features"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDetectorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDetectorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMemberDetectorsRequest:
    boto3_raw_data: "type_defs.UpdateMemberDetectorsRequestTypeDef" = (
        dataclasses.field()
    )

    DetectorId = field("DetectorId")
    AccountIds = field("AccountIds")

    @cached_property
    def DataSources(self):  # pragma: no cover
        return DataSourceConfigurations.make_one(self.boto3_raw_data["DataSources"])

    @cached_property
    def Features(self):  # pragma: no cover
        return MemberFeaturesConfiguration.make_many(self.boto3_raw_data["Features"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateMemberDetectorsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMemberDetectorsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrganizationDataSourceConfigurationsResult:
    boto3_raw_data: "type_defs.OrganizationDataSourceConfigurationsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def S3Logs(self):  # pragma: no cover
        return OrganizationS3LogsConfigurationResult.make_one(
            self.boto3_raw_data["S3Logs"]
        )

    @cached_property
    def Kubernetes(self):  # pragma: no cover
        return OrganizationKubernetesConfigurationResult.make_one(
            self.boto3_raw_data["Kubernetes"]
        )

    @cached_property
    def MalwareProtection(self):  # pragma: no cover
        return OrganizationMalwareProtectionConfigurationResult.make_one(
            self.boto3_raw_data["MalwareProtection"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OrganizationDataSourceConfigurationsResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrganizationDataSourceConfigurationsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrganizationDataSourceConfigurations:
    boto3_raw_data: "type_defs.OrganizationDataSourceConfigurationsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def S3Logs(self):  # pragma: no cover
        return OrganizationS3LogsConfiguration.make_one(self.boto3_raw_data["S3Logs"])

    @cached_property
    def Kubernetes(self):  # pragma: no cover
        return OrganizationKubernetesConfiguration.make_one(
            self.boto3_raw_data["Kubernetes"]
        )

    @cached_property
    def MalwareProtection(self):  # pragma: no cover
        return OrganizationMalwareProtectionConfiguration.make_one(
            self.boto3_raw_data["MalwareProtection"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OrganizationDataSourceConfigurationsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrganizationDataSourceConfigurationsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrganizationDetails:
    boto3_raw_data: "type_defs.OrganizationDetailsTypeDef" = dataclasses.field()

    UpdatedAt = field("UpdatedAt")

    @cached_property
    def OrganizationStatistics(self):  # pragma: no cover
        return OrganizationStatistics.make_one(
            self.boto3_raw_data["OrganizationStatistics"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OrganizationDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrganizationDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PortProbeAction:
    boto3_raw_data: "type_defs.PortProbeActionTypeDef" = dataclasses.field()

    Blocked = field("Blocked")

    @cached_property
    def PortProbeDetails(self):  # pragma: no cover
        return PortProbeDetail.make_many(self.boto3_raw_data["PortProbeDetails"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PortProbeActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PortProbeActionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceV2:
    boto3_raw_data: "type_defs.ResourceV2TypeDef" = dataclasses.field()

    Uid = field("Uid")
    ResourceType = field("ResourceType")
    Name = field("Name")
    AccountId = field("AccountId")
    Region = field("Region")
    Service = field("Service")
    CloudPartition = field("CloudPartition")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def Data(self):  # pragma: no cover
        return ResourceData.make_one(self.boto3_raw_data["Data"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceV2TypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceV2TypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMalwareScanSettingsResponse:
    boto3_raw_data: "type_defs.GetMalwareScanSettingsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ScanResourceCriteria(self):  # pragma: no cover
        return ScanResourceCriteriaOutput.make_one(
            self.boto3_raw_data["ScanResourceCriteria"]
        )

    EbsSnapshotPreservation = field("EbsSnapshotPreservation")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetMalwareScanSettingsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMalwareScanSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScanDetections:
    boto3_raw_data: "type_defs.ScanDetectionsTypeDef" = dataclasses.field()

    @cached_property
    def ScannedItemCount(self):  # pragma: no cover
        return ScannedItemCount.make_one(self.boto3_raw_data["ScannedItemCount"])

    @cached_property
    def ThreatsDetectedItemCount(self):  # pragma: no cover
        return ThreatsDetectedItemCount.make_one(
            self.boto3_raw_data["ThreatsDetectedItemCount"]
        )

    @cached_property
    def HighestSeverityThreatDetails(self):  # pragma: no cover
        return HighestSeverityThreatDetails.make_one(
            self.boto3_raw_data["HighestSeverityThreatDetails"]
        )

    @cached_property
    def ThreatDetectedByName(self):  # pragma: no cover
        return ThreatDetectedByName.make_one(
            self.boto3_raw_data["ThreatDetectedByName"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScanDetectionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScanDetectionsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UsageStatistics:
    boto3_raw_data: "type_defs.UsageStatisticsTypeDef" = dataclasses.field()

    @cached_property
    def SumByAccount(self):  # pragma: no cover
        return UsageAccountResult.make_many(self.boto3_raw_data["SumByAccount"])

    @cached_property
    def TopAccountsByFeature(self):  # pragma: no cover
        return UsageTopAccountsResult.make_many(
            self.boto3_raw_data["TopAccountsByFeature"]
        )

    @cached_property
    def SumByDataSource(self):  # pragma: no cover
        return UsageDataSourceResult.make_many(self.boto3_raw_data["SumByDataSource"])

    @cached_property
    def SumByResource(self):  # pragma: no cover
        return UsageResourceResult.make_many(self.boto3_raw_data["SumByResource"])

    @cached_property
    def TopResources(self):  # pragma: no cover
        return UsageResourceResult.make_many(self.boto3_raw_data["TopResources"])

    @cached_property
    def SumByFeature(self):  # pragma: no cover
        return UsageFeatureResult.make_many(self.boto3_raw_data["SumByFeature"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UsageStatisticsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UsageStatisticsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3BucketDetail:
    boto3_raw_data: "type_defs.S3BucketDetailTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Name = field("Name")
    Type = field("Type")
    CreatedAt = field("CreatedAt")

    @cached_property
    def Owner(self):  # pragma: no cover
        return Owner.make_one(self.boto3_raw_data["Owner"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def DefaultServerSideEncryption(self):  # pragma: no cover
        return DefaultServerSideEncryption.make_one(
            self.boto3_raw_data["DefaultServerSideEncryption"]
        )

    @cached_property
    def PublicAccess(self):  # pragma: no cover
        return PublicAccess.make_one(self.boto3_raw_data["PublicAccess"])

    @cached_property
    def S3ObjectDetails(self):  # pragma: no cover
        return S3ObjectDetail.make_many(self.boto3_raw_data["S3ObjectDetails"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3BucketDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3BucketDetailTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCoverageResponse:
    boto3_raw_data: "type_defs.ListCoverageResponseTypeDef" = dataclasses.field()

    @cached_property
    def Resources(self):  # pragma: no cover
        return CoverageResource.make_many(self.boto3_raw_data["Resources"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCoverageResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCoverageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRemainingFreeTrialDaysResponse:
    boto3_raw_data: "type_defs.GetRemainingFreeTrialDaysResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Accounts(self):  # pragma: no cover
        return AccountFreeTrialInfo.make_many(self.boto3_raw_data["Accounts"])

    @cached_property
    def UnprocessedAccounts(self):  # pragma: no cover
        return UnprocessedAccount.make_many(self.boto3_raw_data["UnprocessedAccounts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRemainingFreeTrialDaysResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRemainingFreeTrialDaysResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDetectorResponse:
    boto3_raw_data: "type_defs.GetDetectorResponseTypeDef" = dataclasses.field()

    CreatedAt = field("CreatedAt")
    FindingPublishingFrequency = field("FindingPublishingFrequency")
    ServiceRole = field("ServiceRole")
    Status = field("Status")
    UpdatedAt = field("UpdatedAt")

    @cached_property
    def DataSources(self):  # pragma: no cover
        return DataSourceConfigurationsResult.make_one(
            self.boto3_raw_data["DataSources"]
        )

    Tags = field("Tags")

    @cached_property
    def Features(self):  # pragma: no cover
        return DetectorFeatureConfigurationResult.make_many(
            self.boto3_raw_data["Features"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDetectorResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDetectorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MemberDataSourceConfiguration:
    boto3_raw_data: "type_defs.MemberDataSourceConfigurationTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")

    @cached_property
    def DataSources(self):  # pragma: no cover
        return DataSourceConfigurationsResult.make_one(
            self.boto3_raw_data["DataSources"]
        )

    @cached_property
    def Features(self):  # pragma: no cover
        return MemberFeaturesConfigurationResult.make_many(
            self.boto3_raw_data["Features"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.MemberDataSourceConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MemberDataSourceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDetectorResponse:
    boto3_raw_data: "type_defs.CreateDetectorResponseTypeDef" = dataclasses.field()

    DetectorId = field("DetectorId")

    @cached_property
    def UnprocessedDataSources(self):  # pragma: no cover
        return UnprocessedDataSourcesResult.make_one(
            self.boto3_raw_data["UnprocessedDataSources"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDetectorResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDetectorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOrganizationConfigurationResponse:
    boto3_raw_data: "type_defs.DescribeOrganizationConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    AutoEnable = field("AutoEnable")
    MemberAccountLimitReached = field("MemberAccountLimitReached")

    @cached_property
    def DataSources(self):  # pragma: no cover
        return OrganizationDataSourceConfigurationsResult.make_one(
            self.boto3_raw_data["DataSources"]
        )

    @cached_property
    def Features(self):  # pragma: no cover
        return OrganizationFeatureConfigurationResult.make_many(
            self.boto3_raw_data["Features"]
        )

    AutoEnableOrganizationMembers = field("AutoEnableOrganizationMembers")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeOrganizationConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeOrganizationConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateOrganizationConfigurationRequest:
    boto3_raw_data: "type_defs.UpdateOrganizationConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    DetectorId = field("DetectorId")
    AutoEnable = field("AutoEnable")

    @cached_property
    def DataSources(self):  # pragma: no cover
        return OrganizationDataSourceConfigurations.make_one(
            self.boto3_raw_data["DataSources"]
        )

    @cached_property
    def Features(self):  # pragma: no cover
        return OrganizationFeatureConfiguration.make_many(
            self.boto3_raw_data["Features"]
        )

    AutoEnableOrganizationMembers = field("AutoEnableOrganizationMembers")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateOrganizationConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateOrganizationConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOrganizationStatisticsResponse:
    boto3_raw_data: "type_defs.GetOrganizationStatisticsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def OrganizationDetails(self):  # pragma: no cover
        return OrganizationDetails.make_one(self.boto3_raw_data["OrganizationDetails"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetOrganizationStatisticsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOrganizationStatisticsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Action:
    boto3_raw_data: "type_defs.ActionTypeDef" = dataclasses.field()

    ActionType = field("ActionType")

    @cached_property
    def AwsApiCallAction(self):  # pragma: no cover
        return AwsApiCallAction.make_one(self.boto3_raw_data["AwsApiCallAction"])

    @cached_property
    def DnsRequestAction(self):  # pragma: no cover
        return DnsRequestAction.make_one(self.boto3_raw_data["DnsRequestAction"])

    @cached_property
    def NetworkConnectionAction(self):  # pragma: no cover
        return NetworkConnectionAction.make_one(
            self.boto3_raw_data["NetworkConnectionAction"]
        )

    @cached_property
    def PortProbeAction(self):  # pragma: no cover
        return PortProbeAction.make_one(self.boto3_raw_data["PortProbeAction"])

    @cached_property
    def KubernetesApiCallAction(self):  # pragma: no cover
        return KubernetesApiCallAction.make_one(
            self.boto3_raw_data["KubernetesApiCallAction"]
        )

    @cached_property
    def RdsLoginAttemptAction(self):  # pragma: no cover
        return RdsLoginAttemptAction.make_one(
            self.boto3_raw_data["RdsLoginAttemptAction"]
        )

    @cached_property
    def KubernetesPermissionCheckedDetails(self):  # pragma: no cover
        return KubernetesPermissionCheckedDetails.make_one(
            self.boto3_raw_data["KubernetesPermissionCheckedDetails"]
        )

    @cached_property
    def KubernetesRoleBindingDetails(self):  # pragma: no cover
        return KubernetesRoleBindingDetails.make_one(
            self.boto3_raw_data["KubernetesRoleBindingDetails"]
        )

    @cached_property
    def KubernetesRoleDetails(self):  # pragma: no cover
        return KubernetesRoleDetails.make_one(
            self.boto3_raw_data["KubernetesRoleDetails"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ActionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Sequence:
    boto3_raw_data: "type_defs.SequenceTypeDef" = dataclasses.field()

    Uid = field("Uid")
    Description = field("Description")

    @cached_property
    def Signals(self):  # pragma: no cover
        return Signal.make_many(self.boto3_raw_data["Signals"])

    @cached_property
    def Actors(self):  # pragma: no cover
        return Actor.make_many(self.boto3_raw_data["Actors"])

    @cached_property
    def Resources(self):  # pragma: no cover
        return ResourceV2.make_many(self.boto3_raw_data["Resources"])

    @cached_property
    def Endpoints(self):  # pragma: no cover
        return NetworkEndpoint.make_many(self.boto3_raw_data["Endpoints"])

    @cached_property
    def SequenceIndicators(self):  # pragma: no cover
        return Indicator.make_many(self.boto3_raw_data["SequenceIndicators"])

    AdditionalSequenceTypes = field("AdditionalSequenceTypes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SequenceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SequenceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMalwareScanSettingsRequest:
    boto3_raw_data: "type_defs.UpdateMalwareScanSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    DetectorId = field("DetectorId")
    ScanResourceCriteria = field("ScanResourceCriteria")
    EbsSnapshotPreservation = field("EbsSnapshotPreservation")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateMalwareScanSettingsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMalwareScanSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EbsVolumeScanDetails:
    boto3_raw_data: "type_defs.EbsVolumeScanDetailsTypeDef" = dataclasses.field()

    ScanId = field("ScanId")
    ScanStartedAt = field("ScanStartedAt")
    ScanCompletedAt = field("ScanCompletedAt")
    TriggerFindingId = field("TriggerFindingId")
    Sources = field("Sources")

    @cached_property
    def ScanDetections(self):  # pragma: no cover
        return ScanDetections.make_one(self.boto3_raw_data["ScanDetections"])

    ScanType = field("ScanType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EbsVolumeScanDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EbsVolumeScanDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUsageStatisticsResponse:
    boto3_raw_data: "type_defs.GetUsageStatisticsResponseTypeDef" = dataclasses.field()

    @cached_property
    def UsageStatistics(self):  # pragma: no cover
        return UsageStatistics.make_one(self.boto3_raw_data["UsageStatistics"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetUsageStatisticsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetUsageStatisticsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Resource:
    boto3_raw_data: "type_defs.ResourceTypeDef" = dataclasses.field()

    @cached_property
    def AccessKeyDetails(self):  # pragma: no cover
        return AccessKeyDetails.make_one(self.boto3_raw_data["AccessKeyDetails"])

    @cached_property
    def S3BucketDetails(self):  # pragma: no cover
        return S3BucketDetail.make_many(self.boto3_raw_data["S3BucketDetails"])

    @cached_property
    def InstanceDetails(self):  # pragma: no cover
        return InstanceDetails.make_one(self.boto3_raw_data["InstanceDetails"])

    @cached_property
    def EksClusterDetails(self):  # pragma: no cover
        return EksClusterDetails.make_one(self.boto3_raw_data["EksClusterDetails"])

    @cached_property
    def KubernetesDetails(self):  # pragma: no cover
        return KubernetesDetails.make_one(self.boto3_raw_data["KubernetesDetails"])

    ResourceType = field("ResourceType")

    @cached_property
    def EbsVolumeDetails(self):  # pragma: no cover
        return EbsVolumeDetails.make_one(self.boto3_raw_data["EbsVolumeDetails"])

    @cached_property
    def EcsClusterDetails(self):  # pragma: no cover
        return EcsClusterDetails.make_one(self.boto3_raw_data["EcsClusterDetails"])

    @cached_property
    def ContainerDetails(self):  # pragma: no cover
        return Container.make_one(self.boto3_raw_data["ContainerDetails"])

    @cached_property
    def RdsDbInstanceDetails(self):  # pragma: no cover
        return RdsDbInstanceDetails.make_one(
            self.boto3_raw_data["RdsDbInstanceDetails"]
        )

    @cached_property
    def RdsLimitlessDbDetails(self):  # pragma: no cover
        return RdsLimitlessDbDetails.make_one(
            self.boto3_raw_data["RdsLimitlessDbDetails"]
        )

    @cached_property
    def RdsDbUserDetails(self):  # pragma: no cover
        return RdsDbUserDetails.make_one(self.boto3_raw_data["RdsDbUserDetails"])

    @cached_property
    def LambdaDetails(self):  # pragma: no cover
        return LambdaDetails.make_one(self.boto3_raw_data["LambdaDetails"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMemberDetectorsResponse:
    boto3_raw_data: "type_defs.GetMemberDetectorsResponseTypeDef" = dataclasses.field()

    @cached_property
    def MemberDataSourceConfigurations(self):  # pragma: no cover
        return MemberDataSourceConfiguration.make_many(
            self.boto3_raw_data["MemberDataSourceConfigurations"]
        )

    @cached_property
    def UnprocessedAccounts(self):  # pragma: no cover
        return UnprocessedAccount.make_many(self.boto3_raw_data["UnprocessedAccounts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMemberDetectorsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMemberDetectorsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Detection:
    boto3_raw_data: "type_defs.DetectionTypeDef" = dataclasses.field()

    @cached_property
    def Anomaly(self):  # pragma: no cover
        return Anomaly.make_one(self.boto3_raw_data["Anomaly"])

    @cached_property
    def Sequence(self):  # pragma: no cover
        return Sequence.make_one(self.boto3_raw_data["Sequence"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DetectionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DetectionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Service:
    boto3_raw_data: "type_defs.ServiceTypeDef" = dataclasses.field()

    @cached_property
    def Action(self):  # pragma: no cover
        return Action.make_one(self.boto3_raw_data["Action"])

    @cached_property
    def Evidence(self):  # pragma: no cover
        return Evidence.make_one(self.boto3_raw_data["Evidence"])

    Archived = field("Archived")
    Count = field("Count")
    DetectorId = field("DetectorId")
    EventFirstSeen = field("EventFirstSeen")
    EventLastSeen = field("EventLastSeen")
    ResourceRole = field("ResourceRole")
    ServiceName = field("ServiceName")
    UserFeedback = field("UserFeedback")

    @cached_property
    def AdditionalInfo(self):  # pragma: no cover
        return ServiceAdditionalInfo.make_one(self.boto3_raw_data["AdditionalInfo"])

    FeatureName = field("FeatureName")

    @cached_property
    def EbsVolumeScanDetails(self):  # pragma: no cover
        return EbsVolumeScanDetails.make_one(
            self.boto3_raw_data["EbsVolumeScanDetails"]
        )

    @cached_property
    def RuntimeDetails(self):  # pragma: no cover
        return RuntimeDetails.make_one(self.boto3_raw_data["RuntimeDetails"])

    @cached_property
    def Detection(self):  # pragma: no cover
        return Detection.make_one(self.boto3_raw_data["Detection"])

    @cached_property
    def MalwareScanDetails(self):  # pragma: no cover
        return MalwareScanDetails.make_one(self.boto3_raw_data["MalwareScanDetails"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServiceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ServiceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Finding:
    boto3_raw_data: "type_defs.FindingTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    Arn = field("Arn")
    CreatedAt = field("CreatedAt")
    Id = field("Id")
    Region = field("Region")

    @cached_property
    def Resource(self):  # pragma: no cover
        return Resource.make_one(self.boto3_raw_data["Resource"])

    SchemaVersion = field("SchemaVersion")
    Severity = field("Severity")
    Type = field("Type")
    UpdatedAt = field("UpdatedAt")
    Confidence = field("Confidence")
    Description = field("Description")
    Partition = field("Partition")

    @cached_property
    def Service(self):  # pragma: no cover
        return Service.make_one(self.boto3_raw_data["Service"])

    Title = field("Title")
    AssociatedAttackSequenceArn = field("AssociatedAttackSequenceArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FindingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FindingTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFindingsResponse:
    boto3_raw_data: "type_defs.GetFindingsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Findings(self):  # pragma: no cover
        return Finding.make_many(self.boto3_raw_data["Findings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFindingsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFindingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]

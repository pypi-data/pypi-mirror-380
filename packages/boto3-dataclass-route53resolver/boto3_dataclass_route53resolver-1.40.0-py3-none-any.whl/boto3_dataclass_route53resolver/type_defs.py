# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_route53resolver import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


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
class FirewallRuleGroupAssociation:
    boto3_raw_data: "type_defs.FirewallRuleGroupAssociationTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    Arn = field("Arn")
    FirewallRuleGroupId = field("FirewallRuleGroupId")
    VpcId = field("VpcId")
    Name = field("Name")
    Priority = field("Priority")
    MutationProtection = field("MutationProtection")
    ManagedOwnerName = field("ManagedOwnerName")
    Status = field("Status")
    StatusMessage = field("StatusMessage")
    CreatorRequestId = field("CreatorRequestId")
    CreationTime = field("CreationTime")
    ModificationTime = field("ModificationTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FirewallRuleGroupAssociationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FirewallRuleGroupAssociationTypeDef"]
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
class IpAddressUpdate:
    boto3_raw_data: "type_defs.IpAddressUpdateTypeDef" = dataclasses.field()

    IpId = field("IpId")
    SubnetId = field("SubnetId")
    Ip = field("Ip")
    Ipv6 = field("Ipv6")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IpAddressUpdateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IpAddressUpdateTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResolverEndpoint:
    boto3_raw_data: "type_defs.ResolverEndpointTypeDef" = dataclasses.field()

    Id = field("Id")
    CreatorRequestId = field("CreatorRequestId")
    Arn = field("Arn")
    Name = field("Name")
    SecurityGroupIds = field("SecurityGroupIds")
    Direction = field("Direction")
    IpAddressCount = field("IpAddressCount")
    HostVPCId = field("HostVPCId")
    Status = field("Status")
    StatusMessage = field("StatusMessage")
    CreationTime = field("CreationTime")
    ModificationTime = field("ModificationTime")
    OutpostArn = field("OutpostArn")
    PreferredInstanceType = field("PreferredInstanceType")
    ResolverEndpointType = field("ResolverEndpointType")
    Protocols = field("Protocols")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResolverEndpointTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResolverEndpointTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateResolverQueryLogConfigRequest:
    boto3_raw_data: "type_defs.AssociateResolverQueryLogConfigRequestTypeDef" = (
        dataclasses.field()
    )

    ResolverQueryLogConfigId = field("ResolverQueryLogConfigId")
    ResourceId = field("ResourceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateResolverQueryLogConfigRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateResolverQueryLogConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResolverQueryLogConfigAssociation:
    boto3_raw_data: "type_defs.ResolverQueryLogConfigAssociationTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    ResolverQueryLogConfigId = field("ResolverQueryLogConfigId")
    ResourceId = field("ResourceId")
    Status = field("Status")
    Error = field("Error")
    ErrorMessage = field("ErrorMessage")
    CreationTime = field("CreationTime")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResolverQueryLogConfigAssociationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResolverQueryLogConfigAssociationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateResolverRuleRequest:
    boto3_raw_data: "type_defs.AssociateResolverRuleRequestTypeDef" = (
        dataclasses.field()
    )

    ResolverRuleId = field("ResolverRuleId")
    VPCId = field("VPCId")
    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateResolverRuleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateResolverRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResolverRuleAssociation:
    boto3_raw_data: "type_defs.ResolverRuleAssociationTypeDef" = dataclasses.field()

    Id = field("Id")
    ResolverRuleId = field("ResolverRuleId")
    Name = field("Name")
    VPCId = field("VPCId")
    Status = field("Status")
    StatusMessage = field("StatusMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResolverRuleAssociationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResolverRuleAssociationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FirewallDomainList:
    boto3_raw_data: "type_defs.FirewallDomainListTypeDef" = dataclasses.field()

    Id = field("Id")
    Arn = field("Arn")
    Name = field("Name")
    DomainCount = field("DomainCount")
    Status = field("Status")
    StatusMessage = field("StatusMessage")
    ManagedOwnerName = field("ManagedOwnerName")
    CreatorRequestId = field("CreatorRequestId")
    CreationTime = field("CreationTime")
    ModificationTime = field("ModificationTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FirewallDomainListTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FirewallDomainListTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FirewallRuleGroup:
    boto3_raw_data: "type_defs.FirewallRuleGroupTypeDef" = dataclasses.field()

    Id = field("Id")
    Arn = field("Arn")
    Name = field("Name")
    RuleCount = field("RuleCount")
    Status = field("Status")
    StatusMessage = field("StatusMessage")
    OwnerId = field("OwnerId")
    CreatorRequestId = field("CreatorRequestId")
    ShareStatus = field("ShareStatus")
    CreationTime = field("CreationTime")
    ModificationTime = field("ModificationTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FirewallRuleGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FirewallRuleGroupTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFirewallRuleRequest:
    boto3_raw_data: "type_defs.CreateFirewallRuleRequestTypeDef" = dataclasses.field()

    CreatorRequestId = field("CreatorRequestId")
    FirewallRuleGroupId = field("FirewallRuleGroupId")
    Priority = field("Priority")
    Action = field("Action")
    Name = field("Name")
    FirewallDomainListId = field("FirewallDomainListId")
    BlockResponse = field("BlockResponse")
    BlockOverrideDomain = field("BlockOverrideDomain")
    BlockOverrideDnsType = field("BlockOverrideDnsType")
    BlockOverrideTtl = field("BlockOverrideTtl")
    FirewallDomainRedirectionAction = field("FirewallDomainRedirectionAction")
    Qtype = field("Qtype")
    DnsThreatProtection = field("DnsThreatProtection")
    ConfidenceThreshold = field("ConfidenceThreshold")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFirewallRuleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFirewallRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FirewallRule:
    boto3_raw_data: "type_defs.FirewallRuleTypeDef" = dataclasses.field()

    FirewallRuleGroupId = field("FirewallRuleGroupId")
    FirewallDomainListId = field("FirewallDomainListId")
    FirewallThreatProtectionId = field("FirewallThreatProtectionId")
    Name = field("Name")
    Priority = field("Priority")
    Action = field("Action")
    BlockResponse = field("BlockResponse")
    BlockOverrideDomain = field("BlockOverrideDomain")
    BlockOverrideDnsType = field("BlockOverrideDnsType")
    BlockOverrideTtl = field("BlockOverrideTtl")
    CreatorRequestId = field("CreatorRequestId")
    CreationTime = field("CreationTime")
    ModificationTime = field("ModificationTime")
    FirewallDomainRedirectionAction = field("FirewallDomainRedirectionAction")
    Qtype = field("Qtype")
    DnsThreatProtection = field("DnsThreatProtection")
    ConfidenceThreshold = field("ConfidenceThreshold")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FirewallRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FirewallRuleTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutpostResolver:
    boto3_raw_data: "type_defs.OutpostResolverTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CreationTime = field("CreationTime")
    ModificationTime = field("ModificationTime")
    CreatorRequestId = field("CreatorRequestId")
    Id = field("Id")
    InstanceCount = field("InstanceCount")
    PreferredInstanceType = field("PreferredInstanceType")
    Name = field("Name")
    Status = field("Status")
    StatusMessage = field("StatusMessage")
    OutpostArn = field("OutpostArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OutpostResolverTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OutpostResolverTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IpAddressRequest:
    boto3_raw_data: "type_defs.IpAddressRequestTypeDef" = dataclasses.field()

    SubnetId = field("SubnetId")
    Ip = field("Ip")
    Ipv6 = field("Ipv6")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IpAddressRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IpAddressRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResolverQueryLogConfig:
    boto3_raw_data: "type_defs.ResolverQueryLogConfigTypeDef" = dataclasses.field()

    Id = field("Id")
    OwnerId = field("OwnerId")
    Status = field("Status")
    ShareStatus = field("ShareStatus")
    AssociationCount = field("AssociationCount")
    Arn = field("Arn")
    Name = field("Name")
    DestinationArn = field("DestinationArn")
    CreatorRequestId = field("CreatorRequestId")
    CreationTime = field("CreationTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResolverQueryLogConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResolverQueryLogConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetAddress:
    boto3_raw_data: "type_defs.TargetAddressTypeDef" = dataclasses.field()

    Ip = field("Ip")
    Port = field("Port")
    Ipv6 = field("Ipv6")
    Protocol = field("Protocol")
    ServerNameIndication = field("ServerNameIndication")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TargetAddressTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TargetAddressTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFirewallDomainListRequest:
    boto3_raw_data: "type_defs.DeleteFirewallDomainListRequestTypeDef" = (
        dataclasses.field()
    )

    FirewallDomainListId = field("FirewallDomainListId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteFirewallDomainListRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFirewallDomainListRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFirewallRuleGroupRequest:
    boto3_raw_data: "type_defs.DeleteFirewallRuleGroupRequestTypeDef" = (
        dataclasses.field()
    )

    FirewallRuleGroupId = field("FirewallRuleGroupId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteFirewallRuleGroupRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFirewallRuleGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFirewallRuleRequest:
    boto3_raw_data: "type_defs.DeleteFirewallRuleRequestTypeDef" = dataclasses.field()

    FirewallRuleGroupId = field("FirewallRuleGroupId")
    FirewallDomainListId = field("FirewallDomainListId")
    FirewallThreatProtectionId = field("FirewallThreatProtectionId")
    Qtype = field("Qtype")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteFirewallRuleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFirewallRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteOutpostResolverRequest:
    boto3_raw_data: "type_defs.DeleteOutpostResolverRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteOutpostResolverRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteOutpostResolverRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteResolverEndpointRequest:
    boto3_raw_data: "type_defs.DeleteResolverEndpointRequestTypeDef" = (
        dataclasses.field()
    )

    ResolverEndpointId = field("ResolverEndpointId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteResolverEndpointRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteResolverEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteResolverQueryLogConfigRequest:
    boto3_raw_data: "type_defs.DeleteResolverQueryLogConfigRequestTypeDef" = (
        dataclasses.field()
    )

    ResolverQueryLogConfigId = field("ResolverQueryLogConfigId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteResolverQueryLogConfigRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteResolverQueryLogConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteResolverRuleRequest:
    boto3_raw_data: "type_defs.DeleteResolverRuleRequestTypeDef" = dataclasses.field()

    ResolverRuleId = field("ResolverRuleId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteResolverRuleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteResolverRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateFirewallRuleGroupRequest:
    boto3_raw_data: "type_defs.DisassociateFirewallRuleGroupRequestTypeDef" = (
        dataclasses.field()
    )

    FirewallRuleGroupAssociationId = field("FirewallRuleGroupAssociationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateFirewallRuleGroupRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateFirewallRuleGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateResolverQueryLogConfigRequest:
    boto3_raw_data: "type_defs.DisassociateResolverQueryLogConfigRequestTypeDef" = (
        dataclasses.field()
    )

    ResolverQueryLogConfigId = field("ResolverQueryLogConfigId")
    ResourceId = field("ResourceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateResolverQueryLogConfigRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateResolverQueryLogConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateResolverRuleRequest:
    boto3_raw_data: "type_defs.DisassociateResolverRuleRequestTypeDef" = (
        dataclasses.field()
    )

    VPCId = field("VPCId")
    ResolverRuleId = field("ResolverRuleId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DisassociateResolverRuleRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateResolverRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Filter:
    boto3_raw_data: "type_defs.FilterTypeDef" = dataclasses.field()

    Name = field("Name")
    Values = field("Values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FilterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FirewallConfig:
    boto3_raw_data: "type_defs.FirewallConfigTypeDef" = dataclasses.field()

    Id = field("Id")
    ResourceId = field("ResourceId")
    OwnerId = field("OwnerId")
    FirewallFailOpen = field("FirewallFailOpen")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FirewallConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FirewallConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FirewallDomainListMetadata:
    boto3_raw_data: "type_defs.FirewallDomainListMetadataTypeDef" = dataclasses.field()

    Id = field("Id")
    Arn = field("Arn")
    Name = field("Name")
    CreatorRequestId = field("CreatorRequestId")
    ManagedOwnerName = field("ManagedOwnerName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FirewallDomainListMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FirewallDomainListMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FirewallRuleGroupMetadata:
    boto3_raw_data: "type_defs.FirewallRuleGroupMetadataTypeDef" = dataclasses.field()

    Id = field("Id")
    Arn = field("Arn")
    Name = field("Name")
    OwnerId = field("OwnerId")
    CreatorRequestId = field("CreatorRequestId")
    ShareStatus = field("ShareStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FirewallRuleGroupMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FirewallRuleGroupMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFirewallConfigRequest:
    boto3_raw_data: "type_defs.GetFirewallConfigRequestTypeDef" = dataclasses.field()

    ResourceId = field("ResourceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFirewallConfigRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFirewallConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFirewallDomainListRequest:
    boto3_raw_data: "type_defs.GetFirewallDomainListRequestTypeDef" = (
        dataclasses.field()
    )

    FirewallDomainListId = field("FirewallDomainListId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFirewallDomainListRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFirewallDomainListRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFirewallRuleGroupAssociationRequest:
    boto3_raw_data: "type_defs.GetFirewallRuleGroupAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    FirewallRuleGroupAssociationId = field("FirewallRuleGroupAssociationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetFirewallRuleGroupAssociationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFirewallRuleGroupAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFirewallRuleGroupPolicyRequest:
    boto3_raw_data: "type_defs.GetFirewallRuleGroupPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetFirewallRuleGroupPolicyRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFirewallRuleGroupPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFirewallRuleGroupRequest:
    boto3_raw_data: "type_defs.GetFirewallRuleGroupRequestTypeDef" = dataclasses.field()

    FirewallRuleGroupId = field("FirewallRuleGroupId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFirewallRuleGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFirewallRuleGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOutpostResolverRequest:
    boto3_raw_data: "type_defs.GetOutpostResolverRequestTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetOutpostResolverRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOutpostResolverRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResolverConfigRequest:
    boto3_raw_data: "type_defs.GetResolverConfigRequestTypeDef" = dataclasses.field()

    ResourceId = field("ResourceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResolverConfigRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResolverConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResolverConfig:
    boto3_raw_data: "type_defs.ResolverConfigTypeDef" = dataclasses.field()

    Id = field("Id")
    ResourceId = field("ResourceId")
    OwnerId = field("OwnerId")
    AutodefinedReverse = field("AutodefinedReverse")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResolverConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResolverConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResolverDnssecConfigRequest:
    boto3_raw_data: "type_defs.GetResolverDnssecConfigRequestTypeDef" = (
        dataclasses.field()
    )

    ResourceId = field("ResourceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetResolverDnssecConfigRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResolverDnssecConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResolverDnssecConfig:
    boto3_raw_data: "type_defs.ResolverDnssecConfigTypeDef" = dataclasses.field()

    Id = field("Id")
    OwnerId = field("OwnerId")
    ResourceId = field("ResourceId")
    ValidationStatus = field("ValidationStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResolverDnssecConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResolverDnssecConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResolverEndpointRequest:
    boto3_raw_data: "type_defs.GetResolverEndpointRequestTypeDef" = dataclasses.field()

    ResolverEndpointId = field("ResolverEndpointId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResolverEndpointRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResolverEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResolverQueryLogConfigAssociationRequest:
    boto3_raw_data: "type_defs.GetResolverQueryLogConfigAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    ResolverQueryLogConfigAssociationId = field("ResolverQueryLogConfigAssociationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetResolverQueryLogConfigAssociationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResolverQueryLogConfigAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResolverQueryLogConfigPolicyRequest:
    boto3_raw_data: "type_defs.GetResolverQueryLogConfigPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetResolverQueryLogConfigPolicyRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResolverQueryLogConfigPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResolverQueryLogConfigRequest:
    boto3_raw_data: "type_defs.GetResolverQueryLogConfigRequestTypeDef" = (
        dataclasses.field()
    )

    ResolverQueryLogConfigId = field("ResolverQueryLogConfigId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetResolverQueryLogConfigRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResolverQueryLogConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResolverRuleAssociationRequest:
    boto3_raw_data: "type_defs.GetResolverRuleAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    ResolverRuleAssociationId = field("ResolverRuleAssociationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetResolverRuleAssociationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResolverRuleAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResolverRulePolicyRequest:
    boto3_raw_data: "type_defs.GetResolverRulePolicyRequestTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResolverRulePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResolverRulePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResolverRuleRequest:
    boto3_raw_data: "type_defs.GetResolverRuleRequestTypeDef" = dataclasses.field()

    ResolverRuleId = field("ResolverRuleId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResolverRuleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResolverRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportFirewallDomainsRequest:
    boto3_raw_data: "type_defs.ImportFirewallDomainsRequestTypeDef" = (
        dataclasses.field()
    )

    FirewallDomainListId = field("FirewallDomainListId")
    Operation = field("Operation")
    DomainFileUrl = field("DomainFileUrl")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportFirewallDomainsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportFirewallDomainsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IpAddressResponse:
    boto3_raw_data: "type_defs.IpAddressResponseTypeDef" = dataclasses.field()

    IpId = field("IpId")
    SubnetId = field("SubnetId")
    Ip = field("Ip")
    Ipv6 = field("Ipv6")
    Status = field("Status")
    StatusMessage = field("StatusMessage")
    CreationTime = field("CreationTime")
    ModificationTime = field("ModificationTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IpAddressResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IpAddressResponseTypeDef"]
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
class ListFirewallConfigsRequest:
    boto3_raw_data: "type_defs.ListFirewallConfigsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFirewallConfigsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFirewallConfigsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFirewallDomainListsRequest:
    boto3_raw_data: "type_defs.ListFirewallDomainListsRequestTypeDef" = (
        dataclasses.field()
    )

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListFirewallDomainListsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFirewallDomainListsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFirewallDomainsRequest:
    boto3_raw_data: "type_defs.ListFirewallDomainsRequestTypeDef" = dataclasses.field()

    FirewallDomainListId = field("FirewallDomainListId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFirewallDomainsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFirewallDomainsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFirewallRuleGroupAssociationsRequest:
    boto3_raw_data: "type_defs.ListFirewallRuleGroupAssociationsRequestTypeDef" = (
        dataclasses.field()
    )

    FirewallRuleGroupId = field("FirewallRuleGroupId")
    VpcId = field("VpcId")
    Priority = field("Priority")
    Status = field("Status")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListFirewallRuleGroupAssociationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFirewallRuleGroupAssociationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFirewallRuleGroupsRequest:
    boto3_raw_data: "type_defs.ListFirewallRuleGroupsRequestTypeDef" = (
        dataclasses.field()
    )

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListFirewallRuleGroupsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFirewallRuleGroupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFirewallRulesRequest:
    boto3_raw_data: "type_defs.ListFirewallRulesRequestTypeDef" = dataclasses.field()

    FirewallRuleGroupId = field("FirewallRuleGroupId")
    Priority = field("Priority")
    Action = field("Action")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFirewallRulesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFirewallRulesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOutpostResolversRequest:
    boto3_raw_data: "type_defs.ListOutpostResolversRequestTypeDef" = dataclasses.field()

    OutpostArn = field("OutpostArn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListOutpostResolversRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOutpostResolversRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResolverConfigsRequest:
    boto3_raw_data: "type_defs.ListResolverConfigsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListResolverConfigsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResolverConfigsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResolverEndpointIpAddressesRequest:
    boto3_raw_data: "type_defs.ListResolverEndpointIpAddressesRequestTypeDef" = (
        dataclasses.field()
    )

    ResolverEndpointId = field("ResolverEndpointId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResolverEndpointIpAddressesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResolverEndpointIpAddressesRequestTypeDef"]
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
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

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
class PutFirewallRuleGroupPolicyRequest:
    boto3_raw_data: "type_defs.PutFirewallRuleGroupPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    FirewallRuleGroupPolicy = field("FirewallRuleGroupPolicy")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutFirewallRuleGroupPolicyRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutFirewallRuleGroupPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutResolverQueryLogConfigPolicyRequest:
    boto3_raw_data: "type_defs.PutResolverQueryLogConfigPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    ResolverQueryLogConfigPolicy = field("ResolverQueryLogConfigPolicy")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutResolverQueryLogConfigPolicyRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutResolverQueryLogConfigPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutResolverRulePolicyRequest:
    boto3_raw_data: "type_defs.PutResolverRulePolicyRequestTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    ResolverRulePolicy = field("ResolverRulePolicy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutResolverRulePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutResolverRulePolicyRequestTypeDef"]
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
class UpdateFirewallConfigRequest:
    boto3_raw_data: "type_defs.UpdateFirewallConfigRequestTypeDef" = dataclasses.field()

    ResourceId = field("ResourceId")
    FirewallFailOpen = field("FirewallFailOpen")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFirewallConfigRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFirewallConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFirewallDomainsRequest:
    boto3_raw_data: "type_defs.UpdateFirewallDomainsRequestTypeDef" = (
        dataclasses.field()
    )

    FirewallDomainListId = field("FirewallDomainListId")
    Operation = field("Operation")
    Domains = field("Domains")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFirewallDomainsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFirewallDomainsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFirewallRuleGroupAssociationRequest:
    boto3_raw_data: "type_defs.UpdateFirewallRuleGroupAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    FirewallRuleGroupAssociationId = field("FirewallRuleGroupAssociationId")
    Priority = field("Priority")
    MutationProtection = field("MutationProtection")
    Name = field("Name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateFirewallRuleGroupAssociationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFirewallRuleGroupAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFirewallRuleRequest:
    boto3_raw_data: "type_defs.UpdateFirewallRuleRequestTypeDef" = dataclasses.field()

    FirewallRuleGroupId = field("FirewallRuleGroupId")
    FirewallDomainListId = field("FirewallDomainListId")
    FirewallThreatProtectionId = field("FirewallThreatProtectionId")
    Priority = field("Priority")
    Action = field("Action")
    BlockResponse = field("BlockResponse")
    BlockOverrideDomain = field("BlockOverrideDomain")
    BlockOverrideDnsType = field("BlockOverrideDnsType")
    BlockOverrideTtl = field("BlockOverrideTtl")
    Name = field("Name")
    FirewallDomainRedirectionAction = field("FirewallDomainRedirectionAction")
    Qtype = field("Qtype")
    DnsThreatProtection = field("DnsThreatProtection")
    ConfidenceThreshold = field("ConfidenceThreshold")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFirewallRuleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFirewallRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateIpAddress:
    boto3_raw_data: "type_defs.UpdateIpAddressTypeDef" = dataclasses.field()

    IpId = field("IpId")
    Ipv6 = field("Ipv6")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateIpAddressTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UpdateIpAddressTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateOutpostResolverRequest:
    boto3_raw_data: "type_defs.UpdateOutpostResolverRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    Name = field("Name")
    InstanceCount = field("InstanceCount")
    PreferredInstanceType = field("PreferredInstanceType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateOutpostResolverRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateOutpostResolverRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateResolverConfigRequest:
    boto3_raw_data: "type_defs.UpdateResolverConfigRequestTypeDef" = dataclasses.field()

    ResourceId = field("ResourceId")
    AutodefinedReverseFlag = field("AutodefinedReverseFlag")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateResolverConfigRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateResolverConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateResolverDnssecConfigRequest:
    boto3_raw_data: "type_defs.UpdateResolverDnssecConfigRequestTypeDef" = (
        dataclasses.field()
    )

    ResourceId = field("ResourceId")
    Validation = field("Validation")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateResolverDnssecConfigRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateResolverDnssecConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateFirewallRuleGroupRequest:
    boto3_raw_data: "type_defs.AssociateFirewallRuleGroupRequestTypeDef" = (
        dataclasses.field()
    )

    CreatorRequestId = field("CreatorRequestId")
    FirewallRuleGroupId = field("FirewallRuleGroupId")
    VpcId = field("VpcId")
    Priority = field("Priority")
    Name = field("Name")
    MutationProtection = field("MutationProtection")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateFirewallRuleGroupRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateFirewallRuleGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFirewallDomainListRequest:
    boto3_raw_data: "type_defs.CreateFirewallDomainListRequestTypeDef" = (
        dataclasses.field()
    )

    CreatorRequestId = field("CreatorRequestId")
    Name = field("Name")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateFirewallDomainListRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFirewallDomainListRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFirewallRuleGroupRequest:
    boto3_raw_data: "type_defs.CreateFirewallRuleGroupRequestTypeDef" = (
        dataclasses.field()
    )

    CreatorRequestId = field("CreatorRequestId")
    Name = field("Name")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateFirewallRuleGroupRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFirewallRuleGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateOutpostResolverRequest:
    boto3_raw_data: "type_defs.CreateOutpostResolverRequestTypeDef" = (
        dataclasses.field()
    )

    CreatorRequestId = field("CreatorRequestId")
    Name = field("Name")
    PreferredInstanceType = field("PreferredInstanceType")
    OutpostArn = field("OutpostArn")
    InstanceCount = field("InstanceCount")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateOutpostResolverRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateOutpostResolverRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateResolverQueryLogConfigRequest:
    boto3_raw_data: "type_defs.CreateResolverQueryLogConfigRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    DestinationArn = field("DestinationArn")
    CreatorRequestId = field("CreatorRequestId")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateResolverQueryLogConfigRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateResolverQueryLogConfigRequestTypeDef"]
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
class AssociateFirewallRuleGroupResponse:
    boto3_raw_data: "type_defs.AssociateFirewallRuleGroupResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FirewallRuleGroupAssociation(self):  # pragma: no cover
        return FirewallRuleGroupAssociation.make_one(
            self.boto3_raw_data["FirewallRuleGroupAssociation"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateFirewallRuleGroupResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateFirewallRuleGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateFirewallRuleGroupResponse:
    boto3_raw_data: "type_defs.DisassociateFirewallRuleGroupResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FirewallRuleGroupAssociation(self):  # pragma: no cover
        return FirewallRuleGroupAssociation.make_one(
            self.boto3_raw_data["FirewallRuleGroupAssociation"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateFirewallRuleGroupResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateFirewallRuleGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFirewallRuleGroupAssociationResponse:
    boto3_raw_data: "type_defs.GetFirewallRuleGroupAssociationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FirewallRuleGroupAssociation(self):  # pragma: no cover
        return FirewallRuleGroupAssociation.make_one(
            self.boto3_raw_data["FirewallRuleGroupAssociation"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetFirewallRuleGroupAssociationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFirewallRuleGroupAssociationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFirewallRuleGroupPolicyResponse:
    boto3_raw_data: "type_defs.GetFirewallRuleGroupPolicyResponseTypeDef" = (
        dataclasses.field()
    )

    FirewallRuleGroupPolicy = field("FirewallRuleGroupPolicy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetFirewallRuleGroupPolicyResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFirewallRuleGroupPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResolverQueryLogConfigPolicyResponse:
    boto3_raw_data: "type_defs.GetResolverQueryLogConfigPolicyResponseTypeDef" = (
        dataclasses.field()
    )

    ResolverQueryLogConfigPolicy = field("ResolverQueryLogConfigPolicy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetResolverQueryLogConfigPolicyResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResolverQueryLogConfigPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResolverRulePolicyResponse:
    boto3_raw_data: "type_defs.GetResolverRulePolicyResponseTypeDef" = (
        dataclasses.field()
    )

    ResolverRulePolicy = field("ResolverRulePolicy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetResolverRulePolicyResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResolverRulePolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportFirewallDomainsResponse:
    boto3_raw_data: "type_defs.ImportFirewallDomainsResponseTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    Name = field("Name")
    Status = field("Status")
    StatusMessage = field("StatusMessage")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ImportFirewallDomainsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportFirewallDomainsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFirewallDomainsResponse:
    boto3_raw_data: "type_defs.ListFirewallDomainsResponseTypeDef" = dataclasses.field()

    Domains = field("Domains")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFirewallDomainsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFirewallDomainsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFirewallRuleGroupAssociationsResponse:
    boto3_raw_data: "type_defs.ListFirewallRuleGroupAssociationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FirewallRuleGroupAssociations(self):  # pragma: no cover
        return FirewallRuleGroupAssociation.make_many(
            self.boto3_raw_data["FirewallRuleGroupAssociations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListFirewallRuleGroupAssociationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFirewallRuleGroupAssociationsResponseTypeDef"]
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

    NextToken = field("NextToken")

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
class PutFirewallRuleGroupPolicyResponse:
    boto3_raw_data: "type_defs.PutFirewallRuleGroupPolicyResponseTypeDef" = (
        dataclasses.field()
    )

    ReturnValue = field("ReturnValue")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutFirewallRuleGroupPolicyResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutFirewallRuleGroupPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutResolverQueryLogConfigPolicyResponse:
    boto3_raw_data: "type_defs.PutResolverQueryLogConfigPolicyResponseTypeDef" = (
        dataclasses.field()
    )

    ReturnValue = field("ReturnValue")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutResolverQueryLogConfigPolicyResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutResolverQueryLogConfigPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutResolverRulePolicyResponse:
    boto3_raw_data: "type_defs.PutResolverRulePolicyResponseTypeDef" = (
        dataclasses.field()
    )

    ReturnValue = field("ReturnValue")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutResolverRulePolicyResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutResolverRulePolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFirewallDomainsResponse:
    boto3_raw_data: "type_defs.UpdateFirewallDomainsResponseTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    Name = field("Name")
    Status = field("Status")
    StatusMessage = field("StatusMessage")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateFirewallDomainsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFirewallDomainsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFirewallRuleGroupAssociationResponse:
    boto3_raw_data: "type_defs.UpdateFirewallRuleGroupAssociationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FirewallRuleGroupAssociation(self):  # pragma: no cover
        return FirewallRuleGroupAssociation.make_one(
            self.boto3_raw_data["FirewallRuleGroupAssociation"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateFirewallRuleGroupAssociationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFirewallRuleGroupAssociationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateResolverEndpointIpAddressRequest:
    boto3_raw_data: "type_defs.AssociateResolverEndpointIpAddressRequestTypeDef" = (
        dataclasses.field()
    )

    ResolverEndpointId = field("ResolverEndpointId")

    @cached_property
    def IpAddress(self):  # pragma: no cover
        return IpAddressUpdate.make_one(self.boto3_raw_data["IpAddress"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateResolverEndpointIpAddressRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateResolverEndpointIpAddressRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateResolverEndpointIpAddressRequest:
    boto3_raw_data: "type_defs.DisassociateResolverEndpointIpAddressRequestTypeDef" = (
        dataclasses.field()
    )

    ResolverEndpointId = field("ResolverEndpointId")

    @cached_property
    def IpAddress(self):  # pragma: no cover
        return IpAddressUpdate.make_one(self.boto3_raw_data["IpAddress"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateResolverEndpointIpAddressRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateResolverEndpointIpAddressRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateResolverEndpointIpAddressResponse:
    boto3_raw_data: "type_defs.AssociateResolverEndpointIpAddressResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ResolverEndpoint(self):  # pragma: no cover
        return ResolverEndpoint.make_one(self.boto3_raw_data["ResolverEndpoint"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateResolverEndpointIpAddressResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateResolverEndpointIpAddressResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateResolverEndpointResponse:
    boto3_raw_data: "type_defs.CreateResolverEndpointResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ResolverEndpoint(self):  # pragma: no cover
        return ResolverEndpoint.make_one(self.boto3_raw_data["ResolverEndpoint"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateResolverEndpointResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateResolverEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteResolverEndpointResponse:
    boto3_raw_data: "type_defs.DeleteResolverEndpointResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ResolverEndpoint(self):  # pragma: no cover
        return ResolverEndpoint.make_one(self.boto3_raw_data["ResolverEndpoint"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteResolverEndpointResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteResolverEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateResolverEndpointIpAddressResponse:
    boto3_raw_data: "type_defs.DisassociateResolverEndpointIpAddressResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ResolverEndpoint(self):  # pragma: no cover
        return ResolverEndpoint.make_one(self.boto3_raw_data["ResolverEndpoint"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateResolverEndpointIpAddressResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateResolverEndpointIpAddressResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResolverEndpointResponse:
    boto3_raw_data: "type_defs.GetResolverEndpointResponseTypeDef" = dataclasses.field()

    @cached_property
    def ResolverEndpoint(self):  # pragma: no cover
        return ResolverEndpoint.make_one(self.boto3_raw_data["ResolverEndpoint"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResolverEndpointResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResolverEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResolverEndpointsResponse:
    boto3_raw_data: "type_defs.ListResolverEndpointsResponseTypeDef" = (
        dataclasses.field()
    )

    MaxResults = field("MaxResults")

    @cached_property
    def ResolverEndpoints(self):  # pragma: no cover
        return ResolverEndpoint.make_many(self.boto3_raw_data["ResolverEndpoints"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListResolverEndpointsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResolverEndpointsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateResolverEndpointResponse:
    boto3_raw_data: "type_defs.UpdateResolverEndpointResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ResolverEndpoint(self):  # pragma: no cover
        return ResolverEndpoint.make_one(self.boto3_raw_data["ResolverEndpoint"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateResolverEndpointResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateResolverEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateResolverQueryLogConfigResponse:
    boto3_raw_data: "type_defs.AssociateResolverQueryLogConfigResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ResolverQueryLogConfigAssociation(self):  # pragma: no cover
        return ResolverQueryLogConfigAssociation.make_one(
            self.boto3_raw_data["ResolverQueryLogConfigAssociation"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateResolverQueryLogConfigResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateResolverQueryLogConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateResolverQueryLogConfigResponse:
    boto3_raw_data: "type_defs.DisassociateResolverQueryLogConfigResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ResolverQueryLogConfigAssociation(self):  # pragma: no cover
        return ResolverQueryLogConfigAssociation.make_one(
            self.boto3_raw_data["ResolverQueryLogConfigAssociation"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateResolverQueryLogConfigResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateResolverQueryLogConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResolverQueryLogConfigAssociationResponse:
    boto3_raw_data: "type_defs.GetResolverQueryLogConfigAssociationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ResolverQueryLogConfigAssociation(self):  # pragma: no cover
        return ResolverQueryLogConfigAssociation.make_one(
            self.boto3_raw_data["ResolverQueryLogConfigAssociation"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetResolverQueryLogConfigAssociationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResolverQueryLogConfigAssociationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResolverQueryLogConfigAssociationsResponse:
    boto3_raw_data: (
        "type_defs.ListResolverQueryLogConfigAssociationsResponseTypeDef"
    ) = dataclasses.field()

    TotalCount = field("TotalCount")
    TotalFilteredCount = field("TotalFilteredCount")

    @cached_property
    def ResolverQueryLogConfigAssociations(self):  # pragma: no cover
        return ResolverQueryLogConfigAssociation.make_many(
            self.boto3_raw_data["ResolverQueryLogConfigAssociations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResolverQueryLogConfigAssociationsResponseTypeDef"
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
                "type_defs.ListResolverQueryLogConfigAssociationsResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateResolverRuleResponse:
    boto3_raw_data: "type_defs.AssociateResolverRuleResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ResolverRuleAssociation(self):  # pragma: no cover
        return ResolverRuleAssociation.make_one(
            self.boto3_raw_data["ResolverRuleAssociation"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssociateResolverRuleResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateResolverRuleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateResolverRuleResponse:
    boto3_raw_data: "type_defs.DisassociateResolverRuleResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ResolverRuleAssociation(self):  # pragma: no cover
        return ResolverRuleAssociation.make_one(
            self.boto3_raw_data["ResolverRuleAssociation"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DisassociateResolverRuleResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateResolverRuleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResolverRuleAssociationResponse:
    boto3_raw_data: "type_defs.GetResolverRuleAssociationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ResolverRuleAssociation(self):  # pragma: no cover
        return ResolverRuleAssociation.make_one(
            self.boto3_raw_data["ResolverRuleAssociation"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetResolverRuleAssociationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResolverRuleAssociationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResolverRuleAssociationsResponse:
    boto3_raw_data: "type_defs.ListResolverRuleAssociationsResponseTypeDef" = (
        dataclasses.field()
    )

    MaxResults = field("MaxResults")

    @cached_property
    def ResolverRuleAssociations(self):  # pragma: no cover
        return ResolverRuleAssociation.make_many(
            self.boto3_raw_data["ResolverRuleAssociations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResolverRuleAssociationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResolverRuleAssociationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFirewallDomainListResponse:
    boto3_raw_data: "type_defs.CreateFirewallDomainListResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FirewallDomainList(self):  # pragma: no cover
        return FirewallDomainList.make_one(self.boto3_raw_data["FirewallDomainList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateFirewallDomainListResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFirewallDomainListResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFirewallDomainListResponse:
    boto3_raw_data: "type_defs.DeleteFirewallDomainListResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FirewallDomainList(self):  # pragma: no cover
        return FirewallDomainList.make_one(self.boto3_raw_data["FirewallDomainList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteFirewallDomainListResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFirewallDomainListResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFirewallDomainListResponse:
    boto3_raw_data: "type_defs.GetFirewallDomainListResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FirewallDomainList(self):  # pragma: no cover
        return FirewallDomainList.make_one(self.boto3_raw_data["FirewallDomainList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetFirewallDomainListResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFirewallDomainListResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFirewallRuleGroupResponse:
    boto3_raw_data: "type_defs.CreateFirewallRuleGroupResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FirewallRuleGroup(self):  # pragma: no cover
        return FirewallRuleGroup.make_one(self.boto3_raw_data["FirewallRuleGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateFirewallRuleGroupResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFirewallRuleGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFirewallRuleGroupResponse:
    boto3_raw_data: "type_defs.DeleteFirewallRuleGroupResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FirewallRuleGroup(self):  # pragma: no cover
        return FirewallRuleGroup.make_one(self.boto3_raw_data["FirewallRuleGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteFirewallRuleGroupResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFirewallRuleGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFirewallRuleGroupResponse:
    boto3_raw_data: "type_defs.GetFirewallRuleGroupResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FirewallRuleGroup(self):  # pragma: no cover
        return FirewallRuleGroup.make_one(self.boto3_raw_data["FirewallRuleGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFirewallRuleGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFirewallRuleGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFirewallRuleResponse:
    boto3_raw_data: "type_defs.CreateFirewallRuleResponseTypeDef" = dataclasses.field()

    @cached_property
    def FirewallRule(self):  # pragma: no cover
        return FirewallRule.make_one(self.boto3_raw_data["FirewallRule"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFirewallRuleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFirewallRuleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFirewallRuleResponse:
    boto3_raw_data: "type_defs.DeleteFirewallRuleResponseTypeDef" = dataclasses.field()

    @cached_property
    def FirewallRule(self):  # pragma: no cover
        return FirewallRule.make_one(self.boto3_raw_data["FirewallRule"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteFirewallRuleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFirewallRuleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFirewallRulesResponse:
    boto3_raw_data: "type_defs.ListFirewallRulesResponseTypeDef" = dataclasses.field()

    @cached_property
    def FirewallRules(self):  # pragma: no cover
        return FirewallRule.make_many(self.boto3_raw_data["FirewallRules"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFirewallRulesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFirewallRulesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFirewallRuleResponse:
    boto3_raw_data: "type_defs.UpdateFirewallRuleResponseTypeDef" = dataclasses.field()

    @cached_property
    def FirewallRule(self):  # pragma: no cover
        return FirewallRule.make_one(self.boto3_raw_data["FirewallRule"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFirewallRuleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFirewallRuleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateOutpostResolverResponse:
    boto3_raw_data: "type_defs.CreateOutpostResolverResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def OutpostResolver(self):  # pragma: no cover
        return OutpostResolver.make_one(self.boto3_raw_data["OutpostResolver"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateOutpostResolverResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateOutpostResolverResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteOutpostResolverResponse:
    boto3_raw_data: "type_defs.DeleteOutpostResolverResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def OutpostResolver(self):  # pragma: no cover
        return OutpostResolver.make_one(self.boto3_raw_data["OutpostResolver"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteOutpostResolverResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteOutpostResolverResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOutpostResolverResponse:
    boto3_raw_data: "type_defs.GetOutpostResolverResponseTypeDef" = dataclasses.field()

    @cached_property
    def OutpostResolver(self):  # pragma: no cover
        return OutpostResolver.make_one(self.boto3_raw_data["OutpostResolver"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetOutpostResolverResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOutpostResolverResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOutpostResolversResponse:
    boto3_raw_data: "type_defs.ListOutpostResolversResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def OutpostResolvers(self):  # pragma: no cover
        return OutpostResolver.make_many(self.boto3_raw_data["OutpostResolvers"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListOutpostResolversResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOutpostResolversResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateOutpostResolverResponse:
    boto3_raw_data: "type_defs.UpdateOutpostResolverResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def OutpostResolver(self):  # pragma: no cover
        return OutpostResolver.make_one(self.boto3_raw_data["OutpostResolver"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateOutpostResolverResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateOutpostResolverResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateResolverEndpointRequest:
    boto3_raw_data: "type_defs.CreateResolverEndpointRequestTypeDef" = (
        dataclasses.field()
    )

    CreatorRequestId = field("CreatorRequestId")
    SecurityGroupIds = field("SecurityGroupIds")
    Direction = field("Direction")

    @cached_property
    def IpAddresses(self):  # pragma: no cover
        return IpAddressRequest.make_many(self.boto3_raw_data["IpAddresses"])

    Name = field("Name")
    OutpostArn = field("OutpostArn")
    PreferredInstanceType = field("PreferredInstanceType")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    ResolverEndpointType = field("ResolverEndpointType")
    Protocols = field("Protocols")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateResolverEndpointRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateResolverEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateResolverQueryLogConfigResponse:
    boto3_raw_data: "type_defs.CreateResolverQueryLogConfigResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ResolverQueryLogConfig(self):  # pragma: no cover
        return ResolverQueryLogConfig.make_one(
            self.boto3_raw_data["ResolverQueryLogConfig"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateResolverQueryLogConfigResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateResolverQueryLogConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteResolverQueryLogConfigResponse:
    boto3_raw_data: "type_defs.DeleteResolverQueryLogConfigResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ResolverQueryLogConfig(self):  # pragma: no cover
        return ResolverQueryLogConfig.make_one(
            self.boto3_raw_data["ResolverQueryLogConfig"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteResolverQueryLogConfigResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteResolverQueryLogConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResolverQueryLogConfigResponse:
    boto3_raw_data: "type_defs.GetResolverQueryLogConfigResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ResolverQueryLogConfig(self):  # pragma: no cover
        return ResolverQueryLogConfig.make_one(
            self.boto3_raw_data["ResolverQueryLogConfig"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetResolverQueryLogConfigResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResolverQueryLogConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResolverQueryLogConfigsResponse:
    boto3_raw_data: "type_defs.ListResolverQueryLogConfigsResponseTypeDef" = (
        dataclasses.field()
    )

    TotalCount = field("TotalCount")
    TotalFilteredCount = field("TotalFilteredCount")

    @cached_property
    def ResolverQueryLogConfigs(self):  # pragma: no cover
        return ResolverQueryLogConfig.make_many(
            self.boto3_raw_data["ResolverQueryLogConfigs"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResolverQueryLogConfigsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResolverQueryLogConfigsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateResolverRuleRequest:
    boto3_raw_data: "type_defs.CreateResolverRuleRequestTypeDef" = dataclasses.field()

    CreatorRequestId = field("CreatorRequestId")
    RuleType = field("RuleType")
    Name = field("Name")
    DomainName = field("DomainName")

    @cached_property
    def TargetIps(self):  # pragma: no cover
        return TargetAddress.make_many(self.boto3_raw_data["TargetIps"])

    ResolverEndpointId = field("ResolverEndpointId")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    DelegationRecord = field("DelegationRecord")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateResolverRuleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateResolverRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResolverRuleConfig:
    boto3_raw_data: "type_defs.ResolverRuleConfigTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def TargetIps(self):  # pragma: no cover
        return TargetAddress.make_many(self.boto3_raw_data["TargetIps"])

    ResolverEndpointId = field("ResolverEndpointId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResolverRuleConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResolverRuleConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResolverRule:
    boto3_raw_data: "type_defs.ResolverRuleTypeDef" = dataclasses.field()

    Id = field("Id")
    CreatorRequestId = field("CreatorRequestId")
    Arn = field("Arn")
    DomainName = field("DomainName")
    Status = field("Status")
    StatusMessage = field("StatusMessage")
    RuleType = field("RuleType")
    Name = field("Name")

    @cached_property
    def TargetIps(self):  # pragma: no cover
        return TargetAddress.make_many(self.boto3_raw_data["TargetIps"])

    ResolverEndpointId = field("ResolverEndpointId")
    OwnerId = field("OwnerId")
    ShareStatus = field("ShareStatus")
    CreationTime = field("CreationTime")
    ModificationTime = field("ModificationTime")
    DelegationRecord = field("DelegationRecord")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResolverRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResolverRuleTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResolverDnssecConfigsRequest:
    boto3_raw_data: "type_defs.ListResolverDnssecConfigsRequestTypeDef" = (
        dataclasses.field()
    )

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListResolverDnssecConfigsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResolverDnssecConfigsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResolverEndpointsRequest:
    boto3_raw_data: "type_defs.ListResolverEndpointsRequestTypeDef" = (
        dataclasses.field()
    )

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListResolverEndpointsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResolverEndpointsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResolverQueryLogConfigAssociationsRequest:
    boto3_raw_data: "type_defs.ListResolverQueryLogConfigAssociationsRequestTypeDef" = (
        dataclasses.field()
    )

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    SortBy = field("SortBy")
    SortOrder = field("SortOrder")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResolverQueryLogConfigAssociationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResolverQueryLogConfigAssociationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResolverQueryLogConfigsRequest:
    boto3_raw_data: "type_defs.ListResolverQueryLogConfigsRequestTypeDef" = (
        dataclasses.field()
    )

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    SortBy = field("SortBy")
    SortOrder = field("SortOrder")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResolverQueryLogConfigsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResolverQueryLogConfigsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResolverRuleAssociationsRequest:
    boto3_raw_data: "type_defs.ListResolverRuleAssociationsRequestTypeDef" = (
        dataclasses.field()
    )

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResolverRuleAssociationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResolverRuleAssociationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResolverRulesRequest:
    boto3_raw_data: "type_defs.ListResolverRulesRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListResolverRulesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResolverRulesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFirewallConfigResponse:
    boto3_raw_data: "type_defs.GetFirewallConfigResponseTypeDef" = dataclasses.field()

    @cached_property
    def FirewallConfig(self):  # pragma: no cover
        return FirewallConfig.make_one(self.boto3_raw_data["FirewallConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFirewallConfigResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFirewallConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFirewallConfigsResponse:
    boto3_raw_data: "type_defs.ListFirewallConfigsResponseTypeDef" = dataclasses.field()

    @cached_property
    def FirewallConfigs(self):  # pragma: no cover
        return FirewallConfig.make_many(self.boto3_raw_data["FirewallConfigs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFirewallConfigsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFirewallConfigsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFirewallConfigResponse:
    boto3_raw_data: "type_defs.UpdateFirewallConfigResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FirewallConfig(self):  # pragma: no cover
        return FirewallConfig.make_one(self.boto3_raw_data["FirewallConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFirewallConfigResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFirewallConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFirewallDomainListsResponse:
    boto3_raw_data: "type_defs.ListFirewallDomainListsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FirewallDomainLists(self):  # pragma: no cover
        return FirewallDomainListMetadata.make_many(
            self.boto3_raw_data["FirewallDomainLists"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListFirewallDomainListsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFirewallDomainListsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFirewallRuleGroupsResponse:
    boto3_raw_data: "type_defs.ListFirewallRuleGroupsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FirewallRuleGroups(self):  # pragma: no cover
        return FirewallRuleGroupMetadata.make_many(
            self.boto3_raw_data["FirewallRuleGroups"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListFirewallRuleGroupsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFirewallRuleGroupsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResolverConfigResponse:
    boto3_raw_data: "type_defs.GetResolverConfigResponseTypeDef" = dataclasses.field()

    @cached_property
    def ResolverConfig(self):  # pragma: no cover
        return ResolverConfig.make_one(self.boto3_raw_data["ResolverConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResolverConfigResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResolverConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResolverConfigsResponse:
    boto3_raw_data: "type_defs.ListResolverConfigsResponseTypeDef" = dataclasses.field()

    @cached_property
    def ResolverConfigs(self):  # pragma: no cover
        return ResolverConfig.make_many(self.boto3_raw_data["ResolverConfigs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListResolverConfigsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResolverConfigsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateResolverConfigResponse:
    boto3_raw_data: "type_defs.UpdateResolverConfigResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ResolverConfig(self):  # pragma: no cover
        return ResolverConfig.make_one(self.boto3_raw_data["ResolverConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateResolverConfigResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateResolverConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResolverDnssecConfigResponse:
    boto3_raw_data: "type_defs.GetResolverDnssecConfigResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ResolverDNSSECConfig(self):  # pragma: no cover
        return ResolverDnssecConfig.make_one(
            self.boto3_raw_data["ResolverDNSSECConfig"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetResolverDnssecConfigResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResolverDnssecConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResolverDnssecConfigsResponse:
    boto3_raw_data: "type_defs.ListResolverDnssecConfigsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ResolverDnssecConfigs(self):  # pragma: no cover
        return ResolverDnssecConfig.make_many(
            self.boto3_raw_data["ResolverDnssecConfigs"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResolverDnssecConfigsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResolverDnssecConfigsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateResolverDnssecConfigResponse:
    boto3_raw_data: "type_defs.UpdateResolverDnssecConfigResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ResolverDNSSECConfig(self):  # pragma: no cover
        return ResolverDnssecConfig.make_one(
            self.boto3_raw_data["ResolverDNSSECConfig"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateResolverDnssecConfigResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateResolverDnssecConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResolverEndpointIpAddressesResponse:
    boto3_raw_data: "type_defs.ListResolverEndpointIpAddressesResponseTypeDef" = (
        dataclasses.field()
    )

    MaxResults = field("MaxResults")

    @cached_property
    def IpAddresses(self):  # pragma: no cover
        return IpAddressResponse.make_many(self.boto3_raw_data["IpAddresses"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResolverEndpointIpAddressesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResolverEndpointIpAddressesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFirewallConfigsRequestPaginate:
    boto3_raw_data: "type_defs.ListFirewallConfigsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListFirewallConfigsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFirewallConfigsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFirewallDomainListsRequestPaginate:
    boto3_raw_data: "type_defs.ListFirewallDomainListsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListFirewallDomainListsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFirewallDomainListsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFirewallDomainsRequestPaginate:
    boto3_raw_data: "type_defs.ListFirewallDomainsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    FirewallDomainListId = field("FirewallDomainListId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListFirewallDomainsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFirewallDomainsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFirewallRuleGroupAssociationsRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListFirewallRuleGroupAssociationsRequestPaginateTypeDef"
    ) = dataclasses.field()

    FirewallRuleGroupId = field("FirewallRuleGroupId")
    VpcId = field("VpcId")
    Priority = field("Priority")
    Status = field("Status")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListFirewallRuleGroupAssociationsRequestPaginateTypeDef"
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
                "type_defs.ListFirewallRuleGroupAssociationsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFirewallRuleGroupsRequestPaginate:
    boto3_raw_data: "type_defs.ListFirewallRuleGroupsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListFirewallRuleGroupsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFirewallRuleGroupsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFirewallRulesRequestPaginate:
    boto3_raw_data: "type_defs.ListFirewallRulesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    FirewallRuleGroupId = field("FirewallRuleGroupId")
    Priority = field("Priority")
    Action = field("Action")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListFirewallRulesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFirewallRulesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOutpostResolversRequestPaginate:
    boto3_raw_data: "type_defs.ListOutpostResolversRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    OutpostArn = field("OutpostArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListOutpostResolversRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOutpostResolversRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResolverConfigsRequestPaginate:
    boto3_raw_data: "type_defs.ListResolverConfigsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResolverConfigsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResolverConfigsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResolverDnssecConfigsRequestPaginate:
    boto3_raw_data: "type_defs.ListResolverDnssecConfigsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResolverDnssecConfigsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResolverDnssecConfigsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResolverEndpointIpAddressesRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListResolverEndpointIpAddressesRequestPaginateTypeDef"
    ) = dataclasses.field()

    ResolverEndpointId = field("ResolverEndpointId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResolverEndpointIpAddressesRequestPaginateTypeDef"
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
                "type_defs.ListResolverEndpointIpAddressesRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResolverEndpointsRequestPaginate:
    boto3_raw_data: "type_defs.ListResolverEndpointsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResolverEndpointsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResolverEndpointsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResolverQueryLogConfigAssociationsRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListResolverQueryLogConfigAssociationsRequestPaginateTypeDef"
    ) = dataclasses.field()

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    SortBy = field("SortBy")
    SortOrder = field("SortOrder")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResolverQueryLogConfigAssociationsRequestPaginateTypeDef"
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
                "type_defs.ListResolverQueryLogConfigAssociationsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResolverQueryLogConfigsRequestPaginate:
    boto3_raw_data: "type_defs.ListResolverQueryLogConfigsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    SortBy = field("SortBy")
    SortOrder = field("SortOrder")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResolverQueryLogConfigsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResolverQueryLogConfigsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResolverRuleAssociationsRequestPaginate:
    boto3_raw_data: "type_defs.ListResolverRuleAssociationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResolverRuleAssociationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResolverRuleAssociationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResolverRulesRequestPaginate:
    boto3_raw_data: "type_defs.ListResolverRulesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListResolverRulesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResolverRulesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceRequestPaginate:
    boto3_raw_data: "type_defs.ListTagsForResourceRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ResourceArn = field("ResourceArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTagsForResourceRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateResolverEndpointRequest:
    boto3_raw_data: "type_defs.UpdateResolverEndpointRequestTypeDef" = (
        dataclasses.field()
    )

    ResolverEndpointId = field("ResolverEndpointId")
    Name = field("Name")
    ResolverEndpointType = field("ResolverEndpointType")

    @cached_property
    def UpdateIpAddresses(self):  # pragma: no cover
        return UpdateIpAddress.make_many(self.boto3_raw_data["UpdateIpAddresses"])

    Protocols = field("Protocols")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateResolverEndpointRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateResolverEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateResolverRuleRequest:
    boto3_raw_data: "type_defs.UpdateResolverRuleRequestTypeDef" = dataclasses.field()

    ResolverRuleId = field("ResolverRuleId")

    @cached_property
    def Config(self):  # pragma: no cover
        return ResolverRuleConfig.make_one(self.boto3_raw_data["Config"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateResolverRuleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateResolverRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateResolverRuleResponse:
    boto3_raw_data: "type_defs.CreateResolverRuleResponseTypeDef" = dataclasses.field()

    @cached_property
    def ResolverRule(self):  # pragma: no cover
        return ResolverRule.make_one(self.boto3_raw_data["ResolverRule"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateResolverRuleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateResolverRuleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteResolverRuleResponse:
    boto3_raw_data: "type_defs.DeleteResolverRuleResponseTypeDef" = dataclasses.field()

    @cached_property
    def ResolverRule(self):  # pragma: no cover
        return ResolverRule.make_one(self.boto3_raw_data["ResolverRule"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteResolverRuleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteResolverRuleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResolverRuleResponse:
    boto3_raw_data: "type_defs.GetResolverRuleResponseTypeDef" = dataclasses.field()

    @cached_property
    def ResolverRule(self):  # pragma: no cover
        return ResolverRule.make_one(self.boto3_raw_data["ResolverRule"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResolverRuleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResolverRuleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResolverRulesResponse:
    boto3_raw_data: "type_defs.ListResolverRulesResponseTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")

    @cached_property
    def ResolverRules(self):  # pragma: no cover
        return ResolverRule.make_many(self.boto3_raw_data["ResolverRules"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListResolverRulesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResolverRulesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateResolverRuleResponse:
    boto3_raw_data: "type_defs.UpdateResolverRuleResponseTypeDef" = dataclasses.field()

    @cached_property
    def ResolverRule(self):  # pragma: no cover
        return ResolverRule.make_one(self.boto3_raw_data["ResolverRule"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateResolverRuleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateResolverRuleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]

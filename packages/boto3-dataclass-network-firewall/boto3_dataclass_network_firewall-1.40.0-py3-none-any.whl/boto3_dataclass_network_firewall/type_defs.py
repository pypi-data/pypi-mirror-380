# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_network_firewall import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class Attachment:
    boto3_raw_data: "type_defs.AttachmentTypeDef" = dataclasses.field()

    SubnetId = field("SubnetId")
    EndpointId = field("EndpointId")
    Status = field("Status")
    StatusMessage = field("StatusMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AttachmentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AttachmentTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AcceptNetworkFirewallTransitGatewayAttachmentRequest:
    boto3_raw_data: (
        "type_defs.AcceptNetworkFirewallTransitGatewayAttachmentRequestTypeDef"
    ) = dataclasses.field()

    TransitGatewayAttachmentId = field("TransitGatewayAttachmentId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AcceptNetworkFirewallTransitGatewayAttachmentRequestTypeDef"
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
                "type_defs.AcceptNetworkFirewallTransitGatewayAttachmentRequestTypeDef"
            ]
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
class Address:
    boto3_raw_data: "type_defs.AddressTypeDef" = dataclasses.field()

    AddressDefinition = field("AddressDefinition")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AddressTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AddressTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalysisReport:
    boto3_raw_data: "type_defs.AnalysisReportTypeDef" = dataclasses.field()

    AnalysisReportId = field("AnalysisReportId")
    AnalysisType = field("AnalysisType")
    ReportTime = field("ReportTime")
    Status = field("Status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AnalysisReportTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AnalysisReportTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalysisResult:
    boto3_raw_data: "type_defs.AnalysisResultTypeDef" = dataclasses.field()

    IdentifiedRuleIds = field("IdentifiedRuleIds")
    IdentifiedType = field("IdentifiedType")
    AnalysisDetail = field("AnalysisDetail")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AnalysisResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AnalysisResultTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Hits:
    boto3_raw_data: "type_defs.HitsTypeDef" = dataclasses.field()

    Count = field("Count")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HitsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HitsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UniqueSources:
    boto3_raw_data: "type_defs.UniqueSourcesTypeDef" = dataclasses.field()

    Count = field("Count")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UniqueSourcesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UniqueSourcesTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AvailabilityZoneMapping:
    boto3_raw_data: "type_defs.AvailabilityZoneMappingTypeDef" = dataclasses.field()

    AvailabilityZone = field("AvailabilityZone")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AvailabilityZoneMappingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AvailabilityZoneMappingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateFirewallPolicyRequest:
    boto3_raw_data: "type_defs.AssociateFirewallPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    FirewallPolicyArn = field("FirewallPolicyArn")
    UpdateToken = field("UpdateToken")
    FirewallArn = field("FirewallArn")
    FirewallName = field("FirewallName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssociateFirewallPolicyRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateFirewallPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubnetMapping:
    boto3_raw_data: "type_defs.SubnetMappingTypeDef" = dataclasses.field()

    SubnetId = field("SubnetId")
    IPAddressType = field("IPAddressType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SubnetMappingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SubnetMappingTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AvailabilityZoneMetadata:
    boto3_raw_data: "type_defs.AvailabilityZoneMetadataTypeDef" = dataclasses.field()

    IPAddressType = field("IPAddressType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AvailabilityZoneMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AvailabilityZoneMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IPSetMetadata:
    boto3_raw_data: "type_defs.IPSetMetadataTypeDef" = dataclasses.field()

    ResolvedCIDRCount = field("ResolvedCIDRCount")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IPSetMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IPSetMetadataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CheckCertificateRevocationStatusActions:
    boto3_raw_data: "type_defs.CheckCertificateRevocationStatusActionsTypeDef" = (
        dataclasses.field()
    )

    RevokedStatusAction = field("RevokedStatusAction")
    UnknownStatusAction = field("UnknownStatusAction")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CheckCertificateRevocationStatusActionsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CheckCertificateRevocationStatusActionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EncryptionConfiguration:
    boto3_raw_data: "type_defs.EncryptionConfigurationTypeDef" = dataclasses.field()

    Type = field("Type")
    KeyId = field("KeyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EncryptionConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EncryptionConfigurationTypeDef"]
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
class SourceMetadata:
    boto3_raw_data: "type_defs.SourceMetadataTypeDef" = dataclasses.field()

    SourceArn = field("SourceArn")
    SourceUpdateToken = field("SourceUpdateToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SourceMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SourceMetadataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFirewallPolicyRequest:
    boto3_raw_data: "type_defs.DeleteFirewallPolicyRequestTypeDef" = dataclasses.field()

    FirewallPolicyName = field("FirewallPolicyName")
    FirewallPolicyArn = field("FirewallPolicyArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteFirewallPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFirewallPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFirewallRequest:
    boto3_raw_data: "type_defs.DeleteFirewallRequestTypeDef" = dataclasses.field()

    FirewallName = field("FirewallName")
    FirewallArn = field("FirewallArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteFirewallRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFirewallRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteNetworkFirewallTransitGatewayAttachmentRequest:
    boto3_raw_data: (
        "type_defs.DeleteNetworkFirewallTransitGatewayAttachmentRequestTypeDef"
    ) = dataclasses.field()

    TransitGatewayAttachmentId = field("TransitGatewayAttachmentId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteNetworkFirewallTransitGatewayAttachmentRequestTypeDef"
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
                "type_defs.DeleteNetworkFirewallTransitGatewayAttachmentRequestTypeDef"
            ]
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
class DeleteRuleGroupRequest:
    boto3_raw_data: "type_defs.DeleteRuleGroupRequestTypeDef" = dataclasses.field()

    RuleGroupName = field("RuleGroupName")
    RuleGroupArn = field("RuleGroupArn")
    Type = field("Type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteRuleGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRuleGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTLSInspectionConfigurationRequest:
    boto3_raw_data: "type_defs.DeleteTLSInspectionConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    TLSInspectionConfigurationArn = field("TLSInspectionConfigurationArn")
    TLSInspectionConfigurationName = field("TLSInspectionConfigurationName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteTLSInspectionConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTLSInspectionConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVpcEndpointAssociationRequest:
    boto3_raw_data: "type_defs.DeleteVpcEndpointAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    VpcEndpointAssociationArn = field("VpcEndpointAssociationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteVpcEndpointAssociationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVpcEndpointAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFirewallMetadataRequest:
    boto3_raw_data: "type_defs.DescribeFirewallMetadataRequestTypeDef" = (
        dataclasses.field()
    )

    FirewallArn = field("FirewallArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeFirewallMetadataRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFirewallMetadataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFirewallPolicyRequest:
    boto3_raw_data: "type_defs.DescribeFirewallPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    FirewallPolicyName = field("FirewallPolicyName")
    FirewallPolicyArn = field("FirewallPolicyArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeFirewallPolicyRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFirewallPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFirewallRequest:
    boto3_raw_data: "type_defs.DescribeFirewallRequestTypeDef" = dataclasses.field()

    FirewallName = field("FirewallName")
    FirewallArn = field("FirewallArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeFirewallRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFirewallRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFlowOperationRequest:
    boto3_raw_data: "type_defs.DescribeFlowOperationRequestTypeDef" = (
        dataclasses.field()
    )

    FirewallArn = field("FirewallArn")
    FlowOperationId = field("FlowOperationId")
    AvailabilityZone = field("AvailabilityZone")
    VpcEndpointAssociationArn = field("VpcEndpointAssociationArn")
    VpcEndpointId = field("VpcEndpointId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeFlowOperationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFlowOperationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLoggingConfigurationRequest:
    boto3_raw_data: "type_defs.DescribeLoggingConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    FirewallArn = field("FirewallArn")
    FirewallName = field("FirewallName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeLoggingConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLoggingConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeResourcePolicyRequest:
    boto3_raw_data: "type_defs.DescribeResourcePolicyRequestTypeDef" = (
        dataclasses.field()
    )

    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeResourcePolicyRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeResourcePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRuleGroupMetadataRequest:
    boto3_raw_data: "type_defs.DescribeRuleGroupMetadataRequestTypeDef" = (
        dataclasses.field()
    )

    RuleGroupName = field("RuleGroupName")
    RuleGroupArn = field("RuleGroupArn")
    Type = field("Type")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeRuleGroupMetadataRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRuleGroupMetadataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StatefulRuleOptions:
    boto3_raw_data: "type_defs.StatefulRuleOptionsTypeDef" = dataclasses.field()

    RuleOrder = field("RuleOrder")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StatefulRuleOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StatefulRuleOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRuleGroupRequest:
    boto3_raw_data: "type_defs.DescribeRuleGroupRequestTypeDef" = dataclasses.field()

    RuleGroupName = field("RuleGroupName")
    RuleGroupArn = field("RuleGroupArn")
    Type = field("Type")
    AnalyzeRuleGroup = field("AnalyzeRuleGroup")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeRuleGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRuleGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRuleGroupSummaryRequest:
    boto3_raw_data: "type_defs.DescribeRuleGroupSummaryRequestTypeDef" = (
        dataclasses.field()
    )

    RuleGroupName = field("RuleGroupName")
    RuleGroupArn = field("RuleGroupArn")
    Type = field("Type")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeRuleGroupSummaryRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRuleGroupSummaryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTLSInspectionConfigurationRequest:
    boto3_raw_data: "type_defs.DescribeTLSInspectionConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    TLSInspectionConfigurationArn = field("TLSInspectionConfigurationArn")
    TLSInspectionConfigurationName = field("TLSInspectionConfigurationName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeTLSInspectionConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTLSInspectionConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeVpcEndpointAssociationRequest:
    boto3_raw_data: "type_defs.DescribeVpcEndpointAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    VpcEndpointAssociationArn = field("VpcEndpointAssociationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeVpcEndpointAssociationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeVpcEndpointAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Dimension:
    boto3_raw_data: "type_defs.DimensionTypeDef" = dataclasses.field()

    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DimensionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DimensionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateSubnetsRequest:
    boto3_raw_data: "type_defs.DisassociateSubnetsRequestTypeDef" = dataclasses.field()

    SubnetIds = field("SubnetIds")
    UpdateToken = field("UpdateToken")
    FirewallArn = field("FirewallArn")
    FirewallName = field("FirewallName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisassociateSubnetsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateSubnetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FirewallMetadata:
    boto3_raw_data: "type_defs.FirewallMetadataTypeDef" = dataclasses.field()

    FirewallName = field("FirewallName")
    FirewallArn = field("FirewallArn")
    TransitGatewayAttachmentId = field("TransitGatewayAttachmentId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FirewallMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FirewallMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FirewallPolicyMetadata:
    boto3_raw_data: "type_defs.FirewallPolicyMetadataTypeDef" = dataclasses.field()

    Name = field("Name")
    Arn = field("Arn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FirewallPolicyMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FirewallPolicyMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StatelessRuleGroupReference:
    boto3_raw_data: "type_defs.StatelessRuleGroupReferenceTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    Priority = field("Priority")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StatelessRuleGroupReferenceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StatelessRuleGroupReferenceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TransitGatewayAttachmentSyncState:
    boto3_raw_data: "type_defs.TransitGatewayAttachmentSyncStateTypeDef" = (
        dataclasses.field()
    )

    AttachmentId = field("AttachmentId")
    TransitGatewayAttachmentStatus = field("TransitGatewayAttachmentStatus")
    StatusMessage = field("StatusMessage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TransitGatewayAttachmentSyncStateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TransitGatewayAttachmentSyncStateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlowOperationMetadata:
    boto3_raw_data: "type_defs.FlowOperationMetadataTypeDef" = dataclasses.field()

    FlowOperationId = field("FlowOperationId")
    FlowOperationType = field("FlowOperationType")
    FlowRequestTimestamp = field("FlowRequestTimestamp")
    FlowOperationStatus = field("FlowOperationStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FlowOperationMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FlowOperationMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlowTimeouts:
    boto3_raw_data: "type_defs.FlowTimeoutsTypeDef" = dataclasses.field()

    TcpIdleTimeoutSeconds = field("TcpIdleTimeoutSeconds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FlowTimeoutsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FlowTimeoutsTypeDef"]],
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
class GetAnalysisReportResultsRequest:
    boto3_raw_data: "type_defs.GetAnalysisReportResultsRequestTypeDef" = (
        dataclasses.field()
    )

    AnalysisReportId = field("AnalysisReportId")
    FirewallName = field("FirewallName")
    FirewallArn = field("FirewallArn")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetAnalysisReportResultsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAnalysisReportResultsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Header:
    boto3_raw_data: "type_defs.HeaderTypeDef" = dataclasses.field()

    Protocol = field("Protocol")
    Source = field("Source")
    SourcePort = field("SourcePort")
    Direction = field("Direction")
    Destination = field("Destination")
    DestinationPort = field("DestinationPort")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HeaderTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HeaderTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IPSetOutput:
    boto3_raw_data: "type_defs.IPSetOutputTypeDef" = dataclasses.field()

    Definition = field("Definition")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IPSetOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IPSetOutputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IPSetReference:
    boto3_raw_data: "type_defs.IPSetReferenceTypeDef" = dataclasses.field()

    ReferenceArn = field("ReferenceArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IPSetReferenceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IPSetReferenceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IPSet:
    boto3_raw_data: "type_defs.IPSetTypeDef" = dataclasses.field()

    Definition = field("Definition")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IPSetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IPSetTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAnalysisReportsRequest:
    boto3_raw_data: "type_defs.ListAnalysisReportsRequestTypeDef" = dataclasses.field()

    FirewallName = field("FirewallName")
    FirewallArn = field("FirewallArn")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAnalysisReportsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAnalysisReportsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFirewallPoliciesRequest:
    boto3_raw_data: "type_defs.ListFirewallPoliciesRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFirewallPoliciesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFirewallPoliciesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFirewallsRequest:
    boto3_raw_data: "type_defs.ListFirewallsRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    VpcIds = field("VpcIds")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFirewallsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFirewallsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFlowOperationResultsRequest:
    boto3_raw_data: "type_defs.ListFlowOperationResultsRequestTypeDef" = (
        dataclasses.field()
    )

    FirewallArn = field("FirewallArn")
    FlowOperationId = field("FlowOperationId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    AvailabilityZone = field("AvailabilityZone")
    VpcEndpointId = field("VpcEndpointId")
    VpcEndpointAssociationArn = field("VpcEndpointAssociationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListFlowOperationResultsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFlowOperationResultsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFlowOperationsRequest:
    boto3_raw_data: "type_defs.ListFlowOperationsRequestTypeDef" = dataclasses.field()

    FirewallArn = field("FirewallArn")
    AvailabilityZone = field("AvailabilityZone")
    VpcEndpointAssociationArn = field("VpcEndpointAssociationArn")
    VpcEndpointId = field("VpcEndpointId")
    FlowOperationType = field("FlowOperationType")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFlowOperationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFlowOperationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRuleGroupsRequest:
    boto3_raw_data: "type_defs.ListRuleGroupsRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    Scope = field("Scope")
    ManagedType = field("ManagedType")
    Type = field("Type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRuleGroupsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRuleGroupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleGroupMetadata:
    boto3_raw_data: "type_defs.RuleGroupMetadataTypeDef" = dataclasses.field()

    Name = field("Name")
    Arn = field("Arn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleGroupMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuleGroupMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTLSInspectionConfigurationsRequest:
    boto3_raw_data: "type_defs.ListTLSInspectionConfigurationsRequestTypeDef" = (
        dataclasses.field()
    )

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTLSInspectionConfigurationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTLSInspectionConfigurationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TLSInspectionConfigurationMetadata:
    boto3_raw_data: "type_defs.TLSInspectionConfigurationMetadataTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Arn = field("Arn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TLSInspectionConfigurationMetadataTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TLSInspectionConfigurationMetadataTypeDef"]
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
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

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
class ListVpcEndpointAssociationsRequest:
    boto3_raw_data: "type_defs.ListVpcEndpointAssociationsRequestTypeDef" = (
        dataclasses.field()
    )

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    FirewallArn = field("FirewallArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListVpcEndpointAssociationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVpcEndpointAssociationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcEndpointAssociationMetadata:
    boto3_raw_data: "type_defs.VpcEndpointAssociationMetadataTypeDef" = (
        dataclasses.field()
    )

    VpcEndpointAssociationArn = field("VpcEndpointAssociationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.VpcEndpointAssociationMetadataTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcEndpointAssociationMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LogDestinationConfigOutput:
    boto3_raw_data: "type_defs.LogDestinationConfigOutputTypeDef" = dataclasses.field()

    LogType = field("LogType")
    LogDestinationType = field("LogDestinationType")
    LogDestination = field("LogDestination")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LogDestinationConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LogDestinationConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LogDestinationConfig:
    boto3_raw_data: "type_defs.LogDestinationConfigTypeDef" = dataclasses.field()

    LogType = field("LogType")
    LogDestinationType = field("LogDestinationType")
    LogDestination = field("LogDestination")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LogDestinationConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LogDestinationConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PortRange:
    boto3_raw_data: "type_defs.PortRangeTypeDef" = dataclasses.field()

    FromPort = field("FromPort")
    ToPort = field("ToPort")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PortRangeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PortRangeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TCPFlagFieldOutput:
    boto3_raw_data: "type_defs.TCPFlagFieldOutputTypeDef" = dataclasses.field()

    Flags = field("Flags")
    Masks = field("Masks")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TCPFlagFieldOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TCPFlagFieldOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TCPFlagField:
    boto3_raw_data: "type_defs.TCPFlagFieldTypeDef" = dataclasses.field()

    Flags = field("Flags")
    Masks = field("Masks")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TCPFlagFieldTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TCPFlagFieldTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PerObjectStatus:
    boto3_raw_data: "type_defs.PerObjectStatusTypeDef" = dataclasses.field()

    SyncStatus = field("SyncStatus")
    UpdateToken = field("UpdateToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PerObjectStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PerObjectStatusTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PortSetOutput:
    boto3_raw_data: "type_defs.PortSetOutputTypeDef" = dataclasses.field()

    Definition = field("Definition")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PortSetOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PortSetOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PortSet:
    boto3_raw_data: "type_defs.PortSetTypeDef" = dataclasses.field()

    Definition = field("Definition")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PortSetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PortSetTypeDef"]]
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
class RejectNetworkFirewallTransitGatewayAttachmentRequest:
    boto3_raw_data: (
        "type_defs.RejectNetworkFirewallTransitGatewayAttachmentRequestTypeDef"
    ) = dataclasses.field()

    TransitGatewayAttachmentId = field("TransitGatewayAttachmentId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RejectNetworkFirewallTransitGatewayAttachmentRequestTypeDef"
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
                "type_defs.RejectNetworkFirewallTransitGatewayAttachmentRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SummaryConfigurationOutput:
    boto3_raw_data: "type_defs.SummaryConfigurationOutputTypeDef" = dataclasses.field()

    RuleOptions = field("RuleOptions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SummaryConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SummaryConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleOptionOutput:
    boto3_raw_data: "type_defs.RuleOptionOutputTypeDef" = dataclasses.field()

    Keyword = field("Keyword")
    Settings = field("Settings")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleOptionOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuleOptionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleOption:
    boto3_raw_data: "type_defs.RuleOptionTypeDef" = dataclasses.field()

    Keyword = field("Keyword")
    Settings = field("Settings")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleOptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuleOptionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleSummary:
    boto3_raw_data: "type_defs.RuleSummaryTypeDef" = dataclasses.field()

    SID = field("SID")
    Msg = field("Msg")
    Metadata = field("Metadata")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuleSummaryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RulesSourceListOutput:
    boto3_raw_data: "type_defs.RulesSourceListOutputTypeDef" = dataclasses.field()

    Targets = field("Targets")
    TargetTypes = field("TargetTypes")
    GeneratedRulesType = field("GeneratedRulesType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RulesSourceListOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RulesSourceListOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RulesSourceList:
    boto3_raw_data: "type_defs.RulesSourceListTypeDef" = dataclasses.field()

    Targets = field("Targets")
    TargetTypes = field("TargetTypes")
    GeneratedRulesType = field("GeneratedRulesType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RulesSourceListTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RulesSourceListTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServerCertificate:
    boto3_raw_data: "type_defs.ServerCertificateTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServerCertificateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServerCertificateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartAnalysisReportRequest:
    boto3_raw_data: "type_defs.StartAnalysisReportRequestTypeDef" = dataclasses.field()

    AnalysisType = field("AnalysisType")
    FirewallName = field("FirewallName")
    FirewallArn = field("FirewallArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartAnalysisReportRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartAnalysisReportRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StatefulRuleGroupOverride:
    boto3_raw_data: "type_defs.StatefulRuleGroupOverrideTypeDef" = dataclasses.field()

    Action = field("Action")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StatefulRuleGroupOverrideTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StatefulRuleGroupOverrideTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SummaryConfiguration:
    boto3_raw_data: "type_defs.SummaryConfigurationTypeDef" = dataclasses.field()

    RuleOptions = field("RuleOptions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SummaryConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SummaryConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TlsCertificateData:
    boto3_raw_data: "type_defs.TlsCertificateDataTypeDef" = dataclasses.field()

    CertificateArn = field("CertificateArn")
    CertificateSerial = field("CertificateSerial")
    Status = field("Status")
    StatusMessage = field("StatusMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TlsCertificateDataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TlsCertificateDataTypeDef"]
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
class UpdateAvailabilityZoneChangeProtectionRequest:
    boto3_raw_data: "type_defs.UpdateAvailabilityZoneChangeProtectionRequestTypeDef" = (
        dataclasses.field()
    )

    AvailabilityZoneChangeProtection = field("AvailabilityZoneChangeProtection")
    UpdateToken = field("UpdateToken")
    FirewallArn = field("FirewallArn")
    FirewallName = field("FirewallName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateAvailabilityZoneChangeProtectionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAvailabilityZoneChangeProtectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFirewallAnalysisSettingsRequest:
    boto3_raw_data: "type_defs.UpdateFirewallAnalysisSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    EnabledAnalysisTypes = field("EnabledAnalysisTypes")
    FirewallArn = field("FirewallArn")
    FirewallName = field("FirewallName")
    UpdateToken = field("UpdateToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateFirewallAnalysisSettingsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFirewallAnalysisSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFirewallDeleteProtectionRequest:
    boto3_raw_data: "type_defs.UpdateFirewallDeleteProtectionRequestTypeDef" = (
        dataclasses.field()
    )

    DeleteProtection = field("DeleteProtection")
    UpdateToken = field("UpdateToken")
    FirewallArn = field("FirewallArn")
    FirewallName = field("FirewallName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateFirewallDeleteProtectionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFirewallDeleteProtectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFirewallDescriptionRequest:
    boto3_raw_data: "type_defs.UpdateFirewallDescriptionRequestTypeDef" = (
        dataclasses.field()
    )

    UpdateToken = field("UpdateToken")
    FirewallArn = field("FirewallArn")
    FirewallName = field("FirewallName")
    Description = field("Description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateFirewallDescriptionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFirewallDescriptionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFirewallPolicyChangeProtectionRequest:
    boto3_raw_data: "type_defs.UpdateFirewallPolicyChangeProtectionRequestTypeDef" = (
        dataclasses.field()
    )

    FirewallPolicyChangeProtection = field("FirewallPolicyChangeProtection")
    UpdateToken = field("UpdateToken")
    FirewallArn = field("FirewallArn")
    FirewallName = field("FirewallName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateFirewallPolicyChangeProtectionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFirewallPolicyChangeProtectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSubnetChangeProtectionRequest:
    boto3_raw_data: "type_defs.UpdateSubnetChangeProtectionRequestTypeDef" = (
        dataclasses.field()
    )

    SubnetChangeProtection = field("SubnetChangeProtection")
    UpdateToken = field("UpdateToken")
    FirewallArn = field("FirewallArn")
    FirewallName = field("FirewallName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateSubnetChangeProtectionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSubnetChangeProtectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AZSyncState:
    boto3_raw_data: "type_defs.AZSyncStateTypeDef" = dataclasses.field()

    @cached_property
    def Attachment(self):  # pragma: no cover
        return Attachment.make_one(self.boto3_raw_data["Attachment"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AZSyncStateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AZSyncStateTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AcceptNetworkFirewallTransitGatewayAttachmentResponse:
    boto3_raw_data: (
        "type_defs.AcceptNetworkFirewallTransitGatewayAttachmentResponseTypeDef"
    ) = dataclasses.field()

    TransitGatewayAttachmentId = field("TransitGatewayAttachmentId")
    TransitGatewayAttachmentStatus = field("TransitGatewayAttachmentStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AcceptNetworkFirewallTransitGatewayAttachmentResponseTypeDef"
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
                "type_defs.AcceptNetworkFirewallTransitGatewayAttachmentResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateFirewallPolicyResponse:
    boto3_raw_data: "type_defs.AssociateFirewallPolicyResponseTypeDef" = (
        dataclasses.field()
    )

    FirewallArn = field("FirewallArn")
    FirewallName = field("FirewallName")
    FirewallPolicyArn = field("FirewallPolicyArn")
    UpdateToken = field("UpdateToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssociateFirewallPolicyResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateFirewallPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteNetworkFirewallTransitGatewayAttachmentResponse:
    boto3_raw_data: (
        "type_defs.DeleteNetworkFirewallTransitGatewayAttachmentResponseTypeDef"
    ) = dataclasses.field()

    TransitGatewayAttachmentId = field("TransitGatewayAttachmentId")
    TransitGatewayAttachmentStatus = field("TransitGatewayAttachmentStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteNetworkFirewallTransitGatewayAttachmentResponseTypeDef"
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
                "type_defs.DeleteNetworkFirewallTransitGatewayAttachmentResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeResourcePolicyResponse:
    boto3_raw_data: "type_defs.DescribeResourcePolicyResponseTypeDef" = (
        dataclasses.field()
    )

    Policy = field("Policy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeResourcePolicyResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeResourcePolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RejectNetworkFirewallTransitGatewayAttachmentResponse:
    boto3_raw_data: (
        "type_defs.RejectNetworkFirewallTransitGatewayAttachmentResponseTypeDef"
    ) = dataclasses.field()

    TransitGatewayAttachmentId = field("TransitGatewayAttachmentId")
    TransitGatewayAttachmentStatus = field("TransitGatewayAttachmentStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RejectNetworkFirewallTransitGatewayAttachmentResponseTypeDef"
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
                "type_defs.RejectNetworkFirewallTransitGatewayAttachmentResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartAnalysisReportResponse:
    boto3_raw_data: "type_defs.StartAnalysisReportResponseTypeDef" = dataclasses.field()

    AnalysisReportId = field("AnalysisReportId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartAnalysisReportResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartAnalysisReportResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartFlowCaptureResponse:
    boto3_raw_data: "type_defs.StartFlowCaptureResponseTypeDef" = dataclasses.field()

    FirewallArn = field("FirewallArn")
    FlowOperationId = field("FlowOperationId")
    FlowOperationStatus = field("FlowOperationStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartFlowCaptureResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartFlowCaptureResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartFlowFlushResponse:
    boto3_raw_data: "type_defs.StartFlowFlushResponseTypeDef" = dataclasses.field()

    FirewallArn = field("FirewallArn")
    FlowOperationId = field("FlowOperationId")
    FlowOperationStatus = field("FlowOperationStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartFlowFlushResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartFlowFlushResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAvailabilityZoneChangeProtectionResponse:
    boto3_raw_data: (
        "type_defs.UpdateAvailabilityZoneChangeProtectionResponseTypeDef"
    ) = dataclasses.field()

    UpdateToken = field("UpdateToken")
    FirewallArn = field("FirewallArn")
    FirewallName = field("FirewallName")
    AvailabilityZoneChangeProtection = field("AvailabilityZoneChangeProtection")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateAvailabilityZoneChangeProtectionResponseTypeDef"
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
                "type_defs.UpdateAvailabilityZoneChangeProtectionResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFirewallAnalysisSettingsResponse:
    boto3_raw_data: "type_defs.UpdateFirewallAnalysisSettingsResponseTypeDef" = (
        dataclasses.field()
    )

    EnabledAnalysisTypes = field("EnabledAnalysisTypes")
    FirewallArn = field("FirewallArn")
    FirewallName = field("FirewallName")
    UpdateToken = field("UpdateToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateFirewallAnalysisSettingsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFirewallAnalysisSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFirewallDeleteProtectionResponse:
    boto3_raw_data: "type_defs.UpdateFirewallDeleteProtectionResponseTypeDef" = (
        dataclasses.field()
    )

    FirewallArn = field("FirewallArn")
    FirewallName = field("FirewallName")
    DeleteProtection = field("DeleteProtection")
    UpdateToken = field("UpdateToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateFirewallDeleteProtectionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFirewallDeleteProtectionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFirewallDescriptionResponse:
    boto3_raw_data: "type_defs.UpdateFirewallDescriptionResponseTypeDef" = (
        dataclasses.field()
    )

    FirewallArn = field("FirewallArn")
    FirewallName = field("FirewallName")
    Description = field("Description")
    UpdateToken = field("UpdateToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateFirewallDescriptionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFirewallDescriptionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFirewallPolicyChangeProtectionResponse:
    boto3_raw_data: "type_defs.UpdateFirewallPolicyChangeProtectionResponseTypeDef" = (
        dataclasses.field()
    )

    UpdateToken = field("UpdateToken")
    FirewallArn = field("FirewallArn")
    FirewallName = field("FirewallName")
    FirewallPolicyChangeProtection = field("FirewallPolicyChangeProtection")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateFirewallPolicyChangeProtectionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFirewallPolicyChangeProtectionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSubnetChangeProtectionResponse:
    boto3_raw_data: "type_defs.UpdateSubnetChangeProtectionResponseTypeDef" = (
        dataclasses.field()
    )

    UpdateToken = field("UpdateToken")
    FirewallArn = field("FirewallArn")
    FirewallName = field("FirewallName")
    SubnetChangeProtection = field("SubnetChangeProtection")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateSubnetChangeProtectionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSubnetChangeProtectionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlowFilterOutput:
    boto3_raw_data: "type_defs.FlowFilterOutputTypeDef" = dataclasses.field()

    @cached_property
    def SourceAddress(self):  # pragma: no cover
        return Address.make_one(self.boto3_raw_data["SourceAddress"])

    @cached_property
    def DestinationAddress(self):  # pragma: no cover
        return Address.make_one(self.boto3_raw_data["DestinationAddress"])

    SourcePort = field("SourcePort")
    DestinationPort = field("DestinationPort")
    Protocols = field("Protocols")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FlowFilterOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FlowFilterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlowFilter:
    boto3_raw_data: "type_defs.FlowFilterTypeDef" = dataclasses.field()

    @cached_property
    def SourceAddress(self):  # pragma: no cover
        return Address.make_one(self.boto3_raw_data["SourceAddress"])

    @cached_property
    def DestinationAddress(self):  # pragma: no cover
        return Address.make_one(self.boto3_raw_data["DestinationAddress"])

    SourcePort = field("SourcePort")
    DestinationPort = field("DestinationPort")
    Protocols = field("Protocols")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FlowFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FlowFilterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Flow:
    boto3_raw_data: "type_defs.FlowTypeDef" = dataclasses.field()

    @cached_property
    def SourceAddress(self):  # pragma: no cover
        return Address.make_one(self.boto3_raw_data["SourceAddress"])

    @cached_property
    def DestinationAddress(self):  # pragma: no cover
        return Address.make_one(self.boto3_raw_data["DestinationAddress"])

    SourcePort = field("SourcePort")
    DestinationPort = field("DestinationPort")
    Protocol = field("Protocol")
    Age = field("Age")
    PacketCount = field("PacketCount")
    ByteCount = field("ByteCount")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FlowTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FlowTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAnalysisReportsResponse:
    boto3_raw_data: "type_defs.ListAnalysisReportsResponseTypeDef" = dataclasses.field()

    @cached_property
    def AnalysisReports(self):  # pragma: no cover
        return AnalysisReport.make_many(self.boto3_raw_data["AnalysisReports"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAnalysisReportsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAnalysisReportsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalysisTypeReportResult:
    boto3_raw_data: "type_defs.AnalysisTypeReportResultTypeDef" = dataclasses.field()

    Protocol = field("Protocol")
    FirstAccessed = field("FirstAccessed")
    LastAccessed = field("LastAccessed")
    Domain = field("Domain")

    @cached_property
    def Hits(self):  # pragma: no cover
        return Hits.make_one(self.boto3_raw_data["Hits"])

    @cached_property
    def UniqueSources(self):  # pragma: no cover
        return UniqueSources.make_one(self.boto3_raw_data["UniqueSources"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalysisTypeReportResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalysisTypeReportResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateAvailabilityZonesRequest:
    boto3_raw_data: "type_defs.AssociateAvailabilityZonesRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AvailabilityZoneMappings(self):  # pragma: no cover
        return AvailabilityZoneMapping.make_many(
            self.boto3_raw_data["AvailabilityZoneMappings"]
        )

    UpdateToken = field("UpdateToken")
    FirewallArn = field("FirewallArn")
    FirewallName = field("FirewallName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateAvailabilityZonesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateAvailabilityZonesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateAvailabilityZonesResponse:
    boto3_raw_data: "type_defs.AssociateAvailabilityZonesResponseTypeDef" = (
        dataclasses.field()
    )

    FirewallArn = field("FirewallArn")
    FirewallName = field("FirewallName")

    @cached_property
    def AvailabilityZoneMappings(self):  # pragma: no cover
        return AvailabilityZoneMapping.make_many(
            self.boto3_raw_data["AvailabilityZoneMappings"]
        )

    UpdateToken = field("UpdateToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateAvailabilityZonesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateAvailabilityZonesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateAvailabilityZonesRequest:
    boto3_raw_data: "type_defs.DisassociateAvailabilityZonesRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AvailabilityZoneMappings(self):  # pragma: no cover
        return AvailabilityZoneMapping.make_many(
            self.boto3_raw_data["AvailabilityZoneMappings"]
        )

    UpdateToken = field("UpdateToken")
    FirewallArn = field("FirewallArn")
    FirewallName = field("FirewallName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateAvailabilityZonesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateAvailabilityZonesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateAvailabilityZonesResponse:
    boto3_raw_data: "type_defs.DisassociateAvailabilityZonesResponseTypeDef" = (
        dataclasses.field()
    )

    FirewallArn = field("FirewallArn")
    FirewallName = field("FirewallName")

    @cached_property
    def AvailabilityZoneMappings(self):  # pragma: no cover
        return AvailabilityZoneMapping.make_many(
            self.boto3_raw_data["AvailabilityZoneMappings"]
        )

    UpdateToken = field("UpdateToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateAvailabilityZonesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateAvailabilityZonesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateSubnetsRequest:
    boto3_raw_data: "type_defs.AssociateSubnetsRequestTypeDef" = dataclasses.field()

    @cached_property
    def SubnetMappings(self):  # pragma: no cover
        return SubnetMapping.make_many(self.boto3_raw_data["SubnetMappings"])

    UpdateToken = field("UpdateToken")
    FirewallArn = field("FirewallArn")
    FirewallName = field("FirewallName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateSubnetsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateSubnetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateSubnetsResponse:
    boto3_raw_data: "type_defs.AssociateSubnetsResponseTypeDef" = dataclasses.field()

    FirewallArn = field("FirewallArn")
    FirewallName = field("FirewallName")

    @cached_property
    def SubnetMappings(self):  # pragma: no cover
        return SubnetMapping.make_many(self.boto3_raw_data["SubnetMappings"])

    UpdateToken = field("UpdateToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateSubnetsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateSubnetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateSubnetsResponse:
    boto3_raw_data: "type_defs.DisassociateSubnetsResponseTypeDef" = dataclasses.field()

    FirewallArn = field("FirewallArn")
    FirewallName = field("FirewallName")

    @cached_property
    def SubnetMappings(self):  # pragma: no cover
        return SubnetMapping.make_many(self.boto3_raw_data["SubnetMappings"])

    UpdateToken = field("UpdateToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisassociateSubnetsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateSubnetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFirewallMetadataResponse:
    boto3_raw_data: "type_defs.DescribeFirewallMetadataResponseTypeDef" = (
        dataclasses.field()
    )

    FirewallArn = field("FirewallArn")
    FirewallPolicyArn = field("FirewallPolicyArn")
    Description = field("Description")
    Status = field("Status")
    SupportedAvailabilityZones = field("SupportedAvailabilityZones")
    TransitGatewayAttachmentId = field("TransitGatewayAttachmentId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeFirewallMetadataResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFirewallMetadataResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CIDRSummary:
    boto3_raw_data: "type_defs.CIDRSummaryTypeDef" = dataclasses.field()

    AvailableCIDRCount = field("AvailableCIDRCount")
    UtilizedCIDRCount = field("UtilizedCIDRCount")
    IPSetReferences = field("IPSetReferences")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CIDRSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CIDRSummaryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFirewallEncryptionConfigurationRequest:
    boto3_raw_data: "type_defs.UpdateFirewallEncryptionConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    UpdateToken = field("UpdateToken")
    FirewallArn = field("FirewallArn")
    FirewallName = field("FirewallName")

    @cached_property
    def EncryptionConfiguration(self):  # pragma: no cover
        return EncryptionConfiguration.make_one(
            self.boto3_raw_data["EncryptionConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateFirewallEncryptionConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFirewallEncryptionConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFirewallEncryptionConfigurationResponse:
    boto3_raw_data: "type_defs.UpdateFirewallEncryptionConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    FirewallArn = field("FirewallArn")
    FirewallName = field("FirewallName")
    UpdateToken = field("UpdateToken")

    @cached_property
    def EncryptionConfiguration(self):  # pragma: no cover
        return EncryptionConfiguration.make_one(
            self.boto3_raw_data["EncryptionConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateFirewallEncryptionConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFirewallEncryptionConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFirewallRequest:
    boto3_raw_data: "type_defs.CreateFirewallRequestTypeDef" = dataclasses.field()

    FirewallName = field("FirewallName")
    FirewallPolicyArn = field("FirewallPolicyArn")
    VpcId = field("VpcId")

    @cached_property
    def SubnetMappings(self):  # pragma: no cover
        return SubnetMapping.make_many(self.boto3_raw_data["SubnetMappings"])

    DeleteProtection = field("DeleteProtection")
    SubnetChangeProtection = field("SubnetChangeProtection")
    FirewallPolicyChangeProtection = field("FirewallPolicyChangeProtection")
    Description = field("Description")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def EncryptionConfiguration(self):  # pragma: no cover
        return EncryptionConfiguration.make_one(
            self.boto3_raw_data["EncryptionConfiguration"]
        )

    EnabledAnalysisTypes = field("EnabledAnalysisTypes")
    TransitGatewayId = field("TransitGatewayId")

    @cached_property
    def AvailabilityZoneMappings(self):  # pragma: no cover
        return AvailabilityZoneMapping.make_many(
            self.boto3_raw_data["AvailabilityZoneMappings"]
        )

    AvailabilityZoneChangeProtection = field("AvailabilityZoneChangeProtection")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFirewallRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFirewallRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVpcEndpointAssociationRequest:
    boto3_raw_data: "type_defs.CreateVpcEndpointAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    FirewallArn = field("FirewallArn")
    VpcId = field("VpcId")

    @cached_property
    def SubnetMapping(self):  # pragma: no cover
        return SubnetMapping.make_one(self.boto3_raw_data["SubnetMapping"])

    Description = field("Description")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateVpcEndpointAssociationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVpcEndpointAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FirewallPolicyResponse:
    boto3_raw_data: "type_defs.FirewallPolicyResponseTypeDef" = dataclasses.field()

    FirewallPolicyName = field("FirewallPolicyName")
    FirewallPolicyArn = field("FirewallPolicyArn")
    FirewallPolicyId = field("FirewallPolicyId")
    Description = field("Description")
    FirewallPolicyStatus = field("FirewallPolicyStatus")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    ConsumedStatelessRuleCapacity = field("ConsumedStatelessRuleCapacity")
    ConsumedStatefulRuleCapacity = field("ConsumedStatefulRuleCapacity")
    NumberOfAssociations = field("NumberOfAssociations")

    @cached_property
    def EncryptionConfiguration(self):  # pragma: no cover
        return EncryptionConfiguration.make_one(
            self.boto3_raw_data["EncryptionConfiguration"]
        )

    LastModifiedTime = field("LastModifiedTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FirewallPolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FirewallPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Firewall:
    boto3_raw_data: "type_defs.FirewallTypeDef" = dataclasses.field()

    FirewallPolicyArn = field("FirewallPolicyArn")
    VpcId = field("VpcId")

    @cached_property
    def SubnetMappings(self):  # pragma: no cover
        return SubnetMapping.make_many(self.boto3_raw_data["SubnetMappings"])

    FirewallId = field("FirewallId")
    FirewallName = field("FirewallName")
    FirewallArn = field("FirewallArn")
    DeleteProtection = field("DeleteProtection")
    SubnetChangeProtection = field("SubnetChangeProtection")
    FirewallPolicyChangeProtection = field("FirewallPolicyChangeProtection")
    Description = field("Description")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def EncryptionConfiguration(self):  # pragma: no cover
        return EncryptionConfiguration.make_one(
            self.boto3_raw_data["EncryptionConfiguration"]
        )

    NumberOfAssociations = field("NumberOfAssociations")
    EnabledAnalysisTypes = field("EnabledAnalysisTypes")
    TransitGatewayId = field("TransitGatewayId")
    TransitGatewayOwnerAccountId = field("TransitGatewayOwnerAccountId")

    @cached_property
    def AvailabilityZoneMappings(self):  # pragma: no cover
        return AvailabilityZoneMapping.make_many(
            self.boto3_raw_data["AvailabilityZoneMappings"]
        )

    AvailabilityZoneChangeProtection = field("AvailabilityZoneChangeProtection")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FirewallTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FirewallTypeDef"]]
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
class VpcEndpointAssociation:
    boto3_raw_data: "type_defs.VpcEndpointAssociationTypeDef" = dataclasses.field()

    VpcEndpointAssociationArn = field("VpcEndpointAssociationArn")
    FirewallArn = field("FirewallArn")
    VpcId = field("VpcId")

    @cached_property
    def SubnetMapping(self):  # pragma: no cover
        return SubnetMapping.make_one(self.boto3_raw_data["SubnetMapping"])

    VpcEndpointAssociationId = field("VpcEndpointAssociationId")
    Description = field("Description")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VpcEndpointAssociationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcEndpointAssociationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRuleGroupMetadataResponse:
    boto3_raw_data: "type_defs.DescribeRuleGroupMetadataResponseTypeDef" = (
        dataclasses.field()
    )

    RuleGroupArn = field("RuleGroupArn")
    RuleGroupName = field("RuleGroupName")
    Description = field("Description")
    Type = field("Type")
    Capacity = field("Capacity")

    @cached_property
    def StatefulRuleOptions(self):  # pragma: no cover
        return StatefulRuleOptions.make_one(self.boto3_raw_data["StatefulRuleOptions"])

    LastModifiedTime = field("LastModifiedTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRuleGroupMetadataResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRuleGroupMetadataResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PublishMetricActionOutput:
    boto3_raw_data: "type_defs.PublishMetricActionOutputTypeDef" = dataclasses.field()

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return Dimension.make_many(self.boto3_raw_data["Dimensions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PublishMetricActionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PublishMetricActionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PublishMetricAction:
    boto3_raw_data: "type_defs.PublishMetricActionTypeDef" = dataclasses.field()

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return Dimension.make_many(self.boto3_raw_data["Dimensions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PublishMetricActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PublishMetricActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFirewallsResponse:
    boto3_raw_data: "type_defs.ListFirewallsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Firewalls(self):  # pragma: no cover
        return FirewallMetadata.make_many(self.boto3_raw_data["Firewalls"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFirewallsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFirewallsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFirewallPoliciesResponse:
    boto3_raw_data: "type_defs.ListFirewallPoliciesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FirewallPolicies(self):  # pragma: no cover
        return FirewallPolicyMetadata.make_many(self.boto3_raw_data["FirewallPolicies"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFirewallPoliciesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFirewallPoliciesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFlowOperationsResponse:
    boto3_raw_data: "type_defs.ListFlowOperationsResponseTypeDef" = dataclasses.field()

    @cached_property
    def FlowOperations(self):  # pragma: no cover
        return FlowOperationMetadata.make_many(self.boto3_raw_data["FlowOperations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFlowOperationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFlowOperationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StatefulEngineOptions:
    boto3_raw_data: "type_defs.StatefulEngineOptionsTypeDef" = dataclasses.field()

    RuleOrder = field("RuleOrder")
    StreamExceptionPolicy = field("StreamExceptionPolicy")

    @cached_property
    def FlowTimeouts(self):  # pragma: no cover
        return FlowTimeouts.make_one(self.boto3_raw_data["FlowTimeouts"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StatefulEngineOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StatefulEngineOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAnalysisReportResultsRequestPaginate:
    boto3_raw_data: "type_defs.GetAnalysisReportResultsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    AnalysisReportId = field("AnalysisReportId")
    FirewallName = field("FirewallName")
    FirewallArn = field("FirewallArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAnalysisReportResultsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAnalysisReportResultsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAnalysisReportsRequestPaginate:
    boto3_raw_data: "type_defs.ListAnalysisReportsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    FirewallName = field("FirewallName")
    FirewallArn = field("FirewallArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAnalysisReportsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAnalysisReportsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFirewallPoliciesRequestPaginate:
    boto3_raw_data: "type_defs.ListFirewallPoliciesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListFirewallPoliciesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFirewallPoliciesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFirewallsRequestPaginate:
    boto3_raw_data: "type_defs.ListFirewallsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    VpcIds = field("VpcIds")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFirewallsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFirewallsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFlowOperationResultsRequestPaginate:
    boto3_raw_data: "type_defs.ListFlowOperationResultsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    FirewallArn = field("FirewallArn")
    FlowOperationId = field("FlowOperationId")
    AvailabilityZone = field("AvailabilityZone")
    VpcEndpointId = field("VpcEndpointId")
    VpcEndpointAssociationArn = field("VpcEndpointAssociationArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListFlowOperationResultsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFlowOperationResultsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFlowOperationsRequestPaginate:
    boto3_raw_data: "type_defs.ListFlowOperationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    FirewallArn = field("FirewallArn")
    AvailabilityZone = field("AvailabilityZone")
    VpcEndpointAssociationArn = field("VpcEndpointAssociationArn")
    VpcEndpointId = field("VpcEndpointId")
    FlowOperationType = field("FlowOperationType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListFlowOperationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFlowOperationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRuleGroupsRequestPaginate:
    boto3_raw_data: "type_defs.ListRuleGroupsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    Scope = field("Scope")
    ManagedType = field("ManagedType")
    Type = field("Type")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListRuleGroupsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRuleGroupsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTLSInspectionConfigurationsRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListTLSInspectionConfigurationsRequestPaginateTypeDef"
    ) = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTLSInspectionConfigurationsRequestPaginateTypeDef"
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
                "type_defs.ListTLSInspectionConfigurationsRequestPaginateTypeDef"
            ]
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
class ListVpcEndpointAssociationsRequestPaginate:
    boto3_raw_data: "type_defs.ListVpcEndpointAssociationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    FirewallArn = field("FirewallArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListVpcEndpointAssociationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVpcEndpointAssociationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolicyVariablesOutput:
    boto3_raw_data: "type_defs.PolicyVariablesOutputTypeDef" = dataclasses.field()

    RuleVariables = field("RuleVariables")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PolicyVariablesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PolicyVariablesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReferenceSetsOutput:
    boto3_raw_data: "type_defs.ReferenceSetsOutputTypeDef" = dataclasses.field()

    IPSetReferences = field("IPSetReferences")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReferenceSetsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReferenceSetsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReferenceSets:
    boto3_raw_data: "type_defs.ReferenceSetsTypeDef" = dataclasses.field()

    IPSetReferences = field("IPSetReferences")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReferenceSetsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReferenceSetsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolicyVariables:
    boto3_raw_data: "type_defs.PolicyVariablesTypeDef" = dataclasses.field()

    RuleVariables = field("RuleVariables")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PolicyVariablesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PolicyVariablesTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRuleGroupsResponse:
    boto3_raw_data: "type_defs.ListRuleGroupsResponseTypeDef" = dataclasses.field()

    @cached_property
    def RuleGroups(self):  # pragma: no cover
        return RuleGroupMetadata.make_many(self.boto3_raw_data["RuleGroups"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRuleGroupsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRuleGroupsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTLSInspectionConfigurationsResponse:
    boto3_raw_data: "type_defs.ListTLSInspectionConfigurationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TLSInspectionConfigurations(self):  # pragma: no cover
        return TLSInspectionConfigurationMetadata.make_many(
            self.boto3_raw_data["TLSInspectionConfigurations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTLSInspectionConfigurationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTLSInspectionConfigurationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVpcEndpointAssociationsResponse:
    boto3_raw_data: "type_defs.ListVpcEndpointAssociationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def VpcEndpointAssociations(self):  # pragma: no cover
        return VpcEndpointAssociationMetadata.make_many(
            self.boto3_raw_data["VpcEndpointAssociations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListVpcEndpointAssociationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVpcEndpointAssociationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoggingConfigurationOutput:
    boto3_raw_data: "type_defs.LoggingConfigurationOutputTypeDef" = dataclasses.field()

    @cached_property
    def LogDestinationConfigs(self):  # pragma: no cover
        return LogDestinationConfigOutput.make_many(
            self.boto3_raw_data["LogDestinationConfigs"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LoggingConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoggingConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoggingConfiguration:
    boto3_raw_data: "type_defs.LoggingConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def LogDestinationConfigs(self):  # pragma: no cover
        return LogDestinationConfig.make_many(
            self.boto3_raw_data["LogDestinationConfigs"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LoggingConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoggingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServerCertificateScopeOutput:
    boto3_raw_data: "type_defs.ServerCertificateScopeOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Sources(self):  # pragma: no cover
        return Address.make_many(self.boto3_raw_data["Sources"])

    @cached_property
    def Destinations(self):  # pragma: no cover
        return Address.make_many(self.boto3_raw_data["Destinations"])

    @cached_property
    def SourcePorts(self):  # pragma: no cover
        return PortRange.make_many(self.boto3_raw_data["SourcePorts"])

    @cached_property
    def DestinationPorts(self):  # pragma: no cover
        return PortRange.make_many(self.boto3_raw_data["DestinationPorts"])

    Protocols = field("Protocols")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServerCertificateScopeOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServerCertificateScopeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServerCertificateScope:
    boto3_raw_data: "type_defs.ServerCertificateScopeTypeDef" = dataclasses.field()

    @cached_property
    def Sources(self):  # pragma: no cover
        return Address.make_many(self.boto3_raw_data["Sources"])

    @cached_property
    def Destinations(self):  # pragma: no cover
        return Address.make_many(self.boto3_raw_data["Destinations"])

    @cached_property
    def SourcePorts(self):  # pragma: no cover
        return PortRange.make_many(self.boto3_raw_data["SourcePorts"])

    @cached_property
    def DestinationPorts(self):  # pragma: no cover
        return PortRange.make_many(self.boto3_raw_data["DestinationPorts"])

    Protocols = field("Protocols")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServerCertificateScopeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServerCertificateScopeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MatchAttributesOutput:
    boto3_raw_data: "type_defs.MatchAttributesOutputTypeDef" = dataclasses.field()

    @cached_property
    def Sources(self):  # pragma: no cover
        return Address.make_many(self.boto3_raw_data["Sources"])

    @cached_property
    def Destinations(self):  # pragma: no cover
        return Address.make_many(self.boto3_raw_data["Destinations"])

    @cached_property
    def SourcePorts(self):  # pragma: no cover
        return PortRange.make_many(self.boto3_raw_data["SourcePorts"])

    @cached_property
    def DestinationPorts(self):  # pragma: no cover
        return PortRange.make_many(self.boto3_raw_data["DestinationPorts"])

    Protocols = field("Protocols")

    @cached_property
    def TCPFlags(self):  # pragma: no cover
        return TCPFlagFieldOutput.make_many(self.boto3_raw_data["TCPFlags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MatchAttributesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MatchAttributesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MatchAttributes:
    boto3_raw_data: "type_defs.MatchAttributesTypeDef" = dataclasses.field()

    @cached_property
    def Sources(self):  # pragma: no cover
        return Address.make_many(self.boto3_raw_data["Sources"])

    @cached_property
    def Destinations(self):  # pragma: no cover
        return Address.make_many(self.boto3_raw_data["Destinations"])

    @cached_property
    def SourcePorts(self):  # pragma: no cover
        return PortRange.make_many(self.boto3_raw_data["SourcePorts"])

    @cached_property
    def DestinationPorts(self):  # pragma: no cover
        return PortRange.make_many(self.boto3_raw_data["DestinationPorts"])

    Protocols = field("Protocols")

    @cached_property
    def TCPFlags(self):  # pragma: no cover
        return TCPFlagField.make_many(self.boto3_raw_data["TCPFlags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MatchAttributesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MatchAttributesTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SyncState:
    boto3_raw_data: "type_defs.SyncStateTypeDef" = dataclasses.field()

    @cached_property
    def Attachment(self):  # pragma: no cover
        return Attachment.make_one(self.boto3_raw_data["Attachment"])

    Config = field("Config")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SyncStateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SyncStateTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleVariablesOutput:
    boto3_raw_data: "type_defs.RuleVariablesOutputTypeDef" = dataclasses.field()

    IPSets = field("IPSets")
    PortSets = field("PortSets")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RuleVariablesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuleVariablesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleVariables:
    boto3_raw_data: "type_defs.RuleVariablesTypeDef" = dataclasses.field()

    IPSets = field("IPSets")
    PortSets = field("PortSets")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleVariablesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuleVariablesTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleGroupResponse:
    boto3_raw_data: "type_defs.RuleGroupResponseTypeDef" = dataclasses.field()

    RuleGroupArn = field("RuleGroupArn")
    RuleGroupName = field("RuleGroupName")
    RuleGroupId = field("RuleGroupId")
    Description = field("Description")
    Type = field("Type")
    Capacity = field("Capacity")
    RuleGroupStatus = field("RuleGroupStatus")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    ConsumedCapacity = field("ConsumedCapacity")
    NumberOfAssociations = field("NumberOfAssociations")

    @cached_property
    def EncryptionConfiguration(self):  # pragma: no cover
        return EncryptionConfiguration.make_one(
            self.boto3_raw_data["EncryptionConfiguration"]
        )

    @cached_property
    def SourceMetadata(self):  # pragma: no cover
        return SourceMetadata.make_one(self.boto3_raw_data["SourceMetadata"])

    SnsTopic = field("SnsTopic")
    LastModifiedTime = field("LastModifiedTime")

    @cached_property
    def AnalysisResults(self):  # pragma: no cover
        return AnalysisResult.make_many(self.boto3_raw_data["AnalysisResults"])

    @cached_property
    def SummaryConfiguration(self):  # pragma: no cover
        return SummaryConfigurationOutput.make_one(
            self.boto3_raw_data["SummaryConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleGroupResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuleGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StatefulRuleOutput:
    boto3_raw_data: "type_defs.StatefulRuleOutputTypeDef" = dataclasses.field()

    Action = field("Action")

    @cached_property
    def Header(self):  # pragma: no cover
        return Header.make_one(self.boto3_raw_data["Header"])

    @cached_property
    def RuleOptions(self):  # pragma: no cover
        return RuleOptionOutput.make_many(self.boto3_raw_data["RuleOptions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StatefulRuleOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StatefulRuleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StatefulRule:
    boto3_raw_data: "type_defs.StatefulRuleTypeDef" = dataclasses.field()

    Action = field("Action")

    @cached_property
    def Header(self):  # pragma: no cover
        return Header.make_one(self.boto3_raw_data["Header"])

    @cached_property
    def RuleOptions(self):  # pragma: no cover
        return RuleOption.make_many(self.boto3_raw_data["RuleOptions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StatefulRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StatefulRuleTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Summary:
    boto3_raw_data: "type_defs.SummaryTypeDef" = dataclasses.field()

    @cached_property
    def RuleSummaries(self):  # pragma: no cover
        return RuleSummary.make_many(self.boto3_raw_data["RuleSummaries"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SummaryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StatefulRuleGroupReference:
    boto3_raw_data: "type_defs.StatefulRuleGroupReferenceTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    Priority = field("Priority")

    @cached_property
    def Override(self):  # pragma: no cover
        return StatefulRuleGroupOverride.make_one(self.boto3_raw_data["Override"])

    DeepThreatInspection = field("DeepThreatInspection")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StatefulRuleGroupReferenceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StatefulRuleGroupReferenceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TLSInspectionConfigurationResponse:
    boto3_raw_data: "type_defs.TLSInspectionConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    TLSInspectionConfigurationArn = field("TLSInspectionConfigurationArn")
    TLSInspectionConfigurationName = field("TLSInspectionConfigurationName")
    TLSInspectionConfigurationId = field("TLSInspectionConfigurationId")
    TLSInspectionConfigurationStatus = field("TLSInspectionConfigurationStatus")
    Description = field("Description")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    LastModifiedTime = field("LastModifiedTime")
    NumberOfAssociations = field("NumberOfAssociations")

    @cached_property
    def EncryptionConfiguration(self):  # pragma: no cover
        return EncryptionConfiguration.make_one(
            self.boto3_raw_data["EncryptionConfiguration"]
        )

    @cached_property
    def Certificates(self):  # pragma: no cover
        return TlsCertificateData.make_many(self.boto3_raw_data["Certificates"])

    @cached_property
    def CertificateAuthority(self):  # pragma: no cover
        return TlsCertificateData.make_one(self.boto3_raw_data["CertificateAuthority"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TLSInspectionConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TLSInspectionConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcEndpointAssociationStatus:
    boto3_raw_data: "type_defs.VpcEndpointAssociationStatusTypeDef" = (
        dataclasses.field()
    )

    Status = field("Status")
    AssociationSyncState = field("AssociationSyncState")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VpcEndpointAssociationStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcEndpointAssociationStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlowOperation:
    boto3_raw_data: "type_defs.FlowOperationTypeDef" = dataclasses.field()

    MinimumFlowAgeInSeconds = field("MinimumFlowAgeInSeconds")

    @cached_property
    def FlowFilters(self):  # pragma: no cover
        return FlowFilterOutput.make_many(self.boto3_raw_data["FlowFilters"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FlowOperationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FlowOperationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFlowOperationResultsResponse:
    boto3_raw_data: "type_defs.ListFlowOperationResultsResponseTypeDef" = (
        dataclasses.field()
    )

    FirewallArn = field("FirewallArn")
    AvailabilityZone = field("AvailabilityZone")
    VpcEndpointAssociationArn = field("VpcEndpointAssociationArn")
    VpcEndpointId = field("VpcEndpointId")
    FlowOperationId = field("FlowOperationId")
    FlowOperationStatus = field("FlowOperationStatus")
    StatusMessage = field("StatusMessage")
    FlowRequestTimestamp = field("FlowRequestTimestamp")

    @cached_property
    def Flows(self):  # pragma: no cover
        return Flow.make_many(self.boto3_raw_data["Flows"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListFlowOperationResultsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFlowOperationResultsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAnalysisReportResultsResponse:
    boto3_raw_data: "type_defs.GetAnalysisReportResultsResponseTypeDef" = (
        dataclasses.field()
    )

    Status = field("Status")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    ReportTime = field("ReportTime")
    AnalysisType = field("AnalysisType")

    @cached_property
    def AnalysisReportResults(self):  # pragma: no cover
        return AnalysisTypeReportResult.make_many(
            self.boto3_raw_data["AnalysisReportResults"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetAnalysisReportResultsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAnalysisReportResultsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CapacityUsageSummary:
    boto3_raw_data: "type_defs.CapacityUsageSummaryTypeDef" = dataclasses.field()

    @cached_property
    def CIDRs(self):  # pragma: no cover
        return CIDRSummary.make_one(self.boto3_raw_data["CIDRs"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CapacityUsageSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CapacityUsageSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFirewallPolicyResponse:
    boto3_raw_data: "type_defs.CreateFirewallPolicyResponseTypeDef" = (
        dataclasses.field()
    )

    UpdateToken = field("UpdateToken")

    @cached_property
    def FirewallPolicyResponse(self):  # pragma: no cover
        return FirewallPolicyResponse.make_one(
            self.boto3_raw_data["FirewallPolicyResponse"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFirewallPolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFirewallPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFirewallPolicyResponse:
    boto3_raw_data: "type_defs.DeleteFirewallPolicyResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FirewallPolicyResponse(self):  # pragma: no cover
        return FirewallPolicyResponse.make_one(
            self.boto3_raw_data["FirewallPolicyResponse"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteFirewallPolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFirewallPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFirewallPolicyResponse:
    boto3_raw_data: "type_defs.UpdateFirewallPolicyResponseTypeDef" = (
        dataclasses.field()
    )

    UpdateToken = field("UpdateToken")

    @cached_property
    def FirewallPolicyResponse(self):  # pragma: no cover
        return FirewallPolicyResponse.make_one(
            self.boto3_raw_data["FirewallPolicyResponse"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFirewallPolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFirewallPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionDefinitionOutput:
    boto3_raw_data: "type_defs.ActionDefinitionOutputTypeDef" = dataclasses.field()

    @cached_property
    def PublishMetricAction(self):  # pragma: no cover
        return PublishMetricActionOutput.make_one(
            self.boto3_raw_data["PublishMetricAction"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActionDefinitionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActionDefinitionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionDefinition:
    boto3_raw_data: "type_defs.ActionDefinitionTypeDef" = dataclasses.field()

    @cached_property
    def PublishMetricAction(self):  # pragma: no cover
        return PublishMetricAction.make_one(self.boto3_raw_data["PublishMetricAction"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActionDefinitionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActionDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLoggingConfigurationResponse:
    boto3_raw_data: "type_defs.DescribeLoggingConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    FirewallArn = field("FirewallArn")

    @cached_property
    def LoggingConfiguration(self):  # pragma: no cover
        return LoggingConfigurationOutput.make_one(
            self.boto3_raw_data["LoggingConfiguration"]
        )

    EnableMonitoringDashboard = field("EnableMonitoringDashboard")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeLoggingConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLoggingConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateLoggingConfigurationResponse:
    boto3_raw_data: "type_defs.UpdateLoggingConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    FirewallArn = field("FirewallArn")
    FirewallName = field("FirewallName")

    @cached_property
    def LoggingConfiguration(self):  # pragma: no cover
        return LoggingConfigurationOutput.make_one(
            self.boto3_raw_data["LoggingConfiguration"]
        )

    EnableMonitoringDashboard = field("EnableMonitoringDashboard")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateLoggingConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateLoggingConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServerCertificateConfigurationOutput:
    boto3_raw_data: "type_defs.ServerCertificateConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ServerCertificates(self):  # pragma: no cover
        return ServerCertificate.make_many(self.boto3_raw_data["ServerCertificates"])

    @cached_property
    def Scopes(self):  # pragma: no cover
        return ServerCertificateScopeOutput.make_many(self.boto3_raw_data["Scopes"])

    CertificateAuthorityArn = field("CertificateAuthorityArn")

    @cached_property
    def CheckCertificateRevocationStatus(self):  # pragma: no cover
        return CheckCertificateRevocationStatusActions.make_one(
            self.boto3_raw_data["CheckCertificateRevocationStatus"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ServerCertificateConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServerCertificateConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServerCertificateConfiguration:
    boto3_raw_data: "type_defs.ServerCertificateConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ServerCertificates(self):  # pragma: no cover
        return ServerCertificate.make_many(self.boto3_raw_data["ServerCertificates"])

    @cached_property
    def Scopes(self):  # pragma: no cover
        return ServerCertificateScope.make_many(self.boto3_raw_data["Scopes"])

    CertificateAuthorityArn = field("CertificateAuthorityArn")

    @cached_property
    def CheckCertificateRevocationStatus(self):  # pragma: no cover
        return CheckCertificateRevocationStatusActions.make_one(
            self.boto3_raw_data["CheckCertificateRevocationStatus"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ServerCertificateConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServerCertificateConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleDefinitionOutput:
    boto3_raw_data: "type_defs.RuleDefinitionOutputTypeDef" = dataclasses.field()

    @cached_property
    def MatchAttributes(self):  # pragma: no cover
        return MatchAttributesOutput.make_one(self.boto3_raw_data["MatchAttributes"])

    Actions = field("Actions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RuleDefinitionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuleDefinitionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleDefinition:
    boto3_raw_data: "type_defs.RuleDefinitionTypeDef" = dataclasses.field()

    @cached_property
    def MatchAttributes(self):  # pragma: no cover
        return MatchAttributes.make_one(self.boto3_raw_data["MatchAttributes"])

    Actions = field("Actions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleDefinitionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuleDefinitionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRuleGroupResponse:
    boto3_raw_data: "type_defs.CreateRuleGroupResponseTypeDef" = dataclasses.field()

    UpdateToken = field("UpdateToken")

    @cached_property
    def RuleGroupResponse(self):  # pragma: no cover
        return RuleGroupResponse.make_one(self.boto3_raw_data["RuleGroupResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRuleGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRuleGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRuleGroupResponse:
    boto3_raw_data: "type_defs.DeleteRuleGroupResponseTypeDef" = dataclasses.field()

    @cached_property
    def RuleGroupResponse(self):  # pragma: no cover
        return RuleGroupResponse.make_one(self.boto3_raw_data["RuleGroupResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteRuleGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRuleGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRuleGroupResponse:
    boto3_raw_data: "type_defs.UpdateRuleGroupResponseTypeDef" = dataclasses.field()

    UpdateToken = field("UpdateToken")

    @cached_property
    def RuleGroupResponse(self):  # pragma: no cover
        return RuleGroupResponse.make_one(self.boto3_raw_data["RuleGroupResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateRuleGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRuleGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRuleGroupSummaryResponse:
    boto3_raw_data: "type_defs.DescribeRuleGroupSummaryResponseTypeDef" = (
        dataclasses.field()
    )

    RuleGroupName = field("RuleGroupName")
    Description = field("Description")

    @cached_property
    def Summary(self):  # pragma: no cover
        return Summary.make_one(self.boto3_raw_data["Summary"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeRuleGroupSummaryResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRuleGroupSummaryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTLSInspectionConfigurationResponse:
    boto3_raw_data: "type_defs.CreateTLSInspectionConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    UpdateToken = field("UpdateToken")

    @cached_property
    def TLSInspectionConfigurationResponse(self):  # pragma: no cover
        return TLSInspectionConfigurationResponse.make_one(
            self.boto3_raw_data["TLSInspectionConfigurationResponse"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateTLSInspectionConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTLSInspectionConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTLSInspectionConfigurationResponse:
    boto3_raw_data: "type_defs.DeleteTLSInspectionConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TLSInspectionConfigurationResponse(self):  # pragma: no cover
        return TLSInspectionConfigurationResponse.make_one(
            self.boto3_raw_data["TLSInspectionConfigurationResponse"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteTLSInspectionConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTLSInspectionConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTLSInspectionConfigurationResponse:
    boto3_raw_data: "type_defs.UpdateTLSInspectionConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    UpdateToken = field("UpdateToken")

    @cached_property
    def TLSInspectionConfigurationResponse(self):  # pragma: no cover
        return TLSInspectionConfigurationResponse.make_one(
            self.boto3_raw_data["TLSInspectionConfigurationResponse"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateTLSInspectionConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTLSInspectionConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVpcEndpointAssociationResponse:
    boto3_raw_data: "type_defs.CreateVpcEndpointAssociationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def VpcEndpointAssociation(self):  # pragma: no cover
        return VpcEndpointAssociation.make_one(
            self.boto3_raw_data["VpcEndpointAssociation"]
        )

    @cached_property
    def VpcEndpointAssociationStatus(self):  # pragma: no cover
        return VpcEndpointAssociationStatus.make_one(
            self.boto3_raw_data["VpcEndpointAssociationStatus"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateVpcEndpointAssociationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVpcEndpointAssociationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVpcEndpointAssociationResponse:
    boto3_raw_data: "type_defs.DeleteVpcEndpointAssociationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def VpcEndpointAssociation(self):  # pragma: no cover
        return VpcEndpointAssociation.make_one(
            self.boto3_raw_data["VpcEndpointAssociation"]
        )

    @cached_property
    def VpcEndpointAssociationStatus(self):  # pragma: no cover
        return VpcEndpointAssociationStatus.make_one(
            self.boto3_raw_data["VpcEndpointAssociationStatus"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteVpcEndpointAssociationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVpcEndpointAssociationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeVpcEndpointAssociationResponse:
    boto3_raw_data: "type_defs.DescribeVpcEndpointAssociationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def VpcEndpointAssociation(self):  # pragma: no cover
        return VpcEndpointAssociation.make_one(
            self.boto3_raw_data["VpcEndpointAssociation"]
        )

    @cached_property
    def VpcEndpointAssociationStatus(self):  # pragma: no cover
        return VpcEndpointAssociationStatus.make_one(
            self.boto3_raw_data["VpcEndpointAssociationStatus"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeVpcEndpointAssociationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeVpcEndpointAssociationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFlowOperationResponse:
    boto3_raw_data: "type_defs.DescribeFlowOperationResponseTypeDef" = (
        dataclasses.field()
    )

    FirewallArn = field("FirewallArn")
    AvailabilityZone = field("AvailabilityZone")
    VpcEndpointAssociationArn = field("VpcEndpointAssociationArn")
    VpcEndpointId = field("VpcEndpointId")
    FlowOperationId = field("FlowOperationId")
    FlowOperationType = field("FlowOperationType")
    FlowOperationStatus = field("FlowOperationStatus")
    StatusMessage = field("StatusMessage")
    FlowRequestTimestamp = field("FlowRequestTimestamp")

    @cached_property
    def FlowOperation(self):  # pragma: no cover
        return FlowOperation.make_one(self.boto3_raw_data["FlowOperation"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeFlowOperationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFlowOperationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartFlowCaptureRequest:
    boto3_raw_data: "type_defs.StartFlowCaptureRequestTypeDef" = dataclasses.field()

    FirewallArn = field("FirewallArn")
    FlowFilters = field("FlowFilters")
    AvailabilityZone = field("AvailabilityZone")
    VpcEndpointAssociationArn = field("VpcEndpointAssociationArn")
    VpcEndpointId = field("VpcEndpointId")
    MinimumFlowAgeInSeconds = field("MinimumFlowAgeInSeconds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartFlowCaptureRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartFlowCaptureRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartFlowFlushRequest:
    boto3_raw_data: "type_defs.StartFlowFlushRequestTypeDef" = dataclasses.field()

    FirewallArn = field("FirewallArn")
    FlowFilters = field("FlowFilters")
    AvailabilityZone = field("AvailabilityZone")
    VpcEndpointAssociationArn = field("VpcEndpointAssociationArn")
    VpcEndpointId = field("VpcEndpointId")
    MinimumFlowAgeInSeconds = field("MinimumFlowAgeInSeconds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartFlowFlushRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartFlowFlushRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FirewallStatus:
    boto3_raw_data: "type_defs.FirewallStatusTypeDef" = dataclasses.field()

    Status = field("Status")
    ConfigurationSyncStateSummary = field("ConfigurationSyncStateSummary")
    SyncStates = field("SyncStates")

    @cached_property
    def CapacityUsageSummary(self):  # pragma: no cover
        return CapacityUsageSummary.make_one(
            self.boto3_raw_data["CapacityUsageSummary"]
        )

    @cached_property
    def TransitGatewayAttachmentSyncState(self):  # pragma: no cover
        return TransitGatewayAttachmentSyncState.make_one(
            self.boto3_raw_data["TransitGatewayAttachmentSyncState"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FirewallStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FirewallStatusTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomActionOutput:
    boto3_raw_data: "type_defs.CustomActionOutputTypeDef" = dataclasses.field()

    ActionName = field("ActionName")

    @cached_property
    def ActionDefinition(self):  # pragma: no cover
        return ActionDefinitionOutput.make_one(self.boto3_raw_data["ActionDefinition"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomActionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomActionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomAction:
    boto3_raw_data: "type_defs.CustomActionTypeDef" = dataclasses.field()

    ActionName = field("ActionName")

    @cached_property
    def ActionDefinition(self):  # pragma: no cover
        return ActionDefinition.make_one(self.boto3_raw_data["ActionDefinition"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CustomActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CustomActionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateLoggingConfigurationRequest:
    boto3_raw_data: "type_defs.UpdateLoggingConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    FirewallArn = field("FirewallArn")
    FirewallName = field("FirewallName")
    LoggingConfiguration = field("LoggingConfiguration")
    EnableMonitoringDashboard = field("EnableMonitoringDashboard")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateLoggingConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateLoggingConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TLSInspectionConfigurationOutput:
    boto3_raw_data: "type_defs.TLSInspectionConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ServerCertificateConfigurations(self):  # pragma: no cover
        return ServerCertificateConfigurationOutput.make_many(
            self.boto3_raw_data["ServerCertificateConfigurations"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TLSInspectionConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TLSInspectionConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TLSInspectionConfiguration:
    boto3_raw_data: "type_defs.TLSInspectionConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def ServerCertificateConfigurations(self):  # pragma: no cover
        return ServerCertificateConfiguration.make_many(
            self.boto3_raw_data["ServerCertificateConfigurations"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TLSInspectionConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TLSInspectionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StatelessRuleOutput:
    boto3_raw_data: "type_defs.StatelessRuleOutputTypeDef" = dataclasses.field()

    @cached_property
    def RuleDefinition(self):  # pragma: no cover
        return RuleDefinitionOutput.make_one(self.boto3_raw_data["RuleDefinition"])

    Priority = field("Priority")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StatelessRuleOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StatelessRuleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StatelessRule:
    boto3_raw_data: "type_defs.StatelessRuleTypeDef" = dataclasses.field()

    @cached_property
    def RuleDefinition(self):  # pragma: no cover
        return RuleDefinition.make_one(self.boto3_raw_data["RuleDefinition"])

    Priority = field("Priority")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StatelessRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StatelessRuleTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFirewallResponse:
    boto3_raw_data: "type_defs.CreateFirewallResponseTypeDef" = dataclasses.field()

    @cached_property
    def Firewall(self):  # pragma: no cover
        return Firewall.make_one(self.boto3_raw_data["Firewall"])

    @cached_property
    def FirewallStatus(self):  # pragma: no cover
        return FirewallStatus.make_one(self.boto3_raw_data["FirewallStatus"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFirewallResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFirewallResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFirewallResponse:
    boto3_raw_data: "type_defs.DeleteFirewallResponseTypeDef" = dataclasses.field()

    @cached_property
    def Firewall(self):  # pragma: no cover
        return Firewall.make_one(self.boto3_raw_data["Firewall"])

    @cached_property
    def FirewallStatus(self):  # pragma: no cover
        return FirewallStatus.make_one(self.boto3_raw_data["FirewallStatus"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteFirewallResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFirewallResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFirewallResponse:
    boto3_raw_data: "type_defs.DescribeFirewallResponseTypeDef" = dataclasses.field()

    UpdateToken = field("UpdateToken")

    @cached_property
    def Firewall(self):  # pragma: no cover
        return Firewall.make_one(self.boto3_raw_data["Firewall"])

    @cached_property
    def FirewallStatus(self):  # pragma: no cover
        return FirewallStatus.make_one(self.boto3_raw_data["FirewallStatus"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeFirewallResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFirewallResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FirewallPolicyOutput:
    boto3_raw_data: "type_defs.FirewallPolicyOutputTypeDef" = dataclasses.field()

    StatelessDefaultActions = field("StatelessDefaultActions")
    StatelessFragmentDefaultActions = field("StatelessFragmentDefaultActions")

    @cached_property
    def StatelessRuleGroupReferences(self):  # pragma: no cover
        return StatelessRuleGroupReference.make_many(
            self.boto3_raw_data["StatelessRuleGroupReferences"]
        )

    @cached_property
    def StatelessCustomActions(self):  # pragma: no cover
        return CustomActionOutput.make_many(
            self.boto3_raw_data["StatelessCustomActions"]
        )

    @cached_property
    def StatefulRuleGroupReferences(self):  # pragma: no cover
        return StatefulRuleGroupReference.make_many(
            self.boto3_raw_data["StatefulRuleGroupReferences"]
        )

    StatefulDefaultActions = field("StatefulDefaultActions")

    @cached_property
    def StatefulEngineOptions(self):  # pragma: no cover
        return StatefulEngineOptions.make_one(
            self.boto3_raw_data["StatefulEngineOptions"]
        )

    TLSInspectionConfigurationArn = field("TLSInspectionConfigurationArn")

    @cached_property
    def PolicyVariables(self):  # pragma: no cover
        return PolicyVariablesOutput.make_one(self.boto3_raw_data["PolicyVariables"])

    EnableTLSSessionHolding = field("EnableTLSSessionHolding")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FirewallPolicyOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FirewallPolicyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FirewallPolicy:
    boto3_raw_data: "type_defs.FirewallPolicyTypeDef" = dataclasses.field()

    StatelessDefaultActions = field("StatelessDefaultActions")
    StatelessFragmentDefaultActions = field("StatelessFragmentDefaultActions")

    @cached_property
    def StatelessRuleGroupReferences(self):  # pragma: no cover
        return StatelessRuleGroupReference.make_many(
            self.boto3_raw_data["StatelessRuleGroupReferences"]
        )

    @cached_property
    def StatelessCustomActions(self):  # pragma: no cover
        return CustomAction.make_many(self.boto3_raw_data["StatelessCustomActions"])

    @cached_property
    def StatefulRuleGroupReferences(self):  # pragma: no cover
        return StatefulRuleGroupReference.make_many(
            self.boto3_raw_data["StatefulRuleGroupReferences"]
        )

    StatefulDefaultActions = field("StatefulDefaultActions")

    @cached_property
    def StatefulEngineOptions(self):  # pragma: no cover
        return StatefulEngineOptions.make_one(
            self.boto3_raw_data["StatefulEngineOptions"]
        )

    TLSInspectionConfigurationArn = field("TLSInspectionConfigurationArn")

    @cached_property
    def PolicyVariables(self):  # pragma: no cover
        return PolicyVariables.make_one(self.boto3_raw_data["PolicyVariables"])

    EnableTLSSessionHolding = field("EnableTLSSessionHolding")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FirewallPolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FirewallPolicyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTLSInspectionConfigurationResponse:
    boto3_raw_data: "type_defs.DescribeTLSInspectionConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    UpdateToken = field("UpdateToken")

    @cached_property
    def TLSInspectionConfiguration(self):  # pragma: no cover
        return TLSInspectionConfigurationOutput.make_one(
            self.boto3_raw_data["TLSInspectionConfiguration"]
        )

    @cached_property
    def TLSInspectionConfigurationResponse(self):  # pragma: no cover
        return TLSInspectionConfigurationResponse.make_one(
            self.boto3_raw_data["TLSInspectionConfigurationResponse"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeTLSInspectionConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTLSInspectionConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StatelessRulesAndCustomActionsOutput:
    boto3_raw_data: "type_defs.StatelessRulesAndCustomActionsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def StatelessRules(self):  # pragma: no cover
        return StatelessRuleOutput.make_many(self.boto3_raw_data["StatelessRules"])

    @cached_property
    def CustomActions(self):  # pragma: no cover
        return CustomActionOutput.make_many(self.boto3_raw_data["CustomActions"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StatelessRulesAndCustomActionsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StatelessRulesAndCustomActionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StatelessRulesAndCustomActions:
    boto3_raw_data: "type_defs.StatelessRulesAndCustomActionsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def StatelessRules(self):  # pragma: no cover
        return StatelessRule.make_many(self.boto3_raw_data["StatelessRules"])

    @cached_property
    def CustomActions(self):  # pragma: no cover
        return CustomAction.make_many(self.boto3_raw_data["CustomActions"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StatelessRulesAndCustomActionsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StatelessRulesAndCustomActionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFirewallPolicyResponse:
    boto3_raw_data: "type_defs.DescribeFirewallPolicyResponseTypeDef" = (
        dataclasses.field()
    )

    UpdateToken = field("UpdateToken")

    @cached_property
    def FirewallPolicyResponse(self):  # pragma: no cover
        return FirewallPolicyResponse.make_one(
            self.boto3_raw_data["FirewallPolicyResponse"]
        )

    @cached_property
    def FirewallPolicy(self):  # pragma: no cover
        return FirewallPolicyOutput.make_one(self.boto3_raw_data["FirewallPolicy"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeFirewallPolicyResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFirewallPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTLSInspectionConfigurationRequest:
    boto3_raw_data: "type_defs.CreateTLSInspectionConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    TLSInspectionConfigurationName = field("TLSInspectionConfigurationName")
    TLSInspectionConfiguration = field("TLSInspectionConfiguration")
    Description = field("Description")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def EncryptionConfiguration(self):  # pragma: no cover
        return EncryptionConfiguration.make_one(
            self.boto3_raw_data["EncryptionConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateTLSInspectionConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTLSInspectionConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTLSInspectionConfigurationRequest:
    boto3_raw_data: "type_defs.UpdateTLSInspectionConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    TLSInspectionConfiguration = field("TLSInspectionConfiguration")
    UpdateToken = field("UpdateToken")
    TLSInspectionConfigurationArn = field("TLSInspectionConfigurationArn")
    TLSInspectionConfigurationName = field("TLSInspectionConfigurationName")
    Description = field("Description")

    @cached_property
    def EncryptionConfiguration(self):  # pragma: no cover
        return EncryptionConfiguration.make_one(
            self.boto3_raw_data["EncryptionConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateTLSInspectionConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTLSInspectionConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RulesSourceOutput:
    boto3_raw_data: "type_defs.RulesSourceOutputTypeDef" = dataclasses.field()

    RulesString = field("RulesString")

    @cached_property
    def RulesSourceList(self):  # pragma: no cover
        return RulesSourceListOutput.make_one(self.boto3_raw_data["RulesSourceList"])

    @cached_property
    def StatefulRules(self):  # pragma: no cover
        return StatefulRuleOutput.make_many(self.boto3_raw_data["StatefulRules"])

    @cached_property
    def StatelessRulesAndCustomActions(self):  # pragma: no cover
        return StatelessRulesAndCustomActionsOutput.make_one(
            self.boto3_raw_data["StatelessRulesAndCustomActions"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RulesSourceOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RulesSourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RulesSource:
    boto3_raw_data: "type_defs.RulesSourceTypeDef" = dataclasses.field()

    RulesString = field("RulesString")

    @cached_property
    def RulesSourceList(self):  # pragma: no cover
        return RulesSourceList.make_one(self.boto3_raw_data["RulesSourceList"])

    @cached_property
    def StatefulRules(self):  # pragma: no cover
        return StatefulRule.make_many(self.boto3_raw_data["StatefulRules"])

    @cached_property
    def StatelessRulesAndCustomActions(self):  # pragma: no cover
        return StatelessRulesAndCustomActions.make_one(
            self.boto3_raw_data["StatelessRulesAndCustomActions"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RulesSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RulesSourceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFirewallPolicyRequest:
    boto3_raw_data: "type_defs.CreateFirewallPolicyRequestTypeDef" = dataclasses.field()

    FirewallPolicyName = field("FirewallPolicyName")
    FirewallPolicy = field("FirewallPolicy")
    Description = field("Description")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    DryRun = field("DryRun")

    @cached_property
    def EncryptionConfiguration(self):  # pragma: no cover
        return EncryptionConfiguration.make_one(
            self.boto3_raw_data["EncryptionConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFirewallPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFirewallPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFirewallPolicyRequest:
    boto3_raw_data: "type_defs.UpdateFirewallPolicyRequestTypeDef" = dataclasses.field()

    UpdateToken = field("UpdateToken")
    FirewallPolicy = field("FirewallPolicy")
    FirewallPolicyArn = field("FirewallPolicyArn")
    FirewallPolicyName = field("FirewallPolicyName")
    Description = field("Description")
    DryRun = field("DryRun")

    @cached_property
    def EncryptionConfiguration(self):  # pragma: no cover
        return EncryptionConfiguration.make_one(
            self.boto3_raw_data["EncryptionConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFirewallPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFirewallPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleGroupOutput:
    boto3_raw_data: "type_defs.RuleGroupOutputTypeDef" = dataclasses.field()

    @cached_property
    def RulesSource(self):  # pragma: no cover
        return RulesSourceOutput.make_one(self.boto3_raw_data["RulesSource"])

    @cached_property
    def RuleVariables(self):  # pragma: no cover
        return RuleVariablesOutput.make_one(self.boto3_raw_data["RuleVariables"])

    @cached_property
    def ReferenceSets(self):  # pragma: no cover
        return ReferenceSetsOutput.make_one(self.boto3_raw_data["ReferenceSets"])

    @cached_property
    def StatefulRuleOptions(self):  # pragma: no cover
        return StatefulRuleOptions.make_one(self.boto3_raw_data["StatefulRuleOptions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleGroupOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuleGroupOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleGroup:
    boto3_raw_data: "type_defs.RuleGroupTypeDef" = dataclasses.field()

    @cached_property
    def RulesSource(self):  # pragma: no cover
        return RulesSource.make_one(self.boto3_raw_data["RulesSource"])

    @cached_property
    def RuleVariables(self):  # pragma: no cover
        return RuleVariables.make_one(self.boto3_raw_data["RuleVariables"])

    @cached_property
    def ReferenceSets(self):  # pragma: no cover
        return ReferenceSets.make_one(self.boto3_raw_data["ReferenceSets"])

    @cached_property
    def StatefulRuleOptions(self):  # pragma: no cover
        return StatefulRuleOptions.make_one(self.boto3_raw_data["StatefulRuleOptions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuleGroupTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRuleGroupResponse:
    boto3_raw_data: "type_defs.DescribeRuleGroupResponseTypeDef" = dataclasses.field()

    UpdateToken = field("UpdateToken")

    @cached_property
    def RuleGroup(self):  # pragma: no cover
        return RuleGroupOutput.make_one(self.boto3_raw_data["RuleGroup"])

    @cached_property
    def RuleGroupResponse(self):  # pragma: no cover
        return RuleGroupResponse.make_one(self.boto3_raw_data["RuleGroupResponse"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeRuleGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRuleGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRuleGroupRequest:
    boto3_raw_data: "type_defs.CreateRuleGroupRequestTypeDef" = dataclasses.field()

    RuleGroupName = field("RuleGroupName")
    Type = field("Type")
    Capacity = field("Capacity")
    RuleGroup = field("RuleGroup")
    Rules = field("Rules")
    Description = field("Description")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    DryRun = field("DryRun")

    @cached_property
    def EncryptionConfiguration(self):  # pragma: no cover
        return EncryptionConfiguration.make_one(
            self.boto3_raw_data["EncryptionConfiguration"]
        )

    @cached_property
    def SourceMetadata(self):  # pragma: no cover
        return SourceMetadata.make_one(self.boto3_raw_data["SourceMetadata"])

    AnalyzeRuleGroup = field("AnalyzeRuleGroup")
    SummaryConfiguration = field("SummaryConfiguration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRuleGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRuleGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRuleGroupRequest:
    boto3_raw_data: "type_defs.UpdateRuleGroupRequestTypeDef" = dataclasses.field()

    UpdateToken = field("UpdateToken")
    RuleGroupArn = field("RuleGroupArn")
    RuleGroupName = field("RuleGroupName")
    RuleGroup = field("RuleGroup")
    Rules = field("Rules")
    Type = field("Type")
    Description = field("Description")
    DryRun = field("DryRun")

    @cached_property
    def EncryptionConfiguration(self):  # pragma: no cover
        return EncryptionConfiguration.make_one(
            self.boto3_raw_data["EncryptionConfiguration"]
        )

    @cached_property
    def SourceMetadata(self):  # pragma: no cover
        return SourceMetadata.make_one(self.boto3_raw_data["SourceMetadata"])

    AnalyzeRuleGroup = field("AnalyzeRuleGroup")
    SummaryConfiguration = field("SummaryConfiguration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateRuleGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRuleGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]

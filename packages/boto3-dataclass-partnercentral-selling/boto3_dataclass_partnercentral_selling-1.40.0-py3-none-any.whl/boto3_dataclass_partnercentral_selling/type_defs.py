# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_partnercentral_selling import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AcceptEngagementInvitationRequest:
    boto3_raw_data: "type_defs.AcceptEngagementInvitationRequestTypeDef" = (
        dataclasses.field()
    )

    Catalog = field("Catalog")
    Identifier = field("Identifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AcceptEngagementInvitationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AcceptEngagementInvitationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccountReceiver:
    boto3_raw_data: "type_defs.AccountReceiverTypeDef" = dataclasses.field()

    AwsAccountId = field("AwsAccountId")
    Alias = field("Alias")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccountReceiverTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccountReceiverTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddressSummary:
    boto3_raw_data: "type_defs.AddressSummaryTypeDef" = dataclasses.field()

    City = field("City")
    PostalCode = field("PostalCode")
    StateOrRegion = field("StateOrRegion")
    CountryCode = field("CountryCode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AddressSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AddressSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Address:
    boto3_raw_data: "type_defs.AddressTypeDef" = dataclasses.field()

    City = field("City")
    PostalCode = field("PostalCode")
    StateOrRegion = field("StateOrRegion")
    CountryCode = field("CountryCode")
    StreetAddress = field("StreetAddress")

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
class AssigneeContact:
    boto3_raw_data: "type_defs.AssigneeContactTypeDef" = dataclasses.field()

    Email = field("Email")
    FirstName = field("FirstName")
    LastName = field("LastName")
    BusinessTitle = field("BusinessTitle")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssigneeContactTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AssigneeContactTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateOpportunityRequest:
    boto3_raw_data: "type_defs.AssociateOpportunityRequestTypeDef" = dataclasses.field()

    Catalog = field("Catalog")
    OpportunityIdentifier = field("OpportunityIdentifier")
    RelatedEntityType = field("RelatedEntityType")
    RelatedEntityIdentifier = field("RelatedEntityIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateOpportunityRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateOpportunityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Contact:
    boto3_raw_data: "type_defs.ContactTypeDef" = dataclasses.field()

    Email = field("Email")
    FirstName = field("FirstName")
    LastName = field("LastName")
    BusinessTitle = field("BusinessTitle")
    Phone = field("Phone")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContactTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ContactTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AwsOpportunityInsights:
    boto3_raw_data: "type_defs.AwsOpportunityInsightsTypeDef" = dataclasses.field()

    NextBestActions = field("NextBestActions")
    EngagementScore = field("EngagementScore")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AwsOpportunityInsightsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AwsOpportunityInsightsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProfileNextStepsHistory:
    boto3_raw_data: "type_defs.ProfileNextStepsHistoryTypeDef" = dataclasses.field()

    Value = field("Value")
    Time = field("Time")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProfileNextStepsHistoryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProfileNextStepsHistoryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExpectedCustomerSpend:
    boto3_raw_data: "type_defs.ExpectedCustomerSpendTypeDef" = dataclasses.field()

    Amount = field("Amount")
    CurrencyCode = field("CurrencyCode")
    Frequency = field("Frequency")
    TargetCompany = field("TargetCompany")
    EstimationUrl = field("EstimationUrl")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExpectedCustomerSpendTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExpectedCustomerSpendTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AwsOpportunityRelatedEntities:
    boto3_raw_data: "type_defs.AwsOpportunityRelatedEntitiesTypeDef" = (
        dataclasses.field()
    )

    AwsProducts = field("AwsProducts")
    Solutions = field("Solutions")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AwsOpportunityRelatedEntitiesTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AwsOpportunityRelatedEntitiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AwsSubmission:
    boto3_raw_data: "type_defs.AwsSubmissionTypeDef" = dataclasses.field()

    InvolvementType = field("InvolvementType")
    Visibility = field("Visibility")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AwsSubmissionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AwsSubmissionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AwsTeamMember:
    boto3_raw_data: "type_defs.AwsTeamMemberTypeDef" = dataclasses.field()

    Email = field("Email")
    FirstName = field("FirstName")
    LastName = field("LastName")
    BusinessTitle = field("BusinessTitle")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AwsTeamMemberTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AwsTeamMemberTypeDef"]],
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
class CreateResourceSnapshotRequest:
    boto3_raw_data: "type_defs.CreateResourceSnapshotRequestTypeDef" = (
        dataclasses.field()
    )

    Catalog = field("Catalog")
    EngagementIdentifier = field("EngagementIdentifier")
    ResourceType = field("ResourceType")
    ResourceIdentifier = field("ResourceIdentifier")
    ResourceSnapshotTemplateIdentifier = field("ResourceSnapshotTemplateIdentifier")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateResourceSnapshotRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateResourceSnapshotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EngagementCustomerProjectDetails:
    boto3_raw_data: "type_defs.EngagementCustomerProjectDetailsTypeDef" = (
        dataclasses.field()
    )

    Title = field("Title")
    BusinessProblem = field("BusinessProblem")
    TargetCompletionDate = field("TargetCompletionDate")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EngagementCustomerProjectDetailsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EngagementCustomerProjectDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EngagementCustomer:
    boto3_raw_data: "type_defs.EngagementCustomerTypeDef" = dataclasses.field()

    Industry = field("Industry")
    CompanyName = field("CompanyName")
    WebsiteUrl = field("WebsiteUrl")
    CountryCode = field("CountryCode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EngagementCustomerTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EngagementCustomerTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteResourceSnapshotJobRequest:
    boto3_raw_data: "type_defs.DeleteResourceSnapshotJobRequestTypeDef" = (
        dataclasses.field()
    )

    Catalog = field("Catalog")
    ResourceSnapshotJobIdentifier = field("ResourceSnapshotJobIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteResourceSnapshotJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteResourceSnapshotJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateOpportunityRequest:
    boto3_raw_data: "type_defs.DisassociateOpportunityRequestTypeDef" = (
        dataclasses.field()
    )

    Catalog = field("Catalog")
    OpportunityIdentifier = field("OpportunityIdentifier")
    RelatedEntityType = field("RelatedEntityType")
    RelatedEntityIdentifier = field("RelatedEntityIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DisassociateOpportunityRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateOpportunityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EngagementMemberSummary:
    boto3_raw_data: "type_defs.EngagementMemberSummaryTypeDef" = dataclasses.field()

    CompanyName = field("CompanyName")
    WebsiteUrl = field("WebsiteUrl")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EngagementMemberSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EngagementMemberSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EngagementMember:
    boto3_raw_data: "type_defs.EngagementMemberTypeDef" = dataclasses.field()

    CompanyName = field("CompanyName")
    WebsiteUrl = field("WebsiteUrl")
    AccountId = field("AccountId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EngagementMemberTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EngagementMemberTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EngagementResourceAssociationSummary:
    boto3_raw_data: "type_defs.EngagementResourceAssociationSummaryTypeDef" = (
        dataclasses.field()
    )

    Catalog = field("Catalog")
    EngagementId = field("EngagementId")
    ResourceType = field("ResourceType")
    ResourceId = field("ResourceId")
    CreatedBy = field("CreatedBy")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EngagementResourceAssociationSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EngagementResourceAssociationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EngagementSort:
    boto3_raw_data: "type_defs.EngagementSortTypeDef" = dataclasses.field()

    SortOrder = field("SortOrder")
    SortBy = field("SortBy")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EngagementSortTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EngagementSortTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EngagementSummary:
    boto3_raw_data: "type_defs.EngagementSummaryTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Id = field("Id")
    Title = field("Title")
    CreatedAt = field("CreatedAt")
    CreatedBy = field("CreatedBy")
    MemberCount = field("MemberCount")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EngagementSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EngagementSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAwsOpportunitySummaryRequest:
    boto3_raw_data: "type_defs.GetAwsOpportunitySummaryRequestTypeDef" = (
        dataclasses.field()
    )

    Catalog = field("Catalog")
    RelatedOpportunityIdentifier = field("RelatedOpportunityIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetAwsOpportunitySummaryRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAwsOpportunitySummaryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEngagementInvitationRequest:
    boto3_raw_data: "type_defs.GetEngagementInvitationRequestTypeDef" = (
        dataclasses.field()
    )

    Catalog = field("Catalog")
    Identifier = field("Identifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetEngagementInvitationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEngagementInvitationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEngagementRequest:
    boto3_raw_data: "type_defs.GetEngagementRequestTypeDef" = dataclasses.field()

    Catalog = field("Catalog")
    Identifier = field("Identifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEngagementRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEngagementRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOpportunityRequest:
    boto3_raw_data: "type_defs.GetOpportunityRequestTypeDef" = dataclasses.field()

    Catalog = field("Catalog")
    Identifier = field("Identifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetOpportunityRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOpportunityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MarketingOutput:
    boto3_raw_data: "type_defs.MarketingOutputTypeDef" = dataclasses.field()

    CampaignName = field("CampaignName")
    Source = field("Source")
    UseCases = field("UseCases")
    Channels = field("Channels")
    AwsFundingUsed = field("AwsFundingUsed")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MarketingOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MarketingOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RelatedEntityIdentifiers:
    boto3_raw_data: "type_defs.RelatedEntityIdentifiersTypeDef" = dataclasses.field()

    AwsMarketplaceOffers = field("AwsMarketplaceOffers")
    Solutions = field("Solutions")
    AwsProducts = field("AwsProducts")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RelatedEntityIdentifiersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RelatedEntityIdentifiersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourceSnapshotJobRequest:
    boto3_raw_data: "type_defs.GetResourceSnapshotJobRequestTypeDef" = (
        dataclasses.field()
    )

    Catalog = field("Catalog")
    ResourceSnapshotJobIdentifier = field("ResourceSnapshotJobIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetResourceSnapshotJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourceSnapshotJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourceSnapshotRequest:
    boto3_raw_data: "type_defs.GetResourceSnapshotRequestTypeDef" = dataclasses.field()

    Catalog = field("Catalog")
    EngagementIdentifier = field("EngagementIdentifier")
    ResourceType = field("ResourceType")
    ResourceIdentifier = field("ResourceIdentifier")
    ResourceSnapshotTemplateIdentifier = field("ResourceSnapshotTemplateIdentifier")
    Revision = field("Revision")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourceSnapshotRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourceSnapshotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSellingSystemSettingsRequest:
    boto3_raw_data: "type_defs.GetSellingSystemSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    Catalog = field("Catalog")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetSellingSystemSettingsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSellingSystemSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifeCycleForView:
    boto3_raw_data: "type_defs.LifeCycleForViewTypeDef" = dataclasses.field()

    TargetCloseDate = field("TargetCloseDate")
    ReviewStatus = field("ReviewStatus")
    Stage = field("Stage")
    NextSteps = field("NextSteps")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LifeCycleForViewTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifeCycleForViewTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NextStepsHistoryOutput:
    boto3_raw_data: "type_defs.NextStepsHistoryOutputTypeDef" = dataclasses.field()

    Value = field("Value")
    Time = field("Time")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NextStepsHistoryOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NextStepsHistoryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifeCycleSummary:
    boto3_raw_data: "type_defs.LifeCycleSummaryTypeDef" = dataclasses.field()

    Stage = field("Stage")
    ClosedLostReason = field("ClosedLostReason")
    NextSteps = field("NextSteps")
    TargetCloseDate = field("TargetCloseDate")
    ReviewStatus = field("ReviewStatus")
    ReviewComments = field("ReviewComments")
    ReviewStatusReason = field("ReviewStatusReason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LifeCycleSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifeCycleSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEngagementByAcceptingInvitationTaskSummary:
    boto3_raw_data: (
        "type_defs.ListEngagementByAcceptingInvitationTaskSummaryTypeDef"
    ) = dataclasses.field()

    TaskId = field("TaskId")
    TaskArn = field("TaskArn")
    StartTime = field("StartTime")
    TaskStatus = field("TaskStatus")
    Message = field("Message")
    ReasonCode = field("ReasonCode")
    OpportunityId = field("OpportunityId")
    ResourceSnapshotJobId = field("ResourceSnapshotJobId")
    EngagementInvitationId = field("EngagementInvitationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEngagementByAcceptingInvitationTaskSummaryTypeDef"
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
                "type_defs.ListEngagementByAcceptingInvitationTaskSummaryTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTasksSortBase:
    boto3_raw_data: "type_defs.ListTasksSortBaseTypeDef" = dataclasses.field()

    SortOrder = field("SortOrder")
    SortBy = field("SortBy")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListTasksSortBaseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTasksSortBaseTypeDef"]
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
class ListEngagementFromOpportunityTaskSummary:
    boto3_raw_data: "type_defs.ListEngagementFromOpportunityTaskSummaryTypeDef" = (
        dataclasses.field()
    )

    TaskId = field("TaskId")
    TaskArn = field("TaskArn")
    StartTime = field("StartTime")
    TaskStatus = field("TaskStatus")
    Message = field("Message")
    ReasonCode = field("ReasonCode")
    OpportunityId = field("OpportunityId")
    ResourceSnapshotJobId = field("ResourceSnapshotJobId")
    EngagementId = field("EngagementId")
    EngagementInvitationId = field("EngagementInvitationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEngagementFromOpportunityTaskSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEngagementFromOpportunityTaskSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpportunityEngagementInvitationSort:
    boto3_raw_data: "type_defs.OpportunityEngagementInvitationSortTypeDef" = (
        dataclasses.field()
    )

    SortOrder = field("SortOrder")
    SortBy = field("SortBy")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OpportunityEngagementInvitationSortTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpportunityEngagementInvitationSortTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEngagementMembersRequest:
    boto3_raw_data: "type_defs.ListEngagementMembersRequestTypeDef" = (
        dataclasses.field()
    )

    Catalog = field("Catalog")
    Identifier = field("Identifier")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEngagementMembersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEngagementMembersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEngagementResourceAssociationsRequest:
    boto3_raw_data: "type_defs.ListEngagementResourceAssociationsRequestTypeDef" = (
        dataclasses.field()
    )

    Catalog = field("Catalog")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    EngagementIdentifier = field("EngagementIdentifier")
    ResourceType = field("ResourceType")
    ResourceIdentifier = field("ResourceIdentifier")
    CreatedBy = field("CreatedBy")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEngagementResourceAssociationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEngagementResourceAssociationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpportunitySort:
    boto3_raw_data: "type_defs.OpportunitySortTypeDef" = dataclasses.field()

    SortOrder = field("SortOrder")
    SortBy = field("SortBy")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OpportunitySortTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OpportunitySortTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SortObject:
    boto3_raw_data: "type_defs.SortObjectTypeDef" = dataclasses.field()

    SortBy = field("SortBy")
    SortOrder = field("SortOrder")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SortObjectTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SortObjectTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceSnapshotJobSummary:
    boto3_raw_data: "type_defs.ResourceSnapshotJobSummaryTypeDef" = dataclasses.field()

    Id = field("Id")
    Arn = field("Arn")
    EngagementId = field("EngagementId")
    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceSnapshotJobSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceSnapshotJobSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceSnapshotsRequest:
    boto3_raw_data: "type_defs.ListResourceSnapshotsRequestTypeDef" = (
        dataclasses.field()
    )

    Catalog = field("Catalog")
    EngagementIdentifier = field("EngagementIdentifier")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    ResourceType = field("ResourceType")
    ResourceIdentifier = field("ResourceIdentifier")
    ResourceSnapshotTemplateIdentifier = field("ResourceSnapshotTemplateIdentifier")
    CreatedBy = field("CreatedBy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListResourceSnapshotsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceSnapshotsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceSnapshotSummary:
    boto3_raw_data: "type_defs.ResourceSnapshotSummaryTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Revision = field("Revision")
    ResourceType = field("ResourceType")
    ResourceId = field("ResourceId")
    ResourceSnapshotTemplateName = field("ResourceSnapshotTemplateName")
    CreatedBy = field("CreatedBy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceSnapshotSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceSnapshotSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SolutionSort:
    boto3_raw_data: "type_defs.SolutionSortTypeDef" = dataclasses.field()

    SortOrder = field("SortOrder")
    SortBy = field("SortBy")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SolutionSortTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SolutionSortTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SolutionBase:
    boto3_raw_data: "type_defs.SolutionBaseTypeDef" = dataclasses.field()

    Catalog = field("Catalog")
    Id = field("Id")
    Name = field("Name")
    Status = field("Status")
    Category = field("Category")
    CreatedDate = field("CreatedDate")
    Arn = field("Arn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SolutionBaseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SolutionBaseTypeDef"]],
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
class Marketing:
    boto3_raw_data: "type_defs.MarketingTypeDef" = dataclasses.field()

    CampaignName = field("CampaignName")
    Source = field("Source")
    UseCases = field("UseCases")
    Channels = field("Channels")
    AwsFundingUsed = field("AwsFundingUsed")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MarketingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MarketingTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MonetaryValue:
    boto3_raw_data: "type_defs.MonetaryValueTypeDef" = dataclasses.field()

    Amount = field("Amount")
    CurrencyCode = field("CurrencyCode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MonetaryValueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MonetaryValueTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SenderContact:
    boto3_raw_data: "type_defs.SenderContactTypeDef" = dataclasses.field()

    Email = field("Email")
    FirstName = field("FirstName")
    LastName = field("LastName")
    BusinessTitle = field("BusinessTitle")
    Phone = field("Phone")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SenderContactTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SenderContactTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutSellingSystemSettingsRequest:
    boto3_raw_data: "type_defs.PutSellingSystemSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    Catalog = field("Catalog")
    ResourceSnapshotJobRoleIdentifier = field("ResourceSnapshotJobRoleIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutSellingSystemSettingsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutSellingSystemSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RejectEngagementInvitationRequest:
    boto3_raw_data: "type_defs.RejectEngagementInvitationRequestTypeDef" = (
        dataclasses.field()
    )

    Catalog = field("Catalog")
    Identifier = field("Identifier")
    RejectionReason = field("RejectionReason")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RejectEngagementInvitationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RejectEngagementInvitationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartResourceSnapshotJobRequest:
    boto3_raw_data: "type_defs.StartResourceSnapshotJobRequestTypeDef" = (
        dataclasses.field()
    )

    Catalog = field("Catalog")
    ResourceSnapshotJobIdentifier = field("ResourceSnapshotJobIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartResourceSnapshotJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartResourceSnapshotJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopResourceSnapshotJobRequest:
    boto3_raw_data: "type_defs.StopResourceSnapshotJobRequestTypeDef" = (
        dataclasses.field()
    )

    Catalog = field("Catalog")
    ResourceSnapshotJobIdentifier = field("ResourceSnapshotJobIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StopResourceSnapshotJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopResourceSnapshotJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubmitOpportunityRequest:
    boto3_raw_data: "type_defs.SubmitOpportunityRequestTypeDef" = dataclasses.field()

    Catalog = field("Catalog")
    Identifier = field("Identifier")
    InvolvementType = field("InvolvementType")
    Visibility = field("Visibility")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SubmitOpportunityRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubmitOpportunityRequestTypeDef"]
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
class Receiver:
    boto3_raw_data: "type_defs.ReceiverTypeDef" = dataclasses.field()

    @cached_property
    def Account(self):  # pragma: no cover
        return AccountReceiver.make_one(self.boto3_raw_data["Account"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReceiverTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReceiverTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccountSummary:
    boto3_raw_data: "type_defs.AccountSummaryTypeDef" = dataclasses.field()

    CompanyName = field("CompanyName")
    Industry = field("Industry")
    OtherIndustry = field("OtherIndustry")
    WebsiteUrl = field("WebsiteUrl")

    @cached_property
    def Address(self):  # pragma: no cover
        return AddressSummary.make_one(self.boto3_raw_data["Address"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccountSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccountSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Account:
    boto3_raw_data: "type_defs.AccountTypeDef" = dataclasses.field()

    CompanyName = field("CompanyName")
    Industry = field("Industry")
    OtherIndustry = field("OtherIndustry")
    WebsiteUrl = field("WebsiteUrl")
    AwsAccountId = field("AwsAccountId")

    @cached_property
    def Address(self):  # pragma: no cover
        return Address.make_one(self.boto3_raw_data["Address"])

    Duns = field("Duns")

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
class AssignOpportunityRequest:
    boto3_raw_data: "type_defs.AssignOpportunityRequestTypeDef" = dataclasses.field()

    Catalog = field("Catalog")
    Identifier = field("Identifier")

    @cached_property
    def Assignee(self):  # pragma: no cover
        return AssigneeContact.make_one(self.boto3_raw_data["Assignee"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssignOpportunityRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssignOpportunityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AwsOpportunityCustomer:
    boto3_raw_data: "type_defs.AwsOpportunityCustomerTypeDef" = dataclasses.field()

    @cached_property
    def Contacts(self):  # pragma: no cover
        return Contact.make_many(self.boto3_raw_data["Contacts"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AwsOpportunityCustomerTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AwsOpportunityCustomerTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AwsOpportunityLifeCycle:
    boto3_raw_data: "type_defs.AwsOpportunityLifeCycleTypeDef" = dataclasses.field()

    TargetCloseDate = field("TargetCloseDate")
    ClosedLostReason = field("ClosedLostReason")
    Stage = field("Stage")
    NextSteps = field("NextSteps")

    @cached_property
    def NextStepsHistory(self):  # pragma: no cover
        return ProfileNextStepsHistory.make_many(
            self.boto3_raw_data["NextStepsHistory"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AwsOpportunityLifeCycleTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AwsOpportunityLifeCycleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AwsOpportunityProject:
    boto3_raw_data: "type_defs.AwsOpportunityProjectTypeDef" = dataclasses.field()

    @cached_property
    def ExpectedCustomerSpend(self):  # pragma: no cover
        return ExpectedCustomerSpend.make_many(
            self.boto3_raw_data["ExpectedCustomerSpend"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AwsOpportunityProjectTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AwsOpportunityProjectTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProjectDetailsOutput:
    boto3_raw_data: "type_defs.ProjectDetailsOutputTypeDef" = dataclasses.field()

    BusinessProblem = field("BusinessProblem")
    Title = field("Title")
    TargetCompletionDate = field("TargetCompletionDate")

    @cached_property
    def ExpectedCustomerSpend(self):  # pragma: no cover
        return ExpectedCustomerSpend.make_many(
            self.boto3_raw_data["ExpectedCustomerSpend"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProjectDetailsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProjectDetailsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProjectDetails:
    boto3_raw_data: "type_defs.ProjectDetailsTypeDef" = dataclasses.field()

    BusinessProblem = field("BusinessProblem")
    Title = field("Title")
    TargetCompletionDate = field("TargetCompletionDate")

    @cached_property
    def ExpectedCustomerSpend(self):  # pragma: no cover
        return ExpectedCustomerSpend.make_many(
            self.boto3_raw_data["ExpectedCustomerSpend"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProjectDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProjectDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProjectOutput:
    boto3_raw_data: "type_defs.ProjectOutputTypeDef" = dataclasses.field()

    DeliveryModels = field("DeliveryModels")

    @cached_property
    def ExpectedCustomerSpend(self):  # pragma: no cover
        return ExpectedCustomerSpend.make_many(
            self.boto3_raw_data["ExpectedCustomerSpend"]
        )

    Title = field("Title")
    ApnPrograms = field("ApnPrograms")
    CustomerBusinessProblem = field("CustomerBusinessProblem")
    CustomerUseCase = field("CustomerUseCase")
    RelatedOpportunityIdentifier = field("RelatedOpportunityIdentifier")
    SalesActivities = field("SalesActivities")
    CompetitorName = field("CompetitorName")
    OtherCompetitorNames = field("OtherCompetitorNames")
    OtherSolutionDescription = field("OtherSolutionDescription")
    AdditionalComments = field("AdditionalComments")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProjectOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProjectOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProjectSummary:
    boto3_raw_data: "type_defs.ProjectSummaryTypeDef" = dataclasses.field()

    DeliveryModels = field("DeliveryModels")

    @cached_property
    def ExpectedCustomerSpend(self):  # pragma: no cover
        return ExpectedCustomerSpend.make_many(
            self.boto3_raw_data["ExpectedCustomerSpend"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProjectSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProjectSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Project:
    boto3_raw_data: "type_defs.ProjectTypeDef" = dataclasses.field()

    DeliveryModels = field("DeliveryModels")

    @cached_property
    def ExpectedCustomerSpend(self):  # pragma: no cover
        return ExpectedCustomerSpend.make_many(
            self.boto3_raw_data["ExpectedCustomerSpend"]
        )

    Title = field("Title")
    ApnPrograms = field("ApnPrograms")
    CustomerBusinessProblem = field("CustomerBusinessProblem")
    CustomerUseCase = field("CustomerUseCase")
    RelatedOpportunityIdentifier = field("RelatedOpportunityIdentifier")
    SalesActivities = field("SalesActivities")
    CompetitorName = field("CompetitorName")
    OtherCompetitorNames = field("OtherCompetitorNames")
    OtherSolutionDescription = field("OtherSolutionDescription")
    AdditionalComments = field("AdditionalComments")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProjectTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProjectTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProjectView:
    boto3_raw_data: "type_defs.ProjectViewTypeDef" = dataclasses.field()

    DeliveryModels = field("DeliveryModels")

    @cached_property
    def ExpectedCustomerSpend(self):  # pragma: no cover
        return ExpectedCustomerSpend.make_many(
            self.boto3_raw_data["ExpectedCustomerSpend"]
        )

    CustomerUseCase = field("CustomerUseCase")
    SalesActivities = field("SalesActivities")
    OtherSolutionDescription = field("OtherSolutionDescription")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProjectViewTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProjectViewTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEngagementInvitationResponse:
    boto3_raw_data: "type_defs.CreateEngagementInvitationResponseTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    Arn = field("Arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateEngagementInvitationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEngagementInvitationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEngagementResponse:
    boto3_raw_data: "type_defs.CreateEngagementResponseTypeDef" = dataclasses.field()

    Id = field("Id")
    Arn = field("Arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEngagementResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEngagementResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateOpportunityResponse:
    boto3_raw_data: "type_defs.CreateOpportunityResponseTypeDef" = dataclasses.field()

    Id = field("Id")
    PartnerOpportunityIdentifier = field("PartnerOpportunityIdentifier")
    LastModifiedDate = field("LastModifiedDate")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateOpportunityResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateOpportunityResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateResourceSnapshotJobResponse:
    boto3_raw_data: "type_defs.CreateResourceSnapshotJobResponseTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    Arn = field("Arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateResourceSnapshotJobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateResourceSnapshotJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateResourceSnapshotResponse:
    boto3_raw_data: "type_defs.CreateResourceSnapshotResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    Revision = field("Revision")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateResourceSnapshotResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateResourceSnapshotResponseTypeDef"]
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
class GetResourceSnapshotJobResponse:
    boto3_raw_data: "type_defs.GetResourceSnapshotJobResponseTypeDef" = (
        dataclasses.field()
    )

    Catalog = field("Catalog")
    Id = field("Id")
    Arn = field("Arn")
    EngagementId = field("EngagementId")
    ResourceType = field("ResourceType")
    ResourceId = field("ResourceId")
    ResourceArn = field("ResourceArn")
    ResourceSnapshotTemplateName = field("ResourceSnapshotTemplateName")
    CreatedAt = field("CreatedAt")
    Status = field("Status")
    LastSuccessfulExecutionDate = field("LastSuccessfulExecutionDate")
    LastFailure = field("LastFailure")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetResourceSnapshotJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourceSnapshotJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSellingSystemSettingsResponse:
    boto3_raw_data: "type_defs.GetSellingSystemSettingsResponseTypeDef" = (
        dataclasses.field()
    )

    Catalog = field("Catalog")
    ResourceSnapshotJobRoleArn = field("ResourceSnapshotJobRoleArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetSellingSystemSettingsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSellingSystemSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutSellingSystemSettingsResponse:
    boto3_raw_data: "type_defs.PutSellingSystemSettingsResponseTypeDef" = (
        dataclasses.field()
    )

    Catalog = field("Catalog")
    ResourceSnapshotJobRoleArn = field("ResourceSnapshotJobRoleArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutSellingSystemSettingsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutSellingSystemSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartEngagementByAcceptingInvitationTaskResponse:
    boto3_raw_data: (
        "type_defs.StartEngagementByAcceptingInvitationTaskResponseTypeDef"
    ) = dataclasses.field()

    TaskId = field("TaskId")
    TaskArn = field("TaskArn")
    StartTime = field("StartTime")
    TaskStatus = field("TaskStatus")
    Message = field("Message")
    ReasonCode = field("ReasonCode")
    OpportunityId = field("OpportunityId")
    ResourceSnapshotJobId = field("ResourceSnapshotJobId")
    EngagementInvitationId = field("EngagementInvitationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartEngagementByAcceptingInvitationTaskResponseTypeDef"
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
                "type_defs.StartEngagementByAcceptingInvitationTaskResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartEngagementFromOpportunityTaskResponse:
    boto3_raw_data: "type_defs.StartEngagementFromOpportunityTaskResponseTypeDef" = (
        dataclasses.field()
    )

    TaskId = field("TaskId")
    TaskArn = field("TaskArn")
    StartTime = field("StartTime")
    TaskStatus = field("TaskStatus")
    Message = field("Message")
    ReasonCode = field("ReasonCode")
    OpportunityId = field("OpportunityId")
    ResourceSnapshotJobId = field("ResourceSnapshotJobId")
    EngagementId = field("EngagementId")
    EngagementInvitationId = field("EngagementInvitationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartEngagementFromOpportunityTaskResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartEngagementFromOpportunityTaskResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateOpportunityResponse:
    boto3_raw_data: "type_defs.UpdateOpportunityResponseTypeDef" = dataclasses.field()

    Id = field("Id")
    LastModifiedDate = field("LastModifiedDate")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateOpportunityResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateOpportunityResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateResourceSnapshotJobRequest:
    boto3_raw_data: "type_defs.CreateResourceSnapshotJobRequestTypeDef" = (
        dataclasses.field()
    )

    Catalog = field("Catalog")
    ClientToken = field("ClientToken")
    EngagementIdentifier = field("EngagementIdentifier")
    ResourceType = field("ResourceType")
    ResourceIdentifier = field("ResourceIdentifier")
    ResourceSnapshotTemplateIdentifier = field("ResourceSnapshotTemplateIdentifier")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateResourceSnapshotJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateResourceSnapshotJobRequestTypeDef"]
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
class StartEngagementByAcceptingInvitationTaskRequest:
    boto3_raw_data: (
        "type_defs.StartEngagementByAcceptingInvitationTaskRequestTypeDef"
    ) = dataclasses.field()

    Catalog = field("Catalog")
    ClientToken = field("ClientToken")
    Identifier = field("Identifier")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartEngagementByAcceptingInvitationTaskRequestTypeDef"
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
                "type_defs.StartEngagementByAcceptingInvitationTaskRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartEngagementFromOpportunityTaskRequest:
    boto3_raw_data: "type_defs.StartEngagementFromOpportunityTaskRequestTypeDef" = (
        dataclasses.field()
    )

    Catalog = field("Catalog")
    ClientToken = field("ClientToken")
    Identifier = field("Identifier")

    @cached_property
    def AwsSubmission(self):  # pragma: no cover
        return AwsSubmission.make_one(self.boto3_raw_data["AwsSubmission"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartEngagementFromOpportunityTaskRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartEngagementFromOpportunityTaskRequestTypeDef"]
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
class CustomerProjectsContext:
    boto3_raw_data: "type_defs.CustomerProjectsContextTypeDef" = dataclasses.field()

    @cached_property
    def Customer(self):  # pragma: no cover
        return EngagementCustomer.make_one(self.boto3_raw_data["Customer"])

    @cached_property
    def Project(self):  # pragma: no cover
        return EngagementCustomerProjectDetails.make_one(self.boto3_raw_data["Project"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomerProjectsContextTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomerProjectsContextTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEngagementMembersResponse:
    boto3_raw_data: "type_defs.ListEngagementMembersResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EngagementMemberList(self):  # pragma: no cover
        return EngagementMember.make_many(self.boto3_raw_data["EngagementMemberList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListEngagementMembersResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEngagementMembersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEngagementResourceAssociationsResponse:
    boto3_raw_data: "type_defs.ListEngagementResourceAssociationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EngagementResourceAssociationSummaries(self):  # pragma: no cover
        return EngagementResourceAssociationSummary.make_many(
            self.boto3_raw_data["EngagementResourceAssociationSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEngagementResourceAssociationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEngagementResourceAssociationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEngagementsRequest:
    boto3_raw_data: "type_defs.ListEngagementsRequestTypeDef" = dataclasses.field()

    Catalog = field("Catalog")
    CreatedBy = field("CreatedBy")
    ExcludeCreatedBy = field("ExcludeCreatedBy")

    @cached_property
    def Sort(self):  # pragma: no cover
        return EngagementSort.make_one(self.boto3_raw_data["Sort"])

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    EngagementIdentifier = field("EngagementIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEngagementsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEngagementsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEngagementsResponse:
    boto3_raw_data: "type_defs.ListEngagementsResponseTypeDef" = dataclasses.field()

    @cached_property
    def EngagementSummaryList(self):  # pragma: no cover
        return EngagementSummary.make_many(self.boto3_raw_data["EngagementSummaryList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEngagementsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEngagementsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LastModifiedDate:
    boto3_raw_data: "type_defs.LastModifiedDateTypeDef" = dataclasses.field()

    AfterLastModifiedDate = field("AfterLastModifiedDate")
    BeforeLastModifiedDate = field("BeforeLastModifiedDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LastModifiedDateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LastModifiedDateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NextStepsHistory:
    boto3_raw_data: "type_defs.NextStepsHistoryTypeDef" = dataclasses.field()

    Value = field("Value")
    Time = field("Time")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NextStepsHistoryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NextStepsHistoryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifeCycleOutput:
    boto3_raw_data: "type_defs.LifeCycleOutputTypeDef" = dataclasses.field()

    Stage = field("Stage")
    ClosedLostReason = field("ClosedLostReason")
    NextSteps = field("NextSteps")
    TargetCloseDate = field("TargetCloseDate")
    ReviewStatus = field("ReviewStatus")
    ReviewComments = field("ReviewComments")
    ReviewStatusReason = field("ReviewStatusReason")

    @cached_property
    def NextStepsHistory(self):  # pragma: no cover
        return NextStepsHistoryOutput.make_many(self.boto3_raw_data["NextStepsHistory"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LifeCycleOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LifeCycleOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEngagementByAcceptingInvitationTasksResponse:
    boto3_raw_data: (
        "type_defs.ListEngagementByAcceptingInvitationTasksResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def TaskSummaries(self):  # pragma: no cover
        return ListEngagementByAcceptingInvitationTaskSummary.make_many(
            self.boto3_raw_data["TaskSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEngagementByAcceptingInvitationTasksResponseTypeDef"
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
                "type_defs.ListEngagementByAcceptingInvitationTasksResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEngagementByAcceptingInvitationTasksRequest:
    boto3_raw_data: (
        "type_defs.ListEngagementByAcceptingInvitationTasksRequestTypeDef"
    ) = dataclasses.field()

    Catalog = field("Catalog")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @cached_property
    def Sort(self):  # pragma: no cover
        return ListTasksSortBase.make_one(self.boto3_raw_data["Sort"])

    TaskStatus = field("TaskStatus")
    OpportunityIdentifier = field("OpportunityIdentifier")
    EngagementInvitationIdentifier = field("EngagementInvitationIdentifier")
    TaskIdentifier = field("TaskIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEngagementByAcceptingInvitationTasksRequestTypeDef"
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
                "type_defs.ListEngagementByAcceptingInvitationTasksRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEngagementFromOpportunityTasksRequest:
    boto3_raw_data: "type_defs.ListEngagementFromOpportunityTasksRequestTypeDef" = (
        dataclasses.field()
    )

    Catalog = field("Catalog")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @cached_property
    def Sort(self):  # pragma: no cover
        return ListTasksSortBase.make_one(self.boto3_raw_data["Sort"])

    TaskStatus = field("TaskStatus")
    TaskIdentifier = field("TaskIdentifier")
    OpportunityIdentifier = field("OpportunityIdentifier")
    EngagementIdentifier = field("EngagementIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEngagementFromOpportunityTasksRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEngagementFromOpportunityTasksRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEngagementByAcceptingInvitationTasksRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListEngagementByAcceptingInvitationTasksRequestPaginateTypeDef"
    ) = dataclasses.field()

    Catalog = field("Catalog")

    @cached_property
    def Sort(self):  # pragma: no cover
        return ListTasksSortBase.make_one(self.boto3_raw_data["Sort"])

    TaskStatus = field("TaskStatus")
    OpportunityIdentifier = field("OpportunityIdentifier")
    EngagementInvitationIdentifier = field("EngagementInvitationIdentifier")
    TaskIdentifier = field("TaskIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEngagementByAcceptingInvitationTasksRequestPaginateTypeDef"
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
                "type_defs.ListEngagementByAcceptingInvitationTasksRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEngagementFromOpportunityTasksRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListEngagementFromOpportunityTasksRequestPaginateTypeDef"
    ) = dataclasses.field()

    Catalog = field("Catalog")

    @cached_property
    def Sort(self):  # pragma: no cover
        return ListTasksSortBase.make_one(self.boto3_raw_data["Sort"])

    TaskStatus = field("TaskStatus")
    TaskIdentifier = field("TaskIdentifier")
    OpportunityIdentifier = field("OpportunityIdentifier")
    EngagementIdentifier = field("EngagementIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEngagementFromOpportunityTasksRequestPaginateTypeDef"
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
                "type_defs.ListEngagementFromOpportunityTasksRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEngagementMembersRequestPaginate:
    boto3_raw_data: "type_defs.ListEngagementMembersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    Catalog = field("Catalog")
    Identifier = field("Identifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEngagementMembersRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEngagementMembersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEngagementResourceAssociationsRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListEngagementResourceAssociationsRequestPaginateTypeDef"
    ) = dataclasses.field()

    Catalog = field("Catalog")
    EngagementIdentifier = field("EngagementIdentifier")
    ResourceType = field("ResourceType")
    ResourceIdentifier = field("ResourceIdentifier")
    CreatedBy = field("CreatedBy")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEngagementResourceAssociationsRequestPaginateTypeDef"
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
                "type_defs.ListEngagementResourceAssociationsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEngagementsRequestPaginate:
    boto3_raw_data: "type_defs.ListEngagementsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    Catalog = field("Catalog")
    CreatedBy = field("CreatedBy")
    ExcludeCreatedBy = field("ExcludeCreatedBy")

    @cached_property
    def Sort(self):  # pragma: no cover
        return EngagementSort.make_one(self.boto3_raw_data["Sort"])

    EngagementIdentifier = field("EngagementIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListEngagementsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEngagementsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceSnapshotsRequestPaginate:
    boto3_raw_data: "type_defs.ListResourceSnapshotsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    Catalog = field("Catalog")
    EngagementIdentifier = field("EngagementIdentifier")
    ResourceType = field("ResourceType")
    ResourceIdentifier = field("ResourceIdentifier")
    ResourceSnapshotTemplateIdentifier = field("ResourceSnapshotTemplateIdentifier")
    CreatedBy = field("CreatedBy")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResourceSnapshotsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceSnapshotsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEngagementFromOpportunityTasksResponse:
    boto3_raw_data: "type_defs.ListEngagementFromOpportunityTasksResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TaskSummaries(self):  # pragma: no cover
        return ListEngagementFromOpportunityTaskSummary.make_many(
            self.boto3_raw_data["TaskSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEngagementFromOpportunityTasksResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEngagementFromOpportunityTasksResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEngagementInvitationsRequestPaginate:
    boto3_raw_data: "type_defs.ListEngagementInvitationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    Catalog = field("Catalog")
    ParticipantType = field("ParticipantType")

    @cached_property
    def Sort(self):  # pragma: no cover
        return OpportunityEngagementInvitationSort.make_one(self.boto3_raw_data["Sort"])

    PayloadType = field("PayloadType")
    Status = field("Status")
    EngagementIdentifier = field("EngagementIdentifier")
    SenderAwsAccountId = field("SenderAwsAccountId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEngagementInvitationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEngagementInvitationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEngagementInvitationsRequest:
    boto3_raw_data: "type_defs.ListEngagementInvitationsRequestTypeDef" = (
        dataclasses.field()
    )

    Catalog = field("Catalog")
    ParticipantType = field("ParticipantType")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @cached_property
    def Sort(self):  # pragma: no cover
        return OpportunityEngagementInvitationSort.make_one(self.boto3_raw_data["Sort"])

    PayloadType = field("PayloadType")
    Status = field("Status")
    EngagementIdentifier = field("EngagementIdentifier")
    SenderAwsAccountId = field("SenderAwsAccountId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListEngagementInvitationsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEngagementInvitationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceSnapshotJobsRequestPaginate:
    boto3_raw_data: "type_defs.ListResourceSnapshotJobsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    Catalog = field("Catalog")
    EngagementIdentifier = field("EngagementIdentifier")
    Status = field("Status")

    @cached_property
    def Sort(self):  # pragma: no cover
        return SortObject.make_one(self.boto3_raw_data["Sort"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResourceSnapshotJobsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceSnapshotJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceSnapshotJobsRequest:
    boto3_raw_data: "type_defs.ListResourceSnapshotJobsRequestTypeDef" = (
        dataclasses.field()
    )

    Catalog = field("Catalog")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    EngagementIdentifier = field("EngagementIdentifier")
    Status = field("Status")

    @cached_property
    def Sort(self):  # pragma: no cover
        return SortObject.make_one(self.boto3_raw_data["Sort"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListResourceSnapshotJobsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceSnapshotJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceSnapshotJobsResponse:
    boto3_raw_data: "type_defs.ListResourceSnapshotJobsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ResourceSnapshotJobSummaries(self):  # pragma: no cover
        return ResourceSnapshotJobSummary.make_many(
            self.boto3_raw_data["ResourceSnapshotJobSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListResourceSnapshotJobsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceSnapshotJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceSnapshotsResponse:
    boto3_raw_data: "type_defs.ListResourceSnapshotsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ResourceSnapshotSummaries(self):  # pragma: no cover
        return ResourceSnapshotSummary.make_many(
            self.boto3_raw_data["ResourceSnapshotSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListResourceSnapshotsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceSnapshotsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSolutionsRequestPaginate:
    boto3_raw_data: "type_defs.ListSolutionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    Catalog = field("Catalog")

    @cached_property
    def Sort(self):  # pragma: no cover
        return SolutionSort.make_one(self.boto3_raw_data["Sort"])

    Status = field("Status")
    Identifier = field("Identifier")
    Category = field("Category")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSolutionsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSolutionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSolutionsRequest:
    boto3_raw_data: "type_defs.ListSolutionsRequestTypeDef" = dataclasses.field()

    Catalog = field("Catalog")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @cached_property
    def Sort(self):  # pragma: no cover
        return SolutionSort.make_one(self.boto3_raw_data["Sort"])

    Status = field("Status")
    Identifier = field("Identifier")
    Category = field("Category")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSolutionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSolutionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSolutionsResponse:
    boto3_raw_data: "type_defs.ListSolutionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def SolutionSummaries(self):  # pragma: no cover
        return SolutionBase.make_many(self.boto3_raw_data["SolutionSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSolutionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSolutionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SoftwareRevenue:
    boto3_raw_data: "type_defs.SoftwareRevenueTypeDef" = dataclasses.field()

    DeliveryModel = field("DeliveryModel")

    @cached_property
    def Value(self):  # pragma: no cover
        return MonetaryValue.make_one(self.boto3_raw_data["Value"])

    EffectiveDate = field("EffectiveDate")
    ExpirationDate = field("ExpirationDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SoftwareRevenueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SoftwareRevenueTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EngagementInvitationSummary:
    boto3_raw_data: "type_defs.EngagementInvitationSummaryTypeDef" = dataclasses.field()

    Id = field("Id")
    Catalog = field("Catalog")
    Arn = field("Arn")
    PayloadType = field("PayloadType")
    EngagementId = field("EngagementId")
    EngagementTitle = field("EngagementTitle")
    Status = field("Status")
    InvitationDate = field("InvitationDate")
    ExpirationDate = field("ExpirationDate")
    SenderAwsAccountId = field("SenderAwsAccountId")
    SenderCompanyName = field("SenderCompanyName")

    @cached_property
    def Receiver(self):  # pragma: no cover
        return Receiver.make_one(self.boto3_raw_data["Receiver"])

    ParticipantType = field("ParticipantType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EngagementInvitationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EngagementInvitationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomerSummary:
    boto3_raw_data: "type_defs.CustomerSummaryTypeDef" = dataclasses.field()

    @cached_property
    def Account(self):  # pragma: no cover
        return AccountSummary.make_one(self.boto3_raw_data["Account"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CustomerSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CustomerSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomerOutput:
    boto3_raw_data: "type_defs.CustomerOutputTypeDef" = dataclasses.field()

    @cached_property
    def Account(self):  # pragma: no cover
        return Account.make_one(self.boto3_raw_data["Account"])

    @cached_property
    def Contacts(self):  # pragma: no cover
        return Contact.make_many(self.boto3_raw_data["Contacts"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CustomerOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CustomerOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Customer:
    boto3_raw_data: "type_defs.CustomerTypeDef" = dataclasses.field()

    @cached_property
    def Account(self):  # pragma: no cover
        return Account.make_one(self.boto3_raw_data["Account"])

    @cached_property
    def Contacts(self):  # pragma: no cover
        return Contact.make_many(self.boto3_raw_data["Contacts"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CustomerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CustomerTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAwsOpportunitySummaryResponse:
    boto3_raw_data: "type_defs.GetAwsOpportunitySummaryResponseTypeDef" = (
        dataclasses.field()
    )

    Catalog = field("Catalog")
    RelatedOpportunityId = field("RelatedOpportunityId")
    Origin = field("Origin")
    InvolvementType = field("InvolvementType")
    Visibility = field("Visibility")

    @cached_property
    def LifeCycle(self):  # pragma: no cover
        return AwsOpportunityLifeCycle.make_one(self.boto3_raw_data["LifeCycle"])

    @cached_property
    def OpportunityTeam(self):  # pragma: no cover
        return AwsTeamMember.make_many(self.boto3_raw_data["OpportunityTeam"])

    @cached_property
    def Insights(self):  # pragma: no cover
        return AwsOpportunityInsights.make_one(self.boto3_raw_data["Insights"])

    InvolvementTypeChangeReason = field("InvolvementTypeChangeReason")

    @cached_property
    def RelatedEntityIds(self):  # pragma: no cover
        return AwsOpportunityRelatedEntities.make_one(
            self.boto3_raw_data["RelatedEntityIds"]
        )

    @cached_property
    def Customer(self):  # pragma: no cover
        return AwsOpportunityCustomer.make_one(self.boto3_raw_data["Customer"])

    @cached_property
    def Project(self):  # pragma: no cover
        return AwsOpportunityProject.make_one(self.boto3_raw_data["Project"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetAwsOpportunitySummaryResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAwsOpportunitySummaryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpportunityInvitationPayloadOutput:
    boto3_raw_data: "type_defs.OpportunityInvitationPayloadOutputTypeDef" = (
        dataclasses.field()
    )

    ReceiverResponsibilities = field("ReceiverResponsibilities")

    @cached_property
    def Customer(self):  # pragma: no cover
        return EngagementCustomer.make_one(self.boto3_raw_data["Customer"])

    @cached_property
    def Project(self):  # pragma: no cover
        return ProjectDetailsOutput.make_one(self.boto3_raw_data["Project"])

    @cached_property
    def SenderContacts(self):  # pragma: no cover
        return SenderContact.make_many(self.boto3_raw_data["SenderContacts"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OpportunityInvitationPayloadOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpportunityInvitationPayloadOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EngagementContextPayload:
    boto3_raw_data: "type_defs.EngagementContextPayloadTypeDef" = dataclasses.field()

    @cached_property
    def CustomerProject(self):  # pragma: no cover
        return CustomerProjectsContext.make_one(self.boto3_raw_data["CustomerProject"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EngagementContextPayloadTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EngagementContextPayloadTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOpportunitiesRequestPaginate:
    boto3_raw_data: "type_defs.ListOpportunitiesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    Catalog = field("Catalog")

    @cached_property
    def Sort(self):  # pragma: no cover
        return OpportunitySort.make_one(self.boto3_raw_data["Sort"])

    @cached_property
    def LastModifiedDate(self):  # pragma: no cover
        return LastModifiedDate.make_one(self.boto3_raw_data["LastModifiedDate"])

    Identifier = field("Identifier")
    LifeCycleStage = field("LifeCycleStage")
    LifeCycleReviewStatus = field("LifeCycleReviewStatus")
    CustomerCompanyName = field("CustomerCompanyName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListOpportunitiesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOpportunitiesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOpportunitiesRequest:
    boto3_raw_data: "type_defs.ListOpportunitiesRequestTypeDef" = dataclasses.field()

    Catalog = field("Catalog")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @cached_property
    def Sort(self):  # pragma: no cover
        return OpportunitySort.make_one(self.boto3_raw_data["Sort"])

    @cached_property
    def LastModifiedDate(self):  # pragma: no cover
        return LastModifiedDate.make_one(self.boto3_raw_data["LastModifiedDate"])

    Identifier = field("Identifier")
    LifeCycleStage = field("LifeCycleStage")
    LifeCycleReviewStatus = field("LifeCycleReviewStatus")
    CustomerCompanyName = field("CustomerCompanyName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListOpportunitiesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOpportunitiesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifeCycle:
    boto3_raw_data: "type_defs.LifeCycleTypeDef" = dataclasses.field()

    Stage = field("Stage")
    ClosedLostReason = field("ClosedLostReason")
    NextSteps = field("NextSteps")
    TargetCloseDate = field("TargetCloseDate")
    ReviewStatus = field("ReviewStatus")
    ReviewComments = field("ReviewComments")
    ReviewStatusReason = field("ReviewStatusReason")

    @cached_property
    def NextStepsHistory(self):  # pragma: no cover
        return NextStepsHistory.make_many(self.boto3_raw_data["NextStepsHistory"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LifeCycleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LifeCycleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEngagementInvitationsResponse:
    boto3_raw_data: "type_defs.ListEngagementInvitationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EngagementInvitationSummaries(self):  # pragma: no cover
        return EngagementInvitationSummary.make_many(
            self.boto3_raw_data["EngagementInvitationSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEngagementInvitationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEngagementInvitationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpportunitySummary:
    boto3_raw_data: "type_defs.OpportunitySummaryTypeDef" = dataclasses.field()

    Catalog = field("Catalog")
    Id = field("Id")
    Arn = field("Arn")
    PartnerOpportunityIdentifier = field("PartnerOpportunityIdentifier")
    OpportunityType = field("OpportunityType")
    LastModifiedDate = field("LastModifiedDate")
    CreatedDate = field("CreatedDate")

    @cached_property
    def LifeCycle(self):  # pragma: no cover
        return LifeCycleSummary.make_one(self.boto3_raw_data["LifeCycle"])

    @cached_property
    def Customer(self):  # pragma: no cover
        return CustomerSummary.make_one(self.boto3_raw_data["Customer"])

    @cached_property
    def Project(self):  # pragma: no cover
        return ProjectSummary.make_one(self.boto3_raw_data["Project"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OpportunitySummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpportunitySummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOpportunityResponse:
    boto3_raw_data: "type_defs.GetOpportunityResponseTypeDef" = dataclasses.field()

    Catalog = field("Catalog")
    PrimaryNeedsFromAws = field("PrimaryNeedsFromAws")
    NationalSecurity = field("NationalSecurity")
    PartnerOpportunityIdentifier = field("PartnerOpportunityIdentifier")

    @cached_property
    def Customer(self):  # pragma: no cover
        return CustomerOutput.make_one(self.boto3_raw_data["Customer"])

    @cached_property
    def Project(self):  # pragma: no cover
        return ProjectOutput.make_one(self.boto3_raw_data["Project"])

    OpportunityType = field("OpportunityType")

    @cached_property
    def Marketing(self):  # pragma: no cover
        return MarketingOutput.make_one(self.boto3_raw_data["Marketing"])

    @cached_property
    def SoftwareRevenue(self):  # pragma: no cover
        return SoftwareRevenue.make_one(self.boto3_raw_data["SoftwareRevenue"])

    Id = field("Id")
    Arn = field("Arn")
    LastModifiedDate = field("LastModifiedDate")
    CreatedDate = field("CreatedDate")

    @cached_property
    def RelatedEntityIdentifiers(self):  # pragma: no cover
        return RelatedEntityIdentifiers.make_one(
            self.boto3_raw_data["RelatedEntityIdentifiers"]
        )

    @cached_property
    def LifeCycle(self):  # pragma: no cover
        return LifeCycleOutput.make_one(self.boto3_raw_data["LifeCycle"])

    @cached_property
    def OpportunityTeam(self):  # pragma: no cover
        return Contact.make_many(self.boto3_raw_data["OpportunityTeam"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetOpportunityResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOpportunityResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpportunitySummaryView:
    boto3_raw_data: "type_defs.OpportunitySummaryViewTypeDef" = dataclasses.field()

    OpportunityType = field("OpportunityType")

    @cached_property
    def Lifecycle(self):  # pragma: no cover
        return LifeCycleForView.make_one(self.boto3_raw_data["Lifecycle"])

    @cached_property
    def OpportunityTeam(self):  # pragma: no cover
        return Contact.make_many(self.boto3_raw_data["OpportunityTeam"])

    PrimaryNeedsFromAws = field("PrimaryNeedsFromAws")

    @cached_property
    def Customer(self):  # pragma: no cover
        return CustomerOutput.make_one(self.boto3_raw_data["Customer"])

    @cached_property
    def Project(self):  # pragma: no cover
        return ProjectView.make_one(self.boto3_raw_data["Project"])

    @cached_property
    def RelatedEntityIdentifiers(self):  # pragma: no cover
        return RelatedEntityIdentifiers.make_one(
            self.boto3_raw_data["RelatedEntityIdentifiers"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OpportunitySummaryViewTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpportunitySummaryViewTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PayloadOutput:
    boto3_raw_data: "type_defs.PayloadOutputTypeDef" = dataclasses.field()

    @cached_property
    def OpportunityInvitation(self):  # pragma: no cover
        return OpportunityInvitationPayloadOutput.make_one(
            self.boto3_raw_data["OpportunityInvitation"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PayloadOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PayloadOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpportunityInvitationPayload:
    boto3_raw_data: "type_defs.OpportunityInvitationPayloadTypeDef" = (
        dataclasses.field()
    )

    ReceiverResponsibilities = field("ReceiverResponsibilities")

    @cached_property
    def Customer(self):  # pragma: no cover
        return EngagementCustomer.make_one(self.boto3_raw_data["Customer"])

    Project = field("Project")

    @cached_property
    def SenderContacts(self):  # pragma: no cover
        return SenderContact.make_many(self.boto3_raw_data["SenderContacts"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OpportunityInvitationPayloadTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpportunityInvitationPayloadTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EngagementContextDetails:
    boto3_raw_data: "type_defs.EngagementContextDetailsTypeDef" = dataclasses.field()

    Type = field("Type")

    @cached_property
    def Payload(self):  # pragma: no cover
        return EngagementContextPayload.make_one(self.boto3_raw_data["Payload"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EngagementContextDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EngagementContextDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOpportunitiesResponse:
    boto3_raw_data: "type_defs.ListOpportunitiesResponseTypeDef" = dataclasses.field()

    @cached_property
    def OpportunitySummaries(self):  # pragma: no cover
        return OpportunitySummary.make_many(self.boto3_raw_data["OpportunitySummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListOpportunitiesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOpportunitiesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceSnapshotPayload:
    boto3_raw_data: "type_defs.ResourceSnapshotPayloadTypeDef" = dataclasses.field()

    @cached_property
    def OpportunitySummary(self):  # pragma: no cover
        return OpportunitySummaryView.make_one(
            self.boto3_raw_data["OpportunitySummary"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceSnapshotPayloadTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceSnapshotPayloadTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEngagementInvitationResponse:
    boto3_raw_data: "type_defs.GetEngagementInvitationResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    PayloadType = field("PayloadType")
    Id = field("Id")
    EngagementId = field("EngagementId")
    EngagementTitle = field("EngagementTitle")
    Status = field("Status")
    InvitationDate = field("InvitationDate")
    ExpirationDate = field("ExpirationDate")
    SenderAwsAccountId = field("SenderAwsAccountId")
    SenderCompanyName = field("SenderCompanyName")

    @cached_property
    def Receiver(self):  # pragma: no cover
        return Receiver.make_one(self.boto3_raw_data["Receiver"])

    Catalog = field("Catalog")
    RejectionReason = field("RejectionReason")

    @cached_property
    def Payload(self):  # pragma: no cover
        return PayloadOutput.make_one(self.boto3_raw_data["Payload"])

    InvitationMessage = field("InvitationMessage")
    EngagementDescription = field("EngagementDescription")

    @cached_property
    def ExistingMembers(self):  # pragma: no cover
        return EngagementMemberSummary.make_many(self.boto3_raw_data["ExistingMembers"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetEngagementInvitationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEngagementInvitationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEngagementRequest:
    boto3_raw_data: "type_defs.CreateEngagementRequestTypeDef" = dataclasses.field()

    Catalog = field("Catalog")
    ClientToken = field("ClientToken")
    Title = field("Title")
    Description = field("Description")

    @cached_property
    def Contexts(self):  # pragma: no cover
        return EngagementContextDetails.make_many(self.boto3_raw_data["Contexts"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEngagementRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEngagementRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEngagementResponse:
    boto3_raw_data: "type_defs.GetEngagementResponseTypeDef" = dataclasses.field()

    Id = field("Id")
    Arn = field("Arn")
    Title = field("Title")
    Description = field("Description")
    CreatedAt = field("CreatedAt")
    CreatedBy = field("CreatedBy")
    MemberCount = field("MemberCount")

    @cached_property
    def Contexts(self):  # pragma: no cover
        return EngagementContextDetails.make_many(self.boto3_raw_data["Contexts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEngagementResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEngagementResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateOpportunityRequest:
    boto3_raw_data: "type_defs.CreateOpportunityRequestTypeDef" = dataclasses.field()

    Catalog = field("Catalog")
    ClientToken = field("ClientToken")
    PrimaryNeedsFromAws = field("PrimaryNeedsFromAws")
    NationalSecurity = field("NationalSecurity")
    PartnerOpportunityIdentifier = field("PartnerOpportunityIdentifier")
    Customer = field("Customer")
    Project = field("Project")
    OpportunityType = field("OpportunityType")
    Marketing = field("Marketing")

    @cached_property
    def SoftwareRevenue(self):  # pragma: no cover
        return SoftwareRevenue.make_one(self.boto3_raw_data["SoftwareRevenue"])

    LifeCycle = field("LifeCycle")
    Origin = field("Origin")

    @cached_property
    def OpportunityTeam(self):  # pragma: no cover
        return Contact.make_many(self.boto3_raw_data["OpportunityTeam"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateOpportunityRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateOpportunityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateOpportunityRequest:
    boto3_raw_data: "type_defs.UpdateOpportunityRequestTypeDef" = dataclasses.field()

    Catalog = field("Catalog")
    LastModifiedDate = field("LastModifiedDate")
    Identifier = field("Identifier")
    PrimaryNeedsFromAws = field("PrimaryNeedsFromAws")
    NationalSecurity = field("NationalSecurity")
    PartnerOpportunityIdentifier = field("PartnerOpportunityIdentifier")
    Customer = field("Customer")
    Project = field("Project")
    OpportunityType = field("OpportunityType")
    Marketing = field("Marketing")

    @cached_property
    def SoftwareRevenue(self):  # pragma: no cover
        return SoftwareRevenue.make_one(self.boto3_raw_data["SoftwareRevenue"])

    LifeCycle = field("LifeCycle")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateOpportunityRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateOpportunityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourceSnapshotResponse:
    boto3_raw_data: "type_defs.GetResourceSnapshotResponseTypeDef" = dataclasses.field()

    Catalog = field("Catalog")
    Arn = field("Arn")
    CreatedBy = field("CreatedBy")
    CreatedAt = field("CreatedAt")
    EngagementId = field("EngagementId")
    ResourceType = field("ResourceType")
    ResourceId = field("ResourceId")
    ResourceSnapshotTemplateName = field("ResourceSnapshotTemplateName")
    Revision = field("Revision")

    @cached_property
    def Payload(self):  # pragma: no cover
        return ResourceSnapshotPayload.make_one(self.boto3_raw_data["Payload"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourceSnapshotResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourceSnapshotResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Payload:
    boto3_raw_data: "type_defs.PayloadTypeDef" = dataclasses.field()

    OpportunityInvitation = field("OpportunityInvitation")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PayloadTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PayloadTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Invitation:
    boto3_raw_data: "type_defs.InvitationTypeDef" = dataclasses.field()

    Message = field("Message")

    @cached_property
    def Receiver(self):  # pragma: no cover
        return Receiver.make_one(self.boto3_raw_data["Receiver"])

    Payload = field("Payload")

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
class CreateEngagementInvitationRequest:
    boto3_raw_data: "type_defs.CreateEngagementInvitationRequestTypeDef" = (
        dataclasses.field()
    )

    Catalog = field("Catalog")
    ClientToken = field("ClientToken")
    EngagementIdentifier = field("EngagementIdentifier")

    @cached_property
    def Invitation(self):  # pragma: no cover
        return Invitation.make_one(self.boto3_raw_data["Invitation"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateEngagementInvitationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEngagementInvitationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]

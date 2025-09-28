# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_servicecatalog import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AcceptPortfolioShareInput:
    boto3_raw_data: "type_defs.AcceptPortfolioShareInputTypeDef" = dataclasses.field()

    PortfolioId = field("PortfolioId")
    AcceptLanguage = field("AcceptLanguage")
    PortfolioShareType = field("PortfolioShareType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AcceptPortfolioShareInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AcceptPortfolioShareInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccessLevelFilter:
    boto3_raw_data: "type_defs.AccessLevelFilterTypeDef" = dataclasses.field()

    Key = field("Key")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccessLevelFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccessLevelFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateBudgetWithResourceInput:
    boto3_raw_data: "type_defs.AssociateBudgetWithResourceInputTypeDef" = (
        dataclasses.field()
    )

    BudgetName = field("BudgetName")
    ResourceId = field("ResourceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssociateBudgetWithResourceInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateBudgetWithResourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociatePrincipalWithPortfolioInput:
    boto3_raw_data: "type_defs.AssociatePrincipalWithPortfolioInputTypeDef" = (
        dataclasses.field()
    )

    PortfolioId = field("PortfolioId")
    PrincipalARN = field("PrincipalARN")
    PrincipalType = field("PrincipalType")
    AcceptLanguage = field("AcceptLanguage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociatePrincipalWithPortfolioInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociatePrincipalWithPortfolioInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateProductWithPortfolioInput:
    boto3_raw_data: "type_defs.AssociateProductWithPortfolioInputTypeDef" = (
        dataclasses.field()
    )

    ProductId = field("ProductId")
    PortfolioId = field("PortfolioId")
    AcceptLanguage = field("AcceptLanguage")
    SourcePortfolioId = field("SourcePortfolioId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateProductWithPortfolioInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateProductWithPortfolioInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateServiceActionWithProvisioningArtifactInput:
    boto3_raw_data: (
        "type_defs.AssociateServiceActionWithProvisioningArtifactInputTypeDef"
    ) = dataclasses.field()

    ProductId = field("ProductId")
    ProvisioningArtifactId = field("ProvisioningArtifactId")
    ServiceActionId = field("ServiceActionId")
    AcceptLanguage = field("AcceptLanguage")
    IdempotencyToken = field("IdempotencyToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateServiceActionWithProvisioningArtifactInputTypeDef"
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
                "type_defs.AssociateServiceActionWithProvisioningArtifactInputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateTagOptionWithResourceInput:
    boto3_raw_data: "type_defs.AssociateTagOptionWithResourceInputTypeDef" = (
        dataclasses.field()
    )

    ResourceId = field("ResourceId")
    TagOptionId = field("TagOptionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateTagOptionWithResourceInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateTagOptionWithResourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceActionAssociation:
    boto3_raw_data: "type_defs.ServiceActionAssociationTypeDef" = dataclasses.field()

    ServiceActionId = field("ServiceActionId")
    ProductId = field("ProductId")
    ProvisioningArtifactId = field("ProvisioningArtifactId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServiceActionAssociationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceActionAssociationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailedServiceActionAssociation:
    boto3_raw_data: "type_defs.FailedServiceActionAssociationTypeDef" = (
        dataclasses.field()
    )

    ServiceActionId = field("ServiceActionId")
    ProductId = field("ProductId")
    ProvisioningArtifactId = field("ProvisioningArtifactId")
    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.FailedServiceActionAssociationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FailedServiceActionAssociationTypeDef"]
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
class BudgetDetail:
    boto3_raw_data: "type_defs.BudgetDetailTypeDef" = dataclasses.field()

    BudgetName = field("BudgetName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BudgetDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BudgetDetailTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudWatchDashboard:
    boto3_raw_data: "type_defs.CloudWatchDashboardTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CloudWatchDashboardTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudWatchDashboardTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodeStarParameters:
    boto3_raw_data: "type_defs.CodeStarParametersTypeDef" = dataclasses.field()

    ConnectionArn = field("ConnectionArn")
    Repository = field("Repository")
    Branch = field("Branch")
    ArtifactPath = field("ArtifactPath")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CodeStarParametersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodeStarParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConstraintDetail:
    boto3_raw_data: "type_defs.ConstraintDetailTypeDef" = dataclasses.field()

    ConstraintId = field("ConstraintId")
    Type = field("Type")
    Description = field("Description")
    Owner = field("Owner")
    ProductId = field("ProductId")
    PortfolioId = field("PortfolioId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConstraintDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConstraintDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConstraintSummary:
    boto3_raw_data: "type_defs.ConstraintSummaryTypeDef" = dataclasses.field()

    Type = field("Type")
    Description = field("Description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConstraintSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConstraintSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopyProductInput:
    boto3_raw_data: "type_defs.CopyProductInputTypeDef" = dataclasses.field()

    SourceProductArn = field("SourceProductArn")
    IdempotencyToken = field("IdempotencyToken")
    AcceptLanguage = field("AcceptLanguage")
    TargetProductId = field("TargetProductId")
    TargetProductName = field("TargetProductName")
    SourceProvisioningArtifactIdentifiers = field(
        "SourceProvisioningArtifactIdentifiers"
    )
    CopyOptions = field("CopyOptions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CopyProductInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CopyProductInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConstraintInput:
    boto3_raw_data: "type_defs.CreateConstraintInputTypeDef" = dataclasses.field()

    PortfolioId = field("PortfolioId")
    ProductId = field("ProductId")
    Parameters = field("Parameters")
    Type = field("Type")
    IdempotencyToken = field("IdempotencyToken")
    AcceptLanguage = field("AcceptLanguage")
    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateConstraintInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConstraintInputTypeDef"]
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
class PortfolioDetail:
    boto3_raw_data: "type_defs.PortfolioDetailTypeDef" = dataclasses.field()

    Id = field("Id")
    ARN = field("ARN")
    DisplayName = field("DisplayName")
    Description = field("Description")
    CreatedTime = field("CreatedTime")
    ProviderName = field("ProviderName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PortfolioDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PortfolioDetailTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrganizationNode:
    boto3_raw_data: "type_defs.OrganizationNodeTypeDef" = dataclasses.field()

    Type = field("Type")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OrganizationNodeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrganizationNodeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProvisioningArtifactProperties:
    boto3_raw_data: "type_defs.ProvisioningArtifactPropertiesTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Description = field("Description")
    Info = field("Info")
    Type = field("Type")
    DisableTemplateValidation = field("DisableTemplateValidation")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ProvisioningArtifactPropertiesTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProvisioningArtifactPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProvisioningArtifactDetail:
    boto3_raw_data: "type_defs.ProvisioningArtifactDetailTypeDef" = dataclasses.field()

    Id = field("Id")
    Name = field("Name")
    Description = field("Description")
    Type = field("Type")
    CreatedTime = field("CreatedTime")
    Active = field("Active")
    Guidance = field("Guidance")
    SourceRevision = field("SourceRevision")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProvisioningArtifactDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProvisioningArtifactDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateProvisioningParameter:
    boto3_raw_data: "type_defs.UpdateProvisioningParameterTypeDef" = dataclasses.field()

    Key = field("Key")
    Value = field("Value")
    UsePreviousValue = field("UsePreviousValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateProvisioningParameterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateProvisioningParameterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateServiceActionInput:
    boto3_raw_data: "type_defs.CreateServiceActionInputTypeDef" = dataclasses.field()

    Name = field("Name")
    DefinitionType = field("DefinitionType")
    Definition = field("Definition")
    IdempotencyToken = field("IdempotencyToken")
    Description = field("Description")
    AcceptLanguage = field("AcceptLanguage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateServiceActionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateServiceActionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTagOptionInput:
    boto3_raw_data: "type_defs.CreateTagOptionInputTypeDef" = dataclasses.field()

    Key = field("Key")
    Value = field("Value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTagOptionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTagOptionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagOptionDetail:
    boto3_raw_data: "type_defs.TagOptionDetailTypeDef" = dataclasses.field()

    Key = field("Key")
    Value = field("Value")
    Active = field("Active")
    Id = field("Id")
    Owner = field("Owner")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagOptionDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagOptionDetailTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteConstraintInput:
    boto3_raw_data: "type_defs.DeleteConstraintInputTypeDef" = dataclasses.field()

    Id = field("Id")
    AcceptLanguage = field("AcceptLanguage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteConstraintInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteConstraintInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePortfolioInput:
    boto3_raw_data: "type_defs.DeletePortfolioInputTypeDef" = dataclasses.field()

    Id = field("Id")
    AcceptLanguage = field("AcceptLanguage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePortfolioInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePortfolioInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteProductInput:
    boto3_raw_data: "type_defs.DeleteProductInputTypeDef" = dataclasses.field()

    Id = field("Id")
    AcceptLanguage = field("AcceptLanguage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteProductInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteProductInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteProvisionedProductPlanInput:
    boto3_raw_data: "type_defs.DeleteProvisionedProductPlanInputTypeDef" = (
        dataclasses.field()
    )

    PlanId = field("PlanId")
    AcceptLanguage = field("AcceptLanguage")
    IgnoreErrors = field("IgnoreErrors")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteProvisionedProductPlanInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteProvisionedProductPlanInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteProvisioningArtifactInput:
    boto3_raw_data: "type_defs.DeleteProvisioningArtifactInputTypeDef" = (
        dataclasses.field()
    )

    ProductId = field("ProductId")
    ProvisioningArtifactId = field("ProvisioningArtifactId")
    AcceptLanguage = field("AcceptLanguage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteProvisioningArtifactInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteProvisioningArtifactInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteServiceActionInput:
    boto3_raw_data: "type_defs.DeleteServiceActionInputTypeDef" = dataclasses.field()

    Id = field("Id")
    AcceptLanguage = field("AcceptLanguage")
    IdempotencyToken = field("IdempotencyToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteServiceActionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteServiceActionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTagOptionInput:
    boto3_raw_data: "type_defs.DeleteTagOptionInputTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteTagOptionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTagOptionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConstraintInput:
    boto3_raw_data: "type_defs.DescribeConstraintInputTypeDef" = dataclasses.field()

    Id = field("Id")
    AcceptLanguage = field("AcceptLanguage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeConstraintInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConstraintInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCopyProductStatusInput:
    boto3_raw_data: "type_defs.DescribeCopyProductStatusInputTypeDef" = (
        dataclasses.field()
    )

    CopyProductToken = field("CopyProductToken")
    AcceptLanguage = field("AcceptLanguage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeCopyProductStatusInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCopyProductStatusInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePortfolioInput:
    boto3_raw_data: "type_defs.DescribePortfolioInputTypeDef" = dataclasses.field()

    Id = field("Id")
    AcceptLanguage = field("AcceptLanguage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribePortfolioInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePortfolioInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePortfolioShareStatusInput:
    boto3_raw_data: "type_defs.DescribePortfolioShareStatusInputTypeDef" = (
        dataclasses.field()
    )

    PortfolioShareToken = field("PortfolioShareToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribePortfolioShareStatusInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePortfolioShareStatusInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePortfolioSharesInput:
    boto3_raw_data: "type_defs.DescribePortfolioSharesInputTypeDef" = (
        dataclasses.field()
    )

    PortfolioId = field("PortfolioId")
    Type = field("Type")
    PageToken = field("PageToken")
    PageSize = field("PageSize")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribePortfolioSharesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePortfolioSharesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PortfolioShareDetail:
    boto3_raw_data: "type_defs.PortfolioShareDetailTypeDef" = dataclasses.field()

    PrincipalId = field("PrincipalId")
    Type = field("Type")
    Accepted = field("Accepted")
    ShareTagOptions = field("ShareTagOptions")
    SharePrincipals = field("SharePrincipals")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PortfolioShareDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PortfolioShareDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeProductAsAdminInput:
    boto3_raw_data: "type_defs.DescribeProductAsAdminInputTypeDef" = dataclasses.field()

    AcceptLanguage = field("AcceptLanguage")
    Id = field("Id")
    Name = field("Name")
    SourcePortfolioId = field("SourcePortfolioId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeProductAsAdminInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeProductAsAdminInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProvisioningArtifactSummary:
    boto3_raw_data: "type_defs.ProvisioningArtifactSummaryTypeDef" = dataclasses.field()

    Id = field("Id")
    Name = field("Name")
    Description = field("Description")
    CreatedTime = field("CreatedTime")
    ProvisioningArtifactMetadata = field("ProvisioningArtifactMetadata")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProvisioningArtifactSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProvisioningArtifactSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeProductInput:
    boto3_raw_data: "type_defs.DescribeProductInputTypeDef" = dataclasses.field()

    AcceptLanguage = field("AcceptLanguage")
    Id = field("Id")
    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeProductInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeProductInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LaunchPath:
    boto3_raw_data: "type_defs.LaunchPathTypeDef" = dataclasses.field()

    Id = field("Id")
    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LaunchPathTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LaunchPathTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProductViewSummary:
    boto3_raw_data: "type_defs.ProductViewSummaryTypeDef" = dataclasses.field()

    Id = field("Id")
    ProductId = field("ProductId")
    Name = field("Name")
    Owner = field("Owner")
    ShortDescription = field("ShortDescription")
    Type = field("Type")
    Distributor = field("Distributor")
    HasDefaultPath = field("HasDefaultPath")
    SupportEmail = field("SupportEmail")
    SupportDescription = field("SupportDescription")
    SupportUrl = field("SupportUrl")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProductViewSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProductViewSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProvisioningArtifact:
    boto3_raw_data: "type_defs.ProvisioningArtifactTypeDef" = dataclasses.field()

    Id = field("Id")
    Name = field("Name")
    Description = field("Description")
    CreatedTime = field("CreatedTime")
    Guidance = field("Guidance")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProvisioningArtifactTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProvisioningArtifactTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeProductViewInput:
    boto3_raw_data: "type_defs.DescribeProductViewInputTypeDef" = dataclasses.field()

    Id = field("Id")
    AcceptLanguage = field("AcceptLanguage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeProductViewInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeProductViewInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeProvisionedProductInput:
    boto3_raw_data: "type_defs.DescribeProvisionedProductInputTypeDef" = (
        dataclasses.field()
    )

    AcceptLanguage = field("AcceptLanguage")
    Id = field("Id")
    Name = field("Name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeProvisionedProductInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeProvisionedProductInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProvisionedProductDetail:
    boto3_raw_data: "type_defs.ProvisionedProductDetailTypeDef" = dataclasses.field()

    Name = field("Name")
    Arn = field("Arn")
    Type = field("Type")
    Id = field("Id")
    Status = field("Status")
    StatusMessage = field("StatusMessage")
    CreatedTime = field("CreatedTime")
    IdempotencyToken = field("IdempotencyToken")
    LastRecordId = field("LastRecordId")
    LastProvisioningRecordId = field("LastProvisioningRecordId")
    LastSuccessfulProvisioningRecordId = field("LastSuccessfulProvisioningRecordId")
    ProductId = field("ProductId")
    ProvisioningArtifactId = field("ProvisioningArtifactId")
    LaunchRoleArn = field("LaunchRoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProvisionedProductDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProvisionedProductDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeProvisionedProductPlanInput:
    boto3_raw_data: "type_defs.DescribeProvisionedProductPlanInputTypeDef" = (
        dataclasses.field()
    )

    PlanId = field("PlanId")
    AcceptLanguage = field("AcceptLanguage")
    PageSize = field("PageSize")
    PageToken = field("PageToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeProvisionedProductPlanInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeProvisionedProductPlanInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeProvisioningArtifactInput:
    boto3_raw_data: "type_defs.DescribeProvisioningArtifactInputTypeDef" = (
        dataclasses.field()
    )

    AcceptLanguage = field("AcceptLanguage")
    ProvisioningArtifactId = field("ProvisioningArtifactId")
    ProductId = field("ProductId")
    ProvisioningArtifactName = field("ProvisioningArtifactName")
    ProductName = field("ProductName")
    Verbose = field("Verbose")
    IncludeProvisioningArtifactParameters = field(
        "IncludeProvisioningArtifactParameters"
    )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeProvisioningArtifactInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeProvisioningArtifactInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeProvisioningParametersInput:
    boto3_raw_data: "type_defs.DescribeProvisioningParametersInputTypeDef" = (
        dataclasses.field()
    )

    AcceptLanguage = field("AcceptLanguage")
    ProductId = field("ProductId")
    ProductName = field("ProductName")
    ProvisioningArtifactId = field("ProvisioningArtifactId")
    ProvisioningArtifactName = field("ProvisioningArtifactName")
    PathId = field("PathId")
    PathName = field("PathName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeProvisioningParametersInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeProvisioningParametersInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProvisioningArtifactOutput:
    boto3_raw_data: "type_defs.ProvisioningArtifactOutputTypeDef" = dataclasses.field()

    Key = field("Key")
    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProvisioningArtifactOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProvisioningArtifactOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProvisioningArtifactPreferences:
    boto3_raw_data: "type_defs.ProvisioningArtifactPreferencesTypeDef" = (
        dataclasses.field()
    )

    StackSetAccounts = field("StackSetAccounts")
    StackSetRegions = field("StackSetRegions")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ProvisioningArtifactPreferencesTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProvisioningArtifactPreferencesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagOptionSummary:
    boto3_raw_data: "type_defs.TagOptionSummaryTypeDef" = dataclasses.field()

    Key = field("Key")
    Values = field("Values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagOptionSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagOptionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UsageInstruction:
    boto3_raw_data: "type_defs.UsageInstructionTypeDef" = dataclasses.field()

    Type = field("Type")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UsageInstructionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UsageInstructionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRecordInput:
    boto3_raw_data: "type_defs.DescribeRecordInputTypeDef" = dataclasses.field()

    Id = field("Id")
    AcceptLanguage = field("AcceptLanguage")
    PageToken = field("PageToken")
    PageSize = field("PageSize")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeRecordInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRecordInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecordOutput:
    boto3_raw_data: "type_defs.RecordOutputTypeDef" = dataclasses.field()

    OutputKey = field("OutputKey")
    OutputValue = field("OutputValue")
    Description = field("Description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecordOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RecordOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeServiceActionExecutionParametersInput:
    boto3_raw_data: "type_defs.DescribeServiceActionExecutionParametersInputTypeDef" = (
        dataclasses.field()
    )

    ProvisionedProductId = field("ProvisionedProductId")
    ServiceActionId = field("ServiceActionId")
    AcceptLanguage = field("AcceptLanguage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeServiceActionExecutionParametersInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeServiceActionExecutionParametersInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecutionParameter:
    boto3_raw_data: "type_defs.ExecutionParameterTypeDef" = dataclasses.field()

    Name = field("Name")
    Type = field("Type")
    DefaultValues = field("DefaultValues")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExecutionParameterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecutionParameterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeServiceActionInput:
    boto3_raw_data: "type_defs.DescribeServiceActionInputTypeDef" = dataclasses.field()

    Id = field("Id")
    AcceptLanguage = field("AcceptLanguage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeServiceActionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeServiceActionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTagOptionInput:
    boto3_raw_data: "type_defs.DescribeTagOptionInputTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTagOptionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTagOptionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateBudgetFromResourceInput:
    boto3_raw_data: "type_defs.DisassociateBudgetFromResourceInputTypeDef" = (
        dataclasses.field()
    )

    BudgetName = field("BudgetName")
    ResourceId = field("ResourceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateBudgetFromResourceInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateBudgetFromResourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociatePrincipalFromPortfolioInput:
    boto3_raw_data: "type_defs.DisassociatePrincipalFromPortfolioInputTypeDef" = (
        dataclasses.field()
    )

    PortfolioId = field("PortfolioId")
    PrincipalARN = field("PrincipalARN")
    AcceptLanguage = field("AcceptLanguage")
    PrincipalType = field("PrincipalType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociatePrincipalFromPortfolioInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociatePrincipalFromPortfolioInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateProductFromPortfolioInput:
    boto3_raw_data: "type_defs.DisassociateProductFromPortfolioInputTypeDef" = (
        dataclasses.field()
    )

    ProductId = field("ProductId")
    PortfolioId = field("PortfolioId")
    AcceptLanguage = field("AcceptLanguage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateProductFromPortfolioInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateProductFromPortfolioInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateServiceActionFromProvisioningArtifactInput:
    boto3_raw_data: (
        "type_defs.DisassociateServiceActionFromProvisioningArtifactInputTypeDef"
    ) = dataclasses.field()

    ProductId = field("ProductId")
    ProvisioningArtifactId = field("ProvisioningArtifactId")
    ServiceActionId = field("ServiceActionId")
    AcceptLanguage = field("AcceptLanguage")
    IdempotencyToken = field("IdempotencyToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateServiceActionFromProvisioningArtifactInputTypeDef"
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
                "type_defs.DisassociateServiceActionFromProvisioningArtifactInputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateTagOptionFromResourceInput:
    boto3_raw_data: "type_defs.DisassociateTagOptionFromResourceInputTypeDef" = (
        dataclasses.field()
    )

    ResourceId = field("ResourceId")
    TagOptionId = field("TagOptionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateTagOptionFromResourceInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateTagOptionFromResourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UniqueTagResourceIdentifier:
    boto3_raw_data: "type_defs.UniqueTagResourceIdentifierTypeDef" = dataclasses.field()

    Key = field("Key")
    Value = field("Value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UniqueTagResourceIdentifierTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UniqueTagResourceIdentifierTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecuteProvisionedProductPlanInput:
    boto3_raw_data: "type_defs.ExecuteProvisionedProductPlanInputTypeDef" = (
        dataclasses.field()
    )

    PlanId = field("PlanId")
    IdempotencyToken = field("IdempotencyToken")
    AcceptLanguage = field("AcceptLanguage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExecuteProvisionedProductPlanInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecuteProvisionedProductPlanInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecuteProvisionedProductServiceActionInput:
    boto3_raw_data: "type_defs.ExecuteProvisionedProductServiceActionInputTypeDef" = (
        dataclasses.field()
    )

    ProvisionedProductId = field("ProvisionedProductId")
    ServiceActionId = field("ServiceActionId")
    ExecuteToken = field("ExecuteToken")
    AcceptLanguage = field("AcceptLanguage")
    Parameters = field("Parameters")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExecuteProvisionedProductServiceActionInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecuteProvisionedProductServiceActionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetProvisionedProductOutputsInput:
    boto3_raw_data: "type_defs.GetProvisionedProductOutputsInputTypeDef" = (
        dataclasses.field()
    )

    AcceptLanguage = field("AcceptLanguage")
    ProvisionedProductId = field("ProvisionedProductId")
    ProvisionedProductName = field("ProvisionedProductName")
    OutputKeys = field("OutputKeys")
    PageSize = field("PageSize")
    PageToken = field("PageToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetProvisionedProductOutputsInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetProvisionedProductOutputsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportAsProvisionedProductInput:
    boto3_raw_data: "type_defs.ImportAsProvisionedProductInputTypeDef" = (
        dataclasses.field()
    )

    ProductId = field("ProductId")
    ProvisioningArtifactId = field("ProvisioningArtifactId")
    ProvisionedProductName = field("ProvisionedProductName")
    PhysicalId = field("PhysicalId")
    IdempotencyToken = field("IdempotencyToken")
    AcceptLanguage = field("AcceptLanguage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ImportAsProvisionedProductInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportAsProvisionedProductInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LastSync:
    boto3_raw_data: "type_defs.LastSyncTypeDef" = dataclasses.field()

    LastSyncTime = field("LastSyncTime")
    LastSyncStatus = field("LastSyncStatus")
    LastSyncStatusMessage = field("LastSyncStatusMessage")
    LastSuccessfulSyncTime = field("LastSuccessfulSyncTime")
    LastSuccessfulSyncProvisioningArtifactId = field(
        "LastSuccessfulSyncProvisioningArtifactId"
    )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LastSyncTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LastSyncTypeDef"]]
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
class ListAcceptedPortfolioSharesInput:
    boto3_raw_data: "type_defs.ListAcceptedPortfolioSharesInputTypeDef" = (
        dataclasses.field()
    )

    AcceptLanguage = field("AcceptLanguage")
    PageToken = field("PageToken")
    PageSize = field("PageSize")
    PortfolioShareType = field("PortfolioShareType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAcceptedPortfolioSharesInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAcceptedPortfolioSharesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBudgetsForResourceInput:
    boto3_raw_data: "type_defs.ListBudgetsForResourceInputTypeDef" = dataclasses.field()

    ResourceId = field("ResourceId")
    AcceptLanguage = field("AcceptLanguage")
    PageSize = field("PageSize")
    PageToken = field("PageToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBudgetsForResourceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBudgetsForResourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConstraintsForPortfolioInput:
    boto3_raw_data: "type_defs.ListConstraintsForPortfolioInputTypeDef" = (
        dataclasses.field()
    )

    PortfolioId = field("PortfolioId")
    AcceptLanguage = field("AcceptLanguage")
    ProductId = field("ProductId")
    PageSize = field("PageSize")
    PageToken = field("PageToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListConstraintsForPortfolioInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConstraintsForPortfolioInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLaunchPathsInput:
    boto3_raw_data: "type_defs.ListLaunchPathsInputTypeDef" = dataclasses.field()

    ProductId = field("ProductId")
    AcceptLanguage = field("AcceptLanguage")
    PageSize = field("PageSize")
    PageToken = field("PageToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLaunchPathsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLaunchPathsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOrganizationPortfolioAccessInput:
    boto3_raw_data: "type_defs.ListOrganizationPortfolioAccessInputTypeDef" = (
        dataclasses.field()
    )

    PortfolioId = field("PortfolioId")
    OrganizationNodeType = field("OrganizationNodeType")
    AcceptLanguage = field("AcceptLanguage")
    PageToken = field("PageToken")
    PageSize = field("PageSize")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListOrganizationPortfolioAccessInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOrganizationPortfolioAccessInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPortfolioAccessInput:
    boto3_raw_data: "type_defs.ListPortfolioAccessInputTypeDef" = dataclasses.field()

    PortfolioId = field("PortfolioId")
    AcceptLanguage = field("AcceptLanguage")
    OrganizationParentId = field("OrganizationParentId")
    PageToken = field("PageToken")
    PageSize = field("PageSize")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPortfolioAccessInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPortfolioAccessInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPortfoliosForProductInput:
    boto3_raw_data: "type_defs.ListPortfoliosForProductInputTypeDef" = (
        dataclasses.field()
    )

    ProductId = field("ProductId")
    AcceptLanguage = field("AcceptLanguage")
    PageToken = field("PageToken")
    PageSize = field("PageSize")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListPortfoliosForProductInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPortfoliosForProductInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPortfoliosInput:
    boto3_raw_data: "type_defs.ListPortfoliosInputTypeDef" = dataclasses.field()

    AcceptLanguage = field("AcceptLanguage")
    PageToken = field("PageToken")
    PageSize = field("PageSize")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPortfoliosInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPortfoliosInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPrincipalsForPortfolioInput:
    boto3_raw_data: "type_defs.ListPrincipalsForPortfolioInputTypeDef" = (
        dataclasses.field()
    )

    PortfolioId = field("PortfolioId")
    AcceptLanguage = field("AcceptLanguage")
    PageSize = field("PageSize")
    PageToken = field("PageToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListPrincipalsForPortfolioInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPrincipalsForPortfolioInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Principal:
    boto3_raw_data: "type_defs.PrincipalTypeDef" = dataclasses.field()

    PrincipalARN = field("PrincipalARN")
    PrincipalType = field("PrincipalType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PrincipalTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PrincipalTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProvisionedProductPlanSummary:
    boto3_raw_data: "type_defs.ProvisionedProductPlanSummaryTypeDef" = (
        dataclasses.field()
    )

    PlanName = field("PlanName")
    PlanId = field("PlanId")
    ProvisionProductId = field("ProvisionProductId")
    ProvisionProductName = field("ProvisionProductName")
    PlanType = field("PlanType")
    ProvisioningArtifactId = field("ProvisioningArtifactId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ProvisionedProductPlanSummaryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProvisionedProductPlanSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProvisioningArtifactsForServiceActionInput:
    boto3_raw_data: (
        "type_defs.ListProvisioningArtifactsForServiceActionInputTypeDef"
    ) = dataclasses.field()

    ServiceActionId = field("ServiceActionId")
    PageSize = field("PageSize")
    PageToken = field("PageToken")
    AcceptLanguage = field("AcceptLanguage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListProvisioningArtifactsForServiceActionInputTypeDef"
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
                "type_defs.ListProvisioningArtifactsForServiceActionInputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProvisioningArtifactsInput:
    boto3_raw_data: "type_defs.ListProvisioningArtifactsInputTypeDef" = (
        dataclasses.field()
    )

    ProductId = field("ProductId")
    AcceptLanguage = field("AcceptLanguage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListProvisioningArtifactsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProvisioningArtifactsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRecordHistorySearchFilter:
    boto3_raw_data: "type_defs.ListRecordHistorySearchFilterTypeDef" = (
        dataclasses.field()
    )

    Key = field("Key")
    Value = field("Value")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListRecordHistorySearchFilterTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecordHistorySearchFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourcesForTagOptionInput:
    boto3_raw_data: "type_defs.ListResourcesForTagOptionInputTypeDef" = (
        dataclasses.field()
    )

    TagOptionId = field("TagOptionId")
    ResourceType = field("ResourceType")
    PageSize = field("PageSize")
    PageToken = field("PageToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListResourcesForTagOptionInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourcesForTagOptionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceDetail:
    boto3_raw_data: "type_defs.ResourceDetailTypeDef" = dataclasses.field()

    Id = field("Id")
    ARN = field("ARN")
    Name = field("Name")
    Description = field("Description")
    CreatedTime = field("CreatedTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceDetailTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceActionsForProvisioningArtifactInput:
    boto3_raw_data: (
        "type_defs.ListServiceActionsForProvisioningArtifactInputTypeDef"
    ) = dataclasses.field()

    ProductId = field("ProductId")
    ProvisioningArtifactId = field("ProvisioningArtifactId")
    PageSize = field("PageSize")
    PageToken = field("PageToken")
    AcceptLanguage = field("AcceptLanguage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListServiceActionsForProvisioningArtifactInputTypeDef"
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
                "type_defs.ListServiceActionsForProvisioningArtifactInputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceActionSummary:
    boto3_raw_data: "type_defs.ServiceActionSummaryTypeDef" = dataclasses.field()

    Id = field("Id")
    Name = field("Name")
    Description = field("Description")
    DefinitionType = field("DefinitionType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServiceActionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceActionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceActionsInput:
    boto3_raw_data: "type_defs.ListServiceActionsInputTypeDef" = dataclasses.field()

    AcceptLanguage = field("AcceptLanguage")
    PageSize = field("PageSize")
    PageToken = field("PageToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListServiceActionsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServiceActionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStackInstancesForProvisionedProductInput:
    boto3_raw_data: "type_defs.ListStackInstancesForProvisionedProductInputTypeDef" = (
        dataclasses.field()
    )

    ProvisionedProductId = field("ProvisionedProductId")
    AcceptLanguage = field("AcceptLanguage")
    PageToken = field("PageToken")
    PageSize = field("PageSize")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListStackInstancesForProvisionedProductInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStackInstancesForProvisionedProductInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StackInstance:
    boto3_raw_data: "type_defs.StackInstanceTypeDef" = dataclasses.field()

    Account = field("Account")
    Region = field("Region")
    StackInstanceStatus = field("StackInstanceStatus")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StackInstanceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StackInstanceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagOptionsFilters:
    boto3_raw_data: "type_defs.ListTagOptionsFiltersTypeDef" = dataclasses.field()

    Key = field("Key")
    Value = field("Value")
    Active = field("Active")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagOptionsFiltersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagOptionsFiltersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotifyTerminateProvisionedProductEngineWorkflowResultInput:
    boto3_raw_data: (
        "type_defs.NotifyTerminateProvisionedProductEngineWorkflowResultInputTypeDef"
    ) = dataclasses.field()

    WorkflowToken = field("WorkflowToken")
    RecordId = field("RecordId")
    Status = field("Status")
    IdempotencyToken = field("IdempotencyToken")
    FailureReason = field("FailureReason")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.NotifyTerminateProvisionedProductEngineWorkflowResultInputTypeDef"
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
                "type_defs.NotifyTerminateProvisionedProductEngineWorkflowResultInputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParameterConstraints:
    boto3_raw_data: "type_defs.ParameterConstraintsTypeDef" = dataclasses.field()

    AllowedValues = field("AllowedValues")
    AllowedPattern = field("AllowedPattern")
    ConstraintDescription = field("ConstraintDescription")
    MaxLength = field("MaxLength")
    MinLength = field("MinLength")
    MaxValue = field("MaxValue")
    MinValue = field("MinValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ParameterConstraintsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParameterConstraintsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProductViewAggregationValue:
    boto3_raw_data: "type_defs.ProductViewAggregationValueTypeDef" = dataclasses.field()

    Value = field("Value")
    ApproximateCount = field("ApproximateCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProductViewAggregationValueTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProductViewAggregationValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProvisioningParameter:
    boto3_raw_data: "type_defs.ProvisioningParameterTypeDef" = dataclasses.field()

    Key = field("Key")
    Value = field("Value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProvisioningParameterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProvisioningParameterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProvisioningPreferences:
    boto3_raw_data: "type_defs.ProvisioningPreferencesTypeDef" = dataclasses.field()

    StackSetAccounts = field("StackSetAccounts")
    StackSetRegions = field("StackSetRegions")
    StackSetFailureToleranceCount = field("StackSetFailureToleranceCount")
    StackSetFailureTolerancePercentage = field("StackSetFailureTolerancePercentage")
    StackSetMaxConcurrencyCount = field("StackSetMaxConcurrencyCount")
    StackSetMaxConcurrencyPercentage = field("StackSetMaxConcurrencyPercentage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProvisioningPreferencesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProvisioningPreferencesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecordError:
    boto3_raw_data: "type_defs.RecordErrorTypeDef" = dataclasses.field()

    Code = field("Code")
    Description = field("Description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecordErrorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RecordErrorTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecordTag:
    boto3_raw_data: "type_defs.RecordTagTypeDef" = dataclasses.field()

    Key = field("Key")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecordTagTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RecordTagTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RejectPortfolioShareInput:
    boto3_raw_data: "type_defs.RejectPortfolioShareInputTypeDef" = dataclasses.field()

    PortfolioId = field("PortfolioId")
    AcceptLanguage = field("AcceptLanguage")
    PortfolioShareType = field("PortfolioShareType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RejectPortfolioShareInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RejectPortfolioShareInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceTargetDefinition:
    boto3_raw_data: "type_defs.ResourceTargetDefinitionTypeDef" = dataclasses.field()

    Attribute = field("Attribute")
    Name = field("Name")
    RequiresRecreation = field("RequiresRecreation")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceTargetDefinitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceTargetDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchProductsAsAdminInput:
    boto3_raw_data: "type_defs.SearchProductsAsAdminInputTypeDef" = dataclasses.field()

    AcceptLanguage = field("AcceptLanguage")
    PortfolioId = field("PortfolioId")
    Filters = field("Filters")
    SortBy = field("SortBy")
    SortOrder = field("SortOrder")
    PageToken = field("PageToken")
    PageSize = field("PageSize")
    ProductSource = field("ProductSource")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchProductsAsAdminInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchProductsAsAdminInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchProductsInput:
    boto3_raw_data: "type_defs.SearchProductsInputTypeDef" = dataclasses.field()

    AcceptLanguage = field("AcceptLanguage")
    Filters = field("Filters")
    PageSize = field("PageSize")
    SortBy = field("SortBy")
    SortOrder = field("SortOrder")
    PageToken = field("PageToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchProductsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchProductsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ShareError:
    boto3_raw_data: "type_defs.ShareErrorTypeDef" = dataclasses.field()

    Accounts = field("Accounts")
    Message = field("Message")
    Error = field("Error")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ShareErrorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ShareErrorTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TerminateProvisionedProductInput:
    boto3_raw_data: "type_defs.TerminateProvisionedProductInputTypeDef" = (
        dataclasses.field()
    )

    TerminateToken = field("TerminateToken")
    ProvisionedProductName = field("ProvisionedProductName")
    ProvisionedProductId = field("ProvisionedProductId")
    IgnoreErrors = field("IgnoreErrors")
    AcceptLanguage = field("AcceptLanguage")
    RetainPhysicalResources = field("RetainPhysicalResources")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TerminateProvisionedProductInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TerminateProvisionedProductInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateConstraintInput:
    boto3_raw_data: "type_defs.UpdateConstraintInputTypeDef" = dataclasses.field()

    Id = field("Id")
    AcceptLanguage = field("AcceptLanguage")
    Description = field("Description")
    Parameters = field("Parameters")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateConstraintInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateConstraintInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateProvisioningPreferences:
    boto3_raw_data: "type_defs.UpdateProvisioningPreferencesTypeDef" = (
        dataclasses.field()
    )

    StackSetAccounts = field("StackSetAccounts")
    StackSetRegions = field("StackSetRegions")
    StackSetFailureToleranceCount = field("StackSetFailureToleranceCount")
    StackSetFailureTolerancePercentage = field("StackSetFailureTolerancePercentage")
    StackSetMaxConcurrencyCount = field("StackSetMaxConcurrencyCount")
    StackSetMaxConcurrencyPercentage = field("StackSetMaxConcurrencyPercentage")
    StackSetOperationType = field("StackSetOperationType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateProvisioningPreferencesTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateProvisioningPreferencesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateProvisionedProductPropertiesInput:
    boto3_raw_data: "type_defs.UpdateProvisionedProductPropertiesInputTypeDef" = (
        dataclasses.field()
    )

    ProvisionedProductId = field("ProvisionedProductId")
    ProvisionedProductProperties = field("ProvisionedProductProperties")
    IdempotencyToken = field("IdempotencyToken")
    AcceptLanguage = field("AcceptLanguage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateProvisionedProductPropertiesInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateProvisionedProductPropertiesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateProvisioningArtifactInput:
    boto3_raw_data: "type_defs.UpdateProvisioningArtifactInputTypeDef" = (
        dataclasses.field()
    )

    ProductId = field("ProductId")
    ProvisioningArtifactId = field("ProvisioningArtifactId")
    AcceptLanguage = field("AcceptLanguage")
    Name = field("Name")
    Description = field("Description")
    Active = field("Active")
    Guidance = field("Guidance")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateProvisioningArtifactInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateProvisioningArtifactInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateServiceActionInput:
    boto3_raw_data: "type_defs.UpdateServiceActionInputTypeDef" = dataclasses.field()

    Id = field("Id")
    Name = field("Name")
    Definition = field("Definition")
    Description = field("Description")
    AcceptLanguage = field("AcceptLanguage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateServiceActionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateServiceActionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTagOptionInput:
    boto3_raw_data: "type_defs.UpdateTagOptionInputTypeDef" = dataclasses.field()

    Id = field("Id")
    Value = field("Value")
    Active = field("Active")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateTagOptionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTagOptionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProvisionedProductPlansInput:
    boto3_raw_data: "type_defs.ListProvisionedProductPlansInputTypeDef" = (
        dataclasses.field()
    )

    AcceptLanguage = field("AcceptLanguage")
    ProvisionProductId = field("ProvisionProductId")
    PageSize = field("PageSize")
    PageToken = field("PageToken")

    @cached_property
    def AccessLevelFilter(self):  # pragma: no cover
        return AccessLevelFilter.make_one(self.boto3_raw_data["AccessLevelFilter"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListProvisionedProductPlansInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProvisionedProductPlansInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScanProvisionedProductsInput:
    boto3_raw_data: "type_defs.ScanProvisionedProductsInputTypeDef" = (
        dataclasses.field()
    )

    AcceptLanguage = field("AcceptLanguage")

    @cached_property
    def AccessLevelFilter(self):  # pragma: no cover
        return AccessLevelFilter.make_one(self.boto3_raw_data["AccessLevelFilter"])

    PageSize = field("PageSize")
    PageToken = field("PageToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScanProvisionedProductsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScanProvisionedProductsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchProvisionedProductsInput:
    boto3_raw_data: "type_defs.SearchProvisionedProductsInputTypeDef" = (
        dataclasses.field()
    )

    AcceptLanguage = field("AcceptLanguage")

    @cached_property
    def AccessLevelFilter(self):  # pragma: no cover
        return AccessLevelFilter.make_one(self.boto3_raw_data["AccessLevelFilter"])

    Filters = field("Filters")
    SortBy = field("SortBy")
    SortOrder = field("SortOrder")
    PageSize = field("PageSize")
    PageToken = field("PageToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SearchProvisionedProductsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchProvisionedProductsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchAssociateServiceActionWithProvisioningArtifactInput:
    boto3_raw_data: (
        "type_defs.BatchAssociateServiceActionWithProvisioningArtifactInputTypeDef"
    ) = dataclasses.field()

    @cached_property
    def ServiceActionAssociations(self):  # pragma: no cover
        return ServiceActionAssociation.make_many(
            self.boto3_raw_data["ServiceActionAssociations"]
        )

    AcceptLanguage = field("AcceptLanguage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchAssociateServiceActionWithProvisioningArtifactInputTypeDef"
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
                "type_defs.BatchAssociateServiceActionWithProvisioningArtifactInputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDisassociateServiceActionFromProvisioningArtifactInput:
    boto3_raw_data: (
        "type_defs.BatchDisassociateServiceActionFromProvisioningArtifactInputTypeDef"
    ) = dataclasses.field()

    @cached_property
    def ServiceActionAssociations(self):  # pragma: no cover
        return ServiceActionAssociation.make_many(
            self.boto3_raw_data["ServiceActionAssociations"]
        )

    AcceptLanguage = field("AcceptLanguage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDisassociateServiceActionFromProvisioningArtifactInputTypeDef"
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
                "type_defs.BatchDisassociateServiceActionFromProvisioningArtifactInputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchAssociateServiceActionWithProvisioningArtifactOutput:
    boto3_raw_data: (
        "type_defs.BatchAssociateServiceActionWithProvisioningArtifactOutputTypeDef"
    ) = dataclasses.field()

    @cached_property
    def FailedServiceActionAssociations(self):  # pragma: no cover
        return FailedServiceActionAssociation.make_many(
            self.boto3_raw_data["FailedServiceActionAssociations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchAssociateServiceActionWithProvisioningArtifactOutputTypeDef"
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
                "type_defs.BatchAssociateServiceActionWithProvisioningArtifactOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDisassociateServiceActionFromProvisioningArtifactOutput:
    boto3_raw_data: (
        "type_defs.BatchDisassociateServiceActionFromProvisioningArtifactOutputTypeDef"
    ) = dataclasses.field()

    @cached_property
    def FailedServiceActionAssociations(self):  # pragma: no cover
        return FailedServiceActionAssociation.make_many(
            self.boto3_raw_data["FailedServiceActionAssociations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDisassociateServiceActionFromProvisioningArtifactOutputTypeDef"
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
                "type_defs.BatchDisassociateServiceActionFromProvisioningArtifactOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopyProductOutput:
    boto3_raw_data: "type_defs.CopyProductOutputTypeDef" = dataclasses.field()

    CopyProductToken = field("CopyProductToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CopyProductOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CopyProductOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePortfolioShareOutput:
    boto3_raw_data: "type_defs.CreatePortfolioShareOutputTypeDef" = dataclasses.field()

    PortfolioShareToken = field("PortfolioShareToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePortfolioShareOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePortfolioShareOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateProvisionedProductPlanOutput:
    boto3_raw_data: "type_defs.CreateProvisionedProductPlanOutputTypeDef" = (
        dataclasses.field()
    )

    PlanName = field("PlanName")
    PlanId = field("PlanId")
    ProvisionProductId = field("ProvisionProductId")
    ProvisionedProductName = field("ProvisionedProductName")
    ProvisioningArtifactId = field("ProvisioningArtifactId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateProvisionedProductPlanOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateProvisionedProductPlanOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePortfolioShareOutput:
    boto3_raw_data: "type_defs.DeletePortfolioShareOutputTypeDef" = dataclasses.field()

    PortfolioShareToken = field("PortfolioShareToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePortfolioShareOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePortfolioShareOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCopyProductStatusOutput:
    boto3_raw_data: "type_defs.DescribeCopyProductStatusOutputTypeDef" = (
        dataclasses.field()
    )

    CopyProductStatus = field("CopyProductStatus")
    TargetProductId = field("TargetProductId")
    StatusDetail = field("StatusDetail")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeCopyProductStatusOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCopyProductStatusOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAWSOrganizationsAccessStatusOutput:
    boto3_raw_data: "type_defs.GetAWSOrganizationsAccessStatusOutputTypeDef" = (
        dataclasses.field()
    )

    AccessStatus = field("AccessStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAWSOrganizationsAccessStatusOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAWSOrganizationsAccessStatusOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPortfolioAccessOutput:
    boto3_raw_data: "type_defs.ListPortfolioAccessOutputTypeDef" = dataclasses.field()

    AccountIds = field("AccountIds")
    NextPageToken = field("NextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPortfolioAccessOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPortfolioAccessOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePortfolioShareOutput:
    boto3_raw_data: "type_defs.UpdatePortfolioShareOutputTypeDef" = dataclasses.field()

    PortfolioShareToken = field("PortfolioShareToken")
    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePortfolioShareOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePortfolioShareOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateProvisionedProductPropertiesOutput:
    boto3_raw_data: "type_defs.UpdateProvisionedProductPropertiesOutputTypeDef" = (
        dataclasses.field()
    )

    ProvisionedProductId = field("ProvisionedProductId")
    ProvisionedProductProperties = field("ProvisionedProductProperties")
    RecordId = field("RecordId")
    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateProvisionedProductPropertiesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateProvisionedProductPropertiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBudgetsForResourceOutput:
    boto3_raw_data: "type_defs.ListBudgetsForResourceOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Budgets(self):  # pragma: no cover
        return BudgetDetail.make_many(self.boto3_raw_data["Budgets"])

    NextPageToken = field("NextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBudgetsForResourceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBudgetsForResourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceConnectionParameters:
    boto3_raw_data: "type_defs.SourceConnectionParametersTypeDef" = dataclasses.field()

    @cached_property
    def CodeStar(self):  # pragma: no cover
        return CodeStarParameters.make_one(self.boto3_raw_data["CodeStar"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SourceConnectionParametersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourceConnectionParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConstraintOutput:
    boto3_raw_data: "type_defs.CreateConstraintOutputTypeDef" = dataclasses.field()

    @cached_property
    def ConstraintDetail(self):  # pragma: no cover
        return ConstraintDetail.make_one(self.boto3_raw_data["ConstraintDetail"])

    ConstraintParameters = field("ConstraintParameters")
    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateConstraintOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConstraintOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConstraintOutput:
    boto3_raw_data: "type_defs.DescribeConstraintOutputTypeDef" = dataclasses.field()

    @cached_property
    def ConstraintDetail(self):  # pragma: no cover
        return ConstraintDetail.make_one(self.boto3_raw_data["ConstraintDetail"])

    ConstraintParameters = field("ConstraintParameters")
    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeConstraintOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConstraintOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConstraintsForPortfolioOutput:
    boto3_raw_data: "type_defs.ListConstraintsForPortfolioOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ConstraintDetails(self):  # pragma: no cover
        return ConstraintDetail.make_many(self.boto3_raw_data["ConstraintDetails"])

    NextPageToken = field("NextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListConstraintsForPortfolioOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConstraintsForPortfolioOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateConstraintOutput:
    boto3_raw_data: "type_defs.UpdateConstraintOutputTypeDef" = dataclasses.field()

    @cached_property
    def ConstraintDetail(self):  # pragma: no cover
        return ConstraintDetail.make_one(self.boto3_raw_data["ConstraintDetail"])

    ConstraintParameters = field("ConstraintParameters")
    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateConstraintOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateConstraintOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePortfolioInput:
    boto3_raw_data: "type_defs.CreatePortfolioInputTypeDef" = dataclasses.field()

    DisplayName = field("DisplayName")
    ProviderName = field("ProviderName")
    IdempotencyToken = field("IdempotencyToken")
    AcceptLanguage = field("AcceptLanguage")
    Description = field("Description")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePortfolioInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePortfolioInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LaunchPathSummary:
    boto3_raw_data: "type_defs.LaunchPathSummaryTypeDef" = dataclasses.field()

    Id = field("Id")

    @cached_property
    def ConstraintSummaries(self):  # pragma: no cover
        return ConstraintSummary.make_many(self.boto3_raw_data["ConstraintSummaries"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LaunchPathSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LaunchPathSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProvisionedProductAttribute:
    boto3_raw_data: "type_defs.ProvisionedProductAttributeTypeDef" = dataclasses.field()

    Name = field("Name")
    Arn = field("Arn")
    Type = field("Type")
    Id = field("Id")
    Status = field("Status")
    StatusMessage = field("StatusMessage")
    CreatedTime = field("CreatedTime")
    IdempotencyToken = field("IdempotencyToken")
    LastRecordId = field("LastRecordId")
    LastProvisioningRecordId = field("LastProvisioningRecordId")
    LastSuccessfulProvisioningRecordId = field("LastSuccessfulProvisioningRecordId")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    PhysicalId = field("PhysicalId")
    ProductId = field("ProductId")
    ProductName = field("ProductName")
    ProvisioningArtifactId = field("ProvisioningArtifactId")
    ProvisioningArtifactName = field("ProvisioningArtifactName")
    UserArn = field("UserArn")
    UserArnSession = field("UserArnSession")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProvisionedProductAttributeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProvisionedProductAttributeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePortfolioInput:
    boto3_raw_data: "type_defs.UpdatePortfolioInputTypeDef" = dataclasses.field()

    Id = field("Id")
    AcceptLanguage = field("AcceptLanguage")
    DisplayName = field("DisplayName")
    Description = field("Description")
    ProviderName = field("ProviderName")

    @cached_property
    def AddTags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["AddTags"])

    RemoveTags = field("RemoveTags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePortfolioInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePortfolioInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePortfolioOutput:
    boto3_raw_data: "type_defs.CreatePortfolioOutputTypeDef" = dataclasses.field()

    @cached_property
    def PortfolioDetail(self):  # pragma: no cover
        return PortfolioDetail.make_one(self.boto3_raw_data["PortfolioDetail"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePortfolioOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePortfolioOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAcceptedPortfolioSharesOutput:
    boto3_raw_data: "type_defs.ListAcceptedPortfolioSharesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PortfolioDetails(self):  # pragma: no cover
        return PortfolioDetail.make_many(self.boto3_raw_data["PortfolioDetails"])

    NextPageToken = field("NextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAcceptedPortfolioSharesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAcceptedPortfolioSharesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPortfoliosForProductOutput:
    boto3_raw_data: "type_defs.ListPortfoliosForProductOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PortfolioDetails(self):  # pragma: no cover
        return PortfolioDetail.make_many(self.boto3_raw_data["PortfolioDetails"])

    NextPageToken = field("NextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListPortfoliosForProductOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPortfoliosForProductOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPortfoliosOutput:
    boto3_raw_data: "type_defs.ListPortfoliosOutputTypeDef" = dataclasses.field()

    @cached_property
    def PortfolioDetails(self):  # pragma: no cover
        return PortfolioDetail.make_many(self.boto3_raw_data["PortfolioDetails"])

    NextPageToken = field("NextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPortfoliosOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPortfoliosOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePortfolioOutput:
    boto3_raw_data: "type_defs.UpdatePortfolioOutputTypeDef" = dataclasses.field()

    @cached_property
    def PortfolioDetail(self):  # pragma: no cover
        return PortfolioDetail.make_one(self.boto3_raw_data["PortfolioDetail"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePortfolioOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePortfolioOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePortfolioShareInput:
    boto3_raw_data: "type_defs.CreatePortfolioShareInputTypeDef" = dataclasses.field()

    PortfolioId = field("PortfolioId")
    AcceptLanguage = field("AcceptLanguage")
    AccountId = field("AccountId")

    @cached_property
    def OrganizationNode(self):  # pragma: no cover
        return OrganizationNode.make_one(self.boto3_raw_data["OrganizationNode"])

    ShareTagOptions = field("ShareTagOptions")
    SharePrincipals = field("SharePrincipals")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePortfolioShareInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePortfolioShareInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePortfolioShareInput:
    boto3_raw_data: "type_defs.DeletePortfolioShareInputTypeDef" = dataclasses.field()

    PortfolioId = field("PortfolioId")
    AcceptLanguage = field("AcceptLanguage")
    AccountId = field("AccountId")

    @cached_property
    def OrganizationNode(self):  # pragma: no cover
        return OrganizationNode.make_one(self.boto3_raw_data["OrganizationNode"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePortfolioShareInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePortfolioShareInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOrganizationPortfolioAccessOutput:
    boto3_raw_data: "type_defs.ListOrganizationPortfolioAccessOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def OrganizationNodes(self):  # pragma: no cover
        return OrganizationNode.make_many(self.boto3_raw_data["OrganizationNodes"])

    NextPageToken = field("NextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListOrganizationPortfolioAccessOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOrganizationPortfolioAccessOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePortfolioShareInput:
    boto3_raw_data: "type_defs.UpdatePortfolioShareInputTypeDef" = dataclasses.field()

    PortfolioId = field("PortfolioId")
    AcceptLanguage = field("AcceptLanguage")
    AccountId = field("AccountId")

    @cached_property
    def OrganizationNode(self):  # pragma: no cover
        return OrganizationNode.make_one(self.boto3_raw_data["OrganizationNode"])

    ShareTagOptions = field("ShareTagOptions")
    SharePrincipals = field("SharePrincipals")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePortfolioShareInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePortfolioShareInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateProvisioningArtifactInput:
    boto3_raw_data: "type_defs.CreateProvisioningArtifactInputTypeDef" = (
        dataclasses.field()
    )

    ProductId = field("ProductId")

    @cached_property
    def Parameters(self):  # pragma: no cover
        return ProvisioningArtifactProperties.make_one(
            self.boto3_raw_data["Parameters"]
        )

    IdempotencyToken = field("IdempotencyToken")
    AcceptLanguage = field("AcceptLanguage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateProvisioningArtifactInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateProvisioningArtifactInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateProvisioningArtifactOutput:
    boto3_raw_data: "type_defs.CreateProvisioningArtifactOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ProvisioningArtifactDetail(self):  # pragma: no cover
        return ProvisioningArtifactDetail.make_one(
            self.boto3_raw_data["ProvisioningArtifactDetail"]
        )

    Info = field("Info")
    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateProvisioningArtifactOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateProvisioningArtifactOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProvisioningArtifactsOutput:
    boto3_raw_data: "type_defs.ListProvisioningArtifactsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ProvisioningArtifactDetails(self):  # pragma: no cover
        return ProvisioningArtifactDetail.make_many(
            self.boto3_raw_data["ProvisioningArtifactDetails"]
        )

    NextPageToken = field("NextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListProvisioningArtifactsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProvisioningArtifactsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateProvisioningArtifactOutput:
    boto3_raw_data: "type_defs.UpdateProvisioningArtifactOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ProvisioningArtifactDetail(self):  # pragma: no cover
        return ProvisioningArtifactDetail.make_one(
            self.boto3_raw_data["ProvisioningArtifactDetail"]
        )

    Info = field("Info")
    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateProvisioningArtifactOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateProvisioningArtifactOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateProvisionedProductPlanInput:
    boto3_raw_data: "type_defs.CreateProvisionedProductPlanInputTypeDef" = (
        dataclasses.field()
    )

    PlanName = field("PlanName")
    PlanType = field("PlanType")
    ProductId = field("ProductId")
    ProvisionedProductName = field("ProvisionedProductName")
    ProvisioningArtifactId = field("ProvisioningArtifactId")
    IdempotencyToken = field("IdempotencyToken")
    AcceptLanguage = field("AcceptLanguage")
    NotificationArns = field("NotificationArns")
    PathId = field("PathId")

    @cached_property
    def ProvisioningParameters(self):  # pragma: no cover
        return UpdateProvisioningParameter.make_many(
            self.boto3_raw_data["ProvisioningParameters"]
        )

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateProvisionedProductPlanInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateProvisionedProductPlanInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProvisionedProductPlanDetails:
    boto3_raw_data: "type_defs.ProvisionedProductPlanDetailsTypeDef" = (
        dataclasses.field()
    )

    CreatedTime = field("CreatedTime")
    PathId = field("PathId")
    ProductId = field("ProductId")
    PlanName = field("PlanName")
    PlanId = field("PlanId")
    ProvisionProductId = field("ProvisionProductId")
    ProvisionProductName = field("ProvisionProductName")
    PlanType = field("PlanType")
    ProvisioningArtifactId = field("ProvisioningArtifactId")
    Status = field("Status")
    UpdatedTime = field("UpdatedTime")
    NotificationArns = field("NotificationArns")

    @cached_property
    def ProvisioningParameters(self):  # pragma: no cover
        return UpdateProvisioningParameter.make_many(
            self.boto3_raw_data["ProvisioningParameters"]
        )

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    StatusMessage = field("StatusMessage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ProvisionedProductPlanDetailsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProvisionedProductPlanDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTagOptionOutput:
    boto3_raw_data: "type_defs.CreateTagOptionOutputTypeDef" = dataclasses.field()

    @cached_property
    def TagOptionDetail(self):  # pragma: no cover
        return TagOptionDetail.make_one(self.boto3_raw_data["TagOptionDetail"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTagOptionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTagOptionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePortfolioOutput:
    boto3_raw_data: "type_defs.DescribePortfolioOutputTypeDef" = dataclasses.field()

    @cached_property
    def PortfolioDetail(self):  # pragma: no cover
        return PortfolioDetail.make_one(self.boto3_raw_data["PortfolioDetail"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def TagOptions(self):  # pragma: no cover
        return TagOptionDetail.make_many(self.boto3_raw_data["TagOptions"])

    @cached_property
    def Budgets(self):  # pragma: no cover
        return BudgetDetail.make_many(self.boto3_raw_data["Budgets"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribePortfolioOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePortfolioOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTagOptionOutput:
    boto3_raw_data: "type_defs.DescribeTagOptionOutputTypeDef" = dataclasses.field()

    @cached_property
    def TagOptionDetail(self):  # pragma: no cover
        return TagOptionDetail.make_one(self.boto3_raw_data["TagOptionDetail"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTagOptionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTagOptionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagOptionsOutput:
    boto3_raw_data: "type_defs.ListTagOptionsOutputTypeDef" = dataclasses.field()

    @cached_property
    def TagOptionDetails(self):  # pragma: no cover
        return TagOptionDetail.make_many(self.boto3_raw_data["TagOptionDetails"])

    PageToken = field("PageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagOptionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagOptionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTagOptionOutput:
    boto3_raw_data: "type_defs.UpdateTagOptionOutputTypeDef" = dataclasses.field()

    @cached_property
    def TagOptionDetail(self):  # pragma: no cover
        return TagOptionDetail.make_one(self.boto3_raw_data["TagOptionDetail"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateTagOptionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTagOptionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePortfolioSharesOutput:
    boto3_raw_data: "type_defs.DescribePortfolioSharesOutputTypeDef" = (
        dataclasses.field()
    )

    NextPageToken = field("NextPageToken")

    @cached_property
    def PortfolioShareDetails(self):  # pragma: no cover
        return PortfolioShareDetail.make_many(
            self.boto3_raw_data["PortfolioShareDetails"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribePortfolioSharesOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePortfolioSharesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeProductOutput:
    boto3_raw_data: "type_defs.DescribeProductOutputTypeDef" = dataclasses.field()

    @cached_property
    def ProductViewSummary(self):  # pragma: no cover
        return ProductViewSummary.make_one(self.boto3_raw_data["ProductViewSummary"])

    @cached_property
    def ProvisioningArtifacts(self):  # pragma: no cover
        return ProvisioningArtifact.make_many(
            self.boto3_raw_data["ProvisioningArtifacts"]
        )

    @cached_property
    def Budgets(self):  # pragma: no cover
        return BudgetDetail.make_many(self.boto3_raw_data["Budgets"])

    @cached_property
    def LaunchPaths(self):  # pragma: no cover
        return LaunchPath.make_many(self.boto3_raw_data["LaunchPaths"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeProductOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeProductOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeProductViewOutput:
    boto3_raw_data: "type_defs.DescribeProductViewOutputTypeDef" = dataclasses.field()

    @cached_property
    def ProductViewSummary(self):  # pragma: no cover
        return ProductViewSummary.make_one(self.boto3_raw_data["ProductViewSummary"])

    @cached_property
    def ProvisioningArtifacts(self):  # pragma: no cover
        return ProvisioningArtifact.make_many(
            self.boto3_raw_data["ProvisioningArtifacts"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeProductViewOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeProductViewOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProvisioningArtifactView:
    boto3_raw_data: "type_defs.ProvisioningArtifactViewTypeDef" = dataclasses.field()

    @cached_property
    def ProductViewSummary(self):  # pragma: no cover
        return ProductViewSummary.make_one(self.boto3_raw_data["ProductViewSummary"])

    @cached_property
    def ProvisioningArtifact(self):  # pragma: no cover
        return ProvisioningArtifact.make_one(
            self.boto3_raw_data["ProvisioningArtifact"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProvisioningArtifactViewTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProvisioningArtifactViewTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeProvisionedProductOutput:
    boto3_raw_data: "type_defs.DescribeProvisionedProductOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ProvisionedProductDetail(self):  # pragma: no cover
        return ProvisionedProductDetail.make_one(
            self.boto3_raw_data["ProvisionedProductDetail"]
        )

    @cached_property
    def CloudWatchDashboards(self):  # pragma: no cover
        return CloudWatchDashboard.make_many(
            self.boto3_raw_data["CloudWatchDashboards"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeProvisionedProductOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeProvisionedProductOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScanProvisionedProductsOutput:
    boto3_raw_data: "type_defs.ScanProvisionedProductsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ProvisionedProducts(self):  # pragma: no cover
        return ProvisionedProductDetail.make_many(
            self.boto3_raw_data["ProvisionedProducts"]
        )

    NextPageToken = field("NextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ScanProvisionedProductsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScanProvisionedProductsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetProvisionedProductOutputsOutput:
    boto3_raw_data: "type_defs.GetProvisionedProductOutputsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Outputs(self):  # pragma: no cover
        return RecordOutput.make_many(self.boto3_raw_data["Outputs"])

    NextPageToken = field("NextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetProvisionedProductOutputsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetProvisionedProductOutputsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotifyUpdateProvisionedProductEngineWorkflowResultInput:
    boto3_raw_data: (
        "type_defs.NotifyUpdateProvisionedProductEngineWorkflowResultInputTypeDef"
    ) = dataclasses.field()

    WorkflowToken = field("WorkflowToken")
    RecordId = field("RecordId")
    Status = field("Status")
    IdempotencyToken = field("IdempotencyToken")
    FailureReason = field("FailureReason")

    @cached_property
    def Outputs(self):  # pragma: no cover
        return RecordOutput.make_many(self.boto3_raw_data["Outputs"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.NotifyUpdateProvisionedProductEngineWorkflowResultInputTypeDef"
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
                "type_defs.NotifyUpdateProvisionedProductEngineWorkflowResultInputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeServiceActionExecutionParametersOutput:
    boto3_raw_data: (
        "type_defs.DescribeServiceActionExecutionParametersOutputTypeDef"
    ) = dataclasses.field()

    @cached_property
    def ServiceActionParameters(self):  # pragma: no cover
        return ExecutionParameter.make_many(
            self.boto3_raw_data["ServiceActionParameters"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeServiceActionExecutionParametersOutputTypeDef"
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
                "type_defs.DescribeServiceActionExecutionParametersOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EngineWorkflowResourceIdentifier:
    boto3_raw_data: "type_defs.EngineWorkflowResourceIdentifierTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def UniqueTag(self):  # pragma: no cover
        return UniqueTagResourceIdentifier.make_one(self.boto3_raw_data["UniqueTag"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EngineWorkflowResourceIdentifierTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EngineWorkflowResourceIdentifierTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAcceptedPortfolioSharesInputPaginate:
    boto3_raw_data: "type_defs.ListAcceptedPortfolioSharesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    AcceptLanguage = field("AcceptLanguage")
    PortfolioShareType = field("PortfolioShareType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAcceptedPortfolioSharesInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAcceptedPortfolioSharesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConstraintsForPortfolioInputPaginate:
    boto3_raw_data: "type_defs.ListConstraintsForPortfolioInputPaginateTypeDef" = (
        dataclasses.field()
    )

    PortfolioId = field("PortfolioId")
    AcceptLanguage = field("AcceptLanguage")
    ProductId = field("ProductId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListConstraintsForPortfolioInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConstraintsForPortfolioInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLaunchPathsInputPaginate:
    boto3_raw_data: "type_defs.ListLaunchPathsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    ProductId = field("ProductId")
    AcceptLanguage = field("AcceptLanguage")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLaunchPathsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLaunchPathsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOrganizationPortfolioAccessInputPaginate:
    boto3_raw_data: "type_defs.ListOrganizationPortfolioAccessInputPaginateTypeDef" = (
        dataclasses.field()
    )

    PortfolioId = field("PortfolioId")
    OrganizationNodeType = field("OrganizationNodeType")
    AcceptLanguage = field("AcceptLanguage")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListOrganizationPortfolioAccessInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOrganizationPortfolioAccessInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPortfoliosForProductInputPaginate:
    boto3_raw_data: "type_defs.ListPortfoliosForProductInputPaginateTypeDef" = (
        dataclasses.field()
    )

    ProductId = field("ProductId")
    AcceptLanguage = field("AcceptLanguage")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPortfoliosForProductInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPortfoliosForProductInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPortfoliosInputPaginate:
    boto3_raw_data: "type_defs.ListPortfoliosInputPaginateTypeDef" = dataclasses.field()

    AcceptLanguage = field("AcceptLanguage")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPortfoliosInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPortfoliosInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPrincipalsForPortfolioInputPaginate:
    boto3_raw_data: "type_defs.ListPrincipalsForPortfolioInputPaginateTypeDef" = (
        dataclasses.field()
    )

    PortfolioId = field("PortfolioId")
    AcceptLanguage = field("AcceptLanguage")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPrincipalsForPortfolioInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPrincipalsForPortfolioInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProvisionedProductPlansInputPaginate:
    boto3_raw_data: "type_defs.ListProvisionedProductPlansInputPaginateTypeDef" = (
        dataclasses.field()
    )

    AcceptLanguage = field("AcceptLanguage")
    ProvisionProductId = field("ProvisionProductId")

    @cached_property
    def AccessLevelFilter(self):  # pragma: no cover
        return AccessLevelFilter.make_one(self.boto3_raw_data["AccessLevelFilter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListProvisionedProductPlansInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProvisionedProductPlansInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProvisioningArtifactsForServiceActionInputPaginate:
    boto3_raw_data: (
        "type_defs.ListProvisioningArtifactsForServiceActionInputPaginateTypeDef"
    ) = dataclasses.field()

    ServiceActionId = field("ServiceActionId")
    AcceptLanguage = field("AcceptLanguage")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListProvisioningArtifactsForServiceActionInputPaginateTypeDef"
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
                "type_defs.ListProvisioningArtifactsForServiceActionInputPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourcesForTagOptionInputPaginate:
    boto3_raw_data: "type_defs.ListResourcesForTagOptionInputPaginateTypeDef" = (
        dataclasses.field()
    )

    TagOptionId = field("TagOptionId")
    ResourceType = field("ResourceType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResourcesForTagOptionInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourcesForTagOptionInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceActionsForProvisioningArtifactInputPaginate:
    boto3_raw_data: (
        "type_defs.ListServiceActionsForProvisioningArtifactInputPaginateTypeDef"
    ) = dataclasses.field()

    ProductId = field("ProductId")
    ProvisioningArtifactId = field("ProvisioningArtifactId")
    AcceptLanguage = field("AcceptLanguage")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListServiceActionsForProvisioningArtifactInputPaginateTypeDef"
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
                "type_defs.ListServiceActionsForProvisioningArtifactInputPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceActionsInputPaginate:
    boto3_raw_data: "type_defs.ListServiceActionsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    AcceptLanguage = field("AcceptLanguage")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListServiceActionsInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServiceActionsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScanProvisionedProductsInputPaginate:
    boto3_raw_data: "type_defs.ScanProvisionedProductsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    AcceptLanguage = field("AcceptLanguage")

    @cached_property
    def AccessLevelFilter(self):  # pragma: no cover
        return AccessLevelFilter.make_one(self.boto3_raw_data["AccessLevelFilter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ScanProvisionedProductsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScanProvisionedProductsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchProductsAsAdminInputPaginate:
    boto3_raw_data: "type_defs.SearchProductsAsAdminInputPaginateTypeDef" = (
        dataclasses.field()
    )

    AcceptLanguage = field("AcceptLanguage")
    PortfolioId = field("PortfolioId")
    Filters = field("Filters")
    SortBy = field("SortBy")
    SortOrder = field("SortOrder")
    ProductSource = field("ProductSource")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SearchProductsAsAdminInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchProductsAsAdminInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPrincipalsForPortfolioOutput:
    boto3_raw_data: "type_defs.ListPrincipalsForPortfolioOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Principals(self):  # pragma: no cover
        return Principal.make_many(self.boto3_raw_data["Principals"])

    NextPageToken = field("NextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListPrincipalsForPortfolioOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPrincipalsForPortfolioOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProvisionedProductPlansOutput:
    boto3_raw_data: "type_defs.ListProvisionedProductPlansOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ProvisionedProductPlans(self):  # pragma: no cover
        return ProvisionedProductPlanSummary.make_many(
            self.boto3_raw_data["ProvisionedProductPlans"]
        )

    NextPageToken = field("NextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListProvisionedProductPlansOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProvisionedProductPlansOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRecordHistoryInputPaginate:
    boto3_raw_data: "type_defs.ListRecordHistoryInputPaginateTypeDef" = (
        dataclasses.field()
    )

    AcceptLanguage = field("AcceptLanguage")

    @cached_property
    def AccessLevelFilter(self):  # pragma: no cover
        return AccessLevelFilter.make_one(self.boto3_raw_data["AccessLevelFilter"])

    @cached_property
    def SearchFilter(self):  # pragma: no cover
        return ListRecordHistorySearchFilter.make_one(
            self.boto3_raw_data["SearchFilter"]
        )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListRecordHistoryInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecordHistoryInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRecordHistoryInput:
    boto3_raw_data: "type_defs.ListRecordHistoryInputTypeDef" = dataclasses.field()

    AcceptLanguage = field("AcceptLanguage")

    @cached_property
    def AccessLevelFilter(self):  # pragma: no cover
        return AccessLevelFilter.make_one(self.boto3_raw_data["AccessLevelFilter"])

    @cached_property
    def SearchFilter(self):  # pragma: no cover
        return ListRecordHistorySearchFilter.make_one(
            self.boto3_raw_data["SearchFilter"]
        )

    PageSize = field("PageSize")
    PageToken = field("PageToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRecordHistoryInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecordHistoryInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourcesForTagOptionOutput:
    boto3_raw_data: "type_defs.ListResourcesForTagOptionOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ResourceDetails(self):  # pragma: no cover
        return ResourceDetail.make_many(self.boto3_raw_data["ResourceDetails"])

    PageToken = field("PageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListResourcesForTagOptionOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourcesForTagOptionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceActionsForProvisioningArtifactOutput:
    boto3_raw_data: (
        "type_defs.ListServiceActionsForProvisioningArtifactOutputTypeDef"
    ) = dataclasses.field()

    @cached_property
    def ServiceActionSummaries(self):  # pragma: no cover
        return ServiceActionSummary.make_many(
            self.boto3_raw_data["ServiceActionSummaries"]
        )

    NextPageToken = field("NextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListServiceActionsForProvisioningArtifactOutputTypeDef"
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
                "type_defs.ListServiceActionsForProvisioningArtifactOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceActionsOutput:
    boto3_raw_data: "type_defs.ListServiceActionsOutputTypeDef" = dataclasses.field()

    @cached_property
    def ServiceActionSummaries(self):  # pragma: no cover
        return ServiceActionSummary.make_many(
            self.boto3_raw_data["ServiceActionSummaries"]
        )

    NextPageToken = field("NextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListServiceActionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServiceActionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceActionDetail:
    boto3_raw_data: "type_defs.ServiceActionDetailTypeDef" = dataclasses.field()

    @cached_property
    def ServiceActionSummary(self):  # pragma: no cover
        return ServiceActionSummary.make_one(
            self.boto3_raw_data["ServiceActionSummary"]
        )

    Definition = field("Definition")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServiceActionDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceActionDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStackInstancesForProvisionedProductOutput:
    boto3_raw_data: "type_defs.ListStackInstancesForProvisionedProductOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def StackInstances(self):  # pragma: no cover
        return StackInstance.make_many(self.boto3_raw_data["StackInstances"])

    NextPageToken = field("NextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListStackInstancesForProvisionedProductOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStackInstancesForProvisionedProductOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagOptionsInputPaginate:
    boto3_raw_data: "type_defs.ListTagOptionsInputPaginateTypeDef" = dataclasses.field()

    @cached_property
    def Filters(self):  # pragma: no cover
        return ListTagOptionsFilters.make_one(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagOptionsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagOptionsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagOptionsInput:
    boto3_raw_data: "type_defs.ListTagOptionsInputTypeDef" = dataclasses.field()

    @cached_property
    def Filters(self):  # pragma: no cover
        return ListTagOptionsFilters.make_one(self.boto3_raw_data["Filters"])

    PageSize = field("PageSize")
    PageToken = field("PageToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagOptionsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagOptionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProvisioningArtifactParameter:
    boto3_raw_data: "type_defs.ProvisioningArtifactParameterTypeDef" = (
        dataclasses.field()
    )

    ParameterKey = field("ParameterKey")
    DefaultValue = field("DefaultValue")
    ParameterType = field("ParameterType")
    IsNoEcho = field("IsNoEcho")
    Description = field("Description")

    @cached_property
    def ParameterConstraints(self):  # pragma: no cover
        return ParameterConstraints.make_one(
            self.boto3_raw_data["ParameterConstraints"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ProvisioningArtifactParameterTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProvisioningArtifactParameterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchProductsOutput:
    boto3_raw_data: "type_defs.SearchProductsOutputTypeDef" = dataclasses.field()

    @cached_property
    def ProductViewSummaries(self):  # pragma: no cover
        return ProductViewSummary.make_many(self.boto3_raw_data["ProductViewSummaries"])

    ProductViewAggregations = field("ProductViewAggregations")
    NextPageToken = field("NextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchProductsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchProductsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProvisionProductInput:
    boto3_raw_data: "type_defs.ProvisionProductInputTypeDef" = dataclasses.field()

    ProvisionedProductName = field("ProvisionedProductName")
    ProvisionToken = field("ProvisionToken")
    AcceptLanguage = field("AcceptLanguage")
    ProductId = field("ProductId")
    ProductName = field("ProductName")
    ProvisioningArtifactId = field("ProvisioningArtifactId")
    ProvisioningArtifactName = field("ProvisioningArtifactName")
    PathId = field("PathId")
    PathName = field("PathName")

    @cached_property
    def ProvisioningParameters(self):  # pragma: no cover
        return ProvisioningParameter.make_many(
            self.boto3_raw_data["ProvisioningParameters"]
        )

    @cached_property
    def ProvisioningPreferences(self):  # pragma: no cover
        return ProvisioningPreferences.make_one(
            self.boto3_raw_data["ProvisioningPreferences"]
        )

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    NotificationArns = field("NotificationArns")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProvisionProductInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProvisionProductInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecordDetail:
    boto3_raw_data: "type_defs.RecordDetailTypeDef" = dataclasses.field()

    RecordId = field("RecordId")
    ProvisionedProductName = field("ProvisionedProductName")
    Status = field("Status")
    CreatedTime = field("CreatedTime")
    UpdatedTime = field("UpdatedTime")
    ProvisionedProductType = field("ProvisionedProductType")
    RecordType = field("RecordType")
    ProvisionedProductId = field("ProvisionedProductId")
    ProductId = field("ProductId")
    ProvisioningArtifactId = field("ProvisioningArtifactId")
    PathId = field("PathId")

    @cached_property
    def RecordErrors(self):  # pragma: no cover
        return RecordError.make_many(self.boto3_raw_data["RecordErrors"])

    @cached_property
    def RecordTags(self):  # pragma: no cover
        return RecordTag.make_many(self.boto3_raw_data["RecordTags"])

    LaunchRoleArn = field("LaunchRoleArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecordDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RecordDetailTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceChangeDetail:
    boto3_raw_data: "type_defs.ResourceChangeDetailTypeDef" = dataclasses.field()

    @cached_property
    def Target(self):  # pragma: no cover
        return ResourceTargetDefinition.make_one(self.boto3_raw_data["Target"])

    Evaluation = field("Evaluation")
    CausingEntity = field("CausingEntity")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceChangeDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceChangeDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ShareDetails:
    boto3_raw_data: "type_defs.ShareDetailsTypeDef" = dataclasses.field()

    SuccessfulShares = field("SuccessfulShares")

    @cached_property
    def ShareErrors(self):  # pragma: no cover
        return ShareError.make_many(self.boto3_raw_data["ShareErrors"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ShareDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ShareDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateProvisionedProductInput:
    boto3_raw_data: "type_defs.UpdateProvisionedProductInputTypeDef" = (
        dataclasses.field()
    )

    UpdateToken = field("UpdateToken")
    AcceptLanguage = field("AcceptLanguage")
    ProvisionedProductName = field("ProvisionedProductName")
    ProvisionedProductId = field("ProvisionedProductId")
    ProductId = field("ProductId")
    ProductName = field("ProductName")
    ProvisioningArtifactId = field("ProvisioningArtifactId")
    ProvisioningArtifactName = field("ProvisioningArtifactName")
    PathId = field("PathId")
    PathName = field("PathName")

    @cached_property
    def ProvisioningParameters(self):  # pragma: no cover
        return UpdateProvisioningParameter.make_many(
            self.boto3_raw_data["ProvisioningParameters"]
        )

    @cached_property
    def ProvisioningPreferences(self):  # pragma: no cover
        return UpdateProvisioningPreferences.make_one(
            self.boto3_raw_data["ProvisioningPreferences"]
        )

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateProvisionedProductInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateProvisionedProductInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceConnectionDetail:
    boto3_raw_data: "type_defs.SourceConnectionDetailTypeDef" = dataclasses.field()

    Type = field("Type")

    @cached_property
    def ConnectionParameters(self):  # pragma: no cover
        return SourceConnectionParameters.make_one(
            self.boto3_raw_data["ConnectionParameters"]
        )

    @cached_property
    def LastSync(self):  # pragma: no cover
        return LastSync.make_one(self.boto3_raw_data["LastSync"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SourceConnectionDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourceConnectionDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceConnection:
    boto3_raw_data: "type_defs.SourceConnectionTypeDef" = dataclasses.field()

    @cached_property
    def ConnectionParameters(self):  # pragma: no cover
        return SourceConnectionParameters.make_one(
            self.boto3_raw_data["ConnectionParameters"]
        )

    Type = field("Type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SourceConnectionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourceConnectionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLaunchPathsOutput:
    boto3_raw_data: "type_defs.ListLaunchPathsOutputTypeDef" = dataclasses.field()

    @cached_property
    def LaunchPathSummaries(self):  # pragma: no cover
        return LaunchPathSummary.make_many(self.boto3_raw_data["LaunchPathSummaries"])

    NextPageToken = field("NextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLaunchPathsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLaunchPathsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchProvisionedProductsOutput:
    boto3_raw_data: "type_defs.SearchProvisionedProductsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ProvisionedProducts(self):  # pragma: no cover
        return ProvisionedProductAttribute.make_many(
            self.boto3_raw_data["ProvisionedProducts"]
        )

    TotalResultsCount = field("TotalResultsCount")
    NextPageToken = field("NextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SearchProvisionedProductsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchProvisionedProductsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProvisioningArtifactsForServiceActionOutput:
    boto3_raw_data: (
        "type_defs.ListProvisioningArtifactsForServiceActionOutputTypeDef"
    ) = dataclasses.field()

    @cached_property
    def ProvisioningArtifactViews(self):  # pragma: no cover
        return ProvisioningArtifactView.make_many(
            self.boto3_raw_data["ProvisioningArtifactViews"]
        )

    NextPageToken = field("NextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListProvisioningArtifactsForServiceActionOutputTypeDef"
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
                "type_defs.ListProvisioningArtifactsForServiceActionOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotifyProvisionProductEngineWorkflowResultInput:
    boto3_raw_data: (
        "type_defs.NotifyProvisionProductEngineWorkflowResultInputTypeDef"
    ) = dataclasses.field()

    WorkflowToken = field("WorkflowToken")
    RecordId = field("RecordId")
    Status = field("Status")
    IdempotencyToken = field("IdempotencyToken")
    FailureReason = field("FailureReason")

    @cached_property
    def ResourceIdentifier(self):  # pragma: no cover
        return EngineWorkflowResourceIdentifier.make_one(
            self.boto3_raw_data["ResourceIdentifier"]
        )

    @cached_property
    def Outputs(self):  # pragma: no cover
        return RecordOutput.make_many(self.boto3_raw_data["Outputs"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.NotifyProvisionProductEngineWorkflowResultInputTypeDef"
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
                "type_defs.NotifyProvisionProductEngineWorkflowResultInputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateServiceActionOutput:
    boto3_raw_data: "type_defs.CreateServiceActionOutputTypeDef" = dataclasses.field()

    @cached_property
    def ServiceActionDetail(self):  # pragma: no cover
        return ServiceActionDetail.make_one(self.boto3_raw_data["ServiceActionDetail"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateServiceActionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateServiceActionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeServiceActionOutput:
    boto3_raw_data: "type_defs.DescribeServiceActionOutputTypeDef" = dataclasses.field()

    @cached_property
    def ServiceActionDetail(self):  # pragma: no cover
        return ServiceActionDetail.make_one(self.boto3_raw_data["ServiceActionDetail"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeServiceActionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeServiceActionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateServiceActionOutput:
    boto3_raw_data: "type_defs.UpdateServiceActionOutputTypeDef" = dataclasses.field()

    @cached_property
    def ServiceActionDetail(self):  # pragma: no cover
        return ServiceActionDetail.make_one(self.boto3_raw_data["ServiceActionDetail"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateServiceActionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateServiceActionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeProvisioningArtifactOutput:
    boto3_raw_data: "type_defs.DescribeProvisioningArtifactOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ProvisioningArtifactDetail(self):  # pragma: no cover
        return ProvisioningArtifactDetail.make_one(
            self.boto3_raw_data["ProvisioningArtifactDetail"]
        )

    Info = field("Info")
    Status = field("Status")

    @cached_property
    def ProvisioningArtifactParameters(self):  # pragma: no cover
        return ProvisioningArtifactParameter.make_many(
            self.boto3_raw_data["ProvisioningArtifactParameters"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeProvisioningArtifactOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeProvisioningArtifactOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeProvisioningParametersOutput:
    boto3_raw_data: "type_defs.DescribeProvisioningParametersOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ProvisioningArtifactParameters(self):  # pragma: no cover
        return ProvisioningArtifactParameter.make_many(
            self.boto3_raw_data["ProvisioningArtifactParameters"]
        )

    @cached_property
    def ConstraintSummaries(self):  # pragma: no cover
        return ConstraintSummary.make_many(self.boto3_raw_data["ConstraintSummaries"])

    @cached_property
    def UsageInstructions(self):  # pragma: no cover
        return UsageInstruction.make_many(self.boto3_raw_data["UsageInstructions"])

    @cached_property
    def TagOptions(self):  # pragma: no cover
        return TagOptionSummary.make_many(self.boto3_raw_data["TagOptions"])

    @cached_property
    def ProvisioningArtifactPreferences(self):  # pragma: no cover
        return ProvisioningArtifactPreferences.make_one(
            self.boto3_raw_data["ProvisioningArtifactPreferences"]
        )

    @cached_property
    def ProvisioningArtifactOutputs(self):  # pragma: no cover
        return ProvisioningArtifactOutput.make_many(
            self.boto3_raw_data["ProvisioningArtifactOutputs"]
        )

    @cached_property
    def ProvisioningArtifactOutputKeys(self):  # pragma: no cover
        return ProvisioningArtifactOutput.make_many(
            self.boto3_raw_data["ProvisioningArtifactOutputKeys"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeProvisioningParametersOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeProvisioningParametersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRecordOutput:
    boto3_raw_data: "type_defs.DescribeRecordOutputTypeDef" = dataclasses.field()

    @cached_property
    def RecordDetail(self):  # pragma: no cover
        return RecordDetail.make_one(self.boto3_raw_data["RecordDetail"])

    @cached_property
    def RecordOutputs(self):  # pragma: no cover
        return RecordOutput.make_many(self.boto3_raw_data["RecordOutputs"])

    NextPageToken = field("NextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeRecordOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRecordOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecuteProvisionedProductPlanOutput:
    boto3_raw_data: "type_defs.ExecuteProvisionedProductPlanOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RecordDetail(self):  # pragma: no cover
        return RecordDetail.make_one(self.boto3_raw_data["RecordDetail"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExecuteProvisionedProductPlanOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecuteProvisionedProductPlanOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecuteProvisionedProductServiceActionOutput:
    boto3_raw_data: "type_defs.ExecuteProvisionedProductServiceActionOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RecordDetail(self):  # pragma: no cover
        return RecordDetail.make_one(self.boto3_raw_data["RecordDetail"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExecuteProvisionedProductServiceActionOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecuteProvisionedProductServiceActionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportAsProvisionedProductOutput:
    boto3_raw_data: "type_defs.ImportAsProvisionedProductOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RecordDetail(self):  # pragma: no cover
        return RecordDetail.make_one(self.boto3_raw_data["RecordDetail"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ImportAsProvisionedProductOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportAsProvisionedProductOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRecordHistoryOutput:
    boto3_raw_data: "type_defs.ListRecordHistoryOutputTypeDef" = dataclasses.field()

    @cached_property
    def RecordDetails(self):  # pragma: no cover
        return RecordDetail.make_many(self.boto3_raw_data["RecordDetails"])

    NextPageToken = field("NextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRecordHistoryOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecordHistoryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProvisionProductOutput:
    boto3_raw_data: "type_defs.ProvisionProductOutputTypeDef" = dataclasses.field()

    @cached_property
    def RecordDetail(self):  # pragma: no cover
        return RecordDetail.make_one(self.boto3_raw_data["RecordDetail"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProvisionProductOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProvisionProductOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TerminateProvisionedProductOutput:
    boto3_raw_data: "type_defs.TerminateProvisionedProductOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RecordDetail(self):  # pragma: no cover
        return RecordDetail.make_one(self.boto3_raw_data["RecordDetail"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TerminateProvisionedProductOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TerminateProvisionedProductOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateProvisionedProductOutput:
    boto3_raw_data: "type_defs.UpdateProvisionedProductOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RecordDetail(self):  # pragma: no cover
        return RecordDetail.make_one(self.boto3_raw_data["RecordDetail"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateProvisionedProductOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateProvisionedProductOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceChange:
    boto3_raw_data: "type_defs.ResourceChangeTypeDef" = dataclasses.field()

    Action = field("Action")
    LogicalResourceId = field("LogicalResourceId")
    PhysicalResourceId = field("PhysicalResourceId")
    ResourceType = field("ResourceType")
    Replacement = field("Replacement")
    Scope = field("Scope")

    @cached_property
    def Details(self):  # pragma: no cover
        return ResourceChangeDetail.make_many(self.boto3_raw_data["Details"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceChangeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceChangeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePortfolioShareStatusOutput:
    boto3_raw_data: "type_defs.DescribePortfolioShareStatusOutputTypeDef" = (
        dataclasses.field()
    )

    PortfolioShareToken = field("PortfolioShareToken")
    PortfolioId = field("PortfolioId")
    OrganizationNodeValue = field("OrganizationNodeValue")
    Status = field("Status")

    @cached_property
    def ShareDetails(self):  # pragma: no cover
        return ShareDetails.make_one(self.boto3_raw_data["ShareDetails"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribePortfolioShareStatusOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePortfolioShareStatusOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProductViewDetail:
    boto3_raw_data: "type_defs.ProductViewDetailTypeDef" = dataclasses.field()

    @cached_property
    def ProductViewSummary(self):  # pragma: no cover
        return ProductViewSummary.make_one(self.boto3_raw_data["ProductViewSummary"])

    Status = field("Status")
    ProductARN = field("ProductARN")
    CreatedTime = field("CreatedTime")

    @cached_property
    def SourceConnection(self):  # pragma: no cover
        return SourceConnectionDetail.make_one(self.boto3_raw_data["SourceConnection"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProductViewDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProductViewDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateProductInput:
    boto3_raw_data: "type_defs.CreateProductInputTypeDef" = dataclasses.field()

    Name = field("Name")
    Owner = field("Owner")
    ProductType = field("ProductType")
    IdempotencyToken = field("IdempotencyToken")
    AcceptLanguage = field("AcceptLanguage")
    Description = field("Description")
    Distributor = field("Distributor")
    SupportDescription = field("SupportDescription")
    SupportEmail = field("SupportEmail")
    SupportUrl = field("SupportUrl")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def ProvisioningArtifactParameters(self):  # pragma: no cover
        return ProvisioningArtifactProperties.make_one(
            self.boto3_raw_data["ProvisioningArtifactParameters"]
        )

    @cached_property
    def SourceConnection(self):  # pragma: no cover
        return SourceConnection.make_one(self.boto3_raw_data["SourceConnection"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateProductInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateProductInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateProductInput:
    boto3_raw_data: "type_defs.UpdateProductInputTypeDef" = dataclasses.field()

    Id = field("Id")
    AcceptLanguage = field("AcceptLanguage")
    Name = field("Name")
    Owner = field("Owner")
    Description = field("Description")
    Distributor = field("Distributor")
    SupportDescription = field("SupportDescription")
    SupportEmail = field("SupportEmail")
    SupportUrl = field("SupportUrl")

    @cached_property
    def AddTags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["AddTags"])

    RemoveTags = field("RemoveTags")

    @cached_property
    def SourceConnection(self):  # pragma: no cover
        return SourceConnection.make_one(self.boto3_raw_data["SourceConnection"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateProductInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateProductInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeProvisionedProductPlanOutput:
    boto3_raw_data: "type_defs.DescribeProvisionedProductPlanOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ProvisionedProductPlanDetails(self):  # pragma: no cover
        return ProvisionedProductPlanDetails.make_one(
            self.boto3_raw_data["ProvisionedProductPlanDetails"]
        )

    @cached_property
    def ResourceChanges(self):  # pragma: no cover
        return ResourceChange.make_many(self.boto3_raw_data["ResourceChanges"])

    NextPageToken = field("NextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeProvisionedProductPlanOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeProvisionedProductPlanOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateProductOutput:
    boto3_raw_data: "type_defs.CreateProductOutputTypeDef" = dataclasses.field()

    @cached_property
    def ProductViewDetail(self):  # pragma: no cover
        return ProductViewDetail.make_one(self.boto3_raw_data["ProductViewDetail"])

    @cached_property
    def ProvisioningArtifactDetail(self):  # pragma: no cover
        return ProvisioningArtifactDetail.make_one(
            self.boto3_raw_data["ProvisioningArtifactDetail"]
        )

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateProductOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateProductOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeProductAsAdminOutput:
    boto3_raw_data: "type_defs.DescribeProductAsAdminOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ProductViewDetail(self):  # pragma: no cover
        return ProductViewDetail.make_one(self.boto3_raw_data["ProductViewDetail"])

    @cached_property
    def ProvisioningArtifactSummaries(self):  # pragma: no cover
        return ProvisioningArtifactSummary.make_many(
            self.boto3_raw_data["ProvisioningArtifactSummaries"]
        )

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def TagOptions(self):  # pragma: no cover
        return TagOptionDetail.make_many(self.boto3_raw_data["TagOptions"])

    @cached_property
    def Budgets(self):  # pragma: no cover
        return BudgetDetail.make_many(self.boto3_raw_data["Budgets"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeProductAsAdminOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeProductAsAdminOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchProductsAsAdminOutput:
    boto3_raw_data: "type_defs.SearchProductsAsAdminOutputTypeDef" = dataclasses.field()

    @cached_property
    def ProductViewDetails(self):  # pragma: no cover
        return ProductViewDetail.make_many(self.boto3_raw_data["ProductViewDetails"])

    NextPageToken = field("NextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchProductsAsAdminOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchProductsAsAdminOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateProductOutput:
    boto3_raw_data: "type_defs.UpdateProductOutputTypeDef" = dataclasses.field()

    @cached_property
    def ProductViewDetail(self):  # pragma: no cover
        return ProductViewDetail.make_one(self.boto3_raw_data["ProductViewDetail"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateProductOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateProductOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]

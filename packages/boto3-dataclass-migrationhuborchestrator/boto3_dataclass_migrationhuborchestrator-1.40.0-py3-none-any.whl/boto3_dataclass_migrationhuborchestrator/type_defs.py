# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_migrationhuborchestrator import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


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
class StepInputOutput:
    boto3_raw_data: "type_defs.StepInputOutputTypeDef" = dataclasses.field()

    integerValue = field("integerValue")
    stringValue = field("stringValue")
    listOfStringsValue = field("listOfStringsValue")
    mapOfStringValue = field("mapOfStringValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StepInputOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StepInputOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TemplateSource:
    boto3_raw_data: "type_defs.TemplateSourceTypeDef" = dataclasses.field()

    workflowId = field("workflowId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TemplateSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TemplateSourceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWorkflowStepGroupRequest:
    boto3_raw_data: "type_defs.CreateWorkflowStepGroupRequestTypeDef" = (
        dataclasses.field()
    )

    workflowId = field("workflowId")
    name = field("name")
    description = field("description")
    next = field("next")
    previous = field("previous")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateWorkflowStepGroupRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWorkflowStepGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Tool:
    boto3_raw_data: "type_defs.ToolTypeDef" = dataclasses.field()

    name = field("name")
    url = field("url")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ToolTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ToolTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMigrationWorkflowRequest:
    boto3_raw_data: "type_defs.DeleteMigrationWorkflowRequestTypeDef" = (
        dataclasses.field()
    )

    id = field("id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteMigrationWorkflowRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMigrationWorkflowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTemplateRequest:
    boto3_raw_data: "type_defs.DeleteTemplateRequestTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteWorkflowStepGroupRequest:
    boto3_raw_data: "type_defs.DeleteWorkflowStepGroupRequestTypeDef" = (
        dataclasses.field()
    )

    workflowId = field("workflowId")
    id = field("id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteWorkflowStepGroupRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteWorkflowStepGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteWorkflowStepRequest:
    boto3_raw_data: "type_defs.DeleteWorkflowStepRequestTypeDef" = dataclasses.field()

    id = field("id")
    stepGroupId = field("stepGroupId")
    workflowId = field("workflowId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteWorkflowStepRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteWorkflowStepRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMigrationWorkflowRequest:
    boto3_raw_data: "type_defs.GetMigrationWorkflowRequestTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMigrationWorkflowRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMigrationWorkflowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMigrationWorkflowTemplateRequest:
    boto3_raw_data: "type_defs.GetMigrationWorkflowTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    id = field("id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetMigrationWorkflowTemplateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMigrationWorkflowTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TemplateInput:
    boto3_raw_data: "type_defs.TemplateInputTypeDef" = dataclasses.field()

    inputName = field("inputName")
    dataType = field("dataType")
    required = field("required")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TemplateInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TemplateInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTemplateStepGroupRequest:
    boto3_raw_data: "type_defs.GetTemplateStepGroupRequestTypeDef" = dataclasses.field()

    templateId = field("templateId")
    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTemplateStepGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTemplateStepGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTemplateStepRequest:
    boto3_raw_data: "type_defs.GetTemplateStepRequestTypeDef" = dataclasses.field()

    id = field("id")
    templateId = field("templateId")
    stepGroupId = field("stepGroupId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTemplateStepRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTemplateStepRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StepOutput:
    boto3_raw_data: "type_defs.StepOutputTypeDef" = dataclasses.field()

    name = field("name")
    dataType = field("dataType")
    required = field("required")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StepOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StepOutputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWorkflowStepGroupRequest:
    boto3_raw_data: "type_defs.GetWorkflowStepGroupRequestTypeDef" = dataclasses.field()

    id = field("id")
    workflowId = field("workflowId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetWorkflowStepGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWorkflowStepGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWorkflowStepRequest:
    boto3_raw_data: "type_defs.GetWorkflowStepRequestTypeDef" = dataclasses.field()

    workflowId = field("workflowId")
    stepGroupId = field("stepGroupId")
    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetWorkflowStepRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWorkflowStepRequestTypeDef"]
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
class ListMigrationWorkflowTemplatesRequest:
    boto3_raw_data: "type_defs.ListMigrationWorkflowTemplatesRequestTypeDef" = (
        dataclasses.field()
    )

    maxResults = field("maxResults")
    nextToken = field("nextToken")
    name = field("name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListMigrationWorkflowTemplatesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMigrationWorkflowTemplatesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TemplateSummary:
    boto3_raw_data: "type_defs.TemplateSummaryTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    arn = field("arn")
    description = field("description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TemplateSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TemplateSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMigrationWorkflowsRequest:
    boto3_raw_data: "type_defs.ListMigrationWorkflowsRequestTypeDef" = (
        dataclasses.field()
    )

    maxResults = field("maxResults")
    nextToken = field("nextToken")
    templateId = field("templateId")
    adsApplicationConfigurationName = field("adsApplicationConfigurationName")
    status = field("status")
    name = field("name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListMigrationWorkflowsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMigrationWorkflowsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MigrationWorkflowSummary:
    boto3_raw_data: "type_defs.MigrationWorkflowSummaryTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    templateId = field("templateId")
    adsApplicationConfigurationName = field("adsApplicationConfigurationName")
    status = field("status")
    creationTime = field("creationTime")
    endTime = field("endTime")
    statusMessage = field("statusMessage")
    completedSteps = field("completedSteps")
    totalSteps = field("totalSteps")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MigrationWorkflowSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MigrationWorkflowSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPluginsRequest:
    boto3_raw_data: "type_defs.ListPluginsRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPluginsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPluginsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PluginSummary:
    boto3_raw_data: "type_defs.PluginSummaryTypeDef" = dataclasses.field()

    pluginId = field("pluginId")
    hostname = field("hostname")
    status = field("status")
    ipAddress = field("ipAddress")
    version = field("version")
    registeredTime = field("registeredTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PluginSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PluginSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceRequest:
    boto3_raw_data: "type_defs.ListTagsForResourceRequestTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")

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
class ListTemplateStepGroupsRequest:
    boto3_raw_data: "type_defs.ListTemplateStepGroupsRequestTypeDef" = (
        dataclasses.field()
    )

    templateId = field("templateId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListTemplateStepGroupsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTemplateStepGroupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TemplateStepGroupSummary:
    boto3_raw_data: "type_defs.TemplateStepGroupSummaryTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    previous = field("previous")
    next = field("next")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TemplateStepGroupSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TemplateStepGroupSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTemplateStepsRequest:
    boto3_raw_data: "type_defs.ListTemplateStepsRequestTypeDef" = dataclasses.field()

    templateId = field("templateId")
    stepGroupId = field("stepGroupId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTemplateStepsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTemplateStepsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TemplateStepSummary:
    boto3_raw_data: "type_defs.TemplateStepSummaryTypeDef" = dataclasses.field()

    id = field("id")
    stepGroupId = field("stepGroupId")
    templateId = field("templateId")
    name = field("name")
    stepActionType = field("stepActionType")
    targetType = field("targetType")
    owner = field("owner")
    previous = field("previous")
    next = field("next")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TemplateStepSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TemplateStepSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkflowStepGroupsRequest:
    boto3_raw_data: "type_defs.ListWorkflowStepGroupsRequestTypeDef" = (
        dataclasses.field()
    )

    workflowId = field("workflowId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListWorkflowStepGroupsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkflowStepGroupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkflowStepGroupSummary:
    boto3_raw_data: "type_defs.WorkflowStepGroupSummaryTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    owner = field("owner")
    status = field("status")
    previous = field("previous")
    next = field("next")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkflowStepGroupSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkflowStepGroupSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkflowStepsRequest:
    boto3_raw_data: "type_defs.ListWorkflowStepsRequestTypeDef" = dataclasses.field()

    workflowId = field("workflowId")
    stepGroupId = field("stepGroupId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWorkflowStepsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkflowStepsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkflowStepSummary:
    boto3_raw_data: "type_defs.WorkflowStepSummaryTypeDef" = dataclasses.field()

    stepId = field("stepId")
    name = field("name")
    stepActionType = field("stepActionType")
    owner = field("owner")
    previous = field("previous")
    next = field("next")
    status = field("status")
    statusMessage = field("statusMessage")
    noOfSrvCompleted = field("noOfSrvCompleted")
    noOfSrvFailed = field("noOfSrvFailed")
    totalNoOfSrv = field("totalNoOfSrv")
    description = field("description")
    scriptLocation = field("scriptLocation")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkflowStepSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkflowStepSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PlatformCommand:
    boto3_raw_data: "type_defs.PlatformCommandTypeDef" = dataclasses.field()

    linux = field("linux")
    windows = field("windows")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PlatformCommandTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PlatformCommandTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PlatformScriptKey:
    boto3_raw_data: "type_defs.PlatformScriptKeyTypeDef" = dataclasses.field()

    linux = field("linux")
    windows = field("windows")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PlatformScriptKeyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PlatformScriptKeyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetryWorkflowStepRequest:
    boto3_raw_data: "type_defs.RetryWorkflowStepRequestTypeDef" = dataclasses.field()

    workflowId = field("workflowId")
    stepGroupId = field("stepGroupId")
    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RetryWorkflowStepRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetryWorkflowStepRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartMigrationWorkflowRequest:
    boto3_raw_data: "type_defs.StartMigrationWorkflowRequestTypeDef" = (
        dataclasses.field()
    )

    id = field("id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartMigrationWorkflowRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartMigrationWorkflowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StepInput:
    boto3_raw_data: "type_defs.StepInputTypeDef" = dataclasses.field()

    integerValue = field("integerValue")
    stringValue = field("stringValue")
    listOfStringsValue = field("listOfStringsValue")
    mapOfStringValue = field("mapOfStringValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StepInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StepInputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopMigrationWorkflowRequest:
    boto3_raw_data: "type_defs.StopMigrationWorkflowRequestTypeDef" = (
        dataclasses.field()
    )

    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopMigrationWorkflowRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopMigrationWorkflowRequestTypeDef"]
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

    resourceArn = field("resourceArn")
    tags = field("tags")

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
class UntagResourceRequest:
    boto3_raw_data: "type_defs.UntagResourceRequestTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")
    tagKeys = field("tagKeys")

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
class UpdateTemplateRequest:
    boto3_raw_data: "type_defs.UpdateTemplateRequestTypeDef" = dataclasses.field()

    id = field("id")
    templateName = field("templateName")
    templateDescription = field("templateDescription")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateWorkflowStepGroupRequest:
    boto3_raw_data: "type_defs.UpdateWorkflowStepGroupRequestTypeDef" = (
        dataclasses.field()
    )

    workflowId = field("workflowId")
    id = field("id")
    name = field("name")
    description = field("description")
    next = field("next")
    previous = field("previous")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateWorkflowStepGroupRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWorkflowStepGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkflowStepOutputUnionOutput:
    boto3_raw_data: "type_defs.WorkflowStepOutputUnionOutputTypeDef" = (
        dataclasses.field()
    )

    integerValue = field("integerValue")
    stringValue = field("stringValue")
    listOfStringValue = field("listOfStringValue")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.WorkflowStepOutputUnionOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkflowStepOutputUnionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkflowStepOutputUnion:
    boto3_raw_data: "type_defs.WorkflowStepOutputUnionTypeDef" = dataclasses.field()

    integerValue = field("integerValue")
    stringValue = field("stringValue")
    listOfStringValue = field("listOfStringValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkflowStepOutputUnionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkflowStepOutputUnionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTemplateResponse:
    boto3_raw_data: "type_defs.CreateTemplateResponseTypeDef" = dataclasses.field()

    templateId = field("templateId")
    templateArn = field("templateArn")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTemplateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWorkflowStepResponse:
    boto3_raw_data: "type_defs.CreateWorkflowStepResponseTypeDef" = dataclasses.field()

    id = field("id")
    stepGroupId = field("stepGroupId")
    workflowId = field("workflowId")
    name = field("name")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWorkflowStepResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWorkflowStepResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMigrationWorkflowResponse:
    boto3_raw_data: "type_defs.DeleteMigrationWorkflowResponseTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    arn = field("arn")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteMigrationWorkflowResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMigrationWorkflowResponseTypeDef"]
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

    tags = field("tags")

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
class RetryWorkflowStepResponse:
    boto3_raw_data: "type_defs.RetryWorkflowStepResponseTypeDef" = dataclasses.field()

    stepGroupId = field("stepGroupId")
    workflowId = field("workflowId")
    id = field("id")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RetryWorkflowStepResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetryWorkflowStepResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartMigrationWorkflowResponse:
    boto3_raw_data: "type_defs.StartMigrationWorkflowResponseTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    arn = field("arn")
    status = field("status")
    statusMessage = field("statusMessage")
    lastStartTime = field("lastStartTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartMigrationWorkflowResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartMigrationWorkflowResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopMigrationWorkflowResponse:
    boto3_raw_data: "type_defs.StopMigrationWorkflowResponseTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    arn = field("arn")
    status = field("status")
    statusMessage = field("statusMessage")
    lastStopTime = field("lastStopTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StopMigrationWorkflowResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopMigrationWorkflowResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTemplateResponse:
    boto3_raw_data: "type_defs.UpdateTemplateResponseTypeDef" = dataclasses.field()

    templateId = field("templateId")
    templateArn = field("templateArn")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateTemplateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateWorkflowStepResponse:
    boto3_raw_data: "type_defs.UpdateWorkflowStepResponseTypeDef" = dataclasses.field()

    id = field("id")
    stepGroupId = field("stepGroupId")
    workflowId = field("workflowId")
    name = field("name")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateWorkflowStepResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWorkflowStepResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMigrationWorkflowResponse:
    boto3_raw_data: "type_defs.CreateMigrationWorkflowResponseTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    arn = field("arn")
    name = field("name")
    description = field("description")
    templateId = field("templateId")
    adsApplicationConfigurationId = field("adsApplicationConfigurationId")
    workflowInputs = field("workflowInputs")
    stepTargets = field("stepTargets")
    status = field("status")
    creationTime = field("creationTime")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateMigrationWorkflowResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMigrationWorkflowResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMigrationWorkflowResponse:
    boto3_raw_data: "type_defs.UpdateMigrationWorkflowResponseTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    arn = field("arn")
    name = field("name")
    description = field("description")
    templateId = field("templateId")
    adsApplicationConfigurationId = field("adsApplicationConfigurationId")
    workflowInputs = field("workflowInputs")
    stepTargets = field("stepTargets")
    status = field("status")
    creationTime = field("creationTime")
    lastModifiedTime = field("lastModifiedTime")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateMigrationWorkflowResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMigrationWorkflowResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTemplateRequest:
    boto3_raw_data: "type_defs.CreateTemplateRequestTypeDef" = dataclasses.field()

    templateName = field("templateName")

    @cached_property
    def templateSource(self):  # pragma: no cover
        return TemplateSource.make_one(self.boto3_raw_data["templateSource"])

    templateDescription = field("templateDescription")
    clientToken = field("clientToken")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWorkflowStepGroupResponse:
    boto3_raw_data: "type_defs.CreateWorkflowStepGroupResponseTypeDef" = (
        dataclasses.field()
    )

    workflowId = field("workflowId")
    name = field("name")
    id = field("id")
    description = field("description")

    @cached_property
    def tools(self):  # pragma: no cover
        return Tool.make_many(self.boto3_raw_data["tools"])

    next = field("next")
    previous = field("previous")
    creationTime = field("creationTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateWorkflowStepGroupResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWorkflowStepGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMigrationWorkflowResponse:
    boto3_raw_data: "type_defs.GetMigrationWorkflowResponseTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    arn = field("arn")
    name = field("name")
    description = field("description")
    templateId = field("templateId")
    adsApplicationConfigurationId = field("adsApplicationConfigurationId")
    adsApplicationName = field("adsApplicationName")
    status = field("status")
    statusMessage = field("statusMessage")
    creationTime = field("creationTime")
    lastStartTime = field("lastStartTime")
    lastStopTime = field("lastStopTime")
    lastModifiedTime = field("lastModifiedTime")
    endTime = field("endTime")

    @cached_property
    def tools(self):  # pragma: no cover
        return Tool.make_many(self.boto3_raw_data["tools"])

    totalSteps = field("totalSteps")
    completedSteps = field("completedSteps")
    workflowInputs = field("workflowInputs")
    tags = field("tags")
    workflowBucket = field("workflowBucket")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMigrationWorkflowResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMigrationWorkflowResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTemplateStepGroupResponse:
    boto3_raw_data: "type_defs.GetTemplateStepGroupResponseTypeDef" = (
        dataclasses.field()
    )

    templateId = field("templateId")
    id = field("id")
    name = field("name")
    description = field("description")
    status = field("status")
    creationTime = field("creationTime")
    lastModifiedTime = field("lastModifiedTime")

    @cached_property
    def tools(self):  # pragma: no cover
        return Tool.make_many(self.boto3_raw_data["tools"])

    previous = field("previous")
    next = field("next")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTemplateStepGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTemplateStepGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWorkflowStepGroupResponse:
    boto3_raw_data: "type_defs.GetWorkflowStepGroupResponseTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    workflowId = field("workflowId")
    name = field("name")
    description = field("description")
    status = field("status")
    owner = field("owner")
    creationTime = field("creationTime")
    lastModifiedTime = field("lastModifiedTime")
    endTime = field("endTime")

    @cached_property
    def tools(self):  # pragma: no cover
        return Tool.make_many(self.boto3_raw_data["tools"])

    previous = field("previous")
    next = field("next")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetWorkflowStepGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWorkflowStepGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateWorkflowStepGroupResponse:
    boto3_raw_data: "type_defs.UpdateWorkflowStepGroupResponseTypeDef" = (
        dataclasses.field()
    )

    workflowId = field("workflowId")
    name = field("name")
    id = field("id")
    description = field("description")

    @cached_property
    def tools(self):  # pragma: no cover
        return Tool.make_many(self.boto3_raw_data["tools"])

    next = field("next")
    previous = field("previous")
    lastModifiedTime = field("lastModifiedTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateWorkflowStepGroupResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWorkflowStepGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMigrationWorkflowTemplateResponse:
    boto3_raw_data: "type_defs.GetMigrationWorkflowTemplateResponseTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    templateArn = field("templateArn")
    name = field("name")
    description = field("description")

    @cached_property
    def inputs(self):  # pragma: no cover
        return TemplateInput.make_many(self.boto3_raw_data["inputs"])

    @cached_property
    def tools(self):  # pragma: no cover
        return Tool.make_many(self.boto3_raw_data["tools"])

    creationTime = field("creationTime")
    owner = field("owner")
    status = field("status")
    statusMessage = field("statusMessage")
    templateClass = field("templateClass")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetMigrationWorkflowTemplateResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMigrationWorkflowTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMigrationWorkflowTemplatesRequestPaginate:
    boto3_raw_data: "type_defs.ListMigrationWorkflowTemplatesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    name = field("name")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListMigrationWorkflowTemplatesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMigrationWorkflowTemplatesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMigrationWorkflowsRequestPaginate:
    boto3_raw_data: "type_defs.ListMigrationWorkflowsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    templateId = field("templateId")
    adsApplicationConfigurationName = field("adsApplicationConfigurationName")
    status = field("status")
    name = field("name")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListMigrationWorkflowsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMigrationWorkflowsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPluginsRequestPaginate:
    boto3_raw_data: "type_defs.ListPluginsRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPluginsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPluginsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTemplateStepGroupsRequestPaginate:
    boto3_raw_data: "type_defs.ListTemplateStepGroupsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    templateId = field("templateId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTemplateStepGroupsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTemplateStepGroupsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTemplateStepsRequestPaginate:
    boto3_raw_data: "type_defs.ListTemplateStepsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    templateId = field("templateId")
    stepGroupId = field("stepGroupId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListTemplateStepsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTemplateStepsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkflowStepGroupsRequestPaginate:
    boto3_raw_data: "type_defs.ListWorkflowStepGroupsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    workflowId = field("workflowId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListWorkflowStepGroupsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkflowStepGroupsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkflowStepsRequestPaginate:
    boto3_raw_data: "type_defs.ListWorkflowStepsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    workflowId = field("workflowId")
    stepGroupId = field("stepGroupId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListWorkflowStepsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkflowStepsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMigrationWorkflowTemplatesResponse:
    boto3_raw_data: "type_defs.ListMigrationWorkflowTemplatesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def templateSummary(self):  # pragma: no cover
        return TemplateSummary.make_many(self.boto3_raw_data["templateSummary"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListMigrationWorkflowTemplatesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMigrationWorkflowTemplatesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMigrationWorkflowsResponse:
    boto3_raw_data: "type_defs.ListMigrationWorkflowsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def migrationWorkflowSummary(self):  # pragma: no cover
        return MigrationWorkflowSummary.make_many(
            self.boto3_raw_data["migrationWorkflowSummary"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListMigrationWorkflowsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMigrationWorkflowsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPluginsResponse:
    boto3_raw_data: "type_defs.ListPluginsResponseTypeDef" = dataclasses.field()

    @cached_property
    def plugins(self):  # pragma: no cover
        return PluginSummary.make_many(self.boto3_raw_data["plugins"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPluginsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPluginsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTemplateStepGroupsResponse:
    boto3_raw_data: "type_defs.ListTemplateStepGroupsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def templateStepGroupSummary(self):  # pragma: no cover
        return TemplateStepGroupSummary.make_many(
            self.boto3_raw_data["templateStepGroupSummary"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListTemplateStepGroupsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTemplateStepGroupsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTemplateStepsResponse:
    boto3_raw_data: "type_defs.ListTemplateStepsResponseTypeDef" = dataclasses.field()

    @cached_property
    def templateStepSummaryList(self):  # pragma: no cover
        return TemplateStepSummary.make_many(
            self.boto3_raw_data["templateStepSummaryList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTemplateStepsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTemplateStepsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkflowStepGroupsResponse:
    boto3_raw_data: "type_defs.ListWorkflowStepGroupsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def workflowStepGroupsSummary(self):  # pragma: no cover
        return WorkflowStepGroupSummary.make_many(
            self.boto3_raw_data["workflowStepGroupsSummary"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListWorkflowStepGroupsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkflowStepGroupsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkflowStepsResponse:
    boto3_raw_data: "type_defs.ListWorkflowStepsResponseTypeDef" = dataclasses.field()

    @cached_property
    def workflowStepsSummary(self):  # pragma: no cover
        return WorkflowStepSummary.make_many(
            self.boto3_raw_data["workflowStepsSummary"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWorkflowStepsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkflowStepsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StepAutomationConfiguration:
    boto3_raw_data: "type_defs.StepAutomationConfigurationTypeDef" = dataclasses.field()

    scriptLocationS3Bucket = field("scriptLocationS3Bucket")

    @cached_property
    def scriptLocationS3Key(self):  # pragma: no cover
        return PlatformScriptKey.make_one(self.boto3_raw_data["scriptLocationS3Key"])

    @cached_property
    def command(self):  # pragma: no cover
        return PlatformCommand.make_one(self.boto3_raw_data["command"])

    runEnvironment = field("runEnvironment")
    targetType = field("targetType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StepAutomationConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StepAutomationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkflowStepAutomationConfiguration:
    boto3_raw_data: "type_defs.WorkflowStepAutomationConfigurationTypeDef" = (
        dataclasses.field()
    )

    scriptLocationS3Bucket = field("scriptLocationS3Bucket")

    @cached_property
    def scriptLocationS3Key(self):  # pragma: no cover
        return PlatformScriptKey.make_one(self.boto3_raw_data["scriptLocationS3Key"])

    @cached_property
    def command(self):  # pragma: no cover
        return PlatformCommand.make_one(self.boto3_raw_data["command"])

    runEnvironment = field("runEnvironment")
    targetType = field("targetType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.WorkflowStepAutomationConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkflowStepAutomationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkflowStepExtra:
    boto3_raw_data: "type_defs.WorkflowStepExtraTypeDef" = dataclasses.field()

    name = field("name")
    dataType = field("dataType")
    required = field("required")

    @cached_property
    def value(self):  # pragma: no cover
        return WorkflowStepOutputUnionOutput.make_one(self.boto3_raw_data["value"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WorkflowStepExtraTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkflowStepExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTemplateStepResponse:
    boto3_raw_data: "type_defs.GetTemplateStepResponseTypeDef" = dataclasses.field()

    id = field("id")
    stepGroupId = field("stepGroupId")
    templateId = field("templateId")
    name = field("name")
    description = field("description")
    stepActionType = field("stepActionType")
    creationTime = field("creationTime")
    previous = field("previous")
    next = field("next")

    @cached_property
    def outputs(self):  # pragma: no cover
        return StepOutput.make_many(self.boto3_raw_data["outputs"])

    @cached_property
    def stepAutomationConfiguration(self):  # pragma: no cover
        return StepAutomationConfiguration.make_one(
            self.boto3_raw_data["stepAutomationConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTemplateStepResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTemplateStepResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMigrationWorkflowRequest:
    boto3_raw_data: "type_defs.CreateMigrationWorkflowRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    templateId = field("templateId")
    inputParameters = field("inputParameters")
    description = field("description")
    applicationConfigurationId = field("applicationConfigurationId")
    stepTargets = field("stepTargets")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateMigrationWorkflowRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMigrationWorkflowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMigrationWorkflowRequest:
    boto3_raw_data: "type_defs.UpdateMigrationWorkflowRequestTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    name = field("name")
    description = field("description")
    inputParameters = field("inputParameters")
    stepTargets = field("stepTargets")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateMigrationWorkflowRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMigrationWorkflowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWorkflowStepResponse:
    boto3_raw_data: "type_defs.GetWorkflowStepResponseTypeDef" = dataclasses.field()

    name = field("name")
    stepGroupId = field("stepGroupId")
    workflowId = field("workflowId")
    stepId = field("stepId")
    description = field("description")
    stepActionType = field("stepActionType")
    owner = field("owner")

    @cached_property
    def workflowStepAutomationConfiguration(self):  # pragma: no cover
        return WorkflowStepAutomationConfiguration.make_one(
            self.boto3_raw_data["workflowStepAutomationConfiguration"]
        )

    stepTarget = field("stepTarget")

    @cached_property
    def outputs(self):  # pragma: no cover
        return WorkflowStepExtra.make_many(self.boto3_raw_data["outputs"])

    previous = field("previous")
    next = field("next")
    status = field("status")
    statusMessage = field("statusMessage")
    scriptOutputLocation = field("scriptOutputLocation")
    creationTime = field("creationTime")
    lastStartTime = field("lastStartTime")
    endTime = field("endTime")
    noOfSrvCompleted = field("noOfSrvCompleted")
    noOfSrvFailed = field("noOfSrvFailed")
    totalNoOfSrv = field("totalNoOfSrv")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetWorkflowStepResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWorkflowStepResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkflowStepOutput:
    boto3_raw_data: "type_defs.WorkflowStepOutputTypeDef" = dataclasses.field()

    name = field("name")
    dataType = field("dataType")
    required = field("required")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkflowStepOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkflowStepOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWorkflowStepRequest:
    boto3_raw_data: "type_defs.CreateWorkflowStepRequestTypeDef" = dataclasses.field()

    name = field("name")
    stepGroupId = field("stepGroupId")
    workflowId = field("workflowId")
    stepActionType = field("stepActionType")
    description = field("description")

    @cached_property
    def workflowStepAutomationConfiguration(self):  # pragma: no cover
        return WorkflowStepAutomationConfiguration.make_one(
            self.boto3_raw_data["workflowStepAutomationConfiguration"]
        )

    stepTarget = field("stepTarget")
    outputs = field("outputs")
    previous = field("previous")
    next = field("next")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWorkflowStepRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWorkflowStepRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateWorkflowStepRequest:
    boto3_raw_data: "type_defs.UpdateWorkflowStepRequestTypeDef" = dataclasses.field()

    id = field("id")
    stepGroupId = field("stepGroupId")
    workflowId = field("workflowId")
    name = field("name")
    description = field("description")
    stepActionType = field("stepActionType")

    @cached_property
    def workflowStepAutomationConfiguration(self):  # pragma: no cover
        return WorkflowStepAutomationConfiguration.make_one(
            self.boto3_raw_data["workflowStepAutomationConfiguration"]
        )

    stepTarget = field("stepTarget")
    outputs = field("outputs")
    previous = field("previous")
    next = field("next")
    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateWorkflowStepRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWorkflowStepRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]

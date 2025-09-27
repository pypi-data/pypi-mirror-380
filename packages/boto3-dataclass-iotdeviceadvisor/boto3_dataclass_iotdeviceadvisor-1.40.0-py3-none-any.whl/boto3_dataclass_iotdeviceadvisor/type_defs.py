# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_iotdeviceadvisor import type_defs


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
class DeleteSuiteDefinitionRequest:
    boto3_raw_data: "type_defs.DeleteSuiteDefinitionRequestTypeDef" = (
        dataclasses.field()
    )

    suiteDefinitionId = field("suiteDefinitionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSuiteDefinitionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSuiteDefinitionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeviceUnderTest:
    boto3_raw_data: "type_defs.DeviceUnderTestTypeDef" = dataclasses.field()

    thingArn = field("thingArn")
    certificateArn = field("certificateArn")
    deviceRoleArn = field("deviceRoleArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeviceUnderTestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeviceUnderTestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEndpointRequest:
    boto3_raw_data: "type_defs.GetEndpointRequestTypeDef" = dataclasses.field()

    thingArn = field("thingArn")
    certificateArn = field("certificateArn")
    deviceRoleArn = field("deviceRoleArn")
    authenticationMethod = field("authenticationMethod")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEndpointRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSuiteDefinitionRequest:
    boto3_raw_data: "type_defs.GetSuiteDefinitionRequestTypeDef" = dataclasses.field()

    suiteDefinitionId = field("suiteDefinitionId")
    suiteDefinitionVersion = field("suiteDefinitionVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSuiteDefinitionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSuiteDefinitionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSuiteRunReportRequest:
    boto3_raw_data: "type_defs.GetSuiteRunReportRequestTypeDef" = dataclasses.field()

    suiteDefinitionId = field("suiteDefinitionId")
    suiteRunId = field("suiteRunId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSuiteRunReportRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSuiteRunReportRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSuiteRunRequest:
    boto3_raw_data: "type_defs.GetSuiteRunRequestTypeDef" = dataclasses.field()

    suiteDefinitionId = field("suiteDefinitionId")
    suiteRunId = field("suiteRunId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSuiteRunRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSuiteRunRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSuiteDefinitionsRequest:
    boto3_raw_data: "type_defs.ListSuiteDefinitionsRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSuiteDefinitionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSuiteDefinitionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSuiteRunsRequest:
    boto3_raw_data: "type_defs.ListSuiteRunsRequestTypeDef" = dataclasses.field()

    suiteDefinitionId = field("suiteDefinitionId")
    suiteDefinitionVersion = field("suiteDefinitionVersion")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSuiteRunsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSuiteRunsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SuiteRunInformation:
    boto3_raw_data: "type_defs.SuiteRunInformationTypeDef" = dataclasses.field()

    suiteDefinitionId = field("suiteDefinitionId")
    suiteDefinitionVersion = field("suiteDefinitionVersion")
    suiteDefinitionName = field("suiteDefinitionName")
    suiteRunId = field("suiteRunId")
    createdAt = field("createdAt")
    startedAt = field("startedAt")
    endAt = field("endAt")
    status = field("status")
    passed = field("passed")
    failed = field("failed")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SuiteRunInformationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SuiteRunInformationTypeDef"]
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
class StopSuiteRunRequest:
    boto3_raw_data: "type_defs.StopSuiteRunRequestTypeDef" = dataclasses.field()

    suiteDefinitionId = field("suiteDefinitionId")
    suiteRunId = field("suiteRunId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopSuiteRunRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopSuiteRunRequestTypeDef"]
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
class TestCaseScenario:
    boto3_raw_data: "type_defs.TestCaseScenarioTypeDef" = dataclasses.field()

    testCaseScenarioId = field("testCaseScenarioId")
    testCaseScenarioType = field("testCaseScenarioType")
    status = field("status")
    failure = field("failure")
    systemMessage = field("systemMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TestCaseScenarioTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestCaseScenarioTypeDef"]
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
class CreateSuiteDefinitionResponse:
    boto3_raw_data: "type_defs.CreateSuiteDefinitionResponseTypeDef" = (
        dataclasses.field()
    )

    suiteDefinitionId = field("suiteDefinitionId")
    suiteDefinitionArn = field("suiteDefinitionArn")
    suiteDefinitionName = field("suiteDefinitionName")
    createdAt = field("createdAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateSuiteDefinitionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSuiteDefinitionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEndpointResponse:
    boto3_raw_data: "type_defs.GetEndpointResponseTypeDef" = dataclasses.field()

    endpoint = field("endpoint")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEndpointResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSuiteRunReportResponse:
    boto3_raw_data: "type_defs.GetSuiteRunReportResponseTypeDef" = dataclasses.field()

    qualificationReportDownloadUrl = field("qualificationReportDownloadUrl")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSuiteRunReportResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSuiteRunReportResponseTypeDef"]
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
class StartSuiteRunResponse:
    boto3_raw_data: "type_defs.StartSuiteRunResponseTypeDef" = dataclasses.field()

    suiteRunId = field("suiteRunId")
    suiteRunArn = field("suiteRunArn")
    createdAt = field("createdAt")
    endpoint = field("endpoint")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartSuiteRunResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSuiteRunResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSuiteDefinitionResponse:
    boto3_raw_data: "type_defs.UpdateSuiteDefinitionResponseTypeDef" = (
        dataclasses.field()
    )

    suiteDefinitionId = field("suiteDefinitionId")
    suiteDefinitionArn = field("suiteDefinitionArn")
    suiteDefinitionName = field("suiteDefinitionName")
    suiteDefinitionVersion = field("suiteDefinitionVersion")
    createdAt = field("createdAt")
    lastUpdatedAt = field("lastUpdatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateSuiteDefinitionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSuiteDefinitionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SuiteDefinitionConfigurationOutput:
    boto3_raw_data: "type_defs.SuiteDefinitionConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    suiteDefinitionName = field("suiteDefinitionName")
    rootGroup = field("rootGroup")
    devicePermissionRoleArn = field("devicePermissionRoleArn")

    @cached_property
    def devices(self):  # pragma: no cover
        return DeviceUnderTest.make_many(self.boto3_raw_data["devices"])

    intendedForQualification = field("intendedForQualification")
    isLongDurationTest = field("isLongDurationTest")
    protocol = field("protocol")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SuiteDefinitionConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SuiteDefinitionConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SuiteDefinitionConfiguration:
    boto3_raw_data: "type_defs.SuiteDefinitionConfigurationTypeDef" = (
        dataclasses.field()
    )

    suiteDefinitionName = field("suiteDefinitionName")
    rootGroup = field("rootGroup")
    devicePermissionRoleArn = field("devicePermissionRoleArn")

    @cached_property
    def devices(self):  # pragma: no cover
        return DeviceUnderTest.make_many(self.boto3_raw_data["devices"])

    intendedForQualification = field("intendedForQualification")
    isLongDurationTest = field("isLongDurationTest")
    protocol = field("protocol")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SuiteDefinitionConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SuiteDefinitionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SuiteDefinitionInformation:
    boto3_raw_data: "type_defs.SuiteDefinitionInformationTypeDef" = dataclasses.field()

    suiteDefinitionId = field("suiteDefinitionId")
    suiteDefinitionName = field("suiteDefinitionName")

    @cached_property
    def defaultDevices(self):  # pragma: no cover
        return DeviceUnderTest.make_many(self.boto3_raw_data["defaultDevices"])

    intendedForQualification = field("intendedForQualification")
    isLongDurationTest = field("isLongDurationTest")
    protocol = field("protocol")
    createdAt = field("createdAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SuiteDefinitionInformationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SuiteDefinitionInformationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SuiteRunConfigurationOutput:
    boto3_raw_data: "type_defs.SuiteRunConfigurationOutputTypeDef" = dataclasses.field()

    @cached_property
    def primaryDevice(self):  # pragma: no cover
        return DeviceUnderTest.make_one(self.boto3_raw_data["primaryDevice"])

    selectedTestList = field("selectedTestList")
    parallelRun = field("parallelRun")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SuiteRunConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SuiteRunConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SuiteRunConfiguration:
    boto3_raw_data: "type_defs.SuiteRunConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def primaryDevice(self):  # pragma: no cover
        return DeviceUnderTest.make_one(self.boto3_raw_data["primaryDevice"])

    selectedTestList = field("selectedTestList")
    parallelRun = field("parallelRun")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SuiteRunConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SuiteRunConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSuiteRunsResponse:
    boto3_raw_data: "type_defs.ListSuiteRunsResponseTypeDef" = dataclasses.field()

    @cached_property
    def suiteRunsList(self):  # pragma: no cover
        return SuiteRunInformation.make_many(self.boto3_raw_data["suiteRunsList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSuiteRunsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSuiteRunsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestCaseRun:
    boto3_raw_data: "type_defs.TestCaseRunTypeDef" = dataclasses.field()

    testCaseRunId = field("testCaseRunId")
    testCaseDefinitionId = field("testCaseDefinitionId")
    testCaseDefinitionName = field("testCaseDefinitionName")
    status = field("status")
    startTime = field("startTime")
    endTime = field("endTime")
    logUrl = field("logUrl")
    warnings = field("warnings")
    failure = field("failure")

    @cached_property
    def testScenarios(self):  # pragma: no cover
        return TestCaseScenario.make_many(self.boto3_raw_data["testScenarios"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TestCaseRunTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TestCaseRunTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSuiteDefinitionResponse:
    boto3_raw_data: "type_defs.GetSuiteDefinitionResponseTypeDef" = dataclasses.field()

    suiteDefinitionId = field("suiteDefinitionId")
    suiteDefinitionArn = field("suiteDefinitionArn")
    suiteDefinitionVersion = field("suiteDefinitionVersion")
    latestVersion = field("latestVersion")

    @cached_property
    def suiteDefinitionConfiguration(self):  # pragma: no cover
        return SuiteDefinitionConfigurationOutput.make_one(
            self.boto3_raw_data["suiteDefinitionConfiguration"]
        )

    createdAt = field("createdAt")
    lastModifiedAt = field("lastModifiedAt")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSuiteDefinitionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSuiteDefinitionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSuiteDefinitionsResponse:
    boto3_raw_data: "type_defs.ListSuiteDefinitionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def suiteDefinitionInformationList(self):  # pragma: no cover
        return SuiteDefinitionInformation.make_many(
            self.boto3_raw_data["suiteDefinitionInformationList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSuiteDefinitionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSuiteDefinitionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GroupResult:
    boto3_raw_data: "type_defs.GroupResultTypeDef" = dataclasses.field()

    groupId = field("groupId")
    groupName = field("groupName")

    @cached_property
    def tests(self):  # pragma: no cover
        return TestCaseRun.make_many(self.boto3_raw_data["tests"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GroupResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GroupResultTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSuiteDefinitionRequest:
    boto3_raw_data: "type_defs.CreateSuiteDefinitionRequestTypeDef" = (
        dataclasses.field()
    )

    suiteDefinitionConfiguration = field("suiteDefinitionConfiguration")
    tags = field("tags")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSuiteDefinitionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSuiteDefinitionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSuiteDefinitionRequest:
    boto3_raw_data: "type_defs.UpdateSuiteDefinitionRequestTypeDef" = (
        dataclasses.field()
    )

    suiteDefinitionId = field("suiteDefinitionId")
    suiteDefinitionConfiguration = field("suiteDefinitionConfiguration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSuiteDefinitionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSuiteDefinitionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartSuiteRunRequest:
    boto3_raw_data: "type_defs.StartSuiteRunRequestTypeDef" = dataclasses.field()

    suiteDefinitionId = field("suiteDefinitionId")
    suiteRunConfiguration = field("suiteRunConfiguration")
    suiteDefinitionVersion = field("suiteDefinitionVersion")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartSuiteRunRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSuiteRunRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestResult:
    boto3_raw_data: "type_defs.TestResultTypeDef" = dataclasses.field()

    @cached_property
    def groups(self):  # pragma: no cover
        return GroupResult.make_many(self.boto3_raw_data["groups"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TestResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TestResultTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSuiteRunResponse:
    boto3_raw_data: "type_defs.GetSuiteRunResponseTypeDef" = dataclasses.field()

    suiteDefinitionId = field("suiteDefinitionId")
    suiteDefinitionVersion = field("suiteDefinitionVersion")
    suiteRunId = field("suiteRunId")
    suiteRunArn = field("suiteRunArn")

    @cached_property
    def suiteRunConfiguration(self):  # pragma: no cover
        return SuiteRunConfigurationOutput.make_one(
            self.boto3_raw_data["suiteRunConfiguration"]
        )

    @cached_property
    def testResult(self):  # pragma: no cover
        return TestResult.make_one(self.boto3_raw_data["testResult"])

    startTime = field("startTime")
    endTime = field("endTime")
    status = field("status")
    errorReason = field("errorReason")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSuiteRunResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSuiteRunResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]

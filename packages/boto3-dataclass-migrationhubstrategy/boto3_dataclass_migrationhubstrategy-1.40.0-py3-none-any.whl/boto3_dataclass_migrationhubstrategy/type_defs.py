# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_migrationhubstrategy import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AnalysisStatusUnion:
    boto3_raw_data: "type_defs.AnalysisStatusUnionTypeDef" = dataclasses.field()

    runtimeAnalysisStatus = field("runtimeAnalysisStatus")
    srcCodeOrDbAnalysisStatus = field("srcCodeOrDbAnalysisStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalysisStatusUnionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalysisStatusUnionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalyzableServerSummary:
    boto3_raw_data: "type_defs.AnalyzableServerSummaryTypeDef" = dataclasses.field()

    hostname = field("hostname")
    ipAddress = field("ipAddress")
    source = field("source")
    vmId = field("vmId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalyzableServerSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalyzableServerSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalyzerNameUnion:
    boto3_raw_data: "type_defs.AnalyzerNameUnionTypeDef" = dataclasses.field()

    binaryAnalyzerName = field("binaryAnalyzerName")
    runTimeAnalyzerName = field("runTimeAnalyzerName")
    sourceCodeAnalyzerName = field("sourceCodeAnalyzerName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AnalyzerNameUnionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalyzerNameUnionTypeDef"]
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

    s3Bucket = field("s3Bucket")
    s3key = field("s3key")

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
class AntipatternSeveritySummary:
    boto3_raw_data: "type_defs.AntipatternSeveritySummaryTypeDef" = dataclasses.field()

    count = field("count")
    severity = field("severity")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AntipatternSeveritySummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AntipatternSeveritySummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AppUnitError:
    boto3_raw_data: "type_defs.AppUnitErrorTypeDef" = dataclasses.field()

    appUnitErrorCategory = field("appUnitErrorCategory")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AppUnitErrorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AppUnitErrorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatabaseConfigDetail:
    boto3_raw_data: "type_defs.DatabaseConfigDetailTypeDef" = dataclasses.field()

    secretName = field("secretName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DatabaseConfigDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatabaseConfigDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceCodeRepository:
    boto3_raw_data: "type_defs.SourceCodeRepositoryTypeDef" = dataclasses.field()

    branch = field("branch")
    projectName = field("projectName")
    repository = field("repository")
    versionControlType = field("versionControlType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SourceCodeRepositoryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourceCodeRepositoryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationComponentStatusSummary:
    boto3_raw_data: "type_defs.ApplicationComponentStatusSummaryTypeDef" = (
        dataclasses.field()
    )

    count = field("count")
    srcCodeOrDbAnalysisStatus = field("srcCodeOrDbAnalysisStatus")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ApplicationComponentStatusSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationComponentStatusSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationComponentSummary:
    boto3_raw_data: "type_defs.ApplicationComponentSummaryTypeDef" = dataclasses.field()

    appType = field("appType")
    count = field("count")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApplicationComponentSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationComponentSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServerStatusSummary:
    boto3_raw_data: "type_defs.ServerStatusSummaryTypeDef" = dataclasses.field()

    count = field("count")
    runTimeAssessmentStatus = field("runTimeAssessmentStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServerStatusSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServerStatusSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServerSummary:
    boto3_raw_data: "type_defs.ServerSummaryTypeDef" = dataclasses.field()

    ServerOsType = field("ServerOsType")
    count = field("count")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServerSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ServerSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StrategySummary:
    boto3_raw_data: "type_defs.StrategySummaryTypeDef" = dataclasses.field()

    count = field("count")
    strategy = field("strategy")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StrategySummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StrategySummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssessmentTargetOutput:
    boto3_raw_data: "type_defs.AssessmentTargetOutputTypeDef" = dataclasses.field()

    condition = field("condition")
    name = field("name")
    values = field("values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssessmentTargetOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssessmentTargetOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssessmentTarget:
    boto3_raw_data: "type_defs.AssessmentTargetTypeDef" = dataclasses.field()

    condition = field("condition")
    name = field("name")
    values = field("values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssessmentTargetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssessmentTargetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociatedApplication:
    boto3_raw_data: "type_defs.AssociatedApplicationTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociatedApplicationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociatedApplicationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AwsManagedResourcesOutput:
    boto3_raw_data: "type_defs.AwsManagedResourcesOutputTypeDef" = dataclasses.field()

    targetDestination = field("targetDestination")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AwsManagedResourcesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AwsManagedResourcesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AwsManagedResources:
    boto3_raw_data: "type_defs.AwsManagedResourcesTypeDef" = dataclasses.field()

    targetDestination = field("targetDestination")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AwsManagedResourcesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AwsManagedResourcesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BusinessGoals:
    boto3_raw_data: "type_defs.BusinessGoalsTypeDef" = dataclasses.field()

    licenseCostReduction = field("licenseCostReduction")
    modernizeInfrastructureWithCloudNativeTechnologies = field(
        "modernizeInfrastructureWithCloudNativeTechnologies"
    )
    reduceOperationalOverheadWithManagedServices = field(
        "reduceOperationalOverheadWithManagedServices"
    )
    speedOfMigration = field("speedOfMigration")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BusinessGoalsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BusinessGoalsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IPAddressBasedRemoteInfo:
    boto3_raw_data: "type_defs.IPAddressBasedRemoteInfoTypeDef" = dataclasses.field()

    authType = field("authType")
    ipAddressConfigurationTimeStamp = field("ipAddressConfigurationTimeStamp")
    osType = field("osType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IPAddressBasedRemoteInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IPAddressBasedRemoteInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipelineInfo:
    boto3_raw_data: "type_defs.PipelineInfoTypeDef" = dataclasses.field()

    pipelineConfigurationTimeStamp = field("pipelineConfigurationTimeStamp")
    pipelineType = field("pipelineType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PipelineInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PipelineInfoTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoteSourceCodeAnalysisServerInfo:
    boto3_raw_data: "type_defs.RemoteSourceCodeAnalysisServerInfoTypeDef" = (
        dataclasses.field()
    )

    remoteSourceCodeAnalysisServerConfigurationTimestamp = field(
        "remoteSourceCodeAnalysisServerConfigurationTimestamp"
    )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RemoteSourceCodeAnalysisServerInfoTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoteSourceCodeAnalysisServerInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VcenterBasedRemoteInfo:
    boto3_raw_data: "type_defs.VcenterBasedRemoteInfoTypeDef" = dataclasses.field()

    osType = field("osType")
    vcenterConfigurationTimeStamp = field("vcenterConfigurationTimeStamp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VcenterBasedRemoteInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VcenterBasedRemoteInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VersionControlInfo:
    boto3_raw_data: "type_defs.VersionControlInfoTypeDef" = dataclasses.field()

    versionControlConfigurationTimeStamp = field("versionControlConfigurationTimeStamp")
    versionControlType = field("versionControlType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VersionControlInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VersionControlInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataCollectionDetails:
    boto3_raw_data: "type_defs.DataCollectionDetailsTypeDef" = dataclasses.field()

    completionTime = field("completionTime")
    failed = field("failed")
    inProgress = field("inProgress")
    servers = field("servers")
    startTime = field("startTime")
    status = field("status")
    statusMessage = field("statusMessage")
    success = field("success")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataCollectionDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataCollectionDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HeterogeneousOutput:
    boto3_raw_data: "type_defs.HeterogeneousOutputTypeDef" = dataclasses.field()

    targetDatabaseEngine = field("targetDatabaseEngine")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HeterogeneousOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HeterogeneousOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HomogeneousOutput:
    boto3_raw_data: "type_defs.HomogeneousOutputTypeDef" = dataclasses.field()

    targetDatabaseEngine = field("targetDatabaseEngine")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HomogeneousOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HomogeneousOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NoDatabaseMigrationPreferenceOutput:
    boto3_raw_data: "type_defs.NoDatabaseMigrationPreferenceOutputTypeDef" = (
        dataclasses.field()
    )

    targetDatabaseEngine = field("targetDatabaseEngine")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.NoDatabaseMigrationPreferenceOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NoDatabaseMigrationPreferenceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Heterogeneous:
    boto3_raw_data: "type_defs.HeterogeneousTypeDef" = dataclasses.field()

    targetDatabaseEngine = field("targetDatabaseEngine")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HeterogeneousTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HeterogeneousTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Homogeneous:
    boto3_raw_data: "type_defs.HomogeneousTypeDef" = dataclasses.field()

    targetDatabaseEngine = field("targetDatabaseEngine")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HomogeneousTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HomogeneousTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NoDatabaseMigrationPreference:
    boto3_raw_data: "type_defs.NoDatabaseMigrationPreferenceTypeDef" = (
        dataclasses.field()
    )

    targetDatabaseEngine = field("targetDatabaseEngine")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.NoDatabaseMigrationPreferenceTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NoDatabaseMigrationPreferenceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApplicationComponentDetailsRequest:
    boto3_raw_data: "type_defs.GetApplicationComponentDetailsRequestTypeDef" = (
        dataclasses.field()
    )

    applicationComponentId = field("applicationComponentId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetApplicationComponentDetailsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApplicationComponentDetailsRequestTypeDef"]
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
class GetApplicationComponentStrategiesRequest:
    boto3_raw_data: "type_defs.GetApplicationComponentStrategiesRequestTypeDef" = (
        dataclasses.field()
    )

    applicationComponentId = field("applicationComponentId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetApplicationComponentStrategiesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApplicationComponentStrategiesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAssessmentRequest:
    boto3_raw_data: "type_defs.GetAssessmentRequestTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAssessmentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAssessmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetImportFileTaskRequest:
    boto3_raw_data: "type_defs.GetImportFileTaskRequestTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetImportFileTaskRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetImportFileTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRecommendationReportDetailsRequest:
    boto3_raw_data: "type_defs.GetRecommendationReportDetailsRequestTypeDef" = (
        dataclasses.field()
    )

    id = field("id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRecommendationReportDetailsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRecommendationReportDetailsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecommendationReportDetails:
    boto3_raw_data: "type_defs.RecommendationReportDetailsTypeDef" = dataclasses.field()

    completionTime = field("completionTime")
    s3Bucket = field("s3Bucket")
    s3Keys = field("s3Keys")
    startTime = field("startTime")
    status = field("status")
    statusMessage = field("statusMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecommendationReportDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecommendationReportDetailsTypeDef"]
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
class GetServerDetailsRequest:
    boto3_raw_data: "type_defs.GetServerDetailsRequestTypeDef" = dataclasses.field()

    serverId = field("serverId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetServerDetailsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServerDetailsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServerStrategiesRequest:
    boto3_raw_data: "type_defs.GetServerStrategiesRequestTypeDef" = dataclasses.field()

    serverId = field("serverId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetServerStrategiesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServerStrategiesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Group:
    boto3_raw_data: "type_defs.GroupTypeDef" = dataclasses.field()

    name = field("name")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GroupTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportFileTaskInformation:
    boto3_raw_data: "type_defs.ImportFileTaskInformationTypeDef" = dataclasses.field()

    completionTime = field("completionTime")
    id = field("id")
    importName = field("importName")
    inputS3Bucket = field("inputS3Bucket")
    inputS3Key = field("inputS3Key")
    numberOfRecordsFailed = field("numberOfRecordsFailed")
    numberOfRecordsSuccess = field("numberOfRecordsSuccess")
    startTime = field("startTime")
    status = field("status")
    statusReportS3Bucket = field("statusReportS3Bucket")
    statusReportS3Key = field("statusReportS3Key")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportFileTaskInformationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportFileTaskInformationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAnalyzableServersRequest:
    boto3_raw_data: "type_defs.ListAnalyzableServersRequestTypeDef" = (
        dataclasses.field()
    )

    maxResults = field("maxResults")
    nextToken = field("nextToken")
    sort = field("sort")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAnalyzableServersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAnalyzableServersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCollectorsRequest:
    boto3_raw_data: "type_defs.ListCollectorsRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCollectorsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCollectorsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImportFileTaskRequest:
    boto3_raw_data: "type_defs.ListImportFileTaskRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListImportFileTaskRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImportFileTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NoManagementPreferenceOutput:
    boto3_raw_data: "type_defs.NoManagementPreferenceOutputTypeDef" = (
        dataclasses.field()
    )

    targetDestination = field("targetDestination")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NoManagementPreferenceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NoManagementPreferenceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SelfManageResourcesOutput:
    boto3_raw_data: "type_defs.SelfManageResourcesOutputTypeDef" = dataclasses.field()

    targetDestination = field("targetDestination")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SelfManageResourcesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SelfManageResourcesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NoManagementPreference:
    boto3_raw_data: "type_defs.NoManagementPreferenceTypeDef" = dataclasses.field()

    targetDestination = field("targetDestination")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NoManagementPreferenceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NoManagementPreferenceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SelfManageResources:
    boto3_raw_data: "type_defs.SelfManageResourcesTypeDef" = dataclasses.field()

    targetDestination = field("targetDestination")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SelfManageResourcesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SelfManageResourcesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkInfo:
    boto3_raw_data: "type_defs.NetworkInfoTypeDef" = dataclasses.field()

    interfaceName = field("interfaceName")
    ipAddress = field("ipAddress")
    macAddress = field("macAddress")
    netMask = field("netMask")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NetworkInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NetworkInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OSInfo:
    boto3_raw_data: "type_defs.OSInfoTypeDef" = dataclasses.field()

    type = field("type")
    version = field("version")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OSInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OSInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TransformationTool:
    boto3_raw_data: "type_defs.TransformationToolTypeDef" = dataclasses.field()

    description = field("description")
    name = field("name")
    tranformationToolInstallationLink = field("tranformationToolInstallationLink")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TransformationToolTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TransformationToolTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServerError:
    boto3_raw_data: "type_defs.ServerErrorTypeDef" = dataclasses.field()

    serverErrorCategory = field("serverErrorCategory")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServerErrorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ServerErrorTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceCode:
    boto3_raw_data: "type_defs.SourceCodeTypeDef" = dataclasses.field()

    location = field("location")
    projectName = field("projectName")
    sourceVersion = field("sourceVersion")
    versionControl = field("versionControl")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SourceCodeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SourceCodeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopAssessmentRequest:
    boto3_raw_data: "type_defs.StopAssessmentRequestTypeDef" = dataclasses.field()

    assessmentId = field("assessmentId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopAssessmentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopAssessmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StrategyOption:
    boto3_raw_data: "type_defs.StrategyOptionTypeDef" = dataclasses.field()

    isPreferred = field("isPreferred")
    strategy = field("strategy")
    targetDestination = field("targetDestination")
    toolName = field("toolName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StrategyOptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StrategyOptionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AntipatternReportResult:
    boto3_raw_data: "type_defs.AntipatternReportResultTypeDef" = dataclasses.field()

    @cached_property
    def analyzerName(self):  # pragma: no cover
        return AnalyzerNameUnion.make_one(self.boto3_raw_data["analyzerName"])

    @cached_property
    def antiPatternReportS3Object(self):  # pragma: no cover
        return S3Object.make_one(self.boto3_raw_data["antiPatternReportS3Object"])

    antipatternReportStatus = field("antipatternReportStatus")
    antipatternReportStatusMessage = field("antipatternReportStatusMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AntipatternReportResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AntipatternReportResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssessmentSummary:
    boto3_raw_data: "type_defs.AssessmentSummaryTypeDef" = dataclasses.field()

    @cached_property
    def antipatternReportS3Object(self):  # pragma: no cover
        return S3Object.make_one(self.boto3_raw_data["antipatternReportS3Object"])

    antipatternReportStatus = field("antipatternReportStatus")
    antipatternReportStatusMessage = field("antipatternReportStatusMessage")
    lastAnalyzedTimestamp = field("lastAnalyzedTimestamp")

    @cached_property
    def listAntipatternSeveritySummary(self):  # pragma: no cover
        return AntipatternSeveritySummary.make_many(
            self.boto3_raw_data["listAntipatternSeveritySummary"]
        )

    @cached_property
    def listApplicationComponentStatusSummary(self):  # pragma: no cover
        return ApplicationComponentStatusSummary.make_many(
            self.boto3_raw_data["listApplicationComponentStatusSummary"]
        )

    @cached_property
    def listApplicationComponentStrategySummary(self):  # pragma: no cover
        return StrategySummary.make_many(
            self.boto3_raw_data["listApplicationComponentStrategySummary"]
        )

    @cached_property
    def listApplicationComponentSummary(self):  # pragma: no cover
        return ApplicationComponentSummary.make_many(
            self.boto3_raw_data["listApplicationComponentSummary"]
        )

    @cached_property
    def listServerStatusSummary(self):  # pragma: no cover
        return ServerStatusSummary.make_many(
            self.boto3_raw_data["listServerStatusSummary"]
        )

    @cached_property
    def listServerStrategySummary(self):  # pragma: no cover
        return StrategySummary.make_many(
            self.boto3_raw_data["listServerStrategySummary"]
        )

    @cached_property
    def listServerSummary(self):  # pragma: no cover
        return ServerSummary.make_many(self.boto3_raw_data["listServerSummary"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssessmentSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssessmentSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PrioritizeBusinessGoals:
    boto3_raw_data: "type_defs.PrioritizeBusinessGoalsTypeDef" = dataclasses.field()

    @cached_property
    def businessGoals(self):  # pragma: no cover
        return BusinessGoals.make_one(self.boto3_raw_data["businessGoals"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PrioritizeBusinessGoalsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PrioritizeBusinessGoalsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigurationSummary:
    boto3_raw_data: "type_defs.ConfigurationSummaryTypeDef" = dataclasses.field()

    @cached_property
    def ipAddressBasedRemoteInfoList(self):  # pragma: no cover
        return IPAddressBasedRemoteInfo.make_many(
            self.boto3_raw_data["ipAddressBasedRemoteInfoList"]
        )

    @cached_property
    def pipelineInfoList(self):  # pragma: no cover
        return PipelineInfo.make_many(self.boto3_raw_data["pipelineInfoList"])

    @cached_property
    def remoteSourceCodeAnalysisServerInfo(self):  # pragma: no cover
        return RemoteSourceCodeAnalysisServerInfo.make_one(
            self.boto3_raw_data["remoteSourceCodeAnalysisServerInfo"]
        )

    @cached_property
    def vcenterBasedRemoteInfoList(self):  # pragma: no cover
        return VcenterBasedRemoteInfo.make_many(
            self.boto3_raw_data["vcenterBasedRemoteInfoList"]
        )

    @cached_property
    def versionControlInfoList(self):  # pragma: no cover
        return VersionControlInfo.make_many(
            self.boto3_raw_data["versionControlInfoList"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfigurationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigurationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatabaseMigrationPreferenceOutput:
    boto3_raw_data: "type_defs.DatabaseMigrationPreferenceOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def heterogeneous(self):  # pragma: no cover
        return HeterogeneousOutput.make_one(self.boto3_raw_data["heterogeneous"])

    @cached_property
    def homogeneous(self):  # pragma: no cover
        return HomogeneousOutput.make_one(self.boto3_raw_data["homogeneous"])

    @cached_property
    def noPreference(self):  # pragma: no cover
        return NoDatabaseMigrationPreferenceOutput.make_one(
            self.boto3_raw_data["noPreference"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DatabaseMigrationPreferenceOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatabaseMigrationPreferenceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatabaseMigrationPreference:
    boto3_raw_data: "type_defs.DatabaseMigrationPreferenceTypeDef" = dataclasses.field()

    @cached_property
    def heterogeneous(self):  # pragma: no cover
        return Heterogeneous.make_one(self.boto3_raw_data["heterogeneous"])

    @cached_property
    def homogeneous(self):  # pragma: no cover
        return Homogeneous.make_one(self.boto3_raw_data["homogeneous"])

    @cached_property
    def noPreference(self):  # pragma: no cover
        return NoDatabaseMigrationPreference.make_one(
            self.boto3_raw_data["noPreference"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DatabaseMigrationPreferenceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatabaseMigrationPreferenceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAssessmentResponse:
    boto3_raw_data: "type_defs.GetAssessmentResponseTypeDef" = dataclasses.field()

    @cached_property
    def assessmentTargets(self):  # pragma: no cover
        return AssessmentTargetOutput.make_many(
            self.boto3_raw_data["assessmentTargets"]
        )

    @cached_property
    def dataCollectionDetails(self):  # pragma: no cover
        return DataCollectionDetails.make_one(
            self.boto3_raw_data["dataCollectionDetails"]
        )

    id = field("id")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAssessmentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAssessmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetImportFileTaskResponse:
    boto3_raw_data: "type_defs.GetImportFileTaskResponseTypeDef" = dataclasses.field()

    completionTime = field("completionTime")
    id = field("id")
    importName = field("importName")
    inputS3Bucket = field("inputS3Bucket")
    inputS3Key = field("inputS3Key")
    numberOfRecordsFailed = field("numberOfRecordsFailed")
    numberOfRecordsSuccess = field("numberOfRecordsSuccess")
    startTime = field("startTime")
    status = field("status")
    statusReportS3Bucket = field("statusReportS3Bucket")
    statusReportS3Key = field("statusReportS3Key")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetImportFileTaskResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetImportFileTaskResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLatestAssessmentIdResponse:
    boto3_raw_data: "type_defs.GetLatestAssessmentIdResponseTypeDef" = (
        dataclasses.field()
    )

    id = field("id")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetLatestAssessmentIdResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLatestAssessmentIdResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAnalyzableServersResponse:
    boto3_raw_data: "type_defs.ListAnalyzableServersResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def analyzableServers(self):  # pragma: no cover
        return AnalyzableServerSummary.make_many(
            self.boto3_raw_data["analyzableServers"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAnalyzableServersResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAnalyzableServersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartAssessmentResponse:
    boto3_raw_data: "type_defs.StartAssessmentResponseTypeDef" = dataclasses.field()

    assessmentId = field("assessmentId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartAssessmentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartAssessmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartImportFileTaskResponse:
    boto3_raw_data: "type_defs.StartImportFileTaskResponseTypeDef" = dataclasses.field()

    id = field("id")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartImportFileTaskResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartImportFileTaskResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartRecommendationReportGenerationResponse:
    boto3_raw_data: "type_defs.StartRecommendationReportGenerationResponseTypeDef" = (
        dataclasses.field()
    )

    id = field("id")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartRecommendationReportGenerationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartRecommendationReportGenerationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRecommendationReportDetailsResponse:
    boto3_raw_data: "type_defs.GetRecommendationReportDetailsResponseTypeDef" = (
        dataclasses.field()
    )

    id = field("id")

    @cached_property
    def recommendationReportDetails(self):  # pragma: no cover
        return RecommendationReportDetails.make_one(
            self.boto3_raw_data["recommendationReportDetails"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetRecommendationReportDetailsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRecommendationReportDetailsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServerDetailsRequestPaginate:
    boto3_raw_data: "type_defs.GetServerDetailsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    serverId = field("serverId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetServerDetailsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServerDetailsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAnalyzableServersRequestPaginate:
    boto3_raw_data: "type_defs.ListAnalyzableServersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    sort = field("sort")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAnalyzableServersRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAnalyzableServersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCollectorsRequestPaginate:
    boto3_raw_data: "type_defs.ListCollectorsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListCollectorsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCollectorsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImportFileTaskRequestPaginate:
    boto3_raw_data: "type_defs.ListImportFileTaskRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListImportFileTaskRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImportFileTaskRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationComponentsRequestPaginate:
    boto3_raw_data: "type_defs.ListApplicationComponentsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    applicationComponentCriteria = field("applicationComponentCriteria")
    filterValue = field("filterValue")

    @cached_property
    def groupIdFilter(self):  # pragma: no cover
        return Group.make_many(self.boto3_raw_data["groupIdFilter"])

    sort = field("sort")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListApplicationComponentsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationComponentsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationComponentsRequest:
    boto3_raw_data: "type_defs.ListApplicationComponentsRequestTypeDef" = (
        dataclasses.field()
    )

    applicationComponentCriteria = field("applicationComponentCriteria")
    filterValue = field("filterValue")

    @cached_property
    def groupIdFilter(self):  # pragma: no cover
        return Group.make_many(self.boto3_raw_data["groupIdFilter"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")
    sort = field("sort")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListApplicationComponentsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationComponentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServersRequestPaginate:
    boto3_raw_data: "type_defs.ListServersRequestPaginateTypeDef" = dataclasses.field()

    filterValue = field("filterValue")

    @cached_property
    def groupIdFilter(self):  # pragma: no cover
        return Group.make_many(self.boto3_raw_data["groupIdFilter"])

    serverCriteria = field("serverCriteria")
    sort = field("sort")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListServersRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServersRequest:
    boto3_raw_data: "type_defs.ListServersRequestTypeDef" = dataclasses.field()

    filterValue = field("filterValue")

    @cached_property
    def groupIdFilter(self):  # pragma: no cover
        return Group.make_many(self.boto3_raw_data["groupIdFilter"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")
    serverCriteria = field("serverCriteria")
    sort = field("sort")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListServersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartImportFileTaskRequest:
    boto3_raw_data: "type_defs.StartImportFileTaskRequestTypeDef" = dataclasses.field()

    S3Bucket = field("S3Bucket")
    name = field("name")
    s3key = field("s3key")
    dataSourceType = field("dataSourceType")

    @cached_property
    def groupId(self):  # pragma: no cover
        return Group.make_many(self.boto3_raw_data["groupId"])

    s3bucketForReportData = field("s3bucketForReportData")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartImportFileTaskRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartImportFileTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartRecommendationReportGenerationRequest:
    boto3_raw_data: "type_defs.StartRecommendationReportGenerationRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def groupIdFilter(self):  # pragma: no cover
        return Group.make_many(self.boto3_raw_data["groupIdFilter"])

    outputFormat = field("outputFormat")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartRecommendationReportGenerationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartRecommendationReportGenerationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImportFileTaskResponse:
    boto3_raw_data: "type_defs.ListImportFileTaskResponseTypeDef" = dataclasses.field()

    @cached_property
    def taskInfos(self):  # pragma: no cover
        return ImportFileTaskInformation.make_many(self.boto3_raw_data["taskInfos"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListImportFileTaskResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImportFileTaskResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManagementPreferenceOutput:
    boto3_raw_data: "type_defs.ManagementPreferenceOutputTypeDef" = dataclasses.field()

    @cached_property
    def awsManagedResources(self):  # pragma: no cover
        return AwsManagedResourcesOutput.make_one(
            self.boto3_raw_data["awsManagedResources"]
        )

    @cached_property
    def noPreference(self):  # pragma: no cover
        return NoManagementPreferenceOutput.make_one(
            self.boto3_raw_data["noPreference"]
        )

    @cached_property
    def selfManageResources(self):  # pragma: no cover
        return SelfManageResourcesOutput.make_one(
            self.boto3_raw_data["selfManageResources"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ManagementPreferenceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManagementPreferenceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManagementPreference:
    boto3_raw_data: "type_defs.ManagementPreferenceTypeDef" = dataclasses.field()

    @cached_property
    def awsManagedResources(self):  # pragma: no cover
        return AwsManagedResources.make_one(self.boto3_raw_data["awsManagedResources"])

    @cached_property
    def noPreference(self):  # pragma: no cover
        return NoManagementPreference.make_one(self.boto3_raw_data["noPreference"])

    @cached_property
    def selfManageResources(self):  # pragma: no cover
        return SelfManageResources.make_one(self.boto3_raw_data["selfManageResources"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ManagementPreferenceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManagementPreferenceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SystemInfo:
    boto3_raw_data: "type_defs.SystemInfoTypeDef" = dataclasses.field()

    cpuArchitecture = field("cpuArchitecture")
    fileSystemType = field("fileSystemType")

    @cached_property
    def networkInfoList(self):  # pragma: no cover
        return NetworkInfo.make_many(self.boto3_raw_data["networkInfoList"])

    @cached_property
    def osInfo(self):  # pragma: no cover
        return OSInfo.make_one(self.boto3_raw_data["osInfo"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SystemInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SystemInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecommendationSet:
    boto3_raw_data: "type_defs.RecommendationSetTypeDef" = dataclasses.field()

    strategy = field("strategy")
    targetDestination = field("targetDestination")

    @cached_property
    def transformationTool(self):  # pragma: no cover
        return TransformationTool.make_one(self.boto3_raw_data["transformationTool"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecommendationSetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecommendationSetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateApplicationComponentConfigRequest:
    boto3_raw_data: "type_defs.UpdateApplicationComponentConfigRequestTypeDef" = (
        dataclasses.field()
    )

    applicationComponentId = field("applicationComponentId")
    appType = field("appType")
    configureOnly = field("configureOnly")
    inclusionStatus = field("inclusionStatus")
    secretsManagerKey = field("secretsManagerKey")

    @cached_property
    def sourceCodeList(self):  # pragma: no cover
        return SourceCode.make_many(self.boto3_raw_data["sourceCodeList"])

    @cached_property
    def strategyOption(self):  # pragma: no cover
        return StrategyOption.make_one(self.boto3_raw_data["strategyOption"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateApplicationComponentConfigRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateApplicationComponentConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateServerConfigRequest:
    boto3_raw_data: "type_defs.UpdateServerConfigRequestTypeDef" = dataclasses.field()

    serverId = field("serverId")

    @cached_property
    def strategyOption(self):  # pragma: no cover
        return StrategyOption.make_one(self.boto3_raw_data["strategyOption"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateServerConfigRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateServerConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Result:
    boto3_raw_data: "type_defs.ResultTypeDef" = dataclasses.field()

    @cached_property
    def analysisStatus(self):  # pragma: no cover
        return AnalysisStatusUnion.make_one(self.boto3_raw_data["analysisStatus"])

    analysisType = field("analysisType")

    @cached_property
    def antipatternReportResultList(self):  # pragma: no cover
        return AntipatternReportResult.make_many(
            self.boto3_raw_data["antipatternReportResultList"]
        )

    statusMessage = field("statusMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResultTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPortfolioSummaryResponse:
    boto3_raw_data: "type_defs.GetPortfolioSummaryResponseTypeDef" = dataclasses.field()

    @cached_property
    def assessmentSummary(self):  # pragma: no cover
        return AssessmentSummary.make_one(self.boto3_raw_data["assessmentSummary"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPortfolioSummaryResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPortfolioSummaryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartAssessmentRequest:
    boto3_raw_data: "type_defs.StartAssessmentRequestTypeDef" = dataclasses.field()

    assessmentDataSourceType = field("assessmentDataSourceType")
    assessmentTargets = field("assessmentTargets")
    s3bucketForAnalysisData = field("s3bucketForAnalysisData")
    s3bucketForReportData = field("s3bucketForReportData")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartAssessmentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartAssessmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Collector:
    boto3_raw_data: "type_defs.CollectorTypeDef" = dataclasses.field()

    collectorHealth = field("collectorHealth")
    collectorId = field("collectorId")
    collectorVersion = field("collectorVersion")

    @cached_property
    def configurationSummary(self):  # pragma: no cover
        return ConfigurationSummary.make_one(
            self.boto3_raw_data["configurationSummary"]
        )

    hostName = field("hostName")
    ipAddress = field("ipAddress")
    lastActivityTimeStamp = field("lastActivityTimeStamp")
    registeredTimeStamp = field("registeredTimeStamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CollectorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CollectorTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatabasePreferencesOutput:
    boto3_raw_data: "type_defs.DatabasePreferencesOutputTypeDef" = dataclasses.field()

    databaseManagementPreference = field("databaseManagementPreference")

    @cached_property
    def databaseMigrationPreference(self):  # pragma: no cover
        return DatabaseMigrationPreferenceOutput.make_one(
            self.boto3_raw_data["databaseMigrationPreference"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DatabasePreferencesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatabasePreferencesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatabasePreferences:
    boto3_raw_data: "type_defs.DatabasePreferencesTypeDef" = dataclasses.field()

    databaseManagementPreference = field("databaseManagementPreference")

    @cached_property
    def databaseMigrationPreference(self):  # pragma: no cover
        return DatabaseMigrationPreference.make_one(
            self.boto3_raw_data["databaseMigrationPreference"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DatabasePreferencesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatabasePreferencesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationPreferencesOutput:
    boto3_raw_data: "type_defs.ApplicationPreferencesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def managementPreference(self):  # pragma: no cover
        return ManagementPreferenceOutput.make_one(
            self.boto3_raw_data["managementPreference"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApplicationPreferencesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationPreferencesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationPreferences:
    boto3_raw_data: "type_defs.ApplicationPreferencesTypeDef" = dataclasses.field()

    @cached_property
    def managementPreference(self):  # pragma: no cover
        return ManagementPreference.make_one(
            self.boto3_raw_data["managementPreference"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApplicationPreferencesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationPreferencesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationComponentStrategy:
    boto3_raw_data: "type_defs.ApplicationComponentStrategyTypeDef" = (
        dataclasses.field()
    )

    isPreferred = field("isPreferred")

    @cached_property
    def recommendation(self):  # pragma: no cover
        return RecommendationSet.make_one(self.boto3_raw_data["recommendation"])

    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApplicationComponentStrategyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationComponentStrategyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServerDetail:
    boto3_raw_data: "type_defs.ServerDetailTypeDef" = dataclasses.field()

    @cached_property
    def antipatternReportS3Object(self):  # pragma: no cover
        return S3Object.make_one(self.boto3_raw_data["antipatternReportS3Object"])

    antipatternReportStatus = field("antipatternReportStatus")
    antipatternReportStatusMessage = field("antipatternReportStatusMessage")

    @cached_property
    def applicationComponentStrategySummary(self):  # pragma: no cover
        return StrategySummary.make_many(
            self.boto3_raw_data["applicationComponentStrategySummary"]
        )

    dataCollectionStatus = field("dataCollectionStatus")
    id = field("id")
    lastAnalyzedTimestamp = field("lastAnalyzedTimestamp")

    @cached_property
    def listAntipatternSeveritySummary(self):  # pragma: no cover
        return AntipatternSeveritySummary.make_many(
            self.boto3_raw_data["listAntipatternSeveritySummary"]
        )

    name = field("name")

    @cached_property
    def recommendationSet(self):  # pragma: no cover
        return RecommendationSet.make_one(self.boto3_raw_data["recommendationSet"])

    @cached_property
    def serverError(self):  # pragma: no cover
        return ServerError.make_one(self.boto3_raw_data["serverError"])

    serverType = field("serverType")
    statusMessage = field("statusMessage")

    @cached_property
    def systemInfo(self):  # pragma: no cover
        return SystemInfo.make_one(self.boto3_raw_data["systemInfo"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServerDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ServerDetailTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServerStrategy:
    boto3_raw_data: "type_defs.ServerStrategyTypeDef" = dataclasses.field()

    isPreferred = field("isPreferred")
    numberOfApplicationComponents = field("numberOfApplicationComponents")

    @cached_property
    def recommendation(self):  # pragma: no cover
        return RecommendationSet.make_one(self.boto3_raw_data["recommendation"])

    status = field("status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServerStrategyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ServerStrategyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationComponentDetail:
    boto3_raw_data: "type_defs.ApplicationComponentDetailTypeDef" = dataclasses.field()

    analysisStatus = field("analysisStatus")

    @cached_property
    def antipatternReportS3Object(self):  # pragma: no cover
        return S3Object.make_one(self.boto3_raw_data["antipatternReportS3Object"])

    antipatternReportStatus = field("antipatternReportStatus")
    antipatternReportStatusMessage = field("antipatternReportStatusMessage")
    appType = field("appType")

    @cached_property
    def appUnitError(self):  # pragma: no cover
        return AppUnitError.make_one(self.boto3_raw_data["appUnitError"])

    associatedServerId = field("associatedServerId")

    @cached_property
    def databaseConfigDetail(self):  # pragma: no cover
        return DatabaseConfigDetail.make_one(
            self.boto3_raw_data["databaseConfigDetail"]
        )

    id = field("id")
    inclusionStatus = field("inclusionStatus")
    lastAnalyzedTimestamp = field("lastAnalyzedTimestamp")

    @cached_property
    def listAntipatternSeveritySummary(self):  # pragma: no cover
        return AntipatternSeveritySummary.make_many(
            self.boto3_raw_data["listAntipatternSeveritySummary"]
        )

    moreServerAssociationExists = field("moreServerAssociationExists")
    name = field("name")
    osDriver = field("osDriver")
    osVersion = field("osVersion")

    @cached_property
    def recommendationSet(self):  # pragma: no cover
        return RecommendationSet.make_one(self.boto3_raw_data["recommendationSet"])

    resourceSubType = field("resourceSubType")

    @cached_property
    def resultList(self):  # pragma: no cover
        return Result.make_many(self.boto3_raw_data["resultList"])

    runtimeStatus = field("runtimeStatus")
    runtimeStatusMessage = field("runtimeStatusMessage")

    @cached_property
    def sourceCodeRepositories(self):  # pragma: no cover
        return SourceCodeRepository.make_many(
            self.boto3_raw_data["sourceCodeRepositories"]
        )

    statusMessage = field("statusMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApplicationComponentDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationComponentDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCollectorsResponse:
    boto3_raw_data: "type_defs.ListCollectorsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Collectors(self):  # pragma: no cover
        return Collector.make_many(self.boto3_raw_data["Collectors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCollectorsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCollectorsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPortfolioPreferencesResponse:
    boto3_raw_data: "type_defs.GetPortfolioPreferencesResponseTypeDef" = (
        dataclasses.field()
    )

    applicationMode = field("applicationMode")

    @cached_property
    def applicationPreferences(self):  # pragma: no cover
        return ApplicationPreferencesOutput.make_one(
            self.boto3_raw_data["applicationPreferences"]
        )

    @cached_property
    def databasePreferences(self):  # pragma: no cover
        return DatabasePreferencesOutput.make_one(
            self.boto3_raw_data["databasePreferences"]
        )

    @cached_property
    def prioritizeBusinessGoals(self):  # pragma: no cover
        return PrioritizeBusinessGoals.make_one(
            self.boto3_raw_data["prioritizeBusinessGoals"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetPortfolioPreferencesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPortfolioPreferencesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApplicationComponentStrategiesResponse:
    boto3_raw_data: "type_defs.GetApplicationComponentStrategiesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def applicationComponentStrategies(self):  # pragma: no cover
        return ApplicationComponentStrategy.make_many(
            self.boto3_raw_data["applicationComponentStrategies"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetApplicationComponentStrategiesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApplicationComponentStrategiesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServerDetailsResponse:
    boto3_raw_data: "type_defs.GetServerDetailsResponseTypeDef" = dataclasses.field()

    @cached_property
    def associatedApplications(self):  # pragma: no cover
        return AssociatedApplication.make_many(
            self.boto3_raw_data["associatedApplications"]
        )

    @cached_property
    def serverDetail(self):  # pragma: no cover
        return ServerDetail.make_one(self.boto3_raw_data["serverDetail"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetServerDetailsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServerDetailsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServersResponse:
    boto3_raw_data: "type_defs.ListServersResponseTypeDef" = dataclasses.field()

    @cached_property
    def serverInfos(self):  # pragma: no cover
        return ServerDetail.make_many(self.boto3_raw_data["serverInfos"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListServersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServerStrategiesResponse:
    boto3_raw_data: "type_defs.GetServerStrategiesResponseTypeDef" = dataclasses.field()

    @cached_property
    def serverStrategies(self):  # pragma: no cover
        return ServerStrategy.make_many(self.boto3_raw_data["serverStrategies"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetServerStrategiesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServerStrategiesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApplicationComponentDetailsResponse:
    boto3_raw_data: "type_defs.GetApplicationComponentDetailsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def applicationComponentDetail(self):  # pragma: no cover
        return ApplicationComponentDetail.make_one(
            self.boto3_raw_data["applicationComponentDetail"]
        )

    @cached_property
    def associatedApplications(self):  # pragma: no cover
        return AssociatedApplication.make_many(
            self.boto3_raw_data["associatedApplications"]
        )

    associatedServerIds = field("associatedServerIds")
    moreApplicationResource = field("moreApplicationResource")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetApplicationComponentDetailsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApplicationComponentDetailsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationComponentsResponse:
    boto3_raw_data: "type_defs.ListApplicationComponentsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def applicationComponentInfos(self):  # pragma: no cover
        return ApplicationComponentDetail.make_many(
            self.boto3_raw_data["applicationComponentInfos"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListApplicationComponentsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationComponentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutPortfolioPreferencesRequest:
    boto3_raw_data: "type_defs.PutPortfolioPreferencesRequestTypeDef" = (
        dataclasses.field()
    )

    applicationMode = field("applicationMode")
    applicationPreferences = field("applicationPreferences")
    databasePreferences = field("databasePreferences")

    @cached_property
    def prioritizeBusinessGoals(self):  # pragma: no cover
        return PrioritizeBusinessGoals.make_one(
            self.boto3_raw_data["prioritizeBusinessGoals"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutPortfolioPreferencesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutPortfolioPreferencesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]

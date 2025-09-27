# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_iot import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AbortCriteria:
    boto3_raw_data: "type_defs.AbortCriteriaTypeDef" = dataclasses.field()

    failureType = field("failureType")
    action = field("action")
    thresholdPercentage = field("thresholdPercentage")
    minNumberOfExecutedThings = field("minNumberOfExecutedThings")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AbortCriteriaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AbortCriteriaTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AcceptCertificateTransferRequest:
    boto3_raw_data: "type_defs.AcceptCertificateTransferRequestTypeDef" = (
        dataclasses.field()
    )

    certificateId = field("certificateId")
    setAsActive = field("setAsActive")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AcceptCertificateTransferRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AcceptCertificateTransferRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudwatchAlarmAction:
    boto3_raw_data: "type_defs.CloudwatchAlarmActionTypeDef" = dataclasses.field()

    roleArn = field("roleArn")
    alarmName = field("alarmName")
    stateReason = field("stateReason")
    stateValue = field("stateValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CloudwatchAlarmActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudwatchAlarmActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudwatchLogsAction:
    boto3_raw_data: "type_defs.CloudwatchLogsActionTypeDef" = dataclasses.field()

    roleArn = field("roleArn")
    logGroupName = field("logGroupName")
    batchMode = field("batchMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CloudwatchLogsActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudwatchLogsActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudwatchMetricAction:
    boto3_raw_data: "type_defs.CloudwatchMetricActionTypeDef" = dataclasses.field()

    roleArn = field("roleArn")
    metricNamespace = field("metricNamespace")
    metricName = field("metricName")
    metricValue = field("metricValue")
    metricUnit = field("metricUnit")
    metricTimestamp = field("metricTimestamp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CloudwatchMetricActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudwatchMetricActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DynamoDBAction:
    boto3_raw_data: "type_defs.DynamoDBActionTypeDef" = dataclasses.field()

    tableName = field("tableName")
    roleArn = field("roleArn")
    hashKeyField = field("hashKeyField")
    hashKeyValue = field("hashKeyValue")
    operation = field("operation")
    hashKeyType = field("hashKeyType")
    rangeKeyField = field("rangeKeyField")
    rangeKeyValue = field("rangeKeyValue")
    rangeKeyType = field("rangeKeyType")
    payloadField = field("payloadField")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DynamoDBActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DynamoDBActionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ElasticsearchAction:
    boto3_raw_data: "type_defs.ElasticsearchActionTypeDef" = dataclasses.field()

    roleArn = field("roleArn")
    endpoint = field("endpoint")
    index = field("index")
    type = field("type")
    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ElasticsearchActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ElasticsearchActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FirehoseAction:
    boto3_raw_data: "type_defs.FirehoseActionTypeDef" = dataclasses.field()

    roleArn = field("roleArn")
    deliveryStreamName = field("deliveryStreamName")
    separator = field("separator")
    batchMode = field("batchMode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FirehoseActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FirehoseActionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IotAnalyticsAction:
    boto3_raw_data: "type_defs.IotAnalyticsActionTypeDef" = dataclasses.field()

    channelArn = field("channelArn")
    channelName = field("channelName")
    batchMode = field("batchMode")
    roleArn = field("roleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IotAnalyticsActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IotAnalyticsActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IotEventsAction:
    boto3_raw_data: "type_defs.IotEventsActionTypeDef" = dataclasses.field()

    inputName = field("inputName")
    roleArn = field("roleArn")
    messageId = field("messageId")
    batchMode = field("batchMode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IotEventsActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IotEventsActionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KinesisAction:
    boto3_raw_data: "type_defs.KinesisActionTypeDef" = dataclasses.field()

    roleArn = field("roleArn")
    streamName = field("streamName")
    partitionKey = field("partitionKey")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KinesisActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.KinesisActionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaAction:
    boto3_raw_data: "type_defs.LambdaActionTypeDef" = dataclasses.field()

    functionArn = field("functionArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LambdaActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LambdaActionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenSearchAction:
    boto3_raw_data: "type_defs.OpenSearchActionTypeDef" = dataclasses.field()

    roleArn = field("roleArn")
    endpoint = field("endpoint")
    index = field("index")
    type = field("type")
    id = field("id")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OpenSearchActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpenSearchActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Action:
    boto3_raw_data: "type_defs.S3ActionTypeDef" = dataclasses.field()

    roleArn = field("roleArn")
    bucketName = field("bucketName")
    key = field("key")
    cannedAcl = field("cannedAcl")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3ActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3ActionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SalesforceAction:
    boto3_raw_data: "type_defs.SalesforceActionTypeDef" = dataclasses.field()

    token = field("token")
    url = field("url")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SalesforceActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SalesforceActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SnsAction:
    boto3_raw_data: "type_defs.SnsActionTypeDef" = dataclasses.field()

    targetArn = field("targetArn")
    roleArn = field("roleArn")
    messageFormat = field("messageFormat")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SnsActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SnsActionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SqsAction:
    boto3_raw_data: "type_defs.SqsActionTypeDef" = dataclasses.field()

    roleArn = field("roleArn")
    queueUrl = field("queueUrl")
    useBase64 = field("useBase64")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SqsActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SqsActionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StepFunctionsAction:
    boto3_raw_data: "type_defs.StepFunctionsActionTypeDef" = dataclasses.field()

    stateMachineName = field("stateMachineName")
    roleArn = field("roleArn")
    executionNamePrefix = field("executionNamePrefix")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StepFunctionsActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StepFunctionsActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricValueOutput:
    boto3_raw_data: "type_defs.MetricValueOutputTypeDef" = dataclasses.field()

    count = field("count")
    cidrs = field("cidrs")
    ports = field("ports")
    number = field("number")
    numbers = field("numbers")
    strings = field("strings")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricValueOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetricValueOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ViolationEventAdditionalInfo:
    boto3_raw_data: "type_defs.ViolationEventAdditionalInfoTypeDef" = (
        dataclasses.field()
    )

    confidenceLevel = field("confidenceLevel")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ViolationEventAdditionalInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ViolationEventAdditionalInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddThingToBillingGroupRequest:
    boto3_raw_data: "type_defs.AddThingToBillingGroupRequestTypeDef" = (
        dataclasses.field()
    )

    billingGroupName = field("billingGroupName")
    billingGroupArn = field("billingGroupArn")
    thingName = field("thingName")
    thingArn = field("thingArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AddThingToBillingGroupRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddThingToBillingGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddThingToThingGroupRequest:
    boto3_raw_data: "type_defs.AddThingToThingGroupRequestTypeDef" = dataclasses.field()

    thingGroupName = field("thingGroupName")
    thingGroupArn = field("thingGroupArn")
    thingName = field("thingName")
    thingArn = field("thingArn")
    overrideDynamicGroups = field("overrideDynamicGroups")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddThingToThingGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddThingToThingGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddThingsToThingGroupParamsOutput:
    boto3_raw_data: "type_defs.AddThingsToThingGroupParamsOutputTypeDef" = (
        dataclasses.field()
    )

    thingGroupNames = field("thingGroupNames")
    overrideDynamicGroups = field("overrideDynamicGroups")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AddThingsToThingGroupParamsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddThingsToThingGroupParamsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddThingsToThingGroupParams:
    boto3_raw_data: "type_defs.AddThingsToThingGroupParamsTypeDef" = dataclasses.field()

    thingGroupNames = field("thingGroupNames")
    overrideDynamicGroups = field("overrideDynamicGroups")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddThingsToThingGroupParamsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddThingsToThingGroupParamsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AggregationTypeOutput:
    boto3_raw_data: "type_defs.AggregationTypeOutputTypeDef" = dataclasses.field()

    name = field("name")
    values = field("values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AggregationTypeOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AggregationTypeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AggregationType:
    boto3_raw_data: "type_defs.AggregationTypeTypeDef" = dataclasses.field()

    name = field("name")
    values = field("values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AggregationTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AggregationTypeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AlertTarget:
    boto3_raw_data: "type_defs.AlertTargetTypeDef" = dataclasses.field()

    alertTargetArn = field("alertTargetArn")
    roleArn = field("roleArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AlertTargetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AlertTargetTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Policy:
    boto3_raw_data: "type_defs.PolicyTypeDef" = dataclasses.field()

    policyName = field("policyName")
    policyArn = field("policyArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PolicyTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetPropertyTimestamp:
    boto3_raw_data: "type_defs.AssetPropertyTimestampTypeDef" = dataclasses.field()

    timeInSeconds = field("timeInSeconds")
    offsetInNanos = field("offsetInNanos")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssetPropertyTimestampTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssetPropertyTimestampTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetPropertyVariant:
    boto3_raw_data: "type_defs.AssetPropertyVariantTypeDef" = dataclasses.field()

    stringValue = field("stringValue")
    integerValue = field("integerValue")
    doubleValue = field("doubleValue")
    booleanValue = field("booleanValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssetPropertyVariantTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssetPropertyVariantTypeDef"]
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
class AssociateTargetsWithJobRequest:
    boto3_raw_data: "type_defs.AssociateTargetsWithJobRequestTypeDef" = (
        dataclasses.field()
    )

    targets = field("targets")
    jobId = field("jobId")
    comment = field("comment")
    namespaceId = field("namespaceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssociateTargetsWithJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateTargetsWithJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachPolicyRequest:
    boto3_raw_data: "type_defs.AttachPolicyRequestTypeDef" = dataclasses.field()

    policyName = field("policyName")
    target = field("target")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttachPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttachPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachPrincipalPolicyRequest:
    boto3_raw_data: "type_defs.AttachPrincipalPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    policyName = field("policyName")
    principal = field("principal")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttachPrincipalPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttachPrincipalPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachSecurityProfileRequest:
    boto3_raw_data: "type_defs.AttachSecurityProfileRequestTypeDef" = (
        dataclasses.field()
    )

    securityProfileName = field("securityProfileName")
    securityProfileTargetArn = field("securityProfileTargetArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttachSecurityProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttachSecurityProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachThingPrincipalRequest:
    boto3_raw_data: "type_defs.AttachThingPrincipalRequestTypeDef" = dataclasses.field()

    thingName = field("thingName")
    principal = field("principal")
    thingPrincipalType = field("thingPrincipalType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttachThingPrincipalRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttachThingPrincipalRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttributePayloadOutput:
    boto3_raw_data: "type_defs.AttributePayloadOutputTypeDef" = dataclasses.field()

    attributes = field("attributes")
    merge = field("merge")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttributePayloadOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttributePayloadOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttributePayload:
    boto3_raw_data: "type_defs.AttributePayloadTypeDef" = dataclasses.field()

    attributes = field("attributes")
    merge = field("merge")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AttributePayloadTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttributePayloadTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuditCheckConfigurationOutput:
    boto3_raw_data: "type_defs.AuditCheckConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    enabled = field("enabled")
    configuration = field("configuration")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AuditCheckConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuditCheckConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuditCheckConfiguration:
    boto3_raw_data: "type_defs.AuditCheckConfigurationTypeDef" = dataclasses.field()

    enabled = field("enabled")
    configuration = field("configuration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AuditCheckConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuditCheckConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuditCheckDetails:
    boto3_raw_data: "type_defs.AuditCheckDetailsTypeDef" = dataclasses.field()

    checkRunStatus = field("checkRunStatus")
    checkCompliant = field("checkCompliant")
    totalResourcesCount = field("totalResourcesCount")
    nonCompliantResourcesCount = field("nonCompliantResourcesCount")
    suppressedNonCompliantResourcesCount = field("suppressedNonCompliantResourcesCount")
    errorCode = field("errorCode")
    message = field("message")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AuditCheckDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuditCheckDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuditMitigationActionExecutionMetadata:
    boto3_raw_data: "type_defs.AuditMitigationActionExecutionMetadataTypeDef" = (
        dataclasses.field()
    )

    taskId = field("taskId")
    findingId = field("findingId")
    actionName = field("actionName")
    actionId = field("actionId")
    status = field("status")
    startTime = field("startTime")
    endTime = field("endTime")
    errorCode = field("errorCode")
    message = field("message")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AuditMitigationActionExecutionMetadataTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuditMitigationActionExecutionMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuditMitigationActionsTaskMetadata:
    boto3_raw_data: "type_defs.AuditMitigationActionsTaskMetadataTypeDef" = (
        dataclasses.field()
    )

    taskId = field("taskId")
    startTime = field("startTime")
    taskStatus = field("taskStatus")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AuditMitigationActionsTaskMetadataTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuditMitigationActionsTaskMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuditMitigationActionsTaskTargetOutput:
    boto3_raw_data: "type_defs.AuditMitigationActionsTaskTargetOutputTypeDef" = (
        dataclasses.field()
    )

    auditTaskId = field("auditTaskId")
    findingIds = field("findingIds")
    auditCheckToReasonCodeFilter = field("auditCheckToReasonCodeFilter")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AuditMitigationActionsTaskTargetOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuditMitigationActionsTaskTargetOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuditMitigationActionsTaskTarget:
    boto3_raw_data: "type_defs.AuditMitigationActionsTaskTargetTypeDef" = (
        dataclasses.field()
    )

    auditTaskId = field("auditTaskId")
    findingIds = field("findingIds")
    auditCheckToReasonCodeFilter = field("auditCheckToReasonCodeFilter")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AuditMitigationActionsTaskTargetTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuditMitigationActionsTaskTargetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuditNotificationTarget:
    boto3_raw_data: "type_defs.AuditNotificationTargetTypeDef" = dataclasses.field()

    targetArn = field("targetArn")
    roleArn = field("roleArn")
    enabled = field("enabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AuditNotificationTargetTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuditNotificationTargetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuditTaskMetadata:
    boto3_raw_data: "type_defs.AuditTaskMetadataTypeDef" = dataclasses.field()

    taskId = field("taskId")
    taskStatus = field("taskStatus")
    taskType = field("taskType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AuditTaskMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuditTaskMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthInfoOutput:
    boto3_raw_data: "type_defs.AuthInfoOutputTypeDef" = dataclasses.field()

    resources = field("resources")
    actionType = field("actionType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AuthInfoOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AuthInfoOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthInfo:
    boto3_raw_data: "type_defs.AuthInfoTypeDef" = dataclasses.field()

    resources = field("resources")
    actionType = field("actionType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AuthInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AuthInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthorizerConfig:
    boto3_raw_data: "type_defs.AuthorizerConfigTypeDef" = dataclasses.field()

    defaultAuthorizerName = field("defaultAuthorizerName")
    allowAuthorizerOverride = field("allowAuthorizerOverride")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AuthorizerConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthorizerConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthorizerDescription:
    boto3_raw_data: "type_defs.AuthorizerDescriptionTypeDef" = dataclasses.field()

    authorizerName = field("authorizerName")
    authorizerArn = field("authorizerArn")
    authorizerFunctionArn = field("authorizerFunctionArn")
    tokenKeyName = field("tokenKeyName")
    tokenSigningPublicKeys = field("tokenSigningPublicKeys")
    status = field("status")
    creationDate = field("creationDate")
    lastModifiedDate = field("lastModifiedDate")
    signingDisabled = field("signingDisabled")
    enableCachingForHttp = field("enableCachingForHttp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AuthorizerDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthorizerDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthorizerSummary:
    boto3_raw_data: "type_defs.AuthorizerSummaryTypeDef" = dataclasses.field()

    authorizerName = field("authorizerName")
    authorizerArn = field("authorizerArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AuthorizerSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthorizerSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AwsJobAbortCriteria:
    boto3_raw_data: "type_defs.AwsJobAbortCriteriaTypeDef" = dataclasses.field()

    failureType = field("failureType")
    action = field("action")
    thresholdPercentage = field("thresholdPercentage")
    minNumberOfExecutedThings = field("minNumberOfExecutedThings")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AwsJobAbortCriteriaTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AwsJobAbortCriteriaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AwsJobRateIncreaseCriteria:
    boto3_raw_data: "type_defs.AwsJobRateIncreaseCriteriaTypeDef" = dataclasses.field()

    numberOfNotifiedThings = field("numberOfNotifiedThings")
    numberOfSucceededThings = field("numberOfSucceededThings")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AwsJobRateIncreaseCriteriaTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AwsJobRateIncreaseCriteriaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AwsJobPresignedUrlConfig:
    boto3_raw_data: "type_defs.AwsJobPresignedUrlConfigTypeDef" = dataclasses.field()

    expiresInSec = field("expiresInSec")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AwsJobPresignedUrlConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AwsJobPresignedUrlConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AwsJobTimeoutConfig:
    boto3_raw_data: "type_defs.AwsJobTimeoutConfigTypeDef" = dataclasses.field()

    inProgressTimeoutInMinutes = field("inProgressTimeoutInMinutes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AwsJobTimeoutConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AwsJobTimeoutConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MachineLearningDetectionConfig:
    boto3_raw_data: "type_defs.MachineLearningDetectionConfigTypeDef" = (
        dataclasses.field()
    )

    confidenceLevel = field("confidenceLevel")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.MachineLearningDetectionConfigTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MachineLearningDetectionConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StatisticalThreshold:
    boto3_raw_data: "type_defs.StatisticalThresholdTypeDef" = dataclasses.field()

    statistic = field("statistic")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StatisticalThresholdTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StatisticalThresholdTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BehaviorModelTrainingSummary:
    boto3_raw_data: "type_defs.BehaviorModelTrainingSummaryTypeDef" = (
        dataclasses.field()
    )

    securityProfileName = field("securityProfileName")
    behaviorName = field("behaviorName")
    trainingDataCollectionStartDate = field("trainingDataCollectionStartDate")
    modelStatus = field("modelStatus")
    datapointsCollectionPercentage = field("datapointsCollectionPercentage")
    lastModelRefreshDate = field("lastModelRefreshDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BehaviorModelTrainingSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BehaviorModelTrainingSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricDimension:
    boto3_raw_data: "type_defs.MetricDimensionTypeDef" = dataclasses.field()

    dimensionName = field("dimensionName")
    operator = field("operator")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricDimensionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetricDimensionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BillingGroupMetadata:
    boto3_raw_data: "type_defs.BillingGroupMetadataTypeDef" = dataclasses.field()

    creationDate = field("creationDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BillingGroupMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BillingGroupMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BillingGroupProperties:
    boto3_raw_data: "type_defs.BillingGroupPropertiesTypeDef" = dataclasses.field()

    billingGroupDescription = field("billingGroupDescription")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BillingGroupPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BillingGroupPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Bucket:
    boto3_raw_data: "type_defs.BucketTypeDef" = dataclasses.field()

    keyValue = field("keyValue")
    count = field("count")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BucketTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BucketTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TermsAggregation:
    boto3_raw_data: "type_defs.TermsAggregationTypeDef" = dataclasses.field()

    maxBuckets = field("maxBuckets")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TermsAggregationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TermsAggregationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CertificateValidity:
    boto3_raw_data: "type_defs.CertificateValidityTypeDef" = dataclasses.field()

    notBefore = field("notBefore")
    notAfter = field("notAfter")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CertificateValidityTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CertificateValidityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CACertificate:
    boto3_raw_data: "type_defs.CACertificateTypeDef" = dataclasses.field()

    certificateArn = field("certificateArn")
    certificateId = field("certificateId")
    status = field("status")
    creationDate = field("creationDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CACertificateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CACertificateTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelAuditMitigationActionsTaskRequest:
    boto3_raw_data: "type_defs.CancelAuditMitigationActionsTaskRequestTypeDef" = (
        dataclasses.field()
    )

    taskId = field("taskId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CancelAuditMitigationActionsTaskRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelAuditMitigationActionsTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelAuditTaskRequest:
    boto3_raw_data: "type_defs.CancelAuditTaskRequestTypeDef" = dataclasses.field()

    taskId = field("taskId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelAuditTaskRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelAuditTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelCertificateTransferRequest:
    boto3_raw_data: "type_defs.CancelCertificateTransferRequestTypeDef" = (
        dataclasses.field()
    )

    certificateId = field("certificateId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CancelCertificateTransferRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelCertificateTransferRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelDetectMitigationActionsTaskRequest:
    boto3_raw_data: "type_defs.CancelDetectMitigationActionsTaskRequestTypeDef" = (
        dataclasses.field()
    )

    taskId = field("taskId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CancelDetectMitigationActionsTaskRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelDetectMitigationActionsTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelJobExecutionRequest:
    boto3_raw_data: "type_defs.CancelJobExecutionRequestTypeDef" = dataclasses.field()

    jobId = field("jobId")
    thingName = field("thingName")
    force = field("force")
    expectedVersion = field("expectedVersion")
    statusDetails = field("statusDetails")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelJobExecutionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelJobExecutionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelJobRequest:
    boto3_raw_data: "type_defs.CancelJobRequestTypeDef" = dataclasses.field()

    jobId = field("jobId")
    reasonCode = field("reasonCode")
    comment = field("comment")
    force = field("force")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CancelJobRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TransferData:
    boto3_raw_data: "type_defs.TransferDataTypeDef" = dataclasses.field()

    transferMessage = field("transferMessage")
    rejectReason = field("rejectReason")
    transferDate = field("transferDate")
    acceptDate = field("acceptDate")
    rejectDate = field("rejectDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TransferDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TransferDataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CertificateProviderSummary:
    boto3_raw_data: "type_defs.CertificateProviderSummaryTypeDef" = dataclasses.field()

    certificateProviderName = field("certificateProviderName")
    certificateProviderArn = field("certificateProviderArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CertificateProviderSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CertificateProviderSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Certificate:
    boto3_raw_data: "type_defs.CertificateTypeDef" = dataclasses.field()

    certificateArn = field("certificateArn")
    certificateId = field("certificateId")
    status = field("status")
    certificateMode = field("certificateMode")
    creationDate = field("creationDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CertificateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CertificateTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClientCertificateConfig:
    boto3_raw_data: "type_defs.ClientCertificateConfigTypeDef" = dataclasses.field()

    clientCertificateCallbackArn = field("clientCertificateCallbackArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClientCertificateConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClientCertificateConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodeSigningCertificateChain:
    boto3_raw_data: "type_defs.CodeSigningCertificateChainTypeDef" = dataclasses.field()

    certificateName = field("certificateName")
    inlineDocument = field("inlineDocument")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CodeSigningCertificateChainTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodeSigningCertificateChainTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodeSigningSignatureOutput:
    boto3_raw_data: "type_defs.CodeSigningSignatureOutputTypeDef" = dataclasses.field()

    inlineDocument = field("inlineDocument")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CodeSigningSignatureOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodeSigningSignatureOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CommandExecutionResult:
    boto3_raw_data: "type_defs.CommandExecutionResultTypeDef" = dataclasses.field()

    S = field("S")
    B = field("B")
    BIN = field("BIN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CommandExecutionResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CommandExecutionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CommandExecutionSummary:
    boto3_raw_data: "type_defs.CommandExecutionSummaryTypeDef" = dataclasses.field()

    commandArn = field("commandArn")
    executionId = field("executionId")
    targetArn = field("targetArn")
    status = field("status")
    createdAt = field("createdAt")
    startedAt = field("startedAt")
    completedAt = field("completedAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CommandExecutionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CommandExecutionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CommandParameterValueOutput:
    boto3_raw_data: "type_defs.CommandParameterValueOutputTypeDef" = dataclasses.field()

    S = field("S")
    B = field("B")
    I = field("I")
    L = field("L")
    D = field("D")
    BIN = field("BIN")
    UL = field("UL")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CommandParameterValueOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CommandParameterValueOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CommandPayloadOutput:
    boto3_raw_data: "type_defs.CommandPayloadOutputTypeDef" = dataclasses.field()

    content = field("content")
    contentType = field("contentType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CommandPayloadOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CommandPayloadOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CommandSummary:
    boto3_raw_data: "type_defs.CommandSummaryTypeDef" = dataclasses.field()

    commandArn = field("commandArn")
    commandId = field("commandId")
    displayName = field("displayName")
    deprecated = field("deprecated")
    createdAt = field("createdAt")
    lastUpdatedAt = field("lastUpdatedAt")
    pendingDeletion = field("pendingDeletion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CommandSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CommandSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigurationDetails:
    boto3_raw_data: "type_defs.ConfigurationDetailsTypeDef" = dataclasses.field()

    configurationStatus = field("configurationStatus")
    errorCode = field("errorCode")
    errorMessage = field("errorMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfigurationDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigurationDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Configuration:
    boto3_raw_data: "type_defs.ConfigurationTypeDef" = dataclasses.field()

    Enabled = field("Enabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConfigurationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfirmTopicRuleDestinationRequest:
    boto3_raw_data: "type_defs.ConfirmTopicRuleDestinationRequestTypeDef" = (
        dataclasses.field()
    )

    confirmationToken = field("confirmationToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConfirmTopicRuleDestinationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfirmTopicRuleDestinationRequestTypeDef"]
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
class CreateCertificateFromCsrRequest:
    boto3_raw_data: "type_defs.CreateCertificateFromCsrRequestTypeDef" = (
        dataclasses.field()
    )

    certificateSigningRequest = field("certificateSigningRequest")
    setAsActive = field("setAsActive")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateCertificateFromCsrRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCertificateFromCsrRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServerCertificateConfig:
    boto3_raw_data: "type_defs.ServerCertificateConfigTypeDef" = dataclasses.field()

    enableOCSPCheck = field("enableOCSPCheck")
    ocspLambdaArn = field("ocspLambdaArn")
    ocspAuthorizedResponderArn = field("ocspAuthorizedResponderArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServerCertificateConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServerCertificateConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TlsConfig:
    boto3_raw_data: "type_defs.TlsConfigTypeDef" = dataclasses.field()

    securityPolicy = field("securityPolicy")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TlsConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TlsConfigTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PresignedUrlConfig:
    boto3_raw_data: "type_defs.PresignedUrlConfigTypeDef" = dataclasses.field()

    roleArn = field("roleArn")
    expiresInSec = field("expiresInSec")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PresignedUrlConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PresignedUrlConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimeoutConfig:
    boto3_raw_data: "type_defs.TimeoutConfigTypeDef" = dataclasses.field()

    inProgressTimeoutInMinutes = field("inProgressTimeoutInMinutes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TimeoutConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TimeoutConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MaintenanceWindow:
    boto3_raw_data: "type_defs.MaintenanceWindowTypeDef" = dataclasses.field()

    startTime = field("startTime")
    durationInMinutes = field("durationInMinutes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MaintenanceWindowTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MaintenanceWindowTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateKeysAndCertificateRequest:
    boto3_raw_data: "type_defs.CreateKeysAndCertificateRequestTypeDef" = (
        dataclasses.field()
    )

    setAsActive = field("setAsActive")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateKeysAndCertificateRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateKeysAndCertificateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KeyPair:
    boto3_raw_data: "type_defs.KeyPairTypeDef" = dataclasses.field()

    PublicKey = field("PublicKey")
    PrivateKey = field("PrivateKey")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KeyPairTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.KeyPairTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePackageRequest:
    boto3_raw_data: "type_defs.CreatePackageRequestTypeDef" = dataclasses.field()

    packageName = field("packageName")
    description = field("description")
    tags = field("tags")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePackageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePackageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePolicyVersionRequest:
    boto3_raw_data: "type_defs.CreatePolicyVersionRequestTypeDef" = dataclasses.field()

    policyName = field("policyName")
    policyDocument = field("policyDocument")
    setAsDefault = field("setAsDefault")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePolicyVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePolicyVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateProvisioningClaimRequest:
    boto3_raw_data: "type_defs.CreateProvisioningClaimRequestTypeDef" = (
        dataclasses.field()
    )

    templateName = field("templateName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateProvisioningClaimRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateProvisioningClaimRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProvisioningHook:
    boto3_raw_data: "type_defs.ProvisioningHookTypeDef" = dataclasses.field()

    targetArn = field("targetArn")
    payloadVersion = field("payloadVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProvisioningHookTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProvisioningHookTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateProvisioningTemplateVersionRequest:
    boto3_raw_data: "type_defs.CreateProvisioningTemplateVersionRequestTypeDef" = (
        dataclasses.field()
    )

    templateName = field("templateName")
    templateBody = field("templateBody")
    setAsDefault = field("setAsDefault")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateProvisioningTemplateVersionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateProvisioningTemplateVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricsExportConfig:
    boto3_raw_data: "type_defs.MetricsExportConfigTypeDef" = dataclasses.field()

    mqttTopic = field("mqttTopic")
    roleArn = field("roleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MetricsExportConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetricsExportConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAccountAuditConfigurationRequest:
    boto3_raw_data: "type_defs.DeleteAccountAuditConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    deleteScheduledAudits = field("deleteScheduledAudits")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteAccountAuditConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAccountAuditConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAuthorizerRequest:
    boto3_raw_data: "type_defs.DeleteAuthorizerRequestTypeDef" = dataclasses.field()

    authorizerName = field("authorizerName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAuthorizerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAuthorizerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBillingGroupRequest:
    boto3_raw_data: "type_defs.DeleteBillingGroupRequestTypeDef" = dataclasses.field()

    billingGroupName = field("billingGroupName")
    expectedVersion = field("expectedVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBillingGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBillingGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCACertificateRequest:
    boto3_raw_data: "type_defs.DeleteCACertificateRequestTypeDef" = dataclasses.field()

    certificateId = field("certificateId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteCACertificateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCACertificateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCertificateProviderRequest:
    boto3_raw_data: "type_defs.DeleteCertificateProviderRequestTypeDef" = (
        dataclasses.field()
    )

    certificateProviderName = field("certificateProviderName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteCertificateProviderRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCertificateProviderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCertificateRequest:
    boto3_raw_data: "type_defs.DeleteCertificateRequestTypeDef" = dataclasses.field()

    certificateId = field("certificateId")
    forceDelete = field("forceDelete")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteCertificateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCertificateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCommandExecutionRequest:
    boto3_raw_data: "type_defs.DeleteCommandExecutionRequestTypeDef" = (
        dataclasses.field()
    )

    executionId = field("executionId")
    targetArn = field("targetArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteCommandExecutionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCommandExecutionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCommandRequest:
    boto3_raw_data: "type_defs.DeleteCommandRequestTypeDef" = dataclasses.field()

    commandId = field("commandId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteCommandRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCommandRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCustomMetricRequest:
    boto3_raw_data: "type_defs.DeleteCustomMetricRequestTypeDef" = dataclasses.field()

    metricName = field("metricName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteCustomMetricRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCustomMetricRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDimensionRequest:
    boto3_raw_data: "type_defs.DeleteDimensionRequestTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDimensionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDimensionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDomainConfigurationRequest:
    boto3_raw_data: "type_defs.DeleteDomainConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    domainConfigurationName = field("domainConfigurationName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteDomainConfigurationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDomainConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDynamicThingGroupRequest:
    boto3_raw_data: "type_defs.DeleteDynamicThingGroupRequestTypeDef" = (
        dataclasses.field()
    )

    thingGroupName = field("thingGroupName")
    expectedVersion = field("expectedVersion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteDynamicThingGroupRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDynamicThingGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFleetMetricRequest:
    boto3_raw_data: "type_defs.DeleteFleetMetricRequestTypeDef" = dataclasses.field()

    metricName = field("metricName")
    expectedVersion = field("expectedVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteFleetMetricRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFleetMetricRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteJobExecutionRequest:
    boto3_raw_data: "type_defs.DeleteJobExecutionRequestTypeDef" = dataclasses.field()

    jobId = field("jobId")
    thingName = field("thingName")
    executionNumber = field("executionNumber")
    force = field("force")
    namespaceId = field("namespaceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteJobExecutionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteJobExecutionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteJobRequest:
    boto3_raw_data: "type_defs.DeleteJobRequestTypeDef" = dataclasses.field()

    jobId = field("jobId")
    force = field("force")
    namespaceId = field("namespaceId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteJobRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteJobTemplateRequest:
    boto3_raw_data: "type_defs.DeleteJobTemplateRequestTypeDef" = dataclasses.field()

    jobTemplateId = field("jobTemplateId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteJobTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteJobTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMitigationActionRequest:
    boto3_raw_data: "type_defs.DeleteMitigationActionRequestTypeDef" = (
        dataclasses.field()
    )

    actionName = field("actionName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteMitigationActionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMitigationActionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteOTAUpdateRequest:
    boto3_raw_data: "type_defs.DeleteOTAUpdateRequestTypeDef" = dataclasses.field()

    otaUpdateId = field("otaUpdateId")
    deleteStream = field("deleteStream")
    forceDeleteAWSJob = field("forceDeleteAWSJob")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteOTAUpdateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteOTAUpdateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePackageRequest:
    boto3_raw_data: "type_defs.DeletePackageRequestTypeDef" = dataclasses.field()

    packageName = field("packageName")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePackageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePackageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePackageVersionRequest:
    boto3_raw_data: "type_defs.DeletePackageVersionRequestTypeDef" = dataclasses.field()

    packageName = field("packageName")
    versionName = field("versionName")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePackageVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePackageVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePolicyRequest:
    boto3_raw_data: "type_defs.DeletePolicyRequestTypeDef" = dataclasses.field()

    policyName = field("policyName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePolicyVersionRequest:
    boto3_raw_data: "type_defs.DeletePolicyVersionRequestTypeDef" = dataclasses.field()

    policyName = field("policyName")
    policyVersionId = field("policyVersionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePolicyVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePolicyVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteProvisioningTemplateRequest:
    boto3_raw_data: "type_defs.DeleteProvisioningTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    templateName = field("templateName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteProvisioningTemplateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteProvisioningTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteProvisioningTemplateVersionRequest:
    boto3_raw_data: "type_defs.DeleteProvisioningTemplateVersionRequestTypeDef" = (
        dataclasses.field()
    )

    templateName = field("templateName")
    versionId = field("versionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteProvisioningTemplateVersionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteProvisioningTemplateVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRoleAliasRequest:
    boto3_raw_data: "type_defs.DeleteRoleAliasRequestTypeDef" = dataclasses.field()

    roleAlias = field("roleAlias")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteRoleAliasRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRoleAliasRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteScheduledAuditRequest:
    boto3_raw_data: "type_defs.DeleteScheduledAuditRequestTypeDef" = dataclasses.field()

    scheduledAuditName = field("scheduledAuditName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteScheduledAuditRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteScheduledAuditRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSecurityProfileRequest:
    boto3_raw_data: "type_defs.DeleteSecurityProfileRequestTypeDef" = (
        dataclasses.field()
    )

    securityProfileName = field("securityProfileName")
    expectedVersion = field("expectedVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSecurityProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSecurityProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteStreamRequest:
    boto3_raw_data: "type_defs.DeleteStreamRequestTypeDef" = dataclasses.field()

    streamId = field("streamId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteStreamRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteStreamRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteThingGroupRequest:
    boto3_raw_data: "type_defs.DeleteThingGroupRequestTypeDef" = dataclasses.field()

    thingGroupName = field("thingGroupName")
    expectedVersion = field("expectedVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteThingGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteThingGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteThingRequest:
    boto3_raw_data: "type_defs.DeleteThingRequestTypeDef" = dataclasses.field()

    thingName = field("thingName")
    expectedVersion = field("expectedVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteThingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteThingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteThingTypeRequest:
    boto3_raw_data: "type_defs.DeleteThingTypeRequestTypeDef" = dataclasses.field()

    thingTypeName = field("thingTypeName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteThingTypeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteThingTypeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTopicRuleDestinationRequest:
    boto3_raw_data: "type_defs.DeleteTopicRuleDestinationRequestTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteTopicRuleDestinationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTopicRuleDestinationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTopicRuleRequest:
    boto3_raw_data: "type_defs.DeleteTopicRuleRequestTypeDef" = dataclasses.field()

    ruleName = field("ruleName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteTopicRuleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTopicRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteV2LoggingLevelRequest:
    boto3_raw_data: "type_defs.DeleteV2LoggingLevelRequestTypeDef" = dataclasses.field()

    targetType = field("targetType")
    targetName = field("targetName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteV2LoggingLevelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteV2LoggingLevelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeprecateThingTypeRequest:
    boto3_raw_data: "type_defs.DeprecateThingTypeRequestTypeDef" = dataclasses.field()

    thingTypeName = field("thingTypeName")
    undoDeprecate = field("undoDeprecate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeprecateThingTypeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeprecateThingTypeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAuditFindingRequest:
    boto3_raw_data: "type_defs.DescribeAuditFindingRequestTypeDef" = dataclasses.field()

    findingId = field("findingId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAuditFindingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAuditFindingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAuditMitigationActionsTaskRequest:
    boto3_raw_data: "type_defs.DescribeAuditMitigationActionsTaskRequestTypeDef" = (
        dataclasses.field()
    )

    taskId = field("taskId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAuditMitigationActionsTaskRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAuditMitigationActionsTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskStatisticsForAuditCheck:
    boto3_raw_data: "type_defs.TaskStatisticsForAuditCheckTypeDef" = dataclasses.field()

    totalFindingsCount = field("totalFindingsCount")
    failedFindingsCount = field("failedFindingsCount")
    succeededFindingsCount = field("succeededFindingsCount")
    skippedFindingsCount = field("skippedFindingsCount")
    canceledFindingsCount = field("canceledFindingsCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TaskStatisticsForAuditCheckTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TaskStatisticsForAuditCheckTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAuditTaskRequest:
    boto3_raw_data: "type_defs.DescribeAuditTaskRequestTypeDef" = dataclasses.field()

    taskId = field("taskId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAuditTaskRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAuditTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskStatistics:
    boto3_raw_data: "type_defs.TaskStatisticsTypeDef" = dataclasses.field()

    totalChecks = field("totalChecks")
    inProgressChecks = field("inProgressChecks")
    waitingForDataCollectionChecks = field("waitingForDataCollectionChecks")
    compliantChecks = field("compliantChecks")
    nonCompliantChecks = field("nonCompliantChecks")
    failedChecks = field("failedChecks")
    canceledChecks = field("canceledChecks")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TaskStatisticsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TaskStatisticsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAuthorizerRequest:
    boto3_raw_data: "type_defs.DescribeAuthorizerRequestTypeDef" = dataclasses.field()

    authorizerName = field("authorizerName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAuthorizerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAuthorizerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBillingGroupRequest:
    boto3_raw_data: "type_defs.DescribeBillingGroupRequestTypeDef" = dataclasses.field()

    billingGroupName = field("billingGroupName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeBillingGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBillingGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCACertificateRequest:
    boto3_raw_data: "type_defs.DescribeCACertificateRequestTypeDef" = (
        dataclasses.field()
    )

    certificateId = field("certificateId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeCACertificateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCACertificateRequestTypeDef"]
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

    templateBody = field("templateBody")
    roleArn = field("roleArn")
    templateName = field("templateName")

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
class DescribeCertificateProviderRequest:
    boto3_raw_data: "type_defs.DescribeCertificateProviderRequestTypeDef" = (
        dataclasses.field()
    )

    certificateProviderName = field("certificateProviderName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeCertificateProviderRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCertificateProviderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCertificateRequest:
    boto3_raw_data: "type_defs.DescribeCertificateRequestTypeDef" = dataclasses.field()

    certificateId = field("certificateId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeCertificateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCertificateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCustomMetricRequest:
    boto3_raw_data: "type_defs.DescribeCustomMetricRequestTypeDef" = dataclasses.field()

    metricName = field("metricName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeCustomMetricRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCustomMetricRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDetectMitigationActionsTaskRequest:
    boto3_raw_data: "type_defs.DescribeDetectMitigationActionsTaskRequestTypeDef" = (
        dataclasses.field()
    )

    taskId = field("taskId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDetectMitigationActionsTaskRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDetectMitigationActionsTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDimensionRequest:
    boto3_raw_data: "type_defs.DescribeDimensionRequestTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDimensionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDimensionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDomainConfigurationRequest:
    boto3_raw_data: "type_defs.DescribeDomainConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    domainConfigurationName = field("domainConfigurationName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDomainConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDomainConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServerCertificateSummary:
    boto3_raw_data: "type_defs.ServerCertificateSummaryTypeDef" = dataclasses.field()

    serverCertificateArn = field("serverCertificateArn")
    serverCertificateStatus = field("serverCertificateStatus")
    serverCertificateStatusDetail = field("serverCertificateStatusDetail")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServerCertificateSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServerCertificateSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEndpointRequest:
    boto3_raw_data: "type_defs.DescribeEndpointRequestTypeDef" = dataclasses.field()

    endpointType = field("endpointType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEndpointRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFleetMetricRequest:
    boto3_raw_data: "type_defs.DescribeFleetMetricRequestTypeDef" = dataclasses.field()

    metricName = field("metricName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeFleetMetricRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFleetMetricRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeIndexRequest:
    boto3_raw_data: "type_defs.DescribeIndexRequestTypeDef" = dataclasses.field()

    indexName = field("indexName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeIndexRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeIndexRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeJobExecutionRequest:
    boto3_raw_data: "type_defs.DescribeJobExecutionRequestTypeDef" = dataclasses.field()

    jobId = field("jobId")
    thingName = field("thingName")
    executionNumber = field("executionNumber")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeJobExecutionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeJobExecutionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeJobRequest:
    boto3_raw_data: "type_defs.DescribeJobRequestTypeDef" = dataclasses.field()

    jobId = field("jobId")
    beforeSubstitution = field("beforeSubstitution")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeJobTemplateRequest:
    boto3_raw_data: "type_defs.DescribeJobTemplateRequestTypeDef" = dataclasses.field()

    jobTemplateId = field("jobTemplateId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeJobTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeJobTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeManagedJobTemplateRequest:
    boto3_raw_data: "type_defs.DescribeManagedJobTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    templateName = field("templateName")
    templateVersion = field("templateVersion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeManagedJobTemplateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeManagedJobTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentParameter:
    boto3_raw_data: "type_defs.DocumentParameterTypeDef" = dataclasses.field()

    key = field("key")
    description = field("description")
    regex = field("regex")
    example = field("example")
    optional = field("optional")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DocumentParameterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentParameterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMitigationActionRequest:
    boto3_raw_data: "type_defs.DescribeMitigationActionRequestTypeDef" = (
        dataclasses.field()
    )

    actionName = field("actionName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeMitigationActionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMitigationActionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeProvisioningTemplateRequest:
    boto3_raw_data: "type_defs.DescribeProvisioningTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    templateName = field("templateName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeProvisioningTemplateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeProvisioningTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeProvisioningTemplateVersionRequest:
    boto3_raw_data: "type_defs.DescribeProvisioningTemplateVersionRequestTypeDef" = (
        dataclasses.field()
    )

    templateName = field("templateName")
    versionId = field("versionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeProvisioningTemplateVersionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeProvisioningTemplateVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRoleAliasRequest:
    boto3_raw_data: "type_defs.DescribeRoleAliasRequestTypeDef" = dataclasses.field()

    roleAlias = field("roleAlias")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeRoleAliasRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRoleAliasRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoleAliasDescription:
    boto3_raw_data: "type_defs.RoleAliasDescriptionTypeDef" = dataclasses.field()

    roleAlias = field("roleAlias")
    roleAliasArn = field("roleAliasArn")
    roleArn = field("roleArn")
    owner = field("owner")
    credentialDurationSeconds = field("credentialDurationSeconds")
    creationDate = field("creationDate")
    lastModifiedDate = field("lastModifiedDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RoleAliasDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RoleAliasDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeScheduledAuditRequest:
    boto3_raw_data: "type_defs.DescribeScheduledAuditRequestTypeDef" = (
        dataclasses.field()
    )

    scheduledAuditName = field("scheduledAuditName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeScheduledAuditRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeScheduledAuditRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSecurityProfileRequest:
    boto3_raw_data: "type_defs.DescribeSecurityProfileRequestTypeDef" = (
        dataclasses.field()
    )

    securityProfileName = field("securityProfileName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeSecurityProfileRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSecurityProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStreamRequest:
    boto3_raw_data: "type_defs.DescribeStreamRequestTypeDef" = dataclasses.field()

    streamId = field("streamId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeStreamRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStreamRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeThingGroupRequest:
    boto3_raw_data: "type_defs.DescribeThingGroupRequestTypeDef" = dataclasses.field()

    thingGroupName = field("thingGroupName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeThingGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeThingGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeThingRegistrationTaskRequest:
    boto3_raw_data: "type_defs.DescribeThingRegistrationTaskRequestTypeDef" = (
        dataclasses.field()
    )

    taskId = field("taskId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeThingRegistrationTaskRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeThingRegistrationTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeThingRequest:
    boto3_raw_data: "type_defs.DescribeThingRequestTypeDef" = dataclasses.field()

    thingName = field("thingName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeThingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeThingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeThingTypeRequest:
    boto3_raw_data: "type_defs.DescribeThingTypeRequestTypeDef" = dataclasses.field()

    thingTypeName = field("thingTypeName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeThingTypeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeThingTypeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ThingTypeMetadata:
    boto3_raw_data: "type_defs.ThingTypeMetadataTypeDef" = dataclasses.field()

    deprecated = field("deprecated")
    deprecationDate = field("deprecationDate")
    creationDate = field("creationDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ThingTypeMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ThingTypeMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Destination:
    boto3_raw_data: "type_defs.S3DestinationTypeDef" = dataclasses.field()

    bucket = field("bucket")
    prefix = field("prefix")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3DestinationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3DestinationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetachPolicyRequest:
    boto3_raw_data: "type_defs.DetachPolicyRequestTypeDef" = dataclasses.field()

    policyName = field("policyName")
    target = field("target")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetachPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetachPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetachPrincipalPolicyRequest:
    boto3_raw_data: "type_defs.DetachPrincipalPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    policyName = field("policyName")
    principal = field("principal")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetachPrincipalPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetachPrincipalPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetachSecurityProfileRequest:
    boto3_raw_data: "type_defs.DetachSecurityProfileRequestTypeDef" = (
        dataclasses.field()
    )

    securityProfileName = field("securityProfileName")
    securityProfileTargetArn = field("securityProfileTargetArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetachSecurityProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetachSecurityProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetachThingPrincipalRequest:
    boto3_raw_data: "type_defs.DetachThingPrincipalRequestTypeDef" = dataclasses.field()

    thingName = field("thingName")
    principal = field("principal")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetachThingPrincipalRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetachThingPrincipalRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectMitigationActionExecution:
    boto3_raw_data: "type_defs.DetectMitigationActionExecutionTypeDef" = (
        dataclasses.field()
    )

    taskId = field("taskId")
    violationId = field("violationId")
    actionName = field("actionName")
    thingName = field("thingName")
    executionStartDate = field("executionStartDate")
    executionEndDate = field("executionEndDate")
    status = field("status")
    errorCode = field("errorCode")
    message = field("message")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DetectMitigationActionExecutionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectMitigationActionExecutionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectMitigationActionsTaskStatistics:
    boto3_raw_data: "type_defs.DetectMitigationActionsTaskStatisticsTypeDef" = (
        dataclasses.field()
    )

    actionsExecuted = field("actionsExecuted")
    actionsSkipped = field("actionsSkipped")
    actionsFailed = field("actionsFailed")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DetectMitigationActionsTaskStatisticsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectMitigationActionsTaskStatisticsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectMitigationActionsTaskTargetOutput:
    boto3_raw_data: "type_defs.DetectMitigationActionsTaskTargetOutputTypeDef" = (
        dataclasses.field()
    )

    violationIds = field("violationIds")
    securityProfileName = field("securityProfileName")
    behaviorName = field("behaviorName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DetectMitigationActionsTaskTargetOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectMitigationActionsTaskTargetOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ViolationEventOccurrenceRangeOutput:
    boto3_raw_data: "type_defs.ViolationEventOccurrenceRangeOutputTypeDef" = (
        dataclasses.field()
    )

    startTime = field("startTime")
    endTime = field("endTime")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ViolationEventOccurrenceRangeOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ViolationEventOccurrenceRangeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectMitigationActionsTaskTarget:
    boto3_raw_data: "type_defs.DetectMitigationActionsTaskTargetTypeDef" = (
        dataclasses.field()
    )

    violationIds = field("violationIds")
    securityProfileName = field("securityProfileName")
    behaviorName = field("behaviorName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DetectMitigationActionsTaskTargetTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectMitigationActionsTaskTargetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisableTopicRuleRequest:
    boto3_raw_data: "type_defs.DisableTopicRuleRequestTypeDef" = dataclasses.field()

    ruleName = field("ruleName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisableTopicRuleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisableTopicRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateSbomFromPackageVersionRequest:
    boto3_raw_data: "type_defs.DisassociateSbomFromPackageVersionRequestTypeDef" = (
        dataclasses.field()
    )

    packageName = field("packageName")
    versionName = field("versionName")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateSbomFromPackageVersionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateSbomFromPackageVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainConfigurationSummary:
    boto3_raw_data: "type_defs.DomainConfigurationSummaryTypeDef" = dataclasses.field()

    domainConfigurationName = field("domainConfigurationName")
    domainConfigurationArn = field("domainConfigurationArn")
    serviceType = field("serviceType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DomainConfigurationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DomainConfigurationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutItemInput:
    boto3_raw_data: "type_defs.PutItemInputTypeDef" = dataclasses.field()

    tableName = field("tableName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PutItemInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PutItemInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EffectivePolicy:
    boto3_raw_data: "type_defs.EffectivePolicyTypeDef" = dataclasses.field()

    policyName = field("policyName")
    policyArn = field("policyArn")
    policyDocument = field("policyDocument")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EffectivePolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EffectivePolicyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnableIoTLoggingParams:
    boto3_raw_data: "type_defs.EnableIoTLoggingParamsTypeDef" = dataclasses.field()

    roleArnForLogging = field("roleArnForLogging")
    logLevel = field("logLevel")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnableIoTLoggingParamsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnableIoTLoggingParamsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnableTopicRuleRequest:
    boto3_raw_data: "type_defs.EnableTopicRuleRequestTypeDef" = dataclasses.field()

    ruleName = field("ruleName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnableTopicRuleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnableTopicRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ErrorInfo:
    boto3_raw_data: "type_defs.ErrorInfoTypeDef" = dataclasses.field()

    code = field("code")
    message = field("message")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ErrorInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ErrorInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RateIncreaseCriteria:
    boto3_raw_data: "type_defs.RateIncreaseCriteriaTypeDef" = dataclasses.field()

    numberOfNotifiedThings = field("numberOfNotifiedThings")
    numberOfSucceededThings = field("numberOfSucceededThings")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RateIncreaseCriteriaTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RateIncreaseCriteriaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Field:
    boto3_raw_data: "type_defs.FieldTypeDef" = dataclasses.field()

    name = field("name")
    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FieldTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FieldTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Location:
    boto3_raw_data: "type_defs.S3LocationTypeDef" = dataclasses.field()

    bucket = field("bucket")
    key = field("key")
    version = field("version")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3LocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3LocationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Stream:
    boto3_raw_data: "type_defs.StreamTypeDef" = dataclasses.field()

    streamId = field("streamId")
    fileId = field("fileId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StreamTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StreamTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FleetMetricNameAndArn:
    boto3_raw_data: "type_defs.FleetMetricNameAndArnTypeDef" = dataclasses.field()

    metricName = field("metricName")
    metricArn = field("metricArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FleetMetricNameAndArnTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FleetMetricNameAndArnTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GeoLocationTarget:
    boto3_raw_data: "type_defs.GeoLocationTargetTypeDef" = dataclasses.field()

    name = field("name")
    order = field("order")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GeoLocationTargetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GeoLocationTargetTypeDef"]
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
class GetBehaviorModelTrainingSummariesRequest:
    boto3_raw_data: "type_defs.GetBehaviorModelTrainingSummariesRequestTypeDef" = (
        dataclasses.field()
    )

    securityProfileName = field("securityProfileName")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetBehaviorModelTrainingSummariesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBehaviorModelTrainingSummariesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCardinalityRequest:
    boto3_raw_data: "type_defs.GetCardinalityRequestTypeDef" = dataclasses.field()

    queryString = field("queryString")
    indexName = field("indexName")
    aggregationField = field("aggregationField")
    queryVersion = field("queryVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCardinalityRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCardinalityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCommandExecutionRequest:
    boto3_raw_data: "type_defs.GetCommandExecutionRequestTypeDef" = dataclasses.field()

    executionId = field("executionId")
    targetArn = field("targetArn")
    includeResult = field("includeResult")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCommandExecutionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCommandExecutionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StatusReason:
    boto3_raw_data: "type_defs.StatusReasonTypeDef" = dataclasses.field()

    reasonCode = field("reasonCode")
    reasonDescription = field("reasonDescription")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StatusReasonTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StatusReasonTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCommandRequest:
    boto3_raw_data: "type_defs.GetCommandRequestTypeDef" = dataclasses.field()

    commandId = field("commandId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetCommandRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCommandRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEffectivePoliciesRequest:
    boto3_raw_data: "type_defs.GetEffectivePoliciesRequestTypeDef" = dataclasses.field()

    principal = field("principal")
    cognitoIdentityPoolId = field("cognitoIdentityPoolId")
    thingName = field("thingName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEffectivePoliciesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEffectivePoliciesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetJobDocumentRequest:
    boto3_raw_data: "type_defs.GetJobDocumentRequestTypeDef" = dataclasses.field()

    jobId = field("jobId")
    beforeSubstitution = field("beforeSubstitution")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetJobDocumentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetJobDocumentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOTAUpdateRequest:
    boto3_raw_data: "type_defs.GetOTAUpdateRequestTypeDef" = dataclasses.field()

    otaUpdateId = field("otaUpdateId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetOTAUpdateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOTAUpdateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VersionUpdateByJobsConfig:
    boto3_raw_data: "type_defs.VersionUpdateByJobsConfigTypeDef" = dataclasses.field()

    enabled = field("enabled")
    roleArn = field("roleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VersionUpdateByJobsConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VersionUpdateByJobsConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPackageRequest:
    boto3_raw_data: "type_defs.GetPackageRequestTypeDef" = dataclasses.field()

    packageName = field("packageName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetPackageRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPackageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPackageVersionRequest:
    boto3_raw_data: "type_defs.GetPackageVersionRequestTypeDef" = dataclasses.field()

    packageName = field("packageName")
    versionName = field("versionName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPackageVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPackageVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPercentilesRequest:
    boto3_raw_data: "type_defs.GetPercentilesRequestTypeDef" = dataclasses.field()

    queryString = field("queryString")
    indexName = field("indexName")
    aggregationField = field("aggregationField")
    queryVersion = field("queryVersion")
    percents = field("percents")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPercentilesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPercentilesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PercentPair:
    boto3_raw_data: "type_defs.PercentPairTypeDef" = dataclasses.field()

    percent = field("percent")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PercentPairTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PercentPairTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPolicyRequest:
    boto3_raw_data: "type_defs.GetPolicyRequestTypeDef" = dataclasses.field()

    policyName = field("policyName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetPolicyRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPolicyVersionRequest:
    boto3_raw_data: "type_defs.GetPolicyVersionRequestTypeDef" = dataclasses.field()

    policyName = field("policyName")
    policyVersionId = field("policyVersionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPolicyVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPolicyVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStatisticsRequest:
    boto3_raw_data: "type_defs.GetStatisticsRequestTypeDef" = dataclasses.field()

    queryString = field("queryString")
    indexName = field("indexName")
    aggregationField = field("aggregationField")
    queryVersion = field("queryVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetStatisticsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetStatisticsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Statistics:
    boto3_raw_data: "type_defs.StatisticsTypeDef" = dataclasses.field()

    count = field("count")
    average = field("average")
    sum = field("sum")
    minimum = field("minimum")
    maximum = field("maximum")
    sumOfSquares = field("sumOfSquares")
    variance = field("variance")
    stdDeviation = field("stdDeviation")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StatisticsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StatisticsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetThingConnectivityDataRequest:
    boto3_raw_data: "type_defs.GetThingConnectivityDataRequestTypeDef" = (
        dataclasses.field()
    )

    thingName = field("thingName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetThingConnectivityDataRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetThingConnectivityDataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTopicRuleDestinationRequest:
    boto3_raw_data: "type_defs.GetTopicRuleDestinationRequestTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetTopicRuleDestinationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTopicRuleDestinationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTopicRuleRequest:
    boto3_raw_data: "type_defs.GetTopicRuleRequestTypeDef" = dataclasses.field()

    ruleName = field("ruleName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTopicRuleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTopicRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GroupNameAndArn:
    boto3_raw_data: "type_defs.GroupNameAndArnTypeDef" = dataclasses.field()

    groupName = field("groupName")
    groupArn = field("groupArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GroupNameAndArnTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GroupNameAndArnTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HttpActionHeader:
    boto3_raw_data: "type_defs.HttpActionHeaderTypeDef" = dataclasses.field()

    key = field("key")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HttpActionHeaderTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HttpActionHeaderTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SigV4Authorization:
    boto3_raw_data: "type_defs.SigV4AuthorizationTypeDef" = dataclasses.field()

    signingRegion = field("signingRegion")
    serviceName = field("serviceName")
    roleArn = field("roleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SigV4AuthorizationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SigV4AuthorizationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HttpContext:
    boto3_raw_data: "type_defs.HttpContextTypeDef" = dataclasses.field()

    headers = field("headers")
    queryString = field("queryString")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HttpContextTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HttpContextTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HttpUrlDestinationConfiguration:
    boto3_raw_data: "type_defs.HttpUrlDestinationConfigurationTypeDef" = (
        dataclasses.field()
    )

    confirmationUrl = field("confirmationUrl")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.HttpUrlDestinationConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HttpUrlDestinationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HttpUrlDestinationProperties:
    boto3_raw_data: "type_defs.HttpUrlDestinationPropertiesTypeDef" = (
        dataclasses.field()
    )

    confirmationUrl = field("confirmationUrl")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HttpUrlDestinationPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HttpUrlDestinationPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HttpUrlDestinationSummary:
    boto3_raw_data: "type_defs.HttpUrlDestinationSummaryTypeDef" = dataclasses.field()

    confirmationUrl = field("confirmationUrl")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HttpUrlDestinationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HttpUrlDestinationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IssuerCertificateIdentifier:
    boto3_raw_data: "type_defs.IssuerCertificateIdentifierTypeDef" = dataclasses.field()

    issuerCertificateSubject = field("issuerCertificateSubject")
    issuerId = field("issuerId")
    issuerCertificateSerialNumber = field("issuerCertificateSerialNumber")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IssuerCertificateIdentifierTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IssuerCertificateIdentifierTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobExecutionStatusDetails:
    boto3_raw_data: "type_defs.JobExecutionStatusDetailsTypeDef" = dataclasses.field()

    detailsMap = field("detailsMap")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JobExecutionStatusDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobExecutionStatusDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobExecutionSummary:
    boto3_raw_data: "type_defs.JobExecutionSummaryTypeDef" = dataclasses.field()

    status = field("status")
    queuedAt = field("queuedAt")
    startedAt = field("startedAt")
    lastUpdatedAt = field("lastUpdatedAt")
    executionNumber = field("executionNumber")
    retryAttempt = field("retryAttempt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JobExecutionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobExecutionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetryCriteria:
    boto3_raw_data: "type_defs.RetryCriteriaTypeDef" = dataclasses.field()

    failureType = field("failureType")
    numberOfRetries = field("numberOfRetries")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RetryCriteriaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RetryCriteriaTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobProcessDetails:
    boto3_raw_data: "type_defs.JobProcessDetailsTypeDef" = dataclasses.field()

    processingTargets = field("processingTargets")
    numberOfCanceledThings = field("numberOfCanceledThings")
    numberOfSucceededThings = field("numberOfSucceededThings")
    numberOfFailedThings = field("numberOfFailedThings")
    numberOfRejectedThings = field("numberOfRejectedThings")
    numberOfQueuedThings = field("numberOfQueuedThings")
    numberOfInProgressThings = field("numberOfInProgressThings")
    numberOfRemovedThings = field("numberOfRemovedThings")
    numberOfTimedOutThings = field("numberOfTimedOutThings")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobProcessDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobProcessDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobSummary:
    boto3_raw_data: "type_defs.JobSummaryTypeDef" = dataclasses.field()

    jobArn = field("jobArn")
    jobId = field("jobId")
    thingGroupId = field("thingGroupId")
    targetSelection = field("targetSelection")
    status = field("status")
    createdAt = field("createdAt")
    lastUpdatedAt = field("lastUpdatedAt")
    completedAt = field("completedAt")
    isConcurrent = field("isConcurrent")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobSummaryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobTemplateSummary:
    boto3_raw_data: "type_defs.JobTemplateSummaryTypeDef" = dataclasses.field()

    jobTemplateArn = field("jobTemplateArn")
    jobTemplateId = field("jobTemplateId")
    description = field("description")
    createdAt = field("createdAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JobTemplateSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobTemplateSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScheduledJobRollout:
    boto3_raw_data: "type_defs.ScheduledJobRolloutTypeDef" = dataclasses.field()

    startTime = field("startTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScheduledJobRolloutTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScheduledJobRolloutTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KafkaActionHeader:
    boto3_raw_data: "type_defs.KafkaActionHeaderTypeDef" = dataclasses.field()

    key = field("key")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KafkaActionHeaderTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KafkaActionHeaderTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListActiveViolationsRequest:
    boto3_raw_data: "type_defs.ListActiveViolationsRequestTypeDef" = dataclasses.field()

    thingName = field("thingName")
    securityProfileName = field("securityProfileName")
    behaviorCriteriaType = field("behaviorCriteriaType")
    listSuppressedAlerts = field("listSuppressedAlerts")
    verificationState = field("verificationState")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListActiveViolationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListActiveViolationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAttachedPoliciesRequest:
    boto3_raw_data: "type_defs.ListAttachedPoliciesRequestTypeDef" = dataclasses.field()

    target = field("target")
    recursive = field("recursive")
    marker = field("marker")
    pageSize = field("pageSize")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAttachedPoliciesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAttachedPoliciesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAuditMitigationActionsExecutionsRequest:
    boto3_raw_data: "type_defs.ListAuditMitigationActionsExecutionsRequestTypeDef" = (
        dataclasses.field()
    )

    taskId = field("taskId")
    findingId = field("findingId")
    actionStatus = field("actionStatus")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAuditMitigationActionsExecutionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAuditMitigationActionsExecutionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAuthorizersRequest:
    boto3_raw_data: "type_defs.ListAuthorizersRequestTypeDef" = dataclasses.field()

    pageSize = field("pageSize")
    marker = field("marker")
    ascendingOrder = field("ascendingOrder")
    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAuthorizersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAuthorizersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBillingGroupsRequest:
    boto3_raw_data: "type_defs.ListBillingGroupsRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")
    namePrefixFilter = field("namePrefixFilter")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBillingGroupsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBillingGroupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCACertificatesRequest:
    boto3_raw_data: "type_defs.ListCACertificatesRequestTypeDef" = dataclasses.field()

    pageSize = field("pageSize")
    marker = field("marker")
    ascendingOrder = field("ascendingOrder")
    templateName = field("templateName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCACertificatesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCACertificatesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCertificateProvidersRequest:
    boto3_raw_data: "type_defs.ListCertificateProvidersRequestTypeDef" = (
        dataclasses.field()
    )

    nextToken = field("nextToken")
    ascendingOrder = field("ascendingOrder")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListCertificateProvidersRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCertificateProvidersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCertificatesByCARequest:
    boto3_raw_data: "type_defs.ListCertificatesByCARequestTypeDef" = dataclasses.field()

    caCertificateId = field("caCertificateId")
    pageSize = field("pageSize")
    marker = field("marker")
    ascendingOrder = field("ascendingOrder")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCertificatesByCARequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCertificatesByCARequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCertificatesRequest:
    boto3_raw_data: "type_defs.ListCertificatesRequestTypeDef" = dataclasses.field()

    pageSize = field("pageSize")
    marker = field("marker")
    ascendingOrder = field("ascendingOrder")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCertificatesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCertificatesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimeFilter:
    boto3_raw_data: "type_defs.TimeFilterTypeDef" = dataclasses.field()

    after = field("after")
    before = field("before")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TimeFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TimeFilterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCommandsRequest:
    boto3_raw_data: "type_defs.ListCommandsRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")
    namespace = field("namespace")
    commandParameterName = field("commandParameterName")
    sortOrder = field("sortOrder")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCommandsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCommandsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCustomMetricsRequest:
    boto3_raw_data: "type_defs.ListCustomMetricsRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCustomMetricsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCustomMetricsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDimensionsRequest:
    boto3_raw_data: "type_defs.ListDimensionsRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDimensionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDimensionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDomainConfigurationsRequest:
    boto3_raw_data: "type_defs.ListDomainConfigurationsRequestTypeDef" = (
        dataclasses.field()
    )

    marker = field("marker")
    pageSize = field("pageSize")
    serviceType = field("serviceType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDomainConfigurationsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDomainConfigurationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFleetMetricsRequest:
    boto3_raw_data: "type_defs.ListFleetMetricsRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFleetMetricsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFleetMetricsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIndicesRequest:
    boto3_raw_data: "type_defs.ListIndicesRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIndicesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIndicesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobExecutionsForJobRequest:
    boto3_raw_data: "type_defs.ListJobExecutionsForJobRequestTypeDef" = (
        dataclasses.field()
    )

    jobId = field("jobId")
    status = field("status")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListJobExecutionsForJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobExecutionsForJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobExecutionsForThingRequest:
    boto3_raw_data: "type_defs.ListJobExecutionsForThingRequestTypeDef" = (
        dataclasses.field()
    )

    thingName = field("thingName")
    status = field("status")
    namespaceId = field("namespaceId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    jobId = field("jobId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListJobExecutionsForThingRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobExecutionsForThingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobTemplatesRequest:
    boto3_raw_data: "type_defs.ListJobTemplatesRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListJobTemplatesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobTemplatesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobsRequest:
    boto3_raw_data: "type_defs.ListJobsRequestTypeDef" = dataclasses.field()

    status = field("status")
    targetSelection = field("targetSelection")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    thingGroupName = field("thingGroupName")
    thingGroupId = field("thingGroupId")
    namespaceId = field("namespaceId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListJobsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListJobsRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListManagedJobTemplatesRequest:
    boto3_raw_data: "type_defs.ListManagedJobTemplatesRequestTypeDef" = (
        dataclasses.field()
    )

    templateName = field("templateName")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListManagedJobTemplatesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListManagedJobTemplatesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManagedJobTemplateSummary:
    boto3_raw_data: "type_defs.ManagedJobTemplateSummaryTypeDef" = dataclasses.field()

    templateArn = field("templateArn")
    templateName = field("templateName")
    description = field("description")
    environments = field("environments")
    templateVersion = field("templateVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ManagedJobTemplateSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManagedJobTemplateSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMitigationActionsRequest:
    boto3_raw_data: "type_defs.ListMitigationActionsRequestTypeDef" = (
        dataclasses.field()
    )

    actionType = field("actionType")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMitigationActionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMitigationActionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MitigationActionIdentifier:
    boto3_raw_data: "type_defs.MitigationActionIdentifierTypeDef" = dataclasses.field()

    actionName = field("actionName")
    actionArn = field("actionArn")
    creationDate = field("creationDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MitigationActionIdentifierTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MitigationActionIdentifierTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOTAUpdatesRequest:
    boto3_raw_data: "type_defs.ListOTAUpdatesRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")
    otaUpdateStatus = field("otaUpdateStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListOTAUpdatesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOTAUpdatesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OTAUpdateSummary:
    boto3_raw_data: "type_defs.OTAUpdateSummaryTypeDef" = dataclasses.field()

    otaUpdateId = field("otaUpdateId")
    otaUpdateArn = field("otaUpdateArn")
    creationDate = field("creationDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OTAUpdateSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OTAUpdateSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOutgoingCertificatesRequest:
    boto3_raw_data: "type_defs.ListOutgoingCertificatesRequestTypeDef" = (
        dataclasses.field()
    )

    pageSize = field("pageSize")
    marker = field("marker")
    ascendingOrder = field("ascendingOrder")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListOutgoingCertificatesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOutgoingCertificatesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutgoingCertificate:
    boto3_raw_data: "type_defs.OutgoingCertificateTypeDef" = dataclasses.field()

    certificateArn = field("certificateArn")
    certificateId = field("certificateId")
    transferredTo = field("transferredTo")
    transferDate = field("transferDate")
    transferMessage = field("transferMessage")
    creationDate = field("creationDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OutgoingCertificateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OutgoingCertificateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPackageVersionsRequest:
    boto3_raw_data: "type_defs.ListPackageVersionsRequestTypeDef" = dataclasses.field()

    packageName = field("packageName")
    status = field("status")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPackageVersionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPackageVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PackageVersionSummary:
    boto3_raw_data: "type_defs.PackageVersionSummaryTypeDef" = dataclasses.field()

    packageName = field("packageName")
    versionName = field("versionName")
    status = field("status")
    creationDate = field("creationDate")
    lastModifiedDate = field("lastModifiedDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PackageVersionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PackageVersionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPackagesRequest:
    boto3_raw_data: "type_defs.ListPackagesRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPackagesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPackagesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PackageSummary:
    boto3_raw_data: "type_defs.PackageSummaryTypeDef" = dataclasses.field()

    packageName = field("packageName")
    defaultVersionName = field("defaultVersionName")
    creationDate = field("creationDate")
    lastModifiedDate = field("lastModifiedDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PackageSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PackageSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPoliciesRequest:
    boto3_raw_data: "type_defs.ListPoliciesRequestTypeDef" = dataclasses.field()

    marker = field("marker")
    pageSize = field("pageSize")
    ascendingOrder = field("ascendingOrder")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPoliciesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPoliciesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPolicyPrincipalsRequest:
    boto3_raw_data: "type_defs.ListPolicyPrincipalsRequestTypeDef" = dataclasses.field()

    policyName = field("policyName")
    marker = field("marker")
    pageSize = field("pageSize")
    ascendingOrder = field("ascendingOrder")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPolicyPrincipalsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPolicyPrincipalsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPolicyVersionsRequest:
    boto3_raw_data: "type_defs.ListPolicyVersionsRequestTypeDef" = dataclasses.field()

    policyName = field("policyName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPolicyVersionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPolicyVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolicyVersion:
    boto3_raw_data: "type_defs.PolicyVersionTypeDef" = dataclasses.field()

    versionId = field("versionId")
    isDefaultVersion = field("isDefaultVersion")
    createDate = field("createDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PolicyVersionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PolicyVersionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPrincipalPoliciesRequest:
    boto3_raw_data: "type_defs.ListPrincipalPoliciesRequestTypeDef" = (
        dataclasses.field()
    )

    principal = field("principal")
    marker = field("marker")
    pageSize = field("pageSize")
    ascendingOrder = field("ascendingOrder")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPrincipalPoliciesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPrincipalPoliciesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPrincipalThingsRequest:
    boto3_raw_data: "type_defs.ListPrincipalThingsRequestTypeDef" = dataclasses.field()

    principal = field("principal")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPrincipalThingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPrincipalThingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPrincipalThingsV2Request:
    boto3_raw_data: "type_defs.ListPrincipalThingsV2RequestTypeDef" = (
        dataclasses.field()
    )

    principal = field("principal")
    nextToken = field("nextToken")
    maxResults = field("maxResults")
    thingPrincipalType = field("thingPrincipalType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPrincipalThingsV2RequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPrincipalThingsV2RequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PrincipalThingObject:
    boto3_raw_data: "type_defs.PrincipalThingObjectTypeDef" = dataclasses.field()

    thingName = field("thingName")
    thingPrincipalType = field("thingPrincipalType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PrincipalThingObjectTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PrincipalThingObjectTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProvisioningTemplateVersionsRequest:
    boto3_raw_data: "type_defs.ListProvisioningTemplateVersionsRequestTypeDef" = (
        dataclasses.field()
    )

    templateName = field("templateName")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListProvisioningTemplateVersionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProvisioningTemplateVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProvisioningTemplateVersionSummary:
    boto3_raw_data: "type_defs.ProvisioningTemplateVersionSummaryTypeDef" = (
        dataclasses.field()
    )

    versionId = field("versionId")
    creationDate = field("creationDate")
    isDefaultVersion = field("isDefaultVersion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ProvisioningTemplateVersionSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProvisioningTemplateVersionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProvisioningTemplatesRequest:
    boto3_raw_data: "type_defs.ListProvisioningTemplatesRequestTypeDef" = (
        dataclasses.field()
    )

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListProvisioningTemplatesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProvisioningTemplatesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProvisioningTemplateSummary:
    boto3_raw_data: "type_defs.ProvisioningTemplateSummaryTypeDef" = dataclasses.field()

    templateArn = field("templateArn")
    templateName = field("templateName")
    description = field("description")
    creationDate = field("creationDate")
    lastModifiedDate = field("lastModifiedDate")
    enabled = field("enabled")
    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProvisioningTemplateSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProvisioningTemplateSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRelatedResourcesForAuditFindingRequest:
    boto3_raw_data: "type_defs.ListRelatedResourcesForAuditFindingRequestTypeDef" = (
        dataclasses.field()
    )

    findingId = field("findingId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRelatedResourcesForAuditFindingRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRelatedResourcesForAuditFindingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRoleAliasesRequest:
    boto3_raw_data: "type_defs.ListRoleAliasesRequestTypeDef" = dataclasses.field()

    pageSize = field("pageSize")
    marker = field("marker")
    ascendingOrder = field("ascendingOrder")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRoleAliasesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRoleAliasesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSbomValidationResultsRequest:
    boto3_raw_data: "type_defs.ListSbomValidationResultsRequestTypeDef" = (
        dataclasses.field()
    )

    packageName = field("packageName")
    versionName = field("versionName")
    validationResult = field("validationResult")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSbomValidationResultsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSbomValidationResultsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SbomValidationResultSummary:
    boto3_raw_data: "type_defs.SbomValidationResultSummaryTypeDef" = dataclasses.field()

    fileName = field("fileName")
    validationResult = field("validationResult")
    errorCode = field("errorCode")
    errorMessage = field("errorMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SbomValidationResultSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SbomValidationResultSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListScheduledAuditsRequest:
    boto3_raw_data: "type_defs.ListScheduledAuditsRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListScheduledAuditsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListScheduledAuditsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScheduledAuditMetadata:
    boto3_raw_data: "type_defs.ScheduledAuditMetadataTypeDef" = dataclasses.field()

    scheduledAuditName = field("scheduledAuditName")
    scheduledAuditArn = field("scheduledAuditArn")
    frequency = field("frequency")
    dayOfMonth = field("dayOfMonth")
    dayOfWeek = field("dayOfWeek")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScheduledAuditMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScheduledAuditMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSecurityProfilesForTargetRequest:
    boto3_raw_data: "type_defs.ListSecurityProfilesForTargetRequestTypeDef" = (
        dataclasses.field()
    )

    securityProfileTargetArn = field("securityProfileTargetArn")
    nextToken = field("nextToken")
    maxResults = field("maxResults")
    recursive = field("recursive")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSecurityProfilesForTargetRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSecurityProfilesForTargetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSecurityProfilesRequest:
    boto3_raw_data: "type_defs.ListSecurityProfilesRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")
    dimensionName = field("dimensionName")
    metricName = field("metricName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSecurityProfilesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSecurityProfilesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SecurityProfileIdentifier:
    boto3_raw_data: "type_defs.SecurityProfileIdentifierTypeDef" = dataclasses.field()

    name = field("name")
    arn = field("arn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SecurityProfileIdentifierTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SecurityProfileIdentifierTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStreamsRequest:
    boto3_raw_data: "type_defs.ListStreamsRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")
    ascendingOrder = field("ascendingOrder")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListStreamsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStreamsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StreamSummary:
    boto3_raw_data: "type_defs.StreamSummaryTypeDef" = dataclasses.field()

    streamId = field("streamId")
    streamArn = field("streamArn")
    streamVersion = field("streamVersion")
    description = field("description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StreamSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StreamSummaryTypeDef"]],
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
    nextToken = field("nextToken")

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
class ListTargetsForPolicyRequest:
    boto3_raw_data: "type_defs.ListTargetsForPolicyRequestTypeDef" = dataclasses.field()

    policyName = field("policyName")
    marker = field("marker")
    pageSize = field("pageSize")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTargetsForPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTargetsForPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTargetsForSecurityProfileRequest:
    boto3_raw_data: "type_defs.ListTargetsForSecurityProfileRequestTypeDef" = (
        dataclasses.field()
    )

    securityProfileName = field("securityProfileName")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTargetsForSecurityProfileRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTargetsForSecurityProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SecurityProfileTarget:
    boto3_raw_data: "type_defs.SecurityProfileTargetTypeDef" = dataclasses.field()

    arn = field("arn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SecurityProfileTargetTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SecurityProfileTargetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListThingGroupsForThingRequest:
    boto3_raw_data: "type_defs.ListThingGroupsForThingRequestTypeDef" = (
        dataclasses.field()
    )

    thingName = field("thingName")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListThingGroupsForThingRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListThingGroupsForThingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListThingGroupsRequest:
    boto3_raw_data: "type_defs.ListThingGroupsRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")
    parentGroup = field("parentGroup")
    namePrefixFilter = field("namePrefixFilter")
    recursive = field("recursive")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListThingGroupsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListThingGroupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListThingPrincipalsRequest:
    boto3_raw_data: "type_defs.ListThingPrincipalsRequestTypeDef" = dataclasses.field()

    thingName = field("thingName")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListThingPrincipalsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListThingPrincipalsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListThingPrincipalsV2Request:
    boto3_raw_data: "type_defs.ListThingPrincipalsV2RequestTypeDef" = (
        dataclasses.field()
    )

    thingName = field("thingName")
    nextToken = field("nextToken")
    maxResults = field("maxResults")
    thingPrincipalType = field("thingPrincipalType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListThingPrincipalsV2RequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListThingPrincipalsV2RequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ThingPrincipalObject:
    boto3_raw_data: "type_defs.ThingPrincipalObjectTypeDef" = dataclasses.field()

    principal = field("principal")
    thingPrincipalType = field("thingPrincipalType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ThingPrincipalObjectTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ThingPrincipalObjectTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListThingRegistrationTaskReportsRequest:
    boto3_raw_data: "type_defs.ListThingRegistrationTaskReportsRequestTypeDef" = (
        dataclasses.field()
    )

    taskId = field("taskId")
    reportType = field("reportType")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListThingRegistrationTaskReportsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListThingRegistrationTaskReportsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListThingRegistrationTasksRequest:
    boto3_raw_data: "type_defs.ListThingRegistrationTasksRequestTypeDef" = (
        dataclasses.field()
    )

    nextToken = field("nextToken")
    maxResults = field("maxResults")
    status = field("status")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListThingRegistrationTasksRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListThingRegistrationTasksRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListThingTypesRequest:
    boto3_raw_data: "type_defs.ListThingTypesRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")
    thingTypeName = field("thingTypeName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListThingTypesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListThingTypesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListThingsInBillingGroupRequest:
    boto3_raw_data: "type_defs.ListThingsInBillingGroupRequestTypeDef" = (
        dataclasses.field()
    )

    billingGroupName = field("billingGroupName")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListThingsInBillingGroupRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListThingsInBillingGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListThingsInThingGroupRequest:
    boto3_raw_data: "type_defs.ListThingsInThingGroupRequestTypeDef" = (
        dataclasses.field()
    )

    thingGroupName = field("thingGroupName")
    recursive = field("recursive")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListThingsInThingGroupRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListThingsInThingGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListThingsRequest:
    boto3_raw_data: "type_defs.ListThingsRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")
    attributeName = field("attributeName")
    attributeValue = field("attributeValue")
    thingTypeName = field("thingTypeName")
    usePrefixAttributeValue = field("usePrefixAttributeValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListThingsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListThingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ThingAttribute:
    boto3_raw_data: "type_defs.ThingAttributeTypeDef" = dataclasses.field()

    thingName = field("thingName")
    thingTypeName = field("thingTypeName")
    thingArn = field("thingArn")
    attributes = field("attributes")
    version = field("version")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ThingAttributeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ThingAttributeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTopicRuleDestinationsRequest:
    boto3_raw_data: "type_defs.ListTopicRuleDestinationsRequestTypeDef" = (
        dataclasses.field()
    )

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListTopicRuleDestinationsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTopicRuleDestinationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTopicRulesRequest:
    boto3_raw_data: "type_defs.ListTopicRulesRequestTypeDef" = dataclasses.field()

    topic = field("topic")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    ruleDisabled = field("ruleDisabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTopicRulesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTopicRulesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TopicRuleListItem:
    boto3_raw_data: "type_defs.TopicRuleListItemTypeDef" = dataclasses.field()

    ruleArn = field("ruleArn")
    ruleName = field("ruleName")
    topicPattern = field("topicPattern")
    createdAt = field("createdAt")
    ruleDisabled = field("ruleDisabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TopicRuleListItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TopicRuleListItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListV2LoggingLevelsRequest:
    boto3_raw_data: "type_defs.ListV2LoggingLevelsRequestTypeDef" = dataclasses.field()

    targetType = field("targetType")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListV2LoggingLevelsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListV2LoggingLevelsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LocationTimestamp:
    boto3_raw_data: "type_defs.LocationTimestampTypeDef" = dataclasses.field()

    value = field("value")
    unit = field("unit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LocationTimestampTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LocationTimestampTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LogTarget:
    boto3_raw_data: "type_defs.LogTargetTypeDef" = dataclasses.field()

    targetType = field("targetType")
    targetName = field("targetName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LogTargetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LogTargetTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoggingOptionsPayload:
    boto3_raw_data: "type_defs.LoggingOptionsPayloadTypeDef" = dataclasses.field()

    roleArn = field("roleArn")
    logLevel = field("logLevel")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LoggingOptionsPayloadTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoggingOptionsPayloadTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricValue:
    boto3_raw_data: "type_defs.MetricValueTypeDef" = dataclasses.field()

    count = field("count")
    cidrs = field("cidrs")
    ports = field("ports")
    number = field("number")
    numbers = field("numbers")
    strings = field("strings")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricValueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetricValueTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PublishFindingToSnsParams:
    boto3_raw_data: "type_defs.PublishFindingToSnsParamsTypeDef" = dataclasses.field()

    topicArn = field("topicArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PublishFindingToSnsParamsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PublishFindingToSnsParamsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplaceDefaultPolicyVersionParams:
    boto3_raw_data: "type_defs.ReplaceDefaultPolicyVersionParamsTypeDef" = (
        dataclasses.field()
    )

    templateName = field("templateName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ReplaceDefaultPolicyVersionParamsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplaceDefaultPolicyVersionParamsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCACertificateParams:
    boto3_raw_data: "type_defs.UpdateCACertificateParamsTypeDef" = dataclasses.field()

    action = field("action")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateCACertificateParamsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCACertificateParamsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDeviceCertificateParams:
    boto3_raw_data: "type_defs.UpdateDeviceCertificateParamsTypeDef" = (
        dataclasses.field()
    )

    action = field("action")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateDeviceCertificateParamsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDeviceCertificateParamsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PropagatingAttribute:
    boto3_raw_data: "type_defs.PropagatingAttributeTypeDef" = dataclasses.field()

    userPropertyKey = field("userPropertyKey")
    thingAttribute = field("thingAttribute")
    connectionAttribute = field("connectionAttribute")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PropagatingAttributeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PropagatingAttributeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserProperty:
    boto3_raw_data: "type_defs.UserPropertyTypeDef" = dataclasses.field()

    key = field("key")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UserPropertyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UserPropertyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolicyVersionIdentifier:
    boto3_raw_data: "type_defs.PolicyVersionIdentifierTypeDef" = dataclasses.field()

    policyName = field("policyName")
    policyVersionId = field("policyVersionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PolicyVersionIdentifierTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PolicyVersionIdentifierTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutVerificationStateOnViolationRequest:
    boto3_raw_data: "type_defs.PutVerificationStateOnViolationRequestTypeDef" = (
        dataclasses.field()
    )

    violationId = field("violationId")
    verificationState = field("verificationState")
    verificationStateDescription = field("verificationStateDescription")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutVerificationStateOnViolationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutVerificationStateOnViolationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterCertificateRequest:
    boto3_raw_data: "type_defs.RegisterCertificateRequestTypeDef" = dataclasses.field()

    certificatePem = field("certificatePem")
    caCertificatePem = field("caCertificatePem")
    setAsActive = field("setAsActive")
    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterCertificateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterCertificateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterCertificateWithoutCARequest:
    boto3_raw_data: "type_defs.RegisterCertificateWithoutCARequestTypeDef" = (
        dataclasses.field()
    )

    certificatePem = field("certificatePem")
    status = field("status")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RegisterCertificateWithoutCARequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterCertificateWithoutCARequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterThingRequest:
    boto3_raw_data: "type_defs.RegisterThingRequestTypeDef" = dataclasses.field()

    templateBody = field("templateBody")
    parameters = field("parameters")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterThingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterThingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RejectCertificateTransferRequest:
    boto3_raw_data: "type_defs.RejectCertificateTransferRequestTypeDef" = (
        dataclasses.field()
    )

    certificateId = field("certificateId")
    rejectReason = field("rejectReason")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RejectCertificateTransferRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RejectCertificateTransferRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveThingFromBillingGroupRequest:
    boto3_raw_data: "type_defs.RemoveThingFromBillingGroupRequestTypeDef" = (
        dataclasses.field()
    )

    billingGroupName = field("billingGroupName")
    billingGroupArn = field("billingGroupArn")
    thingName = field("thingName")
    thingArn = field("thingArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RemoveThingFromBillingGroupRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveThingFromBillingGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveThingFromThingGroupRequest:
    boto3_raw_data: "type_defs.RemoveThingFromThingGroupRequestTypeDef" = (
        dataclasses.field()
    )

    thingGroupName = field("thingGroupName")
    thingGroupArn = field("thingGroupArn")
    thingName = field("thingName")
    thingArn = field("thingArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RemoveThingFromThingGroupRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveThingFromThingGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchIndexRequest:
    boto3_raw_data: "type_defs.SearchIndexRequestTypeDef" = dataclasses.field()

    queryString = field("queryString")
    indexName = field("indexName")
    nextToken = field("nextToken")
    maxResults = field("maxResults")
    queryVersion = field("queryVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchIndexRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchIndexRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ThingGroupDocument:
    boto3_raw_data: "type_defs.ThingGroupDocumentTypeDef" = dataclasses.field()

    thingGroupName = field("thingGroupName")
    thingGroupId = field("thingGroupId")
    thingGroupDescription = field("thingGroupDescription")
    attributes = field("attributes")
    parentGroupNames = field("parentGroupNames")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ThingGroupDocumentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ThingGroupDocumentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetDefaultAuthorizerRequest:
    boto3_raw_data: "type_defs.SetDefaultAuthorizerRequestTypeDef" = dataclasses.field()

    authorizerName = field("authorizerName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SetDefaultAuthorizerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetDefaultAuthorizerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetDefaultPolicyVersionRequest:
    boto3_raw_data: "type_defs.SetDefaultPolicyVersionRequestTypeDef" = (
        dataclasses.field()
    )

    policyName = field("policyName")
    policyVersionId = field("policyVersionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SetDefaultPolicyVersionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetDefaultPolicyVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetV2LoggingOptionsRequest:
    boto3_raw_data: "type_defs.SetV2LoggingOptionsRequestTypeDef" = dataclasses.field()

    roleArn = field("roleArn")
    defaultLogLevel = field("defaultLogLevel")
    disableAllLogs = field("disableAllLogs")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SetV2LoggingOptionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetV2LoggingOptionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SigningProfileParameter:
    boto3_raw_data: "type_defs.SigningProfileParameterTypeDef" = dataclasses.field()

    certificateArn = field("certificateArn")
    platform = field("platform")
    certificatePathOnDevice = field("certificatePathOnDevice")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SigningProfileParameterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SigningProfileParameterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartOnDemandAuditTaskRequest:
    boto3_raw_data: "type_defs.StartOnDemandAuditTaskRequestTypeDef" = (
        dataclasses.field()
    )

    targetCheckNames = field("targetCheckNames")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartOnDemandAuditTaskRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartOnDemandAuditTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartThingRegistrationTaskRequest:
    boto3_raw_data: "type_defs.StartThingRegistrationTaskRequestTypeDef" = (
        dataclasses.field()
    )

    templateBody = field("templateBody")
    inputFileBucket = field("inputFileBucket")
    inputFileKey = field("inputFileKey")
    roleArn = field("roleArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartThingRegistrationTaskRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartThingRegistrationTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopThingRegistrationTaskRequest:
    boto3_raw_data: "type_defs.StopThingRegistrationTaskRequestTypeDef" = (
        dataclasses.field()
    )

    taskId = field("taskId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StopThingRegistrationTaskRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopThingRegistrationTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TlsContext:
    boto3_raw_data: "type_defs.TlsContextTypeDef" = dataclasses.field()

    serverName = field("serverName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TlsContextTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TlsContextTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ThingConnectivity:
    boto3_raw_data: "type_defs.ThingConnectivityTypeDef" = dataclasses.field()

    connected = field("connected")
    timestamp = field("timestamp")
    disconnectReason = field("disconnectReason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ThingConnectivityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ThingConnectivityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimestreamDimension:
    boto3_raw_data: "type_defs.TimestreamDimensionTypeDef" = dataclasses.field()

    name = field("name")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TimestreamDimensionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimestreamDimensionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimestreamTimestamp:
    boto3_raw_data: "type_defs.TimestreamTimestampTypeDef" = dataclasses.field()

    value = field("value")
    unit = field("unit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TimestreamTimestampTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimestreamTimestampTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcDestinationConfiguration:
    boto3_raw_data: "type_defs.VpcDestinationConfigurationTypeDef" = dataclasses.field()

    subnetIds = field("subnetIds")
    vpcId = field("vpcId")
    roleArn = field("roleArn")
    securityGroups = field("securityGroups")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VpcDestinationConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcDestinationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcDestinationSummary:
    boto3_raw_data: "type_defs.VpcDestinationSummaryTypeDef" = dataclasses.field()

    subnetIds = field("subnetIds")
    securityGroups = field("securityGroups")
    vpcId = field("vpcId")
    roleArn = field("roleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VpcDestinationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcDestinationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcDestinationProperties:
    boto3_raw_data: "type_defs.VpcDestinationPropertiesTypeDef" = dataclasses.field()

    subnetIds = field("subnetIds")
    securityGroups = field("securityGroups")
    vpcId = field("vpcId")
    roleArn = field("roleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VpcDestinationPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcDestinationPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TransferCertificateRequest:
    boto3_raw_data: "type_defs.TransferCertificateRequestTypeDef" = dataclasses.field()

    certificateId = field("certificateId")
    targetAwsAccount = field("targetAwsAccount")
    transferMessage = field("transferMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TransferCertificateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TransferCertificateRequestTypeDef"]
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
class UpdateAuthorizerRequest:
    boto3_raw_data: "type_defs.UpdateAuthorizerRequestTypeDef" = dataclasses.field()

    authorizerName = field("authorizerName")
    authorizerFunctionArn = field("authorizerFunctionArn")
    tokenKeyName = field("tokenKeyName")
    tokenSigningPublicKeys = field("tokenSigningPublicKeys")
    status = field("status")
    enableCachingForHttp = field("enableCachingForHttp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAuthorizerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAuthorizerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCertificateProviderRequest:
    boto3_raw_data: "type_defs.UpdateCertificateProviderRequestTypeDef" = (
        dataclasses.field()
    )

    certificateProviderName = field("certificateProviderName")
    lambdaFunctionArn = field("lambdaFunctionArn")
    accountDefaultForOperations = field("accountDefaultForOperations")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateCertificateProviderRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCertificateProviderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCertificateRequest:
    boto3_raw_data: "type_defs.UpdateCertificateRequestTypeDef" = dataclasses.field()

    certificateId = field("certificateId")
    newStatus = field("newStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateCertificateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCertificateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCommandRequest:
    boto3_raw_data: "type_defs.UpdateCommandRequestTypeDef" = dataclasses.field()

    commandId = field("commandId")
    displayName = field("displayName")
    description = field("description")
    deprecated = field("deprecated")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateCommandRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCommandRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCustomMetricRequest:
    boto3_raw_data: "type_defs.UpdateCustomMetricRequestTypeDef" = dataclasses.field()

    metricName = field("metricName")
    displayName = field("displayName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateCustomMetricRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCustomMetricRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDimensionRequest:
    boto3_raw_data: "type_defs.UpdateDimensionRequestTypeDef" = dataclasses.field()

    name = field("name")
    stringValues = field("stringValues")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDimensionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDimensionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEncryptionConfigurationRequest:
    boto3_raw_data: "type_defs.UpdateEncryptionConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    encryptionType = field("encryptionType")
    kmsKeyArn = field("kmsKeyArn")
    kmsAccessRoleArn = field("kmsAccessRoleArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateEncryptionConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEncryptionConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePackageRequest:
    boto3_raw_data: "type_defs.UpdatePackageRequestTypeDef" = dataclasses.field()

    packageName = field("packageName")
    description = field("description")
    defaultVersionName = field("defaultVersionName")
    unsetDefaultVersion = field("unsetDefaultVersion")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePackageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePackageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRoleAliasRequest:
    boto3_raw_data: "type_defs.UpdateRoleAliasRequestTypeDef" = dataclasses.field()

    roleAlias = field("roleAlias")
    roleArn = field("roleArn")
    credentialDurationSeconds = field("credentialDurationSeconds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateRoleAliasRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRoleAliasRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateScheduledAuditRequest:
    boto3_raw_data: "type_defs.UpdateScheduledAuditRequestTypeDef" = dataclasses.field()

    scheduledAuditName = field("scheduledAuditName")
    frequency = field("frequency")
    dayOfMonth = field("dayOfMonth")
    dayOfWeek = field("dayOfWeek")
    targetCheckNames = field("targetCheckNames")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateScheduledAuditRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateScheduledAuditRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateThingGroupsForThingRequest:
    boto3_raw_data: "type_defs.UpdateThingGroupsForThingRequestTypeDef" = (
        dataclasses.field()
    )

    thingName = field("thingName")
    thingGroupsToAdd = field("thingGroupsToAdd")
    thingGroupsToRemove = field("thingGroupsToRemove")
    overrideDynamicGroups = field("overrideDynamicGroups")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateThingGroupsForThingRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateThingGroupsForThingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTopicRuleDestinationRequest:
    boto3_raw_data: "type_defs.UpdateTopicRuleDestinationRequestTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    status = field("status")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateTopicRuleDestinationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTopicRuleDestinationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValidationError:
    boto3_raw_data: "type_defs.ValidationErrorTypeDef" = dataclasses.field()

    errorMessage = field("errorMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ValidationErrorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ValidationErrorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AbortConfigOutput:
    boto3_raw_data: "type_defs.AbortConfigOutputTypeDef" = dataclasses.field()

    @cached_property
    def criteriaList(self):  # pragma: no cover
        return AbortCriteria.make_many(self.boto3_raw_data["criteriaList"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AbortConfigOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AbortConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AbortConfig:
    boto3_raw_data: "type_defs.AbortConfigTypeDef" = dataclasses.field()

    @cached_property
    def criteriaList(self):  # pragma: no cover
        return AbortCriteria.make_many(self.boto3_raw_data["criteriaList"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AbortConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AbortConfigTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricDatum:
    boto3_raw_data: "type_defs.MetricDatumTypeDef" = dataclasses.field()

    timestamp = field("timestamp")

    @cached_property
    def value(self):  # pragma: no cover
        return MetricValueOutput.make_one(self.boto3_raw_data["value"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricDatumTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetricDatumTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Allowed:
    boto3_raw_data: "type_defs.AllowedTypeDef" = dataclasses.field()

    @cached_property
    def policies(self):  # pragma: no cover
        return Policy.make_many(self.boto3_raw_data["policies"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AllowedTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AllowedTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExplicitDeny:
    boto3_raw_data: "type_defs.ExplicitDenyTypeDef" = dataclasses.field()

    @cached_property
    def policies(self):  # pragma: no cover
        return Policy.make_many(self.boto3_raw_data["policies"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExplicitDenyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExplicitDenyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImplicitDeny:
    boto3_raw_data: "type_defs.ImplicitDenyTypeDef" = dataclasses.field()

    @cached_property
    def policies(self):  # pragma: no cover
        return Policy.make_many(self.boto3_raw_data["policies"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImplicitDenyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ImplicitDenyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetPropertyValue:
    boto3_raw_data: "type_defs.AssetPropertyValueTypeDef" = dataclasses.field()

    @cached_property
    def value(self):  # pragma: no cover
        return AssetPropertyVariant.make_one(self.boto3_raw_data["value"])

    @cached_property
    def timestamp(self):  # pragma: no cover
        return AssetPropertyTimestamp.make_one(self.boto3_raw_data["timestamp"])

    quality = field("quality")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssetPropertyValueTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssetPropertyValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateTargetsWithJobResponse:
    boto3_raw_data: "type_defs.AssociateTargetsWithJobResponseTypeDef" = (
        dataclasses.field()
    )

    jobArn = field("jobArn")
    jobId = field("jobId")
    description = field("description")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssociateTargetsWithJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateTargetsWithJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelJobResponse:
    boto3_raw_data: "type_defs.CancelJobResponseTypeDef" = dataclasses.field()

    jobArn = field("jobArn")
    jobId = field("jobId")
    description = field("description")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CancelJobResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAuthorizerResponse:
    boto3_raw_data: "type_defs.CreateAuthorizerResponseTypeDef" = dataclasses.field()

    authorizerName = field("authorizerName")
    authorizerArn = field("authorizerArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAuthorizerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAuthorizerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBillingGroupResponse:
    boto3_raw_data: "type_defs.CreateBillingGroupResponseTypeDef" = dataclasses.field()

    billingGroupName = field("billingGroupName")
    billingGroupArn = field("billingGroupArn")
    billingGroupId = field("billingGroupId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBillingGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBillingGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCertificateFromCsrResponse:
    boto3_raw_data: "type_defs.CreateCertificateFromCsrResponseTypeDef" = (
        dataclasses.field()
    )

    certificateArn = field("certificateArn")
    certificateId = field("certificateId")
    certificatePem = field("certificatePem")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateCertificateFromCsrResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCertificateFromCsrResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCertificateProviderResponse:
    boto3_raw_data: "type_defs.CreateCertificateProviderResponseTypeDef" = (
        dataclasses.field()
    )

    certificateProviderName = field("certificateProviderName")
    certificateProviderArn = field("certificateProviderArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateCertificateProviderResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCertificateProviderResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCommandResponse:
    boto3_raw_data: "type_defs.CreateCommandResponseTypeDef" = dataclasses.field()

    commandId = field("commandId")
    commandArn = field("commandArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCommandResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCommandResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCustomMetricResponse:
    boto3_raw_data: "type_defs.CreateCustomMetricResponseTypeDef" = dataclasses.field()

    metricName = field("metricName")
    metricArn = field("metricArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCustomMetricResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCustomMetricResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDimensionResponse:
    boto3_raw_data: "type_defs.CreateDimensionResponseTypeDef" = dataclasses.field()

    name = field("name")
    arn = field("arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDimensionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDimensionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDomainConfigurationResponse:
    boto3_raw_data: "type_defs.CreateDomainConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    domainConfigurationName = field("domainConfigurationName")
    domainConfigurationArn = field("domainConfigurationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateDomainConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDomainConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDynamicThingGroupResponse:
    boto3_raw_data: "type_defs.CreateDynamicThingGroupResponseTypeDef" = (
        dataclasses.field()
    )

    thingGroupName = field("thingGroupName")
    thingGroupArn = field("thingGroupArn")
    thingGroupId = field("thingGroupId")
    indexName = field("indexName")
    queryString = field("queryString")
    queryVersion = field("queryVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateDynamicThingGroupResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDynamicThingGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFleetMetricResponse:
    boto3_raw_data: "type_defs.CreateFleetMetricResponseTypeDef" = dataclasses.field()

    metricName = field("metricName")
    metricArn = field("metricArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFleetMetricResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFleetMetricResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateJobResponse:
    boto3_raw_data: "type_defs.CreateJobResponseTypeDef" = dataclasses.field()

    jobArn = field("jobArn")
    jobId = field("jobId")
    description = field("description")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateJobResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateJobTemplateResponse:
    boto3_raw_data: "type_defs.CreateJobTemplateResponseTypeDef" = dataclasses.field()

    jobTemplateArn = field("jobTemplateArn")
    jobTemplateId = field("jobTemplateId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateJobTemplateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateJobTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMitigationActionResponse:
    boto3_raw_data: "type_defs.CreateMitigationActionResponseTypeDef" = (
        dataclasses.field()
    )

    actionArn = field("actionArn")
    actionId = field("actionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateMitigationActionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMitigationActionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateOTAUpdateResponse:
    boto3_raw_data: "type_defs.CreateOTAUpdateResponseTypeDef" = dataclasses.field()

    otaUpdateId = field("otaUpdateId")
    awsIotJobId = field("awsIotJobId")
    otaUpdateArn = field("otaUpdateArn")
    awsIotJobArn = field("awsIotJobArn")
    otaUpdateStatus = field("otaUpdateStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateOTAUpdateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateOTAUpdateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePackageResponse:
    boto3_raw_data: "type_defs.CreatePackageResponseTypeDef" = dataclasses.field()

    packageName = field("packageName")
    packageArn = field("packageArn")
    description = field("description")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePackageResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePackageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePackageVersionResponse:
    boto3_raw_data: "type_defs.CreatePackageVersionResponseTypeDef" = (
        dataclasses.field()
    )

    packageVersionArn = field("packageVersionArn")
    packageName = field("packageName")
    versionName = field("versionName")
    description = field("description")
    attributes = field("attributes")
    status = field("status")
    errorReason = field("errorReason")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePackageVersionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePackageVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePolicyResponse:
    boto3_raw_data: "type_defs.CreatePolicyResponseTypeDef" = dataclasses.field()

    policyName = field("policyName")
    policyArn = field("policyArn")
    policyDocument = field("policyDocument")
    policyVersionId = field("policyVersionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePolicyVersionResponse:
    boto3_raw_data: "type_defs.CreatePolicyVersionResponseTypeDef" = dataclasses.field()

    policyArn = field("policyArn")
    policyDocument = field("policyDocument")
    policyVersionId = field("policyVersionId")
    isDefaultVersion = field("isDefaultVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePolicyVersionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePolicyVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateProvisioningTemplateResponse:
    boto3_raw_data: "type_defs.CreateProvisioningTemplateResponseTypeDef" = (
        dataclasses.field()
    )

    templateArn = field("templateArn")
    templateName = field("templateName")
    defaultVersionId = field("defaultVersionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateProvisioningTemplateResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateProvisioningTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateProvisioningTemplateVersionResponse:
    boto3_raw_data: "type_defs.CreateProvisioningTemplateVersionResponseTypeDef" = (
        dataclasses.field()
    )

    templateArn = field("templateArn")
    templateName = field("templateName")
    versionId = field("versionId")
    isDefaultVersion = field("isDefaultVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateProvisioningTemplateVersionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateProvisioningTemplateVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRoleAliasResponse:
    boto3_raw_data: "type_defs.CreateRoleAliasResponseTypeDef" = dataclasses.field()

    roleAlias = field("roleAlias")
    roleAliasArn = field("roleAliasArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRoleAliasResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRoleAliasResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateScheduledAuditResponse:
    boto3_raw_data: "type_defs.CreateScheduledAuditResponseTypeDef" = (
        dataclasses.field()
    )

    scheduledAuditArn = field("scheduledAuditArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateScheduledAuditResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateScheduledAuditResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSecurityProfileResponse:
    boto3_raw_data: "type_defs.CreateSecurityProfileResponseTypeDef" = (
        dataclasses.field()
    )

    securityProfileName = field("securityProfileName")
    securityProfileArn = field("securityProfileArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateSecurityProfileResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSecurityProfileResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateStreamResponse:
    boto3_raw_data: "type_defs.CreateStreamResponseTypeDef" = dataclasses.field()

    streamId = field("streamId")
    streamArn = field("streamArn")
    description = field("description")
    streamVersion = field("streamVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateStreamResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateStreamResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateThingGroupResponse:
    boto3_raw_data: "type_defs.CreateThingGroupResponseTypeDef" = dataclasses.field()

    thingGroupName = field("thingGroupName")
    thingGroupArn = field("thingGroupArn")
    thingGroupId = field("thingGroupId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateThingGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateThingGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateThingResponse:
    boto3_raw_data: "type_defs.CreateThingResponseTypeDef" = dataclasses.field()

    thingName = field("thingName")
    thingArn = field("thingArn")
    thingId = field("thingId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateThingResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateThingResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateThingTypeResponse:
    boto3_raw_data: "type_defs.CreateThingTypeResponseTypeDef" = dataclasses.field()

    thingTypeName = field("thingTypeName")
    thingTypeArn = field("thingTypeArn")
    thingTypeId = field("thingTypeId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateThingTypeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateThingTypeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCommandResponse:
    boto3_raw_data: "type_defs.DeleteCommandResponseTypeDef" = dataclasses.field()

    statusCode = field("statusCode")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteCommandResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCommandResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCertificateProviderResponse:
    boto3_raw_data: "type_defs.DescribeCertificateProviderResponseTypeDef" = (
        dataclasses.field()
    )

    certificateProviderName = field("certificateProviderName")
    certificateProviderArn = field("certificateProviderArn")
    lambdaFunctionArn = field("lambdaFunctionArn")
    accountDefaultForOperations = field("accountDefaultForOperations")
    creationDate = field("creationDate")
    lastModifiedDate = field("lastModifiedDate")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeCertificateProviderResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCertificateProviderResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCustomMetricResponse:
    boto3_raw_data: "type_defs.DescribeCustomMetricResponseTypeDef" = (
        dataclasses.field()
    )

    metricName = field("metricName")
    metricArn = field("metricArn")
    metricType = field("metricType")
    displayName = field("displayName")
    creationDate = field("creationDate")
    lastModifiedDate = field("lastModifiedDate")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeCustomMetricResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCustomMetricResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDimensionResponse:
    boto3_raw_data: "type_defs.DescribeDimensionResponseTypeDef" = dataclasses.field()

    name = field("name")
    arn = field("arn")
    type = field("type")
    stringValues = field("stringValues")
    creationDate = field("creationDate")
    lastModifiedDate = field("lastModifiedDate")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDimensionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDimensionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEndpointResponse:
    boto3_raw_data: "type_defs.DescribeEndpointResponseTypeDef" = dataclasses.field()

    endpointAddress = field("endpointAddress")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEndpointResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFleetMetricResponse:
    boto3_raw_data: "type_defs.DescribeFleetMetricResponseTypeDef" = dataclasses.field()

    metricName = field("metricName")
    queryString = field("queryString")

    @cached_property
    def aggregationType(self):  # pragma: no cover
        return AggregationTypeOutput.make_one(self.boto3_raw_data["aggregationType"])

    period = field("period")
    aggregationField = field("aggregationField")
    description = field("description")
    queryVersion = field("queryVersion")
    indexName = field("indexName")
    creationDate = field("creationDate")
    lastModifiedDate = field("lastModifiedDate")
    unit = field("unit")
    version = field("version")
    metricArn = field("metricArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeFleetMetricResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFleetMetricResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeIndexResponse:
    boto3_raw_data: "type_defs.DescribeIndexResponseTypeDef" = dataclasses.field()

    indexName = field("indexName")
    indexStatus = field("indexStatus")
    schema = field("schema")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeIndexResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeIndexResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeProvisioningTemplateVersionResponse:
    boto3_raw_data: "type_defs.DescribeProvisioningTemplateVersionResponseTypeDef" = (
        dataclasses.field()
    )

    versionId = field("versionId")
    creationDate = field("creationDate")
    templateBody = field("templateBody")
    isDefaultVersion = field("isDefaultVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeProvisioningTemplateVersionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeProvisioningTemplateVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeScheduledAuditResponse:
    boto3_raw_data: "type_defs.DescribeScheduledAuditResponseTypeDef" = (
        dataclasses.field()
    )

    frequency = field("frequency")
    dayOfMonth = field("dayOfMonth")
    dayOfWeek = field("dayOfWeek")
    targetCheckNames = field("targetCheckNames")
    scheduledAuditName = field("scheduledAuditName")
    scheduledAuditArn = field("scheduledAuditArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeScheduledAuditResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeScheduledAuditResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeThingRegistrationTaskResponse:
    boto3_raw_data: "type_defs.DescribeThingRegistrationTaskResponseTypeDef" = (
        dataclasses.field()
    )

    taskId = field("taskId")
    creationDate = field("creationDate")
    lastModifiedDate = field("lastModifiedDate")
    templateBody = field("templateBody")
    inputFileBucket = field("inputFileBucket")
    inputFileKey = field("inputFileKey")
    roleArn = field("roleArn")
    status = field("status")
    message = field("message")
    successCount = field("successCount")
    failureCount = field("failureCount")
    percentageProgress = field("percentageProgress")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeThingRegistrationTaskResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeThingRegistrationTaskResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeThingResponse:
    boto3_raw_data: "type_defs.DescribeThingResponseTypeDef" = dataclasses.field()

    defaultClientId = field("defaultClientId")
    thingName = field("thingName")
    thingId = field("thingId")
    thingArn = field("thingArn")
    thingTypeName = field("thingTypeName")
    attributes = field("attributes")
    version = field("version")
    billingGroupName = field("billingGroupName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeThingResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeThingResponseTypeDef"]
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
class GetCardinalityResponse:
    boto3_raw_data: "type_defs.GetCardinalityResponseTypeDef" = dataclasses.field()

    cardinality = field("cardinality")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCardinalityResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCardinalityResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetJobDocumentResponse:
    boto3_raw_data: "type_defs.GetJobDocumentResponseTypeDef" = dataclasses.field()

    document = field("document")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetJobDocumentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetJobDocumentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLoggingOptionsResponse:
    boto3_raw_data: "type_defs.GetLoggingOptionsResponseTypeDef" = dataclasses.field()

    roleArn = field("roleArn")
    logLevel = field("logLevel")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLoggingOptionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLoggingOptionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPackageResponse:
    boto3_raw_data: "type_defs.GetPackageResponseTypeDef" = dataclasses.field()

    packageName = field("packageName")
    packageArn = field("packageArn")
    description = field("description")
    defaultVersionName = field("defaultVersionName")
    creationDate = field("creationDate")
    lastModifiedDate = field("lastModifiedDate")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPackageResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPackageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPolicyResponse:
    boto3_raw_data: "type_defs.GetPolicyResponseTypeDef" = dataclasses.field()

    policyName = field("policyName")
    policyArn = field("policyArn")
    policyDocument = field("policyDocument")
    defaultVersionId = field("defaultVersionId")
    creationDate = field("creationDate")
    lastModifiedDate = field("lastModifiedDate")
    generationId = field("generationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetPolicyResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPolicyVersionResponse:
    boto3_raw_data: "type_defs.GetPolicyVersionResponseTypeDef" = dataclasses.field()

    policyArn = field("policyArn")
    policyName = field("policyName")
    policyDocument = field("policyDocument")
    policyVersionId = field("policyVersionId")
    isDefaultVersion = field("isDefaultVersion")
    creationDate = field("creationDate")
    lastModifiedDate = field("lastModifiedDate")
    generationId = field("generationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPolicyVersionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPolicyVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRegistrationCodeResponse:
    boto3_raw_data: "type_defs.GetRegistrationCodeResponseTypeDef" = dataclasses.field()

    registrationCode = field("registrationCode")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRegistrationCodeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRegistrationCodeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetThingConnectivityDataResponse:
    boto3_raw_data: "type_defs.GetThingConnectivityDataResponseTypeDef" = (
        dataclasses.field()
    )

    thingName = field("thingName")
    connected = field("connected")
    timestamp = field("timestamp")
    disconnectReason = field("disconnectReason")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetThingConnectivityDataResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetThingConnectivityDataResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetV2LoggingOptionsResponse:
    boto3_raw_data: "type_defs.GetV2LoggingOptionsResponseTypeDef" = dataclasses.field()

    roleArn = field("roleArn")
    defaultLogLevel = field("defaultLogLevel")
    disableAllLogs = field("disableAllLogs")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetV2LoggingOptionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetV2LoggingOptionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAttachedPoliciesResponse:
    boto3_raw_data: "type_defs.ListAttachedPoliciesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def policies(self):  # pragma: no cover
        return Policy.make_many(self.boto3_raw_data["policies"])

    nextMarker = field("nextMarker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAttachedPoliciesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAttachedPoliciesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCustomMetricsResponse:
    boto3_raw_data: "type_defs.ListCustomMetricsResponseTypeDef" = dataclasses.field()

    metricNames = field("metricNames")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCustomMetricsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCustomMetricsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDimensionsResponse:
    boto3_raw_data: "type_defs.ListDimensionsResponseTypeDef" = dataclasses.field()

    dimensionNames = field("dimensionNames")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDimensionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDimensionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIndicesResponse:
    boto3_raw_data: "type_defs.ListIndicesResponseTypeDef" = dataclasses.field()

    indexNames = field("indexNames")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIndicesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIndicesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPoliciesResponse:
    boto3_raw_data: "type_defs.ListPoliciesResponseTypeDef" = dataclasses.field()

    @cached_property
    def policies(self):  # pragma: no cover
        return Policy.make_many(self.boto3_raw_data["policies"])

    nextMarker = field("nextMarker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPoliciesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPoliciesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPolicyPrincipalsResponse:
    boto3_raw_data: "type_defs.ListPolicyPrincipalsResponseTypeDef" = (
        dataclasses.field()
    )

    principals = field("principals")
    nextMarker = field("nextMarker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPolicyPrincipalsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPolicyPrincipalsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPrincipalPoliciesResponse:
    boto3_raw_data: "type_defs.ListPrincipalPoliciesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def policies(self):  # pragma: no cover
        return Policy.make_many(self.boto3_raw_data["policies"])

    nextMarker = field("nextMarker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListPrincipalPoliciesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPrincipalPoliciesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPrincipalThingsResponse:
    boto3_raw_data: "type_defs.ListPrincipalThingsResponseTypeDef" = dataclasses.field()

    things = field("things")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPrincipalThingsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPrincipalThingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRoleAliasesResponse:
    boto3_raw_data: "type_defs.ListRoleAliasesResponseTypeDef" = dataclasses.field()

    roleAliases = field("roleAliases")
    nextMarker = field("nextMarker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRoleAliasesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRoleAliasesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTargetsForPolicyResponse:
    boto3_raw_data: "type_defs.ListTargetsForPolicyResponseTypeDef" = (
        dataclasses.field()
    )

    targets = field("targets")
    nextMarker = field("nextMarker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTargetsForPolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTargetsForPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListThingPrincipalsResponse:
    boto3_raw_data: "type_defs.ListThingPrincipalsResponseTypeDef" = dataclasses.field()

    principals = field("principals")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListThingPrincipalsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListThingPrincipalsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListThingRegistrationTaskReportsResponse:
    boto3_raw_data: "type_defs.ListThingRegistrationTaskReportsResponseTypeDef" = (
        dataclasses.field()
    )

    resourceLinks = field("resourceLinks")
    reportType = field("reportType")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListThingRegistrationTaskReportsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListThingRegistrationTaskReportsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListThingRegistrationTasksResponse:
    boto3_raw_data: "type_defs.ListThingRegistrationTasksResponseTypeDef" = (
        dataclasses.field()
    )

    taskIds = field("taskIds")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListThingRegistrationTasksResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListThingRegistrationTasksResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListThingsInBillingGroupResponse:
    boto3_raw_data: "type_defs.ListThingsInBillingGroupResponseTypeDef" = (
        dataclasses.field()
    )

    things = field("things")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListThingsInBillingGroupResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListThingsInBillingGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListThingsInThingGroupResponse:
    boto3_raw_data: "type_defs.ListThingsInThingGroupResponseTypeDef" = (
        dataclasses.field()
    )

    things = field("things")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListThingsInThingGroupResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListThingsInThingGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterCACertificateResponse:
    boto3_raw_data: "type_defs.RegisterCACertificateResponseTypeDef" = (
        dataclasses.field()
    )

    certificateArn = field("certificateArn")
    certificateId = field("certificateId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RegisterCACertificateResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterCACertificateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterCertificateResponse:
    boto3_raw_data: "type_defs.RegisterCertificateResponseTypeDef" = dataclasses.field()

    certificateArn = field("certificateArn")
    certificateId = field("certificateId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterCertificateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterCertificateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterCertificateWithoutCAResponse:
    boto3_raw_data: "type_defs.RegisterCertificateWithoutCAResponseTypeDef" = (
        dataclasses.field()
    )

    certificateArn = field("certificateArn")
    certificateId = field("certificateId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RegisterCertificateWithoutCAResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterCertificateWithoutCAResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterThingResponse:
    boto3_raw_data: "type_defs.RegisterThingResponseTypeDef" = dataclasses.field()

    certificatePem = field("certificatePem")
    resourceArns = field("resourceArns")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterThingResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterThingResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetDefaultAuthorizerResponse:
    boto3_raw_data: "type_defs.SetDefaultAuthorizerResponseTypeDef" = (
        dataclasses.field()
    )

    authorizerName = field("authorizerName")
    authorizerArn = field("authorizerArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SetDefaultAuthorizerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetDefaultAuthorizerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartAuditMitigationActionsTaskResponse:
    boto3_raw_data: "type_defs.StartAuditMitigationActionsTaskResponseTypeDef" = (
        dataclasses.field()
    )

    taskId = field("taskId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartAuditMitigationActionsTaskResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartAuditMitigationActionsTaskResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartDetectMitigationActionsTaskResponse:
    boto3_raw_data: "type_defs.StartDetectMitigationActionsTaskResponseTypeDef" = (
        dataclasses.field()
    )

    taskId = field("taskId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartDetectMitigationActionsTaskResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartDetectMitigationActionsTaskResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartOnDemandAuditTaskResponse:
    boto3_raw_data: "type_defs.StartOnDemandAuditTaskResponseTypeDef" = (
        dataclasses.field()
    )

    taskId = field("taskId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartOnDemandAuditTaskResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartOnDemandAuditTaskResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartThingRegistrationTaskResponse:
    boto3_raw_data: "type_defs.StartThingRegistrationTaskResponseTypeDef" = (
        dataclasses.field()
    )

    taskId = field("taskId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartThingRegistrationTaskResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartThingRegistrationTaskResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestInvokeAuthorizerResponse:
    boto3_raw_data: "type_defs.TestInvokeAuthorizerResponseTypeDef" = (
        dataclasses.field()
    )

    isAuthenticated = field("isAuthenticated")
    principalId = field("principalId")
    policyDocuments = field("policyDocuments")
    refreshAfterInSeconds = field("refreshAfterInSeconds")
    disconnectAfterInSeconds = field("disconnectAfterInSeconds")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestInvokeAuthorizerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestInvokeAuthorizerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TransferCertificateResponse:
    boto3_raw_data: "type_defs.TransferCertificateResponseTypeDef" = dataclasses.field()

    transferredCertificateArn = field("transferredCertificateArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TransferCertificateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TransferCertificateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAuthorizerResponse:
    boto3_raw_data: "type_defs.UpdateAuthorizerResponseTypeDef" = dataclasses.field()

    authorizerName = field("authorizerName")
    authorizerArn = field("authorizerArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAuthorizerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAuthorizerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBillingGroupResponse:
    boto3_raw_data: "type_defs.UpdateBillingGroupResponseTypeDef" = dataclasses.field()

    version = field("version")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBillingGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBillingGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCertificateProviderResponse:
    boto3_raw_data: "type_defs.UpdateCertificateProviderResponseTypeDef" = (
        dataclasses.field()
    )

    certificateProviderName = field("certificateProviderName")
    certificateProviderArn = field("certificateProviderArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateCertificateProviderResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCertificateProviderResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCommandResponse:
    boto3_raw_data: "type_defs.UpdateCommandResponseTypeDef" = dataclasses.field()

    commandId = field("commandId")
    displayName = field("displayName")
    description = field("description")
    deprecated = field("deprecated")
    lastUpdatedAt = field("lastUpdatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateCommandResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCommandResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCustomMetricResponse:
    boto3_raw_data: "type_defs.UpdateCustomMetricResponseTypeDef" = dataclasses.field()

    metricName = field("metricName")
    metricArn = field("metricArn")
    metricType = field("metricType")
    displayName = field("displayName")
    creationDate = field("creationDate")
    lastModifiedDate = field("lastModifiedDate")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateCustomMetricResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCustomMetricResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDimensionResponse:
    boto3_raw_data: "type_defs.UpdateDimensionResponseTypeDef" = dataclasses.field()

    name = field("name")
    arn = field("arn")
    type = field("type")
    stringValues = field("stringValues")
    creationDate = field("creationDate")
    lastModifiedDate = field("lastModifiedDate")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDimensionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDimensionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDomainConfigurationResponse:
    boto3_raw_data: "type_defs.UpdateDomainConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    domainConfigurationName = field("domainConfigurationName")
    domainConfigurationArn = field("domainConfigurationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateDomainConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDomainConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDynamicThingGroupResponse:
    boto3_raw_data: "type_defs.UpdateDynamicThingGroupResponseTypeDef" = (
        dataclasses.field()
    )

    version = field("version")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateDynamicThingGroupResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDynamicThingGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMitigationActionResponse:
    boto3_raw_data: "type_defs.UpdateMitigationActionResponseTypeDef" = (
        dataclasses.field()
    )

    actionArn = field("actionArn")
    actionId = field("actionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateMitigationActionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMitigationActionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRoleAliasResponse:
    boto3_raw_data: "type_defs.UpdateRoleAliasResponseTypeDef" = dataclasses.field()

    roleAlias = field("roleAlias")
    roleAliasArn = field("roleAliasArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateRoleAliasResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRoleAliasResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateScheduledAuditResponse:
    boto3_raw_data: "type_defs.UpdateScheduledAuditResponseTypeDef" = (
        dataclasses.field()
    )

    scheduledAuditArn = field("scheduledAuditArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateScheduledAuditResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateScheduledAuditResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateStreamResponse:
    boto3_raw_data: "type_defs.UpdateStreamResponseTypeDef" = dataclasses.field()

    streamId = field("streamId")
    streamArn = field("streamArn")
    description = field("description")
    streamVersion = field("streamVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateStreamResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateStreamResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateThingGroupResponse:
    boto3_raw_data: "type_defs.UpdateThingGroupResponseTypeDef" = dataclasses.field()

    version = field("version")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateThingGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateThingGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ThingGroupPropertiesOutput:
    boto3_raw_data: "type_defs.ThingGroupPropertiesOutputTypeDef" = dataclasses.field()

    thingGroupDescription = field("thingGroupDescription")

    @cached_property
    def attributePayload(self):  # pragma: no cover
        return AttributePayloadOutput.make_one(self.boto3_raw_data["attributePayload"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ThingGroupPropertiesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ThingGroupPropertiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ThingGroupProperties:
    boto3_raw_data: "type_defs.ThingGroupPropertiesTypeDef" = dataclasses.field()

    thingGroupDescription = field("thingGroupDescription")

    @cached_property
    def attributePayload(self):  # pragma: no cover
        return AttributePayload.make_one(self.boto3_raw_data["attributePayload"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ThingGroupPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ThingGroupPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAuditMitigationActionsExecutionsResponse:
    boto3_raw_data: "type_defs.ListAuditMitigationActionsExecutionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def actionsExecutions(self):  # pragma: no cover
        return AuditMitigationActionExecutionMetadata.make_many(
            self.boto3_raw_data["actionsExecutions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAuditMitigationActionsExecutionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAuditMitigationActionsExecutionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAuditMitigationActionsTasksResponse:
    boto3_raw_data: "type_defs.ListAuditMitigationActionsTasksResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def tasks(self):  # pragma: no cover
        return AuditMitigationActionsTaskMetadata.make_many(
            self.boto3_raw_data["tasks"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAuditMitigationActionsTasksResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAuditMitigationActionsTasksResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAccountAuditConfigurationResponse:
    boto3_raw_data: "type_defs.DescribeAccountAuditConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    roleArn = field("roleArn")
    auditNotificationTargetConfigurations = field(
        "auditNotificationTargetConfigurations"
    )
    auditCheckConfigurations = field("auditCheckConfigurations")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAccountAuditConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAccountAuditConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAuditTasksResponse:
    boto3_raw_data: "type_defs.ListAuditTasksResponseTypeDef" = dataclasses.field()

    @cached_property
    def tasks(self):  # pragma: no cover
        return AuditTaskMetadata.make_many(self.boto3_raw_data["tasks"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAuditTasksResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAuditTasksResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAuthorizerResponse:
    boto3_raw_data: "type_defs.DescribeAuthorizerResponseTypeDef" = dataclasses.field()

    @cached_property
    def authorizerDescription(self):  # pragma: no cover
        return AuthorizerDescription.make_one(
            self.boto3_raw_data["authorizerDescription"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAuthorizerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAuthorizerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDefaultAuthorizerResponse:
    boto3_raw_data: "type_defs.DescribeDefaultAuthorizerResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def authorizerDescription(self):  # pragma: no cover
        return AuthorizerDescription.make_one(
            self.boto3_raw_data["authorizerDescription"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDefaultAuthorizerResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDefaultAuthorizerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAuthorizersResponse:
    boto3_raw_data: "type_defs.ListAuthorizersResponseTypeDef" = dataclasses.field()

    @cached_property
    def authorizers(self):  # pragma: no cover
        return AuthorizerSummary.make_many(self.boto3_raw_data["authorizers"])

    nextMarker = field("nextMarker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAuthorizersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAuthorizersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AwsJobAbortConfig:
    boto3_raw_data: "type_defs.AwsJobAbortConfigTypeDef" = dataclasses.field()

    @cached_property
    def abortCriteriaList(self):  # pragma: no cover
        return AwsJobAbortCriteria.make_many(self.boto3_raw_data["abortCriteriaList"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AwsJobAbortConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AwsJobAbortConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AwsJobExponentialRolloutRate:
    boto3_raw_data: "type_defs.AwsJobExponentialRolloutRateTypeDef" = (
        dataclasses.field()
    )

    baseRatePerMinute = field("baseRatePerMinute")
    incrementFactor = field("incrementFactor")

    @cached_property
    def rateIncreaseCriteria(self):  # pragma: no cover
        return AwsJobRateIncreaseCriteria.make_one(
            self.boto3_raw_data["rateIncreaseCriteria"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AwsJobExponentialRolloutRateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AwsJobExponentialRolloutRateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BehaviorCriteriaOutput:
    boto3_raw_data: "type_defs.BehaviorCriteriaOutputTypeDef" = dataclasses.field()

    comparisonOperator = field("comparisonOperator")

    @cached_property
    def value(self):  # pragma: no cover
        return MetricValueOutput.make_one(self.boto3_raw_data["value"])

    durationSeconds = field("durationSeconds")
    consecutiveDatapointsToAlarm = field("consecutiveDatapointsToAlarm")
    consecutiveDatapointsToClear = field("consecutiveDatapointsToClear")

    @cached_property
    def statisticalThreshold(self):  # pragma: no cover
        return StatisticalThreshold.make_one(
            self.boto3_raw_data["statisticalThreshold"]
        )

    @cached_property
    def mlDetectionConfig(self):  # pragma: no cover
        return MachineLearningDetectionConfig.make_one(
            self.boto3_raw_data["mlDetectionConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BehaviorCriteriaOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BehaviorCriteriaOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBehaviorModelTrainingSummariesResponse:
    boto3_raw_data: "type_defs.GetBehaviorModelTrainingSummariesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def summaries(self):  # pragma: no cover
        return BehaviorModelTrainingSummary.make_many(self.boto3_raw_data["summaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetBehaviorModelTrainingSummariesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBehaviorModelTrainingSummariesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricToRetain:
    boto3_raw_data: "type_defs.MetricToRetainTypeDef" = dataclasses.field()

    metric = field("metric")

    @cached_property
    def metricDimension(self):  # pragma: no cover
        return MetricDimension.make_one(self.boto3_raw_data["metricDimension"])

    exportMetric = field("exportMetric")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricToRetainTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetricToRetainTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBillingGroupResponse:
    boto3_raw_data: "type_defs.DescribeBillingGroupResponseTypeDef" = (
        dataclasses.field()
    )

    billingGroupName = field("billingGroupName")
    billingGroupId = field("billingGroupId")
    billingGroupArn = field("billingGroupArn")
    version = field("version")

    @cached_property
    def billingGroupProperties(self):  # pragma: no cover
        return BillingGroupProperties.make_one(
            self.boto3_raw_data["billingGroupProperties"]
        )

    @cached_property
    def billingGroupMetadata(self):  # pragma: no cover
        return BillingGroupMetadata.make_one(
            self.boto3_raw_data["billingGroupMetadata"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeBillingGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBillingGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBillingGroupRequest:
    boto3_raw_data: "type_defs.UpdateBillingGroupRequestTypeDef" = dataclasses.field()

    billingGroupName = field("billingGroupName")

    @cached_property
    def billingGroupProperties(self):  # pragma: no cover
        return BillingGroupProperties.make_one(
            self.boto3_raw_data["billingGroupProperties"]
        )

    expectedVersion = field("expectedVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBillingGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBillingGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodeSigningSignature:
    boto3_raw_data: "type_defs.CodeSigningSignatureTypeDef" = dataclasses.field()

    inlineDocument = field("inlineDocument")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CodeSigningSignatureTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodeSigningSignatureTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CommandParameterValue:
    boto3_raw_data: "type_defs.CommandParameterValueTypeDef" = dataclasses.field()

    S = field("S")
    B = field("B")
    I = field("I")
    L = field("L")
    D = field("D")
    BIN = field("BIN")
    UL = field("UL")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CommandParameterValueTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CommandParameterValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CommandPayload:
    boto3_raw_data: "type_defs.CommandPayloadTypeDef" = dataclasses.field()

    content = field("content")
    contentType = field("contentType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CommandPayloadTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CommandPayloadTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MqttContext:
    boto3_raw_data: "type_defs.MqttContextTypeDef" = dataclasses.field()

    username = field("username")
    password = field("password")
    clientId = field("clientId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MqttContextTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MqttContextTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketsAggregationResponse:
    boto3_raw_data: "type_defs.GetBucketsAggregationResponseTypeDef" = (
        dataclasses.field()
    )

    totalCount = field("totalCount")

    @cached_property
    def buckets(self):  # pragma: no cover
        return Bucket.make_many(self.boto3_raw_data["buckets"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetBucketsAggregationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketsAggregationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BucketsAggregationType:
    boto3_raw_data: "type_defs.BucketsAggregationTypeTypeDef" = dataclasses.field()

    @cached_property
    def termsAggregation(self):  # pragma: no cover
        return TermsAggregation.make_one(self.boto3_raw_data["termsAggregation"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BucketsAggregationTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BucketsAggregationTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CACertificateDescription:
    boto3_raw_data: "type_defs.CACertificateDescriptionTypeDef" = dataclasses.field()

    certificateArn = field("certificateArn")
    certificateId = field("certificateId")
    status = field("status")
    certificatePem = field("certificatePem")
    ownedBy = field("ownedBy")
    creationDate = field("creationDate")
    autoRegistrationStatus = field("autoRegistrationStatus")
    lastModifiedDate = field("lastModifiedDate")
    customerVersion = field("customerVersion")
    generationId = field("generationId")

    @cached_property
    def validity(self):  # pragma: no cover
        return CertificateValidity.make_one(self.boto3_raw_data["validity"])

    certificateMode = field("certificateMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CACertificateDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CACertificateDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCACertificatesResponse:
    boto3_raw_data: "type_defs.ListCACertificatesResponseTypeDef" = dataclasses.field()

    @cached_property
    def certificates(self):  # pragma: no cover
        return CACertificate.make_many(self.boto3_raw_data["certificates"])

    nextMarker = field("nextMarker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCACertificatesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCACertificatesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CertificateDescription:
    boto3_raw_data: "type_defs.CertificateDescriptionTypeDef" = dataclasses.field()

    certificateArn = field("certificateArn")
    certificateId = field("certificateId")
    caCertificateId = field("caCertificateId")
    status = field("status")
    certificatePem = field("certificatePem")
    ownedBy = field("ownedBy")
    previousOwnedBy = field("previousOwnedBy")
    creationDate = field("creationDate")
    lastModifiedDate = field("lastModifiedDate")
    customerVersion = field("customerVersion")

    @cached_property
    def transferData(self):  # pragma: no cover
        return TransferData.make_one(self.boto3_raw_data["transferData"])

    generationId = field("generationId")

    @cached_property
    def validity(self):  # pragma: no cover
        return CertificateValidity.make_one(self.boto3_raw_data["validity"])

    certificateMode = field("certificateMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CertificateDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CertificateDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCertificateProvidersResponse:
    boto3_raw_data: "type_defs.ListCertificateProvidersResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def certificateProviders(self):  # pragma: no cover
        return CertificateProviderSummary.make_many(
            self.boto3_raw_data["certificateProviders"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListCertificateProvidersResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCertificateProvidersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCertificatesByCAResponse:
    boto3_raw_data: "type_defs.ListCertificatesByCAResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def certificates(self):  # pragma: no cover
        return Certificate.make_many(self.boto3_raw_data["certificates"])

    nextMarker = field("nextMarker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCertificatesByCAResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCertificatesByCAResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCertificatesResponse:
    boto3_raw_data: "type_defs.ListCertificatesResponseTypeDef" = dataclasses.field()

    @cached_property
    def certificates(self):  # pragma: no cover
        return Certificate.make_many(self.boto3_raw_data["certificates"])

    nextMarker = field("nextMarker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCertificatesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCertificatesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomCodeSigningOutput:
    boto3_raw_data: "type_defs.CustomCodeSigningOutputTypeDef" = dataclasses.field()

    @cached_property
    def signature(self):  # pragma: no cover
        return CodeSigningSignatureOutput.make_one(self.boto3_raw_data["signature"])

    @cached_property
    def certificateChain(self):  # pragma: no cover
        return CodeSigningCertificateChain.make_one(
            self.boto3_raw_data["certificateChain"]
        )

    hashAlgorithm = field("hashAlgorithm")
    signatureAlgorithm = field("signatureAlgorithm")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomCodeSigningOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomCodeSigningOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCommandExecutionsResponse:
    boto3_raw_data: "type_defs.ListCommandExecutionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def commandExecutions(self):  # pragma: no cover
        return CommandExecutionSummary.make_many(
            self.boto3_raw_data["commandExecutions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListCommandExecutionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCommandExecutionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CommandParameterOutput:
    boto3_raw_data: "type_defs.CommandParameterOutputTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def value(self):  # pragma: no cover
        return CommandParameterValueOutput.make_one(self.boto3_raw_data["value"])

    @cached_property
    def defaultValue(self):  # pragma: no cover
        return CommandParameterValueOutput.make_one(self.boto3_raw_data["defaultValue"])

    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CommandParameterOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CommandParameterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCommandsResponse:
    boto3_raw_data: "type_defs.ListCommandsResponseTypeDef" = dataclasses.field()

    @cached_property
    def commands(self):  # pragma: no cover
        return CommandSummary.make_many(self.boto3_raw_data["commands"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCommandsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCommandsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEncryptionConfigurationResponse:
    boto3_raw_data: "type_defs.DescribeEncryptionConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    encryptionType = field("encryptionType")
    kmsKeyArn = field("kmsKeyArn")
    kmsAccessRoleArn = field("kmsAccessRoleArn")

    @cached_property
    def configurationDetails(self):  # pragma: no cover
        return ConfigurationDetails.make_one(
            self.boto3_raw_data["configurationDetails"]
        )

    lastModifiedDate = field("lastModifiedDate")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEncryptionConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEncryptionConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEventConfigurationsResponse:
    boto3_raw_data: "type_defs.DescribeEventConfigurationsResponseTypeDef" = (
        dataclasses.field()
    )

    eventConfigurations = field("eventConfigurations")
    creationDate = field("creationDate")
    lastModifiedDate = field("lastModifiedDate")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEventConfigurationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEventConfigurationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEventConfigurationsRequest:
    boto3_raw_data: "type_defs.UpdateEventConfigurationsRequestTypeDef" = (
        dataclasses.field()
    )

    eventConfigurations = field("eventConfigurations")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateEventConfigurationsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEventConfigurationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAuditMitigationActionsTasksRequest:
    boto3_raw_data: "type_defs.ListAuditMitigationActionsTasksRequestTypeDef" = (
        dataclasses.field()
    )

    startTime = field("startTime")
    endTime = field("endTime")
    auditTaskId = field("auditTaskId")
    findingId = field("findingId")
    taskStatus = field("taskStatus")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAuditMitigationActionsTasksRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAuditMitigationActionsTasksRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAuditTasksRequest:
    boto3_raw_data: "type_defs.ListAuditTasksRequestTypeDef" = dataclasses.field()

    startTime = field("startTime")
    endTime = field("endTime")
    taskType = field("taskType")
    taskStatus = field("taskStatus")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAuditTasksRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAuditTasksRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDetectMitigationActionsExecutionsRequest:
    boto3_raw_data: "type_defs.ListDetectMitigationActionsExecutionsRequestTypeDef" = (
        dataclasses.field()
    )

    taskId = field("taskId")
    violationId = field("violationId")
    thingName = field("thingName")
    startTime = field("startTime")
    endTime = field("endTime")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDetectMitigationActionsExecutionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDetectMitigationActionsExecutionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDetectMitigationActionsTasksRequest:
    boto3_raw_data: "type_defs.ListDetectMitigationActionsTasksRequestTypeDef" = (
        dataclasses.field()
    )

    startTime = field("startTime")
    endTime = field("endTime")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDetectMitigationActionsTasksRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDetectMitigationActionsTasksRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMetricValuesRequest:
    boto3_raw_data: "type_defs.ListMetricValuesRequestTypeDef" = dataclasses.field()

    thingName = field("thingName")
    metricName = field("metricName")
    startTime = field("startTime")
    endTime = field("endTime")
    dimensionName = field("dimensionName")
    dimensionValueOperator = field("dimensionValueOperator")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMetricValuesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMetricValuesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListViolationEventsRequest:
    boto3_raw_data: "type_defs.ListViolationEventsRequestTypeDef" = dataclasses.field()

    startTime = field("startTime")
    endTime = field("endTime")
    thingName = field("thingName")
    securityProfileName = field("securityProfileName")
    behaviorCriteriaType = field("behaviorCriteriaType")
    listSuppressedAlerts = field("listSuppressedAlerts")
    verificationState = field("verificationState")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListViolationEventsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListViolationEventsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ViolationEventOccurrenceRange:
    boto3_raw_data: "type_defs.ViolationEventOccurrenceRangeTypeDef" = (
        dataclasses.field()
    )

    startTime = field("startTime")
    endTime = field("endTime")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ViolationEventOccurrenceRangeTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ViolationEventOccurrenceRangeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAuthorizerRequest:
    boto3_raw_data: "type_defs.CreateAuthorizerRequestTypeDef" = dataclasses.field()

    authorizerName = field("authorizerName")
    authorizerFunctionArn = field("authorizerFunctionArn")
    tokenKeyName = field("tokenKeyName")
    tokenSigningPublicKeys = field("tokenSigningPublicKeys")
    status = field("status")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    signingDisabled = field("signingDisabled")
    enableCachingForHttp = field("enableCachingForHttp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAuthorizerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAuthorizerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBillingGroupRequest:
    boto3_raw_data: "type_defs.CreateBillingGroupRequestTypeDef" = dataclasses.field()

    billingGroupName = field("billingGroupName")

    @cached_property
    def billingGroupProperties(self):  # pragma: no cover
        return BillingGroupProperties.make_one(
            self.boto3_raw_data["billingGroupProperties"]
        )

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBillingGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBillingGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCertificateProviderRequest:
    boto3_raw_data: "type_defs.CreateCertificateProviderRequestTypeDef" = (
        dataclasses.field()
    )

    certificateProviderName = field("certificateProviderName")
    lambdaFunctionArn = field("lambdaFunctionArn")
    accountDefaultForOperations = field("accountDefaultForOperations")
    clientToken = field("clientToken")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateCertificateProviderRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCertificateProviderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCustomMetricRequest:
    boto3_raw_data: "type_defs.CreateCustomMetricRequestTypeDef" = dataclasses.field()

    metricName = field("metricName")
    metricType = field("metricType")
    clientRequestToken = field("clientRequestToken")
    displayName = field("displayName")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCustomMetricRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCustomMetricRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDimensionRequest:
    boto3_raw_data: "type_defs.CreateDimensionRequestTypeDef" = dataclasses.field()

    name = field("name")
    type = field("type")
    stringValues = field("stringValues")
    clientRequestToken = field("clientRequestToken")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDimensionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDimensionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePolicyRequest:
    boto3_raw_data: "type_defs.CreatePolicyRequestTypeDef" = dataclasses.field()

    policyName = field("policyName")
    policyDocument = field("policyDocument")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRoleAliasRequest:
    boto3_raw_data: "type_defs.CreateRoleAliasRequestTypeDef" = dataclasses.field()

    roleAlias = field("roleAlias")
    roleArn = field("roleArn")
    credentialDurationSeconds = field("credentialDurationSeconds")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRoleAliasRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRoleAliasRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateScheduledAuditRequest:
    boto3_raw_data: "type_defs.CreateScheduledAuditRequestTypeDef" = dataclasses.field()

    frequency = field("frequency")
    targetCheckNames = field("targetCheckNames")
    scheduledAuditName = field("scheduledAuditName")
    dayOfMonth = field("dayOfMonth")
    dayOfWeek = field("dayOfWeek")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateScheduledAuditRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateScheduledAuditRequestTypeDef"]
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
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

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

    resourceArn = field("resourceArn")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

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
class CreateDomainConfigurationRequest:
    boto3_raw_data: "type_defs.CreateDomainConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    domainConfigurationName = field("domainConfigurationName")
    domainName = field("domainName")
    serverCertificateArns = field("serverCertificateArns")
    validationCertificateArn = field("validationCertificateArn")

    @cached_property
    def authorizerConfig(self):  # pragma: no cover
        return AuthorizerConfig.make_one(self.boto3_raw_data["authorizerConfig"])

    serviceType = field("serviceType")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @cached_property
    def tlsConfig(self):  # pragma: no cover
        return TlsConfig.make_one(self.boto3_raw_data["tlsConfig"])

    @cached_property
    def serverCertificateConfig(self):  # pragma: no cover
        return ServerCertificateConfig.make_one(
            self.boto3_raw_data["serverCertificateConfig"]
        )

    authenticationType = field("authenticationType")
    applicationProtocol = field("applicationProtocol")

    @cached_property
    def clientCertificateConfig(self):  # pragma: no cover
        return ClientCertificateConfig.make_one(
            self.boto3_raw_data["clientCertificateConfig"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateDomainConfigurationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDomainConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDomainConfigurationRequest:
    boto3_raw_data: "type_defs.UpdateDomainConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    domainConfigurationName = field("domainConfigurationName")

    @cached_property
    def authorizerConfig(self):  # pragma: no cover
        return AuthorizerConfig.make_one(self.boto3_raw_data["authorizerConfig"])

    domainConfigurationStatus = field("domainConfigurationStatus")
    removeAuthorizerConfig = field("removeAuthorizerConfig")

    @cached_property
    def tlsConfig(self):  # pragma: no cover
        return TlsConfig.make_one(self.boto3_raw_data["tlsConfig"])

    @cached_property
    def serverCertificateConfig(self):  # pragma: no cover
        return ServerCertificateConfig.make_one(
            self.boto3_raw_data["serverCertificateConfig"]
        )

    authenticationType = field("authenticationType")
    applicationProtocol = field("applicationProtocol")

    @cached_property
    def clientCertificateConfig(self):  # pragma: no cover
        return ClientCertificateConfig.make_one(
            self.boto3_raw_data["clientCertificateConfig"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateDomainConfigurationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDomainConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SchedulingConfigOutput:
    boto3_raw_data: "type_defs.SchedulingConfigOutputTypeDef" = dataclasses.field()

    startTime = field("startTime")
    endTime = field("endTime")
    endBehavior = field("endBehavior")

    @cached_property
    def maintenanceWindows(self):  # pragma: no cover
        return MaintenanceWindow.make_many(self.boto3_raw_data["maintenanceWindows"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SchedulingConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SchedulingConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SchedulingConfig:
    boto3_raw_data: "type_defs.SchedulingConfigTypeDef" = dataclasses.field()

    startTime = field("startTime")
    endTime = field("endTime")
    endBehavior = field("endBehavior")

    @cached_property
    def maintenanceWindows(self):  # pragma: no cover
        return MaintenanceWindow.make_many(self.boto3_raw_data["maintenanceWindows"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SchedulingConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SchedulingConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateKeysAndCertificateResponse:
    boto3_raw_data: "type_defs.CreateKeysAndCertificateResponseTypeDef" = (
        dataclasses.field()
    )

    certificateArn = field("certificateArn")
    certificateId = field("certificateId")
    certificatePem = field("certificatePem")

    @cached_property
    def keyPair(self):  # pragma: no cover
        return KeyPair.make_one(self.boto3_raw_data["keyPair"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateKeysAndCertificateResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateKeysAndCertificateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateProvisioningClaimResponse:
    boto3_raw_data: "type_defs.CreateProvisioningClaimResponseTypeDef" = (
        dataclasses.field()
    )

    certificateId = field("certificateId")
    certificatePem = field("certificatePem")

    @cached_property
    def keyPair(self):  # pragma: no cover
        return KeyPair.make_one(self.boto3_raw_data["keyPair"])

    expiration = field("expiration")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateProvisioningClaimResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateProvisioningClaimResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateProvisioningTemplateRequest:
    boto3_raw_data: "type_defs.CreateProvisioningTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    templateName = field("templateName")
    templateBody = field("templateBody")
    provisioningRoleArn = field("provisioningRoleArn")
    description = field("description")
    enabled = field("enabled")

    @cached_property
    def preProvisioningHook(self):  # pragma: no cover
        return ProvisioningHook.make_one(self.boto3_raw_data["preProvisioningHook"])

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    type = field("type")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateProvisioningTemplateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateProvisioningTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeProvisioningTemplateResponse:
    boto3_raw_data: "type_defs.DescribeProvisioningTemplateResponseTypeDef" = (
        dataclasses.field()
    )

    templateArn = field("templateArn")
    templateName = field("templateName")
    description = field("description")
    creationDate = field("creationDate")
    lastModifiedDate = field("lastModifiedDate")
    defaultVersionId = field("defaultVersionId")
    templateBody = field("templateBody")
    enabled = field("enabled")
    provisioningRoleArn = field("provisioningRoleArn")

    @cached_property
    def preProvisioningHook(self):  # pragma: no cover
        return ProvisioningHook.make_one(self.boto3_raw_data["preProvisioningHook"])

    type = field("type")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeProvisioningTemplateResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeProvisioningTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateProvisioningTemplateRequest:
    boto3_raw_data: "type_defs.UpdateProvisioningTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    templateName = field("templateName")
    description = field("description")
    enabled = field("enabled")
    defaultVersionId = field("defaultVersionId")
    provisioningRoleArn = field("provisioningRoleArn")

    @cached_property
    def preProvisioningHook(self):  # pragma: no cover
        return ProvisioningHook.make_one(self.boto3_raw_data["preProvisioningHook"])

    removePreProvisioningHook = field("removePreProvisioningHook")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateProvisioningTemplateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateProvisioningTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAuditTaskResponse:
    boto3_raw_data: "type_defs.DescribeAuditTaskResponseTypeDef" = dataclasses.field()

    taskStatus = field("taskStatus")
    taskType = field("taskType")
    taskStartTime = field("taskStartTime")

    @cached_property
    def taskStatistics(self):  # pragma: no cover
        return TaskStatistics.make_one(self.boto3_raw_data["taskStatistics"])

    scheduledAuditName = field("scheduledAuditName")
    auditDetails = field("auditDetails")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAuditTaskResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAuditTaskResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterCACertificateRequest:
    boto3_raw_data: "type_defs.RegisterCACertificateRequestTypeDef" = (
        dataclasses.field()
    )

    caCertificate = field("caCertificate")
    verificationCertificate = field("verificationCertificate")
    setAsActive = field("setAsActive")
    allowAutoRegistration = field("allowAutoRegistration")

    @cached_property
    def registrationConfig(self):  # pragma: no cover
        return RegistrationConfig.make_one(self.boto3_raw_data["registrationConfig"])

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    certificateMode = field("certificateMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterCACertificateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterCACertificateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCACertificateRequest:
    boto3_raw_data: "type_defs.UpdateCACertificateRequestTypeDef" = dataclasses.field()

    certificateId = field("certificateId")
    newStatus = field("newStatus")
    newAutoRegistrationStatus = field("newAutoRegistrationStatus")

    @cached_property
    def registrationConfig(self):  # pragma: no cover
        return RegistrationConfig.make_one(self.boto3_raw_data["registrationConfig"])

    removeAutoRegistration = field("removeAutoRegistration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateCACertificateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCACertificateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDomainConfigurationResponse:
    boto3_raw_data: "type_defs.DescribeDomainConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    domainConfigurationName = field("domainConfigurationName")
    domainConfigurationArn = field("domainConfigurationArn")
    domainName = field("domainName")

    @cached_property
    def serverCertificates(self):  # pragma: no cover
        return ServerCertificateSummary.make_many(
            self.boto3_raw_data["serverCertificates"]
        )

    @cached_property
    def authorizerConfig(self):  # pragma: no cover
        return AuthorizerConfig.make_one(self.boto3_raw_data["authorizerConfig"])

    domainConfigurationStatus = field("domainConfigurationStatus")
    serviceType = field("serviceType")
    domainType = field("domainType")
    lastStatusChangeDate = field("lastStatusChangeDate")

    @cached_property
    def tlsConfig(self):  # pragma: no cover
        return TlsConfig.make_one(self.boto3_raw_data["tlsConfig"])

    @cached_property
    def serverCertificateConfig(self):  # pragma: no cover
        return ServerCertificateConfig.make_one(
            self.boto3_raw_data["serverCertificateConfig"]
        )

    authenticationType = field("authenticationType")
    applicationProtocol = field("applicationProtocol")

    @cached_property
    def clientCertificateConfig(self):  # pragma: no cover
        return ClientCertificateConfig.make_one(
            self.boto3_raw_data["clientCertificateConfig"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDomainConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDomainConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeManagedJobTemplateResponse:
    boto3_raw_data: "type_defs.DescribeManagedJobTemplateResponseTypeDef" = (
        dataclasses.field()
    )

    templateName = field("templateName")
    templateArn = field("templateArn")
    description = field("description")
    templateVersion = field("templateVersion")
    environments = field("environments")

    @cached_property
    def documentParameters(self):  # pragma: no cover
        return DocumentParameter.make_many(self.boto3_raw_data["documentParameters"])

    document = field("document")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeManagedJobTemplateResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeManagedJobTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRoleAliasResponse:
    boto3_raw_data: "type_defs.DescribeRoleAliasResponseTypeDef" = dataclasses.field()

    @cached_property
    def roleAliasDescription(self):  # pragma: no cover
        return RoleAliasDescription.make_one(
            self.boto3_raw_data["roleAliasDescription"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeRoleAliasResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRoleAliasResponseTypeDef"]
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

    @cached_property
    def s3Destination(self):  # pragma: no cover
        return S3Destination.make_one(self.boto3_raw_data["s3Destination"])

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
class ListDetectMitigationActionsExecutionsResponse:
    boto3_raw_data: "type_defs.ListDetectMitigationActionsExecutionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def actionsExecutions(self):  # pragma: no cover
        return DetectMitigationActionExecution.make_many(
            self.boto3_raw_data["actionsExecutions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDetectMitigationActionsExecutionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDetectMitigationActionsExecutionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDomainConfigurationsResponse:
    boto3_raw_data: "type_defs.ListDomainConfigurationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def domainConfigurations(self):  # pragma: no cover
        return DomainConfigurationSummary.make_many(
            self.boto3_raw_data["domainConfigurations"]
        )

    nextMarker = field("nextMarker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDomainConfigurationsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDomainConfigurationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DynamoDBv2Action:
    boto3_raw_data: "type_defs.DynamoDBv2ActionTypeDef" = dataclasses.field()

    roleArn = field("roleArn")

    @cached_property
    def putItem(self):  # pragma: no cover
        return PutItemInput.make_one(self.boto3_raw_data["putItem"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DynamoDBv2ActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DynamoDBv2ActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEffectivePoliciesResponse:
    boto3_raw_data: "type_defs.GetEffectivePoliciesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def effectivePolicies(self):  # pragma: no cover
        return EffectivePolicy.make_many(self.boto3_raw_data["effectivePolicies"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEffectivePoliciesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEffectivePoliciesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExponentialRolloutRate:
    boto3_raw_data: "type_defs.ExponentialRolloutRateTypeDef" = dataclasses.field()

    baseRatePerMinute = field("baseRatePerMinute")
    incrementFactor = field("incrementFactor")

    @cached_property
    def rateIncreaseCriteria(self):  # pragma: no cover
        return RateIncreaseCriteria.make_one(
            self.boto3_raw_data["rateIncreaseCriteria"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExponentialRolloutRateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExponentialRolloutRateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ThingGroupIndexingConfigurationOutput:
    boto3_raw_data: "type_defs.ThingGroupIndexingConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    thingGroupIndexingMode = field("thingGroupIndexingMode")

    @cached_property
    def managedFields(self):  # pragma: no cover
        return Field.make_many(self.boto3_raw_data["managedFields"])

    @cached_property
    def customFields(self):  # pragma: no cover
        return Field.make_many(self.boto3_raw_data["customFields"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ThingGroupIndexingConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ThingGroupIndexingConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ThingGroupIndexingConfiguration:
    boto3_raw_data: "type_defs.ThingGroupIndexingConfigurationTypeDef" = (
        dataclasses.field()
    )

    thingGroupIndexingMode = field("thingGroupIndexingMode")

    @cached_property
    def managedFields(self):  # pragma: no cover
        return Field.make_many(self.boto3_raw_data["managedFields"])

    @cached_property
    def customFields(self):  # pragma: no cover
        return Field.make_many(self.boto3_raw_data["customFields"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ThingGroupIndexingConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ThingGroupIndexingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PackageVersionArtifact:
    boto3_raw_data: "type_defs.PackageVersionArtifactTypeDef" = dataclasses.field()

    @cached_property
    def s3Location(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["s3Location"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PackageVersionArtifactTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PackageVersionArtifactTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Sbom:
    boto3_raw_data: "type_defs.SbomTypeDef" = dataclasses.field()

    @cached_property
    def s3Location(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["s3Location"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SbomTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SbomTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StreamFile:
    boto3_raw_data: "type_defs.StreamFileTypeDef" = dataclasses.field()

    fileId = field("fileId")

    @cached_property
    def s3Location(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["s3Location"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StreamFileTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StreamFileTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FileLocation:
    boto3_raw_data: "type_defs.FileLocationTypeDef" = dataclasses.field()

    @cached_property
    def stream(self):  # pragma: no cover
        return Stream.make_one(self.boto3_raw_data["stream"])

    @cached_property
    def s3Location(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["s3Location"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FileLocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FileLocationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFleetMetricsResponse:
    boto3_raw_data: "type_defs.ListFleetMetricsResponseTypeDef" = dataclasses.field()

    @cached_property
    def fleetMetrics(self):  # pragma: no cover
        return FleetMetricNameAndArn.make_many(self.boto3_raw_data["fleetMetrics"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFleetMetricsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFleetMetricsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IndexingFilterOutput:
    boto3_raw_data: "type_defs.IndexingFilterOutputTypeDef" = dataclasses.field()

    namedShadowNames = field("namedShadowNames")

    @cached_property
    def geoLocations(self):  # pragma: no cover
        return GeoLocationTarget.make_many(self.boto3_raw_data["geoLocations"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IndexingFilterOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IndexingFilterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IndexingFilter:
    boto3_raw_data: "type_defs.IndexingFilterTypeDef" = dataclasses.field()

    namedShadowNames = field("namedShadowNames")

    @cached_property
    def geoLocations(self):  # pragma: no cover
        return GeoLocationTarget.make_many(self.boto3_raw_data["geoLocations"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IndexingFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IndexingFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBehaviorModelTrainingSummariesRequestPaginate:
    boto3_raw_data: (
        "type_defs.GetBehaviorModelTrainingSummariesRequestPaginateTypeDef"
    ) = dataclasses.field()

    securityProfileName = field("securityProfileName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetBehaviorModelTrainingSummariesRequestPaginateTypeDef"
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
                "type_defs.GetBehaviorModelTrainingSummariesRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListActiveViolationsRequestPaginate:
    boto3_raw_data: "type_defs.ListActiveViolationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    thingName = field("thingName")
    securityProfileName = field("securityProfileName")
    behaviorCriteriaType = field("behaviorCriteriaType")
    listSuppressedAlerts = field("listSuppressedAlerts")
    verificationState = field("verificationState")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListActiveViolationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListActiveViolationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAttachedPoliciesRequestPaginate:
    boto3_raw_data: "type_defs.ListAttachedPoliciesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    target = field("target")
    recursive = field("recursive")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAttachedPoliciesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAttachedPoliciesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAuditMitigationActionsExecutionsRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListAuditMitigationActionsExecutionsRequestPaginateTypeDef"
    ) = dataclasses.field()

    taskId = field("taskId")
    findingId = field("findingId")
    actionStatus = field("actionStatus")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAuditMitigationActionsExecutionsRequestPaginateTypeDef"
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
                "type_defs.ListAuditMitigationActionsExecutionsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAuditMitigationActionsTasksRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListAuditMitigationActionsTasksRequestPaginateTypeDef"
    ) = dataclasses.field()

    startTime = field("startTime")
    endTime = field("endTime")
    auditTaskId = field("auditTaskId")
    findingId = field("findingId")
    taskStatus = field("taskStatus")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAuditMitigationActionsTasksRequestPaginateTypeDef"
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
                "type_defs.ListAuditMitigationActionsTasksRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAuditTasksRequestPaginate:
    boto3_raw_data: "type_defs.ListAuditTasksRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    startTime = field("startTime")
    endTime = field("endTime")
    taskType = field("taskType")
    taskStatus = field("taskStatus")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAuditTasksRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAuditTasksRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAuthorizersRequestPaginate:
    boto3_raw_data: "type_defs.ListAuthorizersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ascendingOrder = field("ascendingOrder")
    status = field("status")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAuthorizersRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAuthorizersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBillingGroupsRequestPaginate:
    boto3_raw_data: "type_defs.ListBillingGroupsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    namePrefixFilter = field("namePrefixFilter")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListBillingGroupsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBillingGroupsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCACertificatesRequestPaginate:
    boto3_raw_data: "type_defs.ListCACertificatesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ascendingOrder = field("ascendingOrder")
    templateName = field("templateName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCACertificatesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCACertificatesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCertificatesByCARequestPaginate:
    boto3_raw_data: "type_defs.ListCertificatesByCARequestPaginateTypeDef" = (
        dataclasses.field()
    )

    caCertificateId = field("caCertificateId")
    ascendingOrder = field("ascendingOrder")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCertificatesByCARequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCertificatesByCARequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCertificatesRequestPaginate:
    boto3_raw_data: "type_defs.ListCertificatesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ascendingOrder = field("ascendingOrder")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListCertificatesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCertificatesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCommandsRequestPaginate:
    boto3_raw_data: "type_defs.ListCommandsRequestPaginateTypeDef" = dataclasses.field()

    namespace = field("namespace")
    commandParameterName = field("commandParameterName")
    sortOrder = field("sortOrder")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCommandsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCommandsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCustomMetricsRequestPaginate:
    boto3_raw_data: "type_defs.ListCustomMetricsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListCustomMetricsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCustomMetricsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDetectMitigationActionsExecutionsRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListDetectMitigationActionsExecutionsRequestPaginateTypeDef"
    ) = dataclasses.field()

    taskId = field("taskId")
    violationId = field("violationId")
    thingName = field("thingName")
    startTime = field("startTime")
    endTime = field("endTime")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDetectMitigationActionsExecutionsRequestPaginateTypeDef"
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
                "type_defs.ListDetectMitigationActionsExecutionsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDetectMitigationActionsTasksRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListDetectMitigationActionsTasksRequestPaginateTypeDef"
    ) = dataclasses.field()

    startTime = field("startTime")
    endTime = field("endTime")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDetectMitigationActionsTasksRequestPaginateTypeDef"
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
                "type_defs.ListDetectMitigationActionsTasksRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDimensionsRequestPaginate:
    boto3_raw_data: "type_defs.ListDimensionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDimensionsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDimensionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDomainConfigurationsRequestPaginate:
    boto3_raw_data: "type_defs.ListDomainConfigurationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    serviceType = field("serviceType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDomainConfigurationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDomainConfigurationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFleetMetricsRequestPaginate:
    boto3_raw_data: "type_defs.ListFleetMetricsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListFleetMetricsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFleetMetricsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIndicesRequestPaginate:
    boto3_raw_data: "type_defs.ListIndicesRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIndicesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIndicesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobExecutionsForJobRequestPaginate:
    boto3_raw_data: "type_defs.ListJobExecutionsForJobRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    jobId = field("jobId")
    status = field("status")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListJobExecutionsForJobRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobExecutionsForJobRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobExecutionsForThingRequestPaginate:
    boto3_raw_data: "type_defs.ListJobExecutionsForThingRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    thingName = field("thingName")
    status = field("status")
    namespaceId = field("namespaceId")
    jobId = field("jobId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListJobExecutionsForThingRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobExecutionsForThingRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobTemplatesRequestPaginate:
    boto3_raw_data: "type_defs.ListJobTemplatesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListJobTemplatesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobTemplatesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobsRequestPaginate:
    boto3_raw_data: "type_defs.ListJobsRequestPaginateTypeDef" = dataclasses.field()

    status = field("status")
    targetSelection = field("targetSelection")
    thingGroupName = field("thingGroupName")
    thingGroupId = field("thingGroupId")
    namespaceId = field("namespaceId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListJobsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListManagedJobTemplatesRequestPaginate:
    boto3_raw_data: "type_defs.ListManagedJobTemplatesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    templateName = field("templateName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListManagedJobTemplatesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListManagedJobTemplatesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMetricValuesRequestPaginate:
    boto3_raw_data: "type_defs.ListMetricValuesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    thingName = field("thingName")
    metricName = field("metricName")
    startTime = field("startTime")
    endTime = field("endTime")
    dimensionName = field("dimensionName")
    dimensionValueOperator = field("dimensionValueOperator")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListMetricValuesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMetricValuesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMitigationActionsRequestPaginate:
    boto3_raw_data: "type_defs.ListMitigationActionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    actionType = field("actionType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListMitigationActionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMitigationActionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOTAUpdatesRequestPaginate:
    boto3_raw_data: "type_defs.ListOTAUpdatesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    otaUpdateStatus = field("otaUpdateStatus")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListOTAUpdatesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOTAUpdatesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOutgoingCertificatesRequestPaginate:
    boto3_raw_data: "type_defs.ListOutgoingCertificatesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ascendingOrder = field("ascendingOrder")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListOutgoingCertificatesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOutgoingCertificatesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPackageVersionsRequestPaginate:
    boto3_raw_data: "type_defs.ListPackageVersionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    packageName = field("packageName")
    status = field("status")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPackageVersionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPackageVersionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPackagesRequestPaginate:
    boto3_raw_data: "type_defs.ListPackagesRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPackagesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPackagesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPoliciesRequestPaginate:
    boto3_raw_data: "type_defs.ListPoliciesRequestPaginateTypeDef" = dataclasses.field()

    ascendingOrder = field("ascendingOrder")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPoliciesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPoliciesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPolicyPrincipalsRequestPaginate:
    boto3_raw_data: "type_defs.ListPolicyPrincipalsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    policyName = field("policyName")
    ascendingOrder = field("ascendingOrder")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPolicyPrincipalsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPolicyPrincipalsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPrincipalPoliciesRequestPaginate:
    boto3_raw_data: "type_defs.ListPrincipalPoliciesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    principal = field("principal")
    ascendingOrder = field("ascendingOrder")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPrincipalPoliciesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPrincipalPoliciesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPrincipalThingsRequestPaginate:
    boto3_raw_data: "type_defs.ListPrincipalThingsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    principal = field("principal")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPrincipalThingsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPrincipalThingsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPrincipalThingsV2RequestPaginate:
    boto3_raw_data: "type_defs.ListPrincipalThingsV2RequestPaginateTypeDef" = (
        dataclasses.field()
    )

    principal = field("principal")
    thingPrincipalType = field("thingPrincipalType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPrincipalThingsV2RequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPrincipalThingsV2RequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProvisioningTemplateVersionsRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListProvisioningTemplateVersionsRequestPaginateTypeDef"
    ) = dataclasses.field()

    templateName = field("templateName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListProvisioningTemplateVersionsRequestPaginateTypeDef"
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
                "type_defs.ListProvisioningTemplateVersionsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProvisioningTemplatesRequestPaginate:
    boto3_raw_data: "type_defs.ListProvisioningTemplatesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListProvisioningTemplatesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProvisioningTemplatesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRelatedResourcesForAuditFindingRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListRelatedResourcesForAuditFindingRequestPaginateTypeDef"
    ) = dataclasses.field()

    findingId = field("findingId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRelatedResourcesForAuditFindingRequestPaginateTypeDef"
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
                "type_defs.ListRelatedResourcesForAuditFindingRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRoleAliasesRequestPaginate:
    boto3_raw_data: "type_defs.ListRoleAliasesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ascendingOrder = field("ascendingOrder")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListRoleAliasesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRoleAliasesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSbomValidationResultsRequestPaginate:
    boto3_raw_data: "type_defs.ListSbomValidationResultsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    packageName = field("packageName")
    versionName = field("versionName")
    validationResult = field("validationResult")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSbomValidationResultsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSbomValidationResultsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListScheduledAuditsRequestPaginate:
    boto3_raw_data: "type_defs.ListScheduledAuditsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListScheduledAuditsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListScheduledAuditsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSecurityProfilesForTargetRequestPaginate:
    boto3_raw_data: "type_defs.ListSecurityProfilesForTargetRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    securityProfileTargetArn = field("securityProfileTargetArn")
    recursive = field("recursive")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSecurityProfilesForTargetRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSecurityProfilesForTargetRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSecurityProfilesRequestPaginate:
    boto3_raw_data: "type_defs.ListSecurityProfilesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    dimensionName = field("dimensionName")
    metricName = field("metricName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSecurityProfilesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSecurityProfilesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStreamsRequestPaginate:
    boto3_raw_data: "type_defs.ListStreamsRequestPaginateTypeDef" = dataclasses.field()

    ascendingOrder = field("ascendingOrder")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListStreamsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStreamsRequestPaginateTypeDef"]
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

    resourceArn = field("resourceArn")

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
class ListTargetsForPolicyRequestPaginate:
    boto3_raw_data: "type_defs.ListTargetsForPolicyRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    policyName = field("policyName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTargetsForPolicyRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTargetsForPolicyRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTargetsForSecurityProfileRequestPaginate:
    boto3_raw_data: "type_defs.ListTargetsForSecurityProfileRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    securityProfileName = field("securityProfileName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTargetsForSecurityProfileRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTargetsForSecurityProfileRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListThingGroupsForThingRequestPaginate:
    boto3_raw_data: "type_defs.ListThingGroupsForThingRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    thingName = field("thingName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListThingGroupsForThingRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListThingGroupsForThingRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListThingGroupsRequestPaginate:
    boto3_raw_data: "type_defs.ListThingGroupsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    parentGroup = field("parentGroup")
    namePrefixFilter = field("namePrefixFilter")
    recursive = field("recursive")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListThingGroupsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListThingGroupsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListThingPrincipalsRequestPaginate:
    boto3_raw_data: "type_defs.ListThingPrincipalsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    thingName = field("thingName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListThingPrincipalsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListThingPrincipalsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListThingPrincipalsV2RequestPaginate:
    boto3_raw_data: "type_defs.ListThingPrincipalsV2RequestPaginateTypeDef" = (
        dataclasses.field()
    )

    thingName = field("thingName")
    thingPrincipalType = field("thingPrincipalType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListThingPrincipalsV2RequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListThingPrincipalsV2RequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListThingRegistrationTaskReportsRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListThingRegistrationTaskReportsRequestPaginateTypeDef"
    ) = dataclasses.field()

    taskId = field("taskId")
    reportType = field("reportType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListThingRegistrationTaskReportsRequestPaginateTypeDef"
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
                "type_defs.ListThingRegistrationTaskReportsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListThingRegistrationTasksRequestPaginate:
    boto3_raw_data: "type_defs.ListThingRegistrationTasksRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    status = field("status")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListThingRegistrationTasksRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListThingRegistrationTasksRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListThingTypesRequestPaginate:
    boto3_raw_data: "type_defs.ListThingTypesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    thingTypeName = field("thingTypeName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListThingTypesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListThingTypesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListThingsInBillingGroupRequestPaginate:
    boto3_raw_data: "type_defs.ListThingsInBillingGroupRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    billingGroupName = field("billingGroupName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListThingsInBillingGroupRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListThingsInBillingGroupRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListThingsInThingGroupRequestPaginate:
    boto3_raw_data: "type_defs.ListThingsInThingGroupRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    thingGroupName = field("thingGroupName")
    recursive = field("recursive")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListThingsInThingGroupRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListThingsInThingGroupRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListThingsRequestPaginate:
    boto3_raw_data: "type_defs.ListThingsRequestPaginateTypeDef" = dataclasses.field()

    attributeName = field("attributeName")
    attributeValue = field("attributeValue")
    thingTypeName = field("thingTypeName")
    usePrefixAttributeValue = field("usePrefixAttributeValue")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListThingsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListThingsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTopicRuleDestinationsRequestPaginate:
    boto3_raw_data: "type_defs.ListTopicRuleDestinationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTopicRuleDestinationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTopicRuleDestinationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTopicRulesRequestPaginate:
    boto3_raw_data: "type_defs.ListTopicRulesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    topic = field("topic")
    ruleDisabled = field("ruleDisabled")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListTopicRulesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTopicRulesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListV2LoggingLevelsRequestPaginate:
    boto3_raw_data: "type_defs.ListV2LoggingLevelsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    targetType = field("targetType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListV2LoggingLevelsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListV2LoggingLevelsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListViolationEventsRequestPaginate:
    boto3_raw_data: "type_defs.ListViolationEventsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    startTime = field("startTime")
    endTime = field("endTime")
    thingName = field("thingName")
    securityProfileName = field("securityProfileName")
    behaviorCriteriaType = field("behaviorCriteriaType")
    listSuppressedAlerts = field("listSuppressedAlerts")
    verificationState = field("verificationState")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListViolationEventsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListViolationEventsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCommandExecutionResponse:
    boto3_raw_data: "type_defs.GetCommandExecutionResponseTypeDef" = dataclasses.field()

    executionId = field("executionId")
    commandArn = field("commandArn")
    targetArn = field("targetArn")
    status = field("status")

    @cached_property
    def statusReason(self):  # pragma: no cover
        return StatusReason.make_one(self.boto3_raw_data["statusReason"])

    result = field("result")
    parameters = field("parameters")
    executionTimeoutSeconds = field("executionTimeoutSeconds")
    createdAt = field("createdAt")
    lastUpdatedAt = field("lastUpdatedAt")
    startedAt = field("startedAt")
    completedAt = field("completedAt")
    timeToLive = field("timeToLive")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCommandExecutionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCommandExecutionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPackageConfigurationResponse:
    boto3_raw_data: "type_defs.GetPackageConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def versionUpdateByJobsConfig(self):  # pragma: no cover
        return VersionUpdateByJobsConfig.make_one(
            self.boto3_raw_data["versionUpdateByJobsConfig"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetPackageConfigurationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPackageConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePackageConfigurationRequest:
    boto3_raw_data: "type_defs.UpdatePackageConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def versionUpdateByJobsConfig(self):  # pragma: no cover
        return VersionUpdateByJobsConfig.make_one(
            self.boto3_raw_data["versionUpdateByJobsConfig"]
        )

    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdatePackageConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePackageConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPercentilesResponse:
    boto3_raw_data: "type_defs.GetPercentilesResponseTypeDef" = dataclasses.field()

    @cached_property
    def percentiles(self):  # pragma: no cover
        return PercentPair.make_many(self.boto3_raw_data["percentiles"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPercentilesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPercentilesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStatisticsResponse:
    boto3_raw_data: "type_defs.GetStatisticsResponseTypeDef" = dataclasses.field()

    @cached_property
    def statistics(self):  # pragma: no cover
        return Statistics.make_one(self.boto3_raw_data["statistics"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetStatisticsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetStatisticsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBillingGroupsResponse:
    boto3_raw_data: "type_defs.ListBillingGroupsResponseTypeDef" = dataclasses.field()

    @cached_property
    def billingGroups(self):  # pragma: no cover
        return GroupNameAndArn.make_many(self.boto3_raw_data["billingGroups"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBillingGroupsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBillingGroupsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListThingGroupsForThingResponse:
    boto3_raw_data: "type_defs.ListThingGroupsForThingResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def thingGroups(self):  # pragma: no cover
        return GroupNameAndArn.make_many(self.boto3_raw_data["thingGroups"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListThingGroupsForThingResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListThingGroupsForThingResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListThingGroupsResponse:
    boto3_raw_data: "type_defs.ListThingGroupsResponseTypeDef" = dataclasses.field()

    @cached_property
    def thingGroups(self):  # pragma: no cover
        return GroupNameAndArn.make_many(self.boto3_raw_data["thingGroups"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListThingGroupsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListThingGroupsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ThingGroupMetadata:
    boto3_raw_data: "type_defs.ThingGroupMetadataTypeDef" = dataclasses.field()

    parentGroupName = field("parentGroupName")

    @cached_property
    def rootToParentThingGroups(self):  # pragma: no cover
        return GroupNameAndArn.make_many(self.boto3_raw_data["rootToParentThingGroups"])

    creationDate = field("creationDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ThingGroupMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ThingGroupMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HttpAuthorization:
    boto3_raw_data: "type_defs.HttpAuthorizationTypeDef" = dataclasses.field()

    @cached_property
    def sigv4(self):  # pragma: no cover
        return SigV4Authorization.make_one(self.boto3_raw_data["sigv4"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HttpAuthorizationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HttpAuthorizationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobExecution:
    boto3_raw_data: "type_defs.JobExecutionTypeDef" = dataclasses.field()

    jobId = field("jobId")
    status = field("status")
    forceCanceled = field("forceCanceled")

    @cached_property
    def statusDetails(self):  # pragma: no cover
        return JobExecutionStatusDetails.make_one(self.boto3_raw_data["statusDetails"])

    thingArn = field("thingArn")
    queuedAt = field("queuedAt")
    startedAt = field("startedAt")
    lastUpdatedAt = field("lastUpdatedAt")
    executionNumber = field("executionNumber")
    versionNumber = field("versionNumber")
    approximateSecondsBeforeTimedOut = field("approximateSecondsBeforeTimedOut")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobExecutionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobExecutionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobExecutionSummaryForJob:
    boto3_raw_data: "type_defs.JobExecutionSummaryForJobTypeDef" = dataclasses.field()

    thingArn = field("thingArn")

    @cached_property
    def jobExecutionSummary(self):  # pragma: no cover
        return JobExecutionSummary.make_one(self.boto3_raw_data["jobExecutionSummary"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JobExecutionSummaryForJobTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobExecutionSummaryForJobTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobExecutionSummaryForThing:
    boto3_raw_data: "type_defs.JobExecutionSummaryForThingTypeDef" = dataclasses.field()

    jobId = field("jobId")

    @cached_property
    def jobExecutionSummary(self):  # pragma: no cover
        return JobExecutionSummary.make_one(self.boto3_raw_data["jobExecutionSummary"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JobExecutionSummaryForThingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobExecutionSummaryForThingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobExecutionsRetryConfigOutput:
    boto3_raw_data: "type_defs.JobExecutionsRetryConfigOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def criteriaList(self):  # pragma: no cover
        return RetryCriteria.make_many(self.boto3_raw_data["criteriaList"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.JobExecutionsRetryConfigOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobExecutionsRetryConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobExecutionsRetryConfig:
    boto3_raw_data: "type_defs.JobExecutionsRetryConfigTypeDef" = dataclasses.field()

    @cached_property
    def criteriaList(self):  # pragma: no cover
        return RetryCriteria.make_many(self.boto3_raw_data["criteriaList"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JobExecutionsRetryConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobExecutionsRetryConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobsResponse:
    boto3_raw_data: "type_defs.ListJobsResponseTypeDef" = dataclasses.field()

    @cached_property
    def jobs(self):  # pragma: no cover
        return JobSummary.make_many(self.boto3_raw_data["jobs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListJobsResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobTemplatesResponse:
    boto3_raw_data: "type_defs.ListJobTemplatesResponseTypeDef" = dataclasses.field()

    @cached_property
    def jobTemplates(self):  # pragma: no cover
        return JobTemplateSummary.make_many(self.boto3_raw_data["jobTemplates"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListJobTemplatesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobTemplatesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KafkaActionOutput:
    boto3_raw_data: "type_defs.KafkaActionOutputTypeDef" = dataclasses.field()

    destinationArn = field("destinationArn")
    topic = field("topic")
    clientProperties = field("clientProperties")
    key = field("key")
    partition = field("partition")

    @cached_property
    def headers(self):  # pragma: no cover
        return KafkaActionHeader.make_many(self.boto3_raw_data["headers"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KafkaActionOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KafkaActionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KafkaAction:
    boto3_raw_data: "type_defs.KafkaActionTypeDef" = dataclasses.field()

    destinationArn = field("destinationArn")
    topic = field("topic")
    clientProperties = field("clientProperties")
    key = field("key")
    partition = field("partition")

    @cached_property
    def headers(self):  # pragma: no cover
        return KafkaActionHeader.make_many(self.boto3_raw_data["headers"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KafkaActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.KafkaActionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCommandExecutionsRequestPaginate:
    boto3_raw_data: "type_defs.ListCommandExecutionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    namespace = field("namespace")
    status = field("status")
    sortOrder = field("sortOrder")

    @cached_property
    def startedTimeFilter(self):  # pragma: no cover
        return TimeFilter.make_one(self.boto3_raw_data["startedTimeFilter"])

    @cached_property
    def completedTimeFilter(self):  # pragma: no cover
        return TimeFilter.make_one(self.boto3_raw_data["completedTimeFilter"])

    targetArn = field("targetArn")
    commandArn = field("commandArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCommandExecutionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCommandExecutionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCommandExecutionsRequest:
    boto3_raw_data: "type_defs.ListCommandExecutionsRequestTypeDef" = (
        dataclasses.field()
    )

    maxResults = field("maxResults")
    nextToken = field("nextToken")
    namespace = field("namespace")
    status = field("status")
    sortOrder = field("sortOrder")

    @cached_property
    def startedTimeFilter(self):  # pragma: no cover
        return TimeFilter.make_one(self.boto3_raw_data["startedTimeFilter"])

    @cached_property
    def completedTimeFilter(self):  # pragma: no cover
        return TimeFilter.make_one(self.boto3_raw_data["completedTimeFilter"])

    targetArn = field("targetArn")
    commandArn = field("commandArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCommandExecutionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCommandExecutionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListManagedJobTemplatesResponse:
    boto3_raw_data: "type_defs.ListManagedJobTemplatesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def managedJobTemplates(self):  # pragma: no cover
        return ManagedJobTemplateSummary.make_many(
            self.boto3_raw_data["managedJobTemplates"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListManagedJobTemplatesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListManagedJobTemplatesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMitigationActionsResponse:
    boto3_raw_data: "type_defs.ListMitigationActionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def actionIdentifiers(self):  # pragma: no cover
        return MitigationActionIdentifier.make_many(
            self.boto3_raw_data["actionIdentifiers"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListMitigationActionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMitigationActionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOTAUpdatesResponse:
    boto3_raw_data: "type_defs.ListOTAUpdatesResponseTypeDef" = dataclasses.field()

    @cached_property
    def otaUpdates(self):  # pragma: no cover
        return OTAUpdateSummary.make_many(self.boto3_raw_data["otaUpdates"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListOTAUpdatesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOTAUpdatesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOutgoingCertificatesResponse:
    boto3_raw_data: "type_defs.ListOutgoingCertificatesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def outgoingCertificates(self):  # pragma: no cover
        return OutgoingCertificate.make_many(
            self.boto3_raw_data["outgoingCertificates"]
        )

    nextMarker = field("nextMarker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListOutgoingCertificatesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOutgoingCertificatesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPackageVersionsResponse:
    boto3_raw_data: "type_defs.ListPackageVersionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def packageVersionSummaries(self):  # pragma: no cover
        return PackageVersionSummary.make_many(
            self.boto3_raw_data["packageVersionSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPackageVersionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPackageVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPackagesResponse:
    boto3_raw_data: "type_defs.ListPackagesResponseTypeDef" = dataclasses.field()

    @cached_property
    def packageSummaries(self):  # pragma: no cover
        return PackageSummary.make_many(self.boto3_raw_data["packageSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPackagesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPackagesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPolicyVersionsResponse:
    boto3_raw_data: "type_defs.ListPolicyVersionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def policyVersions(self):  # pragma: no cover
        return PolicyVersion.make_many(self.boto3_raw_data["policyVersions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPolicyVersionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPolicyVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPrincipalThingsV2Response:
    boto3_raw_data: "type_defs.ListPrincipalThingsV2ResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def principalThingObjects(self):  # pragma: no cover
        return PrincipalThingObject.make_many(
            self.boto3_raw_data["principalThingObjects"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListPrincipalThingsV2ResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPrincipalThingsV2ResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProvisioningTemplateVersionsResponse:
    boto3_raw_data: "type_defs.ListProvisioningTemplateVersionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def versions(self):  # pragma: no cover
        return ProvisioningTemplateVersionSummary.make_many(
            self.boto3_raw_data["versions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListProvisioningTemplateVersionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProvisioningTemplateVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProvisioningTemplatesResponse:
    boto3_raw_data: "type_defs.ListProvisioningTemplatesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def templates(self):  # pragma: no cover
        return ProvisioningTemplateSummary.make_many(self.boto3_raw_data["templates"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListProvisioningTemplatesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProvisioningTemplatesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSbomValidationResultsResponse:
    boto3_raw_data: "type_defs.ListSbomValidationResultsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def validationResultSummaries(self):  # pragma: no cover
        return SbomValidationResultSummary.make_many(
            self.boto3_raw_data["validationResultSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSbomValidationResultsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSbomValidationResultsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListScheduledAuditsResponse:
    boto3_raw_data: "type_defs.ListScheduledAuditsResponseTypeDef" = dataclasses.field()

    @cached_property
    def scheduledAudits(self):  # pragma: no cover
        return ScheduledAuditMetadata.make_many(self.boto3_raw_data["scheduledAudits"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListScheduledAuditsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListScheduledAuditsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSecurityProfilesResponse:
    boto3_raw_data: "type_defs.ListSecurityProfilesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def securityProfileIdentifiers(self):  # pragma: no cover
        return SecurityProfileIdentifier.make_many(
            self.boto3_raw_data["securityProfileIdentifiers"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSecurityProfilesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSecurityProfilesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStreamsResponse:
    boto3_raw_data: "type_defs.ListStreamsResponseTypeDef" = dataclasses.field()

    @cached_property
    def streams(self):  # pragma: no cover
        return StreamSummary.make_many(self.boto3_raw_data["streams"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListStreamsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStreamsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTargetsForSecurityProfileResponse:
    boto3_raw_data: "type_defs.ListTargetsForSecurityProfileResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def securityProfileTargets(self):  # pragma: no cover
        return SecurityProfileTarget.make_many(
            self.boto3_raw_data["securityProfileTargets"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTargetsForSecurityProfileResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTargetsForSecurityProfileResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SecurityProfileTargetMapping:
    boto3_raw_data: "type_defs.SecurityProfileTargetMappingTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def securityProfileIdentifier(self):  # pragma: no cover
        return SecurityProfileIdentifier.make_one(
            self.boto3_raw_data["securityProfileIdentifier"]
        )

    @cached_property
    def target(self):  # pragma: no cover
        return SecurityProfileTarget.make_one(self.boto3_raw_data["target"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SecurityProfileTargetMappingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SecurityProfileTargetMappingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListThingPrincipalsV2Response:
    boto3_raw_data: "type_defs.ListThingPrincipalsV2ResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def thingPrincipalObjects(self):  # pragma: no cover
        return ThingPrincipalObject.make_many(
            self.boto3_raw_data["thingPrincipalObjects"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListThingPrincipalsV2ResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListThingPrincipalsV2ResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListThingsResponse:
    boto3_raw_data: "type_defs.ListThingsResponseTypeDef" = dataclasses.field()

    @cached_property
    def things(self):  # pragma: no cover
        return ThingAttribute.make_many(self.boto3_raw_data["things"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListThingsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListThingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTopicRulesResponse:
    boto3_raw_data: "type_defs.ListTopicRulesResponseTypeDef" = dataclasses.field()

    @cached_property
    def rules(self):  # pragma: no cover
        return TopicRuleListItem.make_many(self.boto3_raw_data["rules"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTopicRulesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTopicRulesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LocationAction:
    boto3_raw_data: "type_defs.LocationActionTypeDef" = dataclasses.field()

    roleArn = field("roleArn")
    trackerName = field("trackerName")
    deviceId = field("deviceId")
    latitude = field("latitude")
    longitude = field("longitude")

    @cached_property
    def timestamp(self):  # pragma: no cover
        return LocationTimestamp.make_one(self.boto3_raw_data["timestamp"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LocationActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LocationActionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LogTargetConfiguration:
    boto3_raw_data: "type_defs.LogTargetConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def logTarget(self):  # pragma: no cover
        return LogTarget.make_one(self.boto3_raw_data["logTarget"])

    logLevel = field("logLevel")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LogTargetConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LogTargetConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetV2LoggingLevelRequest:
    boto3_raw_data: "type_defs.SetV2LoggingLevelRequestTypeDef" = dataclasses.field()

    @cached_property
    def logTarget(self):  # pragma: no cover
        return LogTarget.make_one(self.boto3_raw_data["logTarget"])

    logLevel = field("logLevel")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SetV2LoggingLevelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetV2LoggingLevelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetLoggingOptionsRequest:
    boto3_raw_data: "type_defs.SetLoggingOptionsRequestTypeDef" = dataclasses.field()

    @cached_property
    def loggingOptionsPayload(self):  # pragma: no cover
        return LoggingOptionsPayload.make_one(
            self.boto3_raw_data["loggingOptionsPayload"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SetLoggingOptionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetLoggingOptionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MitigationActionParamsOutput:
    boto3_raw_data: "type_defs.MitigationActionParamsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def updateDeviceCertificateParams(self):  # pragma: no cover
        return UpdateDeviceCertificateParams.make_one(
            self.boto3_raw_data["updateDeviceCertificateParams"]
        )

    @cached_property
    def updateCACertificateParams(self):  # pragma: no cover
        return UpdateCACertificateParams.make_one(
            self.boto3_raw_data["updateCACertificateParams"]
        )

    @cached_property
    def addThingsToThingGroupParams(self):  # pragma: no cover
        return AddThingsToThingGroupParamsOutput.make_one(
            self.boto3_raw_data["addThingsToThingGroupParams"]
        )

    @cached_property
    def replaceDefaultPolicyVersionParams(self):  # pragma: no cover
        return ReplaceDefaultPolicyVersionParams.make_one(
            self.boto3_raw_data["replaceDefaultPolicyVersionParams"]
        )

    @cached_property
    def enableIoTLoggingParams(self):  # pragma: no cover
        return EnableIoTLoggingParams.make_one(
            self.boto3_raw_data["enableIoTLoggingParams"]
        )

    @cached_property
    def publishFindingToSnsParams(self):  # pragma: no cover
        return PublishFindingToSnsParams.make_one(
            self.boto3_raw_data["publishFindingToSnsParams"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MitigationActionParamsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MitigationActionParamsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MitigationActionParams:
    boto3_raw_data: "type_defs.MitigationActionParamsTypeDef" = dataclasses.field()

    @cached_property
    def updateDeviceCertificateParams(self):  # pragma: no cover
        return UpdateDeviceCertificateParams.make_one(
            self.boto3_raw_data["updateDeviceCertificateParams"]
        )

    @cached_property
    def updateCACertificateParams(self):  # pragma: no cover
        return UpdateCACertificateParams.make_one(
            self.boto3_raw_data["updateCACertificateParams"]
        )

    @cached_property
    def addThingsToThingGroupParams(self):  # pragma: no cover
        return AddThingsToThingGroupParams.make_one(
            self.boto3_raw_data["addThingsToThingGroupParams"]
        )

    @cached_property
    def replaceDefaultPolicyVersionParams(self):  # pragma: no cover
        return ReplaceDefaultPolicyVersionParams.make_one(
            self.boto3_raw_data["replaceDefaultPolicyVersionParams"]
        )

    @cached_property
    def enableIoTLoggingParams(self):  # pragma: no cover
        return EnableIoTLoggingParams.make_one(
            self.boto3_raw_data["enableIoTLoggingParams"]
        )

    @cached_property
    def publishFindingToSnsParams(self):  # pragma: no cover
        return PublishFindingToSnsParams.make_one(
            self.boto3_raw_data["publishFindingToSnsParams"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MitigationActionParamsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MitigationActionParamsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Mqtt5ConfigurationOutput:
    boto3_raw_data: "type_defs.Mqtt5ConfigurationOutputTypeDef" = dataclasses.field()

    @cached_property
    def propagatingAttributes(self):  # pragma: no cover
        return PropagatingAttribute.make_many(
            self.boto3_raw_data["propagatingAttributes"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.Mqtt5ConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Mqtt5ConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Mqtt5Configuration:
    boto3_raw_data: "type_defs.Mqtt5ConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def propagatingAttributes(self):  # pragma: no cover
        return PropagatingAttribute.make_many(
            self.boto3_raw_data["propagatingAttributes"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.Mqtt5ConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Mqtt5ConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MqttHeadersOutput:
    boto3_raw_data: "type_defs.MqttHeadersOutputTypeDef" = dataclasses.field()

    payloadFormatIndicator = field("payloadFormatIndicator")
    contentType = field("contentType")
    responseTopic = field("responseTopic")
    correlationData = field("correlationData")
    messageExpiry = field("messageExpiry")

    @cached_property
    def userProperties(self):  # pragma: no cover
        return UserProperty.make_many(self.boto3_raw_data["userProperties"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MqttHeadersOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MqttHeadersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MqttHeaders:
    boto3_raw_data: "type_defs.MqttHeadersTypeDef" = dataclasses.field()

    payloadFormatIndicator = field("payloadFormatIndicator")
    contentType = field("contentType")
    responseTopic = field("responseTopic")
    correlationData = field("correlationData")
    messageExpiry = field("messageExpiry")

    @cached_property
    def userProperties(self):  # pragma: no cover
        return UserProperty.make_many(self.boto3_raw_data["userProperties"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MqttHeadersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MqttHeadersTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceIdentifier:
    boto3_raw_data: "type_defs.ResourceIdentifierTypeDef" = dataclasses.field()

    deviceCertificateId = field("deviceCertificateId")
    caCertificateId = field("caCertificateId")
    cognitoIdentityPoolId = field("cognitoIdentityPoolId")
    clientId = field("clientId")

    @cached_property
    def policyVersionIdentifier(self):  # pragma: no cover
        return PolicyVersionIdentifier.make_one(
            self.boto3_raw_data["policyVersionIdentifier"]
        )

    account = field("account")
    iamRoleArn = field("iamRoleArn")
    roleAliasArn = field("roleAliasArn")

    @cached_property
    def issuerCertificateIdentifier(self):  # pragma: no cover
        return IssuerCertificateIdentifier.make_one(
            self.boto3_raw_data["issuerCertificateIdentifier"]
        )

    deviceCertificateArn = field("deviceCertificateArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceIdentifierTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceIdentifierTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ThingDocument:
    boto3_raw_data: "type_defs.ThingDocumentTypeDef" = dataclasses.field()

    thingName = field("thingName")
    thingId = field("thingId")
    thingTypeName = field("thingTypeName")
    thingGroupNames = field("thingGroupNames")
    attributes = field("attributes")
    shadow = field("shadow")
    deviceDefender = field("deviceDefender")

    @cached_property
    def connectivity(self):  # pragma: no cover
        return ThingConnectivity.make_one(self.boto3_raw_data["connectivity"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ThingDocumentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ThingDocumentTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimestreamActionOutput:
    boto3_raw_data: "type_defs.TimestreamActionOutputTypeDef" = dataclasses.field()

    roleArn = field("roleArn")
    databaseName = field("databaseName")
    tableName = field("tableName")

    @cached_property
    def dimensions(self):  # pragma: no cover
        return TimestreamDimension.make_many(self.boto3_raw_data["dimensions"])

    @cached_property
    def timestamp(self):  # pragma: no cover
        return TimestreamTimestamp.make_one(self.boto3_raw_data["timestamp"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TimestreamActionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimestreamActionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimestreamAction:
    boto3_raw_data: "type_defs.TimestreamActionTypeDef" = dataclasses.field()

    roleArn = field("roleArn")
    databaseName = field("databaseName")
    tableName = field("tableName")

    @cached_property
    def dimensions(self):  # pragma: no cover
        return TimestreamDimension.make_many(self.boto3_raw_data["dimensions"])

    @cached_property
    def timestamp(self):  # pragma: no cover
        return TimestreamTimestamp.make_one(self.boto3_raw_data["timestamp"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TimestreamActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimestreamActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TopicRuleDestinationConfiguration:
    boto3_raw_data: "type_defs.TopicRuleDestinationConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def httpUrlConfiguration(self):  # pragma: no cover
        return HttpUrlDestinationConfiguration.make_one(
            self.boto3_raw_data["httpUrlConfiguration"]
        )

    @cached_property
    def vpcConfiguration(self):  # pragma: no cover
        return VpcDestinationConfiguration.make_one(
            self.boto3_raw_data["vpcConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TopicRuleDestinationConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TopicRuleDestinationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TopicRuleDestinationSummary:
    boto3_raw_data: "type_defs.TopicRuleDestinationSummaryTypeDef" = dataclasses.field()

    arn = field("arn")
    status = field("status")
    createdAt = field("createdAt")
    lastUpdatedAt = field("lastUpdatedAt")
    statusReason = field("statusReason")

    @cached_property
    def httpUrlSummary(self):  # pragma: no cover
        return HttpUrlDestinationSummary.make_one(self.boto3_raw_data["httpUrlSummary"])

    @cached_property
    def vpcDestinationSummary(self):  # pragma: no cover
        return VpcDestinationSummary.make_one(
            self.boto3_raw_data["vpcDestinationSummary"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TopicRuleDestinationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TopicRuleDestinationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TopicRuleDestination:
    boto3_raw_data: "type_defs.TopicRuleDestinationTypeDef" = dataclasses.field()

    arn = field("arn")
    status = field("status")
    createdAt = field("createdAt")
    lastUpdatedAt = field("lastUpdatedAt")
    statusReason = field("statusReason")

    @cached_property
    def httpUrlProperties(self):  # pragma: no cover
        return HttpUrlDestinationProperties.make_one(
            self.boto3_raw_data["httpUrlProperties"]
        )

    @cached_property
    def vpcProperties(self):  # pragma: no cover
        return VpcDestinationProperties.make_one(self.boto3_raw_data["vpcProperties"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TopicRuleDestinationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TopicRuleDestinationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValidateSecurityProfileBehaviorsResponse:
    boto3_raw_data: "type_defs.ValidateSecurityProfileBehaviorsResponseTypeDef" = (
        dataclasses.field()
    )

    valid = field("valid")

    @cached_property
    def validationErrors(self):  # pragma: no cover
        return ValidationError.make_many(self.boto3_raw_data["validationErrors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ValidateSecurityProfileBehaviorsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValidateSecurityProfileBehaviorsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMetricValuesResponse:
    boto3_raw_data: "type_defs.ListMetricValuesResponseTypeDef" = dataclasses.field()

    @cached_property
    def metricDatumList(self):  # pragma: no cover
        return MetricDatum.make_many(self.boto3_raw_data["metricDatumList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMetricValuesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMetricValuesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFleetMetricRequest:
    boto3_raw_data: "type_defs.CreateFleetMetricRequestTypeDef" = dataclasses.field()

    metricName = field("metricName")
    queryString = field("queryString")
    aggregationType = field("aggregationType")
    period = field("period")
    aggregationField = field("aggregationField")
    description = field("description")
    queryVersion = field("queryVersion")
    indexName = field("indexName")
    unit = field("unit")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFleetMetricRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFleetMetricRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFleetMetricRequest:
    boto3_raw_data: "type_defs.UpdateFleetMetricRequestTypeDef" = dataclasses.field()

    metricName = field("metricName")
    indexName = field("indexName")
    queryString = field("queryString")
    aggregationType = field("aggregationType")
    period = field("period")
    aggregationField = field("aggregationField")
    description = field("description")
    queryVersion = field("queryVersion")
    unit = field("unit")
    expectedVersion = field("expectedVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFleetMetricRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFleetMetricRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Denied:
    boto3_raw_data: "type_defs.DeniedTypeDef" = dataclasses.field()

    @cached_property
    def implicitDeny(self):  # pragma: no cover
        return ImplicitDeny.make_one(self.boto3_raw_data["implicitDeny"])

    @cached_property
    def explicitDeny(self):  # pragma: no cover
        return ExplicitDeny.make_one(self.boto3_raw_data["explicitDeny"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeniedTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeniedTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutAssetPropertyValueEntryOutput:
    boto3_raw_data: "type_defs.PutAssetPropertyValueEntryOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def propertyValues(self):  # pragma: no cover
        return AssetPropertyValue.make_many(self.boto3_raw_data["propertyValues"])

    entryId = field("entryId")
    assetId = field("assetId")
    propertyId = field("propertyId")
    propertyAlias = field("propertyAlias")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutAssetPropertyValueEntryOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutAssetPropertyValueEntryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutAssetPropertyValueEntry:
    boto3_raw_data: "type_defs.PutAssetPropertyValueEntryTypeDef" = dataclasses.field()

    @cached_property
    def propertyValues(self):  # pragma: no cover
        return AssetPropertyValue.make_many(self.boto3_raw_data["propertyValues"])

    entryId = field("entryId")
    assetId = field("assetId")
    propertyId = field("propertyId")
    propertyAlias = field("propertyAlias")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutAssetPropertyValueEntryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutAssetPropertyValueEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateThingRequest:
    boto3_raw_data: "type_defs.CreateThingRequestTypeDef" = dataclasses.field()

    thingName = field("thingName")
    thingTypeName = field("thingTypeName")
    attributePayload = field("attributePayload")
    billingGroupName = field("billingGroupName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateThingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateThingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateThingRequest:
    boto3_raw_data: "type_defs.UpdateThingRequestTypeDef" = dataclasses.field()

    thingName = field("thingName")
    thingTypeName = field("thingTypeName")
    attributePayload = field("attributePayload")
    expectedVersion = field("expectedVersion")
    removeThingType = field("removeThingType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateThingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateThingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAccountAuditConfigurationRequest:
    boto3_raw_data: "type_defs.UpdateAccountAuditConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    roleArn = field("roleArn")
    auditNotificationTargetConfigurations = field(
        "auditNotificationTargetConfigurations"
    )
    auditCheckConfigurations = field("auditCheckConfigurations")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateAccountAuditConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAccountAuditConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartAuditMitigationActionsTaskRequest:
    boto3_raw_data: "type_defs.StartAuditMitigationActionsTaskRequestTypeDef" = (
        dataclasses.field()
    )

    taskId = field("taskId")
    target = field("target")
    auditCheckToActionsMapping = field("auditCheckToActionsMapping")
    clientRequestToken = field("clientRequestToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartAuditMitigationActionsTaskRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartAuditMitigationActionsTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestAuthorizationRequest:
    boto3_raw_data: "type_defs.TestAuthorizationRequestTypeDef" = dataclasses.field()

    authInfos = field("authInfos")
    principal = field("principal")
    cognitoIdentityPoolId = field("cognitoIdentityPoolId")
    clientId = field("clientId")
    policyNamesToAdd = field("policyNamesToAdd")
    policyNamesToSkip = field("policyNamesToSkip")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestAuthorizationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestAuthorizationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AwsJobExecutionsRolloutConfig:
    boto3_raw_data: "type_defs.AwsJobExecutionsRolloutConfigTypeDef" = (
        dataclasses.field()
    )

    maximumPerMinute = field("maximumPerMinute")

    @cached_property
    def exponentialRate(self):  # pragma: no cover
        return AwsJobExponentialRolloutRate.make_one(
            self.boto3_raw_data["exponentialRate"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AwsJobExecutionsRolloutConfigTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AwsJobExecutionsRolloutConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BehaviorOutput:
    boto3_raw_data: "type_defs.BehaviorOutputTypeDef" = dataclasses.field()

    name = field("name")
    metric = field("metric")

    @cached_property
    def metricDimension(self):  # pragma: no cover
        return MetricDimension.make_one(self.boto3_raw_data["metricDimension"])

    @cached_property
    def criteria(self):  # pragma: no cover
        return BehaviorCriteriaOutput.make_one(self.boto3_raw_data["criteria"])

    suppressAlerts = field("suppressAlerts")
    exportMetric = field("exportMetric")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BehaviorOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BehaviorOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestInvokeAuthorizerRequest:
    boto3_raw_data: "type_defs.TestInvokeAuthorizerRequestTypeDef" = dataclasses.field()

    authorizerName = field("authorizerName")
    token = field("token")
    tokenSignature = field("tokenSignature")

    @cached_property
    def httpContext(self):  # pragma: no cover
        return HttpContext.make_one(self.boto3_raw_data["httpContext"])

    @cached_property
    def mqttContext(self):  # pragma: no cover
        return MqttContext.make_one(self.boto3_raw_data["mqttContext"])

    @cached_property
    def tlsContext(self):  # pragma: no cover
        return TlsContext.make_one(self.boto3_raw_data["tlsContext"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestInvokeAuthorizerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestInvokeAuthorizerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketsAggregationRequest:
    boto3_raw_data: "type_defs.GetBucketsAggregationRequestTypeDef" = (
        dataclasses.field()
    )

    queryString = field("queryString")
    aggregationField = field("aggregationField")

    @cached_property
    def bucketsAggregationType(self):  # pragma: no cover
        return BucketsAggregationType.make_one(
            self.boto3_raw_data["bucketsAggregationType"]
        )

    indexName = field("indexName")
    queryVersion = field("queryVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBucketsAggregationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketsAggregationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCACertificateResponse:
    boto3_raw_data: "type_defs.DescribeCACertificateResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def certificateDescription(self):  # pragma: no cover
        return CACertificateDescription.make_one(
            self.boto3_raw_data["certificateDescription"]
        )

    @cached_property
    def registrationConfig(self):  # pragma: no cover
        return RegistrationConfig.make_one(self.boto3_raw_data["registrationConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeCACertificateResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCACertificateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCertificateResponse:
    boto3_raw_data: "type_defs.DescribeCertificateResponseTypeDef" = dataclasses.field()

    @cached_property
    def certificateDescription(self):  # pragma: no cover
        return CertificateDescription.make_one(
            self.boto3_raw_data["certificateDescription"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeCertificateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCertificateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCommandResponse:
    boto3_raw_data: "type_defs.GetCommandResponseTypeDef" = dataclasses.field()

    commandId = field("commandId")
    commandArn = field("commandArn")
    namespace = field("namespace")
    displayName = field("displayName")
    description = field("description")

    @cached_property
    def mandatoryParameters(self):  # pragma: no cover
        return CommandParameterOutput.make_many(
            self.boto3_raw_data["mandatoryParameters"]
        )

    @cached_property
    def payload(self):  # pragma: no cover
        return CommandPayloadOutput.make_one(self.boto3_raw_data["payload"])

    roleArn = field("roleArn")
    createdAt = field("createdAt")
    lastUpdatedAt = field("lastUpdatedAt")
    deprecated = field("deprecated")
    pendingDeletion = field("pendingDeletion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCommandResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCommandResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartSigningJobParameter:
    boto3_raw_data: "type_defs.StartSigningJobParameterTypeDef" = dataclasses.field()

    @cached_property
    def signingProfileParameter(self):  # pragma: no cover
        return SigningProfileParameter.make_one(
            self.boto3_raw_data["signingProfileParameter"]
        )

    signingProfileName = field("signingProfileName")

    @cached_property
    def destination(self):  # pragma: no cover
        return Destination.make_one(self.boto3_raw_data["destination"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartSigningJobParameterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSigningJobParameterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobExecutionsRolloutConfig:
    boto3_raw_data: "type_defs.JobExecutionsRolloutConfigTypeDef" = dataclasses.field()

    maximumPerMinute = field("maximumPerMinute")

    @cached_property
    def exponentialRate(self):  # pragma: no cover
        return ExponentialRolloutRate.make_one(self.boto3_raw_data["exponentialRate"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JobExecutionsRolloutConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobExecutionsRolloutConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePackageVersionRequest:
    boto3_raw_data: "type_defs.CreatePackageVersionRequestTypeDef" = dataclasses.field()

    packageName = field("packageName")
    versionName = field("versionName")
    description = field("description")
    attributes = field("attributes")

    @cached_property
    def artifact(self):  # pragma: no cover
        return PackageVersionArtifact.make_one(self.boto3_raw_data["artifact"])

    recipe = field("recipe")
    tags = field("tags")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePackageVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePackageVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePackageVersionRequest:
    boto3_raw_data: "type_defs.UpdatePackageVersionRequestTypeDef" = dataclasses.field()

    packageName = field("packageName")
    versionName = field("versionName")
    description = field("description")
    attributes = field("attributes")

    @cached_property
    def artifact(self):  # pragma: no cover
        return PackageVersionArtifact.make_one(self.boto3_raw_data["artifact"])

    action = field("action")
    recipe = field("recipe")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePackageVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePackageVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateSbomWithPackageVersionRequest:
    boto3_raw_data: "type_defs.AssociateSbomWithPackageVersionRequestTypeDef" = (
        dataclasses.field()
    )

    packageName = field("packageName")
    versionName = field("versionName")

    @cached_property
    def sbom(self):  # pragma: no cover
        return Sbom.make_one(self.boto3_raw_data["sbom"])

    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateSbomWithPackageVersionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateSbomWithPackageVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateSbomWithPackageVersionResponse:
    boto3_raw_data: "type_defs.AssociateSbomWithPackageVersionResponseTypeDef" = (
        dataclasses.field()
    )

    packageName = field("packageName")
    versionName = field("versionName")

    @cached_property
    def sbom(self):  # pragma: no cover
        return Sbom.make_one(self.boto3_raw_data["sbom"])

    sbomValidationStatus = field("sbomValidationStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateSbomWithPackageVersionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateSbomWithPackageVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPackageVersionResponse:
    boto3_raw_data: "type_defs.GetPackageVersionResponseTypeDef" = dataclasses.field()

    packageVersionArn = field("packageVersionArn")
    packageName = field("packageName")
    versionName = field("versionName")
    description = field("description")
    attributes = field("attributes")

    @cached_property
    def artifact(self):  # pragma: no cover
        return PackageVersionArtifact.make_one(self.boto3_raw_data["artifact"])

    status = field("status")
    errorReason = field("errorReason")
    creationDate = field("creationDate")
    lastModifiedDate = field("lastModifiedDate")

    @cached_property
    def sbom(self):  # pragma: no cover
        return Sbom.make_one(self.boto3_raw_data["sbom"])

    sbomValidationStatus = field("sbomValidationStatus")
    recipe = field("recipe")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPackageVersionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPackageVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateStreamRequest:
    boto3_raw_data: "type_defs.CreateStreamRequestTypeDef" = dataclasses.field()

    streamId = field("streamId")

    @cached_property
    def files(self):  # pragma: no cover
        return StreamFile.make_many(self.boto3_raw_data["files"])

    roleArn = field("roleArn")
    description = field("description")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateStreamRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateStreamRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StreamInfo:
    boto3_raw_data: "type_defs.StreamInfoTypeDef" = dataclasses.field()

    streamId = field("streamId")
    streamArn = field("streamArn")
    streamVersion = field("streamVersion")
    description = field("description")

    @cached_property
    def files(self):  # pragma: no cover
        return StreamFile.make_many(self.boto3_raw_data["files"])

    createdAt = field("createdAt")
    lastUpdatedAt = field("lastUpdatedAt")
    roleArn = field("roleArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StreamInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StreamInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateStreamRequest:
    boto3_raw_data: "type_defs.UpdateStreamRequestTypeDef" = dataclasses.field()

    streamId = field("streamId")
    description = field("description")

    @cached_property
    def files(self):  # pragma: no cover
        return StreamFile.make_many(self.boto3_raw_data["files"])

    roleArn = field("roleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateStreamRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateStreamRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ThingIndexingConfigurationOutput:
    boto3_raw_data: "type_defs.ThingIndexingConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    thingIndexingMode = field("thingIndexingMode")
    thingConnectivityIndexingMode = field("thingConnectivityIndexingMode")
    deviceDefenderIndexingMode = field("deviceDefenderIndexingMode")
    namedShadowIndexingMode = field("namedShadowIndexingMode")

    @cached_property
    def managedFields(self):  # pragma: no cover
        return Field.make_many(self.boto3_raw_data["managedFields"])

    @cached_property
    def customFields(self):  # pragma: no cover
        return Field.make_many(self.boto3_raw_data["customFields"])

    @cached_property
    def filter(self):  # pragma: no cover
        return IndexingFilterOutput.make_one(self.boto3_raw_data["filter"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ThingIndexingConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ThingIndexingConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ThingIndexingConfiguration:
    boto3_raw_data: "type_defs.ThingIndexingConfigurationTypeDef" = dataclasses.field()

    thingIndexingMode = field("thingIndexingMode")
    thingConnectivityIndexingMode = field("thingConnectivityIndexingMode")
    deviceDefenderIndexingMode = field("deviceDefenderIndexingMode")
    namedShadowIndexingMode = field("namedShadowIndexingMode")

    @cached_property
    def managedFields(self):  # pragma: no cover
        return Field.make_many(self.boto3_raw_data["managedFields"])

    @cached_property
    def customFields(self):  # pragma: no cover
        return Field.make_many(self.boto3_raw_data["customFields"])

    @cached_property
    def filter(self):  # pragma: no cover
        return IndexingFilter.make_one(self.boto3_raw_data["filter"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ThingIndexingConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ThingIndexingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeThingGroupResponse:
    boto3_raw_data: "type_defs.DescribeThingGroupResponseTypeDef" = dataclasses.field()

    thingGroupName = field("thingGroupName")
    thingGroupId = field("thingGroupId")
    thingGroupArn = field("thingGroupArn")
    version = field("version")

    @cached_property
    def thingGroupProperties(self):  # pragma: no cover
        return ThingGroupPropertiesOutput.make_one(
            self.boto3_raw_data["thingGroupProperties"]
        )

    @cached_property
    def thingGroupMetadata(self):  # pragma: no cover
        return ThingGroupMetadata.make_one(self.boto3_raw_data["thingGroupMetadata"])

    indexName = field("indexName")
    queryString = field("queryString")
    queryVersion = field("queryVersion")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeThingGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeThingGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HttpActionOutput:
    boto3_raw_data: "type_defs.HttpActionOutputTypeDef" = dataclasses.field()

    url = field("url")
    confirmationUrl = field("confirmationUrl")

    @cached_property
    def headers(self):  # pragma: no cover
        return HttpActionHeader.make_many(self.boto3_raw_data["headers"])

    @cached_property
    def auth(self):  # pragma: no cover
        return HttpAuthorization.make_one(self.boto3_raw_data["auth"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HttpActionOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HttpActionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HttpAction:
    boto3_raw_data: "type_defs.HttpActionTypeDef" = dataclasses.field()

    url = field("url")
    confirmationUrl = field("confirmationUrl")

    @cached_property
    def headers(self):  # pragma: no cover
        return HttpActionHeader.make_many(self.boto3_raw_data["headers"])

    @cached_property
    def auth(self):  # pragma: no cover
        return HttpAuthorization.make_one(self.boto3_raw_data["auth"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HttpActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HttpActionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeJobExecutionResponse:
    boto3_raw_data: "type_defs.DescribeJobExecutionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def execution(self):  # pragma: no cover
        return JobExecution.make_one(self.boto3_raw_data["execution"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeJobExecutionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeJobExecutionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobExecutionsForJobResponse:
    boto3_raw_data: "type_defs.ListJobExecutionsForJobResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def executionSummaries(self):  # pragma: no cover
        return JobExecutionSummaryForJob.make_many(
            self.boto3_raw_data["executionSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListJobExecutionsForJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobExecutionsForJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobExecutionsForThingResponse:
    boto3_raw_data: "type_defs.ListJobExecutionsForThingResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def executionSummaries(self):  # pragma: no cover
        return JobExecutionSummaryForThing.make_many(
            self.boto3_raw_data["executionSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListJobExecutionsForThingResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobExecutionsForThingResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSecurityProfilesForTargetResponse:
    boto3_raw_data: "type_defs.ListSecurityProfilesForTargetResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def securityProfileTargetMappings(self):  # pragma: no cover
        return SecurityProfileTargetMapping.make_many(
            self.boto3_raw_data["securityProfileTargetMappings"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSecurityProfilesForTargetResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSecurityProfilesForTargetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListV2LoggingLevelsResponse:
    boto3_raw_data: "type_defs.ListV2LoggingLevelsResponseTypeDef" = dataclasses.field()

    @cached_property
    def logTargetConfigurations(self):  # pragma: no cover
        return LogTargetConfiguration.make_many(
            self.boto3_raw_data["logTargetConfigurations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListV2LoggingLevelsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListV2LoggingLevelsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BehaviorCriteria:
    boto3_raw_data: "type_defs.BehaviorCriteriaTypeDef" = dataclasses.field()

    comparisonOperator = field("comparisonOperator")
    value = field("value")
    durationSeconds = field("durationSeconds")
    consecutiveDatapointsToAlarm = field("consecutiveDatapointsToAlarm")
    consecutiveDatapointsToClear = field("consecutiveDatapointsToClear")

    @cached_property
    def statisticalThreshold(self):  # pragma: no cover
        return StatisticalThreshold.make_one(
            self.boto3_raw_data["statisticalThreshold"]
        )

    @cached_property
    def mlDetectionConfig(self):  # pragma: no cover
        return MachineLearningDetectionConfig.make_one(
            self.boto3_raw_data["mlDetectionConfig"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BehaviorCriteriaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BehaviorCriteriaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMitigationActionResponse:
    boto3_raw_data: "type_defs.DescribeMitigationActionResponseTypeDef" = (
        dataclasses.field()
    )

    actionName = field("actionName")
    actionType = field("actionType")
    actionArn = field("actionArn")
    actionId = field("actionId")
    roleArn = field("roleArn")

    @cached_property
    def actionParams(self):  # pragma: no cover
        return MitigationActionParamsOutput.make_one(
            self.boto3_raw_data["actionParams"]
        )

    creationDate = field("creationDate")
    lastModifiedDate = field("lastModifiedDate")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeMitigationActionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMitigationActionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MitigationAction:
    boto3_raw_data: "type_defs.MitigationActionTypeDef" = dataclasses.field()

    name = field("name")
    id = field("id")
    roleArn = field("roleArn")

    @cached_property
    def actionParams(self):  # pragma: no cover
        return MitigationActionParamsOutput.make_one(
            self.boto3_raw_data["actionParams"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MitigationActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MitigationActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ThingTypePropertiesOutput:
    boto3_raw_data: "type_defs.ThingTypePropertiesOutputTypeDef" = dataclasses.field()

    thingTypeDescription = field("thingTypeDescription")
    searchableAttributes = field("searchableAttributes")

    @cached_property
    def mqtt5Configuration(self):  # pragma: no cover
        return Mqtt5ConfigurationOutput.make_one(
            self.boto3_raw_data["mqtt5Configuration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ThingTypePropertiesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ThingTypePropertiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ThingTypeProperties:
    boto3_raw_data: "type_defs.ThingTypePropertiesTypeDef" = dataclasses.field()

    thingTypeDescription = field("thingTypeDescription")
    searchableAttributes = field("searchableAttributes")

    @cached_property
    def mqtt5Configuration(self):  # pragma: no cover
        return Mqtt5Configuration.make_one(self.boto3_raw_data["mqtt5Configuration"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ThingTypePropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ThingTypePropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RepublishActionOutput:
    boto3_raw_data: "type_defs.RepublishActionOutputTypeDef" = dataclasses.field()

    roleArn = field("roleArn")
    topic = field("topic")
    qos = field("qos")

    @cached_property
    def headers(self):  # pragma: no cover
        return MqttHeadersOutput.make_one(self.boto3_raw_data["headers"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RepublishActionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RepublishActionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuditSuppression:
    boto3_raw_data: "type_defs.AuditSuppressionTypeDef" = dataclasses.field()

    checkName = field("checkName")

    @cached_property
    def resourceIdentifier(self):  # pragma: no cover
        return ResourceIdentifier.make_one(self.boto3_raw_data["resourceIdentifier"])

    expirationDate = field("expirationDate")
    suppressIndefinitely = field("suppressIndefinitely")
    description = field("description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AuditSuppressionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuditSuppressionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAuditSuppressionRequest:
    boto3_raw_data: "type_defs.CreateAuditSuppressionRequestTypeDef" = (
        dataclasses.field()
    )

    checkName = field("checkName")

    @cached_property
    def resourceIdentifier(self):  # pragma: no cover
        return ResourceIdentifier.make_one(self.boto3_raw_data["resourceIdentifier"])

    clientRequestToken = field("clientRequestToken")
    expirationDate = field("expirationDate")
    suppressIndefinitely = field("suppressIndefinitely")
    description = field("description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateAuditSuppressionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAuditSuppressionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAuditSuppressionRequest:
    boto3_raw_data: "type_defs.DeleteAuditSuppressionRequestTypeDef" = (
        dataclasses.field()
    )

    checkName = field("checkName")

    @cached_property
    def resourceIdentifier(self):  # pragma: no cover
        return ResourceIdentifier.make_one(self.boto3_raw_data["resourceIdentifier"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteAuditSuppressionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAuditSuppressionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAuditSuppressionRequest:
    boto3_raw_data: "type_defs.DescribeAuditSuppressionRequestTypeDef" = (
        dataclasses.field()
    )

    checkName = field("checkName")

    @cached_property
    def resourceIdentifier(self):  # pragma: no cover
        return ResourceIdentifier.make_one(self.boto3_raw_data["resourceIdentifier"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeAuditSuppressionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAuditSuppressionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAuditSuppressionResponse:
    boto3_raw_data: "type_defs.DescribeAuditSuppressionResponseTypeDef" = (
        dataclasses.field()
    )

    checkName = field("checkName")

    @cached_property
    def resourceIdentifier(self):  # pragma: no cover
        return ResourceIdentifier.make_one(self.boto3_raw_data["resourceIdentifier"])

    expirationDate = field("expirationDate")
    suppressIndefinitely = field("suppressIndefinitely")
    description = field("description")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeAuditSuppressionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAuditSuppressionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAuditFindingsRequestPaginate:
    boto3_raw_data: "type_defs.ListAuditFindingsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    taskId = field("taskId")
    checkName = field("checkName")

    @cached_property
    def resourceIdentifier(self):  # pragma: no cover
        return ResourceIdentifier.make_one(self.boto3_raw_data["resourceIdentifier"])

    startTime = field("startTime")
    endTime = field("endTime")
    listSuppressedFindings = field("listSuppressedFindings")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAuditFindingsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAuditFindingsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAuditFindingsRequest:
    boto3_raw_data: "type_defs.ListAuditFindingsRequestTypeDef" = dataclasses.field()

    taskId = field("taskId")
    checkName = field("checkName")

    @cached_property
    def resourceIdentifier(self):  # pragma: no cover
        return ResourceIdentifier.make_one(self.boto3_raw_data["resourceIdentifier"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")
    startTime = field("startTime")
    endTime = field("endTime")
    listSuppressedFindings = field("listSuppressedFindings")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAuditFindingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAuditFindingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAuditSuppressionsRequestPaginate:
    boto3_raw_data: "type_defs.ListAuditSuppressionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    checkName = field("checkName")

    @cached_property
    def resourceIdentifier(self):  # pragma: no cover
        return ResourceIdentifier.make_one(self.boto3_raw_data["resourceIdentifier"])

    ascendingOrder = field("ascendingOrder")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAuditSuppressionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAuditSuppressionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAuditSuppressionsRequest:
    boto3_raw_data: "type_defs.ListAuditSuppressionsRequestTypeDef" = (
        dataclasses.field()
    )

    checkName = field("checkName")

    @cached_property
    def resourceIdentifier(self):  # pragma: no cover
        return ResourceIdentifier.make_one(self.boto3_raw_data["resourceIdentifier"])

    ascendingOrder = field("ascendingOrder")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAuditSuppressionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAuditSuppressionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NonCompliantResource:
    boto3_raw_data: "type_defs.NonCompliantResourceTypeDef" = dataclasses.field()

    resourceType = field("resourceType")

    @cached_property
    def resourceIdentifier(self):  # pragma: no cover
        return ResourceIdentifier.make_one(self.boto3_raw_data["resourceIdentifier"])

    additionalInfo = field("additionalInfo")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NonCompliantResourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NonCompliantResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RelatedResource:
    boto3_raw_data: "type_defs.RelatedResourceTypeDef" = dataclasses.field()

    resourceType = field("resourceType")

    @cached_property
    def resourceIdentifier(self):  # pragma: no cover
        return ResourceIdentifier.make_one(self.boto3_raw_data["resourceIdentifier"])

    additionalInfo = field("additionalInfo")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RelatedResourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RelatedResourceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAuditSuppressionRequest:
    boto3_raw_data: "type_defs.UpdateAuditSuppressionRequestTypeDef" = (
        dataclasses.field()
    )

    checkName = field("checkName")

    @cached_property
    def resourceIdentifier(self):  # pragma: no cover
        return ResourceIdentifier.make_one(self.boto3_raw_data["resourceIdentifier"])

    expirationDate = field("expirationDate")
    suppressIndefinitely = field("suppressIndefinitely")
    description = field("description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateAuditSuppressionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAuditSuppressionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchIndexResponse:
    boto3_raw_data: "type_defs.SearchIndexResponseTypeDef" = dataclasses.field()

    @cached_property
    def things(self):  # pragma: no cover
        return ThingDocument.make_many(self.boto3_raw_data["things"])

    @cached_property
    def thingGroups(self):  # pragma: no cover
        return ThingGroupDocument.make_many(self.boto3_raw_data["thingGroups"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchIndexResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchIndexResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTopicRuleDestinationRequest:
    boto3_raw_data: "type_defs.CreateTopicRuleDestinationRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def destinationConfiguration(self):  # pragma: no cover
        return TopicRuleDestinationConfiguration.make_one(
            self.boto3_raw_data["destinationConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateTopicRuleDestinationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTopicRuleDestinationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTopicRuleDestinationsResponse:
    boto3_raw_data: "type_defs.ListTopicRuleDestinationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def destinationSummaries(self):  # pragma: no cover
        return TopicRuleDestinationSummary.make_many(
            self.boto3_raw_data["destinationSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTopicRuleDestinationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTopicRuleDestinationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTopicRuleDestinationResponse:
    boto3_raw_data: "type_defs.CreateTopicRuleDestinationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def topicRuleDestination(self):  # pragma: no cover
        return TopicRuleDestination.make_one(
            self.boto3_raw_data["topicRuleDestination"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateTopicRuleDestinationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTopicRuleDestinationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTopicRuleDestinationResponse:
    boto3_raw_data: "type_defs.GetTopicRuleDestinationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def topicRuleDestination(self):  # pragma: no cover
        return TopicRuleDestination.make_one(
            self.boto3_raw_data["topicRuleDestination"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetTopicRuleDestinationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTopicRuleDestinationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthResult:
    boto3_raw_data: "type_defs.AuthResultTypeDef" = dataclasses.field()

    @cached_property
    def authInfo(self):  # pragma: no cover
        return AuthInfoOutput.make_one(self.boto3_raw_data["authInfo"])

    @cached_property
    def allowed(self):  # pragma: no cover
        return Allowed.make_one(self.boto3_raw_data["allowed"])

    @cached_property
    def denied(self):  # pragma: no cover
        return Denied.make_one(self.boto3_raw_data["denied"])

    authDecision = field("authDecision")
    missingContextValues = field("missingContextValues")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AuthResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AuthResultTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IotSiteWiseActionOutput:
    boto3_raw_data: "type_defs.IotSiteWiseActionOutputTypeDef" = dataclasses.field()

    @cached_property
    def putAssetPropertyValueEntries(self):  # pragma: no cover
        return PutAssetPropertyValueEntryOutput.make_many(
            self.boto3_raw_data["putAssetPropertyValueEntries"]
        )

    roleArn = field("roleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IotSiteWiseActionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IotSiteWiseActionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDynamicThingGroupRequest:
    boto3_raw_data: "type_defs.CreateDynamicThingGroupRequestTypeDef" = (
        dataclasses.field()
    )

    thingGroupName = field("thingGroupName")
    queryString = field("queryString")
    thingGroupProperties = field("thingGroupProperties")
    indexName = field("indexName")
    queryVersion = field("queryVersion")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateDynamicThingGroupRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDynamicThingGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateThingGroupRequest:
    boto3_raw_data: "type_defs.CreateThingGroupRequestTypeDef" = dataclasses.field()

    thingGroupName = field("thingGroupName")
    parentGroupName = field("parentGroupName")
    thingGroupProperties = field("thingGroupProperties")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateThingGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateThingGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDynamicThingGroupRequest:
    boto3_raw_data: "type_defs.UpdateDynamicThingGroupRequestTypeDef" = (
        dataclasses.field()
    )

    thingGroupName = field("thingGroupName")
    thingGroupProperties = field("thingGroupProperties")
    expectedVersion = field("expectedVersion")
    indexName = field("indexName")
    queryString = field("queryString")
    queryVersion = field("queryVersion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateDynamicThingGroupRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDynamicThingGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateThingGroupRequest:
    boto3_raw_data: "type_defs.UpdateThingGroupRequestTypeDef" = dataclasses.field()

    thingGroupName = field("thingGroupName")
    thingGroupProperties = field("thingGroupProperties")
    expectedVersion = field("expectedVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateThingGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateThingGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActiveViolation:
    boto3_raw_data: "type_defs.ActiveViolationTypeDef" = dataclasses.field()

    violationId = field("violationId")
    thingName = field("thingName")
    securityProfileName = field("securityProfileName")

    @cached_property
    def behavior(self):  # pragma: no cover
        return BehaviorOutput.make_one(self.boto3_raw_data["behavior"])

    @cached_property
    def lastViolationValue(self):  # pragma: no cover
        return MetricValueOutput.make_one(self.boto3_raw_data["lastViolationValue"])

    @cached_property
    def violationEventAdditionalInfo(self):  # pragma: no cover
        return ViolationEventAdditionalInfo.make_one(
            self.boto3_raw_data["violationEventAdditionalInfo"]
        )

    verificationState = field("verificationState")
    verificationStateDescription = field("verificationStateDescription")
    lastViolationTime = field("lastViolationTime")
    violationStartTime = field("violationStartTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActiveViolationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ActiveViolationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSecurityProfileResponse:
    boto3_raw_data: "type_defs.DescribeSecurityProfileResponseTypeDef" = (
        dataclasses.field()
    )

    securityProfileName = field("securityProfileName")
    securityProfileArn = field("securityProfileArn")
    securityProfileDescription = field("securityProfileDescription")

    @cached_property
    def behaviors(self):  # pragma: no cover
        return BehaviorOutput.make_many(self.boto3_raw_data["behaviors"])

    alertTargets = field("alertTargets")
    additionalMetricsToRetain = field("additionalMetricsToRetain")

    @cached_property
    def additionalMetricsToRetainV2(self):  # pragma: no cover
        return MetricToRetain.make_many(
            self.boto3_raw_data["additionalMetricsToRetainV2"]
        )

    version = field("version")
    creationDate = field("creationDate")
    lastModifiedDate = field("lastModifiedDate")

    @cached_property
    def metricsExportConfig(self):  # pragma: no cover
        return MetricsExportConfig.make_one(self.boto3_raw_data["metricsExportConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeSecurityProfileResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSecurityProfileResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSecurityProfileResponse:
    boto3_raw_data: "type_defs.UpdateSecurityProfileResponseTypeDef" = (
        dataclasses.field()
    )

    securityProfileName = field("securityProfileName")
    securityProfileArn = field("securityProfileArn")
    securityProfileDescription = field("securityProfileDescription")

    @cached_property
    def behaviors(self):  # pragma: no cover
        return BehaviorOutput.make_many(self.boto3_raw_data["behaviors"])

    alertTargets = field("alertTargets")
    additionalMetricsToRetain = field("additionalMetricsToRetain")

    @cached_property
    def additionalMetricsToRetainV2(self):  # pragma: no cover
        return MetricToRetain.make_many(
            self.boto3_raw_data["additionalMetricsToRetainV2"]
        )

    version = field("version")
    creationDate = field("creationDate")
    lastModifiedDate = field("lastModifiedDate")

    @cached_property
    def metricsExportConfig(self):  # pragma: no cover
        return MetricsExportConfig.make_one(self.boto3_raw_data["metricsExportConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateSecurityProfileResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSecurityProfileResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ViolationEvent:
    boto3_raw_data: "type_defs.ViolationEventTypeDef" = dataclasses.field()

    violationId = field("violationId")
    thingName = field("thingName")
    securityProfileName = field("securityProfileName")

    @cached_property
    def behavior(self):  # pragma: no cover
        return BehaviorOutput.make_one(self.boto3_raw_data["behavior"])

    @cached_property
    def metricValue(self):  # pragma: no cover
        return MetricValueOutput.make_one(self.boto3_raw_data["metricValue"])

    @cached_property
    def violationEventAdditionalInfo(self):  # pragma: no cover
        return ViolationEventAdditionalInfo.make_one(
            self.boto3_raw_data["violationEventAdditionalInfo"]
        )

    violationEventType = field("violationEventType")
    verificationState = field("verificationState")
    verificationStateDescription = field("verificationStateDescription")
    violationEventTime = field("violationEventTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ViolationEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ViolationEventTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomCodeSigning:
    boto3_raw_data: "type_defs.CustomCodeSigningTypeDef" = dataclasses.field()

    signature = field("signature")

    @cached_property
    def certificateChain(self):  # pragma: no cover
        return CodeSigningCertificateChain.make_one(
            self.boto3_raw_data["certificateChain"]
        )

    hashAlgorithm = field("hashAlgorithm")
    signatureAlgorithm = field("signatureAlgorithm")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CustomCodeSigningTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomCodeSigningTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CommandParameter:
    boto3_raw_data: "type_defs.CommandParameterTypeDef" = dataclasses.field()

    name = field("name")
    value = field("value")
    defaultValue = field("defaultValue")
    description = field("description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CommandParameterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CommandParameterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartDetectMitigationActionsTaskRequest:
    boto3_raw_data: "type_defs.StartDetectMitigationActionsTaskRequestTypeDef" = (
        dataclasses.field()
    )

    taskId = field("taskId")
    target = field("target")
    actions = field("actions")
    clientRequestToken = field("clientRequestToken")
    violationEventOccurrenceRange = field("violationEventOccurrenceRange")
    includeOnlyActiveViolations = field("includeOnlyActiveViolations")
    includeSuppressedAlerts = field("includeSuppressedAlerts")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartDetectMitigationActionsTaskRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartDetectMitigationActionsTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodeSigningOutput:
    boto3_raw_data: "type_defs.CodeSigningOutputTypeDef" = dataclasses.field()

    awsSignerJobId = field("awsSignerJobId")

    @cached_property
    def startSigningJobParameter(self):  # pragma: no cover
        return StartSigningJobParameter.make_one(
            self.boto3_raw_data["startSigningJobParameter"]
        )

    @cached_property
    def customCodeSigning(self):  # pragma: no cover
        return CustomCodeSigningOutput.make_one(
            self.boto3_raw_data["customCodeSigning"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CodeSigningOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodeSigningOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeJobTemplateResponse:
    boto3_raw_data: "type_defs.DescribeJobTemplateResponseTypeDef" = dataclasses.field()

    jobTemplateArn = field("jobTemplateArn")
    jobTemplateId = field("jobTemplateId")
    description = field("description")
    documentSource = field("documentSource")
    document = field("document")
    createdAt = field("createdAt")

    @cached_property
    def presignedUrlConfig(self):  # pragma: no cover
        return PresignedUrlConfig.make_one(self.boto3_raw_data["presignedUrlConfig"])

    @cached_property
    def jobExecutionsRolloutConfig(self):  # pragma: no cover
        return JobExecutionsRolloutConfig.make_one(
            self.boto3_raw_data["jobExecutionsRolloutConfig"]
        )

    @cached_property
    def abortConfig(self):  # pragma: no cover
        return AbortConfigOutput.make_one(self.boto3_raw_data["abortConfig"])

    @cached_property
    def timeoutConfig(self):  # pragma: no cover
        return TimeoutConfig.make_one(self.boto3_raw_data["timeoutConfig"])

    @cached_property
    def jobExecutionsRetryConfig(self):  # pragma: no cover
        return JobExecutionsRetryConfigOutput.make_one(
            self.boto3_raw_data["jobExecutionsRetryConfig"]
        )

    @cached_property
    def maintenanceWindows(self):  # pragma: no cover
        return MaintenanceWindow.make_many(self.boto3_raw_data["maintenanceWindows"])

    destinationPackageVersions = field("destinationPackageVersions")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeJobTemplateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeJobTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Job:
    boto3_raw_data: "type_defs.JobTypeDef" = dataclasses.field()

    jobArn = field("jobArn")
    jobId = field("jobId")
    targetSelection = field("targetSelection")
    status = field("status")
    forceCanceled = field("forceCanceled")
    reasonCode = field("reasonCode")
    comment = field("comment")
    targets = field("targets")
    description = field("description")

    @cached_property
    def presignedUrlConfig(self):  # pragma: no cover
        return PresignedUrlConfig.make_one(self.boto3_raw_data["presignedUrlConfig"])

    @cached_property
    def jobExecutionsRolloutConfig(self):  # pragma: no cover
        return JobExecutionsRolloutConfig.make_one(
            self.boto3_raw_data["jobExecutionsRolloutConfig"]
        )

    @cached_property
    def abortConfig(self):  # pragma: no cover
        return AbortConfigOutput.make_one(self.boto3_raw_data["abortConfig"])

    createdAt = field("createdAt")
    lastUpdatedAt = field("lastUpdatedAt")
    completedAt = field("completedAt")

    @cached_property
    def jobProcessDetails(self):  # pragma: no cover
        return JobProcessDetails.make_one(self.boto3_raw_data["jobProcessDetails"])

    @cached_property
    def timeoutConfig(self):  # pragma: no cover
        return TimeoutConfig.make_one(self.boto3_raw_data["timeoutConfig"])

    namespaceId = field("namespaceId")
    jobTemplateArn = field("jobTemplateArn")

    @cached_property
    def jobExecutionsRetryConfig(self):  # pragma: no cover
        return JobExecutionsRetryConfigOutput.make_one(
            self.boto3_raw_data["jobExecutionsRetryConfig"]
        )

    documentParameters = field("documentParameters")
    isConcurrent = field("isConcurrent")

    @cached_property
    def schedulingConfig(self):  # pragma: no cover
        return SchedulingConfigOutput.make_one(self.boto3_raw_data["schedulingConfig"])

    @cached_property
    def scheduledJobRollouts(self):  # pragma: no cover
        return ScheduledJobRollout.make_many(
            self.boto3_raw_data["scheduledJobRollouts"]
        )

    destinationPackageVersions = field("destinationPackageVersions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStreamResponse:
    boto3_raw_data: "type_defs.DescribeStreamResponseTypeDef" = dataclasses.field()

    @cached_property
    def streamInfo(self):  # pragma: no cover
        return StreamInfo.make_one(self.boto3_raw_data["streamInfo"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeStreamResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStreamResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIndexingConfigurationResponse:
    boto3_raw_data: "type_defs.GetIndexingConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def thingIndexingConfiguration(self):  # pragma: no cover
        return ThingIndexingConfigurationOutput.make_one(
            self.boto3_raw_data["thingIndexingConfiguration"]
        )

    @cached_property
    def thingGroupIndexingConfiguration(self):  # pragma: no cover
        return ThingGroupIndexingConfigurationOutput.make_one(
            self.boto3_raw_data["thingGroupIndexingConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetIndexingConfigurationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIndexingConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateJobRequest:
    boto3_raw_data: "type_defs.CreateJobRequestTypeDef" = dataclasses.field()

    jobId = field("jobId")
    targets = field("targets")
    documentSource = field("documentSource")
    document = field("document")
    description = field("description")

    @cached_property
    def presignedUrlConfig(self):  # pragma: no cover
        return PresignedUrlConfig.make_one(self.boto3_raw_data["presignedUrlConfig"])

    targetSelection = field("targetSelection")

    @cached_property
    def jobExecutionsRolloutConfig(self):  # pragma: no cover
        return JobExecutionsRolloutConfig.make_one(
            self.boto3_raw_data["jobExecutionsRolloutConfig"]
        )

    abortConfig = field("abortConfig")

    @cached_property
    def timeoutConfig(self):  # pragma: no cover
        return TimeoutConfig.make_one(self.boto3_raw_data["timeoutConfig"])

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    namespaceId = field("namespaceId")
    jobTemplateArn = field("jobTemplateArn")
    jobExecutionsRetryConfig = field("jobExecutionsRetryConfig")
    documentParameters = field("documentParameters")
    schedulingConfig = field("schedulingConfig")
    destinationPackageVersions = field("destinationPackageVersions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateJobRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateJobTemplateRequest:
    boto3_raw_data: "type_defs.CreateJobTemplateRequestTypeDef" = dataclasses.field()

    jobTemplateId = field("jobTemplateId")
    description = field("description")
    jobArn = field("jobArn")
    documentSource = field("documentSource")
    document = field("document")

    @cached_property
    def presignedUrlConfig(self):  # pragma: no cover
        return PresignedUrlConfig.make_one(self.boto3_raw_data["presignedUrlConfig"])

    @cached_property
    def jobExecutionsRolloutConfig(self):  # pragma: no cover
        return JobExecutionsRolloutConfig.make_one(
            self.boto3_raw_data["jobExecutionsRolloutConfig"]
        )

    abortConfig = field("abortConfig")

    @cached_property
    def timeoutConfig(self):  # pragma: no cover
        return TimeoutConfig.make_one(self.boto3_raw_data["timeoutConfig"])

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    jobExecutionsRetryConfig = field("jobExecutionsRetryConfig")

    @cached_property
    def maintenanceWindows(self):  # pragma: no cover
        return MaintenanceWindow.make_many(self.boto3_raw_data["maintenanceWindows"])

    destinationPackageVersions = field("destinationPackageVersions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateJobTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateJobTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateJobRequest:
    boto3_raw_data: "type_defs.UpdateJobRequestTypeDef" = dataclasses.field()

    jobId = field("jobId")
    description = field("description")

    @cached_property
    def presignedUrlConfig(self):  # pragma: no cover
        return PresignedUrlConfig.make_one(self.boto3_raw_data["presignedUrlConfig"])

    @cached_property
    def jobExecutionsRolloutConfig(self):  # pragma: no cover
        return JobExecutionsRolloutConfig.make_one(
            self.boto3_raw_data["jobExecutionsRolloutConfig"]
        )

    abortConfig = field("abortConfig")

    @cached_property
    def timeoutConfig(self):  # pragma: no cover
        return TimeoutConfig.make_one(self.boto3_raw_data["timeoutConfig"])

    namespaceId = field("namespaceId")
    jobExecutionsRetryConfig = field("jobExecutionsRetryConfig")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateJobRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAuditMitigationActionsTaskResponse:
    boto3_raw_data: "type_defs.DescribeAuditMitigationActionsTaskResponseTypeDef" = (
        dataclasses.field()
    )

    taskStatus = field("taskStatus")
    startTime = field("startTime")
    endTime = field("endTime")
    taskStatistics = field("taskStatistics")

    @cached_property
    def target(self):  # pragma: no cover
        return AuditMitigationActionsTaskTargetOutput.make_one(
            self.boto3_raw_data["target"]
        )

    auditCheckToActionsMapping = field("auditCheckToActionsMapping")

    @cached_property
    def actionsDefinition(self):  # pragma: no cover
        return MitigationAction.make_many(self.boto3_raw_data["actionsDefinition"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAuditMitigationActionsTaskResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAuditMitigationActionsTaskResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectMitigationActionsTaskSummary:
    boto3_raw_data: "type_defs.DetectMitigationActionsTaskSummaryTypeDef" = (
        dataclasses.field()
    )

    taskId = field("taskId")
    taskStatus = field("taskStatus")
    taskStartTime = field("taskStartTime")
    taskEndTime = field("taskEndTime")

    @cached_property
    def target(self):  # pragma: no cover
        return DetectMitigationActionsTaskTargetOutput.make_one(
            self.boto3_raw_data["target"]
        )

    @cached_property
    def violationEventOccurrenceRange(self):  # pragma: no cover
        return ViolationEventOccurrenceRangeOutput.make_one(
            self.boto3_raw_data["violationEventOccurrenceRange"]
        )

    onlyActiveViolationsIncluded = field("onlyActiveViolationsIncluded")
    suppressedAlertsIncluded = field("suppressedAlertsIncluded")

    @cached_property
    def actionsDefinition(self):  # pragma: no cover
        return MitigationAction.make_many(self.boto3_raw_data["actionsDefinition"])

    @cached_property
    def taskStatistics(self):  # pragma: no cover
        return DetectMitigationActionsTaskStatistics.make_one(
            self.boto3_raw_data["taskStatistics"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DetectMitigationActionsTaskSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectMitigationActionsTaskSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMitigationActionRequest:
    boto3_raw_data: "type_defs.CreateMitigationActionRequestTypeDef" = (
        dataclasses.field()
    )

    actionName = field("actionName")
    roleArn = field("roleArn")
    actionParams = field("actionParams")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateMitigationActionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMitigationActionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMitigationActionRequest:
    boto3_raw_data: "type_defs.UpdateMitigationActionRequestTypeDef" = (
        dataclasses.field()
    )

    actionName = field("actionName")
    roleArn = field("roleArn")
    actionParams = field("actionParams")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateMitigationActionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMitigationActionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeThingTypeResponse:
    boto3_raw_data: "type_defs.DescribeThingTypeResponseTypeDef" = dataclasses.field()

    thingTypeName = field("thingTypeName")
    thingTypeId = field("thingTypeId")
    thingTypeArn = field("thingTypeArn")

    @cached_property
    def thingTypeProperties(self):  # pragma: no cover
        return ThingTypePropertiesOutput.make_one(
            self.boto3_raw_data["thingTypeProperties"]
        )

    @cached_property
    def thingTypeMetadata(self):  # pragma: no cover
        return ThingTypeMetadata.make_one(self.boto3_raw_data["thingTypeMetadata"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeThingTypeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeThingTypeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ThingTypeDefinition:
    boto3_raw_data: "type_defs.ThingTypeDefinitionTypeDef" = dataclasses.field()

    thingTypeName = field("thingTypeName")
    thingTypeArn = field("thingTypeArn")

    @cached_property
    def thingTypeProperties(self):  # pragma: no cover
        return ThingTypePropertiesOutput.make_one(
            self.boto3_raw_data["thingTypeProperties"]
        )

    @cached_property
    def thingTypeMetadata(self):  # pragma: no cover
        return ThingTypeMetadata.make_one(self.boto3_raw_data["thingTypeMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ThingTypeDefinitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ThingTypeDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RepublishAction:
    boto3_raw_data: "type_defs.RepublishActionTypeDef" = dataclasses.field()

    roleArn = field("roleArn")
    topic = field("topic")
    qos = field("qos")
    headers = field("headers")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RepublishActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RepublishActionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAuditSuppressionsResponse:
    boto3_raw_data: "type_defs.ListAuditSuppressionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def suppressions(self):  # pragma: no cover
        return AuditSuppression.make_many(self.boto3_raw_data["suppressions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAuditSuppressionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAuditSuppressionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuditFinding:
    boto3_raw_data: "type_defs.AuditFindingTypeDef" = dataclasses.field()

    findingId = field("findingId")
    taskId = field("taskId")
    checkName = field("checkName")
    taskStartTime = field("taskStartTime")
    findingTime = field("findingTime")
    severity = field("severity")

    @cached_property
    def nonCompliantResource(self):  # pragma: no cover
        return NonCompliantResource.make_one(
            self.boto3_raw_data["nonCompliantResource"]
        )

    @cached_property
    def relatedResources(self):  # pragma: no cover
        return RelatedResource.make_many(self.boto3_raw_data["relatedResources"])

    reasonForNonCompliance = field("reasonForNonCompliance")
    reasonForNonComplianceCode = field("reasonForNonComplianceCode")
    isSuppressed = field("isSuppressed")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AuditFindingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AuditFindingTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRelatedResourcesForAuditFindingResponse:
    boto3_raw_data: "type_defs.ListRelatedResourcesForAuditFindingResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def relatedResources(self):  # pragma: no cover
        return RelatedResource.make_many(self.boto3_raw_data["relatedResources"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRelatedResourcesForAuditFindingResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRelatedResourcesForAuditFindingResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestAuthorizationResponse:
    boto3_raw_data: "type_defs.TestAuthorizationResponseTypeDef" = dataclasses.field()

    @cached_property
    def authResults(self):  # pragma: no cover
        return AuthResult.make_many(self.boto3_raw_data["authResults"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestAuthorizationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestAuthorizationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionOutput:
    boto3_raw_data: "type_defs.ActionOutputTypeDef" = dataclasses.field()

    @cached_property
    def dynamoDB(self):  # pragma: no cover
        return DynamoDBAction.make_one(self.boto3_raw_data["dynamoDB"])

    @cached_property
    def dynamoDBv2(self):  # pragma: no cover
        return DynamoDBv2Action.make_one(self.boto3_raw_data["dynamoDBv2"])

    @cached_property
    def lambda_(self):  # pragma: no cover
        return LambdaAction.make_one(self.boto3_raw_data["lambda"])

    @cached_property
    def sns(self):  # pragma: no cover
        return SnsAction.make_one(self.boto3_raw_data["sns"])

    @cached_property
    def sqs(self):  # pragma: no cover
        return SqsAction.make_one(self.boto3_raw_data["sqs"])

    @cached_property
    def kinesis(self):  # pragma: no cover
        return KinesisAction.make_one(self.boto3_raw_data["kinesis"])

    @cached_property
    def republish(self):  # pragma: no cover
        return RepublishActionOutput.make_one(self.boto3_raw_data["republish"])

    @cached_property
    def s3(self):  # pragma: no cover
        return S3Action.make_one(self.boto3_raw_data["s3"])

    @cached_property
    def firehose(self):  # pragma: no cover
        return FirehoseAction.make_one(self.boto3_raw_data["firehose"])

    @cached_property
    def cloudwatchMetric(self):  # pragma: no cover
        return CloudwatchMetricAction.make_one(self.boto3_raw_data["cloudwatchMetric"])

    @cached_property
    def cloudwatchAlarm(self):  # pragma: no cover
        return CloudwatchAlarmAction.make_one(self.boto3_raw_data["cloudwatchAlarm"])

    @cached_property
    def cloudwatchLogs(self):  # pragma: no cover
        return CloudwatchLogsAction.make_one(self.boto3_raw_data["cloudwatchLogs"])

    @cached_property
    def elasticsearch(self):  # pragma: no cover
        return ElasticsearchAction.make_one(self.boto3_raw_data["elasticsearch"])

    @cached_property
    def salesforce(self):  # pragma: no cover
        return SalesforceAction.make_one(self.boto3_raw_data["salesforce"])

    @cached_property
    def iotAnalytics(self):  # pragma: no cover
        return IotAnalyticsAction.make_one(self.boto3_raw_data["iotAnalytics"])

    @cached_property
    def iotEvents(self):  # pragma: no cover
        return IotEventsAction.make_one(self.boto3_raw_data["iotEvents"])

    @cached_property
    def iotSiteWise(self):  # pragma: no cover
        return IotSiteWiseActionOutput.make_one(self.boto3_raw_data["iotSiteWise"])

    @cached_property
    def stepFunctions(self):  # pragma: no cover
        return StepFunctionsAction.make_one(self.boto3_raw_data["stepFunctions"])

    @cached_property
    def timestream(self):  # pragma: no cover
        return TimestreamActionOutput.make_one(self.boto3_raw_data["timestream"])

    @cached_property
    def http(self):  # pragma: no cover
        return HttpActionOutput.make_one(self.boto3_raw_data["http"])

    @cached_property
    def kafka(self):  # pragma: no cover
        return KafkaActionOutput.make_one(self.boto3_raw_data["kafka"])

    @cached_property
    def openSearch(self):  # pragma: no cover
        return OpenSearchAction.make_one(self.boto3_raw_data["openSearch"])

    @cached_property
    def location(self):  # pragma: no cover
        return LocationAction.make_one(self.boto3_raw_data["location"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActionOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ActionOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IotSiteWiseAction:
    boto3_raw_data: "type_defs.IotSiteWiseActionTypeDef" = dataclasses.field()

    putAssetPropertyValueEntries = field("putAssetPropertyValueEntries")
    roleArn = field("roleArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IotSiteWiseActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IotSiteWiseActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListActiveViolationsResponse:
    boto3_raw_data: "type_defs.ListActiveViolationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def activeViolations(self):  # pragma: no cover
        return ActiveViolation.make_many(self.boto3_raw_data["activeViolations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListActiveViolationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListActiveViolationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListViolationEventsResponse:
    boto3_raw_data: "type_defs.ListViolationEventsResponseTypeDef" = dataclasses.field()

    @cached_property
    def violationEvents(self):  # pragma: no cover
        return ViolationEvent.make_many(self.boto3_raw_data["violationEvents"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListViolationEventsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListViolationEventsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OTAUpdateFileOutput:
    boto3_raw_data: "type_defs.OTAUpdateFileOutputTypeDef" = dataclasses.field()

    fileName = field("fileName")
    fileType = field("fileType")
    fileVersion = field("fileVersion")

    @cached_property
    def fileLocation(self):  # pragma: no cover
        return FileLocation.make_one(self.boto3_raw_data["fileLocation"])

    @cached_property
    def codeSigning(self):  # pragma: no cover
        return CodeSigningOutput.make_one(self.boto3_raw_data["codeSigning"])

    attributes = field("attributes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OTAUpdateFileOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OTAUpdateFileOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeJobResponse:
    boto3_raw_data: "type_defs.DescribeJobResponseTypeDef" = dataclasses.field()

    documentSource = field("documentSource")

    @cached_property
    def job(self):  # pragma: no cover
        return Job.make_one(self.boto3_raw_data["job"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateIndexingConfigurationRequest:
    boto3_raw_data: "type_defs.UpdateIndexingConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    thingIndexingConfiguration = field("thingIndexingConfiguration")
    thingGroupIndexingConfiguration = field("thingGroupIndexingConfiguration")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateIndexingConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateIndexingConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Behavior:
    boto3_raw_data: "type_defs.BehaviorTypeDef" = dataclasses.field()

    name = field("name")
    metric = field("metric")

    @cached_property
    def metricDimension(self):  # pragma: no cover
        return MetricDimension.make_one(self.boto3_raw_data["metricDimension"])

    criteria = field("criteria")
    suppressAlerts = field("suppressAlerts")
    exportMetric = field("exportMetric")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BehaviorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BehaviorTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDetectMitigationActionsTaskResponse:
    boto3_raw_data: "type_defs.DescribeDetectMitigationActionsTaskResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def taskSummary(self):  # pragma: no cover
        return DetectMitigationActionsTaskSummary.make_one(
            self.boto3_raw_data["taskSummary"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDetectMitigationActionsTaskResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDetectMitigationActionsTaskResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDetectMitigationActionsTasksResponse:
    boto3_raw_data: "type_defs.ListDetectMitigationActionsTasksResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def tasks(self):  # pragma: no cover
        return DetectMitigationActionsTaskSummary.make_many(
            self.boto3_raw_data["tasks"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDetectMitigationActionsTasksResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDetectMitigationActionsTasksResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListThingTypesResponse:
    boto3_raw_data: "type_defs.ListThingTypesResponseTypeDef" = dataclasses.field()

    @cached_property
    def thingTypes(self):  # pragma: no cover
        return ThingTypeDefinition.make_many(self.boto3_raw_data["thingTypes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListThingTypesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListThingTypesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateThingTypeRequest:
    boto3_raw_data: "type_defs.CreateThingTypeRequestTypeDef" = dataclasses.field()

    thingTypeName = field("thingTypeName")
    thingTypeProperties = field("thingTypeProperties")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateThingTypeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateThingTypeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateThingTypeRequest:
    boto3_raw_data: "type_defs.UpdateThingTypeRequestTypeDef" = dataclasses.field()

    thingTypeName = field("thingTypeName")
    thingTypeProperties = field("thingTypeProperties")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateThingTypeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateThingTypeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAuditFindingResponse:
    boto3_raw_data: "type_defs.DescribeAuditFindingResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def finding(self):  # pragma: no cover
        return AuditFinding.make_one(self.boto3_raw_data["finding"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAuditFindingResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAuditFindingResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAuditFindingsResponse:
    boto3_raw_data: "type_defs.ListAuditFindingsResponseTypeDef" = dataclasses.field()

    @cached_property
    def findings(self):  # pragma: no cover
        return AuditFinding.make_many(self.boto3_raw_data["findings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAuditFindingsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAuditFindingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TopicRule:
    boto3_raw_data: "type_defs.TopicRuleTypeDef" = dataclasses.field()

    ruleName = field("ruleName")
    sql = field("sql")
    description = field("description")
    createdAt = field("createdAt")

    @cached_property
    def actions(self):  # pragma: no cover
        return ActionOutput.make_many(self.boto3_raw_data["actions"])

    ruleDisabled = field("ruleDisabled")
    awsIotSqlVersion = field("awsIotSqlVersion")

    @cached_property
    def errorAction(self):  # pragma: no cover
        return ActionOutput.make_one(self.boto3_raw_data["errorAction"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TopicRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TopicRuleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodeSigning:
    boto3_raw_data: "type_defs.CodeSigningTypeDef" = dataclasses.field()

    awsSignerJobId = field("awsSignerJobId")

    @cached_property
    def startSigningJobParameter(self):  # pragma: no cover
        return StartSigningJobParameter.make_one(
            self.boto3_raw_data["startSigningJobParameter"]
        )

    customCodeSigning = field("customCodeSigning")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CodeSigningTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CodeSigningTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCommandRequest:
    boto3_raw_data: "type_defs.CreateCommandRequestTypeDef" = dataclasses.field()

    commandId = field("commandId")
    namespace = field("namespace")
    displayName = field("displayName")
    description = field("description")
    payload = field("payload")
    mandatoryParameters = field("mandatoryParameters")
    roleArn = field("roleArn")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCommandRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCommandRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OTAUpdateInfo:
    boto3_raw_data: "type_defs.OTAUpdateInfoTypeDef" = dataclasses.field()

    otaUpdateId = field("otaUpdateId")
    otaUpdateArn = field("otaUpdateArn")
    creationDate = field("creationDate")
    lastModifiedDate = field("lastModifiedDate")
    description = field("description")
    targets = field("targets")
    protocols = field("protocols")

    @cached_property
    def awsJobExecutionsRolloutConfig(self):  # pragma: no cover
        return AwsJobExecutionsRolloutConfig.make_one(
            self.boto3_raw_data["awsJobExecutionsRolloutConfig"]
        )

    @cached_property
    def awsJobPresignedUrlConfig(self):  # pragma: no cover
        return AwsJobPresignedUrlConfig.make_one(
            self.boto3_raw_data["awsJobPresignedUrlConfig"]
        )

    targetSelection = field("targetSelection")

    @cached_property
    def otaUpdateFiles(self):  # pragma: no cover
        return OTAUpdateFileOutput.make_many(self.boto3_raw_data["otaUpdateFiles"])

    otaUpdateStatus = field("otaUpdateStatus")
    awsIotJobId = field("awsIotJobId")
    awsIotJobArn = field("awsIotJobArn")

    @cached_property
    def errorInfo(self):  # pragma: no cover
        return ErrorInfo.make_one(self.boto3_raw_data["errorInfo"])

    additionalParameters = field("additionalParameters")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OTAUpdateInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OTAUpdateInfoTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTopicRuleResponse:
    boto3_raw_data: "type_defs.GetTopicRuleResponseTypeDef" = dataclasses.field()

    ruleArn = field("ruleArn")

    @cached_property
    def rule(self):  # pragma: no cover
        return TopicRule.make_one(self.boto3_raw_data["rule"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTopicRuleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTopicRuleResponseTypeDef"]
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

    @cached_property
    def dynamoDB(self):  # pragma: no cover
        return DynamoDBAction.make_one(self.boto3_raw_data["dynamoDB"])

    @cached_property
    def dynamoDBv2(self):  # pragma: no cover
        return DynamoDBv2Action.make_one(self.boto3_raw_data["dynamoDBv2"])

    @cached_property
    def lambda_(self):  # pragma: no cover
        return LambdaAction.make_one(self.boto3_raw_data["lambda"])

    @cached_property
    def sns(self):  # pragma: no cover
        return SnsAction.make_one(self.boto3_raw_data["sns"])

    @cached_property
    def sqs(self):  # pragma: no cover
        return SqsAction.make_one(self.boto3_raw_data["sqs"])

    @cached_property
    def kinesis(self):  # pragma: no cover
        return KinesisAction.make_one(self.boto3_raw_data["kinesis"])

    republish = field("republish")

    @cached_property
    def s3(self):  # pragma: no cover
        return S3Action.make_one(self.boto3_raw_data["s3"])

    @cached_property
    def firehose(self):  # pragma: no cover
        return FirehoseAction.make_one(self.boto3_raw_data["firehose"])

    @cached_property
    def cloudwatchMetric(self):  # pragma: no cover
        return CloudwatchMetricAction.make_one(self.boto3_raw_data["cloudwatchMetric"])

    @cached_property
    def cloudwatchAlarm(self):  # pragma: no cover
        return CloudwatchAlarmAction.make_one(self.boto3_raw_data["cloudwatchAlarm"])

    @cached_property
    def cloudwatchLogs(self):  # pragma: no cover
        return CloudwatchLogsAction.make_one(self.boto3_raw_data["cloudwatchLogs"])

    @cached_property
    def elasticsearch(self):  # pragma: no cover
        return ElasticsearchAction.make_one(self.boto3_raw_data["elasticsearch"])

    @cached_property
    def salesforce(self):  # pragma: no cover
        return SalesforceAction.make_one(self.boto3_raw_data["salesforce"])

    @cached_property
    def iotAnalytics(self):  # pragma: no cover
        return IotAnalyticsAction.make_one(self.boto3_raw_data["iotAnalytics"])

    @cached_property
    def iotEvents(self):  # pragma: no cover
        return IotEventsAction.make_one(self.boto3_raw_data["iotEvents"])

    iotSiteWise = field("iotSiteWise")

    @cached_property
    def stepFunctions(self):  # pragma: no cover
        return StepFunctionsAction.make_one(self.boto3_raw_data["stepFunctions"])

    timestream = field("timestream")
    http = field("http")
    kafka = field("kafka")

    @cached_property
    def openSearch(self):  # pragma: no cover
        return OpenSearchAction.make_one(self.boto3_raw_data["openSearch"])

    @cached_property
    def location(self):  # pragma: no cover
        return LocationAction.make_one(self.boto3_raw_data["location"])

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
class GetOTAUpdateResponse:
    boto3_raw_data: "type_defs.GetOTAUpdateResponseTypeDef" = dataclasses.field()

    @cached_property
    def otaUpdateInfo(self):  # pragma: no cover
        return OTAUpdateInfo.make_one(self.boto3_raw_data["otaUpdateInfo"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetOTAUpdateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOTAUpdateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSecurityProfileRequest:
    boto3_raw_data: "type_defs.CreateSecurityProfileRequestTypeDef" = (
        dataclasses.field()
    )

    securityProfileName = field("securityProfileName")
    securityProfileDescription = field("securityProfileDescription")
    behaviors = field("behaviors")
    alertTargets = field("alertTargets")
    additionalMetricsToRetain = field("additionalMetricsToRetain")

    @cached_property
    def additionalMetricsToRetainV2(self):  # pragma: no cover
        return MetricToRetain.make_many(
            self.boto3_raw_data["additionalMetricsToRetainV2"]
        )

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @cached_property
    def metricsExportConfig(self):  # pragma: no cover
        return MetricsExportConfig.make_one(self.boto3_raw_data["metricsExportConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSecurityProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSecurityProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSecurityProfileRequest:
    boto3_raw_data: "type_defs.UpdateSecurityProfileRequestTypeDef" = (
        dataclasses.field()
    )

    securityProfileName = field("securityProfileName")
    securityProfileDescription = field("securityProfileDescription")
    behaviors = field("behaviors")
    alertTargets = field("alertTargets")
    additionalMetricsToRetain = field("additionalMetricsToRetain")

    @cached_property
    def additionalMetricsToRetainV2(self):  # pragma: no cover
        return MetricToRetain.make_many(
            self.boto3_raw_data["additionalMetricsToRetainV2"]
        )

    deleteBehaviors = field("deleteBehaviors")
    deleteAlertTargets = field("deleteAlertTargets")
    deleteAdditionalMetricsToRetain = field("deleteAdditionalMetricsToRetain")
    expectedVersion = field("expectedVersion")

    @cached_property
    def metricsExportConfig(self):  # pragma: no cover
        return MetricsExportConfig.make_one(self.boto3_raw_data["metricsExportConfig"])

    deleteMetricsExportConfig = field("deleteMetricsExportConfig")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSecurityProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSecurityProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValidateSecurityProfileBehaviorsRequest:
    boto3_raw_data: "type_defs.ValidateSecurityProfileBehaviorsRequestTypeDef" = (
        dataclasses.field()
    )

    behaviors = field("behaviors")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ValidateSecurityProfileBehaviorsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValidateSecurityProfileBehaviorsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OTAUpdateFile:
    boto3_raw_data: "type_defs.OTAUpdateFileTypeDef" = dataclasses.field()

    fileName = field("fileName")
    fileType = field("fileType")
    fileVersion = field("fileVersion")

    @cached_property
    def fileLocation(self):  # pragma: no cover
        return FileLocation.make_one(self.boto3_raw_data["fileLocation"])

    codeSigning = field("codeSigning")
    attributes = field("attributes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OTAUpdateFileTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OTAUpdateFileTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TopicRulePayload:
    boto3_raw_data: "type_defs.TopicRulePayloadTypeDef" = dataclasses.field()

    sql = field("sql")
    actions = field("actions")
    description = field("description")
    ruleDisabled = field("ruleDisabled")
    awsIotSqlVersion = field("awsIotSqlVersion")
    errorAction = field("errorAction")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TopicRulePayloadTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TopicRulePayloadTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTopicRuleRequest:
    boto3_raw_data: "type_defs.CreateTopicRuleRequestTypeDef" = dataclasses.field()

    ruleName = field("ruleName")

    @cached_property
    def topicRulePayload(self):  # pragma: no cover
        return TopicRulePayload.make_one(self.boto3_raw_data["topicRulePayload"])

    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTopicRuleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTopicRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplaceTopicRuleRequest:
    boto3_raw_data: "type_defs.ReplaceTopicRuleRequestTypeDef" = dataclasses.field()

    ruleName = field("ruleName")

    @cached_property
    def topicRulePayload(self):  # pragma: no cover
        return TopicRulePayload.make_one(self.boto3_raw_data["topicRulePayload"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReplaceTopicRuleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplaceTopicRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateOTAUpdateRequest:
    boto3_raw_data: "type_defs.CreateOTAUpdateRequestTypeDef" = dataclasses.field()

    otaUpdateId = field("otaUpdateId")
    targets = field("targets")
    files = field("files")
    roleArn = field("roleArn")
    description = field("description")
    protocols = field("protocols")
    targetSelection = field("targetSelection")

    @cached_property
    def awsJobExecutionsRolloutConfig(self):  # pragma: no cover
        return AwsJobExecutionsRolloutConfig.make_one(
            self.boto3_raw_data["awsJobExecutionsRolloutConfig"]
        )

    @cached_property
    def awsJobPresignedUrlConfig(self):  # pragma: no cover
        return AwsJobPresignedUrlConfig.make_one(
            self.boto3_raw_data["awsJobPresignedUrlConfig"]
        )

    @cached_property
    def awsJobAbortConfig(self):  # pragma: no cover
        return AwsJobAbortConfig.make_one(self.boto3_raw_data["awsJobAbortConfig"])

    @cached_property
    def awsJobTimeoutConfig(self):  # pragma: no cover
        return AwsJobTimeoutConfig.make_one(self.boto3_raw_data["awsJobTimeoutConfig"])

    additionalParameters = field("additionalParameters")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateOTAUpdateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateOTAUpdateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]

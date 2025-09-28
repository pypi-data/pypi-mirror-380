# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_mturk import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AcceptQualificationRequestRequest:
    boto3_raw_data: "type_defs.AcceptQualificationRequestRequestTypeDef" = (
        dataclasses.field()
    )

    QualificationRequestId = field("QualificationRequestId")
    IntegerValue = field("IntegerValue")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AcceptQualificationRequestRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AcceptQualificationRequestRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApproveAssignmentRequest:
    boto3_raw_data: "type_defs.ApproveAssignmentRequestTypeDef" = dataclasses.field()

    AssignmentId = field("AssignmentId")
    RequesterFeedback = field("RequesterFeedback")
    OverrideRejection = field("OverrideRejection")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApproveAssignmentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApproveAssignmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Assignment:
    boto3_raw_data: "type_defs.AssignmentTypeDef" = dataclasses.field()

    AssignmentId = field("AssignmentId")
    WorkerId = field("WorkerId")
    HITId = field("HITId")
    AssignmentStatus = field("AssignmentStatus")
    AutoApprovalTime = field("AutoApprovalTime")
    AcceptTime = field("AcceptTime")
    SubmitTime = field("SubmitTime")
    ApprovalTime = field("ApprovalTime")
    RejectionTime = field("RejectionTime")
    Deadline = field("Deadline")
    Answer = field("Answer")
    RequesterFeedback = field("RequesterFeedback")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssignmentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AssignmentTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateQualificationWithWorkerRequest:
    boto3_raw_data: "type_defs.AssociateQualificationWithWorkerRequestTypeDef" = (
        dataclasses.field()
    )

    QualificationTypeId = field("QualificationTypeId")
    WorkerId = field("WorkerId")
    IntegerValue = field("IntegerValue")
    SendNotification = field("SendNotification")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateQualificationWithWorkerRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateQualificationWithWorkerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BonusPayment:
    boto3_raw_data: "type_defs.BonusPaymentTypeDef" = dataclasses.field()

    WorkerId = field("WorkerId")
    BonusAmount = field("BonusAmount")
    AssignmentId = field("AssignmentId")
    Reason = field("Reason")
    GrantTime = field("GrantTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BonusPaymentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BonusPaymentTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAdditionalAssignmentsForHITRequest:
    boto3_raw_data: "type_defs.CreateAdditionalAssignmentsForHITRequestTypeDef" = (
        dataclasses.field()
    )

    HITId = field("HITId")
    NumberOfAdditionalAssignments = field("NumberOfAdditionalAssignments")
    UniqueRequestToken = field("UniqueRequestToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateAdditionalAssignmentsForHITRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAdditionalAssignmentsForHITRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HITLayoutParameter:
    boto3_raw_data: "type_defs.HITLayoutParameterTypeDef" = dataclasses.field()

    Name = field("Name")
    Value = field("Value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HITLayoutParameterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HITLayoutParameterTypeDef"]
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
class CreateQualificationTypeRequest:
    boto3_raw_data: "type_defs.CreateQualificationTypeRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Description = field("Description")
    QualificationTypeStatus = field("QualificationTypeStatus")
    Keywords = field("Keywords")
    RetryDelayInSeconds = field("RetryDelayInSeconds")
    Test = field("Test")
    AnswerKey = field("AnswerKey")
    TestDurationInSeconds = field("TestDurationInSeconds")
    AutoGranted = field("AutoGranted")
    AutoGrantedValue = field("AutoGrantedValue")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateQualificationTypeRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateQualificationTypeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QualificationType:
    boto3_raw_data: "type_defs.QualificationTypeTypeDef" = dataclasses.field()

    QualificationTypeId = field("QualificationTypeId")
    CreationTime = field("CreationTime")
    Name = field("Name")
    Description = field("Description")
    Keywords = field("Keywords")
    QualificationTypeStatus = field("QualificationTypeStatus")
    Test = field("Test")
    TestDurationInSeconds = field("TestDurationInSeconds")
    AnswerKey = field("AnswerKey")
    RetryDelayInSeconds = field("RetryDelayInSeconds")
    IsRequestable = field("IsRequestable")
    AutoGranted = field("AutoGranted")
    AutoGrantedValue = field("AutoGrantedValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QualificationTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QualificationTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWorkerBlockRequest:
    boto3_raw_data: "type_defs.CreateWorkerBlockRequestTypeDef" = dataclasses.field()

    WorkerId = field("WorkerId")
    Reason = field("Reason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWorkerBlockRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWorkerBlockRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteHITRequest:
    boto3_raw_data: "type_defs.DeleteHITRequestTypeDef" = dataclasses.field()

    HITId = field("HITId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteHITRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteHITRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteQualificationTypeRequest:
    boto3_raw_data: "type_defs.DeleteQualificationTypeRequestTypeDef" = (
        dataclasses.field()
    )

    QualificationTypeId = field("QualificationTypeId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteQualificationTypeRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteQualificationTypeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteWorkerBlockRequest:
    boto3_raw_data: "type_defs.DeleteWorkerBlockRequestTypeDef" = dataclasses.field()

    WorkerId = field("WorkerId")
    Reason = field("Reason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteWorkerBlockRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteWorkerBlockRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateQualificationFromWorkerRequest:
    boto3_raw_data: "type_defs.DisassociateQualificationFromWorkerRequestTypeDef" = (
        dataclasses.field()
    )

    WorkerId = field("WorkerId")
    QualificationTypeId = field("QualificationTypeId")
    Reason = field("Reason")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateQualificationFromWorkerRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateQualificationFromWorkerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAssignmentRequest:
    boto3_raw_data: "type_defs.GetAssignmentRequestTypeDef" = dataclasses.field()

    AssignmentId = field("AssignmentId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAssignmentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAssignmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFileUploadURLRequest:
    boto3_raw_data: "type_defs.GetFileUploadURLRequestTypeDef" = dataclasses.field()

    AssignmentId = field("AssignmentId")
    QuestionIdentifier = field("QuestionIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFileUploadURLRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFileUploadURLRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetHITRequest:
    boto3_raw_data: "type_defs.GetHITRequestTypeDef" = dataclasses.field()

    HITId = field("HITId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetHITRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetHITRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQualificationScoreRequest:
    boto3_raw_data: "type_defs.GetQualificationScoreRequestTypeDef" = (
        dataclasses.field()
    )

    QualificationTypeId = field("QualificationTypeId")
    WorkerId = field("WorkerId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetQualificationScoreRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetQualificationScoreRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQualificationTypeRequest:
    boto3_raw_data: "type_defs.GetQualificationTypeRequestTypeDef" = dataclasses.field()

    QualificationTypeId = field("QualificationTypeId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetQualificationTypeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetQualificationTypeRequestTypeDef"]
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
class ListAssignmentsForHITRequest:
    boto3_raw_data: "type_defs.ListAssignmentsForHITRequestTypeDef" = (
        dataclasses.field()
    )

    HITId = field("HITId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    AssignmentStatuses = field("AssignmentStatuses")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAssignmentsForHITRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssignmentsForHITRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBonusPaymentsRequest:
    boto3_raw_data: "type_defs.ListBonusPaymentsRequestTypeDef" = dataclasses.field()

    HITId = field("HITId")
    AssignmentId = field("AssignmentId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBonusPaymentsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBonusPaymentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListHITsForQualificationTypeRequest:
    boto3_raw_data: "type_defs.ListHITsForQualificationTypeRequestTypeDef" = (
        dataclasses.field()
    )

    QualificationTypeId = field("QualificationTypeId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListHITsForQualificationTypeRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListHITsForQualificationTypeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListHITsRequest:
    boto3_raw_data: "type_defs.ListHITsRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListHITsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListHITsRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQualificationRequestsRequest:
    boto3_raw_data: "type_defs.ListQualificationRequestsRequestTypeDef" = (
        dataclasses.field()
    )

    QualificationTypeId = field("QualificationTypeId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListQualificationRequestsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListQualificationRequestsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QualificationRequest:
    boto3_raw_data: "type_defs.QualificationRequestTypeDef" = dataclasses.field()

    QualificationRequestId = field("QualificationRequestId")
    QualificationTypeId = field("QualificationTypeId")
    WorkerId = field("WorkerId")
    Test = field("Test")
    Answer = field("Answer")
    SubmitTime = field("SubmitTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QualificationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QualificationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQualificationTypesRequest:
    boto3_raw_data: "type_defs.ListQualificationTypesRequestTypeDef" = (
        dataclasses.field()
    )

    MustBeRequestable = field("MustBeRequestable")
    Query = field("Query")
    MustBeOwnedByCaller = field("MustBeOwnedByCaller")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListQualificationTypesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListQualificationTypesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReviewPolicyResultsForHITRequest:
    boto3_raw_data: "type_defs.ListReviewPolicyResultsForHITRequestTypeDef" = (
        dataclasses.field()
    )

    HITId = field("HITId")
    PolicyLevels = field("PolicyLevels")
    RetrieveActions = field("RetrieveActions")
    RetrieveResults = field("RetrieveResults")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListReviewPolicyResultsForHITRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReviewPolicyResultsForHITRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReviewableHITsRequest:
    boto3_raw_data: "type_defs.ListReviewableHITsRequestTypeDef" = dataclasses.field()

    HITTypeId = field("HITTypeId")
    Status = field("Status")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListReviewableHITsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReviewableHITsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkerBlocksRequest:
    boto3_raw_data: "type_defs.ListWorkerBlocksRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWorkerBlocksRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkerBlocksRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkerBlock:
    boto3_raw_data: "type_defs.WorkerBlockTypeDef" = dataclasses.field()

    WorkerId = field("WorkerId")
    Reason = field("Reason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WorkerBlockTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WorkerBlockTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkersWithQualificationTypeRequest:
    boto3_raw_data: "type_defs.ListWorkersWithQualificationTypeRequestTypeDef" = (
        dataclasses.field()
    )

    QualificationTypeId = field("QualificationTypeId")
    Status = field("Status")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListWorkersWithQualificationTypeRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkersWithQualificationTypeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Locale:
    boto3_raw_data: "type_defs.LocaleTypeDef" = dataclasses.field()

    Country = field("Country")
    Subdivision = field("Subdivision")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LocaleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LocaleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotificationSpecification:
    boto3_raw_data: "type_defs.NotificationSpecificationTypeDef" = dataclasses.field()

    Destination = field("Destination")
    Transport = field("Transport")
    Version = field("Version")
    EventTypes = field("EventTypes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NotificationSpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotificationSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotifyWorkersFailureStatus:
    boto3_raw_data: "type_defs.NotifyWorkersFailureStatusTypeDef" = dataclasses.field()

    NotifyWorkersFailureCode = field("NotifyWorkersFailureCode")
    NotifyWorkersFailureMessage = field("NotifyWorkersFailureMessage")
    WorkerId = field("WorkerId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NotifyWorkersFailureStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotifyWorkersFailureStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotifyWorkersRequest:
    boto3_raw_data: "type_defs.NotifyWorkersRequestTypeDef" = dataclasses.field()

    Subject = field("Subject")
    MessageText = field("MessageText")
    WorkerIds = field("WorkerIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NotifyWorkersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotifyWorkersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParameterMapEntryOutput:
    boto3_raw_data: "type_defs.ParameterMapEntryOutputTypeDef" = dataclasses.field()

    Key = field("Key")
    Values = field("Values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ParameterMapEntryOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParameterMapEntryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParameterMapEntry:
    boto3_raw_data: "type_defs.ParameterMapEntryTypeDef" = dataclasses.field()

    Key = field("Key")
    Values = field("Values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ParameterMapEntryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParameterMapEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RejectAssignmentRequest:
    boto3_raw_data: "type_defs.RejectAssignmentRequestTypeDef" = dataclasses.field()

    AssignmentId = field("AssignmentId")
    RequesterFeedback = field("RequesterFeedback")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RejectAssignmentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RejectAssignmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RejectQualificationRequestRequest:
    boto3_raw_data: "type_defs.RejectQualificationRequestRequestTypeDef" = (
        dataclasses.field()
    )

    QualificationRequestId = field("QualificationRequestId")
    Reason = field("Reason")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RejectQualificationRequestRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RejectQualificationRequestRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReviewActionDetail:
    boto3_raw_data: "type_defs.ReviewActionDetailTypeDef" = dataclasses.field()

    ActionId = field("ActionId")
    ActionName = field("ActionName")
    TargetId = field("TargetId")
    TargetType = field("TargetType")
    Status = field("Status")
    CompleteTime = field("CompleteTime")
    Result = field("Result")
    ErrorCode = field("ErrorCode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReviewActionDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReviewActionDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReviewResultDetail:
    boto3_raw_data: "type_defs.ReviewResultDetailTypeDef" = dataclasses.field()

    ActionId = field("ActionId")
    SubjectId = field("SubjectId")
    SubjectType = field("SubjectType")
    QuestionId = field("QuestionId")
    Key = field("Key")
    Value = field("Value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReviewResultDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReviewResultDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendBonusRequest:
    boto3_raw_data: "type_defs.SendBonusRequestTypeDef" = dataclasses.field()

    WorkerId = field("WorkerId")
    BonusAmount = field("BonusAmount")
    AssignmentId = field("AssignmentId")
    Reason = field("Reason")
    UniqueRequestToken = field("UniqueRequestToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SendBonusRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendBonusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateHITReviewStatusRequest:
    boto3_raw_data: "type_defs.UpdateHITReviewStatusRequestTypeDef" = (
        dataclasses.field()
    )

    HITId = field("HITId")
    Revert = field("Revert")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateHITReviewStatusRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateHITReviewStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateHITTypeOfHITRequest:
    boto3_raw_data: "type_defs.UpdateHITTypeOfHITRequestTypeDef" = dataclasses.field()

    HITId = field("HITId")
    HITTypeId = field("HITTypeId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateHITTypeOfHITRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateHITTypeOfHITRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateQualificationTypeRequest:
    boto3_raw_data: "type_defs.UpdateQualificationTypeRequestTypeDef" = (
        dataclasses.field()
    )

    QualificationTypeId = field("QualificationTypeId")
    Description = field("Description")
    QualificationTypeStatus = field("QualificationTypeStatus")
    Test = field("Test")
    AnswerKey = field("AnswerKey")
    TestDurationInSeconds = field("TestDurationInSeconds")
    RetryDelayInSeconds = field("RetryDelayInSeconds")
    AutoGranted = field("AutoGranted")
    AutoGrantedValue = field("AutoGrantedValue")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateQualificationTypeRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateQualificationTypeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateHITTypeResponse:
    boto3_raw_data: "type_defs.CreateHITTypeResponseTypeDef" = dataclasses.field()

    HITTypeId = field("HITTypeId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateHITTypeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateHITTypeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccountBalanceResponse:
    boto3_raw_data: "type_defs.GetAccountBalanceResponseTypeDef" = dataclasses.field()

    AvailableBalance = field("AvailableBalance")
    OnHoldBalance = field("OnHoldBalance")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAccountBalanceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccountBalanceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFileUploadURLResponse:
    boto3_raw_data: "type_defs.GetFileUploadURLResponseTypeDef" = dataclasses.field()

    FileUploadURL = field("FileUploadURL")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFileUploadURLResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFileUploadURLResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssignmentsForHITResponse:
    boto3_raw_data: "type_defs.ListAssignmentsForHITResponseTypeDef" = (
        dataclasses.field()
    )

    NumResults = field("NumResults")

    @cached_property
    def Assignments(self):  # pragma: no cover
        return Assignment.make_many(self.boto3_raw_data["Assignments"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAssignmentsForHITResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssignmentsForHITResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBonusPaymentsResponse:
    boto3_raw_data: "type_defs.ListBonusPaymentsResponseTypeDef" = dataclasses.field()

    NumResults = field("NumResults")

    @cached_property
    def BonusPayments(self):  # pragma: no cover
        return BonusPayment.make_many(self.boto3_raw_data["BonusPayments"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBonusPaymentsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBonusPaymentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateQualificationTypeResponse:
    boto3_raw_data: "type_defs.CreateQualificationTypeResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def QualificationType(self):  # pragma: no cover
        return QualificationType.make_one(self.boto3_raw_data["QualificationType"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateQualificationTypeResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateQualificationTypeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQualificationTypeResponse:
    boto3_raw_data: "type_defs.GetQualificationTypeResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def QualificationType(self):  # pragma: no cover
        return QualificationType.make_one(self.boto3_raw_data["QualificationType"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetQualificationTypeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetQualificationTypeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQualificationTypesResponse:
    boto3_raw_data: "type_defs.ListQualificationTypesResponseTypeDef" = (
        dataclasses.field()
    )

    NumResults = field("NumResults")

    @cached_property
    def QualificationTypes(self):  # pragma: no cover
        return QualificationType.make_many(self.boto3_raw_data["QualificationTypes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListQualificationTypesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListQualificationTypesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateQualificationTypeResponse:
    boto3_raw_data: "type_defs.UpdateQualificationTypeResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def QualificationType(self):  # pragma: no cover
        return QualificationType.make_one(self.boto3_raw_data["QualificationType"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateQualificationTypeResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateQualificationTypeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssignmentsForHITRequestPaginate:
    boto3_raw_data: "type_defs.ListAssignmentsForHITRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    HITId = field("HITId")
    AssignmentStatuses = field("AssignmentStatuses")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAssignmentsForHITRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssignmentsForHITRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBonusPaymentsRequestPaginate:
    boto3_raw_data: "type_defs.ListBonusPaymentsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    HITId = field("HITId")
    AssignmentId = field("AssignmentId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListBonusPaymentsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBonusPaymentsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListHITsForQualificationTypeRequestPaginate:
    boto3_raw_data: "type_defs.ListHITsForQualificationTypeRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    QualificationTypeId = field("QualificationTypeId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListHITsForQualificationTypeRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListHITsForQualificationTypeRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListHITsRequestPaginate:
    boto3_raw_data: "type_defs.ListHITsRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListHITsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListHITsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQualificationRequestsRequestPaginate:
    boto3_raw_data: "type_defs.ListQualificationRequestsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    QualificationTypeId = field("QualificationTypeId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListQualificationRequestsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListQualificationRequestsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQualificationTypesRequestPaginate:
    boto3_raw_data: "type_defs.ListQualificationTypesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    MustBeRequestable = field("MustBeRequestable")
    Query = field("Query")
    MustBeOwnedByCaller = field("MustBeOwnedByCaller")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListQualificationTypesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListQualificationTypesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReviewableHITsRequestPaginate:
    boto3_raw_data: "type_defs.ListReviewableHITsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    HITTypeId = field("HITTypeId")
    Status = field("Status")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListReviewableHITsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReviewableHITsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkerBlocksRequestPaginate:
    boto3_raw_data: "type_defs.ListWorkerBlocksRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListWorkerBlocksRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkerBlocksRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkersWithQualificationTypeRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListWorkersWithQualificationTypeRequestPaginateTypeDef"
    ) = dataclasses.field()

    QualificationTypeId = field("QualificationTypeId")
    Status = field("Status")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListWorkersWithQualificationTypeRequestPaginateTypeDef"
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
                "type_defs.ListWorkersWithQualificationTypeRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQualificationRequestsResponse:
    boto3_raw_data: "type_defs.ListQualificationRequestsResponseTypeDef" = (
        dataclasses.field()
    )

    NumResults = field("NumResults")

    @cached_property
    def QualificationRequests(self):  # pragma: no cover
        return QualificationRequest.make_many(
            self.boto3_raw_data["QualificationRequests"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListQualificationRequestsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListQualificationRequestsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkerBlocksResponse:
    boto3_raw_data: "type_defs.ListWorkerBlocksResponseTypeDef" = dataclasses.field()

    NumResults = field("NumResults")

    @cached_property
    def WorkerBlocks(self):  # pragma: no cover
        return WorkerBlock.make_many(self.boto3_raw_data["WorkerBlocks"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWorkerBlocksResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkerBlocksResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QualificationRequirementOutput:
    boto3_raw_data: "type_defs.QualificationRequirementOutputTypeDef" = (
        dataclasses.field()
    )

    QualificationTypeId = field("QualificationTypeId")
    Comparator = field("Comparator")
    IntegerValues = field("IntegerValues")

    @cached_property
    def LocaleValues(self):  # pragma: no cover
        return Locale.make_many(self.boto3_raw_data["LocaleValues"])

    RequiredToPreview = field("RequiredToPreview")
    ActionsGuarded = field("ActionsGuarded")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.QualificationRequirementOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QualificationRequirementOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QualificationRequirement:
    boto3_raw_data: "type_defs.QualificationRequirementTypeDef" = dataclasses.field()

    QualificationTypeId = field("QualificationTypeId")
    Comparator = field("Comparator")
    IntegerValues = field("IntegerValues")

    @cached_property
    def LocaleValues(self):  # pragma: no cover
        return Locale.make_many(self.boto3_raw_data["LocaleValues"])

    RequiredToPreview = field("RequiredToPreview")
    ActionsGuarded = field("ActionsGuarded")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QualificationRequirementTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QualificationRequirementTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Qualification:
    boto3_raw_data: "type_defs.QualificationTypeDef" = dataclasses.field()

    QualificationTypeId = field("QualificationTypeId")
    WorkerId = field("WorkerId")
    GrantTime = field("GrantTime")
    IntegerValue = field("IntegerValue")

    @cached_property
    def LocaleValue(self):  # pragma: no cover
        return Locale.make_one(self.boto3_raw_data["LocaleValue"])

    Status = field("Status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QualificationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.QualificationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendTestEventNotificationRequest:
    boto3_raw_data: "type_defs.SendTestEventNotificationRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Notification(self):  # pragma: no cover
        return NotificationSpecification.make_one(self.boto3_raw_data["Notification"])

    TestEventType = field("TestEventType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SendTestEventNotificationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendTestEventNotificationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateNotificationSettingsRequest:
    boto3_raw_data: "type_defs.UpdateNotificationSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    HITTypeId = field("HITTypeId")

    @cached_property
    def Notification(self):  # pragma: no cover
        return NotificationSpecification.make_one(self.boto3_raw_data["Notification"])

    Active = field("Active")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateNotificationSettingsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateNotificationSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotifyWorkersResponse:
    boto3_raw_data: "type_defs.NotifyWorkersResponseTypeDef" = dataclasses.field()

    @cached_property
    def NotifyWorkersFailureStatuses(self):  # pragma: no cover
        return NotifyWorkersFailureStatus.make_many(
            self.boto3_raw_data["NotifyWorkersFailureStatuses"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NotifyWorkersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotifyWorkersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolicyParameterOutput:
    boto3_raw_data: "type_defs.PolicyParameterOutputTypeDef" = dataclasses.field()

    Key = field("Key")
    Values = field("Values")

    @cached_property
    def MapEntries(self):  # pragma: no cover
        return ParameterMapEntryOutput.make_many(self.boto3_raw_data["MapEntries"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PolicyParameterOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PolicyParameterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolicyParameter:
    boto3_raw_data: "type_defs.PolicyParameterTypeDef" = dataclasses.field()

    Key = field("Key")
    Values = field("Values")

    @cached_property
    def MapEntries(self):  # pragma: no cover
        return ParameterMapEntry.make_many(self.boto3_raw_data["MapEntries"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PolicyParameterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PolicyParameterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReviewReport:
    boto3_raw_data: "type_defs.ReviewReportTypeDef" = dataclasses.field()

    @cached_property
    def ReviewResults(self):  # pragma: no cover
        return ReviewResultDetail.make_many(self.boto3_raw_data["ReviewResults"])

    @cached_property
    def ReviewActions(self):  # pragma: no cover
        return ReviewActionDetail.make_many(self.boto3_raw_data["ReviewActions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReviewReportTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReviewReportTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateExpirationForHITRequest:
    boto3_raw_data: "type_defs.UpdateExpirationForHITRequestTypeDef" = (
        dataclasses.field()
    )

    HITId = field("HITId")
    ExpireAt = field("ExpireAt")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateExpirationForHITRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateExpirationForHITRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HIT:
    boto3_raw_data: "type_defs.HITTypeDef" = dataclasses.field()

    HITId = field("HITId")
    HITTypeId = field("HITTypeId")
    HITGroupId = field("HITGroupId")
    HITLayoutId = field("HITLayoutId")
    CreationTime = field("CreationTime")
    Title = field("Title")
    Description = field("Description")
    Question = field("Question")
    Keywords = field("Keywords")
    HITStatus = field("HITStatus")
    MaxAssignments = field("MaxAssignments")
    Reward = field("Reward")
    AutoApprovalDelayInSeconds = field("AutoApprovalDelayInSeconds")
    Expiration = field("Expiration")
    AssignmentDurationInSeconds = field("AssignmentDurationInSeconds")
    RequesterAnnotation = field("RequesterAnnotation")

    @cached_property
    def QualificationRequirements(self):  # pragma: no cover
        return QualificationRequirementOutput.make_many(
            self.boto3_raw_data["QualificationRequirements"]
        )

    HITReviewStatus = field("HITReviewStatus")
    NumberOfAssignmentsPending = field("NumberOfAssignmentsPending")
    NumberOfAssignmentsAvailable = field("NumberOfAssignmentsAvailable")
    NumberOfAssignmentsCompleted = field("NumberOfAssignmentsCompleted")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HITTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HITTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQualificationScoreResponse:
    boto3_raw_data: "type_defs.GetQualificationScoreResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Qualification(self):  # pragma: no cover
        return Qualification.make_one(self.boto3_raw_data["Qualification"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetQualificationScoreResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetQualificationScoreResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkersWithQualificationTypeResponse:
    boto3_raw_data: "type_defs.ListWorkersWithQualificationTypeResponseTypeDef" = (
        dataclasses.field()
    )

    NumResults = field("NumResults")

    @cached_property
    def Qualifications(self):  # pragma: no cover
        return Qualification.make_many(self.boto3_raw_data["Qualifications"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListWorkersWithQualificationTypeResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkersWithQualificationTypeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReviewPolicyOutput:
    boto3_raw_data: "type_defs.ReviewPolicyOutputTypeDef" = dataclasses.field()

    PolicyName = field("PolicyName")

    @cached_property
    def Parameters(self):  # pragma: no cover
        return PolicyParameterOutput.make_many(self.boto3_raw_data["Parameters"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReviewPolicyOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReviewPolicyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReviewPolicy:
    boto3_raw_data: "type_defs.ReviewPolicyTypeDef" = dataclasses.field()

    PolicyName = field("PolicyName")

    @cached_property
    def Parameters(self):  # pragma: no cover
        return PolicyParameter.make_many(self.boto3_raw_data["Parameters"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReviewPolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReviewPolicyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateHITResponse:
    boto3_raw_data: "type_defs.CreateHITResponseTypeDef" = dataclasses.field()

    @cached_property
    def HIT(self):  # pragma: no cover
        return HIT.make_one(self.boto3_raw_data["HIT"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateHITResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateHITResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateHITWithHITTypeResponse:
    boto3_raw_data: "type_defs.CreateHITWithHITTypeResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def HIT(self):  # pragma: no cover
        return HIT.make_one(self.boto3_raw_data["HIT"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateHITWithHITTypeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateHITWithHITTypeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAssignmentResponse:
    boto3_raw_data: "type_defs.GetAssignmentResponseTypeDef" = dataclasses.field()

    @cached_property
    def Assignment(self):  # pragma: no cover
        return Assignment.make_one(self.boto3_raw_data["Assignment"])

    @cached_property
    def HIT(self):  # pragma: no cover
        return HIT.make_one(self.boto3_raw_data["HIT"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAssignmentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAssignmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetHITResponse:
    boto3_raw_data: "type_defs.GetHITResponseTypeDef" = dataclasses.field()

    @cached_property
    def HIT(self):  # pragma: no cover
        return HIT.make_one(self.boto3_raw_data["HIT"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetHITResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetHITResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListHITsForQualificationTypeResponse:
    boto3_raw_data: "type_defs.ListHITsForQualificationTypeResponseTypeDef" = (
        dataclasses.field()
    )

    NumResults = field("NumResults")

    @cached_property
    def HITs(self):  # pragma: no cover
        return HIT.make_many(self.boto3_raw_data["HITs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListHITsForQualificationTypeResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListHITsForQualificationTypeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListHITsResponse:
    boto3_raw_data: "type_defs.ListHITsResponseTypeDef" = dataclasses.field()

    NumResults = field("NumResults")

    @cached_property
    def HITs(self):  # pragma: no cover
        return HIT.make_many(self.boto3_raw_data["HITs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListHITsResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListHITsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReviewableHITsResponse:
    boto3_raw_data: "type_defs.ListReviewableHITsResponseTypeDef" = dataclasses.field()

    NumResults = field("NumResults")

    @cached_property
    def HITs(self):  # pragma: no cover
        return HIT.make_many(self.boto3_raw_data["HITs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListReviewableHITsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReviewableHITsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateHITTypeRequest:
    boto3_raw_data: "type_defs.CreateHITTypeRequestTypeDef" = dataclasses.field()

    AssignmentDurationInSeconds = field("AssignmentDurationInSeconds")
    Reward = field("Reward")
    Title = field("Title")
    Description = field("Description")
    AutoApprovalDelayInSeconds = field("AutoApprovalDelayInSeconds")
    Keywords = field("Keywords")
    QualificationRequirements = field("QualificationRequirements")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateHITTypeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateHITTypeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReviewPolicyResultsForHITResponse:
    boto3_raw_data: "type_defs.ListReviewPolicyResultsForHITResponseTypeDef" = (
        dataclasses.field()
    )

    HITId = field("HITId")

    @cached_property
    def AssignmentReviewPolicy(self):  # pragma: no cover
        return ReviewPolicyOutput.make_one(
            self.boto3_raw_data["AssignmentReviewPolicy"]
        )

    @cached_property
    def HITReviewPolicy(self):  # pragma: no cover
        return ReviewPolicyOutput.make_one(self.boto3_raw_data["HITReviewPolicy"])

    @cached_property
    def AssignmentReviewReport(self):  # pragma: no cover
        return ReviewReport.make_one(self.boto3_raw_data["AssignmentReviewReport"])

    @cached_property
    def HITReviewReport(self):  # pragma: no cover
        return ReviewReport.make_one(self.boto3_raw_data["HITReviewReport"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListReviewPolicyResultsForHITResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReviewPolicyResultsForHITResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateHITRequest:
    boto3_raw_data: "type_defs.CreateHITRequestTypeDef" = dataclasses.field()

    LifetimeInSeconds = field("LifetimeInSeconds")
    AssignmentDurationInSeconds = field("AssignmentDurationInSeconds")
    Reward = field("Reward")
    Title = field("Title")
    Description = field("Description")
    MaxAssignments = field("MaxAssignments")
    AutoApprovalDelayInSeconds = field("AutoApprovalDelayInSeconds")
    Keywords = field("Keywords")
    Question = field("Question")
    RequesterAnnotation = field("RequesterAnnotation")
    QualificationRequirements = field("QualificationRequirements")
    UniqueRequestToken = field("UniqueRequestToken")
    AssignmentReviewPolicy = field("AssignmentReviewPolicy")
    HITReviewPolicy = field("HITReviewPolicy")
    HITLayoutId = field("HITLayoutId")

    @cached_property
    def HITLayoutParameters(self):  # pragma: no cover
        return HITLayoutParameter.make_many(self.boto3_raw_data["HITLayoutParameters"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateHITRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateHITRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateHITWithHITTypeRequest:
    boto3_raw_data: "type_defs.CreateHITWithHITTypeRequestTypeDef" = dataclasses.field()

    HITTypeId = field("HITTypeId")
    LifetimeInSeconds = field("LifetimeInSeconds")
    MaxAssignments = field("MaxAssignments")
    Question = field("Question")
    RequesterAnnotation = field("RequesterAnnotation")
    UniqueRequestToken = field("UniqueRequestToken")
    AssignmentReviewPolicy = field("AssignmentReviewPolicy")
    HITReviewPolicy = field("HITReviewPolicy")
    HITLayoutId = field("HITLayoutId")

    @cached_property
    def HITLayoutParameters(self):  # pragma: no cover
        return HITLayoutParameter.make_many(self.boto3_raw_data["HITLayoutParameters"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateHITWithHITTypeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateHITWithHITTypeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]

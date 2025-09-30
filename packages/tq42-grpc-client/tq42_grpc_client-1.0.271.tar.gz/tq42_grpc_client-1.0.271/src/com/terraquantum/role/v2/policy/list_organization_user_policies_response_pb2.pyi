from com.terraquantum.role.v1.policy import policy_pb2 as _policy_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListOrganizationUserPoliciesResponse(_message.Message):
    __slots__ = ("policies",)
    POLICIES_FIELD_NUMBER: _ClassVar[int]
    policies: _containers.RepeatedCompositeFieldContainer[_policy_pb2.PolicyProto]
    def __init__(self, policies: _Optional[_Iterable[_Union[_policy_pb2.PolicyProto, _Mapping]]] = ...) -> None: ...

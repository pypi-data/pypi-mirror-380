from buf.validate import validate_pb2 as _validate_pb2
from com.terraquantum.experiment.v1.experimentrun.algorithm.ml_layers import quantum_layer_pb2 as _quantum_layer_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CPHNLayer(_message.Message):
    __slots__ = ("quantum_layer", "hidden_dim")
    QUANTUM_LAYER_FIELD_NUMBER: _ClassVar[int]
    HIDDEN_DIM_FIELD_NUMBER: _ClassVar[int]
    quantum_layer: _quantum_layer_pb2.QuantumLayer
    hidden_dim: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, quantum_layer: _Optional[_Union[_quantum_layer_pb2.QuantumLayer, _Mapping]] = ..., hidden_dim: _Optional[_Iterable[int]] = ...) -> None: ...

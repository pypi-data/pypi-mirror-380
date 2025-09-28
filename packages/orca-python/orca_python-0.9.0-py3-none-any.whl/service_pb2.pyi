from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from vendor import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ResultType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NOT_SPECIFIED: _ClassVar[ResultType]
    STRUCT: _ClassVar[ResultType]
    VALUE: _ClassVar[ResultType]
    ARRAY: _ClassVar[ResultType]
    NONE: _ClassVar[ResultType]

class ResultStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RESULT_STATUS_HANDLED_FAILED: _ClassVar[ResultStatus]
    RESULT_STATUS_UNHANDLED_FAILED: _ClassVar[ResultStatus]
    RESULT_STATUS_SUCEEDED: _ClassVar[ResultStatus]
NOT_SPECIFIED: ResultType
STRUCT: ResultType
VALUE: ResultType
ARRAY: ResultType
NONE: ResultType
RESULT_STATUS_HANDLED_FAILED: ResultStatus
RESULT_STATUS_UNHANDLED_FAILED: ResultStatus
RESULT_STATUS_SUCEEDED: ResultStatus

class Window(_message.Message):
    __slots__ = ("time_from", "time_to", "window_type_name", "window_type_version", "origin", "metadata")
    TIME_FROM_FIELD_NUMBER: _ClassVar[int]
    TIME_TO_FIELD_NUMBER: _ClassVar[int]
    WINDOW_TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
    WINDOW_TYPE_VERSION_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    time_from: _timestamp_pb2.Timestamp
    time_to: _timestamp_pb2.Timestamp
    window_type_name: str
    window_type_version: str
    origin: str
    metadata: _struct_pb2.Struct
    def __init__(self, time_from: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., time_to: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., window_type_name: _Optional[str] = ..., window_type_version: _Optional[str] = ..., origin: _Optional[str] = ..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class MetadataField(_message.Message):
    __slots__ = ("name", "description")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class WindowType(_message.Message):
    __slots__ = ("name", "version", "description", "metadataFields")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    METADATAFIELDS_FIELD_NUMBER: _ClassVar[int]
    name: str
    version: str
    description: str
    metadataFields: _containers.RepeatedCompositeFieldContainer[MetadataField]
    def __init__(self, name: _Optional[str] = ..., version: _Optional[str] = ..., description: _Optional[str] = ..., metadataFields: _Optional[_Iterable[_Union[MetadataField, _Mapping]]] = ...) -> None: ...

class WindowEmitStatus(_message.Message):
    __slots__ = ("status",)
    class StatusEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_TRIGGERED_ALGORITHMS: _ClassVar[WindowEmitStatus.StatusEnum]
        PROCESSING_TRIGGERED: _ClassVar[WindowEmitStatus.StatusEnum]
        TRIGGERING_FAILED: _ClassVar[WindowEmitStatus.StatusEnum]
    NO_TRIGGERED_ALGORITHMS: WindowEmitStatus.StatusEnum
    PROCESSING_TRIGGERED: WindowEmitStatus.StatusEnum
    TRIGGERING_FAILED: WindowEmitStatus.StatusEnum
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: WindowEmitStatus.StatusEnum
    def __init__(self, status: _Optional[_Union[WindowEmitStatus.StatusEnum, str]] = ...) -> None: ...

class AlgorithmDependency(_message.Message):
    __slots__ = ("name", "version", "processor_name", "processor_runtime")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    PROCESSOR_NAME_FIELD_NUMBER: _ClassVar[int]
    PROCESSOR_RUNTIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    version: str
    processor_name: str
    processor_runtime: str
    def __init__(self, name: _Optional[str] = ..., version: _Optional[str] = ..., processor_name: _Optional[str] = ..., processor_runtime: _Optional[str] = ...) -> None: ...

class Algorithm(_message.Message):
    __slots__ = ("name", "version", "window_type", "dependencies", "result_type")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    WINDOW_TYPE_FIELD_NUMBER: _ClassVar[int]
    DEPENDENCIES_FIELD_NUMBER: _ClassVar[int]
    RESULT_TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    version: str
    window_type: WindowType
    dependencies: _containers.RepeatedCompositeFieldContainer[AlgorithmDependency]
    result_type: ResultType
    def __init__(self, name: _Optional[str] = ..., version: _Optional[str] = ..., window_type: _Optional[_Union[WindowType, _Mapping]] = ..., dependencies: _Optional[_Iterable[_Union[AlgorithmDependency, _Mapping]]] = ..., result_type: _Optional[_Union[ResultType, str]] = ...) -> None: ...

class FloatArray(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, values: _Optional[_Iterable[float]] = ...) -> None: ...

class Result(_message.Message):
    __slots__ = ("status", "single_value", "float_values", "struct_value", "timestamp")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SINGLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    FLOAT_VALUES_FIELD_NUMBER: _ClassVar[int]
    STRUCT_VALUE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    status: ResultStatus
    single_value: float
    float_values: FloatArray
    struct_value: _struct_pb2.Struct
    timestamp: int
    def __init__(self, status: _Optional[_Union[ResultStatus, str]] = ..., single_value: _Optional[float] = ..., float_values: _Optional[_Union[FloatArray, _Mapping]] = ..., struct_value: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., timestamp: _Optional[int] = ...) -> None: ...

class ProcessorRegistration(_message.Message):
    __slots__ = ("name", "runtime", "connection_str", "supported_algorithms")
    NAME_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_STR_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_ALGORITHMS_FIELD_NUMBER: _ClassVar[int]
    name: str
    runtime: str
    connection_str: str
    supported_algorithms: _containers.RepeatedCompositeFieldContainer[Algorithm]
    def __init__(self, name: _Optional[str] = ..., runtime: _Optional[str] = ..., connection_str: _Optional[str] = ..., supported_algorithms: _Optional[_Iterable[_Union[Algorithm, _Mapping]]] = ...) -> None: ...

class ProcessingTask(_message.Message):
    __slots__ = ("task_id", "algorithm", "window", "dependency_results")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    WINDOW_FIELD_NUMBER: _ClassVar[int]
    DEPENDENCY_RESULTS_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    algorithm: Algorithm
    window: Window
    dependency_results: _containers.RepeatedCompositeFieldContainer[Result]
    def __init__(self, task_id: _Optional[str] = ..., algorithm: _Optional[_Union[Algorithm, _Mapping]] = ..., window: _Optional[_Union[Window, _Mapping]] = ..., dependency_results: _Optional[_Iterable[_Union[Result, _Mapping]]] = ...) -> None: ...

class ExecutionRequest(_message.Message):
    __slots__ = ("exec_id", "window", "algorithm_results", "algorithms")
    EXEC_ID_FIELD_NUMBER: _ClassVar[int]
    WINDOW_FIELD_NUMBER: _ClassVar[int]
    ALGORITHM_RESULTS_FIELD_NUMBER: _ClassVar[int]
    ALGORITHMS_FIELD_NUMBER: _ClassVar[int]
    exec_id: str
    window: Window
    algorithm_results: _containers.RepeatedCompositeFieldContainer[AlgorithmResult]
    algorithms: _containers.RepeatedCompositeFieldContainer[Algorithm]
    def __init__(self, exec_id: _Optional[str] = ..., window: _Optional[_Union[Window, _Mapping]] = ..., algorithm_results: _Optional[_Iterable[_Union[AlgorithmResult, _Mapping]]] = ..., algorithms: _Optional[_Iterable[_Union[Algorithm, _Mapping]]] = ...) -> None: ...

class ExecutionResult(_message.Message):
    __slots__ = ("exec_id", "algorithm_result")
    EXEC_ID_FIELD_NUMBER: _ClassVar[int]
    ALGORITHM_RESULT_FIELD_NUMBER: _ClassVar[int]
    exec_id: str
    algorithm_result: AlgorithmResult
    def __init__(self, exec_id: _Optional[str] = ..., algorithm_result: _Optional[_Union[AlgorithmResult, _Mapping]] = ...) -> None: ...

class AlgorithmResult(_message.Message):
    __slots__ = ("algorithm", "result")
    ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    algorithm: Algorithm
    result: Result
    def __init__(self, algorithm: _Optional[_Union[Algorithm, _Mapping]] = ..., result: _Optional[_Union[Result, _Mapping]] = ...) -> None: ...

class Status(_message.Message):
    __slots__ = ("received", "message")
    RECEIVED_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    received: bool
    message: str
    def __init__(self, received: bool = ..., message: _Optional[str] = ...) -> None: ...

class HealthCheckRequest(_message.Message):
    __slots__ = ("timestamp",)
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    timestamp: int
    def __init__(self, timestamp: _Optional[int] = ...) -> None: ...

class HealthCheckResponse(_message.Message):
    __slots__ = ("status", "message", "metrics")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNKNOWN: _ClassVar[HealthCheckResponse.Status]
        STATUS_SERVING: _ClassVar[HealthCheckResponse.Status]
        STATUS_TRANSITIONING: _ClassVar[HealthCheckResponse.Status]
        STATUS_NOT_SERVING: _ClassVar[HealthCheckResponse.Status]
    STATUS_UNKNOWN: HealthCheckResponse.Status
    STATUS_SERVING: HealthCheckResponse.Status
    STATUS_TRANSITIONING: HealthCheckResponse.Status
    STATUS_NOT_SERVING: HealthCheckResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    status: HealthCheckResponse.Status
    message: str
    metrics: ProcessorMetrics
    def __init__(self, status: _Optional[_Union[HealthCheckResponse.Status, str]] = ..., message: _Optional[str] = ..., metrics: _Optional[_Union[ProcessorMetrics, _Mapping]] = ...) -> None: ...

class ProcessorMetrics(_message.Message):
    __slots__ = ("active_tasks", "memory_bytes", "cpu_percent", "uptime_seconds")
    ACTIVE_TASKS_FIELD_NUMBER: _ClassVar[int]
    MEMORY_BYTES_FIELD_NUMBER: _ClassVar[int]
    CPU_PERCENT_FIELD_NUMBER: _ClassVar[int]
    UPTIME_SECONDS_FIELD_NUMBER: _ClassVar[int]
    active_tasks: int
    memory_bytes: int
    cpu_percent: float
    uptime_seconds: int
    def __init__(self, active_tasks: _Optional[int] = ..., memory_bytes: _Optional[int] = ..., cpu_percent: _Optional[float] = ..., uptime_seconds: _Optional[int] = ...) -> None: ...

class WindowTypeRead(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class WindowTypes(_message.Message):
    __slots__ = ("windows",)
    WINDOWS_FIELD_NUMBER: _ClassVar[int]
    windows: _containers.RepeatedCompositeFieldContainer[WindowType]
    def __init__(self, windows: _Optional[_Iterable[_Union[WindowType, _Mapping]]] = ...) -> None: ...

class AlgorithmsRead(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Algorithms(_message.Message):
    __slots__ = ("algorithm",)
    ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    algorithm: _containers.RepeatedCompositeFieldContainer[Algorithm]
    def __init__(self, algorithm: _Optional[_Iterable[_Union[Algorithm, _Mapping]]] = ...) -> None: ...

class ProcessorsRead(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Processors(_message.Message):
    __slots__ = ("processor",)
    class Processor(_message.Message):
        __slots__ = ("name", "runtime")
        NAME_FIELD_NUMBER: _ClassVar[int]
        RUNTIME_FIELD_NUMBER: _ClassVar[int]
        name: str
        runtime: str
        def __init__(self, name: _Optional[str] = ..., runtime: _Optional[str] = ...) -> None: ...
    PROCESSOR_FIELD_NUMBER: _ClassVar[int]
    processor: _containers.RepeatedCompositeFieldContainer[Processors.Processor]
    def __init__(self, processor: _Optional[_Iterable[_Union[Processors.Processor, _Mapping]]] = ...) -> None: ...

class ResultsStatsRead(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ResultsStats(_message.Message):
    __slots__ = ("Count",)
    COUNT_FIELD_NUMBER: _ClassVar[int]
    Count: int
    def __init__(self, Count: _Optional[int] = ...) -> None: ...

class AlgorithmFieldsRead(_message.Message):
    __slots__ = ("time_from", "time_to", "algorithm")
    TIME_FROM_FIELD_NUMBER: _ClassVar[int]
    TIME_TO_FIELD_NUMBER: _ClassVar[int]
    ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    time_from: _timestamp_pb2.Timestamp
    time_to: _timestamp_pb2.Timestamp
    algorithm: Algorithm
    def __init__(self, time_from: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., time_to: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., algorithm: _Optional[_Union[Algorithm, _Mapping]] = ...) -> None: ...

class AlgorithmFields(_message.Message):
    __slots__ = ("field",)
    FIELD_FIELD_NUMBER: _ClassVar[int]
    field: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, field: _Optional[_Iterable[str]] = ...) -> None: ...

class ResultsForAlgorithmRead(_message.Message):
    __slots__ = ("time_from", "time_to", "algorithm")
    TIME_FROM_FIELD_NUMBER: _ClassVar[int]
    TIME_TO_FIELD_NUMBER: _ClassVar[int]
    ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    time_from: _timestamp_pb2.Timestamp
    time_to: _timestamp_pb2.Timestamp
    algorithm: Algorithm
    def __init__(self, time_from: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., time_to: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., algorithm: _Optional[_Union[Algorithm, _Mapping]] = ...) -> None: ...

class ResultsForAlgorithm(_message.Message):
    __slots__ = ("results",)
    class ResultsRow(_message.Message):
        __slots__ = ("time", "single_value", "array_values", "struct_value")
        TIME_FIELD_NUMBER: _ClassVar[int]
        SINGLE_VALUE_FIELD_NUMBER: _ClassVar[int]
        ARRAY_VALUES_FIELD_NUMBER: _ClassVar[int]
        STRUCT_VALUE_FIELD_NUMBER: _ClassVar[int]
        time: _timestamp_pb2.Timestamp
        single_value: float
        array_values: FloatArray
        struct_value: _struct_pb2.Struct
        def __init__(self, time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., single_value: _Optional[float] = ..., array_values: _Optional[_Union[FloatArray, _Mapping]] = ..., struct_value: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ResultsForAlgorithm.ResultsRow]
    def __init__(self, results: _Optional[_Iterable[_Union[ResultsForAlgorithm.ResultsRow, _Mapping]]] = ...) -> None: ...

class WindowsRead(_message.Message):
    __slots__ = ("time_from", "time_to", "window")
    TIME_FROM_FIELD_NUMBER: _ClassVar[int]
    TIME_TO_FIELD_NUMBER: _ClassVar[int]
    WINDOW_FIELD_NUMBER: _ClassVar[int]
    time_from: _timestamp_pb2.Timestamp
    time_to: _timestamp_pb2.Timestamp
    window: WindowType
    def __init__(self, time_from: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., time_to: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., window: _Optional[_Union[WindowType, _Mapping]] = ...) -> None: ...

class Windows(_message.Message):
    __slots__ = ("window",)
    WINDOW_FIELD_NUMBER: _ClassVar[int]
    window: _containers.RepeatedCompositeFieldContainer[Window]
    def __init__(self, window: _Optional[_Iterable[_Union[Window, _Mapping]]] = ...) -> None: ...

class DistinctMetadataForWindowTypeRead(_message.Message):
    __slots__ = ("time_from", "time_to", "window_type")
    TIME_FROM_FIELD_NUMBER: _ClassVar[int]
    TIME_TO_FIELD_NUMBER: _ClassVar[int]
    WINDOW_TYPE_FIELD_NUMBER: _ClassVar[int]
    time_from: _timestamp_pb2.Timestamp
    time_to: _timestamp_pb2.Timestamp
    window_type: WindowType
    def __init__(self, time_from: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., time_to: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., window_type: _Optional[_Union[WindowType, _Mapping]] = ...) -> None: ...

class DistinctMetadataForWindowType(_message.Message):
    __slots__ = ("metadata",)
    METADATA_FIELD_NUMBER: _ClassVar[int]
    metadata: _struct_pb2.ListValue
    def __init__(self, metadata: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ...) -> None: ...

class WindowsForMetadataRead(_message.Message):
    __slots__ = ("time_from", "time_to", "window", "metadata")
    class Metadata(_message.Message):
        __slots__ = ("field", "value")
        FIELD_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        field: str
        value: _struct_pb2.Value
        def __init__(self, field: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
    TIME_FROM_FIELD_NUMBER: _ClassVar[int]
    TIME_TO_FIELD_NUMBER: _ClassVar[int]
    WINDOW_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    time_from: _timestamp_pb2.Timestamp
    time_to: _timestamp_pb2.Timestamp
    window: WindowType
    metadata: _containers.RepeatedCompositeFieldContainer[WindowsForMetadataRead.Metadata]
    def __init__(self, time_from: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., time_to: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., window: _Optional[_Union[WindowType, _Mapping]] = ..., metadata: _Optional[_Iterable[_Union[WindowsForMetadataRead.Metadata, _Mapping]]] = ...) -> None: ...

class WindowsForMetadata(_message.Message):
    __slots__ = ("window",)
    WINDOW_FIELD_NUMBER: _ClassVar[int]
    window: _containers.RepeatedCompositeFieldContainer[Window]
    def __init__(self, window: _Optional[_Iterable[_Union[Window, _Mapping]]] = ...) -> None: ...

class ResultsForAlgorithmAndMetadataRead(_message.Message):
    __slots__ = ("time_from", "time_to", "algorithm", "metadata")
    class Metadata(_message.Message):
        __slots__ = ("field", "value")
        FIELD_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        field: str
        value: _struct_pb2.Value
        def __init__(self, field: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
    TIME_FROM_FIELD_NUMBER: _ClassVar[int]
    TIME_TO_FIELD_NUMBER: _ClassVar[int]
    ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    time_from: _timestamp_pb2.Timestamp
    time_to: _timestamp_pb2.Timestamp
    algorithm: Algorithm
    metadata: _containers.RepeatedCompositeFieldContainer[ResultsForAlgorithmAndMetadataRead.Metadata]
    def __init__(self, time_from: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., time_to: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., algorithm: _Optional[_Union[Algorithm, _Mapping]] = ..., metadata: _Optional[_Iterable[_Union[ResultsForAlgorithmAndMetadataRead.Metadata, _Mapping]]] = ...) -> None: ...

class ResultsForAlgorithmAndMetadata(_message.Message):
    __slots__ = ("results",)
    class ResultsRow(_message.Message):
        __slots__ = ("time", "single_value", "array_values", "struct_value")
        TIME_FIELD_NUMBER: _ClassVar[int]
        SINGLE_VALUE_FIELD_NUMBER: _ClassVar[int]
        ARRAY_VALUES_FIELD_NUMBER: _ClassVar[int]
        STRUCT_VALUE_FIELD_NUMBER: _ClassVar[int]
        time: _timestamp_pb2.Timestamp
        single_value: float
        array_values: FloatArray
        struct_value: _struct_pb2.Struct
        def __init__(self, time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., single_value: _Optional[float] = ..., array_values: _Optional[_Union[FloatArray, _Mapping]] = ..., struct_value: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ResultsForAlgorithmAndMetadata.ResultsRow]
    def __init__(self, results: _Optional[_Iterable[_Union[ResultsForAlgorithmAndMetadata.ResultsRow, _Mapping]]] = ...) -> None: ...

class AnnotateWrite(_message.Message):
    __slots__ = ("time_from", "time_to", "captured_algorithms", "captured_windows", "description", "metadata")
    TIME_FROM_FIELD_NUMBER: _ClassVar[int]
    TIME_TO_FIELD_NUMBER: _ClassVar[int]
    CAPTURED_ALGORITHMS_FIELD_NUMBER: _ClassVar[int]
    CAPTURED_WINDOWS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    time_from: _timestamp_pb2.Timestamp
    time_to: _timestamp_pb2.Timestamp
    captured_algorithms: _containers.RepeatedCompositeFieldContainer[Algorithm]
    captured_windows: _containers.RepeatedCompositeFieldContainer[WindowType]
    description: str
    metadata: _struct_pb2.Struct
    def __init__(self, time_from: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., time_to: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., captured_algorithms: _Optional[_Iterable[_Union[Algorithm, _Mapping]]] = ..., captured_windows: _Optional[_Iterable[_Union[WindowType, _Mapping]]] = ..., description: _Optional[str] = ..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class AnnotateResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KnowledgeBaseType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    KNOWLEDGE_BASE_TYPE_UNSPECIFIED: _ClassVar[KnowledgeBaseType]
    KNOWLEDGE_BASE_TYPE_PROMPT: _ClassVar[KnowledgeBaseType]
    KNOWLEDGE_BASE_TYPE_EMBEDDING: _ClassVar[KnowledgeBaseType]
KNOWLEDGE_BASE_TYPE_UNSPECIFIED: KnowledgeBaseType
KNOWLEDGE_BASE_TYPE_PROMPT: KnowledgeBaseType
KNOWLEDGE_BASE_TYPE_EMBEDDING: KnowledgeBaseType

class CreateOrUpdateKnowledgeBaseRequest(_message.Message):
    __slots__ = ("attachment_rid", "summary_description", "type")
    ATTACHMENT_RID_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    attachment_rid: str
    summary_description: str
    type: KnowledgeBaseType
    def __init__(self, attachment_rid: _Optional[str] = ..., summary_description: _Optional[str] = ..., type: _Optional[_Union[KnowledgeBaseType, str]] = ...) -> None: ...

class CreateOrUpdateKnowledgeBaseResponse(_message.Message):
    __slots__ = ("knowledge_base_rid",)
    KNOWLEDGE_BASE_RID_FIELD_NUMBER: _ClassVar[int]
    knowledge_base_rid: str
    def __init__(self, knowledge_base_rid: _Optional[str] = ...) -> None: ...

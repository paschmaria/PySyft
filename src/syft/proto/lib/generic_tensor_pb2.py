# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/lib/generic_tensor.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from syft.proto.lib.numpy import tensor_pb2 as proto_dot_lib_dot_numpy_dot_tensor__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name="proto/lib/generic_tensor.proto",
    package="syft.lib",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x1eproto/lib/generic_tensor.proto\x12\x08syft.lib\x1a\x1cproto/lib/numpy/tensor.proto"B\n\rGenericTensor\x12\x31\n\x0cnumpy_tensor\x18\x01 \x01(\x0b\x32\x1b.syft.lib.numpy.TensorProtob\x06proto3',
    dependencies=[proto_dot_lib_dot_numpy_dot_tensor__pb2.DESCRIPTOR,],
)


_GENERICTENSOR = _descriptor.Descriptor(
    name="GenericTensor",
    full_name="syft.lib.GenericTensor",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="numpy_tensor",
            full_name="syft.lib.GenericTensor.numpy_tensor",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=74,
    serialized_end=140,
)

_GENERICTENSOR.fields_by_name[
    "numpy_tensor"
].message_type = proto_dot_lib_dot_numpy_dot_tensor__pb2._TENSORPROTO
DESCRIPTOR.message_types_by_name["GenericTensor"] = _GENERICTENSOR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GenericTensor = _reflection.GeneratedProtocolMessageType(
    "GenericTensor",
    (_message.Message,),
    {
        "DESCRIPTOR": _GENERICTENSOR,
        "__module__": "proto.lib.generic_tensor_pb2"
        # @@protoc_insertion_point(class_scope:syft.lib.GenericTensor)
    },
)
_sym_db.RegisterMessage(GenericTensor)


# @@protoc_insertion_point(module_scope)

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: update_metadata.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="update_metadata.proto",
    package="chromeos_update_engine",
    syntax="proto2",
    serialized_pb=_b(
        '\n\x15update_metadata.proto\x12\x16\x63hromeos_update_engine"1\n\x06\x45xtent\x12\x13\n\x0bstart_block\x18\x01 \x01(\x04\x12\x12\n\nnum_blocks\x18\x02 \x01(\x04"z\n\nSignatures\x12@\n\nsignatures\x18\x01 \x03(\x0b\x32,.chromeos_update_engine.Signatures.Signature\x1a*\n\tSignature\x12\x0f\n\x07version\x18\x01 \x01(\r\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c"+\n\rPartitionInfo\x12\x0c\n\x04size\x18\x01 \x01(\x04\x12\x0c\n\x04hash\x18\x02 \x01(\x0c"w\n\tImageInfo\x12\r\n\x05\x62oard\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x0f\n\x07\x63hannel\x18\x03 \x01(\t\x12\x0f\n\x07version\x18\x04 \x01(\t\x12\x15\n\rbuild_channel\x18\x05 \x01(\t\x12\x15\n\rbuild_version\x18\x06 \x01(\t"\xd3\x03\n\x10InstallOperation\x12;\n\x04type\x18\x01 \x02(\x0e\x32-.chromeos_update_engine.InstallOperation.Type\x12\x13\n\x0b\x64\x61ta_offset\x18\x02 \x01(\r\x12\x13\n\x0b\x64\x61ta_length\x18\x03 \x01(\r\x12\x33\n\x0bsrc_extents\x18\x04 \x03(\x0b\x32\x1e.chromeos_update_engine.Extent\x12\x12\n\nsrc_length\x18\x05 \x01(\x04\x12\x33\n\x0b\x64st_extents\x18\x06 \x03(\x0b\x32\x1e.chromeos_update_engine.Extent\x12\x12\n\ndst_length\x18\x07 \x01(\x04\x12\x18\n\x10\x64\x61ta_sha256_hash\x18\x08 \x01(\x0c\x12\x17\n\x0fsrc_sha256_hash\x18\t \x01(\x0c"\x92\x01\n\x04Type\x12\x0b\n\x07REPLACE\x10\x00\x12\x0e\n\nREPLACE_BZ\x10\x01\x12\x08\n\x04MOVE\x10\x02\x12\n\n\x06\x42SDIFF\x10\x03\x12\x0f\n\x0bSOURCE_COPY\x10\x04\x12\x11\n\rSOURCE_BSDIFF\x10\x05\x12\x08\n\x04ZERO\x10\x06\x12\x0b\n\x07\x44ISCARD\x10\x07\x12\x0e\n\nREPLACE_XZ\x10\x08\x12\x0c\n\x08PUFFDIFF\x10\t"\xa6\x03\n\x0fPartitionUpdate\x12\x16\n\x0epartition_name\x18\x01 \x02(\t\x12\x17\n\x0frun_postinstall\x18\x02 \x01(\x08\x12\x18\n\x10postinstall_path\x18\x03 \x01(\t\x12\x17\n\x0f\x66ilesystem_type\x18\x04 \x01(\t\x12M\n\x17new_partition_signature\x18\x05 \x03(\x0b\x32,.chromeos_update_engine.Signatures.Signature\x12\x41\n\x12old_partition_info\x18\x06 \x01(\x0b\x32%.chromeos_update_engine.PartitionInfo\x12\x41\n\x12new_partition_info\x18\x07 \x01(\x0b\x32%.chromeos_update_engine.PartitionInfo\x12<\n\noperations\x18\x08 \x03(\x0b\x32(.chromeos_update_engine.InstallOperation\x12\x1c\n\x14postinstall_optional\x18\t \x01(\x08"\xc4\x05\n\x14\x44\x65ltaArchiveManifest\x12\x44\n\x12install_operations\x18\x01 \x03(\x0b\x32(.chromeos_update_engine.InstallOperation\x12K\n\x19kernel_install_operations\x18\x02 \x03(\x0b\x32(.chromeos_update_engine.InstallOperation\x12\x18\n\nblock_size\x18\x03 \x01(\r:\x04\x34\x30\x39\x36\x12\x19\n\x11signatures_offset\x18\x04 \x01(\x04\x12\x17\n\x0fsignatures_size\x18\x05 \x01(\x04\x12>\n\x0fold_kernel_info\x18\x06 \x01(\x0b\x32%.chromeos_update_engine.PartitionInfo\x12>\n\x0fnew_kernel_info\x18\x07 \x01(\x0b\x32%.chromeos_update_engine.PartitionInfo\x12>\n\x0fold_rootfs_info\x18\x08 \x01(\x0b\x32%.chromeos_update_engine.PartitionInfo\x12>\n\x0fnew_rootfs_info\x18\t \x01(\x0b\x32%.chromeos_update_engine.PartitionInfo\x12\x39\n\x0eold_image_info\x18\n \x01(\x0b\x32!.chromeos_update_engine.ImageInfo\x12\x39\n\x0enew_image_info\x18\x0b \x01(\x0b\x32!.chromeos_update_engine.ImageInfo\x12\x18\n\rminor_version\x18\x0c \x01(\r:\x01\x30\x12;\n\npartitions\x18\r \x03(\x0b\x32\'.chromeos_update_engine.PartitionUpdateB\x02H\x03'
    ),
)


_INSTALLOPERATION_TYPE = _descriptor.EnumDescriptor(
    name="Type",
    full_name="chromeos_update_engine.InstallOperation.Type",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="REPLACE", index=0, number=0, options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="REPLACE_BZ", index=1, number=1, options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="MOVE", index=2, number=2, options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="BSDIFF", index=3, number=3, options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="SOURCE_COPY", index=4, number=4, options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="SOURCE_BSDIFF", index=5, number=5, options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="ZERO", index=6, number=6, options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="DISCARD", index=7, number=7, options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="REPLACE_XZ", index=8, number=8, options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="PUFFDIFF", index=9, number=9, options=None, type=None
        ),
    ],
    containing_type=None,
    options=None,
    serialized_start=712,
    serialized_end=858,
)
_sym_db.RegisterEnumDescriptor(_INSTALLOPERATION_TYPE)


_EXTENT = _descriptor.Descriptor(
    name="Extent",
    full_name="chromeos_update_engine.Extent",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="start_block",
            full_name="chromeos_update_engine.Extent.start_block",
            index=0,
            number=1,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="num_blocks",
            full_name="chromeos_update_engine.Extent.num_blocks",
            index=1,
            number=2,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=49,
    serialized_end=98,
)


_SIGNATURES_SIGNATURE = _descriptor.Descriptor(
    name="Signature",
    full_name="chromeos_update_engine.Signatures.Signature",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="version",
            full_name="chromeos_update_engine.Signatures.Signature.version",
            index=0,
            number=1,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="data",
            full_name="chromeos_update_engine.Signatures.Signature.data",
            index=1,
            number=2,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b(""),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=180,
    serialized_end=222,
)

_SIGNATURES = _descriptor.Descriptor(
    name="Signatures",
    full_name="chromeos_update_engine.Signatures",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="signatures",
            full_name="chromeos_update_engine.Signatures.signatures",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
    ],
    extensions=[],
    nested_types=[
        _SIGNATURES_SIGNATURE,
    ],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=100,
    serialized_end=222,
)


_PARTITIONINFO = _descriptor.Descriptor(
    name="PartitionInfo",
    full_name="chromeos_update_engine.PartitionInfo",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="size",
            full_name="chromeos_update_engine.PartitionInfo.size",
            index=0,
            number=1,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="hash",
            full_name="chromeos_update_engine.PartitionInfo.hash",
            index=1,
            number=2,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b(""),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=224,
    serialized_end=267,
)


_IMAGEINFO = _descriptor.Descriptor(
    name="ImageInfo",
    full_name="chromeos_update_engine.ImageInfo",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="board",
            full_name="chromeos_update_engine.ImageInfo.board",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="key",
            full_name="chromeos_update_engine.ImageInfo.key",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="channel",
            full_name="chromeos_update_engine.ImageInfo.channel",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="version",
            full_name="chromeos_update_engine.ImageInfo.version",
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="build_channel",
            full_name="chromeos_update_engine.ImageInfo.build_channel",
            index=4,
            number=5,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="build_version",
            full_name="chromeos_update_engine.ImageInfo.build_version",
            index=5,
            number=6,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=269,
    serialized_end=388,
)


_INSTALLOPERATION = _descriptor.Descriptor(
    name="InstallOperation",
    full_name="chromeos_update_engine.InstallOperation",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="type",
            full_name="chromeos_update_engine.InstallOperation.type",
            index=0,
            number=1,
            type=14,
            cpp_type=8,
            label=2,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="data_offset",
            full_name="chromeos_update_engine.InstallOperation.data_offset",
            index=1,
            number=2,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="data_length",
            full_name="chromeos_update_engine.InstallOperation.data_length",
            index=2,
            number=3,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="src_extents",
            full_name="chromeos_update_engine.InstallOperation.src_extents",
            index=3,
            number=4,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="src_length",
            full_name="chromeos_update_engine.InstallOperation.src_length",
            index=4,
            number=5,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="dst_extents",
            full_name="chromeos_update_engine.InstallOperation.dst_extents",
            index=5,
            number=6,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="dst_length",
            full_name="chromeos_update_engine.InstallOperation.dst_length",
            index=6,
            number=7,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="data_sha256_hash",
            full_name="chromeos_update_engine.InstallOperation.data_sha256_hash",
            index=7,
            number=8,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b(""),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="src_sha256_hash",
            full_name="chromeos_update_engine.InstallOperation.src_sha256_hash",
            index=8,
            number=9,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b(""),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[
        _INSTALLOPERATION_TYPE,
    ],
    options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=391,
    serialized_end=858,
)


_PARTITIONUPDATE = _descriptor.Descriptor(
    name="PartitionUpdate",
    full_name="chromeos_update_engine.PartitionUpdate",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="partition_name",
            full_name="chromeos_update_engine.PartitionUpdate.partition_name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=2,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="run_postinstall",
            full_name="chromeos_update_engine.PartitionUpdate.run_postinstall",
            index=1,
            number=2,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="postinstall_path",
            full_name="chromeos_update_engine.PartitionUpdate.postinstall_path",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="filesystem_type",
            full_name="chromeos_update_engine.PartitionUpdate.filesystem_type",
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="new_partition_signature",
            full_name="chromeos_update_engine.PartitionUpdate.new_partition_signature",
            index=4,
            number=5,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="old_partition_info",
            full_name="chromeos_update_engine.PartitionUpdate.old_partition_info",
            index=5,
            number=6,
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
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="new_partition_info",
            full_name="chromeos_update_engine.PartitionUpdate.new_partition_info",
            index=6,
            number=7,
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
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="operations",
            full_name="chromeos_update_engine.PartitionUpdate.operations",
            index=7,
            number=8,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="postinstall_optional",
            full_name="chromeos_update_engine.PartitionUpdate.postinstall_optional",
            index=8,
            number=9,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=861,
    serialized_end=1283,
)


_DELTAARCHIVEMANIFEST = _descriptor.Descriptor(
    name="DeltaArchiveManifest",
    full_name="chromeos_update_engine.DeltaArchiveManifest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="install_operations",
            full_name="chromeos_update_engine.DeltaArchiveManifest.install_operations",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="kernel_install_operations",
            full_name="chromeos_update_engine.DeltaArchiveManifest.kernel_install_operations",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="block_size",
            full_name="chromeos_update_engine.DeltaArchiveManifest.block_size",
            index=2,
            number=3,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=True,
            default_value=4096,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="signatures_offset",
            full_name="chromeos_update_engine.DeltaArchiveManifest.signatures_offset",
            index=3,
            number=4,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="signatures_size",
            full_name="chromeos_update_engine.DeltaArchiveManifest.signatures_size",
            index=4,
            number=5,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="old_kernel_info",
            full_name="chromeos_update_engine.DeltaArchiveManifest.old_kernel_info",
            index=5,
            number=6,
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
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="new_kernel_info",
            full_name="chromeos_update_engine.DeltaArchiveManifest.new_kernel_info",
            index=6,
            number=7,
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
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="old_rootfs_info",
            full_name="chromeos_update_engine.DeltaArchiveManifest.old_rootfs_info",
            index=7,
            number=8,
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
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="new_rootfs_info",
            full_name="chromeos_update_engine.DeltaArchiveManifest.new_rootfs_info",
            index=8,
            number=9,
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
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="old_image_info",
            full_name="chromeos_update_engine.DeltaArchiveManifest.old_image_info",
            index=9,
            number=10,
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
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="new_image_info",
            full_name="chromeos_update_engine.DeltaArchiveManifest.new_image_info",
            index=10,
            number=11,
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
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="minor_version",
            full_name="chromeos_update_engine.DeltaArchiveManifest.minor_version",
            index=11,
            number=12,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=True,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="partitions",
            full_name="chromeos_update_engine.DeltaArchiveManifest.partitions",
            index=12,
            number=13,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1286,
    serialized_end=1994,
)

_SIGNATURES_SIGNATURE.containing_type = _SIGNATURES
_SIGNATURES.fields_by_name["signatures"].message_type = _SIGNATURES_SIGNATURE
_INSTALLOPERATION.fields_by_name["type"].enum_type = _INSTALLOPERATION_TYPE
_INSTALLOPERATION.fields_by_name["src_extents"].message_type = _EXTENT
_INSTALLOPERATION.fields_by_name["dst_extents"].message_type = _EXTENT
_INSTALLOPERATION_TYPE.containing_type = _INSTALLOPERATION
_PARTITIONUPDATE.fields_by_name[
    "new_partition_signature"
].message_type = _SIGNATURES_SIGNATURE
_PARTITIONUPDATE.fields_by_name["old_partition_info"].message_type = _PARTITIONINFO
_PARTITIONUPDATE.fields_by_name["new_partition_info"].message_type = _PARTITIONINFO
_PARTITIONUPDATE.fields_by_name["operations"].message_type = _INSTALLOPERATION
_DELTAARCHIVEMANIFEST.fields_by_name[
    "install_operations"
].message_type = _INSTALLOPERATION
_DELTAARCHIVEMANIFEST.fields_by_name[
    "kernel_install_operations"
].message_type = _INSTALLOPERATION
_DELTAARCHIVEMANIFEST.fields_by_name["old_kernel_info"].message_type = _PARTITIONINFO
_DELTAARCHIVEMANIFEST.fields_by_name["new_kernel_info"].message_type = _PARTITIONINFO
_DELTAARCHIVEMANIFEST.fields_by_name["old_rootfs_info"].message_type = _PARTITIONINFO
_DELTAARCHIVEMANIFEST.fields_by_name["new_rootfs_info"].message_type = _PARTITIONINFO
_DELTAARCHIVEMANIFEST.fields_by_name["old_image_info"].message_type = _IMAGEINFO
_DELTAARCHIVEMANIFEST.fields_by_name["new_image_info"].message_type = _IMAGEINFO
_DELTAARCHIVEMANIFEST.fields_by_name["partitions"].message_type = _PARTITIONUPDATE
DESCRIPTOR.message_types_by_name["Extent"] = _EXTENT
DESCRIPTOR.message_types_by_name["Signatures"] = _SIGNATURES
DESCRIPTOR.message_types_by_name["PartitionInfo"] = _PARTITIONINFO
DESCRIPTOR.message_types_by_name["ImageInfo"] = _IMAGEINFO
DESCRIPTOR.message_types_by_name["InstallOperation"] = _INSTALLOPERATION
DESCRIPTOR.message_types_by_name["PartitionUpdate"] = _PARTITIONUPDATE
DESCRIPTOR.message_types_by_name["DeltaArchiveManifest"] = _DELTAARCHIVEMANIFEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Extent = _reflection.GeneratedProtocolMessageType(
    "Extent",
    (_message.Message,),
    dict(
        DESCRIPTOR=_EXTENT,
        __module__="update_metadata_pb2"
        # @@protoc_insertion_point(class_scope:chromeos_update_engine.Extent)
    ),
)
_sym_db.RegisterMessage(Extent)

Signatures = _reflection.GeneratedProtocolMessageType(
    "Signatures",
    (_message.Message,),
    dict(
        Signature=_reflection.GeneratedProtocolMessageType(
            "Signature",
            (_message.Message,),
            dict(
                DESCRIPTOR=_SIGNATURES_SIGNATURE,
                __module__="update_metadata_pb2"
                # @@protoc_insertion_point(class_scope:chromeos_update_engine.Signatures.Signature)
            ),
        ),
        DESCRIPTOR=_SIGNATURES,
        __module__="update_metadata_pb2"
        # @@protoc_insertion_point(class_scope:chromeos_update_engine.Signatures)
    ),
)
_sym_db.RegisterMessage(Signatures)
_sym_db.RegisterMessage(Signatures.Signature)

PartitionInfo = _reflection.GeneratedProtocolMessageType(
    "PartitionInfo",
    (_message.Message,),
    dict(
        DESCRIPTOR=_PARTITIONINFO,
        __module__="update_metadata_pb2"
        # @@protoc_insertion_point(class_scope:chromeos_update_engine.PartitionInfo)
    ),
)
_sym_db.RegisterMessage(PartitionInfo)

ImageInfo = _reflection.GeneratedProtocolMessageType(
    "ImageInfo",
    (_message.Message,),
    dict(
        DESCRIPTOR=_IMAGEINFO,
        __module__="update_metadata_pb2"
        # @@protoc_insertion_point(class_scope:chromeos_update_engine.ImageInfo)
    ),
)
_sym_db.RegisterMessage(ImageInfo)

InstallOperation = _reflection.GeneratedProtocolMessageType(
    "InstallOperation",
    (_message.Message,),
    dict(
        DESCRIPTOR=_INSTALLOPERATION,
        __module__="update_metadata_pb2"
        # @@protoc_insertion_point(class_scope:chromeos_update_engine.InstallOperation)
    ),
)
_sym_db.RegisterMessage(InstallOperation)

PartitionUpdate = _reflection.GeneratedProtocolMessageType(
    "PartitionUpdate",
    (_message.Message,),
    dict(
        DESCRIPTOR=_PARTITIONUPDATE,
        __module__="update_metadata_pb2"
        # @@protoc_insertion_point(class_scope:chromeos_update_engine.PartitionUpdate)
    ),
)
_sym_db.RegisterMessage(PartitionUpdate)

DeltaArchiveManifest = _reflection.GeneratedProtocolMessageType(
    "DeltaArchiveManifest",
    (_message.Message,),
    dict(
        DESCRIPTOR=_DELTAARCHIVEMANIFEST,
        __module__="update_metadata_pb2"
        # @@protoc_insertion_point(class_scope:chromeos_update_engine.DeltaArchiveManifest)
    ),
)
_sym_db.RegisterMessage(DeltaArchiveManifest)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(
    descriptor_pb2.FileOptions(), _b("H\003")
)
# @@protoc_insertion_point(module_scope)

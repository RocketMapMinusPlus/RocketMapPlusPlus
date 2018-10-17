# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/encounter_type.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/enums/encounter_type.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n%pogoprotos/enums/encounter_type.proto\x12\x10pogoprotos.enums*\x82\x01\n\rEncounterType\x12\x0f\n\x0bSPAWN_POINT\x10\x00\x12\x0b\n\x07INCENSE\x10\x01\x12\x08\n\x04\x44ISK\x10\x02\x12\r\n\tPOST_RAID\x10\x03\x12\x0f\n\x0bSTORY_QUEST\x10\x04\x12\x14\n\x10QUEST_STAMP_CARD\x10\x05\x12\x13\n\x0f\x43HALLENGE_QUEST\x10\x06\x62\x06proto3')
)

_ENCOUNTERTYPE = _descriptor.EnumDescriptor(
  name='EncounterType',
  full_name='pogoprotos.enums.EncounterType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SPAWN_POINT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INCENSE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISK', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POST_RAID', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STORY_QUEST', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUEST_STAMP_CARD', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHALLENGE_QUEST', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=60,
  serialized_end=190,
)
_sym_db.RegisterEnumDescriptor(_ENCOUNTERTYPE)

EncounterType = enum_type_wrapper.EnumTypeWrapper(_ENCOUNTERTYPE)
SPAWN_POINT = 0
INCENSE = 1
DISK = 2
POST_RAID = 3
STORY_QUEST = 4
QUEST_STAMP_CARD = 5
CHALLENGE_QUEST = 6


DESCRIPTOR.enum_types_by_name['EncounterType'] = _ENCOUNTERTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)

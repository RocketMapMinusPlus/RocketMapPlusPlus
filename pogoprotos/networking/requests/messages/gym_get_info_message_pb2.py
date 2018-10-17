# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/gym_get_info_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/messages/gym_get_info_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nBpogoprotos/networking/requests/messages/gym_get_info_message.proto\x12\'pogoprotos.networking.requests.messages\"\x8d\x01\n\x11GymGetInfoMessage\x12\x0e\n\x06gym_id\x18\x01 \x01(\t\x12\x1a\n\x12player_lat_degrees\x18\x02 \x01(\x01\x12\x1a\n\x12player_lng_degrees\x18\x03 \x01(\x01\x12\x17\n\x0fgym_lat_degrees\x18\x04 \x01(\x01\x12\x17\n\x0fgym_lng_degrees\x18\x05 \x01(\x01\x62\x06proto3')
)




_GYMGETINFOMESSAGE = _descriptor.Descriptor(
  name='GymGetInfoMessage',
  full_name='pogoprotos.networking.requests.messages.GymGetInfoMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gym_id', full_name='pogoprotos.networking.requests.messages.GymGetInfoMessage.gym_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='player_lat_degrees', full_name='pogoprotos.networking.requests.messages.GymGetInfoMessage.player_lat_degrees', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='player_lng_degrees', full_name='pogoprotos.networking.requests.messages.GymGetInfoMessage.player_lng_degrees', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gym_lat_degrees', full_name='pogoprotos.networking.requests.messages.GymGetInfoMessage.gym_lat_degrees', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gym_lng_degrees', full_name='pogoprotos.networking.requests.messages.GymGetInfoMessage.gym_lng_degrees', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=112,
  serialized_end=253,
)

DESCRIPTOR.message_types_by_name['GymGetInfoMessage'] = _GYMGETINFOMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GymGetInfoMessage = _reflection.GeneratedProtocolMessageType('GymGetInfoMessage', (_message.Message,), dict(
  DESCRIPTOR = _GYMGETINFOMESSAGE,
  __module__ = 'pogoprotos.networking.requests.messages.gym_get_info_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.GymGetInfoMessage)
  ))
_sym_db.RegisterMessage(GymGetInfoMessage)


# @@protoc_insertion_point(module_scope)

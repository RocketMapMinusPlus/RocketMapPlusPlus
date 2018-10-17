# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/telemetry/login_action_telemetry.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import telemetry_ids_pb2 as pogoprotos_dot_enums_dot_telemetry__ids__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/telemetry/login_action_telemetry.proto',
  package='pogoprotos.data.telemetry',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n6pogoprotos/data/telemetry/login_action_telemetry.proto\x12\x19pogoprotos.data.telemetry\x1a$pogoprotos/enums/telemetry_ids.proto\"\xbc\x01\n\x14LoginActionTelemetry\x12\x42\n\x0flogin_action_id\x18\x01 \x01(\x0e\x32).pogoprotos.enums.LoginActionTelemetryIds\x12\x12\n\nfirst_time\x18\x02 \x01(\x08\x12\x0f\n\x07success\x18\x03 \x01(\t\x12\r\n\x05\x65rror\x18\x04 \x01(\t\x12\x17\n\x0fintent_existing\x18\x05 \x01(\t\x12\x13\n\x0b\x61uth_status\x18\x06 \x01(\tb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_telemetry__ids__pb2.DESCRIPTOR,])




_LOGINACTIONTELEMETRY = _descriptor.Descriptor(
  name='LoginActionTelemetry',
  full_name='pogoprotos.data.telemetry.LoginActionTelemetry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='login_action_id', full_name='pogoprotos.data.telemetry.LoginActionTelemetry.login_action_id', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='first_time', full_name='pogoprotos.data.telemetry.LoginActionTelemetry.first_time', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='success', full_name='pogoprotos.data.telemetry.LoginActionTelemetry.success', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='pogoprotos.data.telemetry.LoginActionTelemetry.error', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='intent_existing', full_name='pogoprotos.data.telemetry.LoginActionTelemetry.intent_existing', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='auth_status', full_name='pogoprotos.data.telemetry.LoginActionTelemetry.auth_status', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=124,
  serialized_end=312,
)

_LOGINACTIONTELEMETRY.fields_by_name['login_action_id'].enum_type = pogoprotos_dot_enums_dot_telemetry__ids__pb2._LOGINACTIONTELEMETRYIDS
DESCRIPTOR.message_types_by_name['LoginActionTelemetry'] = _LOGINACTIONTELEMETRY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LoginActionTelemetry = _reflection.GeneratedProtocolMessageType('LoginActionTelemetry', (_message.Message,), dict(
  DESCRIPTOR = _LOGINACTIONTELEMETRY,
  __module__ = 'pogoprotos.data.telemetry.login_action_telemetry_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.telemetry.LoginActionTelemetry)
  ))
_sym_db.RegisterMessage(LoginActionTelemetry)


# @@protoc_insertion_point(module_scope)

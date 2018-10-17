# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/player/currency.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/player/currency.proto',
  package='pogoprotos.data.player',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n%pogoprotos/data/player/currency.proto\x12\x16pogoprotos.data.player\"\x8f\x01\n\x08\x43urrency\x12\x15\n\rcurrency_type\x18\x01 \x01(\t\x12\x10\n\x08quantity\x18\x02 \x01(\x05\x12\x1f\n\x17\x66iat_purchased_quantity\x18\x03 \x01(\x05\x12\x1a\n\x12\x66iat_currency_type\x18\x04 \x01(\t\x12\x1d\n\x15\x66iat_currency_cost_e6\x18\x05 \x01(\x03\x62\x06proto3')
)




_CURRENCY = _descriptor.Descriptor(
  name='Currency',
  full_name='pogoprotos.data.player.Currency',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='currency_type', full_name='pogoprotos.data.player.Currency.currency_type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quantity', full_name='pogoprotos.data.player.Currency.quantity', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fiat_purchased_quantity', full_name='pogoprotos.data.player.Currency.fiat_purchased_quantity', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fiat_currency_type', full_name='pogoprotos.data.player.Currency.fiat_currency_type', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fiat_currency_cost_e6', full_name='pogoprotos.data.player.Currency.fiat_currency_cost_e6', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=66,
  serialized_end=209,
)

DESCRIPTOR.message_types_by_name['Currency'] = _CURRENCY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Currency = _reflection.GeneratedProtocolMessageType('Currency', (_message.Message,), dict(
  DESCRIPTOR = _CURRENCY,
  __module__ = 'pogoprotos.data.player.currency_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.player.Currency)
  ))
_sym_db.RegisterMessage(Currency)


# @@protoc_insertion_point(module_scope)

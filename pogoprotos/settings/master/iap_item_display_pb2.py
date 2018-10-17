# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/master/iap_item_display.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import iap_item_category_pb2 as pogoprotos_dot_enums_dot_iap__item__category__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/master/iap_item_display.proto',
  package='pogoprotos.settings.master',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n1pogoprotos/settings/master/iap_item_display.proto\x12\x1apogoprotos.settings.master\x1a(pogoprotos/enums/iap_item_category.proto\"\xbf\x01\n\x0eIapItemDisplay\x12\x0b\n\x03sku\x18\x01 \x01(\t\x12\x37\n\x08\x63\x61tegory\x18\x02 \x01(\x0e\x32%.pogoprotos.enums.HoloIapItemCategory\x12\x12\n\nsort_order\x18\x03 \x01(\x05\x12\x0e\n\x06hidden\x18\x06 \x01(\x08\x12\x0c\n\x04sale\x18\x07 \x01(\x08\x12\x11\n\tsprite_id\x18\x08 \x01(\t\x12\r\n\x05title\x18\t \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\n \x01(\tb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_iap__item__category__pb2.DESCRIPTOR,])




_IAPITEMDISPLAY = _descriptor.Descriptor(
  name='IapItemDisplay',
  full_name='pogoprotos.settings.master.IapItemDisplay',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sku', full_name='pogoprotos.settings.master.IapItemDisplay.sku', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='pogoprotos.settings.master.IapItemDisplay.category', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sort_order', full_name='pogoprotos.settings.master.IapItemDisplay.sort_order', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hidden', full_name='pogoprotos.settings.master.IapItemDisplay.hidden', index=3,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sale', full_name='pogoprotos.settings.master.IapItemDisplay.sale', index=4,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sprite_id', full_name='pogoprotos.settings.master.IapItemDisplay.sprite_id', index=5,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='pogoprotos.settings.master.IapItemDisplay.title', index=6,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='pogoprotos.settings.master.IapItemDisplay.description', index=7,
      number=10, type=9, cpp_type=9, label=1,
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
  serialized_end=315,
)

_IAPITEMDISPLAY.fields_by_name['category'].enum_type = pogoprotos_dot_enums_dot_iap__item__category__pb2._HOLOIAPITEMCATEGORY
DESCRIPTOR.message_types_by_name['IapItemDisplay'] = _IAPITEMDISPLAY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

IapItemDisplay = _reflection.GeneratedProtocolMessageType('IapItemDisplay', (_message.Message,), dict(
  DESCRIPTOR = _IAPITEMDISPLAY,
  __module__ = 'pogoprotos.settings.master.iap_item_display_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.IapItemDisplay)
  ))
_sym_db.RegisterMessage(IapItemDisplay)


# @@protoc_insertion_point(module_scope)

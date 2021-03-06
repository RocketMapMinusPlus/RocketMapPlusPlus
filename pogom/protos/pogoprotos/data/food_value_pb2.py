# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/food_value.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.inventory.item import item_id_pb2 as pogoprotos_dot_inventory_dot_item_dot_item__id__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/food_value.proto',
  package='pogoprotos.data',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n pogoprotos/data/food_value.proto\x12\x0fpogoprotos.data\x1a\'pogoprotos/inventory/item/item_id.proto\"s\n\tFoodValue\x12\x1b\n\x13motivation_increase\x18\x01 \x01(\x02\x12\x13\n\x0b\x63p_increase\x18\x02 \x01(\x05\x12\x34\n\tfood_item\x18\x03 \x01(\x0e\x32!.pogoprotos.inventory.item.ItemIdb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_inventory_dot_item_dot_item__id__pb2.DESCRIPTOR,])




_FOODVALUE = _descriptor.Descriptor(
  name='FoodValue',
  full_name='pogoprotos.data.FoodValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='motivation_increase', full_name='pogoprotos.data.FoodValue.motivation_increase', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cp_increase', full_name='pogoprotos.data.FoodValue.cp_increase', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='food_item', full_name='pogoprotos.data.FoodValue.food_item', index=2,
      number=3, type=14, cpp_type=8, label=1,
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
  serialized_start=94,
  serialized_end=209,
)

_FOODVALUE.fields_by_name['food_item'].enum_type = pogoprotos_dot_inventory_dot_item_dot_item__id__pb2._ITEMID
DESCRIPTOR.message_types_by_name['FoodValue'] = _FOODVALUE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FoodValue = _reflection.GeneratedProtocolMessageType('FoodValue', (_message.Message,), dict(
  DESCRIPTOR = _FOODVALUE,
  __module__ = 'pogoprotos.data.food_value_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.FoodValue)
  ))
_sym_db.RegisterMessage(FoodValue)


# @@protoc_insertion_point(module_scope)

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/pokemon_trading_type.proto

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
  name='pogoprotos/enums/pokemon_trading_type.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n+pogoprotos/enums/pokemon_trading_type.proto\x12\x10pogoprotos.enums*\xda\x01\n\x12PokemonTradingType\x12\x19\n\x15UNSET_POKEMON_TRADING\x10\x00\x12\x16\n\x12REGULAR_IN_POKEDEX\x10\x01\x12\x16\n\x12SPECIAL_IN_POKEDEX\x10\x02\x12\x17\n\x13REGULAR_NON_POKEDEX\x10\x03\x12\x18\n\x14REGIONAL_NON_POKEDEX\x10\x04\x12\x14\n\x10\x46ORM_NON_POKEDEX\x10\x05\x12\x19\n\x15LEGENDARY_NON_POKEDEX\x10\x06\x12\x15\n\x11SHINY_NON_POKEDEX\x10\x07\x62\x06proto3')
)

_POKEMONTRADINGTYPE = _descriptor.EnumDescriptor(
  name='PokemonTradingType',
  full_name='pogoprotos.enums.PokemonTradingType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET_POKEMON_TRADING', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REGULAR_IN_POKEDEX', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPECIAL_IN_POKEDEX', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REGULAR_NON_POKEDEX', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REGIONAL_NON_POKEDEX', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FORM_NON_POKEDEX', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LEGENDARY_NON_POKEDEX', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHINY_NON_POKEDEX', index=7, number=7,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=66,
  serialized_end=284,
)
_sym_db.RegisterEnumDescriptor(_POKEMONTRADINGTYPE)

PokemonTradingType = enum_type_wrapper.EnumTypeWrapper(_POKEMONTRADINGTYPE)
UNSET_POKEMON_TRADING = 0
REGULAR_IN_POKEDEX = 1
SPECIAL_IN_POKEDEX = 2
REGULAR_NON_POKEDEX = 3
REGIONAL_NON_POKEDEX = 4
FORM_NON_POKEDEX = 5
LEGENDARY_NON_POKEDEX = 6
SHINY_NON_POKEDEX = 7


DESCRIPTOR.enum_types_by_name['PokemonTradingType'] = _POKEMONTRADINGTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)

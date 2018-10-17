# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/master/item_settings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import item_category_pb2 as pogoprotos_dot_enums_dot_item__category__pb2
from pogoprotos.inventory.item import item_id_pb2 as pogoprotos_dot_inventory_dot_item_dot_item__id__pb2
from pogoprotos.inventory.item import item_type_pb2 as pogoprotos_dot_inventory_dot_item_dot_item__type__pb2
from pogoprotos.settings.master.item import food_attributes_pb2 as pogoprotos_dot_settings_dot_master_dot_item_dot_food__attributes__pb2
from pogoprotos.settings.master.item import potion_attributes_pb2 as pogoprotos_dot_settings_dot_master_dot_item_dot_potion__attributes__pb2
from pogoprotos.settings.master.item import revive_attributes_pb2 as pogoprotos_dot_settings_dot_master_dot_item_dot_revive__attributes__pb2
from pogoprotos.settings.master.item import battle_attributes_pb2 as pogoprotos_dot_settings_dot_master_dot_item_dot_battle__attributes__pb2
from pogoprotos.settings.master.item import incense_attributes_pb2 as pogoprotos_dot_settings_dot_master_dot_item_dot_incense__attributes__pb2
from pogoprotos.settings.master.item import pokeball_attributes_pb2 as pogoprotos_dot_settings_dot_master_dot_item_dot_pokeball__attributes__pb2
from pogoprotos.settings.master.item import fort_modifier_attributes_pb2 as pogoprotos_dot_settings_dot_master_dot_item_dot_fort__modifier__attributes__pb2
from pogoprotos.settings.master.item import egg_incubator_attributes_pb2 as pogoprotos_dot_settings_dot_master_dot_item_dot_egg__incubator__attributes__pb2
from pogoprotos.settings.master.item import experience_boost_attributes_pb2 as pogoprotos_dot_settings_dot_master_dot_item_dot_experience__boost__attributes__pb2
from pogoprotos.settings.master.item import inventory_upgrade_attributes_pb2 as pogoprotos_dot_settings_dot_master_dot_item_dot_inventory__upgrade__attributes__pb2
from pogoprotos.settings.master.item import stardust_boost_attributes_pb2 as pogoprotos_dot_settings_dot_master_dot_item_dot_stardust__boost__attributes__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/master/item_settings.proto',
  package='pogoprotos.settings.master',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n.pogoprotos/settings/master/item_settings.proto\x12\x1apogoprotos.settings.master\x1a$pogoprotos/enums/item_category.proto\x1a\'pogoprotos/inventory/item/item_id.proto\x1a)pogoprotos/inventory/item/item_type.proto\x1a\x35pogoprotos/settings/master/item/food_attributes.proto\x1a\x37pogoprotos/settings/master/item/potion_attributes.proto\x1a\x37pogoprotos/settings/master/item/revive_attributes.proto\x1a\x37pogoprotos/settings/master/item/battle_attributes.proto\x1a\x38pogoprotos/settings/master/item/incense_attributes.proto\x1a\x39pogoprotos/settings/master/item/pokeball_attributes.proto\x1a>pogoprotos/settings/master/item/fort_modifier_attributes.proto\x1a>pogoprotos/settings/master/item/egg_incubator_attributes.proto\x1a\x41pogoprotos/settings/master/item/experience_boost_attributes.proto\x1a\x42pogoprotos/settings/master/item/inventory_upgrade_attributes.proto\x1a?pogoprotos/settings/master/item/stardust_boost_attributes.proto\"\x87\x08\n\x0cItemSettings\x12\x32\n\x07item_id\x18\x01 \x01(\x0e\x32!.pogoprotos.inventory.item.ItemId\x12\x36\n\titem_type\x18\x02 \x01(\x0e\x32#.pogoprotos.inventory.item.ItemType\x12\x30\n\x08\x63\x61tegory\x18\x03 \x01(\x0e\x32\x1e.pogoprotos.enums.ItemCategory\x12\x11\n\tdrop_freq\x18\x04 \x01(\x02\x12\x1a\n\x12\x64rop_trainer_level\x18\x05 \x01(\x05\x12\x45\n\x08pokeball\x18\x06 \x01(\x0b\x32\x33.pogoprotos.settings.master.item.PokeballAttributes\x12\x41\n\x06potion\x18\x07 \x01(\x0b\x32\x31.pogoprotos.settings.master.item.PotionAttributes\x12\x41\n\x06revive\x18\x08 \x01(\x0b\x32\x31.pogoprotos.settings.master.item.ReviveAttributes\x12\x41\n\x06\x62\x61ttle\x18\t \x01(\x0b\x32\x31.pogoprotos.settings.master.item.BattleAttributes\x12=\n\x04\x66ood\x18\n \x01(\x0b\x32/.pogoprotos.settings.master.item.FoodAttributes\x12V\n\x11inventory_upgrade\x18\x0b \x01(\x0b\x32;.pogoprotos.settings.master.item.InventoryUpgradeAttributes\x12L\n\x08xp_boost\x18\x0c \x01(\x0b\x32:.pogoprotos.settings.master.item.ExperienceBoostAttributes\x12\x43\n\x07incense\x18\r \x01(\x0b\x32\x32.pogoprotos.settings.master.item.IncenseAttributes\x12N\n\regg_incubator\x18\x0e \x01(\x0b\x32\x37.pogoprotos.settings.master.item.EggIncubatorAttributes\x12N\n\rfort_modifier\x18\x0f \x01(\x0b\x32\x37.pogoprotos.settings.master.item.FortModifierAttributes\x12P\n\x0estardust_boost\x18\x10 \x01(\x0b\x32\x38.pogoprotos.settings.master.item.StardustBoostAttributesb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_item__category__pb2.DESCRIPTOR,pogoprotos_dot_inventory_dot_item_dot_item__id__pb2.DESCRIPTOR,pogoprotos_dot_inventory_dot_item_dot_item__type__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_master_dot_item_dot_food__attributes__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_master_dot_item_dot_potion__attributes__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_master_dot_item_dot_revive__attributes__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_master_dot_item_dot_battle__attributes__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_master_dot_item_dot_incense__attributes__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_master_dot_item_dot_pokeball__attributes__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_master_dot_item_dot_fort__modifier__attributes__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_master_dot_item_dot_egg__incubator__attributes__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_master_dot_item_dot_experience__boost__attributes__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_master_dot_item_dot_inventory__upgrade__attributes__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_master_dot_item_dot_stardust__boost__attributes__pb2.DESCRIPTOR,])




_ITEMSETTINGS = _descriptor.Descriptor(
  name='ItemSettings',
  full_name='pogoprotos.settings.master.ItemSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_id', full_name='pogoprotos.settings.master.ItemSettings.item_id', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='item_type', full_name='pogoprotos.settings.master.ItemSettings.item_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='pogoprotos.settings.master.ItemSettings.category', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='drop_freq', full_name='pogoprotos.settings.master.ItemSettings.drop_freq', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='drop_trainer_level', full_name='pogoprotos.settings.master.ItemSettings.drop_trainer_level', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pokeball', full_name='pogoprotos.settings.master.ItemSettings.pokeball', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='potion', full_name='pogoprotos.settings.master.ItemSettings.potion', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='revive', full_name='pogoprotos.settings.master.ItemSettings.revive', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='battle', full_name='pogoprotos.settings.master.ItemSettings.battle', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='food', full_name='pogoprotos.settings.master.ItemSettings.food', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inventory_upgrade', full_name='pogoprotos.settings.master.ItemSettings.inventory_upgrade', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='xp_boost', full_name='pogoprotos.settings.master.ItemSettings.xp_boost', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='incense', full_name='pogoprotos.settings.master.ItemSettings.incense', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='egg_incubator', full_name='pogoprotos.settings.master.ItemSettings.egg_incubator', index=13,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fort_modifier', full_name='pogoprotos.settings.master.ItemSettings.fort_modifier', index=14,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stardust_boost', full_name='pogoprotos.settings.master.ItemSettings.stardust_boost', index=15,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=872,
  serialized_end=1903,
)

_ITEMSETTINGS.fields_by_name['item_id'].enum_type = pogoprotos_dot_inventory_dot_item_dot_item__id__pb2._ITEMID
_ITEMSETTINGS.fields_by_name['item_type'].enum_type = pogoprotos_dot_inventory_dot_item_dot_item__type__pb2._ITEMTYPE
_ITEMSETTINGS.fields_by_name['category'].enum_type = pogoprotos_dot_enums_dot_item__category__pb2._ITEMCATEGORY
_ITEMSETTINGS.fields_by_name['pokeball'].message_type = pogoprotos_dot_settings_dot_master_dot_item_dot_pokeball__attributes__pb2._POKEBALLATTRIBUTES
_ITEMSETTINGS.fields_by_name['potion'].message_type = pogoprotos_dot_settings_dot_master_dot_item_dot_potion__attributes__pb2._POTIONATTRIBUTES
_ITEMSETTINGS.fields_by_name['revive'].message_type = pogoprotos_dot_settings_dot_master_dot_item_dot_revive__attributes__pb2._REVIVEATTRIBUTES
_ITEMSETTINGS.fields_by_name['battle'].message_type = pogoprotos_dot_settings_dot_master_dot_item_dot_battle__attributes__pb2._BATTLEATTRIBUTES
_ITEMSETTINGS.fields_by_name['food'].message_type = pogoprotos_dot_settings_dot_master_dot_item_dot_food__attributes__pb2._FOODATTRIBUTES
_ITEMSETTINGS.fields_by_name['inventory_upgrade'].message_type = pogoprotos_dot_settings_dot_master_dot_item_dot_inventory__upgrade__attributes__pb2._INVENTORYUPGRADEATTRIBUTES
_ITEMSETTINGS.fields_by_name['xp_boost'].message_type = pogoprotos_dot_settings_dot_master_dot_item_dot_experience__boost__attributes__pb2._EXPERIENCEBOOSTATTRIBUTES
_ITEMSETTINGS.fields_by_name['incense'].message_type = pogoprotos_dot_settings_dot_master_dot_item_dot_incense__attributes__pb2._INCENSEATTRIBUTES
_ITEMSETTINGS.fields_by_name['egg_incubator'].message_type = pogoprotos_dot_settings_dot_master_dot_item_dot_egg__incubator__attributes__pb2._EGGINCUBATORATTRIBUTES
_ITEMSETTINGS.fields_by_name['fort_modifier'].message_type = pogoprotos_dot_settings_dot_master_dot_item_dot_fort__modifier__attributes__pb2._FORTMODIFIERATTRIBUTES
_ITEMSETTINGS.fields_by_name['stardust_boost'].message_type = pogoprotos_dot_settings_dot_master_dot_item_dot_stardust__boost__attributes__pb2._STARDUSTBOOSTATTRIBUTES
DESCRIPTOR.message_types_by_name['ItemSettings'] = _ITEMSETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ItemSettings = _reflection.GeneratedProtocolMessageType('ItemSettings', (_message.Message,), dict(
  DESCRIPTOR = _ITEMSETTINGS,
  __module__ = 'pogoprotos.settings.master.item_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.ItemSettings)
  ))
_sym_db.RegisterMessage(ItemSettings)


# @@protoc_insertion_point(module_scope)

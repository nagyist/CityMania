# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import service
from google.protobuf import service_reflection
from google.protobuf import descriptor_pb2


_LOGINRESPONSE_TYPE = descriptor.EnumDescriptor(
  name='Type',
  full_name='LoginResponse.Type',
  filename='Type',
  values=[
    descriptor.EnumValueDescriptor(
      name='FAILURE', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      options=None,
      type=None),
  ],
  options=None,
)

_LOGINRESPONSE_USERTYPE = descriptor.EnumDescriptor(
  name='Usertype',
  full_name='LoginResponse.Usertype',
  filename='Usertype',
  values=[
    descriptor.EnumValueDescriptor(
      name='OBSERVE', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='NORMAL', index=1, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='GM', index=2, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ADMIN', index=3, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='OWNER', index=4, number=4,
      options=None,
      type=None),
  ],
  options=None,
)

_SELECTCITYRESPONSE_TYPE = descriptor.EnumDescriptor(
  name='Type',
  full_name='SelectCityResponse.Type',
  filename='Type',
  values=[
    descriptor.EnumValueDescriptor(
      name='FAILURE', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      options=None,
      type=None),
  ],
  options=None,
)

_NEWCITYRESPONSE_TYPE = descriptor.EnumDescriptor(
  name='Type',
  full_name='NewCityResponse.Type',
  filename='Type',
  values=[
    descriptor.EnumValueDescriptor(
      name='FAILURE', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      options=None,
      type=None),
  ],
  options=None,
)


_CONTAINER = descriptor.Descriptor(
  name='Container',
  full_name='Container',
  filename='protocol.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='chat', full_name='Container.chat', index=0,
      number=1, type=11, cpp_type=10, label=1,
      default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='login', full_name='Container.login', index=1,
      number=2, type=11, cpp_type=10, label=1,
      default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='loginResponse', full_name='Container.loginResponse', index=2,
      number=3, type=11, cpp_type=10, label=1,
      default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='selectCity', full_name='Container.selectCity', index=3,
      number=4, type=11, cpp_type=10, label=1,
      default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='selectCityResponse', full_name='Container.selectCityResponse', index=4,
      number=5, type=11, cpp_type=10, label=1,
      default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='maps', full_name='Container.maps', index=5,
      number=6, type=11, cpp_type=10, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='serverState', full_name='Container.serverState', index=6,
      number=7, type=5, cpp_type=1, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='response', full_name='Container.response', index=7,
      number=8, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='gameState', full_name='Container.gameState', index=8,
      number=10, type=11, cpp_type=10, label=1,
      default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='requestServerState', full_name='Container.requestServerState', index=9,
      number=100, type=8, cpp_type=7, label=1,
      default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='requestMaps', full_name='Container.requestMaps', index=10,
      number=101, type=8, cpp_type=7, label=1,
      default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='mapRequest', full_name='Container.mapRequest', index=11,
      number=102, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='newCityRequest', full_name='Container.newCityRequest', index=12,
      number=103, type=11, cpp_type=10, label=1,
      default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='requestGameState', full_name='Container.requestGameState', index=13,
      number=104, type=5, cpp_type=1, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='requestUnfoundCity', full_name='Container.requestUnfoundCity', index=14,
      number=105, type=5, cpp_type=1, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='requestEnterCity', full_name='Container.requestEnterCity', index=15,
      number=106, type=5, cpp_type=1, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='requestExitCity', full_name='Container.requestExitCity', index=16,
      number=107, type=8, cpp_type=7, label=1,
      default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='newCityResponse', full_name='Container.newCityResponse', index=17,
      number=200, type=11, cpp_type=10, label=1,
      default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='gamestate', full_name='Container.gamestate', index=18,
      number=201, type=11, cpp_type=10, label=1,
      default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='mapSelectError', full_name='Container.mapSelectError', index=19,
      number=202, type=11, cpp_type=10, label=1,
      default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='newCity', full_name='Container.newCity', index=20,
      number=203, type=11, cpp_type=10, label=1,
      default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='updatedTiles', full_name='Container.updatedTiles', index=21,
      number=204, type=11, cpp_type=10, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='unfoundCity', full_name='Container.unfoundCity', index=22,
      number=205, type=5, cpp_type=1, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='enterCity', full_name='Container.enterCity', index=23,
      number=206, type=5, cpp_type=1, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='disconnect', full_name='Container.disconnect', index=24,
      number=300, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_CHAT = descriptor.Descriptor(
  name='Chat',
  full_name='Chat',
  filename='protocol.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='message', full_name='Chat.message', index=0,
      number=1, type=9, cpp_type=9, label=2,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='to', full_name='Chat.to', index=1,
      number=2, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sender', full_name='Chat.sender', index=2,
      number=3, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_LOGIN = descriptor.Descriptor(
  name='Login',
  full_name='Login',
  filename='protocol.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='Login.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='password', full_name='Login.password', index=1,
      number=2, type=9, cpp_type=9, label=2,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='regionPassword', full_name='Login.regionPassword', index=2,
      number=3, type=9, cpp_type=9, label=2,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_LOGINRESPONSE = descriptor.Descriptor(
  name='LoginResponse',
  full_name='LoginResponse',
  filename='protocol.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='type', full_name='LoginResponse.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='LoginResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='usertype', full_name='LoginResponse.usertype', index=2,
      number=3, type=14, cpp_type=8, label=2,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='username', full_name='LoginResponse.username', index=3,
      number=4, type=9, cpp_type=9, label=2,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
    _LOGINRESPONSE_TYPE,
    _LOGINRESPONSE_USERTYPE,
  ],
  options=None)


_SELECTCITY = descriptor.Descriptor(
  name='SelectCity',
  full_name='SelectCity',
  filename='protocol.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='cityID', full_name='SelectCity.cityID', index=0,
      number=1, type=5, cpp_type=1, label=2,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_SELECTCITYRESPONSE = descriptor.Descriptor(
  name='SelectCityResponse',
  full_name='SelectCityResponse',
  filename='protocol.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='type', full_name='SelectCityResponse.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
    _SELECTCITYRESPONSE_TYPE,
  ],
  options=None)


_MAP = descriptor.Descriptor(
  name='Map',
  full_name='Map',
  filename='protocol.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='Map.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='heightmap', full_name='Map.heightmap', index=1,
      number=2, type=9, cpp_type=9, label=2,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_GAMESTATE = descriptor.Descriptor(
  name='GameState',
  full_name='GameState',
  filename='protocol.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='GameState.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='heightmap', full_name='GameState.heightmap', index=1,
      number=2, type=9, cpp_type=9, label=2,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='tiles', full_name='GameState.tiles', index=2,
      number=3, type=11, cpp_type=10, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='cities', full_name='GameState.cities', index=3,
      number=4, type=11, cpp_type=10, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_TILE = descriptor.Descriptor(
  name='Tile',
  full_name='Tile',
  filename='protocol.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='Tile.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='positionx', full_name='Tile.positionx', index=1,
      number=2, type=5, cpp_type=1, label=2,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='positiony', full_name='Tile.positiony', index=2,
      number=3, type=5, cpp_type=1, label=2,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='cityid', full_name='Tile.cityid', index=3,
      number=4, type=5, cpp_type=1, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_NEWCITYREQUEST = descriptor.Descriptor(
  name='NewCityRequest',
  full_name='NewCityRequest',
  filename='protocol.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='NewCityRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='positionx', full_name='NewCityRequest.positionx', index=1,
      number=2, type=5, cpp_type=1, label=2,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='positiony', full_name='NewCityRequest.positiony', index=2,
      number=3, type=5, cpp_type=1, label=2,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='password', full_name='NewCityRequest.password', index=3,
      number=4, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_NEWCITYRESPONSE = descriptor.Descriptor(
  name='NewCityResponse',
  full_name='NewCityResponse',
  filename='protocol.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='type', full_name='NewCityResponse.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='NewCityResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
    _NEWCITYRESPONSE_TYPE,
  ],
  options=None)


_MAPSELECTERROR = descriptor.Descriptor(
  name='MapSelectError',
  full_name='MapSelectError',
  filename='protocol.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='message', full_name='MapSelectError.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_CITY = descriptor.Descriptor(
  name='City',
  full_name='City',
  filename='protocol.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='City.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='name', full_name='City.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='mayor', full_name='City.mayor', index=2,
      number=3, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='population', full_name='City.population', index=3,
      number=4, type=5, cpp_type=1, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='funds', full_name='City.funds', index=4,
      number=5, type=5, cpp_type=1, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_CONTAINER.fields_by_name['chat'].message_type = _CHAT
_CONTAINER.fields_by_name['login'].message_type = _LOGIN
_CONTAINER.fields_by_name['loginResponse'].message_type = _LOGINRESPONSE
_CONTAINER.fields_by_name['selectCity'].message_type = _SELECTCITY
_CONTAINER.fields_by_name['selectCityResponse'].message_type = _SELECTCITYRESPONSE
_CONTAINER.fields_by_name['maps'].message_type = _MAP
_CONTAINER.fields_by_name['gameState'].message_type = _GAMESTATE
_CONTAINER.fields_by_name['newCityRequest'].message_type = _NEWCITYREQUEST
_CONTAINER.fields_by_name['newCityResponse'].message_type = _NEWCITYRESPONSE
_CONTAINER.fields_by_name['gamestate'].message_type = _GAMESTATE
_CONTAINER.fields_by_name['mapSelectError'].message_type = _MAPSELECTERROR
_CONTAINER.fields_by_name['newCity'].message_type = _CITY
_CONTAINER.fields_by_name['updatedTiles'].message_type = _TILE
_LOGINRESPONSE.fields_by_name['type'].enum_type = _LOGINRESPONSE_TYPE
_LOGINRESPONSE.fields_by_name['usertype'].enum_type = _LOGINRESPONSE_USERTYPE
_SELECTCITYRESPONSE.fields_by_name['type'].enum_type = _SELECTCITYRESPONSE_TYPE
_GAMESTATE.fields_by_name['tiles'].message_type = _TILE
_GAMESTATE.fields_by_name['cities'].message_type = _CITY
_NEWCITYRESPONSE.fields_by_name['type'].enum_type = _NEWCITYRESPONSE_TYPE

class Container(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CONTAINER

class Chat(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CHAT

class Login(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LOGIN

class LoginResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LOGINRESPONSE

class SelectCity(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SELECTCITY

class SelectCityResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SELECTCITYRESPONSE

class Map(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MAP

class GameState(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GAMESTATE

class Tile(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TILE

class NewCityRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _NEWCITYREQUEST

class NewCityResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _NEWCITYRESPONSE

class MapSelectError(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MAPSELECTERROR

class City(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CITY


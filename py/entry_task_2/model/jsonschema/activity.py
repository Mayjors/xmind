import model.jsonschema.schema_defs as sd

LIST = {
	'type': 'object',
	'properties': {
		'channel': sd.STR64,
		'pageno': sd.UINT16_SCHEMA,
		'count': sd.UINT32_SCHEMA,
		'min_datetime': sd.UINT32_SCHEMA,
		'max_datetime': sd.UINT32_SCHEMA,
	}
}

ADD = {
	'type': 'object',
	'properties': {
		"name": sd.STR128,
		"channel": sd.STR128,
		"icon_url": sd.STR128,
		"begin_time": sd.UINT32_SCHEMA,
		"end_time": sd.UINT32_SCHEMA,
		"place": sd.STR128,
		"detail": sd.STR1024
	},
	"required": ["name", "channel", "begin_time", "end_time", "place", "detail"]
}

EDIT = {
	'type': 'object',
	'properties': {
		"id": sd.UINT64_SCHEMA,
		"name": sd.STR128,
		"channel": sd.STR128,
		"icon_url": sd.STR128,
		"begin_time": sd.UINT32_SCHEMA,
		"end_time": sd.UINT32_SCHEMA,
		"place": sd.STR128,
		"detail": sd.STR1024
	}
}

REMOVE = {
	'type': 'object',
	'properties': {
		'activity_id': sd.UINT64_SCHEMA,
		'name': sd.STR128
	},
	'required': ['activity_id']
}

DETAIL = {
	'type': 'object',
	'properties': {'activity_id': sd.UINT32_SCHEMA},
	'required': ['activity_id']
}

COMMENT_OR_ENTER_LIST = {
	'type': 'object',
	'properties': {
		'activity_id': sd.UINT32_SCHEMA,
		'pageno': sd.UINT16_SCHEMA,
		'count': sd.UINT32_SCHEMA
	},
	'required': ['activity_id']
}

COMMENT_ADD = {
	'type': 'object',
	'properties': {
		'activity_id': sd.UINT32_SCHEMA,
		'content': sd.STR1024
	},
	'required': ['activity_id', 'content']
}

ENTER_SAVE = {
	'type': 'object',
	'properties': {
		'activity_id': sd.UINT32_SCHEMA
	},
	'required': ['activity_id']
}

CHANNEL_REMOVE = {
	'type': 'object',
	'properties': {
		'channel_id': sd.UINT64_SCHEMA,
		'name': sd.STR128
	},
	'required': ['channel_id', 'name']
}

CHANNEL_ADD = {
	'type': 'object',
	'properties': {
		'name': sd.STR128,
	},
	'required': ['name']
}

CHANNEL_EDIT = {
	'type': 'object',
	'properties': {
		'channel_id': sd.UINT64_SCHEMA,
		'name': sd.STR128,
	},
	'required': ['channel_id', 'name']
}

CHANNEL_LIST = {
	'type': 'object',
	'properties': {
		'pageno': sd.UINT16_SCHEMA,
		'count': sd.UINT32_SCHEMA
	}
}

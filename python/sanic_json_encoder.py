
from sanic.response import json
from orjson import dumps as orjson_dumps
from functools import partial
json_dumps = partial(orjson_dumps)
from fastapi.encoders import jsonable_encoder
data = {"ll": chat_model, "kk": "ee", "pp": [chat_model], "lo": {"ll": chat_model, "kk": "ee", "pp": [chat_model, workflow]}}
print(data)
print(json(data, dumps=jsonable_encoder))

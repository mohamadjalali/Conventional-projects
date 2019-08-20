import redis
from collections.abc import MutableMapping
import json


r = redis.Redis()

restaurant_484272 = {
    "name": "Ravagh",
    "type": "Persian",
    "address": {
        "street": {
            "line1": "11 E 30th St",
            "line2": "APT 1",
        },
        "city": "Tehran",
        "state": "Shahre-Rey",
        "zip": 10016,
    }
}

result = {'city': 'Tehran', 'zip':10016,
          'street':{'line2': 'APT1', 'line1': '11E 30th St'},
          'state': 'Shahre-Rey'}


r.set(484272, json.dumps(restaurant_484272))

def setflat_skeys(
        r: redis.Redis,
        obj: dict,
        prefix: str,
        delim: str = ":",
        *,
        _autopfix=""
    ) -> None:
    print(_autopfix) 
    print()
    allowed_vtypes = (str, bytes, float, int)
    for key, value in obj.items():
        key = _autopfix + key
        if isinstance(value, allowed_vtypes):
            r.set("{}{}{}".format(prefix, delim, key), value)
        elif isinstance(value, MutableMapping):
            setflat_skeys(
                r, value, prefix, delim, _autopfix =\
                        "{}{}".format(key, delim)
            )
        else:
            raise TypeError("unsupported value type {}".\
                format(type(value)))

r.flushdb()
setflat_skeys(r, restaurant_484272, 484272)

for key in sorted(r.keys("484272*")): # Filter to this pattern
    print("{:35}{:15}".format(repr(key), repr(r.get(key))))


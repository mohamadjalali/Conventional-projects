import redis
from collections.abc import MutableMapping
import json


r = redis.Redis()

restaurant_484272 = {
    "name": "Godarz",
    "type": "Persian",
    "address": {
        "street": {
            "line1": "11 E 30th St",
            "line2": "APT 1",
        },
        "city": "Tehran",
        "state": "Rey City",
        "zip": 10016,
    }
}


def setflat_skeys(
        r: redis.Redis,  obj: dict,
        prefix: str,  delim: str = ":",
        *,  _autopfix=""
    ) -> None:
    
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


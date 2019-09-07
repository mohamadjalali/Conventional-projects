# New shell window or tab
import datetime
import ipaddress
import redis


r = redis.Redis(db=5)
for _ in range(20):
    r.lpush("ips", "104.174.118.18")

# Where we put all the bad egg IP addresses
blacklist = set()
MAXVISITS = 15

ipwatcher = redis.Redis(db=5)

while True:
    _, addr = ipwatcher.blpop("ips")
    addr = ipaddress.ip_address(addr.decode("utf-8"))
    now = datetime.datetime.utcnow()
    addrts = "{}:{}".format(addr, now.minute)
    n = ipwatcher.incrby(addrts, 1)
    if n >= MAXVISITS:
        print("Hat bot detected!:   {}".format(addr))
        blacklist.add(addr)
    else:
        print("{}:    saw {}".format(now, addr))
    _ = ipwatcher.expire(addrts, 60)


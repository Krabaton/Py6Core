from datetime import datetime, timedelta

d_war = datetime(year=2022, month=2, day=24, hour=5)
d_now = datetime.now()

diff = d_now.timestamp() - d_war.timestamp()

d_next = datetime.fromtimestamp(d_now.timestamp() + diff)
print(d_next)

interval = timedelta(days=180)
d_next2 = d_now + interval
print(d_next2)

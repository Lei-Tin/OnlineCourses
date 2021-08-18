from datetime import datetime
from pytz import timezone
import pytz

now = datetime.now()

print(now)

now = datetime.now(pytz.utc)

asian = 'Asia/Chongqing'

print(now.astimezone(timezone(asian)).strftime("%H:%M:%S"))

print(now.astimezone(timezone(asian)).strftime("%m/%d/%Y"))
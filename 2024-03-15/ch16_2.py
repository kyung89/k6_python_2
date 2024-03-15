import datetime
from datetime import datetime as dt

today = dt.strptime('2024-03-15', '%Y-%m-%d')
# today = dt.now()
print(today, type(today), type('2024-30-15'))

print(today + datetime.timedelta(days=3))


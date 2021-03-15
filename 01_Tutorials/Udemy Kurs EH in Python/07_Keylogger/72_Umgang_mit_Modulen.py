# Import Komplettes Modul (Hauptmodul)
import datetime
a = datetime.datetime.fromtimestamp(123213213)
b = datetime.date.fromtimestamp(123213213)

print(datetime.__dict__)

print(a.hour)
print(a.day)

# Import UnterModul
from datetime import date
date.fromtimestamp(123213213)

# Import UnterModul
from datetime import datetime
datetime.fromtimestamp(123213213)

from datetime import datetime as dt
dt.fromtimestamp(123213213)


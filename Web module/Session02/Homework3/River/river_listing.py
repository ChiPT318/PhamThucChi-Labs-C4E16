import mlab
from models.river import *

mlab.connect()
all_rivers = Rivers.objects()
for river in all_rivers:
    print(river["name"])

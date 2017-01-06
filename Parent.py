import gc
import sys
from types import ModuleType

def Parent():
    print("Hello am Parent")

left=[]
for o in gc.get_objects():
    if isinstance(o, ModuleType):
        left.append(o.__name__)

import Child

Child.Child()

right=[]
for o in gc.get_objects():
    if isinstance(o, ModuleType):
        right.append(o.__name__)

for i in set(right).difference(set(left)):
    print(i)


print "----------------------------------"

del Child
del sys.modules["Child"]
gc.collect()
c=sys.modules["GrandChild"]
del c
print sys.getrefcount(sys.modules["GrandChild"])

left=right
right=[]
for o in gc.get_objects():
    if isinstance(o, ModuleType):
        right.append(o.__name__)



for i in set(left).difference(set(right)):
    print(i)
import gc
import sys
import os
from types import ModuleType, FunctionType, DictType
from importlib import import_module

gc.set_debug(False)
print gc.isenabled()

def trace():
    l=gc.get_objects();
    d=gc.collect(2)
    r=gc.get_objects();
    # print len(l)
    # print len(r)
    la = [i.__name__ for i in l if type(i)==ModuleType]
    ra = [i.__name__ for i in r if type(i)==ModuleType]
    set(ra).difference(set(la))

def collect():
    m = gc.get_objects()
    d = {}
    d["total"]=0
    for i in m:
        d["total"]=d["total"]+1
        j = type(i)
        p = d.get(j)
        if p == None:
            d[j] = 1
        else:
            d[j] = p + 1
    return d.get(DictType)

def delta(d1, d2):
    print "------------------------------------"
    r={}
    d=set(d1.keys())&set(d2.keys())
    for i in d:
        delt=d2.get(i)-d1.get(i)
        if delt!=0:
            print "d1 : " + str(i) + " : " + str(d1.get(i))
            print "d2 : " + str(i) + " : " + str(d2.get(i))


def gxc():
    gc.collect(2)

def t():
    gxc()
    d1=collect()
    print(d1)
    test=import_module("Rule1.test")
    d2=collect()
    print(d2)
    return d2
    #del rule

def unloadModule(module, depth=1):
    if(depth == 0):
        return
    try:
        file=module.__file__
        if os.getcwd() not in file:
            return
    except AttributeError:
        return;
    depth=depth-1;
    list=dir(module)
    for i in list:
        h=getattr(module, i)
        unloadModule(h, depth)
    name=module.__name__
    h=[i for i in sys.modules if name in i]
    for i in h:
        del sys.modules[i]
        print ">>> " + i
    del module
    del sys.modules[name]
    print "Removed: " + name

gxc()
collect()
delta({},{})

d2=t()
unloadModule(sys.modules["Rule1.test"], depth=-1)
gxc()
d3=collect()
print(d3)
print os.getcwd()
print "End"



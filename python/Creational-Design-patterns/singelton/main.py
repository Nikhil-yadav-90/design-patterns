from simple_singelton import Singelton
from eager_singelton import EagerSingelton
from thread_safe_singelton import SingeltonThread


obj1 = Singelton()
obj2 = Singelton()

print(obj1 is obj2)



obj1 = SingeltonThread()
obj2 = SingeltonThread()

print(obj1 is obj2)

obj1 = EagerSingelton.get_instance()
obj2 = EagerSingelton.get_instance()

print(obj1 is obj2)

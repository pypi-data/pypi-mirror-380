from PyAcessModifier import *
from internal_test import *
from internal_otherfolder.internal_test2 import *
@AutoPrivateInit
class Test :
    class_private = Private(10)

    @public
    def show_private(self):
        return self.class_private


obj = Test()
print(obj.show_private())

obj2 = Test2()
obj3 = Test3()
obj3.test()
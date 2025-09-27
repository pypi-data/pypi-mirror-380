import inspect
import os
from functools import wraps

# -------------------
# HELPER
# -------------------
def _get_caller_info():
    frame = inspect.currentframe()
    outer = frame.f_back.f_back  # 데코레이터/Descriptor 호출 기준
    module = outer.f_globals.get("__name__")
    cls = outer.f_locals.get("self", None)
    return module, cls

def _get_caller_file():
    frame = inspect.currentframe().f_back.f_back
    return inspect.getfile(inspect.getmodule(frame))
# -------------------
# VARIABLE DESCRIPTORS
# -------------------
class Private:
    def __init__(self, value):
        self._value = value
        self._owner_class = None  # 클래스에서 세팅

    def __set_name__(self, owner, name):
        self._owner_class = owner

    def __get__(self, instance, owner):
        _, caller_cls = _get_caller_info()
        if caller_cls is not instance.__class__:
            raise PermissionError(f"Private variable cannot be accessed from outside class '{self._owner_class.__name__}'")
        return self._value

    def __set__(self, instance, value):
        _, caller_cls = _get_caller_info()
        if caller_cls is not instance.__class__:
            raise PermissionError(f"Private variable cannot be modified from outside class '{self._owner_class.__name__}'")
        self._value = value

class Protected:
    def __init__(self, value):
        self._value = value
        self._owner_class = None

    def __set_name__(self, owner, name):
        self._owner_class = owner

    def __get__(self, instance, owner):
        _, caller_cls = _get_caller_info()
        if caller_cls is None or not issubclass(caller_cls.__class__, self._owner_class):
            raise PermissionError(f"Protected variable cannot be accessed from outside class '{self._owner_class.__name__}' or subclasses")
        return self._value

    def __set__(self, instance, value):
        _, caller_cls = _get_caller_info()
        if caller_cls is None or not issubclass(caller_cls.__class__, self._owner_class):
            raise PermissionError(f"Protected variable cannot be modified from outside class '{self._owner_class.__name__}' or subclasses")
        self._value = value

class Internal:
    def __init__(self, value):
        self._value = value
        self._owner_file = None

    def __set_name__(self, owner, name):
        self._owner_file = inspect.getfile(owner)

    def __get__(self, instance, owner):
        caller_file = inspect.getfile(inspect.getmodule(inspect.currentframe().f_back))
        if os.path.dirname(caller_file) != os.path.dirname(self._owner_file):
            raise PermissionError(f"Internal variable cannot be accessed from outside folder")
        return self._value

    def __set__(self, instance, value):
        caller_file = inspect.getfile(inspect.getmodule(inspect.currentframe().f_back))
        if os.path.dirname(caller_file) != os.path.dirname(self._owner_file):
            raise PermissionError(f"Internal variable cannot be modified from outside folder")
        self._value = value

class Public:
    def __init__(self, value):
        self._value = value

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        self._value = value

# -------------------
# FUNCTION DECORATORS
# -------------------
def private(obj):
    if inspect.isclass(obj):
        # 클래스 자체에 적용
        orig_init = obj.__init__

        @wraps(orig_init)
        def new_init(self, *args, **kwargs):
            _, caller_instance = _get_caller_info()
            if caller_instance is not obj:
                raise PermissionError(f"Private class '{obj.__name__}' cannot be accessed from outside class")
            return orig_init(self, *args, **kwargs)

        obj.__init__ = new_init
        return obj
    else:
        # 인스턴스 메서드 전용
        @wraps(obj)
        def wrapper(self, *args, **kwargs):
            _, caller_instance = _get_caller_info()
            if caller_instance is not self.__class__:
                raise PermissionError(f"Private method '{obj.__name__}' cannot be accessed from outside class")
            return obj(self, *args, **kwargs)
        return wrapper

def protected(obj):
    if inspect.isclass(obj):
        # 클래스 전체에 붙였을 때
        orig_init = obj.__init__

        @wraps(orig_init)
        def new_init(self, *args, **kwargs):
            _, caller_instance = _get_caller_info()
            if caller_instance is None or not isinstance(caller_instance, obj):
                raise PermissionError(f"Protected class '{obj.__name__}' cannot be accessed from outside class or subclasses")
            return orig_init(self, *args, **kwargs)

        obj.__init__ = new_init
        return obj
    else:
        # 기존 인스턴스 메서드 보호
        @wraps(obj)
        def wrapper(self, *args, **kwargs):
            _, caller_instance = _get_caller_info()
            if caller_instance is None or not isinstance(caller_instance, self.__class__):
                raise PermissionError(f"Protected method '{obj.__name__}' cannot be accessed from outside class or subclasses")
            return obj(self, *args, **kwargs)
        return wrapper


def internal(obj):
    # 함수일 때
    if inspect.isfunction(obj):
        @wraps(obj)
        def wrapper(*args, **kwargs):
            caller_file = inspect.getfile(inspect.getmodule(inspect.currentframe().f_back))
            func_file = inspect.getfile(inspect.getmodule(obj))
            if os.path.dirname(caller_file) != os.path.dirname(func_file):
                raise PermissionError(f"Internal function '{obj.__name__}' cannot be accessed from outside folder")
            return obj(*args, **kwargs)
        return wrapper

    # 클래스일 때
    elif inspect.isclass(obj):
        obj.__access__ = "internal"

        # 생성자 호출 감싸기 → 다른 폴더에서 인스턴스 생성 못 하게 막음
        orig_init = obj.__init__

        def __init__(self, *args, **kwargs):
            caller_file = inspect.getfile(inspect.getmodule(inspect.currentframe().f_back))
            class_file = inspect.getfile(obj)
            if os.path.dirname(caller_file) != os.path.dirname(class_file):
                raise PermissionError(f"Internal class '{obj.__name__}' cannot be instantiated from outside folder")
            orig_init(self, *args, **kwargs)

        obj.__init__ = __init__
        return obj

    # 그 외 (안 쓰는 경우)
    else:
        return obj


def public(func):
    return func


class PrivateInit:
    def __init__(self, func):
        self.func = func
        wraps(func)(self)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        # 인스턴스 생성 시 자동 실행
        self.func(instance)
        return lambda *args, **kwargs: self.func(instance, *args, **kwargs)


def privateinit(func):
    return PrivateInit(func)
# -------------------
# EXAMPLE USAGE
# -------------------
if __name__ == '__main__':
    class MyClass:
        my_private = Private(42)
        my_protected = Protected(10)
        my_internal = Internal(99)
        my_public = Public(123)

        @private
        def secret_method(self):
            print("Private Method:", self.my_private)

        @protected
        def prot_method(self):
            print("Protected Method:", self.my_protected)

        @internal
        def internal_method(self):
            print("Internal Method:", self.my_internal)

        @public
        def pub_method(self):
            print("Public Method:", self.my_public)


    class Child(MyClass):
        def access_protected(self):
            print("Access Protected:", self.my_protected)
            self.prot_method()

import inspect
from functools import wraps
import os
import sys

# -------------------
# HELPER
# -------------------
def _get_caller_instance():
    frame = inspect.currentframe().f_back.f_back
    return frame.f_locals.get("self", None)

def _get_main_path():
    if "__main__" in sys.modules:
        return os.path.dirname(sys.modules["__main__"].__file__)
    return None

# -------------------
# PRIVATE DESCRIPTOR
# -------------------

class Private:
    def __init__(self, value):
        self._value = value
        self._owner_class = None

    def __set_name__(self, owner, name):
        self._owner_class = owner
        self._name = name

    def __get__(self, instance, owner):
        # instance가 없으면 클래스 단 접근 → 막기
        if instance is None:
            raise PermissionError(
                f"Private class variable '{self._name}' cannot be accessed directly"
            )

        # 호출자 검사
        caller_self = inspect.currentframe().f_back.f_locals.get('self', None)
        if caller_self is not instance:
            # 외부에서 인스턴스를 통해 접근하면 막기
            raise PermissionError(
                f"Private variable '{self._name}' cannot be accessed from outside instance methods"
            )

        return instance.__dict__.get(self._name, self._value)

    def __set__(self, instance, value):
        caller_self = inspect.currentframe().f_back.f_locals.get('self', None)
        if caller_self is not instance:
            raise PermissionError(
                f"Private variable '{self._name}' cannot be modified from outside instance methods"
            )
        instance.__dict__[self._name] = value

# -------------------
# PROTECTED / INTERNAL / PUBLIC DESCRIPTORS
# -------------------
class Protected:
    def __init__(self, value):
        self._value = value
        self._owner_class = None
        self._name = None

    def __set_name__(self, owner, name):
        self._owner_class = owner
        self._name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        caller = _get_caller_instance()
        if caller is not None and isinstance(caller, self._owner_class):
            return instance.__dict__.get(self._name, self._value)
        raise PermissionError(
            f"Protected variable '{self._name}' cannot be accessed from outside class '{self._owner_class.__name__}' or subclasses"
        )

    def __set__(self, instance, value):
        caller = _get_caller_instance()
        if caller is not None and isinstance(caller, self._owner_class):
            instance.__dict__[self._name] = value
        else:
            raise PermissionError(
                f"Protected variable '{self._name}' cannot be modified from outside class '{self._owner_class.__name__}' or subclasses"
            )

class Internal:
    def __init__(self, value):
        self._value = value
        self._owner_class = None
        self._name = None
        self._folder_path = None

    def __set_name__(self, owner, name):
        self._owner_class = owner
        self._name = name
        self._folder_path = os.path.dirname(sys.modules[owner.__module__].__file__)

    def __get__(self, instance, owner):
        main_path = _get_main_path()
        if main_path != self._folder_path:
            raise PermissionError(
                f"Internal variable '{self._name}' cannot be accessed from outside folder"
            )
        if instance is None:
            return self
        return instance.__dict__.get(self._name, self._value)

    def __set__(self, instance, value):
        main_path = _get_main_path()
        if main_path != self._folder_path:
            raise PermissionError(
                f"Internal variable '{self._name}' cannot be modified from outside folder"
            )
        instance.__dict__[self._name] = value

class Public:
    def __init__(self, value):
        self._value = value
        self._name = None

    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self._name, self._value)

    def __set__(self, instance, value):
        instance.__dict__[self._name] = value


# -------------------
# METHOD DECORATORS
# -------------------

def private(obj):
    if inspect.isclass(obj):
        orig_init = obj.__init__
        @wraps(orig_init)
        def new_init(self, *args, **kwargs):
            caller = _get_caller_instance()
            if caller is None or type(caller) is not obj:
                raise PermissionError(f"Private class '{obj.__name__}' cannot be accessed from outside class")
            return orig_init(self, *args, **kwargs)
        obj.__init__ = new_init
        return obj
    else:
        # 메서드 프라이빗은 기존 로직 그대로
        @wraps(obj)
        def wrapper(self, *args, **kwargs):
            caller_self = inspect.currentframe().f_back.f_locals.get('self', None)
            if caller_self is not self and caller_self is not None and type(caller_self) is not type(self):
                raise PermissionError(f"Private method '{obj.__name__}' cannot be accessed from outside class")
            return obj(self, *args, **kwargs)
        return wrapper

def protected(obj):
    if inspect.isclass(obj):
        orig_init = obj.__init__
        @wraps(orig_init)
        def new_init(self, *args, **kwargs):
            caller = _get_caller_instance()
            if caller is None or not isinstance(caller, obj):
                raise PermissionError(f"Protected class '{obj.__name__}' cannot be accessed from outside class or subclasses")
            return orig_init(self, *args, **kwargs)
        obj.__init__ = new_init
        return obj
    else:
        @wraps(obj)
        def wrapper(self, *args, **kwargs):
            caller = _get_caller_instance()
            if caller is not None and isinstance(caller, type(self)):
                return obj(self, *args, **kwargs)
            raise PermissionError(f"Protected method '{obj.__name__}' cannot be accessed from outside class or subclasses")
        return wrapper

def internal(obj):
    """
    Internal decorator for both methods and classes.
    - For methods: restrict call to same folder/module.
    - For classes: restrict instantiation to same folder/module.
    """
    if inspect.isclass(obj):
        # ----------------------
        # Class-level Internal
        # ----------------------
        cls = obj
        orig_init = cls.__init__

        @wraps(orig_init)
        def new_init(self, *args, **kwargs):
            # 호출한 파일 경로
            frame = inspect.currentframe()
            try:
                caller_frame = frame.f_back
                mod = inspect.getmodule(caller_frame)
                caller_dir = None
                if mod is not None and hasattr(mod, "__file__"):
                    caller_dir = os.path.dirname(os.path.abspath(mod.__file__))

                # 클래스 정의 파일 경로
                class_file = os.path.abspath(sys.modules[cls.__module__].__file__)
                class_dir = os.path.dirname(class_file)

                if caller_dir != class_dir:
                    raise PermissionError(
                        f"Cannot instantiate class '{cls.__name__}' from outside its folder"
                    )
            finally:
                del frame

            orig_init(self, *args, **kwargs)

        cls.__init__ = new_init
        return cls

    else:
        # ----------------------
        # Method-level Internal
        # ----------------------
        func = obj

        @wraps(func)
        def wrapper(self, *args, **kwargs):
            frame = inspect.currentframe()
            try:
                caller_frame = frame.f_back
                mod = inspect.getmodule(caller_frame)
                caller_dir = None
                if mod is not None and hasattr(mod, "__file__"):
                    caller_dir = os.path.dirname(os.path.abspath(mod.__file__))

                # 메서드 정의 파일 경로
                method_file = os.path.abspath(sys.modules[type(self).__module__].__file__)
                method_dir = os.path.dirname(method_file)

                if caller_dir != method_dir:
                    raise PermissionError(
                        f"Cannot call method '{func.__name__}' from outside its folder"
                    )
            finally:
                del frame

            return func(self, *args, **kwargs)

        return wrapper

def public(func):
    return func

# -------------------
# PRIVATEINIT
# -------------------
def privateinit(func):
    func._is_privateinit = True
    return func

def AutoPrivateInit(cls):
    orig_init = cls.__init__

    @wraps(orig_init)
    def new_init(self, *args, **kwargs):
        # __init__ 원래 실행
        orig_init(self, *args, **kwargs)

        # @privateinit 자동 실행
        for attr_name in dir(self):
            attr = getattr(self, attr_name)
            if callable(attr) and getattr(attr, "_is_privateinit", False):
                attr()

        # 클래스 단 Private 변수 __set_name__ 처리
        for k, v in cls.__dict__.items():
            if hasattr(v, "_owner_class") and v._owner_class is None:
                v.__set_name__(cls, k)

        # 초기화 완료 표시 (Private __setattr__ 검사용)
        setattr(self, "_init_done", True)

    # 인스턴스 setattr 후킹: 외부에서 Private 객체 덮어쓰기 금지
    orig_setattr = cls.__setattr__

    def new_setattr(self, name, value):
        # 클래스에 정의된 Private 객체를 덮어쓰려 하면 PermissionError
        attr = getattr(type(self), name, None)
        if isinstance(attr, Private):
            raise PermissionError(f"Cannot overwrite Private variable '{name}'")
        # 인스턴스 단 Private도 초기화 완료 후 덮어쓰기 금지
        if hasattr(self, name) and isinstance(getattr(self, name), Private):
            raise PermissionError(f"Cannot overwrite Private variable '{name}'")
        object.__setattr__(self, name, value)

    cls.__init__ = new_init
    cls.__setattr__ = new_setattr
    return cls

API = AutoPrivateInit

from PyAccessModifier import constant, Constant

class MyClass:
    @constant
    def my_method(self):
        return 42

    my_const = Constant(10)

# 테스트
obj = MyClass()

# 호출은 정상
print(obj.my_method())   # 42
print(obj.my_const)      # 10

# 재정의 시도
try:
    obj.my_method = lambda: 99  # 재할당 시도
except PermissionError as e:
    print("Cannot override method:", e)

try:
    MyClass.my_const = 20  # 클래스 상수 재할당 시도
except PermissionError as e:
    print("Cannot override constant:", e)

from PyAcessModifier import Private, privateinit, API

@API
class MyClass:
    @privateinit
    def init_private(self):
        self.Secret = Private(123)  # 인스턴스 단 Private

    # 게터 구현
    @property
    def secret(self):
        # Private 객체에서 바로 값 꺼내기
        return self.Secret.__get__(self, type(self))

    @secret.setter
    def secret(self, value):
        # Private 객체에 값 설정
        self.Secret.__set__(self, value)


if __name__ == "__main__":
    obj = MyClass()
    print("게터로 접근:", obj.secret)   # 123

    obj.secret = 999
    # obj.Secret = 999
    print("값 변경 후:", obj.secret)    # 999

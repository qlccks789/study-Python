class Member:
    abc = "aaa"

    # 생성자  : __init__  (객체 생성시 호출됨)
    def __init__(self, name="장보고", age=0, email="jang@a.com"):
        print("생성자 호출")
        self.name = name
        self.age = age
        self.email = email

    def print_info(self):
        print("name", self.name)
        print("age", self.age)
        print("email", self.email)


def process():
    m = Member()
    m.print_info()

    m = Member("홍길동", 22, "hong@hong.com")
    m.print_info()


process()

# TypeError: print_info() missing 1 required positional argument: 'self'
# 에러발생함
# Member.print_info()
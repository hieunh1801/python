"""
    - Bản chât của decorator
    - Decorator không tham số
"""


def my_decorator(func):
    def wrapper():
        print("do something before call function")
        func()
        print("do something after call function")
    return wrapper


# Sử dụng thuần túy
def say_hello():
    print("Hello: Hieu")


say_hello = my_decorator(say_hello)
say_hello()

print("--------------------------------")
# Tuong duong
@my_decorator
def say_goodbye():
    print("Good by: Hieu")


say_goodbye()

import functools


def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Do something before call function")
        func(*args, **kwargs)
        print("Do something after call function")
    return wrapper


@my_decorator
def say_hello(name: str):
    print("Hello: ", name)


say_hello("Nguyeen Huu Hieu")

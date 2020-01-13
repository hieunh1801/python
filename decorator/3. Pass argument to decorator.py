import functools


def required_privilege(privilege: str):
    def my_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("Do something before check role. Your privlege is: ", privilege)
            return func()
        return wrapper
    return my_decorator


@required_privilege(privilege="sysem_admin")
def api_get(name="Nguyen Huu Hieu"):
    print("Danh sach hoc vien", name)


api_get()

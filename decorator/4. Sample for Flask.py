import functools


def get_user_info():
    return {"user_id": 1}


def get_resource_privilege(sytem_resource_name: str = None, user_id: int = None):
    if sytem_resource_name == "system_admin":
        return {"resource_id": 1, "user_id": 1, "privilege": 1}
    return None


def required_privilege(privilege: str):
    def check_privilege_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            user_info = get_user_info()
            user_id = user_info.get("user_id")
            privilege_info = get_resource_privilege(sytem_resource_name=privilege,
                                                    user_id=user_id)
            # Denine
            if privilege_info in (None, [], {}):
                print("privilege is denined")
                print("call abort function")
                return "abort"
            # Pass and call funct
            else:
                print("privilege is access - func is called")
                return func(*args, **kwargs)
        return wrapper
    return check_privilege_decorator


@required_privilege(privilege="system_admin")
def api_get():
    print("Get all student")
    print("API GET IS CALLED")


api_get()

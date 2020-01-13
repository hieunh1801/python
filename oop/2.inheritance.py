class Parent:
    def __init__(self):
        print("parent constructor")

    def parent_method(self):
        print("This is parent method")


class Mother:
    def __init__(self):
        print("mother constructor")

    def mother_method(self):
        print("This is mother method")


class Child1(Parent, Mother):
    def __init__(self):
        super().__init__()


chi1 = Child1()

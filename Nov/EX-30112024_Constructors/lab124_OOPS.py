a = 10


class person:
    b = 11  # Instance - Belong to class

    def __init__(self):
        self.c = None

    def print_info(self):
        c = 20  # local variable
        print(c)
        print(self.b)
        global a
        print(a)


object_ref = person()
object_ref.print_info()

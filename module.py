class Module(object):
    """docstring for Mol."""

    def __init__(self,):
        super(Module, self).__init__()
        self.name = ""
        self.age = 0

    def change_name(self, name):
        self.name = name

    def change_age(self, age):
        self.age = age

    def show_name(self):
        print(self.name)

    def show_age(self):
        print(self.age)

name = "Ramasamy"
reverse = name[::-1]
print(reverse,end="")


list_a = ["apple", "orange", 2, "mango"]
list_a.pop()
print(list_a)

class Phone:
    name = "ram"
    def __init__(self, var_name):
        self.Vname = var_name # 1. Store the passed value in an instance attribute 'self.name'

    def display_name(self):
        return self.name # 2. Access the stored instance attribute 'self.name'

obj_class = Phone("ram")
print(obj_class.display_name())

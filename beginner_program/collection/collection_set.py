a = {1,2,3,3,4,4,5,5,6}
print(a) # will display only non duplicates set values

a.add(10)
print(a)
a.pop()
print(a)
a.remove(4)
print(a)
a.remove(3)
print(a)
a.pop()
print(a)


fruit = {"apple", "orange"}
more_fruits = ["apple", "mango"]
even_fruits = ("banana", "cherry")
fruit.update(more_fruits)
fruit.update(even_fruits)
print(fruit)
# update() merge sets and other collection as well
# set support add(), update(), remove(), pop()s

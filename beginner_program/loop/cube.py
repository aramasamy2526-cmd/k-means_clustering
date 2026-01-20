#cube of the input 5 numbers

num = []
cube_array = []
for i in range(5):
    a = int(input("enter the " +str(i+1)+ "st value"))
    num.append(a)
    cube = (a*a*a)
    cube_array.append(cube)
print(cube_array)

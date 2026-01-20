a = input("enter any number")
b = input("enter any number")
average = (int(a)+int(b))/2
print (average)

#using list to find aveage
list = [2, 4, 6, 8, 10]
average = sum(list) / len(list)
print("The average of the list is:", average)


#using numpy module used to find a average(mean)
import numpy as np

list = [2, 4, 6, 6, 8, 10]
mean = np.mean(list)
print("The mean of the list is:", mean)
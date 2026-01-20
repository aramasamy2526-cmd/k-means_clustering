a = [1,2,3,4,5,6]
a.pop() # pop() will remove the last element present in the list
print(a)

a.pop(0) # pop(index) will remove the mentioned index value
print(a)

a.append(10) # will insert the new element at last position in list
print(a)

a.insert(2,90) # insert(index, inserting value) will insert the element in mentioned indext value
print(a)

a[5]=80 # ) will insert the element in mentioned indext value a[index] = assignemt value
print(a)


# merging two list

i = [2,5,7,"i", "emc", "k"]
j = [3,7]
k = ["Study", "well"]
i.extend(j)
i.extend(k)
print(i)


#list support inser(), pop(), append(), extend()

# a = 4
# for i in range(a):
#     print(i)
# print("the value of i is ", i)

# a = "ramasamy"
# reverse =""
# print(reverse)
# for i in a:
#     print(i)
#     reverse = i+ reverse
# print(reverse)




list_check = ['4','3','3','3','6']

new_list = []
for i in list_check:
    print(i)
    if i == '3':
        print("pop value 3")
    else:
        print("for loop execute...")
        new_list.append(i)

list_check = new_list
print(list_check)


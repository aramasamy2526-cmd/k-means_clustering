reverse = "Python"
reverse_string = reverse[::-1]
print(reverse_string)

#Using for loop
string = str(input("enter the string to be reversed"))
reverse = ""
for i in string:
    reverse = i + reverse
print (reverse)

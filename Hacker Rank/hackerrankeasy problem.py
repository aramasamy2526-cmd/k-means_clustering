a = [10,20,40,50]
for i, num in enumerate(a):
    if i ==0:
        continue
    if i ==3:
        previous_elements = a[:::-i]
        print(previous_elements)

if __name__ == '__main__':
    n = int(input("enter the number element you want to mention inside the list:"))
    
    arr = []
    for i in range(n):
        print("enter",n,"element:")
        a = int(input())
        arr.append(a)


# Convert to set to remove duplicates
unique_scores = set(arr)

# Remove the maximum score
unique_scores.remove(max(unique_scores))

# Now print the next maximum (runner-up)
print("Runner-up score:", max(unique_scores))

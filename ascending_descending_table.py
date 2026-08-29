num = int(input("Enter the number which table you want to print "))
choice = int(input("Do you want to print table ascending or descending order\nPress 0 for Desceding\nPress 1 for ascending"))

print("your choice is", choice)

if choice:
    i =1
    while i<=10:
        print(f"{num} * {i} = {(num*i)}")
        i+=1
else:
    i = 10
    while i>=1:
        print(f"{num} * {i} = {(num*i)}")
        i-=1
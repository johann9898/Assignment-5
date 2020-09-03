n = int(input("Enter the length of the sequence: ")) # Do not change this line

n1 = 1
n2 = 2
n3 = 3

print(n1)
print(n2)
print(n3)
for i in range(0,n-3):
    sum_all = n1 + n2 + n3
    n1 = n2
    n2 = n3
    n3 = sum_all
        
        
    print(sum_all)

    
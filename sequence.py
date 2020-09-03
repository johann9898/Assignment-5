n = int(input("Enter the length of the sequence: ")) # Do not change this line

n1 = 0
n2 = 0
n3 = 1
for i in range(0,n):
    if n3 < 2:
        sum_all = n1 + n2 + n3
        n2 = n3
        n3 = sum_all  
    else:
        sum_all = n1 + n2 + n3
        n1 = n2
        n2 = n3
        n3 = sum_all
        
    print(sum_all)
    


a = list()
for i in range(1,100):
    flag = 0
    for j in range(2,i):
        if (i % j == 0):
            flag = 1
    if (flag == 0):
        a.append(i)
print(a)
            
        

    

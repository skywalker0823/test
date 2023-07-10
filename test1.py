

def adder(n):
    total = 0
    for i in range(1,n+1):
        if i==1:
            total+=1
        elif i%2!=0:
            total+=i*-1
        else:
            total+=i
    return total

print(adder(10))






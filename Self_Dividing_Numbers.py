a=int(input())
b=int(input())
for i in range(a,b+1):
    q=i
    while i!=0:
        r=i%10
        i=i//10
        if r==0:
            break
        if q%r!=0:
            break
    else:
        print(q,end=" ")
            
n=int(input())
l=[]
while n>0:
    r=n%10
    n=n//10
    l.append(r)
    if(l.count(r)!=1):
        print('Not Unique Number')
        break
else:
    print('Unique Number')
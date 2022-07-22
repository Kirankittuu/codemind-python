x=int(input())
l=[]
while x>0:
    r=x%10
    x=x//10
    l.append(r)
    if(l.count(r)!=1):
        print('Not Unique Number')
        break
else:
    print('Unique Number')
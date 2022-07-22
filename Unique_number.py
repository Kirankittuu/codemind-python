n=list(str(input()))
l=[]
for i in n:
    if i not in l:
        l.append(i)
    else:
        break
if l!=n:
    print('Not Unique Number')
else:
    print('Unique Number')
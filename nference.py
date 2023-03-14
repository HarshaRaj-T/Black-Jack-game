a=[13,92,6,162,71,4,21,36,660,6,99]
c=0
for i in range(1,len(a)-1):
    if 10<=a[i-1]<=99 and 10<=a[i]<=99:
        if a[i]>=55 or a[i-1]>=55:
            c+=1
            continue
    if a[i]>=55 and not 10<=a[i-1]<=99 and not 10<=a[i+1]<=99:
        c+=1
print(c)
c=0
for i in range(len(a)):
    if 55<=a[i-1]<=99:
        c+=1
print(c)

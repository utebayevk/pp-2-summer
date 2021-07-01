a = [i for i in input().split()]
x=''
for i in range(len(a)):
    if i%2==0:
        x +=a[i]+" "
print(x)
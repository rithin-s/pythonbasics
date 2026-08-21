n = 7
flag = False
for i in range(2,n) :
    if n % i == 0 :
        flag = True
if flag:
    print("not prime")
else:
    print("prime")



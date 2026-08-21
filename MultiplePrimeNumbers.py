
def loopfunction():
    global flag
    flag = False
    for i in range(2, 10):
        if n % i == 0:
            flag = True
flag = False
for j in range (2,10):
    loopfunction()
if flag:
    print("not prime")
else:
     print("prime")

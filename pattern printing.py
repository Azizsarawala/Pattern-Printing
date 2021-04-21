print("how many lines of star you want")
a = int(input())
print("enter 1 to get stars in incresing mannar ,"
      "or enter 0 to get stars in decresing mannar")

b = int(input())
i=0
while(True):
    if i==a+1:
        break
    elif a == 0:
        break
    elif b==1:
        print("*"*i,end="")
        print("\n",end="")
        i=i+1
        continue
    else:
        b == 0
        print("*" * a, end="")
        print("\n", end="")
        a = a - 1
        continue

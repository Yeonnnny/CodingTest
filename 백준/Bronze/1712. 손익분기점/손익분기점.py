fixed,variable,price = map(int,input().split())


if variable >= price:
    print(-1)
else:
    num = (fixed//(price-variable))+1
    print(num)

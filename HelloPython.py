print("Hello Python")
# n  = int(input("Enter first value"))
# x = int(input("Enter second value"))
# print(n)
# print(x)
# answer = n+x
# print('Sum is: ', answer)

for i in range(1,11):
    print(i)

def factorialFun(n):
    if(n==1):
        return 1
    else:
        return n* factorialFun(n-1)

ans = factorialFun(4)
print(ans)
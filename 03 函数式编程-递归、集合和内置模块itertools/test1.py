
def factorial(x):
    if x == 1:  #第二个条件：结束递归的条件；
        return 1
    else:
        return x * factorial(x - 1) #第一个条件：调用自身的方法；
print(factorial(5)) #5的阶乘
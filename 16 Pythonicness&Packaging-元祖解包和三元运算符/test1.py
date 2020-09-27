#元组解包允许你将一个可迭代的元素（通常是一个元组）分配给变量。列表其实也可以的；
numbers = (1, 2, 3)
a, b, c = numbers
print(a)
print(b)
print(c)
#交换值的方式也可以这样；
m = 11
n = 22
m,n = n,m
print(m)
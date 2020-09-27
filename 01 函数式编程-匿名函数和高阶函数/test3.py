#函数名 = lambda[参数列表]:表达式
def my_func(f, arg):
  return f(arg) #f(5) x=5
print(my_func(lambda x: 2*x*x, 5))
#这个带有参数的；
g = lambda y:2*y
print(g(3))
#这个不带参数的写法；
gg = lambda :123
print(gg())
#可以有N个参数；
ggg = lambda x,y,z:x+y+z
print(ggg(1,2,3))
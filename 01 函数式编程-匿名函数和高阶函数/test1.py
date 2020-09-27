#函数式编程是基于函数
def apply_twice(func, arg):
   return func(func(arg)) #add_five(add_five(10)) add_five(15)

def add_five(x):
   return x + 5
print(apply_twice(add_five, 10))
#还记得之前我们讲过，可变函数；
def fun():
    print('hello')
name = fun #之前讲过的可变函数，道理是一样的，但不能加单双引号
name()
#纯函数：每次给固定的值都是返回相同的值；
def pure_function(x, y):
  temp = x + 2*y
  return temp / (2*x + y)
print(pure_function(2,6))
print(pure_function(2,6))
#非纯函数，每次给固定的值，但是返回的结果是不一样的；
some_list = []
def impure(arg):
  some_list.append(arg)
impure(123)
impure(123)
print(some_list)
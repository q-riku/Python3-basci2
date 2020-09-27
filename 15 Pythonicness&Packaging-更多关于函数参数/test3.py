"""
    **kwargs（代表关键字参数）允许你处理尚未预先定义的命名参数。
    关键字参数返回一个字典，其中键是参数名称，值是参数数值。一定要有键值；
"""
def my_func(x, y=7, *args, **kwargs):
   print(kwargs)
   print(x)
   print(y)
   print(args)

my_func(2, 3, 4, 5, 6, 7,8,aa=100)
"""
Python 允许具有不同数量的参数的函数。
使用 *args 作为函数参数，可以将任意数量的参数传递给该函数。
参数可以作为函数主体中的元组参数访问。
注意事项：
*args必须放在最后面； 实参和形参都要一一对应
"""
def function(named_arg, *args):
   print(named_arg)
   print(args)

function(1, 2, 3, 4, 5)
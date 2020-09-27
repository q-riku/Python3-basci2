"""
map接受一个函数和一个迭代器作为参数，并返回一个新的迭代器，该函数应用于每个参数；
语法：列表名 = map(一个函数，一个可迭代序列)
"""
def add_five(x):
  return x + 5
nums = [11, 22, 33, 44, 55]
#对列表中的每个值都加5
result = list(map(add_five, nums))
print(result)
#用lambda表达式也可以达到效果；
nums = [11, 22, 33, 44, 55]
result = list(map(lambda x: x+5, nums))
print(result)
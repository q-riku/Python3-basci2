"""
filter函数通过删除与谓词不匹配的项来过滤一个迭代；
语法：列表名 = filter(一个函数，一个可迭代序列)
集合：列表、字典、元组
"""
nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x%2==0, nums))
print(res)
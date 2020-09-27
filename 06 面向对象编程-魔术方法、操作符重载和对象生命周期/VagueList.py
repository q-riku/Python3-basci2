"""
几个神奇的方法使类像容器一样行事：
__len__ 对应 len()
__getitem__ 对应 获取索引
__setitem__ 对应 分配索引值
__delitem__ 对应 删除索引值
__iter__ 对应 迭代对象（例如for循环）
__contains__ 对应 in
"""
import random
class VagueList:
  def __init__(self, cont):
    self.cont = cont
  def __getitem__(self, index):
    return self.cont[index + random.randint(-1, 1)]
  def __len__(self):
    return random.randint(0, len(self.cont)*2)
vague_list = VagueList(["A", "B", "C", "D", "E"])
print(len(vague_list)) #10 都是随机产生; 自动调用__len__()方法；
print(len(vague_list)) #7
print(vague_list[2]) #C 自动调用__getitem__魔术方法
print(vague_list[2]) #D 
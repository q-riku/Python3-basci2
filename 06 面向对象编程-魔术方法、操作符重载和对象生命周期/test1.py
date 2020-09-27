"""
比较运算符的魔术方法：
__lt__ 对应 <
__le__ 对应 <=
__eq__ 对应 ==
__ne__ 对应 !=
__gt__ 对应 >
__ge__ 对应 >=
"""
class SpecialString:
  def __init__(self, cont):
    self.cont = cont
  def __gt__(self, other):
    for index in range(len(other.cont)+1):
      result = other.cont[:index] + ">" + self.cont
      print(result)
      result += ">" + other.cont[index:]
      print(result)
      # print(result)
  def __ge__(self, other):
    print(str(self.cont+other.cont))
spam = SpecialString("spam")
eggs = SpecialString("eggs")
# spam > eggs
spam >= eggs
"""
    >spam>eggs
    e>spam>ggs
    eg>spam>gs
    egg>spam>s
    eggs>spam>
"""
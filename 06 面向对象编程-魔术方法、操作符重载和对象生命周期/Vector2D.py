"""
常见的魔术方法：对象【相加】时 __函数名__
__sub__对应 -
__mul__对应 *
__truediv__对应 /
__floordiv__对应 //
__mod__对应 %
__pow__对应 **
__and__对应 +
__xor__对应 ^
__or__对应 |
"""
class Vector2D:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def __add__(self, other):
    return Vector2D(self.x + other.x, self.y + other.y)
first = Vector2D(5, 7)
second = Vector2D(3, 9)
result = first + second #此时会自动调用__add__魔术方法；
print(result.x)
print(result.y)
"""
  类方法语法：
    ＠classmethod 用这个装饰器标记，后面紧跟着方法；
  有了类方法，就可以直接用类名调用
"""
class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height
  def calculate_area(self):
    return self.width * self.height
  @classmethod
  def new_square(cls, side_length):
    return cls(side_length, side_length)
square = Rectangle.new_square(5)
print(square.calculate_area()) #25
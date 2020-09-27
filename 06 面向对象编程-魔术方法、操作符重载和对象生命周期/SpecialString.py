class SpecialString:
  def __init__(self, cont):
    self.cont = cont
  def __truediv__(self, other):
    line = "=" * len(other.cont)
    return "\n".join([self.cont, line, other.cont])
  def __mod__(self, other):
    list = [self.cont,other.cont]
    return list

spam = SpecialString("spam")
hello = SpecialString("Hello world!")
print(spam / hello) #此时会自动调用__truediv__魔术方法；
print(spam % hello) #这个道理也是一样，后面我就不举了；
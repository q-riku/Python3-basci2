"""
强私有：用两个＿下划线来表示，不能直接调，如果真要调，还是有办法的，语法如下：
        对象名．＿类名＿＿变量名  这样即可调用；
"""
class Spam:
  __egg = 7 #private
  def print_egg(self):
    print(self.__egg)
s = Spam()
# print(s.__egg)
s.print_egg()
print(s._Spam__egg) #不管怎么样，还是有办法调用的
# # print(s.__egg) #此时没有权限，抛出AttributeError异常；
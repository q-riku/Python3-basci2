"""
装饰器语法：@包装函数名    即在函数内嵌套函数；
"""
# def decor(func):
#   name = "w3cschool"
#   def wrap():
#     print("======"+name+"======")
#     func() #print_text()
#     print("============")
#   return wrap
# def print_text():
#   print("Hello world!")
# decorated = decor(print_text) #wrap
# decorated() #wrap()
# print("----------------------------")
def decor(func):
  def wrap():
    print("============")
    func()
    print("============")
  return wrap
@decor #这个可以多次被调用；
def print_text():
  print("Hello world123!")
print_text()
@decor
def fun():
    print("这是一个测试方法！")
fun()
"""
    静态方法语法：
    @staticmethod 用这个装饰器标记
    理解静态？
    答：静态与对象无关，只跟类有关；
"""
class Pizza:
  def __init__(self, toppings):
    self.toppings = toppings
  @staticmethod
  def validate_topping(topping):
    if topping == "pineapple":
      raise ValueError("No pineapples!")
    else:
      return True

ingredients = ["cheese", "onions", "spam"]
if all(Pizza.validate_topping(i) for i in ingredients):
  pizza = Pizza(ingredients)
  print(pizza.toppings) #['cheese', 'onions', 'spam']
#再举一个简单的例子
class A:
    def __init__(self,num):
        self.num = num
    @staticmethod
    def fun1(num):
        return num
    def fun2(self):
        return self.num
print(A.fun1(123456)) #静态方法可以用类名直接调用；
a = A(789)
print(a.fun2())#普通方法只能用对象调用；

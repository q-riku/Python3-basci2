"""
属性方法语法：
    @property 后面紧跟着方法；
备注：当访问属性时，属性名要是同上面的方法名一致，则调用该方法；
"""
class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
    @property #当访问跟方法名相同的属性时，被调用；
    def pineapple_allowed(self):
        return False
pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed) #此时调用上面的属性方法；
pizza.pineapple_allowed = True #属性只读，不能赋值；
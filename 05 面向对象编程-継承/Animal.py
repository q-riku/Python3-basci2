"""
    继承的语法：
    class 子类(父类)：
        《代码块》
        拥有父类里面所有的属性和方法；
"""
class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color
class Cat(Animal):
    def purr(self):
        print("Purr...")
class Dog(Animal):
    def bark(self):
        print("Woof!")
fido = Dog("Fido", "brown") #fido=>法斗、菲多
print(fido.color) #父类的属性也是可以调用的；
fido.bark()
class Pig(Cat,Dog):  #可以一次继承几个类；
    pass
p = Pig('阿狗','黄色')
p.purr()
p.bark()
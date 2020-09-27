class AA:
    name = "helloworld"
    def __init__(self):
        print('构造方法')
    def spam(self):
        print(1)
class BB(AA):
    def spam(self): #重写；
        print(2)
        super().spam() #调用父类的方法  super()函数一定是放在子类中； 解决方法名和属性相同时；
        print(super().name) #调用父类的属性
        AA.__init__(self) #调用父类的构造方法，一定要用类名来调用；
b = BB() #new出一个对象，创建一个对象；
b.spam()
BB().spam() #匿名对象的写法；
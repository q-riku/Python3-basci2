"""
对象生命周期由对象的创建、操作和销毁三个部分组成；
"""
class Test:
    # 类中第一个被调用的方法，即对对象的实例；
    def __new__(cls, string):
        super().__new__(cls) #被重写了
        return 'hello'+str(string)
    #实例化属性；
    def __init__(self,name):
        self.name = name
        print("我是构造方法")
    #当类执行完时，被调用；析造方法
    def __del__(self):
        print('对象执行结束！???')
class A:
    def __init__(self):
        print("我是构造方法")
    def fun(self):
        print("我是fun方法")

    def __del__(self):
        print('我是析造方法')
a = A()
a.fun()
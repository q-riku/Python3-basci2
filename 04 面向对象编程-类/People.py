class People:
    def __init__(self,name,age): #初始化方法，当定义出对象时，被调用；
        self.name = name
        self.age = age
    #不带参数；
    def test_self(self): #self==this(当前类的对象)
        return '姓名：'+self.name+"，年龄："+str(self.age)
    #带参数
    def test_self_v(self,xx):
        return xx
p = People('小明',18) #此时的self就是p对象；
print(p.test_self()) #调用类中的方法 对象.类的方法或属性；
print(p.name) #调用类中的属性
print(p.test_self_v('我有带参数！'))
print(p.xx) #调用类中不存在的属性，抛出的AttributeError异常；


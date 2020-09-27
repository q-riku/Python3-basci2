"""
    类的创建语法：
    class 类名：
        《代码块》
    备注：类名命名规则不能以数字开头，尽量以大写字母开头； 驼峰式命名法
    helloworld   HelloWorld
    类的调用：变量名 = 类名([是否带参]) 叫对象；
    对象能干么?
    答：能够调用类中所有的属性和方法；
"""
class Cat:
    def __init__(self, color, legs): #构造方法
        self.color = color
        self.legs = legs
felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
stumpy = Cat("brown", 3)

# print("felix:",felix.__dict__) #dict是用来存储对象属性的一个字典，其键为属性名，值为属性的值.
# print("rover:",rover.__dict__)
# print("stumpy:",stumpy.__dict__)

class AAA:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print(str(name)+"  "+str(age))
a = AAA('黄老师','18')

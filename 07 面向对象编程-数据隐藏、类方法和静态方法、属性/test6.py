"""
setter和getter函数设置；
可以利用函数名.setter///函数名.getter
"""
class A:
    def __init__(self,name):
        self.name = name
    @property
    def test_vv(self):
        return self.name
    @test_vv.setter
    def test_vv(self,value):
        print('确定是调用set方法！')
        self.name = value
    @test_vv.getter
    def test_vv(self):
        return '确定是调用get方法：'+self.name
a = A('小明')
a.test_vv = '小红' #赋值过程
print(a.test_vv)
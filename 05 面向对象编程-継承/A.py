class A:
    def method(self):
        print("A method")
class B(A):
    def another_method(self):
        print("B method")
class C(B):
    def third_method(self):
        print("C method")
c = C() #说明此时C类拥有A,B类中所有的属性和方法；
c.method()
c.another_method()
c.third_method()

class BB:
    name = "小明"
    age = 18
    def fun(self):
        return str(self.name) + str(self.age)
b = BB()
print(b.name)
print(b.age)
print(b.fun())
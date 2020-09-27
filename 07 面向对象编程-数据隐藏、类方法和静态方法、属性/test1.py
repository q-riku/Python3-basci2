class Queue:
    def __init__(self, contents):
        self._hiddenlist = list(contents) #弱私有_变量名
    def push(self, value):
        self._hiddenlist.insert(0, value)
    def pop(self):
        return self._hiddenlist.pop(-1)
    #如果将一个对象创建完成后，放到一个列表中，然后再打印这个列表，
    #那么会打印这个列表中所有的对象，这时候会调用__repr__魔术方法.
    def __repr__(self):
        return "Queue({})".format(self._hiddenlist)
queue = Queue([1, 2, 3])
print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenlist) #弱私有变量；用_下划线来表示；
print("================")

class Person(object):
    def __init__(self,name):
        self.name = name
    def __repr__(self): #理解这个魔术方法的使用；
        return "Person<%s>"%self.name
p1 = Person('小红')
print(p1)
p2 = Person('小丽')
a = [p1,p2]
print(a)


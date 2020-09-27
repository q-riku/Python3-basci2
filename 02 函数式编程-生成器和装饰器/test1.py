def countdown():
    i = 5
    while i > 0:
        yield i #yield可以无限存储；
        i -= 1
#采用for循环来迭代；
for i in countdown():
    print(i)
#yield在这边的功能相当于是临时挂起来；
def test_yield():
    print("生成器被执行！")
    yield 1
    yield 2
    yield 22
num = test_yield()
print(next(num)) #使用next()方法来迭代；
print(next(num))
print(next(num))

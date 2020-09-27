def numbers(x):
  for i in range(x):
    if i % 2 == 0:
      yield i
#生成器也可以用list()方法来存储；
print(list(numbers(11))) # [0, 2, 4, 6, 8, 10]
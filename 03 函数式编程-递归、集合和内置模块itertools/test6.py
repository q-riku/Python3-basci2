first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second) #{1, 2, 3, 4, 5, 6, 7, 8, 9}
print(first & second) #{4, 5, 6}
print(first - second) #{1, 2, 3} 第一个变量里面有的，而第二个变量没有的值；
print(second - first) #{8, 9, 7}
print(first ^ second) #{1, 2, 3, 7, 8, 9} #获取集合中非共有的子项；
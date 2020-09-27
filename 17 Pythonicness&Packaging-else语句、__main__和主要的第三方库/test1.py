"""
else 语句与 if 语句一起使用最为普遍，但它也可以遵循 for 或 while 循环，从而赋予它不同的含义。
使用 for 或 while 循环，如果循环正常结束（当 break 语句不会导致循环退出时），则会调用其中的代码。
"""
#当循环内执行完，没有遇到满足if条件/break关键字，此时，就执行else
for i in range(10):
   if i == 999:
      break
else:
   print("Unbroken 1")

for i in range(10):
   if i == 5:
      break
else:
   print("Unbroken 2")
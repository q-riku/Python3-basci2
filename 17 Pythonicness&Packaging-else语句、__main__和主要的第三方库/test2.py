"""
else 语句也可以和 try/except 语句一起使用。
在这种情况下，只有在 try 语句中没有发生错误时才会执行其中的代码。
"""
try:
   print(1)
except ZeroDivisionError:
   print(2)
else:
   print(3)
print("-------------------------")
try:
   print(1/0)
except ZeroDivisionError:
   print(4)
else:
   print(5)
"""
    三元运算符语法：
    变量名 = 值1 if 判断条件 else 值2
"""
a = 7
b = 100 if a >= 5 else 42
print(b)
print("========================================")
status  = 1
msg = "注销" if status == 2 else "登录"
print(msg)
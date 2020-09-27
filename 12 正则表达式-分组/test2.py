import re
#可以调用 group(0) 或者 group() 返回整个匹配。
#调用 group(n) ,n 要大于 0,返回匹配的第 n 个组。 下标是从1开始；
#groups() 返回所有匹配的分组。
pattern = r"a(bc)(de)(f(g)h)i"
match = re.match(pattern, "abcdefghijklmnop") #返回一个对象
if match:
   print(match.group())  #abcdefghi
   print(match.group(0)) #abcdefghi
   print(match.group(1)) #bc
   print(match.group(2)) #de
   print(match.groups()) #('bc', 'de', 'fgh', 'g')
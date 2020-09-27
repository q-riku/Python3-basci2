import re
"""
    {}的几种用法：
    {1，2}表示1次或2次；
    {1,}表示至少1次；
    {n}表示刚好n次；
"""
pattern = r"9{1,3}$"
if re.match(pattern, "9"):
   print("Match 1")
if re.match(pattern, "999"):
   print("Match 2")
if re.match(pattern, "9999"):
   print("Match 3")
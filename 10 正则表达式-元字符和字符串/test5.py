import re
#在字符类的开头放置一个 ^ 来反转它, 这使得它匹配除包含的字符之外的任何字符。
pattern = r"[^A-Z]"
if re.search(pattern, "this is all quiet"):
   print("Match 1")
if re.search(pattern, "AbCdEfG123"): #模糊匹配
   print("Match 2")
if re.search(pattern, "THISISALLSHOUTING"):
   print("Match 3")
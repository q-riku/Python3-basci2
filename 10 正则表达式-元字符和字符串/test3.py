import re
# 字符类提供了一种只匹配特定字符集中的一个的方法。
# 通过将匹配的字符放在方括号内来创建字符类。
pattern = r"[aeiou]"
if re.search(pattern, "grey"):
   print("Match 1")
if re.search(pattern, "qwertyuiop"):
   print("Match 2")
if re.search(pattern, "rhythm myths"):
   print("Match 3")
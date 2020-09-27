import re
# [a-z] 匹配任何小写字母字符。
# [G-P] 匹配从 G 到 P 的任何大写字符。
# [0-9] 匹配任何数字。
# 一个字符类可以包含多个范围。例如，[A-Za-z] 匹配任何一个字母。
pattern = r"[A-Z][A-Z][0-9]"
if re.search(pattern, "LS8"):
   print("Match 1")
if re.search(pattern, "E3"):
   print("Match 2")
if re.search(pattern, "1ab"):
   print("Match 3")
import re
#^表示以什么开头；
#$表示以什么结尾； 精准匹配
pattern = r"^gr.y$"
if re.match(pattern, "grey"):
   print("Match 1")
if re.match(pattern, "gray"):
   print("Match 2")
if re.match(pattern, "stingray"):
   print("Match 3")
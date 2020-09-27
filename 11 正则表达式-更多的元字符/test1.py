import re
# *表示0或多次；
pattern = r"egg(spam)*" #元字符只跟上一个字符有关
if re.match(pattern, "egg"):
   print("Match 1")
if re.match(pattern, "eggspamspamegg"):
   print("Match 2")
if re.search(pattern, "spamegg"):
   print("Match 3")
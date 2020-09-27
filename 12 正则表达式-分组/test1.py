import re
#()可以表示组，这意味着一个组可以作为元字符的参数，如 * 和？
pattern = r"egg(spam)*"
if re.match(pattern, "egg"):
   print("Match 1")
if re.match(pattern, "eggspamspamspamegg"):
   print("Match 2")
if re.match(pattern, "spam"):
   print("Match 3")
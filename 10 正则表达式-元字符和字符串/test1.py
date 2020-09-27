import re
pattern = r"gr.y" #点表示任意字符，但不包括新的行；
if re.match(pattern, "grey"):
   print("Match 1")
if re.match(pattern, "gray"):
   print("Match 2")
if re.match(pattern, "blue"):
   print("Match 3")
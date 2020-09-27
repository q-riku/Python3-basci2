import re
#+表示一次或多次；
pattern = r"g+"
if re.match(pattern, "g"):
   print("Match 1")
if re.match(pattern, "gggggggggggggg"):
   print("Match 2")
if re.match(pattern, "abc"):
   print("Match 3")

pattern = r"[0-9]+"
res = re.findall(pattern,'ab1212cd34ef56')
print(res)


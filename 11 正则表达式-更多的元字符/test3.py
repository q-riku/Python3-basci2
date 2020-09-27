import re
#?表示0次或1次；
pattern = r"ice(-)?cream"
if re.match(pattern, "ice-cream"):
   print("Match 1")
if re.match(pattern, "icecream"):
   print("Match 2")
if re.match(pattern, "sausages"):
   print("Match 3")
if re.match(pattern, "ice--ice"):
   print("Match 4")
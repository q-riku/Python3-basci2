import re
#\1表示小括号内的字符；
pattern = r"(.+) \1"
match = re.match(pattern, "word word")
if match:
   print ("Match 1")
match = re.match(pattern, "?! ?!")
if match:
   print ("Match 2")
match = re.match(pattern, "abc abc2")
if match:
   print ("Match 3")

time = "2020-7-3 10:10:10"
pattern = r"\d{4}(-)\d{1,2}\1\d{1,2} \d{1,2}(:)\d{1,2}\2\d{1,2}"
match = re.match(pattern,time)
if match:
   print(match.group())


import re
"""
    \d:[0-9]，
    \s:[\t \n \r \f \v]，
    \w:[a-zA-Z0-9_]，
    \D,\S,\W三个刚好与上面三个相反；
"""
pattern = r"(\D+\d)"
match = re.match(pattern, "Hi 999!")
if match:
   print("Match 1")
match = re.match(pattern, "1, 23, 456!")
if match:
   print("Match 2")
match = re.match(pattern, " ! $?")
if match:
    print("Match 3")
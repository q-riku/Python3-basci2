import re
"""
    \A	匹配字符串开始
    \Z	匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串。
    \b	匹配一个单词边界，也就是指单词和空格间的位置。
    例如， 'w3c\b' 可以匹配"chinaw3c" 中的 'w3c'，但不能匹配 "chinaw3cb" 中的 'w3c'。
注意事项：
    如果在re.MULTILINE模式内^和$可以匹配换行符的位置；而\A和\Z就不可以了。
"""
pattern = r"\b(cat)\b"
match = re.search(pattern, "The cat sat!")
if match:
   print ("Match 1")
match = re.search(pattern, "We s!cat<tered?") #特殊符号也可以
if match:
   print ("Match 2")
match = re.search(pattern, "We s cattered.")
if match:
   print ("Match 3")

pattern = r"abc\Z"
pattern = r"abc$"
match = re.search(pattern,"abc\n1234",re.M) #能够匹配换行前的字符
if match:
    print('Match 111')


import re
"""
    命名组格式为  (?P<name>...) 
        name表示组名，...表示内容，？表示()内的内容会被存储记录下来；
    非捕获组格式为 (?:...)
        ?:表示()内的内容不会被存储记录下来；
"""
pattern = r"(?P<first>abc)(?:def)(ghi)"
match = re.match(pattern, "abcdefghi")
if match: #None
   print(match.group("first")) #abc
   print(match.groups())  #('abc', 'ghi')
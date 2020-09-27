import re
"""
    [\w\.-]+ 匹配一个或多个单词字符，点或短划线。 
"""
pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
str = "Please contact info@w3cschool.cn for assistance"

match = re.search(pattern, str)
if match:
   print(match.group())
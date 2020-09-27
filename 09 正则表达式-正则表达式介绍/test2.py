"""
    search(匹配条件,被匹配的内容) 函数在字符串中的任何位置找到匹配的模式
    findall(匹配条件,被匹配的内容) 函数返回一个与模式匹配的所有子串的列表
"""
import re
pattern = r"spam"
#很显然被匹配的字符串，不是从spam开始；
if re.match(pattern, "eggspamsausagespam"):
    print("Match")
else:
    print("No match")
#search()函数是在字符串中的任何位置找到匹配的模式。
if re.search(pattern, "eggspamsausagespam"):
    print("Match")
else:
    print("No match")
#findall()函数返回一个与模式匹配的所有子串的列表
print(re.findall(pattern, "eggspamsausagespam"))
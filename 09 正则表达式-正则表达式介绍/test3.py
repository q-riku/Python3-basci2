"""
   search()返回的对象方法；
"""
import re
pattern = r"pam"
match = re.search(pattern, "eggspamsausagepam")
if match:
   print(match.group()) #输出找到的第一项；
   print(match.start()) #输出查找字符串的第一个索引位置；
   print(match.end()) #输出查找字符串的最后一个字符的索引位置；
   print(match.span()) #输出以上两个方法的值，并以元组进行存储；
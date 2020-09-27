"""
   原始字符串： r"字符串"
   match(匹配条件,被匹配的内容) 匹配的字符必须是有序列的；
"""
import re
pattern = r"spam" #原始字符串，不会转义任何东西；
if re.match(pattern, "2spamspamspam"): #查找spam在字符串"spamspamspam"中是否存在?
   print("Match")
else:
   print("No match")
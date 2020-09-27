"""
    re.sub(pattern,repl,string,max=0)
    repl替换字符串中所有出现的模式，除非提供max限定修改数量；
    sub方法返回修改后的字符串；
"""
import re
str = "My name is Loen. Hi Loen."
pattern = r"Loen"
newstr = re.sub(pattern, "Amy", str) #My name is Amy. Hi Amy.
print(newstr)
newstr = re.sub(pattern, "Amy", str,1) #My name is Amy. Hi Loen.
print(newstr)

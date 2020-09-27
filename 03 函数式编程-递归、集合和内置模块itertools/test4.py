num_set = {1, 2, 3, 4, 5}
word_set = set(["spam", "eggs", "sausage"])
#以上两种创建方式都可以创建；
print(word_set)
print(3 in num_set)
print("spam" not in word_set)
#同时也拥有列表和字典的功能，如in和not in;
dd_set = {1,2,3,4,3,2}
print(dd_set) #{1, 2, 3, 4} 自动过滤相同的数字；集合是一个唯一不重复的'集合'；
#要创建一个空集，必须使用 set()，如 {} 是创建一个空字典。
list = {}
print(type(list)) #<class 'dict'>
list_set = set()
print(type(list_set)) #<class 'set'>
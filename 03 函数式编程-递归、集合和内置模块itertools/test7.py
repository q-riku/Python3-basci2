# from itertools import count
# for i in count(): #count()函数无限增加；
#   print(i)
#   if i >=11:
#     break
# 3到11的值；
#cycle()函数重复循环一组值;
# from itertools import cycle
# for i in cycle(range(3)):
#     if i==2:
#         print('结束')
#         break
#     else:
#         print(i)
#repeat()函数一直重复一个对象；
from itertools import repeat
for i in repeat(range(2)):
    print(i) #一直重复range(0,2)对象；
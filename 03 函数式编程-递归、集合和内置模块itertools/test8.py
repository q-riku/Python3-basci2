from itertools import accumulate, takewhile,chain
#以可迭代的方式返回一个正在运行的值；
nums = list(accumulate(range(8))) #【0，1，2，3，4，5，6，7】
print(nums) #[0, 1, 3, 6, 10, 15, 21, 28]
print(list(takewhile(lambda x: x<= 6, nums))) #[0, 1, 3, 6]
a = [1,2,3,4]
b = ['x','y','z']
for each in chain(a,b): #两个列表合在一起
    print(each)
"""
    默认参数：必须放在参数的最后面；
    注意事项：默认值也是可以替代；
"""
def function(x, y, fruit="apple"):
   print(fruit)

# function(1, 2)
function(3, 4, "banana")
def is_even(x):
  if x == 0: #x=0 0==0
    return True
  else:
    return is_odd(x-1)

def is_odd(x):
  return not is_even(x)

print(is_odd(17)) #True
print(is_even(23)) #False 相当于not 22
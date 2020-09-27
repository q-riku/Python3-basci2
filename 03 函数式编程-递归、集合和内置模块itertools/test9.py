from itertools import product, permutations
letters = ("A", "B")
#product(参数1,参数2)依次取出参数1中每1个元素,与参数2中的每1个元素,组成元组,将所有元组组合成一个列表返回
print(list(product(letters, range(2)))) #[('A', 0), ('A', 1), ('B', 0), ('B', 1)]
print(list(permutations(letters))) #permutations函数重在排列；[('A', 'B'), ('B', 'A')]
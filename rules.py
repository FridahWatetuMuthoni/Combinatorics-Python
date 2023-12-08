import itertools


# THE RULE OF SUM EXAMPLE:
A = ['Alice', 'Bob', 'Charlie']
B = [0, 1, 2, 3]

print(A+B)

# THE PRODUCT RULE EXAMPLE:


A1 = ['a', 'b']
B1 = [1, 2, 3]

print(list(itertools.product(A1, B1)))


# TUPLES:
product_result = itertools.product("ab", repeat=4)
for p in product_result:
    print("".join(p))

# Permutations
lets = ['a', 'b', 'c', 'd']
permutation_result = itertools.permutations(lets, 2)
# print(list(permutation_result))
for element in permutation_result:
    print("".join(element))

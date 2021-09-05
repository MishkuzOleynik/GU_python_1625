import sys
from time import perf_counter
from itertools import islice




start = perf_counter()
nums = []
for num in range(1, 10 ** 6 + 1, 2):
    nums.append(num ** 2)
num_sum = sum(nums)
print(num_sum, perf_counter() - start)

start = perf_counter()
num_gen = (num ** 2 for num in range(1, 10 ** 6 +1, 1))
# num_gen_sum = sum(num_gen)
# print(num_gen_sum, perf_counter() - start)



# print(next(num_gen))

print(*islice(num_gen, 30))



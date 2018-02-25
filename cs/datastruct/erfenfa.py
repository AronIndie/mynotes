# 第二题
# 二分法求数值解
from functools import reduce

func = lambda r: reduce(lambda x, y: x+y, map(lambda k: 60.0 / (1 + r)**k, range(1, 8))) + 1000.0/(1+r)**7

print(func(0.28))
v = 750
delta = 1000
delta_target = 0.0001
r = 0.04
r_bound = [0, 1]

while abs(delta) > delta_target:
    y_1 = func(r)
    if v < y_1:
        r, r_bound[0] = (r+r_bound[1]) / 2, r
    else:
        r, r_bound[1] = (r + r_bound[0]) / 2, r
    delta = y_1 - v

print(r, v)

sum = 0
for i in range(1,21):
    sum += 0.025 / (1+0.03)**i

sum += 1 / (1 + 0.03)**20
print(sum)

sum_1 = 0
for i in range(1,21):
    sum_1 += 0.025 * i * (i+1) / (1 + 0.03)**(i+2)

print(sum_1/sum)

print(sum_1/sum / (1 + 0.03))

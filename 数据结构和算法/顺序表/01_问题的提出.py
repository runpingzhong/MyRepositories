# 如果a b c 均为自然数 a+b+c=1000 且啊a^2+b^2=c^2 如何求出所有组合？
import time
start=time.time()
for a in range(1001):
    for b in range(1001):
        for c in range(1001):
            if a ** 2 + b ** 2 == c ** 2 and a + b + c == 1000:
                print('a, b, c:%d,%d,%d'%(a,b,c))
end=time.time()
print('用时：%d'%(end-start))
# 改进 在已知a,b的前提下 =1000-a-b
start = time.time()
for a in range(1001):
    for b in range(1001):
        c = 1000-a-b
        if a ** 2 + b ** 2 == c ** 2:
                print('a, b, c:%d,%d,%d'%(a,b,c))
end = time.time()
print('用时：%d'%(end-start))


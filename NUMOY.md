# Numerical Python 
是一个开源的Python科学数组，用于快速处理任意维度数组。提供了常见的数组和矩阵操作

## ndarray 介绍
ndarray与python的原生list运算效率来比较
~~~
import random 
import time 
import numpy as np 
a = [] for i in range(
100000000
): 
a.append(random.random()) 
# 通过%time魔法方法, 查看当前行的代码运行一次所花费的时间 
%time sum1=sum(a) 
b=np.array(a) 
%time sum2=np.sum(b)
~~~
我们可以看到
~~~
CPU times: user 
852
 ms, sys: 
262
 ms, total: 
1.11
 s 
Wall time: 
1.13
 s

CPU times: user 
133
 ms, sys: 
653
 µs, total: 
133
 ms 
Wall time: 
134
 ms
~~~
-----
我们知道 **机器学习**最大的特点是大量的数据处理，所以python的numpy在其中起到了非常重要的作用

### 那为什么会产生如此大的差异呢
1.numpy内置了并行运算功能，当系统有多个核心时，做某种计算时，numpy会自动做并行计算
2.Numpy底层使用C语言编写，内部解除了GIL（全局解释器锁），其对数组的操作速度不受Python解释器的限制，所以，其效率远高于纯 Python代码。
---
# array的参数说明
~~~
import numpy as np 
a=np.array([
1,2,3,4,5,6],ndmin=3) 
print(a)
~~~







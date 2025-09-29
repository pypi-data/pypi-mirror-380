import numbers
import yaml
import sys, re, random, math
import tempfile
import tlog.tlogging as tl
import tio.tfile as tf
import tio.tshell as ts
import tutils.thpe as thpe
import tutils.context_opt as tcontext

log = tl.log

"""
根据一个分母及倍数,计算出一个分数的分子数组,它们的和为分母*倍数
"""


def edu_with_core_array(multiples=10, demoniator=2, count=3):
    sum_demoniator = demoniator * multiples
    while True:
        sum_value = 0
        int_array = []
        for index in range(0, count):
            random_demoniator = random.randint(1, sum_demoniator)
            int_array.append(random_demoniator)
            sum_value += random_demoniator
        if sum_value == sum_demoniator:
            return int_array


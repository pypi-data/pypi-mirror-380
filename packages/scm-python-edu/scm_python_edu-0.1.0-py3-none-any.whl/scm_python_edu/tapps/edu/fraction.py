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


def edu_fraction_to_markdown(
    int0: int, molecular: int, demoniator: int, to_random=False
) -> str or int:

    if to_random:
        boolean_array = [True, False]
        use_decimal = boolean_array[random.randint(0, len(boolean_array) - 1)]
        if use_decimal:
            return molecular / demoniator + int0
    if molecular > demoniator:
        int0 += math.floor(molecular / demoniator)
        molecular %= demoniator
    if molecular == 0:
        return str(int0)
    if molecular == demoniator:
        return str(int0 + 1)
    if molecular < 0:
        molecular += demoniator
        int0 -= 1
    str_values = f"\\frac{{{molecular}}}{{{demoniator}}}"
    return str(int0) + str_values if int0 > 0 else str_values


def edu_delta_original_core_handler(limit=100, count=10):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    deltas = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    len_primes = len(primes) - 1
    len_deltas = len(deltas) - 1
    log.info(
        f"do original core for limit={limit}, limit={count}, length of primes={len_primes +1}"
    )
    questions = []
    while True:
        demoniator = primes[random.randint(0, len_primes)]
        molecular = demoniator - deltas[random.randint(0, len_deltas)]
        if molecular <= 0 or 2 * molecular > demoniator:
            continue
        question = (
            f"如果\\frac{{{molecular}+a}}{{{demoniator}+a}}=\\frac{{2}}{{3}},计算原分数"
        )
        questions.append(question)
        count -= 1
        if count <= 0:
            break
    return questions


def edu_sum_original_core_handler(limit=100, count=2):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    deltas = [2, 3, 5, 7, 9]
    len_primes = len(primes) - 1
    len_deltas = len(deltas) - 1
    log.info(
        f"do original core for limit={limit}, limit={count}, length of primes={len_primes +1}"
    )
    questions = []
    while True:
        demoniator = primes[random.randint(0, len_primes)]
        molecular = demoniator - deltas[random.randint(0, len_deltas)]
        sum_value = deltas[random.randint(0, len_deltas)] * (demoniator + molecular)
        if molecular <= 0:
            continue
        question = f"分子与分母的和为{sum_value},化简为\\frac{{{molecular}}}{{{demoniator}}},计算原分数"
        questions.append(question)
        count -= 1
        if count <= 0:
            break
    return questions

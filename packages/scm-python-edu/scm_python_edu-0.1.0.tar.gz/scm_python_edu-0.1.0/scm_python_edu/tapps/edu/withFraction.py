import numbers
import yaml
import sys, re, random, math, fractions
import tempfile
import tlog.tlogging as tl
import tio.tfile as tf
import tio.tshell as ts
import tutils.thpe as thpe
import tutils.context_opt as tcontext
import tapps.edu.fraction as edu_fraction
import tapps.edu.latex as edu_latex

log = tl.log
SIGNS = ["+", "-"]

"""
随机返回一个小于int0且和它互素的正整数, 一般用于已知分母求真分数的分母
"""


def inner_get_prime(int0: int):
    while True:
        value0 = random.randint(1, int0 - 1)
        # 是否共素
        if math.gcd(value0, int0) == 1:
            return value0


"""
计算带符号的整数值,例如把"+" 10 -> 10, "-" 10 -> -10, 此时leading表示为-(,所以其必定是整数求反
"""


def inner_calc_int_with_sign(sign: str, int0: int, leading=False):
    int_value = int0 if sign == "+" else 0 - int0
    return 0 - int_value if leading else int_value


"""
计算带符号的分数值,例如把"+" 1 1/10 -> 1 1/10, "-" 1 1/10 -> -1 1/10, 此时leading表示为-(,所以其必定是分数求反

"""


def inner_calc_fraction_with_sign(
    sign: str, fraction0: fractions.Fraction, leading=False
):
    fraction_value = fraction0 if sign == "+" else 0 - fraction0
    return 0 - fraction_value if leading else fraction_value


def inner_generate_denominator_list(primes, multiple, items):
    len_primes = len(primes) - 1
    half_items = int(items / 2)
    denominators = [1 for int0 in range(0, items)]
    sum_denominator = 0
    for index in range(0, half_items):
        random_prime = primes[random.randint(0, len_primes)]
        denominator0 = random_prime
        sum_denominator += denominator0
        denominator1 = random.randint(2, multiple) * denominator0
        if denominator0 == denominator1:
            print(denominator0)
        denominators[index] = denominator0
        denominators[index + half_items] = denominator1
    # 如果所有的分母都相同,重新分配分母
    if sum_denominator == denominators[0] * half_items:
        return inner_generate_denominator_list(primes, multiple, items)
    return denominators


def inner_generate_molecular_list(denominators: list[int], items: int):
    moleculars = []
    for index in range(0, items):
        denominator = denominators[index]
        molecular = inner_get_prime(denominator)
        moleculars.append(molecular)
    return moleculars


def inner_generate_fraction_list(
    x_values: list[int],
    moleculars: list[int],
    denominators: list[int],
    items: int,
    limit: int,
    x=False,
):
    integers = [random.randint(0, limit) for int0 in range(0, items)]
    integers.sort(reverse=True)
    len_x = len(x_values) - 1
    output: list[str] = []
    # 必须分整数和分数部分,不然负分数计算后分子不对
    markdown0 = edu_fraction.edu_fraction_to_markdown(
        integers[0] + x_values[random.randint(0, len_x)] if x else integers[0],
        moleculars[0],
        denominators[0],
    )
    markdown1 = edu_fraction.edu_fraction_to_markdown(
        integers[1], moleculars[1], denominators[1]
    )
    markdown2 = edu_fraction.edu_fraction_to_markdown(
        integers[2], moleculars[2], denominators[2]
    )
    markdown3 = edu_fraction.edu_fraction_to_markdown(
        integers[3], moleculars[3], denominators[3]
    )
    sign1 = SIGNS[random.randint(0, 1)]
    sign3 = SIGNS[random.randint(0, 1)]
    x_sign = "x+" if x else ""
    statement = f"{markdown0}{sign1}{markdown1}-({x_sign}{markdown2}{sign3}{markdown3})"
    output.append(statement)
    sum_franction = (
        inner_calc_fraction_with_sign(
            "+", fractions.Fraction(moleculars[0], denominators[0]), False
        )
        + inner_calc_fraction_with_sign(
            sign1, fractions.Fraction(moleculars[1], denominators[1]), False
        )
        + inner_calc_fraction_with_sign(
            "-", fractions.Fraction(moleculars[2], denominators[2]), False
        )
        + inner_calc_fraction_with_sign(
            sign3, fractions.Fraction(moleculars[3], denominators[3]), True
        )
    )
    sum_int_value = (
        inner_calc_int_with_sign("+", integers[0], False)
        + inner_calc_int_with_sign(sign1, integers[1], False)
        + inner_calc_int_with_sign("-", integers[2], False)
        + inner_calc_int_with_sign(sign3, integers[3], True)
    )
    sum_franction < 0 and (sum_franction := sum_franction + 1) and (
        sum_int_value := sum_int_value - 1
    )
    return sum_int_value, sum_franction, output


"""
出单个分数计算题
sum_int_value, franction_values, output
求和的整数值, 分数值,题目的各个部分, 如果返回None,None,None, 表示跳过此题

"""


def inner_single_score_calculation(
    primes: list[int],
    x_values: list[int],
    items: int,
    multiple: int,
    limit: int,
    x=False,
):

    denominators = inner_generate_denominator_list(primes, multiple, items)
    moleculars = inner_generate_molecular_list(denominators, items)
    sum_int_value, sum_franction, output = inner_generate_fraction_list(
        x_values, moleculars, denominators, items, limit, x
    )
    # 分数运算后的结果
    # sum_franction:fractions.Fraction = franction_values[0]
    # for index in range(1, len(franction_values)): sum_franction += franction_values[index]
    return sum_int_value, sum_franction, output


"""
x: 表示是否其为解方程题目
"""


def edu_with_score_calculation(
    primes: list[int],
    x_values: list[int],
    count: int,
    items: int,
    multiple: int,
    limit: int,
    demoniate_limit: int,
    x=False,
):

    statements: list[str] = []
    while True:
        sum_int_value, sum_franction, output = inner_single_score_calculation(
            primes, x_values, items, multiple, limit, x
        )
        if not output:
            continue
        if sum_int_value > 1:
            # 如果分母太大了,题目太复杂,跳过此题
            if sum_franction.denominator > demoniate_limit:
                continue
            count -= 1
            output.append(
                f"={edu_fraction.edu_fraction_to_markdown(sum_int_value, sum_franction.numerator, sum_franction.denominator)}"
            )
            statements.append("".join(output))
            print("".join(output), edu_latex.TWO_EM_SPACE, edu_latex.TWO_EM_SPACE)
        if count <= 0:
            break
    return statements

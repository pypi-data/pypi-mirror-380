import sys, re, os, socket, copy

if os.name == "nt":
    from asyncio.windows_events import NULL
import glob
import fnmatch
import math
import random
import fractions
import datetime
import tlog.tlogging as tl
import tio.tfile as tf
import tio.tshell as ts
import tutils.context_opt as tcontext
import tutils.thpe as thpe
import tutils.tssh as tssh
import tutils.ttemplate as ttemplate
import tapps.edu.fraction as edu_fraction
import tapps.edu.latex as edu_latex
import tapps.edu.common as edu_common
import tapps.edu.math as edu_math
import tapps.edu.withFraction as edu_withFraction
import tapps.edu.disjunction as edu_disjunction

from tio.tcli import *


log = tl.log
# for each new plugin, please register cmd/sh in ${SCM_PYTHON_SH_HOME}/bin
# use for SUB_PLUGIN_NAME helper, for example xxxxx

# name= means that name follow string parameter
# mandatory is by func with default parameter
flags = [
    ("d", "debug", "enable/disable debug, boolean type sample", ["edu", "edu/hello"]),
    ("n:", ["name="], "foo name, data passed sample", ["edu", "edu/hello"]),
]

opp = OptParser(flags)


# please put entry function into top, and hello function in the top 1
@cli_invoker(
    "edu/hello"
)  # generate eclipse projecct for ops, please sure the current folder is web-console
def edu_hello_world(debug=False, name="diameter"):
    log.info(f"do something for debug={debug}, name={name}")
    print(0 - fractions.Fraction(1, 3) - fractions.Fraction(1, 4))


# 素因数分解出题
@cli_invoker("edu/prime-factor")  # generate the statement for prime factorization
def edu_prime_factor(
    limit=100, count=10, primes=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
):
    len_primes = len(primes) - 1
    log.info(
        f"do prime factor for limit={limit}, limit={count}, length of primes={len_primes +1}"
    )
    int_values = []
    while True:
        int_value = 1
        factors = []
        while True:
            random_prime = primes[random.randint(0, len_primes)]
            if int_value * random_prime >= limit:
                if (
                    int_value not in int_values
                    and len(factors) > 1
                    and int_value > limit / 10
                ):
                    count -= 1
                    log.info(f"int value {int_value}, factors{factors}")
                    int_values.append(int_value)
                break
            factors.append(random_prime)
            int_value *= factors[len(factors) - 1]
        if count <= 0:
            break
    return int_values


# 原分数
@cli_invoker("edu/delta-original-core")  # generate the original score
def edu_delta_original_core_handler(limit=100, count=10):
    edu_fraction.edu_delta_original_core_handler(limit, count)


# 乘法交换律分数混合计算
@cli_invoker("edu/|commutative-with-core")  # generate commutative the with score
def edu_commutative_with_score_calculation(limit=100, count=2):
    demoniators = [2, 4]
    log.info(f"do commutative with core for limit={limit}, limit={count}")
    statments = []
    while True:
        sum = 10
        demoniator_value = demoniators[random.randint(0, len(demoniators) - 1)]
        molecular_array = edu_math.edu_with_core_array(sum, demoniator_value, 3)
        unit_molecular = random.randint(5, sum)
        unit_demoniator = demoniators[random.randint(0, len(demoniators) - 1)]
        statment_output = []
        for int0 in molecular_array:
            statment_output.append(
                f"{edu_fraction.edu_fraction_to_markdown(0,unit_molecular,unit_demoniator, True)}{edu_latex.MULTIPILE}{edu_fraction.edu_fraction_to_markdown(0, int0, demoniator_value, True)}"
            )
        statments.append("+".join(statment_output))
        count -= 1
        if count <= 0:
            break
    return statments


# 原分数
@cli_invoker("edu/|sum-original-core")  # generate the original score
def edu_sum_original_core_handler(limit=100, count=2):
    edu_fraction.edu_sum_original_core_handler(limit, count)


# 裂项
@cli_invoker("edu/disjunction")  # generate the disjunction score
def edu_math_disjunction(limit=100, count=2, items=10):
    log.info(f"do math disjunction for limit={limit}, count={count}")
    questions = []
    while True:
        delta = random.randint(1, 5)
        questions.append(edu_disjunction.edu_math_single_disjunction(items, delta))
        count -= 1
        if count <= 0:
            break
    return questions


# 带分数出题
# latex占位 https://wenku.baidu.com/view/4cc39f5c59cfa1c7aa00b52acfc789eb172d9ee0.html
@cli_invoker("edu/with-score-calc")  # generate the statement with score calculation
def edu_with_score_calculation(
    limit=10, demoniate_limit=100, multiple=4, count=10, items=4, x=False
):
    log.info(f"do prime factor for limit={limit}, multiple={multiple}")
    # python 函数需要显式return
    return edu_withFraction.edu_with_score_calculation(
        [2, 3, 5, 7, 11, 13, 17, 19],
        [2, 3, 5, 7, 9],
        count,
        items,
        multiple,
        limit,
        demoniate_limit,
        x,
    )


@cli_invoker("edu/|math-to-md")  # generate the statement with score calculation
def edu_math_export_to_md_handler():
    # https://blog.aspose.com/2022/06/21/convert-markdown-to-pdf-in-python/

    print(edu_math.edu_with_core_array(10, 3))
    TWO_EM_SPACE = edu_latex.TWO_EM_SPACE
    SPACE_LINE = edu_latex.SPACE_LINE
    qquad = (
        f"{TWO_EM_SPACE} {TWO_EM_SPACE} {TWO_EM_SPACE} {TWO_EM_SPACE} {TWO_EM_SPACE}"
    )
    plugin_folder, context = edu_common.parse_python_extension_context(
        [
            [
                "PRIME_FACTOR",
                edu_prime_factor(100, 10),
                lambda a1, a2: f"${a1}={qquad}{a2}=$",
            ],
            [
                "PRIME_7_11_13_FACTOR",
                edu_prime_factor(1000, 10, [2, 3, 5, 7, 11, 13]),
                lambda a1, a2: f"${a1}={qquad}{a2}=$",
            ],
            [
                "WITH_SCORE",
                edu_with_score_calculation(10, 100, 3, 2, 4, False),
                lambda a1, a2: f"$${a1}{qquad}{a2}$${SPACE_LINE}{SPACE_LINE}{SPACE_LINE}{SPACE_LINE}{SPACE_LINE}{SPACE_LINE}{SPACE_LINE}{SPACE_LINE}",
            ],
            [
                "X_WITH_SCORE",
                edu_with_score_calculation(10, 100, 3, 1, 4, True),
                lambda a1, a2: f"$${a1}{qquad}{a2}$${SPACE_LINE}{SPACE_LINE}{SPACE_LINE}{SPACE_LINE}",
            ],
            [
                "DELTA_ORIGINAL_SCORE",
                edu_delta_original_core_handler(100, 2),
                lambda a1, a2: f"$${a1}{qquad}{a2}$${SPACE_LINE}{SPACE_LINE}",
            ],
            [
                "SUM_ORIGINAL_SCORE",
                edu_sum_original_core_handler(100, 2),
                lambda a1, a2: f"$${a1}{qquad}{a2}$${SPACE_LINE}{SPACE_LINE}",
            ],
            [
                "COMMUTATIVE_WITH_SCORE",
                edu_commutative_with_score_calculation(100, 2),
                lambda a1, a2: f"$${a1}{qquad}{a2}$${SPACE_LINE}{SPACE_LINE}",
            ],
            [
                "DISJUNCTION",
                edu_math_disjunction(100, 10, 8),
                lambda a1, a2: f"$${a1}{qquad}{a2}$${SPACE_LINE}{SPACE_LINE}",
            ],
        ]
    )

    new_files = ttemplate.handle_template_for_common_scripts(
        plugin_folder,
        tcontext.load_item(thpe.load_template_yaml("edu"), f"shes/math"),
        context,
    )
    # edu_common.conver_md_to_pdf(new_files[0])

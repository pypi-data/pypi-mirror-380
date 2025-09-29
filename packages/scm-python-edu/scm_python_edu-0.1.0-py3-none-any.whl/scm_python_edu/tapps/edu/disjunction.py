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


def edu_math_single_disjunction(items: int, delta: int) -> str or int:
    denominators = []
    last_denominator = random.randint(1, 10)
    for n in range(1, items + 1):
        denominator1 = last_denominator
        denominator2 = last_denominator + delta
        last_denominator = denominator2
        denominators.append(denominator1 * denominator2)
    return "+".join([f"\\frac{{{1}}}{{{denominator}}}" for denominator in denominators])

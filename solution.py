import numpy as np
import pandas as pd
from hyppo.ksample import MMD

chat_id = 356550601

def solution(x: np.array, y: np.array) -> bool:
    stat, pvalue = MMD().test(x, y)
    return pvalue < 0.07

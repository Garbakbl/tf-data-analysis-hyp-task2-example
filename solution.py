import pandas as pd
import numpy as np
from scipy.stats import ks_2samp

chat_id = 356550601

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.07
    stat, pval = ks_2samp(x, y)
    return pval < alpha

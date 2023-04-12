from scipy.stats import ks_2samp
import numpy as np

chat_id = 356550601

def solution(x: np.array, y: np.array) -> bool:
    _, p_value = ks_2samp(x, y)
    return p_value >= 0.07

import pandas as pd
import numpy as np
from scipy.stats import ks_2samp

chat_id = 422633669 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    stat, p = ks_2samp(x, y)
    return p < 0.04 # Ваш ответ, True или False

import pandas as pd
import numpy as np


chat_id = 422633669 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    
    var_x = np.var(x)
    var_y = np.var(y)
    
    t_stat = (mean_x - mean_y) / np.sqrt(var_x / len(x) + var_y / len(y))
    
    p_value = 2 * scipy.stats.t.cdf(-abs(t_stat), len(x) + len(y) - 2)
    
    return p_value < 0.05

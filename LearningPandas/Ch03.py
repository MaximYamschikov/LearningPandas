import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

s = pd.Series(np.arange(100, 110), index = np.arange(10, 20))
print(s[0:2])
print(s.loc[10:12])
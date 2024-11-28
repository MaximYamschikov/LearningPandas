
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# original_series = pd.Series([1, 2, 3])
# element_to_add = pd.Series([4])
# new_series = original_series.append(element_to_add, ignore_index=True)
#
# print(new_series)

original_series = pd.Series([1, 2, 3])
element_to_add = pd.Series([4])
new_series = pd.concat([original_series, element_to_add], ignore_index=True)
print(new_series)

original_series = pd.Series([1, 2, 3])
original_series.loc[len(original_series)] = 4
print(original_series)

original_series = pd.Series([1, 2, 3])
original_series[len(original_series)] = 4
print(original_series)

print(max(original_series.index + 1))
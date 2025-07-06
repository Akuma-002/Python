import numpy as np

arr = np.identity(4)

narr = np.insert(arr, (2, 3), 5)


print(narr)
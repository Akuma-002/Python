import numpy as np
import pandas as pd

a = {
    "name" : ["sahil", "Ram"],
    "marks" : [12, 34]
}

print(type(a))

ar = pd.DataFrame(a)
print(ar.iloc[1])

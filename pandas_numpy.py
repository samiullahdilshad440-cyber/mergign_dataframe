import pandas as pd
import numpy as np
 
# random = np.random.rand(5, 3)
# df = pd.DataFrame(random, columns=['A', 'B', 'C'])
inside = ["A", "B", "C","A", "B", "C"]
outside = ["School1", "School1", "School1", "School2", "School2", "School2"]
zip(outside, inside)
multi_index = list(zip(outside, inside))
hier_index = pd.MultiIndex.from_tuples(multi_index)
semester = ["semester 1", "semester2"]
df = pd.DataFrame(np.random.randn(6, 2), index=hier_index, columns=semester)
print(df)
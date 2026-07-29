import pandas as pd
import numpy as np
 
# random = np.random.rand(5, 3)
# df = pd.DataFrame(random, columns=['A', 'B', 'C'])
inside = ["Class A", "Class B", "Class C","Class A", "Class B", "Class C"]
outside = ["School 1", "School 1", "School 1", "School 2", "School 2", "School 2"]
zip(outside, inside)
multi_index = list(zip(outside, inside))
hier_index = pd.MultiIndex.from_tuples(multi_index)
semester = ["semester 1", "semester2"]
df = pd.DataFrame(np.random.randn(6, 2), index=hier_index, columns=semester)
school2 = df.xs("School 2")
classA = df.xs(("School 2", "Class A"), level= [0,1])
class_level = df.xs("Class A", level=1)
print(df)
print(school2)
print(classA)
print(class_level)
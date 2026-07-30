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
df1 = pd.DataFrame({'X':["X0","X1","X2","X3"],
        'Y':["Y0","Y1","Y2","Y3"],
        'Z':["Z0","Z1","Z2","Z3"],
        'T':["T0","T1","T2","T3"]})
df2 = pd.DataFrame({'X':["X4","X5","X6","X7"],
        'Y':["Y4","Y5","Y6","Y7"],
        'Z':["Z4","Z5","Z6","Z7"],
        'T':["T4","T5","T2","T3"]})
df3 = pd.DataFrame({'X':["X8","X9","X10","X11"],
        'Y':["Y8","Y9","Y10","Y11"],
        'Z':["Z8","Z9","Z10","Z11"],
        'T':["T8","T9","T10","T11"]})
concate = pd.concat([df1, df2, df3])
concate_withignoreindex = pd.concat([df1, df2, df3], ignore_index=True)
df2.columns = ["X","Y","Z","A"]
df1df2 = pd.concat([df1,df2], ignore_index=True)
hori = pd.concat([df1,df2,df3], ignore_index=True, axis=1)
# print(concate)
# print(concate_withignoreindex)
# print(df2)
# print(df1df2)
print(hori)

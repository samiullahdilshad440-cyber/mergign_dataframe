import pandas as pd
import numpy as np
df1 = pd.DataFrame({'X':["X0","X1","X2","X3"],
        'Y':["Y0","Y1","Y2","Y3"],
        'Z':["Z0","Z1","Z2","Z3"],
        'T':["T0","T1","T2","T3"],},
        index = [1,2,3,4]
        )
df2 = pd.DataFrame({'X':["X4","X5","X6","X7"],
        'Y':["Y4","Y5","Y6","Y7"],
        'Z':["Z4","Z5","Z6","Z7"],
        'T':["T4","T5","T2","T3"]},
        index = [5,6,7,8]
        )
df3 = pd.DataFrame({'X':["X8","X9","X10","X11"],
        'Y':["Y8","Y9","Y10","Y11"],
        'Z':["Z8","Z9","Z10","Z11"],
        'T':["T8","T9","T10","T11"]
        },
        index = [9,10,11,12]
        )
concate =pd.concat([df1,df2,df3], axis=1)
print(concate)


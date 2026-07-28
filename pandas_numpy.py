import pandas as pd
import numpy as np
 
random = np.random.rand(5, 3)
df = pd.DataFrame(random, columns=['A', 'B', 'C'])
print(df)
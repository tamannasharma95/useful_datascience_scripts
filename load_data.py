#import libraries
import numpy as np
import pandas as pd

# specify the file 
data=pd.read_csv('path-to-file') 

# show the data types 
data.dtypes

# shape of the data 
data.shape 

# stats of the data 
data.describe()

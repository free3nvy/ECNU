import numpy as np # linear algebra
import pandas as pd # data processing
# import matplotlib.pyplot as plt
# import seaborn as sns
 
df = pd.read_csv('Social_Network_Ads.csv')
df=df.iloc[:,2:]
print(df.sample(5))

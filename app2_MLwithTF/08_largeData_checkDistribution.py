# it might be wise to confirm that our dataset is a perfect 50/50 split

import pandas as pd
from collections import Counter

df = pd.read_csv('train_set.csv', names=['sentiment', 'tweet'], delimiter=':::')
print(Counter(df['sentiment']))

Counter({})

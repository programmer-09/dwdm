

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
!pip install apyori
from apyori import apriori

store_data = pd.read_csv('/bread basket.csv')

transactions = store_data.groupby('Transaction')['Item'].apply(list).tolist()

association_results = apriori(transactions, min_support=0.01, min_confidence=0.2, min_lift=1.0, min_length=2)

association_results = list(association_results)

for rule in association_results[:5]:
    items = list(rule.items)
    print(f"Rule: {items}")
    print(f"Support: {rule.support}")
    for ordered_stat in rule.ordered_statistics:
        print(f"Confidence: {ordered_stat.confidence}")
        print(f"Lift: {ordered_stat.lift}")
    print("=" * 40)
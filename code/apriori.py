from itertools import combinations
from collections import defaultdict

# Step 1: Convert transactions into a list of lists
transaction_list = transactions.tolist()

# Step 2: Create a function to calculate support for itemsets
def calculate_support(transactions, itemsets):
    itemset_support = defaultdict(int)
    for transaction in transactions:
        for itemset in itemsets:
            if set(itemset).issubset(set(transaction)):
                itemset_support[itemset] += 1
    total_transactions = len(transactions)
    return {itemset: support / total_transactions for itemset, support in itemset_support.items()}

# Step 3: Generate frequent itemsets
def apriori(transactions, min_support=0.01):
    single_items = {frozenset([item]) for transaction in transactions for item in transaction}
    current_itemsets = single_items
    frequent_itemsets = {}
    
    while current_itemsets:
        # Calculate support for current itemsets
        support = calculate_support(transactions, current_itemsets)
        # Filter itemsets by min_support
        current_itemsets = {itemset for itemset, sup in support.items() if sup >= min_support}
        # Add frequent itemsets to the result
        frequent_itemsets.update({itemset: sup for itemset, sup in support.items() if sup >= min_support})
        # Generate combinations of next size
        current_itemsets = {i.union(j) for i in current_itemsets for j in current_itemsets if len(i.union(j)) == len(i) + 1}
    
    return frequent_itemsets

# Apply Apriori algorithm
min_support = 0.01
frequent_itemsets = apriori(transaction_list, min_support=min_support)

# Display the top frequent itemsets
sorted_frequent_itemsets = sorted(frequent_itemsets.items(), key=lambda x: x[1], reverse=True)
sorted_frequent_itemsets[:10]

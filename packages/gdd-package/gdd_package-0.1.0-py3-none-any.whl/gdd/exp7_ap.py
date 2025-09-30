import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# Load dataset
transactions = pd.read_csv("transactions_onehot.csv")

# Convert rows to list of items
transactions_list = []
for _, row in transactions.iterrows():
    transaction = row[row == 1].index.tolist()
    transactions_list.append(transaction)

# Encode
te = TransactionEncoder()
te_ary = te.fit(transactions_list).transform(transactions_list)
df_encoded = pd.DataFrame(te_ary, columns=te.columns_)

# Frequent itemsets
frequent_itemsets = apriori(df_encoded, min_support=0.01, use_colnames=True)
print("Frequent Itemsets:")
print(frequent_itemsets)

# Association rules
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
print("\nAssociation Rules:")
print(rules)

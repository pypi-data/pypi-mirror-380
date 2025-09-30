from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

X_kmeans = insta[['Instagram visit score', 'Spending_rank(0 to 100)']]

# KMeans clustering
kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)
kmeans.fit(X_kmeans)

insta['cluster'] = kmeans.labels_
print(insta.head())

# Visualization
plt.figure(figsize=(10,6))
plt.scatter(X_kmeans['Instagram visit score'],
            X_kmeans['Spending_rank(0 to 100)'],
            c=insta['cluster'], cmap='rainbow')
plt.title("K-Means Clustering")
plt.xlabel("Instagram visit score")
plt.ylabel("Spending Rank")
plt.show()

from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt

X_hcluster = insta[['Instagram visit score', 'Spending_rank(0 to 100)']]

# Agglomerative clustering
agg_clustering = AgglomerativeClustering(n_clusters=4, linkage='ward')
insta['h_cluster'] = agg_clustering.fit_predict(X_hcluster)

# Dendrogram
linked = linkage(X_hcluster, 'ward')
plt.figure(figsize=(10,7))
dendrogram(linked, orientation='top', distance_sort='descending', show_leaf_counts=True)
plt.title("Hierarchical Clustering Dendrogram")
plt.show()

print(insta.head())

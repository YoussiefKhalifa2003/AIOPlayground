# Example usage
data = [
    [1.0, 2.0],
    [1.5, 1.8],
    [5.0, 8.0],
    [8.0, 8.0],
    [1.1, 2.1],
    [9.0, 2.0],
    [8.9, 8.1],
    [8.8, 7.9],
]

centroids, labels = kmeans(data, k=3, seed=42)
print("Centroids:", centroids)
print("Labels:", labels)

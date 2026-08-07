# kmeans.py
"""K‑means clustering implementation.

Provides a simple, deterministic k‑means algorithm with Euclidean distance.
"""

from __future__ import annotations

import random
from typing import List, Tuple, Sequence
import math


def euclidean_distance(a: Sequence[float], b: Sequence[float]) -> float:
    """Return Euclidean distance between two vectors."""
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def initialize_centroids(
    data: Sequence[Sequence[float]], k: int, seed: int | None = None
) -> List[List[float]]:
    """Randomly select *k* distinct points from *data* as initial centroids."""
    if seed is not None:
        random.seed(seed)

    indices = random.sample(range(len(data)), k)
    return [list(data[i]) for i in indices]


def assign_clusters(
    data: Sequence[Sequence[float]], centroids: Sequence[Sequence[float]]
) -> List[int]:
    """Assign each point in *data* to the nearest centroid.

    Returns a list where the i‑th element is the index of the centroid
    closest to ``data[i]``.
    """
    clusters = []
    for point in data:
        distances = [
            euclidean_distance(point, centroid) for centroid in centroids
        ]
        clusters.append(int(min(range(len(distances)), key=lambda i: distances[i]))
    return clusters


def update_centroids(
    data: Sequence[Sequence[float]], clusters: Sequence[int], k: int
) -> List[List[float]]:
    """Compute new centroids as the mean of points assigned to each cluster."""
    new_centroids: List[List[float]] = []
    for cluster_id in range(k):
        # Gather points belonging to this cluster
        points = [data[i] for i, cid in enumerate(clusters) if cid == cluster_id]

        if not points:
            # Keep previous centroid if cluster becomes empty
            raise ValueError(
                f"Cluster {cluster_id} is empty – consider re‑initializing."
            )

        # Compute mean for each dimension
        dim = len(points[0])
        centroid = [sum(p[d] for p in points) / len(points) for d in range(dim)]
        new_centroids.append(centroid)

    return new_centroids


def kmeans(
    data: Sequence[Sequence[float]],
    k: int,
    max_iters: int = 100,
    tol: float = 1e-4,
    seed: int | None = None,
) -> Tuple[List[List[float]], List[int]]:
    """Perform k‑means clustering.

    Args:
        data: Iterable of feature vectors (each a sequence of floats).
        k: Number of clusters.
        max_iters: Maximum number of iterations.
        tol: Convergence tolerance on centroid movement.
        seed: Random seed for reproducible centroid initialization.

    Returns:
        A tuple ``(centroids, clusters)`` where ``centroids`` is a list of the
        final cluster centers and ``clusters`` maps each input point to its
        assigned cluster index.
    """
    # Input validation
    if k <= 0:
        raise ValueError("k must be positive")
    if not data:
        raise ValueError("data must not be empty")

    centroids = initialize_centroids(data, k, seed)

    for _ in range(max_iters):
        clusters = assign_clusters(data, centroids)

        new_centroids = update_centroids(data, clusters, k)

        # Check for convergence
        if all(
            euclidean_distance(c, nc) < tol
            for c, nc in zip(centroids, new_centroids)
        ):
            break

        centroids = new_centroids

    return centroids, clusters

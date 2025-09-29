# KElbowFinder

This package provides tools for determining the optimal number of clusters in K-Means clustering using the **Elbow Method**. It automatically calculates the sum of squared errors (SSE) for different values of *k*, detects the optimal k, and visualizes the results with an elbow plot.

---

## Installation

You can install the package using pip. Make sure to have the required dependencies listed in `requirements.txt`.

```bash
pip install -r requirements.txt
```

If you are working locally and want to install the package in development mode:

```bash
pip install -e .
```

---


## Usage

To use the package, import the main function and pass your scaled data:

```python
import pandas as pd
from sklearn.preprocessing import StandardScaler
from KElbowFinder.elbow import find_best_k

# Example dataset
data = pd.DataFrame({
    'Income_$': [15, 16, 17, 18, 19, 20],
    'SpendingScore': [39, 81, 6, 77, 40, 76]
})

# Scale the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(data)

# Find the best k and save the elbow plot
best_k = find_best_k(X_scaled, max_k=10, save_plot=True)
print(f"Optimal k: {best_k}")
# The elbow plot will be saved as 'elbow_plot.png' in your working directory.
```

---

## Package Structure

* `KElbowFinder/__init__.py`: Initializes the package and defines exports.
* `KElbowFinder/elbow.py`: Core functionality for determining optimal clusters and plotting.
* `setup.py`: Configuration file for package metadata.
* `requirements.txt`: Lists dependencies required for the package.
* `tests/elbow_test.py`: Unit tests for the main functionality.

---

## Choosing a Package Name

The package name is **KElbowFinder**.
It is descriptive and relevant to the functionality provided.
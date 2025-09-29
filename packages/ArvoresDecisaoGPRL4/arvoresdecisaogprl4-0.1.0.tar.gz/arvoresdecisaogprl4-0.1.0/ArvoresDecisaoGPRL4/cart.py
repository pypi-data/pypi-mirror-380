import numpy as np
import pandas as pd
from collections import Counter

class CARTNode:
    """Node class for CART decision tree"""
    def __init__(self):
        self.feature = None
        self.threshold = None
        self.left = None
        self.right = None
        self.value = None  # For leaf nodes
        self.samples = 0
        self.gini = 0.0
        self.class_counts = None

class CART:
    """CART (Classification and Regression Trees) implementation with Gini criterion"""

    def __init__(self, max_depth=None, min_samples_split=2, min_samples_leaf=1, max_features=None):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.min_samples_leaf = min_samples_leaf
        self.max_features = max_features
        self.root = None
        self.n_classes = None
        self.feature_names = None

    def gini_impurity(self, y):
        """Calculate Gini impurity for a set of labels"""
        if len(y) == 0:
            return 0.0

        class_counts = Counter(y)
        total = len(y)
        gini = 1.0

        for count in class_counts.values():
            prob = count / total
            gini -= prob ** 2

        return gini

    def information_gain(self, y, left_mask, right_mask):
        """Calculate information gain using Gini impurity"""
        n = len(y)
        n_left = np.sum(left_mask)
        n_right = np.sum(right_mask)

        if n_left == 0 or n_right == 0:
            return 0.0

        # Current gini impurity
        current_gini = self.gini_impurity(y)

        # Weighted average of child gini impurities
        left_gini = self.gini_impurity(y[left_mask])
        right_gini = self.gini_impurity(y[right_mask])

        weighted_gini = (n_left / n) * left_gini + (n_right / n) * right_gini

        return current_gini - weighted_gini

    def find_best_split(self, X, y):
        """Find the best feature and threshold for splitting"""
        n_samples, n_features = X.shape

        if self.max_features is None:
            features_to_consider = range(n_features)
        else:
            n_features_to_consider = min(self.max_features, n_features)
            features_to_consider = np.random.choice(n_features, n_features_to_consider, replace=False)

        best_gain = -1
        best_feature = None
        best_threshold = None

        for feature in features_to_consider:
            # Get unique values for this feature and sort them
            unique_values = np.unique(X[:, feature])

            # Skip if only one unique value
            if len(unique_values) <= 1:
                continue

            # Try thresholds between consecutive unique values
            for i in range(len(unique_values) - 1):
                threshold = (unique_values[i] + unique_values[i + 1]) / 2

                # Create masks for left and right splits
                left_mask = X[:, feature] <= threshold
                right_mask = ~left_mask

                # Skip if split doesn't satisfy minimum samples per leaf
                if np.sum(left_mask) < self.min_samples_leaf or np.sum(right_mask) < self.min_samples_leaf:
                    continue

                # Calculate information gain
                gain = self.information_gain(y, left_mask, right_mask)

                if gain > best_gain:
                    best_gain = gain
                    best_feature = feature
                    best_threshold = threshold

        return best_feature, best_threshold, best_gain

    def build_tree(self, X, y, depth=0):
        """Recursively build the decision tree"""
        n_samples = len(y)

        # Create node
        node = CARTNode()
        node.samples = n_samples
        node.gini = self.gini_impurity(y)
        node.class_counts = Counter(y)

        # Determine the most common class (for prediction)
        node.value = max(node.class_counts.items(), key=lambda x: x[1])[0]

        # Stopping criteria
        if (self.max_depth is not None and depth >= self.max_depth) or \
           (n_samples < self.min_samples_split) or \
           (node.gini == 0.0):  # Pure node
            return node

        # Find best split
        best_feature, best_threshold, best_gain = self.find_best_split(X, y)

        # If no good split found, make it a leaf
        if best_feature is None or best_gain <= 0:
            return node

        # Apply the split
        node.feature = best_feature
        node.threshold = best_threshold

        left_mask = X[:, best_feature] <= best_threshold
        right_mask = ~left_mask

        # Recursively build left and right subtrees
        node.left = self.build_tree(X[left_mask], y[left_mask], depth + 1)
        node.right = self.build_tree(X[right_mask], y[right_mask], depth + 1)

        return node

    def fit(self, X, y, feature_names=None):
        """Train the CART model"""
        if isinstance(X, pd.DataFrame):
            self.feature_names = X.columns.tolist()
            X = X.values
        else:
            self.feature_names = feature_names or [f"feature_{i}" for i in range(X.shape[1])]

        if isinstance(y, pd.Series):
            y = y.values

        self.n_classes = len(np.unique(y))
        self.root = self.build_tree(X, y)
        return self

    def predict_sample(self, x, node):
        """Predict a single sample"""
        if node.left is None and node.right is None:  # Leaf node
            return node.value

        if x[node.feature] <= node.threshold:
            return self.predict_sample(x, node.left)
        else:
            return self.predict_sample(x, node.right)

    def predict(self, X):
        """Make predictions on new data"""
        if isinstance(X, pd.DataFrame):
            X = X.values

        predictions = []
        for x in X:
            pred = self.predict_sample(x, self.root)
            predictions.append(pred)

        return np.array(predictions)

    def predict_proba_sample(self, x, node):
        """Get prediction probabilities for a single sample"""
        if node.left is None and node.right is None:  # Leaf node
            total_samples = node.samples
            proba = np.zeros(self.n_classes)
            for class_label, count in node.class_counts.items():
                proba[class_label] = count / total_samples
            return proba

        if x[node.feature] <= node.threshold:
            return self.predict_proba_sample(x, node.left)
        else:
            return self.predict_proba_sample(x, node.right)

    def predict_proba(self, X):
        """Get prediction probabilities"""
        if isinstance(X, pd.DataFrame):
            X = X.values

        probas = []
        for x in X:
            proba = self.predict_proba_sample(x, self.root)
            probas.append(proba)

        return np.array(probas)

    def print_tree(self, node=None, depth=0, prefix="Root", max_depth=5):
        """Print the decision tree structure."""
        if node is None:
            node = self.root

        if node is None:
            print("Tree has not been fitted yet.")
            return

        if depth > max_depth:
            print("  " * depth + "... (truncated)")
            return

        indent = "  " * depth

        if node.left is None and node.right is None:  # Leaf node
            print(f"{indent}{prefix}: Leaf -> {node.value} (gini: {node.gini:.3f}, (samples: {node.samples})")
        else:
            feature_name = self.feature_names[node.feature] if self.feature_names else f"X[{node.feature}]"
            print(f"{indent}{prefix}: {feature_name} <= {node.threshold:.3f} (gini: {node.gini:.3f}, (samples: {node.samples})")

            if node.left:
                self.print_tree(node.left, depth + 1, "True", max_depth)
            if node.right:
                self.print_tree(node.right, depth + 1, "False", max_depth)
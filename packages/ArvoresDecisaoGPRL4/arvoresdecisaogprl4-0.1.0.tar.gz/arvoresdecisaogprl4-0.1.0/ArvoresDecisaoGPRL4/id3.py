import numpy as np
import pandas as pd
from collections import Counter
import math

class ID3Node:
    """Node class for ID3 decision tree"""
    def __init__(self):
        self.attribute = None
        self.branches = {}  # Dictionary of branches
        self.class_label = None  # For leaf nodes
        self.is_leaf = False
        self.samples = 0
        self.class_counts = None

class ID3:
    """ID3 Decision Tree implementation with information gain criterion"""

    def __init__(self, max_depth=None, min_samples_split=2, min_samples_leaf=1, min_information_gain=0.01):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.min_samples_leaf = min_samples_leaf
        self.min_information_gain = min_information_gain
        self.root = None
        self.feature_names = None

    def entropy(self, y):
        """Calculate entropy of a set of labels"""
        if len(y) == 0:
            return 0.0

        class_counts = Counter(y)
        total = len(y)
        entropy = 0.0

        for count in class_counts.values():
            if count > 0:
                prob = count / total
                entropy -= prob * math.log2(prob)

        return entropy

    def information_gain(self, y, splits):
        """Calculate information gain for given splits"""
        total = len(y)
        current_entropy = self.entropy(y)

        weighted_entropy = 0.0
        for split_indices in splits:
            if len(split_indices) > 0:
                weight = len(split_indices) / total
                split_entropy = self.entropy(y[split_indices])
                weighted_entropy += weight * split_entropy

        return current_entropy - weighted_entropy

    def find_best_split(self, X, y):
        """Find the best attribute to split on"""
        n_samples, n_features = X.shape

        best_gain = -1
        best_feature = None

        for feature in range(n_features):
            X_feature = X[:, feature]

            # Skip if all values are the same
            unique_values = np.unique(X_feature)
            if len(unique_values) <= 1:
                continue

            # Create splits based on unique values (categorical approach)
            splits = []
            valid_split = True

            for value in unique_values:
                indices = np.where(X_feature == value)[0]
                if len(indices) < self.min_samples_leaf:
                    valid_split = False
                    break
                splits.append(indices)

            # Skip if any split doesn't satisfy min_samples_leaf
            if not valid_split or len(splits) <= 1:
                continue

            # Calculate information gain
            gain = self.information_gain(y, splits)

            if gain > best_gain:
                best_gain = gain
                best_feature = feature

        return best_feature, best_gain

    def build_tree(self, X, y, depth=0, used_features=None):
        """Recursively build the decision tree"""
        if used_features is None:
            used_features = set()

        n_samples = len(y)

        # Create node
        node = ID3Node()
        node.samples = n_samples
        node.class_counts = Counter(y)

        # Determine the most common class
        node.class_label = max(node.class_counts.items(), key=lambda x: x[1])[0]

        # Stopping criteria
        if (self.max_depth is not None and depth >= self.max_depth) or \
           (n_samples < self.min_samples_split) or \
           (len(np.unique(y)) == 1) or \
           (len(used_features) == X.shape[1]):  # All features used (ID3 specific)
            node.is_leaf = True
            return node

        # Find best split
        best_feature, best_gain = self.find_best_split(X, y)

        # If no good split found or gain too low, make it a leaf
        if best_feature is None or best_gain < self.min_information_gain:
            node.is_leaf = True
            return node

        # Apply the split
        node.attribute = best_feature

        # Create branches for each unique value of the selected feature
        unique_values = np.unique(X[:, best_feature])

        # Add current feature to used features (ID3 doesn't reuse features)
        new_used_features = used_features.copy()
        new_used_features.add(best_feature)

        # Check if all branches would satisfy min_samples_leaf before proceeding
        valid_branches = {}
        for value in unique_values:
            mask = X[:, best_feature] == value
            if np.sum(mask) >= self.min_samples_leaf:
                valid_branches[value] = mask

        # If no valid branches, make it a leaf
        if len(valid_branches) == 0:
            node.is_leaf = True
            return node

        for value, mask in valid_branches.items():
            # Recursively build subtree for this branch
            # Remove the selected feature from X for ID3 (features are not reused)
            X_subset = np.delete(X[mask], best_feature, axis=1)
            y_subset = y[mask]

            # Adjust feature indices for the subset
            adjusted_used_features = set()
            for used_feat in new_used_features:
                if used_feat < best_feature:
                    adjusted_used_features.add(used_feat)
                elif used_feat > best_feature:
                    adjusted_used_features.add(used_feat - 1)
                # Skip the current feature as it's removed

            if X_subset.shape[1] > 0:  # Still have features to split on
                node.branches[value] = self.build_tree(X_subset, y_subset, depth + 1, adjusted_used_features)
            else:
                # No more features, create leaf
                leaf = ID3Node()
                leaf.is_leaf = True
                leaf.samples = len(y_subset)
                leaf.class_counts = Counter(y_subset)
                leaf.class_label = max(leaf.class_counts.items(), key=lambda x: x[1])[0]
                node.branches[value] = leaf

        # If no valid branches were created, make it a leaf
        if len(node.branches) == 0:
            node.is_leaf = True

        return node

    def fit(self, X, y, feature_names=None):
        """Train the ID3 model"""
        if isinstance(X, pd.DataFrame):
            self.feature_names = X.columns.tolist()
            X = X.values
        else:
            self.feature_names = feature_names or [f"feature_{i}" for i in range(X.shape[1])]

        if isinstance(y, pd.Series):
            y = y.values

        # Build tree
        self.root = self.build_tree(X, y)
        return self

    def predict_sample(self, x, node, feature_mapping=None):
        """Predict a single sample"""
        if feature_mapping is None:
            feature_mapping = list(range(len(x)))

        if node is None or node.is_leaf:
            return node.class_label if node else None

        # Get the feature value
        original_feature_idx = feature_mapping[node.attribute] if node.attribute < len(feature_mapping) else node.attribute
        feature_value = x[original_feature_idx]

        # Follow the appropriate branch
        if feature_value in node.branches:
            # Create new feature mapping for the subtree (removing the used feature)
            new_feature_mapping = []
            for i, orig_idx in enumerate(feature_mapping):
                if i != node.attribute:
                    new_feature_mapping.append(orig_idx)

            return self.predict_sample(x, node.branches[feature_value], new_feature_mapping)
        else:
            # Value not seen in training, return majority class from current node
            return node.class_label

    def predict(self, X):
        """Make predictions on new data"""
        if isinstance(X, pd.DataFrame):
            X = X.values

        predictions = []
        for x in X:
            pred = self.predict_sample(x, self.root)
            predictions.append(pred)

        return np.array(predictions)

    def print_tree(self, node=None, depth=0, prefix="Root", max_depth=5, feature_mapping=None):
        """Print the decision tree structure."""
        if node is None:
            node = self.root
            feature_mapping = list(range(len(self.feature_names)))

        if node is None:
            print("Tree has not been fitted yet.")
            return

        if depth > max_depth:
            print("  " * depth + "... (truncated)")
            return

        indent = "  " * depth

        if node.is_leaf:
            print(f"{indent}{prefix}: Leaf -> {node.class_label} (samples: {node.samples})")
        else:
            original_feature_idx = feature_mapping[node.attribute] if node.attribute < len(feature_mapping) else node.attribute
            feature_name = self.feature_names[original_feature_idx] if original_feature_idx < len(self.feature_names) else f"X[{original_feature_idx}]"
            print(f"{indent}{prefix}: {feature_name} (samples: {node.samples})")

            # Create new feature mapping for subtrees
            new_feature_mapping = []
            for i, orig_idx in enumerate(feature_mapping):
                if i != node.attribute:
                    new_feature_mapping.append(orig_idx)

            for value, child_node in node.branches.items():
                self.print_tree(child_node, depth + 1, f"= {value}", max_depth, new_feature_mapping)
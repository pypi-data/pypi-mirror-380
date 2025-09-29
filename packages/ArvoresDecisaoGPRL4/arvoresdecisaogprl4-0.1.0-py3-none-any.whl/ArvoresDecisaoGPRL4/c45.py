import numpy as np
import pandas as pd
from collections import Counter
import math

class C45Node:
    """Node class for C4.5 decision tree"""
    def __init__(self):
        self.attribute = None
        self.threshold = None  # Pros atributos contínuos
        self.branches = {}  # Dict de branches
        self.class_label = None  # Pra nós folhas
        self.is_leaf = False
        self.samples = 0
        self.class_counts = None
        self.split_info = 0.0  # Split info pra razão de ganho

class C45:
    def __init__(self, max_depth=None, min_samples_split=2, min_samples_leaf=1, min_gain_ratio=0.01):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.min_samples_leaf = min_samples_leaf
        self.min_gain_ratio = min_gain_ratio
        self.root = None
        self.feature_names = None
        self.continuous_features = None
        self.categorical_features = None

    # Calcula entropia
    def entropy(self, y):
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

    # Calcula ganho
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

    def split_information(self, splits, total):
        """Calculate split information for gain ratio"""
        if total == 0:
            return 0.0

        split_info = 0.0
        for split_indices in splits:
            if len(split_indices) > 0:
                prob = len(split_indices) / total
                split_info -= prob * math.log2(prob)

        return split_info

    def gain_ratio(self, y, splits):
        """Calculate gain ratio (information gain normalized by split information)"""
        gain = self.information_gain(y, splits)
        split_info = self.split_information(splits, len(y))

        if split_info == 0:
            return 0.0

        return gain / split_info

    def find_best_threshold_continuous(self, X_feature, y):
        """Find the best threshold for a continuous feature"""
        # Sort unique values
        unique_values = np.unique(X_feature)

        if len(unique_values) <= 1:
            return None, -1

        best_gain_ratio = -1
        best_threshold = None

        # Try thresholds between consecutive unique values
        for i in range(len(unique_values) - 1):
            threshold = (unique_values[i] + unique_values[i + 1]) / 2

            # Create binary splits
            left_indices = np.where(X_feature <= threshold)[0]
            right_indices = np.where(X_feature > threshold)[0]

            # Skip if split doesn't satisfy minimum samples per leaf
            if len(left_indices) < self.min_samples_leaf or len(right_indices) < self.min_samples_leaf:
                continue

            splits = [left_indices, right_indices]
            ratio = self.gain_ratio(y, splits)

            if ratio > best_gain_ratio:
                best_gain_ratio = ratio
                best_threshold = threshold

        return best_threshold, best_gain_ratio

    def find_best_split_categorical(self, X_feature, y):
        """Find the best multi-way split for a categorical feature"""
        unique_values = np.unique(X_feature)

        if len(unique_values) <= 1:
            return None, -1

        # Create multi-way split
        splits = []
        for value in unique_values:
            indices = np.where(X_feature == value)[0]
            if len(indices) >= self.min_samples_leaf:
                splits.append(indices)

        if len(splits) <= 1:
            return None, -1

        ratio = self.gain_ratio(y, splits)
        return unique_values, ratio

    def find_best_split(self, X, y):
        """Find the best attribute and split"""
        n_samples, n_features = X.shape

        best_gain_ratio = -1
        best_feature = None
        best_threshold = None
        best_values = None

        for feature in range(n_features):
            X_feature = X[:, feature]

            # Skip if all values are missing (NaN)
            if np.all(np.isnan(X_feature)):
                continue

            if self.continuous_features[feature]:
                # Handle continuous feature
                threshold, ratio = self.find_best_threshold_continuous(X_feature, y)

                if threshold is not None and ratio > best_gain_ratio:
                    best_gain_ratio = ratio
                    best_feature = feature
                    best_threshold = threshold
                    best_values = None
            else:
                # Handle categorical feature
                values, ratio = self.find_best_split_categorical(X_feature, y)

                if values is not None and ratio > best_gain_ratio:
                    best_gain_ratio = ratio
                    best_feature = feature
                    best_threshold = None
                    best_values = values

        return best_feature, best_threshold, best_values, best_gain_ratio

    def handle_missing_values(self, X):
        """Handle missing values using mean for continuous and mode for categorical"""
        X_filled = X.copy()

        for feature in range(X.shape[1]):
            feature_data = X[:, feature]
            missing_mask = np.isnan(feature_data)

            if np.any(missing_mask):
                if self.continuous_features[feature]:
                    # Use mean for continuous features
                    mean_value = np.nanmean(feature_data)
                    X_filled[missing_mask, feature] = mean_value
                else:
                    # Use mode for categorical features
                    non_missing = feature_data[~missing_mask]
                    if len(non_missing) > 0:
                        mode_value = Counter(non_missing).most_common(1)[0][0]
                        X_filled[missing_mask, feature] = mode_value

        return X_filled

    def build_tree(self, X, y, depth=0):
        """Recursively build the decision tree"""
        n_samples = len(y)

        # Create node
        node = C45Node()
        node.samples = n_samples
        node.class_counts = Counter(y)

        # Determine the most common class
        node.class_label = max(node.class_counts.items(), key=lambda x: x[1])[0]

        # Stopping criteria
        if (self.max_depth is not None and depth >= self.max_depth) or \
           (n_samples < self.min_samples_split) or \
           (len(np.unique(y)) == 1):  # Pure node
            node.is_leaf = True
            return node

        # Find best split
        best_feature, best_threshold, best_values, best_gain_ratio = self.find_best_split(X, y)

        # If no good split found or gain ratio too low, make it a leaf
        if best_feature is None or best_gain_ratio < self.min_gain_ratio:
            node.is_leaf = True
            return node

        # Apply the split
        node.attribute = best_feature
        node.threshold = best_threshold

        if self.continuous_features[best_feature]:
            # Binary split for continuous feature
            left_mask = X[:, best_feature] <= best_threshold
            right_mask = ~left_mask

            # Recursively build left and right subtrees
            if np.sum(left_mask) >= self.min_samples_leaf:
                node.branches['<='] = self.build_tree(X[left_mask], y[left_mask], depth + 1)
            if np.sum(right_mask) >= self.min_samples_leaf:
                node.branches['>'] = self.build_tree(X[right_mask], y[right_mask], depth + 1)
        else:
            # Multi-way split for categorical feature
            for value in best_values:
                mask = X[:, best_feature] == value
                if np.sum(mask) >= self.min_samples_leaf:
                    node.branches[value] = self.build_tree(X[mask], y[mask], depth + 1)

        # If no valid branches were created, make it a leaf
        if len(node.branches) == 0:
            node.is_leaf = True

        return node

    def fit(self, X, y, feature_names=None, continuous_features=None):
        """Train the C4.5 model"""
        if isinstance(X, pd.DataFrame):
            self.feature_names = X.columns.tolist()
            X = X.values
        else:
            self.feature_names = feature_names or [f"feature_{i}" for i in range(X.shape[1])]

        if isinstance(y, pd.Series):
            y = y.values

        # Determine feature types
        if continuous_features is None:
            # Auto-detect: assume numeric columns with > 10 unique values are continuous
            self.continuous_features = []
            for i in range(X.shape[1]):
                unique_vals = len(np.unique(X[~np.isnan(X[:, i]), i]))
                self.continuous_features.append(unique_vals > 10)
        else:
            self.continuous_features = continuous_features

        self.categorical_features = [not cont for cont in self.continuous_features]

        # Handle missing values
        X_processed = self.handle_missing_values(X)

        # Build tree
        self.root = self.build_tree(X_processed, y)
        return self

    def predict_sample(self, x, node):
        """Predict a single sample"""
        if node is None or node.is_leaf:
            return node.class_label if node else None

        feature_value = x[node.attribute]

        if self.continuous_features[node.attribute]:
            # Binary split for continuous feature
            if feature_value <= node.threshold:
                return self.predict_sample(x, node.branches.get('<='))
            else:
                return self.predict_sample(x, node.branches.get('>'))
        else:
            # Multi-way split for categorical feature
            return self.predict_sample(x, node.branches.get(feature_value))

    def predict(self, X):
        """Make predictions on new data"""
        if isinstance(X, pd.DataFrame):
            X = X.values

        # Handle missing values
        X_processed = self.handle_missing_values(X)

        predictions = []
        for x in X_processed:
            pred = self.predict_sample(x, self.root)
            predictions.append(pred)

        return np.array(predictions)

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

        if node.is_leaf:
            print(f"{indent}{prefix}: Leaf -> {node.class_label} (samples: {node.samples})")
        else:
            if node.threshold is not None:
                feature_name = self.feature_names[node.attribute] if self.feature_names else f"X[{node.attribute}]"
                print(f"{indent}{prefix}: {feature_name} <= {node.threshold:.3f} (samples: {node.samples})")
                if '<=' in node.branches:
                    self.print_tree(node.branches['<='], depth + 1, "True", max_depth)
                if '>' in node.branches:
                    self.print_tree(node.branches['>'], depth + 1, "False", max_depth)
            else:
                feature_name = self.feature_names[node.attribute] if self.feature_names else f"X[{node.attribute}]"
                print(f"{indent}{prefix}: {feature_name} (samples: {node.samples})")
                for value, child_node in node.branches.items():
                    self.print_tree(child_node, depth + 1, f"= {value}", max_depth)
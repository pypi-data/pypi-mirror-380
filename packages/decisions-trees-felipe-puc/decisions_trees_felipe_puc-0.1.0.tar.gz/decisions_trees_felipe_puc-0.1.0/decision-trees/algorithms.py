import pandas as pd
import numpy as np
from itertools import combinations
import json

def prepare_data(file_path, is_id3=False):
    """
    Carrega o dataset, trata valores ausentes e discretiza atributos contínuos
    se is_id3 for True.
    """
    df = pd.read_csv(file_path, on_bad_lines='skip', encoding='latin1')
    
    df.columns = [col.strip() for col in df.columns]
    
    df['Age'] = df['Age'].fillna(df['Age'].mean())
    df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
    
    df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1, inplace=True)
    
    if is_id3:
        bins_age = [0, 10, 20, 30, 40, 50, 60, 70, 100]
        labels_age = ['0-10', '11-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71+']
        df['Age'] = pd.cut(df['Age'], bins=bins_age, labels=labels_age)
        
        df['Fare'] = pd.qcut(df['Fare'], q=4, labels=['low', 'medium', 'high', 'very_high'])
        
        df['SibSp'] = df['SibSp'].apply(lambda x: '0' if x == 0 else '1+')
        df['Parch'] = df['Parch'].apply(lambda x: '0' if x == 0 else '1+')

    return df

# --- Funções de Impureza e Ganho ---

def entropy(target_col):
    elements, counts = np.unique(target_col, return_counts=True)
    total_elements = len(target_col)
    entropy_val = np.sum([(-counts[i]/total_elements) * np.log2(counts[i]/total_elements) for i in range(len(elements)) if counts[i] > 0])
    return entropy_val

def information_gain(data, split_attribute, target_name="Survived"):
    total_entropy = entropy(data[target_name])
    values, counts = np.unique(data[split_attribute], return_counts=True)
    weighted_entropy = np.sum([(counts[i]/np.sum(counts)) * entropy(data.where(data[split_attribute]==values[i]).dropna()[target_name]) for i in range(len(values))])
    gain = total_entropy - weighted_entropy
    return gain

def split_info(data, split_attribute):
    values, counts = np.unique(data[split_attribute], return_counts=True)
    total = len(data)
    split_info_val = np.sum([-(counts[i]/total) * np.log2(counts[i]/total) for i in range(len(values)) if counts[i] > 0])
    return split_info_val

def gain_ratio(data, split_attribute, target_name="Survived"):
    gain = information_gain(data, split_attribute, target_name)
    split_info_val = split_info(data, split_attribute)
    if split_info_val == 0:
        return 0
    return gain / split_info_val

def gini_index(target_col):
    elements, counts = np.unique(target_col, return_counts=True)
    total_elements = len(target_col)
    p_sq = np.sum([(counts[i]/total_elements)**2 for i in range(len(elements))])
    gini = 1 - p_sq
    return gini

def weighted_gini(subsets, target_name):
    total = sum([len(subset) for subset in subsets])
    weighted_gini_val = sum([(len(subset)/total) * gini_index(subset[target_name]) for subset in subsets if len(subset) > 0])
    return weighted_gini_val

# --- Implementação dos Algoritmos ---

def id3(data, original_data, features, target_attribute_name="Survived", parent_node_class=None, max_depth=None, current_depth=0):
    if max_depth is not None and current_depth >= max_depth:
        return int(np.unique(data[target_attribute_name])[np.argmax(np.unique(data[target_attribute_name], return_counts=True)[1])])
        
    unique_classes = np.unique(data[target_attribute_name])
    if len(unique_classes) <= 1:
        return int(unique_classes[0])
    
    elif len(features) == 0:
        return int(np.unique(original_data[target_attribute_name])[np.argmax(np.unique(original_data[target_attribute_name], return_counts=True)[1])])
    
    else:
        parent_node_class = int(np.unique(data[target_attribute_name])[np.argmax(np.unique(data[target_attribute_name], return_counts=True)[1])])
        item_gains = [information_gain(data, feature, target_attribute_name) for feature in features]
        best_feature_index = np.argmax(item_gains)
        best_feature = features[best_feature_index]
        tree = {str(best_feature): {}}
        features = [i for i in features if i != best_feature]
        
        for value in np.unique(data[best_feature]):
            if isinstance(value, np.integer):
                key_value = int(value)
            else:
                key_value = str(value)
            sub_data = data[data[best_feature] == value]
            
            if len(sub_data) == 0:
                tree[str(best_feature)][key_value] = parent_node_class
            else:
                subtree = id3(sub_data, original_data, features, target_attribute_name, parent_node_class, max_depth, current_depth + 1)
                tree[str(best_feature)][key_value] = subtree
        return tree

def c45_tree(data, original_data, features, target_attribute_name="Survived", parent_node_class=None, max_depth=None, current_depth=0):
    if max_depth is not None and current_depth >= max_depth:
        return int(np.unique(data[target_attribute_name])[np.argmax(np.unique(data[target_attribute_name], return_counts=True)[1])])
        
    if len(np.unique(data[target_attribute_name])) <= 1:
        return int(np.unique(data[target_attribute_name])[0])
    
    elif len(features) == 0:
        return int(np.unique(original_data[target_attribute_name])[np.argmax(np.unique(original_data[target_attribute_name], return_counts=True)[1])])
    
    else:
        parent_node_class = int(np.unique(data[target_attribute_name])[np.argmax(np.unique(data[target_attribute_name], return_counts=True)[1])])
        
        best_gain_ratio = -1
        best_feature = None
        best_threshold = None
        
        categorical_features = [f for f in features if data[f].dtype not in [np.float64, np.int64]]
        continuous_features = [f for f in features if data[f].dtype in [np.float64, np.int64]]

        for feature in categorical_features:
            current_gain_ratio = gain_ratio(data, feature, target_attribute_name)
            if current_gain_ratio > best_gain_ratio:
                best_gain_ratio = current_gain_ratio
                best_feature = feature
                best_threshold = None
        
        for feature in continuous_features:
            current_gain_ratio, threshold = find_best_split_for_continuous(data, feature, target_attribute_name)
            if current_gain_ratio is not None and current_gain_ratio > best_gain_ratio:
                best_gain_ratio = current_gain_ratio
                best_feature = feature
                best_threshold = threshold
        
        if best_feature is None:
            return parent_node_class

        tree = {str(best_feature): {}}
        remaining_features = [f for f in features if f != best_feature]

        if best_threshold is not None:
            left_subset = data[data[best_feature] <= best_threshold]
            right_subset = data[data[best_feature] > best_threshold]

            tree[str(best_feature)][f"<= {best_threshold:.2f}"] = c45_tree(left_subset, original_data, remaining_features, target_attribute_name, parent_node_class, max_depth, current_depth + 1)
            tree[str(best_feature)][f"> {best_threshold:.2f}"] = c45_tree(right_subset, original_data, remaining_features, target_attribute_name, parent_node_class, max_depth, current_depth + 1)
        else:
            for value in np.unique(data[best_feature]):
                sub_data = data[data[best_feature] == value]
                if len(sub_data) == 0:
                    tree[str(best_feature)][str(value)] = parent_node_class
                else:
                    subtree = c45_tree(sub_data, original_data, remaining_features, target_attribute_name, parent_node_class, max_depth, current_depth + 1)
                    tree[str(best_feature)][str(value)] = subtree

        return tree

def find_best_split_for_continuous_cart(data, attribute, target_name):
    unique_values = data[attribute].unique()
    unique_values.sort()
    
    best_threshold = None
    min_weighted_gini = 1
    
    for i in range(len(unique_values) - 1):
        threshold = (unique_values[i] + unique_values[i+1]) / 2
        
        subset_le = data[data[attribute] <= threshold]
        subset_gt = data[data[attribute] > threshold]
        
        if len(subset_le) == 0 or len(subset_gt) == 0:
            continue
        
        current_weighted_gini = weighted_gini([subset_le, subset_gt], target_name)
        
        if current_weighted_gini < min_weighted_gini:
            min_weighted_gini = current_weighted_gini
            best_threshold = threshold
            
    gain = gini_index(data[target_name]) - min_weighted_gini if min_weighted_gini < 1 else 0
    return gain, best_threshold

def find_best_split_for_categorical_cart(data, attribute, target_name):
    values = np.unique(data[attribute])
    if len(values) <= 1:
        return -1, None
    
    min_weighted_gini = 1
    best_split_set = None
    
    for k in range(1, len(values) // 2 + 1):
        for combo in combinations(values, k):
            subset1 = data[data[attribute].isin(list(combo))]
            subset2 = data[~data[attribute].isin(list(combo))]
            
            if len(subset1) == 0 or len(subset2) == 0:
                continue

            current_weighted_gini = weighted_gini([subset1, subset2], target_name)
            
            if current_weighted_gini < min_weighted_gini:
                min_weighted_gini = current_weighted_gini
                best_split_set = list(combo)
    
    gain = gini_index(data[target_name]) - min_weighted_gini if min_weighted_gini < 1 else 0
    return gain, best_split_set

def cart_tree(data, original_data, features, target_attribute_name="Survived", parent_node_class=None, max_depth=None, current_depth=0):
    if max_depth is not None and current_depth >= max_depth:
        return int(np.unique(data[target_attribute_name])[np.argmax(np.unique(data[target_attribute_name], return_counts=True)[1])])
        
    if len(data) == 0:
        return parent_node_class
        
    unique_classes = np.unique(data[target_attribute_name])
    if len(unique_classes) <= 1:
        return int(unique_classes[0])
    
    elif len(features) == 0:
        return int(np.unique(original_data[target_attribute_name])[np.argmax(np.unique(original_data[target_attribute_name], return_counts=True)[1])])
    
    else:
        parent_node_class = int(np.unique(data[target_attribute_name])[np.argmax(np.unique(data[target_attribute_name], return_counts=True)[1])])
        
        max_gini_gain = -1
        best_feature = None
        split_condition = None
        
        for feature in features:
            if data[feature].dtype in [np.float64, np.int64]:
                gain, threshold = find_best_split_for_continuous_cart(data, feature, target_attribute_name)
                if gain > max_gini_gain:
                    max_gini_gain = gain
                    best_feature = feature
                    split_condition = threshold
            else:
                gain, split_set = find_best_split_for_categorical_cart(data, feature, target_attribute_name)
                if gain > max_gini_gain:
                    max_gini_gain = gain
                    best_feature = feature
                    split_condition = split_set

        if best_feature is None or max_gini_gain == 0:
            return parent_node_class

        tree = {str(best_feature): {}}
        remaining_features = [f for f in features if f != best_feature]

        if isinstance(split_condition, list):
            subset1 = data[data[best_feature].isin(split_condition)]
            subset2 = data[~data[best_feature].isin(split_condition)]
            
            tree[str(best_feature)][f"isin({split_condition})"] = cart_tree(subset1, original_data, remaining_features, target_attribute_name, parent_node_class, max_depth, current_depth + 1)
            tree[str(best_feature)][f"not isin({split_condition})"] = cart_tree(subset2, original_data, remaining_features, target_attribute_name, parent_node_class, max_depth, current_depth + 1)
        else:
            subset1 = data[data[best_feature] <= split_condition]
            subset2 = data[data[best_feature] > split_condition]
            
            tree[str(best_feature)][f"<= {split_condition:.2f}"] = cart_tree(subset1, original_data, remaining_features, target_attribute_name, parent_node_class, max_depth, current_depth + 1)
            tree[str(best_feature)][f"> {split_condition:.2f}"] = cart_tree(subset2, original_data, remaining_features, target_attribute_name, parent_node_class, max_depth, current_depth + 1)

        return tree
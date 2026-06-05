"""
engUtl.py — Feature Engineering Utilities
Retail Sales Predictive Analytics Pipeline

Standalone encoding utilities used across the modeling notebooks.
"""

import pandas as pd


def targetEncode(df, feature, target):
    """
    Target encoding: replaces each category with the median of the target variable
    for that category. Useful for high-cardinality features.

    Args:
        df (pd.DataFrame): Input dataframe
        feature (str): Categorical column to encode
        target (str): Target column to compute median from

    Returns:
        pd.Series: Encoded column with median target values
    """
    medians = df.groupby(feature)[target].median()
    return df[feature].map(medians)


def labelEncode(df, feature):
    """
    Label encoding: assigns an integer code to each unique category value.
    Preserves ordinality implied by sort order.

    Args:
        df (pd.DataFrame): Input dataframe
        feature (str): Categorical column to encode

    Returns:
        pd.Series: Integer-encoded column
    """
    return df[feature].astype("category").cat.codes


def oneHotEncode(df, features):
    """
    One-hot encoding using pandas get_dummies. Drops the first category
    per feature to avoid multicollinearity.

    Args:
        df (pd.DataFrame): Input dataframe
        features (list): List of categorical columns to encode

    Returns:
        pd.DataFrame: Dataframe with original columns replaced by dummy columns
    """
    return pd.get_dummies(df, columns=features, drop_first=True)


if __name__ == "__main__":
    # Demonstrate encoding utilities on a small sample
    sample = pd.DataFrame({
        "category":   ["Electronics", "Beauty", "Electronics", "Clothing", "Beauty"],
        "region":     ["North", "South", "East", "North", "West"],
        "total_amount": [352.70, 285.11, 1346.12, 318.46, 331.73],
    })

    print("Original data:")
    print(sample.to_string(index=False))

    print("\nTarget-encoded 'category' (by median total_amount):")
    print(targetEncode(sample, "category", "total_amount").values)

    print("\nLabel-encoded 'region':")
    print(labelEncode(sample, "region").values)

    print("\nOne-hot encoded ['category', 'region']:")
    print(oneHotEncode(sample, ["category", "region"]).to_string(index=False))

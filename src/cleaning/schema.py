#Separates features (X) from response (y)


#returns all columns except target
TARGET_COLUMN = "Outcome"
def get_feature_columns(columns):
    """
    Given all column names, return predictor columns X
    by excluding the target.
    """
    return [c for c in columns if c != TARGET_COLUMN]
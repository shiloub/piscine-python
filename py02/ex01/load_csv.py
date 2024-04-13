import pandas as pd
import os


def load(path: str) -> pd.DataFrame:
    try:
        assert path.endswith(".csv")
        dataset = pd.read_csv(path)
        print(f"Loading dataset of dimensions {dataset.shape}")
        return dataset
    except (FileNotFoundError, AssertionError, PermissionError) as err:
        print("Error loading the file")
        return None
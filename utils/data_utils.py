import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_nav_data(file_path):
    """
    Load navigation data from a CSV file.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        pandas DataFrame: The loaded navigation data.
    """
    data = pd.read_csv(file_path)
    return data

def preprocess_nav_data(data):
    """
    Preprocess navigation data by scaling and normalizing the features.

    Args:
        data (pandas DataFrame): The navigation data to preprocess.

    Returns:
        pandas DataFrame: The preprocessed navigation data.
    """
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data.drop("target", axis=1))
    data_preprocessed = pd.DataFrame(data_scaled, columns=data.columns[:-1])
    data_preprocessed["target"] = data["target"]
    return data_preprocessed

def generate_synthetic_data(num_samples, num_features):
    """
    Generate synthetic data using a Gaussian mixture model.

    Args:
        num_samples (int): The number of samples to generate.
        num_features (int): The number of features to generate.

    Returns:
        pandas DataFrame: The generated synthetic data.
    """
    from sklearn.mixture import GaussianMixture
    gmm = GaussianMixture(n_components=3, covariance_type="full")
    data = gmm.sample(num_samples)[0]
    data = pd.DataFrame(data, columns=[f"feature_{i}" for i in range(num_features)])
    return data

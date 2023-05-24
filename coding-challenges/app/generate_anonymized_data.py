import pandas as pd
from faker import Faker
import hashlib
import json

def load_config(file_path):
    """
    Load configuration from a JSON file.

    Args:
        file_path (str): Path to the JSON configuration file.

    Returns:
        dict: Configuration loaded from the JSON file.
    """
    with open(file_path) as json_file:
        config = json.load(json_file)
    return config


def generate_data(config):
    """
    Generate synthetic data based on the provided configuration.

    Args:
        config (dict): Configuration dictionary containing information about the columns and data types.

    Returns:
        pd.DataFrame: Generated data as a Pandas DataFrame.
    """
    fake = Faker()
    df = pd.DataFrame()
    for column, dtype in config['columns_list'].items():
        if dtype == 'first_name()':
            data = [fake.first_name() for _ in range(config['N'])]
        elif dtype == 'last_name()':
            data = [fake.last_name() for _ in range(config['N'])]
        elif dtype == 'address()':
            data = [fake.address().replace('\n', ', ') for _ in range(config['N'])]
        elif dtype == 'date_of_birth()':
            data = [fake.date_of_birth(minimum_age=18, maximum_age=99).strftime('%Y-%m-%d') for _ in
                    range(config['N'])]
        else:
            raise ValueError(f"Invalid dtype '{dtype}' for column '{column}'")
        df[column] = data

    generated_output_file = config.get('generated_output_file')
    if generated_output_file:
        df.to_csv(generated_output_file, index=False)

    return df


def write_to_file(df, file_path):
    """
    Write DataFrame to a CSV file.

    Args:
        df (pd.DataFrame): DataFrame to be written.
        file_path (str): Path to the output CSV file.
    """
    df.to_csv(file_path, index=False)


def anonymize_series(series):
    """
    Anonymize a series by hashing the values using SHA256.

    Args:
        series (pd.Series): Series to be anonymized.

    Returns:
        pd.Series: Anonymized series with hashed values.
    """
    return series.apply(lambda x: hashlib.sha256(x.encode()).hexdigest())


def anonymize_data(config_file):
    """
    Anonymize data based on the provided configuration.

    Args:
        config_file (str): Path to the JSON configuration file.
    """
    try:
        # Load configuration
        with open(config_file) as f:
            config = json.load(f)

        # Generate data
        df = generate_data(config)

        # Anonymize columns based on config
        anonymize_columns_list = config.get('anonymize_columns_list', [])
        for column in anonymize_columns_list:
            if column in df.columns:
                df[column] = anonymize_series(df[column])
            else:
                raise ValueError(f'Column "{column}" not found in dataframe.')

        # Write anonymized data back to CSV
        anonymized_output_file = config.get('anonymized_output_file')
        if anonymized_output_file:
            df.to_csv(anonymized_output_file, index=False)
            print(f"Data anonymized and saved to '{anonymized_output_file}'.")
        else:
            print("Anonymized data is not saved as 'anonymized_output_file' is not specified in the config.")
    except Exception as e:
        print("An error occurred while anonymizing data.")
        print(str(e))

def main():
    """
    Main function to execute the data generation and anonymization process.
    """
    config = load_config('config.json')
    df = generate_data(config)
    write_to_file(df, config['generated_output_file'])
    anonymize_data('config.json')


if __name__ == "__main__":
    main()

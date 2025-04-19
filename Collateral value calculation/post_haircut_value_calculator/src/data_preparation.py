def prepare_data(csv_file_path):
    import pandas as pd
    import os

    # Read the CSV file
    data = pd.read_csv(csv_file_path)

    # Normalize column names (strip whitespace and convert to lowercase)
    data.columns = data.columns.str.strip().str.lower()

    # Define the required columns in lowercase
    required_columns = ['s.no', 'stock name', 'isin', 'last traded price', 'haircut percentage']
    if not all(column in data.columns for column in required_columns):
        raise ValueError(f"The input CSV file must contain the following columns: {', '.join(required_columns)}")

    # Process the data to extract relevant columns
    processed_data = data[['stock name', 'last traded price', 'haircut percentage']]

    # Convert Haircut Percentage to decimal
    processed_data['haircut percentage'] = processed_data['haircut percentage'] / 100

    # Assume a default stock quantity of 1000
    stock_quantity = 1000

    # Calculate the post-haircut value
    processed_data['post haircut value'] = (
        processed_data['last traded price'] * (1 - processed_data['haircut percentage']) * stock_quantity
    )

    # Ensure the 'data' directory exists
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, '..', 'data')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Save the processed data as a new CSV file
    processed_csv_path = os.path.join(output_dir, 'processed_data.csv')
    processed_data.to_csv(processed_csv_path, index=False)

    return processed_csv_path
import pandas as pd
import os

def get_stock_name_and_quantity(processed_csv_path):
    """
    Handles user input for stock name and quantity by referring to the processed data file.

    Args:
        processed_csv_path (str): Path to the processed data CSV file.

    Returns:
        tuple: Stock name and quantity entered by the user.
    """
    try:
        # Load the processed data
        processed_data = pd.read_csv(processed_csv_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"Processed data file not found at {processed_csv_path}. Please ensure the data preparation step is completed.")

    # Display available stock names
    print("\nAvailable stock names:")
    print(processed_data['stock name'].tolist())  # Use normalized column name

    # Get user input for stock name
    while True:
        stock_name = input("Enter the stock name (from the list above): ").strip()
        if stock_name in processed_data['stock name'].values:  # Use normalized column name
            break
        print("Invalid stock name. Please enter a valid stock name from the list.")

    # Get user input for quantity
    while True:
        try:
            quantity = int(input("Enter the quantity of stocks: "))
            if quantity > 0:
                break
            else:
                print("Quantity must be a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer for quantity.")

    return stock_name, quantity
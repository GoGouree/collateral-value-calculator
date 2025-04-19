import pandas as pd
from data_preparation import prepare_data
from user_input import get_stock_name_and_quantity
from notification import generate_notification  # Import the notification function

def main():
    # Step 1: Data Preparation
    print("Please provide the path to your raw CSV file (e.g., 'data/sample_data.csv').")
    csv_file_path = input("Enter the path to the CSV file: ").strip()
    try:
        # Prepare data and calculate post-haircut value for 1000 shares
        processed_csv_path = prepare_data(csv_file_path)
        print(f"Data processed successfully. The processed file is saved at: {processed_csv_path}")
    except FileNotFoundError:
        print(f"Error: The file at '{csv_file_path}' was not found. Please check the path and try again.")
        return
    except ValueError as e:
        print(f"Error: {e}")
        return

    # Step 2: Get user input for specific stock and quantity
    try:
        stock_name, quantity = get_stock_name_and_quantity(processed_csv_path)
    except FileNotFoundError as e:
        print(e)
        return

    # Step 3: Generate notification
    try:
        # Load the processed data
        stock_data = pd.read_csv(processed_csv_path)
    except FileNotFoundError:
        print("Error: Processed data file not found. Please ensure the data preparation step completed successfully.")
        return

    # Find the stock details
    stock_info = stock_data[stock_data['stock name'] == stock_name].iloc[0]  # Use normalized column name
    last_traded_price = stock_info['last traded price']  # Use normalized column name
    haircut_percentage = stock_info['haircut percentage']  # Use normalized column name
    post_haircut_value = last_traded_price * (1 - haircut_percentage / 100) * quantity

    # Generate the notification
    notification = generate_notification(stock_name, quantity, post_haircut_value)
    print("\n" + notification)

if __name__ == "__main__":
    main()
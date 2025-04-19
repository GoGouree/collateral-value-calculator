# Post Haircut Value Calculator

This project calculates the post-haircut value of securities based on the last traded price and haircut percentage. It processes all stocks with a default quantity of 1000 and allows users to specify a particular stock and quantity for a detailed notification report.

## Usage

1. **Prepare your CSV file**  
   Ensure your CSV file contains the required data format (stock names, last traded prices, haircut percentages). Save the file in the `data` folder as `sample_data.csv`. This can be a data sourcing directly to remove the manual step to save the CSV file.

2. **Run the application**  
   - **Command-line mode**:  
     Execute the following command to run the application in command-line mode:
     ```bash
     post-haircut-value-calculator
     ```
   - **Front-end mode**:  
     To use the front-end UI, start the Flask server by running:
     ```bash
     flask run
     ```
     Then, open your browser and navigate to the provided URL (usually `http://127.0.0.1:5000`) to interact with the application visually..

3. **Front-end UI**  
   A front-end UI has been created, allowing users to interact with the application visually. To generate the Flask and HTML files, a PNG file was used as a sample design and dragged into the GitHub chat window, where the necessary code was generated.

4. **Process all stocks**  
   The application will process all stocks in the file with a default quantity of 1000 and display the post-haircut values and save the file output in the data folder. This helps reuse the Excel further in other processes also.

5. **Generate a notification for a specific stock**  
   - Select a stock name from the processed data list displayed by the application.  
   - Enter the stock name and desired quantity when prompted.  
   - The application will prepare a notification report for the selected stock.

## Module Descriptions

- **`main.py`**: Orchestrates the execution of the application.
- **`data_preparation.py`**: Reads and processes the CSV file to extract necessary data. Contains the logic to compute the post-haircut value.
- **`user_input.py`**: Handles user input for stock selection and quantity.
- **`notification.py`**: Formats the output for report/notification messages.

## Sample Data

The `data/sample_data.csv` file should contain the following columns:
- **Stock Name**
- **Last Traded Price**
- **Haircut Percentage**

# Post Haircut Value Calculator

This project calculates the post-haircut value of securities based on the last traded price and haircut percentage. It processes all stocks with a default quantity of 1000 and allows users to specify a particular stock and quantity for a detailed notification report.

## Usage

1. **Prepare your CSV file**  
   Ensure your CSV file contains the required data format (stock names, last traded prices, haircut percentages). Save the file in the `data` folder as `sample_data.csv`. This can be a data sourcing directly to remove the manual step to save csv file.

2. **Run the application**  
   Execute the following command to run the application:
   ```bash
   post-haircut-value-calculator
   ```

3. **Front-end UI**  
   A front-end UI has been created, allowing users to interact with the application visually. The UI was generated using a PNG file as an example to design the interface and generate the necessary code. 

4. **Process all stocks**  
   The application will process all stocks in the file with a default quantity of 1000 and display the post-haircut values and save the file output in the data folder. This helps reuse the excel further in other processes also.

5. **Generate a notification for a specific stock**  
   - Select a stock name from the processed data list displayed by the application.  
   - Enter the stock name and desired quantity when prompted.  
   - The application will prepare a notification report for the selected stock.

## Publishing to Heroku

To publish the application to Heroku, follow these high-level steps:
1. Ensure your application has a `Procfile` specifying the entry point for the app.
2. Install the Heroku CLI and log in to your Heroku account.
3. Create a new Heroku app using the CLI:
   ```bash
   heroku create <app-name>
   ```
4. Push your code to Heroku:
   ```bash
   git push heroku main
   ```
5. Set up any required environment variables using the Heroku dashboard or CLI.
6. Open the app in your browser:
   ```bash
   heroku open
   ```

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

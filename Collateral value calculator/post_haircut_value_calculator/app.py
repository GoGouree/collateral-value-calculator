from flask import Flask, render_template, request, send_file
import pandas as pd
import os

app = Flask(__name__)

# Path to the processed data file
PROCESSED_DATA_PATH = os.path.join("data", "processed_data.csv")

@app.route("/")
def index():
    # Load the processed data
    if os.path.exists(PROCESSED_DATA_PATH):
        data = pd.read_csv(PROCESSED_DATA_PATH)
    else:
        # Empty table if file doesn't exist
        data = pd.DataFrame(columns=["stock name", "last traded price", "haircut percentage", "post haircut value"])

    # Convert data to a list of dictionaries for rendering in the template on the front end UI 
    securities = data.to_dict(orient="records")
    return render_template("index.html", securities=securities)

@app.route("/download")
def download():
    # Serve the processed data file for download
    if os.path.exists(PROCESSED_DATA_PATH):
        return send_file(PROCESSED_DATA_PATH, as_attachment=True)
    else:
        return "Processed data file not found.", 404

if __name__ == "__main__":
    app.run(debug=True)
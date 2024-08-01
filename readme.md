# GHG Protocol Emissions Calculator

## Overview

This project is a Greenhouse Gas (GHG) Protocol emissions calculator built using Python and Flask. It allows users to input emission factors and activity data to calculate total GHG emissions. The web-based interface provides an easy and interactive way to perform these calculations.

## Features

- **Emissions Calculation**: Calculate GHG emissions based on activity data and emission factors.
- **Web Dashboard**: User-friendly web interface for inputting data and viewing results.
- **Modular Code**: Easily extendable and customizable Python scripts.

## Installation

Follow these steps to set up and run the project locally on your machine:

### Prerequisites

- Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Steps

1. **Clone the Repository**

   ```bash
   git clone git@github.com:anthonynoronha/ghg-protocol-calculator.git
   cd ghg-protocol-calculator
   ```

2. **Create a Virtual Environment (Optional but Recommended)**

   ```bash
   python -m venv ghg_calculator_env
   source ghg_calculator_env/bin/activate  # On Windows use `ghg_calculator_env\Scripts\activate`
   ```

3. **Install Required Libraries**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask Application**

   ```bash
   python app.py
   ```

5. **Access the Web Dashboard**

   Open your web browser and navigate to `http://127.0.0.1:5000/`.

## Usage

### Web Interface

1. Open the web dashboard in your browser.
2. Enter the amount of activity (e.g., kWh) in the provided input field.
3. Enter the emission factor (e.g., kg CO2 per kWh) in the provided input field.
4. Click the "Calculate" button to view the total GHG emissions.

### Python Script

You can also use the calculator directly via the command line:

```bash
python ghg_calculator.py
```

Follow the prompts to enter the activity data and emission factor.

## Project Structure

```
|-- ghg_calculator.py        # Python script for GHG emissions calculation
|-- app.py                   # Flask application script
|-- templates/               # HTML templates for the web interface
|   |-- index.html           # Home page template
|   |-- result.html          # Result page template
|-- requirements.txt         # List of required Python libraries
|-- README.md                # Project documentation
```

## Contributing

Contributions are welcome! If you have suggestions for improvements or find any issues, please create an issue or submit a pull request. Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a pull request.



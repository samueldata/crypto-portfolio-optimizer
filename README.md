# Crypto Portfolio Optimizer

The **Crypto Portfolio Optimizer** is a project designed to optimize cryptocurrency portfolios based on historical returns. It applies the Efficient Frontier technique to maximize the Sharpe Ratio. The application uses Streamlit to provide an interactive interface for users.

## Project Structure

```bash
crypto-portfolio-optimizer/
│
├── data/                          # Raw and processed data
│   ├── raw/                       # Raw historical data of cryptocurrencies
│   └── processed/                 # Data prepared for analysis
│
├── notebooks/                     # Jupyter Notebooks for experimentation
│
├── src/                           # Project source code
│   ├── data/                      # Scripts for data collection and processing
│   ├── optimization/              # Portfolio optimization logic
│   └── interface/                 # Code for the interface (Streamlit)
│
├── tests/                         # Automated test scripts
│
├── venv/                          # Python virtual environment
│
├── .gitignore                     # Gitignore file
├── README.md                      # Project documentation
└── requirements.txt               # Project dependencies
```

### Directory Overview

- **data/**: Contains data used in the project.
  - **raw/**: Stores raw cryptocurrency data for analysis.
  - **processed/**: Contains cleaned and processed data ready for analysis.
- **notebooks/**: Jupyter notebooks used for exploration, analysis, and algorithm development.
- **src/**: All source code for the project.
  - **data/**: Scripts to collect, clean, and process cryptocurrency data.
  - **optimization/**: Portfolio optimization logic, including Efficient Frontier calculation algorithms.
  - **interface/**: Streamlit code for the user interface.
- **tests/**: Automated test scripts to ensure proper functionality.
- **venv/**: Python virtual environment to isolate project dependencies.
- **.gitignore**: Specifies which files and directories to ignore in Git.
- **README.md**: Project documentation (this file).
- **requirements.txt**: Lists all the dependencies and libraries required to run the project.

## Prerequisites

- **Python 3.8+**: Make sure you have Python installed.
- **Streamlit**: Used to create the interactive web interface.
- **PyPortfolioOpt**: A library for portfolio optimization.

## Installation

1. Clone the repository to your local environment:

```bash
git clone https://github.com/samueldata/crypto-portfolio-optimizer.git
cd crypto-portfolio-optimizer
```

1. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate   # For Linux/macOS
venv\Scripts\activate      # For Windows
```

1. Install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### 1. Data Collection

Before running the interface, make sure cryptocurrency data is available. Run the appropriate script to collect the data or manually add the necessary files to the `data/raw/` folder and process them.

### 2. Running the Interface

Launch the Streamlit app using the following command:

```bash
streamlit run src/interface/app.py
```

This will open the interface in your default browser, where you can select data and optimize your portfolio.

### 3. Running Tests

To run the automated tests, execute:

```bash
pytest tests/
```

## Features

- Portfolio optimization using Efficient Frontier.
- Maximizes Sharpe Ratio for cryptocurrency portfolios.
- Simple and intuitive graphical interface built with Streamlit.

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Open a Pull Request.
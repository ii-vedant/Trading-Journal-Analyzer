# 📊 Trading Journal Analyzer (CLI-Based)

A comprehensive command-line Trading Journal built using Python that allows traders to record, analyze, and visualize their trading performance.

This project is designed to simulate a real-world trading analytics system by combining data storage, performance metrics, and visualization tools to improve trading discipline and decision-making.

---

## 🚀 Features

### 📌 Trade Management
- Add new trades with:
  - Trade Type (Buy/Sell)
  - Entry Price
  - Exit Price
  - Quantity
  - Automatically calculated Profit/Loss
- Store all trades persistently in a CSV file
- Maintain structured and clean trade records
### 🎨 Enhanced CLI Output
- Colored terminal output:
  - 🟢 Profit shown in green
  - 🔴 Loss shown in red
- Improves readability and quick analysis

---

### 🔍 Advanced Trade Filtering
- Filter trades based on:
  - Instrument (e.g., Nifty, BankNifty, Gold)
- Helps analyze performance per asset

---

### 📊 Risk Management Metrics
- Risk-Reward Ratio calculation
- Helps evaluate trade quality
- Encourages better trading decisions

---

### 📉 Drawdown Analysis
- Tracks peak-to-loss decline
- Helps understand risk exposure
- Useful for improving trading psychology

---

### 📈 Performance Analytics
- Total Profit / Loss calculation
- Win Rate (%)
- Number of Winning Trades
- Number of Losing Trades
- Trade-wise performance tracking

---

### 📜 Trade History
- View complete history of all trades
- Clean and readable CLI output
- Helps in reviewing past decisions

---

### 📊 Data Analysis (Pandas)
- Efficient data handling using Pandas DataFrames
- Aggregation of trade data
- Performance metric calculations
- Structured data processing

---

### 📉 Data Visualization (Matplotlib)
- Visual representation of trading performance
- Helps identify patterns and trends
- Graph-based analysis of results

---

### 💾 Data Persistence
- CSV-based storage system
- Automatic file creation if not present
- Data retained between program runs

---

### ⚡ CLI Menu-Based Interface
- User-friendly command-line interface
- Menu-driven navigation
- Easy interaction for adding/viewing/analyzing trades

---

### 🧩 Modular Code Structure
- Clean separation of logic:
  - `main.py` → main program flow
  - `utils.py` → helper functions and calculations
- Improves maintainability and scalability

---

### 🛡️ Error Handling & Validation
- Input validation for user entries
- Handles invalid data gracefully
- Prevents runtime crashes

---

## 🧠 Concepts Used

- Python Functions
- Modular Programming
- File Handling (Read/Write CSV)
- Data Analysis using Pandas
- Data Visualization using Matplotlib
- CLI-based Application Design
- Exception Handling
- Aggregation Logic (Win/Loss calculations)

---

## 🔄 Example Workflow

1. User selects an option from the CLI menu  
2. Inputs trade details  
3. Trade is saved into CSV file  
4. Data is loaded and processed using Pandas  
5. Calculations performed:
   - Profit/Loss
   - Win Rate
   - Trade statistics  
6. Visualization generated using Matplotlib  
7. Results displayed to the user  

---

## 🛠️ Technologies & Libraries

- **Python 3.x**
- **Pandas** (Data Analysis)
- **Matplotlib** (Data Visualization)
- **CSV** (Data Storage)
- Built-in Libraries:
  - `os`
  - `csv`

---

## 📂 Project Structure
Trading-Journal-Analyser/
│
├── main.py # Main CLI application
├── utils.py # Helper functions & calculations
├── trades.csv # Trade data (auto-generated)
├── requirements.txt # Project dependencies
├── .gitignore # Ignored files
└── README.md # Documentation


---

## ▶️ How to Run

### 1. Clone the repository
git clone https://github.com/ii-vedant/trading-journal-analyser.git
### 2. Navigate to the project folder
cd trading-journal-analyser

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run the application
python main.py
## 🔥 Future Scope

- 🖥️ Convert CLI application into a GUI using Tkinter or PyQt
- 🌐 Build a web-based version using Flask or Django
- 🗄️ Replace CSV storage with a database (SQLite / PostgreSQL)
- 📊 Advanced analytics dashboard (interactive charts)
- 📅 Date-wise filtering and performance tracking
- 📈 Equity curve visualization
- 📉 Maximum drawdown visualization (graph-based)
- 📤 Export reports (PDF / Excel)
- 🔔 Add trade notes and journaling features (psychology tracking)
- 🤖 AI-based trade insights and suggestions

## 📚 What I Learned

- Built a complete CLI-based application from scratch using Python  
- Gained hands-on experience in file handling using CSV for data storage  
- Learned how to structure a project using modular programming (separating logic into different files)  

- Developed data analysis skills using Pandas:
  - Handling structured data
  - Performing aggregations and calculations
  - Extracting meaningful insights from trading data  

- Implemented data visualization using Matplotlib:
  - Representing trading performance graphically
  - Understanding trends and patterns  

- Understood key trading performance metrics:
  - Profit & Loss calculation  
  - Win Rate  
  - Risk-Reward Ratio  
  - Drawdown Analysis  

- Improved problem-solving and logical thinking by building real-world features  
- Learned how to manage and track projects using Git and GitHub  
- Gained experience in building user-friendly CLI interfaces  


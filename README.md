# Superstore Sales Data Analysis

This project provides a comprehensive analysis of the "Superstore" dataset using Python and prepares the data for advanced visualization in Power BI.

## 📁 Project Structure

```text
├── dataset/             # Raw and cleaned CSV files
├── powerbi/             # Power BI dashboard files
├── python-analysis/      # Data cleaning and exploratory analysis scripts
├── screenshots/          # Exported visualizations from the analysis
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- [Power BI Desktop](https://powerbi.microsoft.com/desktop/) (optional, for viewing dashboards)

### Installation

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd future_interns_task1
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows (PowerShell):
   .\venv\Scripts\Activate.ps1
   # On Windows (cmd):
   .\venv\Scripts\activate.bat
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Analysis

To perform data cleaning and generate visualizations:
```bash
python python-analysis/analysis.py
```

This will:
- Clean the raw `superstore.csv`.
- Save the results as `cleaned_superstore.csv`.
- Export charts to the `screenshots/` folder.

## 📊 Visualizations
The analysis generates the following insights:
- **Yearly Sales Trend**: Tracking growth over time.
- **Top 10 Selling Products**: Identifying high-performing items.
- **Sales by Region**: Geographical distribution of revenue.

## 🛠 Tools Used
- **Python**: (Pandas, Matplotlib) for data processing and EDA.
- **Power BI**: For building interactive dashboards.
- **Visual Studio Code**: Integrated development environment.

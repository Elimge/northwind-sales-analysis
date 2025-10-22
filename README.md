# Northwind Sales Analysis Project

This project performs a comprehensive sales analysis of the Northwind dataset, a sample database representing a small trading company. The primary goal is to extract, transform, and visualize sales data to derive key business insights and Key Performance Indicators (KPIs).

The analysis is conducted in a structured project environment, leveraging industry-standard tools like Python, Pandas, SQLAlchemy, and PostgreSQL.

## Project Objective

The main objective is to answer critical business questions by analyzing customer, order, and product data. The project follows a step-by-step process covering:
1.  **Data Integration:** Combining data from multiple tables (`customers`, `orders`, `products`, etc.).
2.  **KPI Calculation:** Computing metrics like gross profit, profit margins, and shipping times.
3.  **Data Aggregation:** Grouping data to identify trends and segments (e.g., by month, city, category).
4.  **Statistical Analysis:** Calculating the Coefficient of Variation to understand customer spending behavior.
5.  **Data Visualization:** Creating charts to communicate findings effectively.

## Key Insights Derived

- **Profitability Trends:** Monthly profit analysis reveals a significant upward trend, peaking in the first quarter of 1998.
- **Geographic Performance:** The analysis identifies the most and least profitable cities, with **Cunewalde** showing the highest total profit and **Walla Walla** the lowest (non-zero) profit.
- **Customer Spending Behavior:** The Coefficient of Variation (CV) for customer spending is **~1.42**, which is greater than 1. This indicates a high variability in spending habits, suggesting a diverse customer base with both low-spending and high-spending segments.
- **Category Performance:** The project visualizes the profit margins and total profit by product category, highlighting the most and least lucrative segments.

## Project Structure

The repository is organized following a standard data analysis project structure:
``` bash
.
├── notebooks/
│   └── 01_analysis.ipynb     # Main Jupyter Notebook with the step-by-step analysis.
├── src/
│   ├── config/
│   │   └── northwind.sql     # The DDL and DML script to set up the database.
│   └── db/
│       ├── __init__.py
│       ├── database.py       # SQLAlchemy engine and connection module.
│       └── setup_database.py # Script to initialize and populate the database.
├── .env                      # Environment variables for database credentials (ignored by Git).
├── .gitignore                # Specifies files to be ignored by Git.
├── README.md                 # This project overview.
└── requirements.txt          # Python dependencies for the project.
```

## Technologies & Libraries Used

- **Language:** Python
- **Database:** PostgreSQL
- **Database Toolkit:** SQLAlchemy
- **Data Manipulation:** Pandas
- **Visualization:** Matplotlib & Seaborn
- **Environment Management:** `python-dotenv`, `venv`

## How to Run This Project

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/Elimge/northwind-sales-analysis.git
    cd northwind-sales-analysis
    ```

2.  **Set Up Environment:**
    - Create a virtual environment: `python -m venv .venv`
    - Activate it: `source .venv/bin/activate` (Mac/Linux) or `.venv\Scripts\activate` (Windows).
    - Install dependencies: `pip install -r requirements.txt`

3.  **Configure Database Credentials:**
    - Create a `.env` file in the project root.
    - Add your PostgreSQL connection details to the `.env` file:
      ```
      DB_NAME=northwind_db
      DB_USER=your_user
      DB_PASSWORD=your_password
      DB_HOST=localhost
      DB_PORT=5432
      ```

4.  **Set Up the Database:**
    - Ensure your PostgreSQL server is running.
    - Run the setup script to create and populate the `northwind_db` database:
      ```bash
      python src/db/setup_database.py
      ```

5.  **Run the Analysis:**
    - Open the Jupyter Notebook `notebooks/01_analysis.ipynb` in VS Code or Jupyter Lab.
    - Execute the cells sequentially to see the full analysis.
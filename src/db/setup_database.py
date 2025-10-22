# src/db/setup_database.py

import os 
from sqlalchemy import text
from src.db.database import get_engine

def setup_database():
    """
    Prepare the database by creating necessary tables and inserting initial data.
    """

    # Path to the SQL script file
    sql_file_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'northwind.sql')

    # Get the database engine
    engine = get_engine()
    if engine is None:
        print("Failed to get database engine. Exiting setup.")
        return
    
    try:
        print("Reading SQL script...")
        with open(sql_file_path, 'r', encoding='utf-8') as file:
            sql_script = file.read()

        # Using a pool connection to execute the script
        with engine.connect() as conn:
            print("Executing SQL script to continue database setup...")

            # Transactional execution of the script
            with conn.begin():
                conn.execute(text(sql_script))

        print("Database setup completed successfully.")

    except Exception as e:
        print(f"An error occurred during database setup: {e}")

    finally:
        # Dispose the engine to free up resources
        if engine:
            engine.dispose()
            print("Database engine disposed.")

if __name__ == "__main__":
    print("Starting database setup...")
    setup_database()

    
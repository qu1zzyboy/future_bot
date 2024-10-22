import pandas as pd
import numpy as np
import os
import glob
import sqlite3

class DB:
    def __init__(self):
        current_dictionary=os.path.abspath(os.getcwd())
        print(current_dictionary)
        file_path=os.path.join(current_dictionary,"binance_data")
        self.files_path=glob.glob(os.path.join(file_path,"*.csv"))
        self.db_path="wld.db"
    def db_init(self):
        dfs=[]
        for file in sorted(self.files_path):
            print(f"loading {file}")
            df=pd.read_csv(file)
            dfs.append(df)
        combined_db=pd.concat(dfs,ignore_index=True)
        
        return combined_db

    def setup_database(self):
        """Create SQLite database and table"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Create table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS price_data (
            open_time TIMESTAMP PRIMARY KEY,
            open REAL,
            high REAL,
            low REAL,
            close REAL,
            volume REAL,
            close_time TIMESTAMP,
            quote_volume REAL,
            count INTEGER,
            taker_buy_volume REAL,
            taker_buy_quote_volume REAL,
            ignore INTEGER
        )
        ''')
        
        conn.commit()
        return conn
    def load_to_database(self, df):
        """Load DataFrame into SQLite database"""
        conn = self.setup_database()
        
        # Convert DataFrame to SQL
        df.to_sql('price_data', conn, if_exists='replace', index=False)
        
        print(f"Data loaded to database: {self.db_path}")
        conn.close()


database=DB()
database.setup_database()
database.load_to_database(database.db_init())
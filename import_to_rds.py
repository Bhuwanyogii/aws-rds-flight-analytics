import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

# Load variables from .env
load_dotenv()

# Read CSV
df = pd.read_csv(r"D:\Flights_sql_app\flights.csv")

# Get RDS password from .env
password = os.getenv("MYSQL_PASSWORD")

if not password:
    raise ValueError("MYSQL_PASSWORD was not found in .env")

# Create database connection
connection_url = URL.create(
    drivername="mysql+pymysql",
    username="admin",
    password=password,
    host="bhuwan-mysql.cp8gaok8090x.ap-southeast-2.rds.amazonaws.com",
    port=3306,
    database="flights"
)

engine = create_engine(connection_url)

print("Connected to AWS RDS successfully!")
print(f"Rows to upload: {len(df)}")

# Upload complete CSV to MySQL
df.to_sql(
    name="flights",
    con=engine,
    if_exists="replace",
    index=False,
    chunksize=500
)

print("Data imported successfully!")
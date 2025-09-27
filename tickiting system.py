"""
Ticket Sales Loader & Analyzer
Beginner-friendly Python program
Steps:
1. Connect to MySQL
2. Load ticket sales CSV data into the database
3. Query and display popular tickets (top-selling events)
"""

import mysql.connector
import csv
from datetime import datetime

# -------------------------------
# Step 1. Setup database connection
# -------------------------------
def create_connection():
    try:
        connection = mysql.connector.connect(
            host="Local instance MySQL80",      
            port=3306,              
            user="Hontos",          
            password="123456",   
            database="ticketdb"
        )
        print("✅ Connection successful")
        return connection
    except mysql.connector.Error as e:
        print(f"❌ Error connecting to MySQL: {e}")
        return None


# -------------------------------
# Step 2. Load CSV into the table
# -------------------------------
def load_csv_to_table(connection, csv_file):
    cursor = connection.cursor()

    # Create the sales table if it does not exist
    create_table_query = """
    CREATE TABLE IF NOT EXISTS sales (
        ticket_id INT AUTO_INCREMENT PRIMARY KEY,
        trans_date DATE,
        event_id INT,
        event_name VARCHAR(50),
        event_date DATE,
        event_type VARCHAR(10),
        event_city VARCHAR(20),
        customer_id INT,
        price DECIMAL(10,2),
        num_tickets INT
    );
    """
    cursor.execute(create_table_query)

    # Open the CSV file and insert each row
    with open(csv_file, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            insert_query = """
            INSERT INTO sales
            (trans_date, event_id, event_name, event_date, event_type, event_city,
             customer_id, price, num_tickets)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            data = (
                row["trans_date"],
                row["event_id"],
                row["event_name"],
                row["event_date"],
                row["event_type"],
                row["event_city"],
                row["customer_id"],
                row["price"],
                row["num_tickets"]
            )
            cursor.execute(insert_query, data)

    connection.commit()
    print("✅ CSV data loaded into sales table")
    cursor.close()


# -------------------------------
# Step 3. Query and analyze
# -------------------------------
def query_popular_tickets(connection):
    cursor = connection.cursor()

    # SQL to find the most popular event in the past month
    sql_statement = """
    SELECT event_name, SUM(num_tickets) as total_tickets
    FROM sales
    WHERE trans_date >= DATE_SUB(CURDATE(), INTERVAL 1 MONTH)
    GROUP BY event_name
    ORDER BY total_tickets DESC
    LIMIT 5;
    """
    cursor.execute(sql_statement)
    records = cursor.fetchall()
    cursor.close()
    return records


def display_results(records):
    print("\n Top-Selling Events in the Past Month")
    for idx, (event_name, total_tickets) in enumerate(records, start=1):
        print(f"{idx}. {event_name} - {total_tickets} tickets sold")


# -------------------------------
# Main Program
# -------------------------------
if __name__ == "__main__":
    conn = create_connection()
    if conn:
        # Step 2: load CSV into table (replace with your CSV file path)
        load_csv_to_table(conn, "ticket_sales.csv")

        # Step 3: query & display
        results = query_popular_tickets(conn)
        display_results(results)

        conn.close()

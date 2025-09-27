===========================================
 Ticket Sales Loader & Analyzer - README
===========================================

DESCRIPTION
-----------
This program is a beginner-friendly Python tool for managing and analyzing
ticket sales data. It connects to a MySQL database, loads sales records
from a CSV file, and displays the most popular (top-selling) events 
from the last month.

FUNCTIONALITY
-------------
1. Connects to a MySQL database called "ticketdb".
2. Creates a "sales" table if it doesn’t already exist.
3. Loads ticket sales data from a CSV file (default: ticket_sales.csv).
4. Runs a query to find the top 5 events (by number of tickets sold) 
   in the past month.
5. Displays the results in the console.

REQUIREMENTS
------------
- Python 3.x
- MySQL Server installed and running
- MySQL user account with access to "ticketdb"
- Required Python libraries:
    - mysql-connector-python
    - csv (standard library)
    - datetime (standard library)

INSTALLATION
------------
1. Install Python 3 if not already installed.
2. Install MySQL Server and create a database named "ticketdb".
3. Install the MySQL Python connector by running:
       pip install mysql-connector-python
4. Place your ticket sales CSV file (e.g., ticket_sales.csv) in the
   same directory as the Python script.
   The CSV should have the following columns:
   trans_date, event_id, event_name, event_date, event_type, 
   event_city, customer_id, price, num_tickets

HOW TO RUN
----------
1. Open a terminal (Command Prompt or PowerShell on Windows).
2. Navigate to the folder containing "tickiting system.py".
3. Run the script:
       python "tickiting system.py"
4. The program will:
   - Connect to MySQL
   - Load data from ticket_sales.csv into the "sales" table
   - Display the top-selling events for the past month

NOTES
-----
- Update the database connection details in `create_connection()` if needed:
      host, user, password, database
- If you want to analyze a different CSV file, change the filename
  in the main program section:
      load_csv_to_table(conn, "ticket_sales.csv")
- Make sure your CSV data matches the expected columns.

-------------------------------------------
Enjoy analyzing your ticket sales data! 🎟️
-------------------------------------------

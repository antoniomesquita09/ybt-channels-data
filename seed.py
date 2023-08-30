import pandas as pd
import psycopg2
import uuid


def insert_csv_to_database(csv_file, host, port, user, password, database, table_name):
    # Load CSV data into a DataFrame
    try:
        df = pd.read_csv(csv_file)
    except FileNotFoundError:
        print("CSV file not found.")
        return
    
    # Replace empty cells with None
    df = df.where(pd.notna(df), None)
    
    # Establish a connection to the database
    try:
        conn = psycopg2.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )
        cursor = conn.cursor()
    except psycopg2.Error as err:
        print("Error while connecting to the database:", err)
        return
    
    # Create a SQL query to insert data with a random UUID
    query = f"INSERT INTO {table_name} (id, {', '.join(df.columns)}) VALUES (%s, {'%s, ' * (len(df.columns) - 1)}%s)"
    
    # Insert each row from the DataFrame into the database
    for row in df.itertuples(index=False):
        row_data = [str(uuid.uuid4())] + list(row)
        try:
            cursor.execute(query, row_data)
            conn.commit()  # Commit after each successful insert
        except psycopg2.Error as err:
            print("SQL Error:", err)
    
    # Close the connection
    conn.close()
    
    print("Data inserted into the database.")


if __name__ == "__main__":
    csv_filename = "output.csv"  # Replace with your CSV file name
    db_host = "localhost"
    db_user = "ytbchannels"  # Replace with your MySQL username
    db_password = "postgres"  # Replace with your MySQL password
    db_name = "ytbchannels"  # Replace with your MySQL database name
    table_name = "channels"  # Replace with your table name
    port = 5432
    
    insert_csv_to_database(csv_filename, db_host, port, db_user, db_password, db_name, table_name)

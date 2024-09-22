import psycopg2
import os

def update_db():
    # Get DB connection details from environment variables
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT'),
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD')
    )
    cursor = conn.cursor()

    # Example SQL query to update the database
    cursor.execute("UPDATE your_table SET column_name = 'new_value' WHERE condition_column = 'condition_value';")

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    update_db()

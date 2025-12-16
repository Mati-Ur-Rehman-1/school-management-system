import psycopg2

def connection():
    return psycopg2.connect(
    host="localhost",
    port=5432,
    database="student",
    user="postgres",
    password="root"
)

def create_table():
    conn = connection()
    cur = conn.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS students (
        roll_no VARCHAR(20) PRIMARY KEY,
        name VARCHAR(50),
        f_name VARCHAR(50),
        class_name VARCHAR(20)
    )
    """

    cur.execute(create_table_query) #we can also directly create table in cur.execute()

    # Step 5: save changes
    conn.commit()

    print("Table created successfully!")

    cur.close()
    conn.close()

create_table()





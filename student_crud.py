import psycopg2

DB_NAME = "postgres"
DB_USER = "postgres.hrdkoosvgmuwyexvqzjt"
DB_PASSWORD = "Shw3chchh4@"
DB_HOST = "aws-0-ap-southeast-1.pooler.supabase.com"
DB_PORT = "5432"

def db_connection():
    try:
        conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
        print("Connection successful")
        return conn
    except Exception as e:
        print("Error connecting to database:", e)
        return None

def create_table():
    conn = db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS teacher (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                age INT NOT NULL
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS departments (
                id SERIAL PRIMARY KEY,
                course_name VARCHAR(100) NOT NULL,
                credits INT NOT NULL,
                teacher_id INT REFERENCES teacher(id)
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS subjects1 (
                id SERIAL PRIMARY KEY,
                subject_name VARCHAR(100) NOT NULL,
                credits INT NOT NULL
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS enrollments (
                enrollment_id SERIAL PRIMARY KEY,
                course_id INT REFERENCES departments(id),
                subject_id INT REFERENCES subjects1(id)
            );
        """)
        conn.commit()
        cursor.close()
        conn.close()
        print("Tables created")

def insert_departments(course_name, credits, teacher_id):
    conn = db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO departments (course_name, credits, teacher_id)
            VALUES (%s, %s, %s)
        """, (course_name, credits, teacher_id))
        conn.commit()
        cursor.close()
        conn.close()
        print(f"Department '{course_name}' inserted.")

def insert_subject(subject_name, credits):
    conn = db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO subjects1 (subject_name, credits)
            VALUES (%s, %s)
        """, (subject_name, credits))
        conn.commit()
        cursor.close()
        conn.close()
        print(f"Subject '{subject_name}' inserted.")

def insert_teacher(name, age):
    conn = db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO teacher (name, age)
            VALUES (%s, %s)
        """, (name, age))
        conn.commit()
        cursor.close()
        conn.close()
        print(f"Teacher '{name}' inserted.")

def insert_enrollments(course_id, subject_id):
    conn = db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO enrollments (course_id, subject_id)
            VALUES (%s, %s)
        """, (course_id, subject_id))
        conn.commit()
        cursor.close()
        conn.close()
        print("Enrollment data inserted.")

if __name__ == "__main__":
    create_table()

    insert_departments("chemistry", 3, 2)
    insert_departments("Algebra", 3, 4)


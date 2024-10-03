import sqlite3


class Database:
    def __init__(self, db_name='users.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                family TEXT,
                age INTEGER,
                email TEXT
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS teachers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                family TEXT,
                age INTEGER,
                email TEXT
            )
        ''')
        self.conn.commit()

    def insert_student(self, student):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO students (name, family, age, email) VALUES (?, ?, ?, ?)
        ''', (student.name, student.family, student.age, student.email))
        self.conn.commit()

    def insert_teacher(self, teacher):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO teachers (name, family, age, email) VALUES (?, ?, ?, ?)
        ''', (teacher.name, teacher.family, teacher.age, teacher.email))
        self.conn.commit()

    def get_students(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT name, family, age, email FROM students')
        return cursor.fetchall()

    def get_teachers(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT name, family, age, email FROM teachers')
        return cursor.fetchall()

    def close(self):
        self.conn.close()

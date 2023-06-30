import psycopg2
from decouple import config


def init_db() -> None:
    conn = psycopg2.connect(
        host=config('HOST'),
        database=config('DB'),
        user=config('USER'),
        password=config('PASSWORD'))
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS users ('
                'id SERIAL PRIMARY KEY,'
                'telegram_id INT UNIQUE,'
                'full_name VARCHAR(255) NOT NULL,'
                'token TEXT UNIQUE,'
                'department VARCHAR(255),'
                'is_admin BOOLEAN NOT NULL DEFAULT true);'
                
                'CREATE TABLE IF NOT EXISTS activity_categories ('
                'id SERIAL PRIMARY KEY,'
                'name VARCHAR(255) NOT NULL,'
                'points FLOAT NOT NULL CHECK (points > 0));'
                
                'CREATE TABLE IF NOT EXISTS activity ('
                'id SERIAL PRIMARY KEY,'
                'name VARCHAR(255) NOT NULL,'
                'category_id INT REFERENCES activity_categories(id),'
                'user_id INT REFERENCES users(id),'
                'points FLOAT CHECK (points > 0));'
                
                'CREATE TABLE IF NOT EXISTS sponsors ('
                'id SERIAL PRIMARY KEY,'
                'instagram VARCHAR(255),'
                'phone_number VARCHAR(255),'
                'department_added VARCHAR(255),'
                'user_added INT REFERENCES users(id),'
                'date_added DATE NOT NULL);')
    conn.commit()
    cur.close()
    conn.close()

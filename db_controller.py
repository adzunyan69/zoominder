import sqlite3

DB_PATH = 'zoominder.db'

class db_api:
    def create_database(selft):
        db = sqlite3.connect(DB_PATH)
        if db is not None:
            db.execute(
                """
                CREATE TABLE user(id, full_name)
                """
            )
        
    def add_user(selft, id, full_name):
        db = sqlite3.connect(DB_PATH)
        if db is not None:
            db.execute(
                f"""
                INSERT INTO user (id, full_name) VALUES (\'{id}\', \'{full_name}\')                
                """
            )
            
    def get_user_name(selft, id):
        db = sqlite3.connect(DB_PATH)
        if db is not None:
            return db.execute(f"SELECT full_name FROM user WHERE id = \'{id}\'").fetchall()
        
        return None

    def clear(selft, db):
        if db is not None:
            db.execute('DROP TABLE user')
        
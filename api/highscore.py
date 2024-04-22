import sqlite3

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return None

def create_table(conn):
    """Create a high scores table."""
    try:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS high_scores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                game TEXT NOT NULL,
                score INTEGER NOT NULL
            )
        """)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def save_high_score(conn, name, game, score):
    """Save a high score entry to the database."""
    try:
        c = conn.cursor()
        c.execute("""
            INSERT INTO high_scores (name, game, score)
            VALUES (?, ?, ?)
        """, (name, game, score))
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def get_high_scores(conn):
    """Retrieve high scores from the database."""
    try:
        c = conn.cursor()
        c.execute("""
            SELECT name, game, score
            FROM high_scores
            ORDER BY score DESC
        """)
        return c.fetchall()
    except sqlite3.Error as e:
        print(e)

def main():
    database = "highscores.db"
    conn = create_connection(database)
    if conn is not None:
        create_table(conn)
    else:
        print("Error! Cannot create the database connection.")

if __name__ == "__main__":
    main()

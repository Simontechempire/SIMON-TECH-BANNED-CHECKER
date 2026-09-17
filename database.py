import sqlite3

DB_NAME = "simon_checker.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            first_name TEXT,
            joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS checks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            phone TEXT,
            country TEXT,
            status TEXT,
            checked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def add_user(user_id, username, first_name):
    conn = sqlite3.connect(DB_NAME)

    conn.execute(
        """
        INSERT OR IGNORE INTO users
        (user_id, username, first_name)
        VALUES (?, ?, ?)
        """,
        (user_id, username, first_name)
    )

    conn.commit()
    conn.close()


def save_check(user_id, phone, country, status):
    conn = sqlite3.connect(DB_NAME)

    conn.execute(
        """
        INSERT INTO checks
        (user_id, phone, country, status)
        VALUES (?, ?, ?, ?)
        """,
        (user_id, phone, country, status)
    )

    conn.commit()
    conn.close()


def get_history(user_id, limit=10):
    conn = sqlite3.connect(DB_NAME)

    cursor = conn.execute(
        """
        SELECT phone, country, status, checked_at
        FROM checks
        WHERE user_id = ?
        ORDER BY id DESC
        LIMIT ?
        """,
        (user_id, limit)
    )

    results = cursor.fetchall()
    conn.close()

    return results

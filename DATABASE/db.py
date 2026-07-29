import sqlite3
from pathlib import Path
import sys


# Project Root Configuration
PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from config import DATABASE_PATH


# DATABASE CONNECTION


def get_connection():
    """
    Creates and returns a SQLite connection.

    Foreign key constraints are enabled for every connection.
    """

    try:
        conn = sqlite3.connect(DATABASE_PATH)
        conn.execute("PRAGMA foreign_keys = ON;")
        return conn

    except sqlite3.Error as e:
        print(f"Database Connection Error: {e}")
        return None



# CREATE TABLES


def create_tables():
    conn = get_connection()

    if conn is None:
        return

    try:
        with conn:
            cursor = conn.cursor()

            
            # USERS
         

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE,
                    full_name TEXT,
                    email TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    last_login TIMESTAMP
                )
            """)

            
            # CONVERSATIONS

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS conversations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    title TEXT NOT NULL,
                    status TEXT DEFAULT 'active',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

                    FOREIGN KEY(user_id)
                    REFERENCES users(id)
                    ON DELETE CASCADE
                )
            """)

            # MESSAGES

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS messages (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    conversation_id INTEGER NOT NULL,
                    role TEXT NOT NULL,
                    message TEXT NOT NULL,
                    token_count INTEGER DEFAULT 0,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

                    FOREIGN KEY(conversation_id)
                    REFERENCES conversations(id)
                    ON DELETE CASCADE
                )
            """)

            # NOTES

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS notes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    title TEXT NOT NULL,
                    content TEXT NOT NULL,
                    category TEXT DEFAULT 'General',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

                    FOREIGN KEY(user_id)
                    REFERENCES users(id)
                    ON DELETE CASCADE
                )
            """)

            # REMINDERS

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS reminders (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    task TEXT NOT NULL,
                    reminder_date TEXT NOT NULL,
                    reminder_time TEXT NOT NULL,
                    status TEXT DEFAULT 'Pending',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

                    FOREIGN KEY(user_id)
                    REFERENCES users(id)
                    ON DELETE CASCADE
                )
            """)

            # ==================================================
            # MEMORIES
            # ==================================================

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS memories (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    memory TEXT NOT NULL,
                    category TEXT DEFAULT 'General',
                    importance INTEGER DEFAULT 1,
                    source TEXT DEFAULT 'manual',
                    last_accessed TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

                    FOREIGN KEY(user_id)
                    REFERENCES users(id)
                    ON DELETE CASCADE
                )
            """)

            # INDEXES

            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_notes_user
                ON notes(user_id)
            """)

            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_reminders_user
                ON reminders(user_id)
            """)

            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_memories_user
                ON memories(user_id)
            """)

            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_conversations_user
                ON conversations(user_id)
            """)

            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_messages_conversation
                ON messages(conversation_id)
            """)

            print("All tables initialized successfully.")

    except sqlite3.Error as e:
        print(f"Table Creation Error: {e}")

    finally:
        conn.close()


# INITIALIZE DATABASE

if __name__ == "__main__":
    create_tables()
from DATABASE.db import get_connection


def create_note(user_id, title, content, category="General"):
    conn = get_connection()

    if conn is None:
        return None

    try:
        with conn:
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO notes
                (user_id, title, content, category)
                VALUES
                (:user_id, :title, :content, :category)
            """, {
                "user_id": user_id,
                "title": title,
                "content": content,
                "category": category
            })

            return cursor.lastrowid

    except Exception as e:
        print(f"Error creating note: {e}")
        return None

    finally:
        conn.close()


def get_all_notes(user_id):
    conn = get_connection()

    if conn is None:
        return []

    try:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM notes
            WHERE user_id = :user_id
            ORDER BY updated_at DESC
        """, {"user_id": user_id})

        return cursor.fetchall()

    except Exception as e:
        print(f"Error retrieving notes: {e}")
        return []

    finally:
        conn.close()


def get_note_by_id(note_id):
    conn = get_connection()

    if conn is None:
        return None

    try:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM notes
            WHERE id = :id
        """, {"id": note_id})

        return cursor.fetchone()

    except Exception as e:
        print(f"Error retrieving note: {e}")
        return None

    finally:
        conn.close()


def search_notes(user_id, keyword):
    conn = get_connection()

    if conn is None:
        return []

    try:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM notes
            WHERE user_id = :user_id
            AND (
                    LOWER(title) LIKE LOWER(:keyword)
                    OR LOWER(content) LIKE LOWER(:keyword)
                    OR LOWER(category) LIKE LOWER(:keyword)
            )
            ORDER BY updated_at DESC
        """, {
            "user_id": user_id,
            "keyword": f"%{keyword}%"
        })

        return cursor.fetchall()

    except Exception as e:
        print(f"Error searching notes: {e}")
        return []

    finally:
        conn.close()


def get_note_by_title(user_id, title):
    conn = get_connection()

    if conn is None:
        return None

    try:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM notes
            WHERE user_id = :user_id
            AND LOWER(title) = LOWER(:title)
            LIMIT 1
        """, {
            "user_id": user_id,
            "title": title
        })

        return cursor.fetchone()

    except Exception as e:
        print(f"Error retrieving note by title: {e}")
        return None

    finally:
        conn.close()


def update_note(note_id, title, content, category):
    conn = get_connection()

    if conn is None:
        return False

    try:
        with conn:
            cursor = conn.cursor()

            cursor.execute("""
                UPDATE notes
                SET
                    title = :title,
                    content = :content,
                    category = :category,
                    updated_at = CURRENT_TIMESTAMP
                WHERE id = :id
            """, {
                "title": title,
                "content": content,
                "category": category,
                "id": note_id
            })

            return cursor.rowcount > 0

    except Exception as e:
        print(f"Error updating note: {e}")
        return False

    finally:
        conn.close()


def delete_note(note_id):
    conn = get_connection()

    if conn is None:
        return False

    try:
        with conn:
            cursor = conn.cursor()

            cursor.execute("""
                DELETE FROM notes
                WHERE id = :id
            """, {"id": note_id})

            return cursor.rowcount > 0

    except Exception as e:
        print(f"Error deleting note: {e}")
        return False

    finally:
        conn.close()
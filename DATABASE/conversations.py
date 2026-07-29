from DATABASE.db import get_connection


def create_conversation(user_id, title):
    conn = get_connection()

    if conn is None:
        return None

    try:
        with conn:
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO conversations
                (user_id, title)
                VALUES
                (:user_id, :title)
            """, {
                "user_id": user_id,
                "title": title
            })

            return cursor.lastrowid

    except Exception as e:
        print(f"Error creating conversation: {e}")
        return None

    finally:
        conn.close()


def get_all_conversations(user_id):
    conn = get_connection()

    if conn is None:
        return []

    try:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM conversations
            WHERE user_id = :user_id
            ORDER BY updated_at DESC
        """, {
            "user_id": user_id
        })

        return cursor.fetchall()

    except Exception as e:
        print(f"Error retrieving conversations: {e}")
        return []

    finally:
        conn.close()


def get_conversation_by_id(conversation_id):
    conn = get_connection()

    if conn is None:
        return None

    try:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM conversations
            WHERE id = :id
        """, {
            "id": conversation_id
        })

        return cursor.fetchone()

    except Exception as e:
        print(f"Error retrieving conversation: {e}")
        return None

    finally:
        conn.close()


def update_conversation_title(conversation_id, title):
    conn = get_connection()

    if conn is None:
        return False

    try:
        with conn:
            cursor = conn.cursor()

            cursor.execute("""
                UPDATE conversations
                SET
                    title = :title,
                    updated_at = CURRENT_TIMESTAMP
                WHERE id = :id
            """, {
                "title": title,
                "id": conversation_id
            })

            return cursor.rowcount > 0

    except Exception as e:
        print(f"Error updating conversation title: {e}")
        return False

    finally:
        conn.close()


def update_conversation_status(conversation_id, status):
    conn = get_connection()

    if conn is None:
        return False

    try:
        with conn:
            cursor = conn.cursor()

            cursor.execute("""
                UPDATE conversations
                SET
                    status = :status,
                    updated_at = CURRENT_TIMESTAMP
                WHERE id = :id
            """, {
                "status": status,
                "id": conversation_id
            })

            return cursor.rowcount > 0

    except Exception as e:
        print(f"Error updating conversation status: {e}")
        return False

    finally:
        conn.close()


def delete_conversation(conversation_id):
    conn = get_connection()

    if conn is None:
        return False

    try:
        with conn:
            cursor = conn.cursor()

            cursor.execute("""
                DELETE FROM conversations
                WHERE id = :id
            """, {
                "id": conversation_id
            })

            return cursor.rowcount > 0

    except Exception as e:
        print(f"Error deleting conversation: {e}")
        return False

    finally:
        conn.close()
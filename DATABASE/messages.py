from DATABASE.db import get_connection


def create_message(conversation_id, role, message, token_count=0):
    conn = get_connection()

    if conn is None:
        return None

    try:
        with conn:
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO messages
                (conversation_id, role, message, token_count)
                VALUES
                (:conversation_id, :role, :message, :token_count)
            """, {
                "conversation_id": conversation_id,
                "role": role,
                "message": message,
                "token_count": token_count
            })

            return cursor.lastrowid

    except Exception as e:
        print(f"Error creating message: {e}")
        return None

    finally:
        conn.close()


def get_messages(conversation_id):
    conn = get_connection()

    if conn is None:
        return []

    try:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM messages
            WHERE conversation_id = :conversation_id
            ORDER BY timestamp ASC
        """, {
            "conversation_id": conversation_id
        })

        return cursor.fetchall()

    except Exception as e:
        print(f"Error retrieving messages: {e}")
        return []

    finally:
        conn.close()


def get_message_by_id(message_id):
    conn = get_connection()

    if conn is None:
        return None

    try:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM messages
            WHERE id = :id
        """, {
            "id": message_id
        })

        return cursor.fetchone()

    except Exception as e:
        print(f"Error retrieving message: {e}")
        return None

    finally:
        conn.close()


def update_message(message_id, message):
    conn = get_connection()

    if conn is None:
        return False

    try:
        with conn:
            cursor = conn.cursor()

            cursor.execute("""
                UPDATE messages
                SET
                    message = :message
                WHERE id = :id
            """, {
                "message": message,
                "id": message_id
            })

            return cursor.rowcount > 0

    except Exception as e:
        print(f"Error updating message: {e}")
        return False

    finally:
        conn.close()


def delete_message(message_id):
    conn = get_connection()

    if conn is None:
        return False

    try:
        with conn:
            cursor = conn.cursor()

            cursor.execute("""
                DELETE FROM messages
                WHERE id = :id
            """, {
                "id": message_id
            })

            return cursor.rowcount > 0

    except Exception as e:
        print(f"Error deleting message: {e}")
        return False

    finally:
        conn.close()


def delete_conversation_messages(conversation_id):
    conn = get_connection()

    if conn is None:
        return False

    try:
        with conn:
            cursor = conn.cursor()

            cursor.execute("""
                DELETE FROM messages
                WHERE conversation_id = :conversation_id
            """, {
                "conversation_id": conversation_id
            })

            return cursor.rowcount >= 0

    except Exception as e:
        print(f"Error deleting conversation messages: {e}")
        return False

    finally:
        conn.close()
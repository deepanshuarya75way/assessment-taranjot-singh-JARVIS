from DATABASE.db import get_connection


def create_memory(user_id, memory, category="General", importance=1, source="manual"):
    conn = get_connection()

    if conn is None:
        return None

    try:
        with conn:
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO memories
                (user_id, memory, category, importance, source)
                VALUES
                (:user_id, :memory, :category, :importance, :source)
            """, {
                "user_id": user_id,
                "memory": memory,
                "category": category,
                "importance": importance,
                "source": source
            })

            return cursor.lastrowid

    except Exception as e:
        print(f"Error creating memory: {e}")
        return None

    finally:
        conn.close()


def get_all_memories(user_id):
    conn = get_connection()

    if conn is None:
        return []

    try:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM memories
            WHERE user_id = :user_id
            ORDER BY importance DESC, created_at DESC
        """, {
            "user_id": user_id
        })

        return cursor.fetchall()

    except Exception as e:
        print(f"Error retrieving memories: {e}")
        return []

    finally:
        conn.close()


def get_memory_by_id(memory_id):
    conn = get_connection()

    if conn is None:
        return None

    try:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM memories
            WHERE id = :id
        """, {
            "id": memory_id
        })

        return cursor.fetchone()

    except Exception as e:
        print(f"Error retrieving memory: {e}")
        return None

    finally:
        conn.close()


def get_memories_by_category(user_id, category):
    conn = get_connection()

    if conn is None:
        return []

    try:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM memories
            WHERE
                user_id = :user_id
                AND category = :category
            ORDER BY importance DESC
        """, {
            "user_id": user_id,
            "category": category
        })

        return cursor.fetchall()

    except Exception as e:
        print(f"Error retrieving memories by category: {e}")
        return []

    finally:
        conn.close()


def update_memory(memory_id, memory, category, importance):
    conn = get_connection()

    if conn is None:
        return False

    try:
        with conn:
            cursor = conn.cursor()

            cursor.execute("""
                UPDATE memories
                SET
                    memory = :memory,
                    category = :category,
                    importance = :importance,
                    last_accessed = CURRENT_TIMESTAMP
                WHERE id = :id
            """, {
                "memory": memory,
                "category": category,
                "importance": importance,
                "id": memory_id
            })

            return cursor.rowcount > 0

    except Exception as e:
        print(f"Error updating memory: {e}")
        return False

    finally:
        conn.close()


def update_last_accessed(memory_id):
    conn = get_connection()

    if conn is None:
        return False

    try:
        with conn:
            cursor = conn.cursor()

            cursor.execute("""
                UPDATE memories
                SET
                    last_accessed = CURRENT_TIMESTAMP
                WHERE id = :id
            """, {
                "id": memory_id
            })

            return cursor.rowcount > 0

    except Exception as e:
        print(f"Error updating last accessed: {e}")
        return False

    finally:
        conn.close()


def delete_memory(memory_id):
    conn = get_connection()

    if conn is None:
        return False

    try:
        with conn:
            cursor = conn.cursor()

            cursor.execute("""
                DELETE FROM memories
                WHERE id = :id
            """, {
                "id": memory_id
            })

            return cursor.rowcount > 0

    except Exception as e:
        print(f"Error deleting memory: {e}")
        return False

    finally:
        conn.close()
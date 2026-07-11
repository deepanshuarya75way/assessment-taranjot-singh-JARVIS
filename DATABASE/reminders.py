from DATABASE.db import get_connection

def create_reinder(user_id,task,reminder_date,reminder_time):
    conn = get_connection()

    if conn is None:
        return None
    
    try:
        with conn:
            cursor = conn.cursor()

            cursor.execute(
                "INSERT INTO reminders(user_id,task,reminder_date,reminder_time) VALUES(:user_id,:task,:reminder_date,:reminder_time)",
                {"user_id":user_id,"task":task,"reminder_date":reminder_date,"reminder_time":reminder_time}
            )

            return cursor.lastrowid

    except Exception as e:
        print(f"Error creating reminder: {e}")
        return False
    
    finally:
        conn.close()

def update_reminder_date(user_id,updated_date):
    conn = get_connection()

    if conn is None:
        return False
    
    try:
        with conn:
            cursor = conn.cursor()

            cursor.execute(
                "UPDATE reminders SET reminder_date = :updated_reminder WHERE id=:id",
                {"updated_reminder":updated_date,"id":user_id}
            )
            return cursor.rowcount>0


    except Exception as e:
        print(f"Error updating the date: {e}")
        return False

    finally:
        conn.close()

def update_reminder_time(user_id,updated_time):
    conn = get_connection()

    if conn is None:
        return False
    
    try:
        with conn:
            cursor = conn.cursor()

            cursor.execute(
                "UPDATE reminders SET reminder_time = :updated_reminder WHERE id=:id",
                {"updated_reminder":updated_time,"id":user_id}
            )

            return cursor.rowcount>0
        

    except Exception as e:
        print(f"Error updating the time: {e}")
        return False

    finally:
        conn.close()


def update_status(user_id,updated_status):
    conn = get_connection()

    if conn is None:
        return False
    
    try:
        with conn:
            cursor = conn.cursor()

            cursor.execute(
                "UPDATE reminders SET status = :updated_status WHERE id=:id",
                {"updated_status":updated_status,"id":user_id}
            )

            return cursor.rowcount>0
        

    except Exception as e:
        print(f"Error updating the status: {e}")
        return False

    finally:
        conn.close()

def get_reminders_by_date(user_id,reminder_date):
    conn = get_connection()

    if conn is None:
        return False

    try:
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM remindrs WHERE user_id = :id AND reminder_date = :reminder",
                {"id":user_id,"reminder":reminder_date}
            )

            dates = cursor.fetchall()
            return dates
    
    except Exception as e:
        print(f"Error retrieving dates: {e}")
        return False
    
    finally:
        conn.close()


def get_reminders_by_time(user_id,reminder_time):
    conn = get_connection()

    if conn is None:
        return False

    try:
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM remindrs WHERE user_id = :id AND reminder_time = :reminder",
                {"id":user_id,"reminder":reminder_time}
            )

            time = cursor.fetchall()
            return time
    
    except Exception as e:
        print(f"Error retrieving time: {e}")
        return False
    
    finally:
        conn.close()

def get_all_reminders(user_id):
    conn = get_connection()

    if conn is None:
        return False
    
    try:
        with conn:
            cursor = conn.cursor()

            cursor.execute(
                "SELECT * FROM reminders WHERE user_id = :id",
                {"id":user_id}
            )
            reminders = cursor.fetchall()
            return reminders
    
    except Exception as e:
        print(f"Error retreiving the reminders: {e}")
        return False
    
    finally:
        conn.close()

def delete_reminder(user_id):
    conn = get_connection()
    if conn is None:
        return False

    try:
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM reminders WHERE user_id= :user_id",
                {"user_id":user_id}
            )
            return cursor.rowcount > 0
    except Exception as e:
        print(f"Error deleting the reminder: {e}")
        return False
    
    finally:
        conn.close()
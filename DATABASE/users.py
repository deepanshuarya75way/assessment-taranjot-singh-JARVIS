from DATABASE.db import get_connection


def create_user(username, email, password):
    conn = get_connection()

    if conn is None:
        return False

    try:
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO users (username, email, password) VALUES (:name,:email,:password)",
                {"name":username,"email":email,"password":password}
            )
        return cursor.lastrowid

    except Exception as e:
        print(f"Error creating user: {e}")
        return False

    finally:
        conn.close()

def get_user_by_id(user_id):
    conn = get_connection()

    if conn is None:
        return None

    try:
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM users WHERE id = :id",
                {"id":user_id}
            )

            user = cursor.fetchone()
            return user

    except Exception as e:
        print(f"Error retrieving user with ID {user_id}: {e}")
        return None

    finally:
        conn.close()

        
def get_user_by_username(username):
    conn = get_connection()

    if conn is None:
        return None
    
    try:
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM users WHERE username = :username",
                {"username":username}
            )
            user = cursor.fetchone()
            return user

    except Exception as e:
        print(f"Error retrieving user with username {username}: {e}")
        return None
    
    finally:
        conn.close()

def get_user_by_email(email):
    conn = get_connection()

    if conn is None:
        return None

    try:
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM users WHERE email = :email",
                {"email": email}
            )

            user = cursor.fetchone()
            return user

    except Exception as e:
        print(f"Error retrieving user with email {email}: {e}")
        return None

    finally:
        conn.close()

def get_all_users():

    conn = get_connection()

    if conn is None:
        return None

    
    try:
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM users"
            )
            users = cursor.fetchall()
            return users
        
    except Exception as e:
        print(f"Error retrieving all users: {e}")
        return None
    
    finally:
        conn.close()

def update_username(user_id,username):

    conn = get_connection()

    if conn is None:
        return None
    
    try:
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE users SET username= :username WHERE id = :id",
                {"username":username,"id": user_id}
            )
            return cursor.rowcount > 0
            
    except Exception as e:
        print(f"Error updating username: {e}")
        return False
    
    finally:
        conn.close()

def update_email(user_id,email):
    conn = get_connection()
    if conn is None:
        return False

    try:
        with conn:
            cursor = conn.cursor() 
            cursor.execute(
                "UPDATE users SET email= :email WHERE id = :id ",
                {"email": email,"id": user_id}
            )

            return cursor.rowcount > 0
    except Exception as e:
        print(f"Error updating email: {e}")
        return False
    finally:
        conn.close()

def update_password(user_id,password):
    conn = get_connection()
    if conn is None:
        return False
    
    try:
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE users SET password =:password WHERE id = :id",
                {"password":password,"id":user_id}
            )

            return cursor.rowcount>0
    except Exception as e:
        print(f"Error updating password: {e}")
        return False
    finally:
        conn.close()

def delete_user(user_id):
   conn = get_connection()

   if conn is None:
       return False
   try:
       with conn:
           cursor = conn.cursor()
           cursor.execute(
               "DELETE FROM users WHERE id = :id",
               {"id":user_id}
           )

           return cursor.rowcount > 0
    
   except Exception as e:
       print(f"Error deleting the user: {e}")
       return False
   
   finally:
       conn.close()
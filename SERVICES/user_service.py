from DATABASE.users import (
    create_user,
    get_user_by_username,
    get_user_by_email,
)


# VALIDATION

def validate_username(username):
    username = username.strip()

    if not username:
        return False, "Username cannot be empty."

    if len(username) < 3:
        return False, "Username must be at least 3 characters long."

    existing_user = get_user_by_username(username)

    if existing_user is not None:
        return False, "Username already exists."

    return True, ""


def validate_email(email):
    email = email.strip().lower()

    if not email:
        return False, "Email cannot be empty."

    if email.count("@") != 1:
        return False, "Invalid email address."

    local_part, domain = email.split("@")

    if not local_part:
        return False, "Invalid email address."

    if "." not in domain:
        return False, "Invalid email address."

    existing_email = get_user_by_email(email)

    if existing_email is not None:
        return False, "Email already exists."

    return True, ""


def validate_password(password):
    if not password:
        return False, "Password cannot be empty."

    if " " in password:
        return False, "Password cannot contain spaces."

    if len(password) < 8:
        return False, "Password must be at least 8 characters long."

    if not any(char.islower() for char in password):
        return False, "Password must contain at least one lowercase letter."

    if not any(char.isupper() for char in password):
        return False, "Password must contain at least one uppercase letter."

    if not any(char.isdigit() for char in password):
        return False, "Password must contain at least one digit."

    special_characters = "!@#$%^&*()-_=+[]{}|\\:;\"'<>,.?/`~"

    if not any(char in special_characters for char in password):
        return False, "Password must contain at least one special character."

    return True, ""


# BUSINESS LOGIC

def register_user(username, email, password):
    username = username.strip()
    email = email.strip().lower()

    is_valid, message = validate_username(username)
    if not is_valid:
        return {
            "success": False,
            "message": message,
        }

    is_valid, message = validate_email(email)
    if not is_valid:
        return {
            "success": False,
            "message": message,
        }

    is_valid, message = validate_password(password)
    if not is_valid:
        return {
            "success": False,
            "message": message,
        }

    user_id = create_user(
        username=username,
        email=email,
        password=password,
    )

    if user_id is None:
        return {
            "success": False,
            "message": "Failed to register user.",
        }

    return {
        "success": True,
        "message": "User registered successfully.",
        "user_id": user_id,
    }
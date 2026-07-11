from DATABASE.users import (
    create_user,
    get_user_by_id,
    get_user_by_username,
    get_all_users,
    update_username,
    update_email,
    update_password,
    delete_user,
)


def main():
    print("===== USERS CRUD TEST =====")

    # CREATE
    print("\n[CREATE]")
    created = create_user("Taran", "taran@example.com", "password123")
    print("User created:", created)

    # READ ALL
    print("\n[READ ALL]")
    users = get_all_users()
    print(users)

    if not users:
        print("No users found. Stopping test.")
        return

    user_id = users[-1][0]

    # READ BY ID
    print("\n[READ BY ID]")
    print(get_user_by_id(user_id))

    # READ BY USERNAME
    print("\n[READ BY USERNAME]")
    print(get_user_by_username("Taran"))

    # UPDATE USERNAME
    print("\n[UPDATE USERNAME]")
    print(update_username(user_id, "TaranSingh"))

    # UPDATE EMAIL
    print("\n[UPDATE EMAIL]")
    print(update_email(user_id, "taran.singh@example.com"))

    # UPDATE PASSWORD
    print("\n[UPDATE PASSWORD]")
    print(update_password(user_id, "newpassword123"))

    # VERIFY UPDATES
    print("\n[VERIFY]")
    print(get_user_by_id(user_id))

    # DELETE
    print("\n[DELETE]")
    print(delete_user(user_id))

    # FINAL STATE
    print("\n[FINAL USERS]")
    print(get_all_users())


if __name__ == "__main__":
    main()
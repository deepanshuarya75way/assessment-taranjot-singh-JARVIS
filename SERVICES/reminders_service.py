from DATABASE.reminders import (
    create_reminder,
    get_all_reminders,
    get_reminders_by_date,
    get_reminders_by_time,
    update_reminder_date,
    update_reminder_time,
    update_status,
    delete_reminder,
)


def validate_task(task):
    if not task or not task.strip():
        raise ValueError("Task cannot be empty.")

    return task.strip()


def validate_date(reminder_date):
    if not reminder_date or not reminder_date.strip():
        raise ValueError("Reminder date cannot be empty.")

    return reminder_date.strip()


def validate_time(reminder_time):
    if not reminder_time or not reminder_time.strip():
        raise ValueError("Reminder time cannot be empty.")

    return reminder_time.strip()


def create_new_reminder(user_id, task, reminder_date, reminder_time):
    task = validate_task(task)
    reminder_date = validate_date(reminder_date)
    reminder_time = validate_time(reminder_time)

    reminder_id = create_reminder(
        user_id,
        task,
        reminder_date,
        reminder_time,
    )

    return reminder_id


def fetch_all_reminders(user_id):
    return get_all_reminders(user_id)


def fetch_reminders_by_date(user_id, reminder_date):
    reminder_date = validate_date(reminder_date)
    return get_reminders_by_date(user_id, reminder_date)


def fetch_reminders_by_time(user_id, reminder_time):
    reminder_time = validate_time(reminder_time)
    return get_reminders_by_time(user_id, reminder_time)


def change_reminder_date(reminder_id, updated_date):
    updated_date = validate_date(updated_date)
    return update_reminder_date(reminder_id, updated_date)


def change_reminder_time(reminder_id, updated_time):
    updated_time = validate_time(updated_time)
    return update_reminder_time(reminder_id, updated_time)


def mark_reminder_completed(reminder_id):
    return update_status(reminder_id, "Completed")


def mark_reminder_pending(reminder_id):
    return update_status(reminder_id, "Pending")


def remove_reminder(reminder_id):
    return delete_reminder(reminder_id)
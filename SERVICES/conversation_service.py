from DATABASE.conversations import (
    create_conversation,
    get_all_conversations,
    get_conversation_by_id,
    update_conversation_title,
    update_conversation_status,
    delete_conversation,
)


# VALIDATION

def validate_title(title):
    if not title or not title.strip():
        raise ValueError("Conversation title cannot be empty.")

    return title.strip()


def validate_status(status):
    allowed_status = {"active", "archived"}

    status = status.strip().lower()

    if status not in allowed_status:
        raise ValueError(
            f"Status must be one of: {', '.join(allowed_status)}"
        )

    return status


# BUSINESS LOGIC

def start_conversation(user_id, title="New Conversation"):
    title = validate_title(title)

    return create_conversation(
        user_id=user_id,
        title=title,
    )


def fetch_all_conversations(user_id):
    return get_all_conversations(user_id)


def fetch_conversation(conversation_id):
    return get_conversation_by_id(conversation_id)


def rename_conversation(conversation_id, title):
    title = validate_title(title)

    return update_conversation_title(
        conversation_id,
        title,
    )


def archive_conversation(conversation_id):
    return update_conversation_status(
        conversation_id,
        "archived",
    )


def activate_conversation(conversation_id):
    return update_conversation_status(
        conversation_id,
        "active",
    )


def remove_conversation(conversation_id):
    return delete_conversation(conversation_id)
from DATABASE.notes import (
    create_note,
    get_all_notes,
    get_note_by_title,
    search_notes,
    update_note,
    delete_note,
)


# ==========================
# VALIDATION
# ==========================

def validate_title(title):
    if not title or not title.strip():
        raise ValueError("Title cannot be empty.")

    return title.strip()


def validate_content(content):
    if not content or not content.strip():
        raise ValueError("Content cannot be empty.")

    return content.strip()


def validate_category(category):
    if not category or not category.strip():
        return "General"

    return category.strip()


# ==========================
# BUSINESS LOGIC
# ==========================

def create_new_note(user_id, title, content, category="General"):
    title = validate_title(title)
    content = validate_content(content)
    category = validate_category(category)

    note_id = create_note(
        user_id=user_id,
        title=title,
        content=content,
        category=category,
    )

    return {
        "success": True,
        "note_id": note_id,
        "message": f'Note "{title}" created successfully.'
    }


def fetch_all_notes(user_id):
    notes = get_all_notes(user_id)

    if not notes:
        return {
            "success": True,
            "message": "You don't have any notes yet.",
            "data": []
        }

    lines = ["Your Notes:", ""]

    for index, note in enumerate(notes, start=1):
        title = note[2]
        lines.append(f"{index}. {title}")

    return {
        "success": True,
        "message": "\n".join(lines),
        "data": notes,
    }


def fetch_note(user_id, title):
    title = validate_title(title)

    note = get_note_by_title(user_id, title)

    if note is None:
        return {
            "success": False,
            "message": f'Note "{title}" not found.'
        }

    return {
        "success": True,
        "message": f'Note "{title}" found.',
        "data": note
    }


def find_notes(user_id, keyword):
    if not keyword or not keyword.strip():
        return {
            "success": False,
            "message": "Please provide a keyword to search."
        }

    notes = search_notes(user_id, keyword.strip())

    if not notes:
        return {
            "success": False,
            "message": "No matching notes found."
        }

    return {
        "success": True,
        "message": f"Found {len(notes)} matching note(s).",
        "data": notes
    }


def edit_note(user_id, title, content, category="General"):
    title = validate_title(title)
    content = validate_content(content)
    category = validate_category(category)

    note = get_note_by_title(user_id, title)

    if note is None:
        return {
            "success": False,
            "message": f'Note "{title}" not found.'
        }

    note_id = note[0]

    update_note(
        note_id,
        title,
        content,
        category,
    )

    return {
        "success": True,
        "message": f'Note "{title}" updated successfully.'
    }


def remove_note(user_id, title):
    title = validate_title(title)

    note = get_note_by_title(user_id, title)

    if note is None:
        return {
            "success": False,
            "message": f'Note "{title}" not found.'
        }

    note_id = note[0]

    delete_note(note_id)

    return {
        "success": True,
        "message": f'Note "{title}" deleted successfully.'
    }
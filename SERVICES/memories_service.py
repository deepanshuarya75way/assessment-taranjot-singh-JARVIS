from DATABASE.memories import (
    create_memory,
    get_all_memories,
    get_memory_by_id,
    get_memories_by_category,
    update_memory,
    update_last_accessed,
    delete_memory,
)


# VALIDATION

def validate_memory(memory):
    if not memory or not memory.strip():
        raise ValueError("Memory cannot be empty.")

    return memory.strip()


def validate_category(category):
    if not category or not category.strip():
        return "General"

    return category.strip()


def validate_importance(importance):
    try:
        importance = int(importance)
    except (ValueError, TypeError):
        importance = 1

    return max(1, min(10, importance))


# BUSINESS LOGIC

def create_new_memory(
    user_id,
    memory,
    category="General",
    importance=1,
    source="manual",
):
    memory = validate_memory(memory)
    category = validate_category(category)
    importance = validate_importance(importance)

    return create_memory(
        user_id=user_id,
        memory=memory,
        category=category,
        importance=importance,
        source=source,
    )


def fetch_all_memories(user_id):
    return get_all_memories(user_id)


def fetch_memory(memory_id):
    return get_memory_by_id(memory_id)


def fetch_memories_by_category(user_id, category):
    category = validate_category(category)
    return get_memories_by_category(user_id, category)


def edit_memory(memory_id, memory, category, importance):
    memory = validate_memory(memory)
    category = validate_category(category)
    importance = validate_importance(importance)

    return update_memory(
        memory_id,
        memory,
        category,
        importance,
    )


def touch_memory(memory_id):
    """
    Updates the last_accessed timestamp whenever
    JARVIS retrieves a memory.
    """
    return update_last_accessed(memory_id)


def remove_memory(memory_id):
    return delete_memory(memory_id)
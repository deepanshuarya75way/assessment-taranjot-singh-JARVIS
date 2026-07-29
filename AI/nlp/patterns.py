"""
Defines spaCy Matcher patterns used for intent detection.

This module only contains language patterns.
It does not contain business logic or application logic.
"""

# Notes Module

NOTE_PATTERNS = {
    "CREATE_NOTE": [
        [{"LEMMA": "create"}, {"LOWER": "a", "OP": "?"}, {"LEMMA": "note"}],
        [{"LEMMA": "add"}, {"LOWER": "a", "OP": "?"}, {"LEMMA": "note"}],
        [{"LEMMA": "make"}, {"LOWER": "a", "OP": "?"}, {"LEMMA": "note"}],
        [{"LEMMA": "write"}, {"LOWER": "a", "OP": "?"}, {"LEMMA": "note"}],
        [{"LEMMA": "take"}, {"LOWER": "a", "OP": "?"}, {"LEMMA": "note"}],
    ],

    "READ_NOTE": [
        [{"LEMMA": "show"}, {"LOWER": "me", "OP": "?"}, {"LEMMA": "note"}],
        [{"LEMMA": "open"}, {"LEMMA": "note"}],
        [{"LEMMA": "display"}, {"LEMMA": "note"}],
        [{"LEMMA": "list"}, {"LEMMA": "note"}],
        [{"LEMMA": "view"}, {"LEMMA": "note"}],
        [{"LEMMA": "read"}, {"LEMMA": "note"}],
    ],

    "LIST_NOTES": [
        [{"LEMMA": "show"}, {"LOWER": "all", "OP": "?"}, {"LOWER": "my", "OP": "?"}, {"LEMMA": "note"}],
        [{"LEMMA": "list"}, {"LOWER": "all", "OP": "?"}, {"LOWER": "my", "OP": "?"}, {"LEMMA": "note"}],
        [{"LEMMA": "display"}, {"LOWER": "all", "OP": "?"}, {"LOWER": "my", "OP": "?"}, {"LEMMA": "note"}],
        [{"LEMMA": "view"}, {"LOWER": "all", "OP": "?"}, {"LOWER": "my", "OP": "?"}, {"LEMMA": "note"}],
    ],

    "UPDATE_NOTE": [
        [{"LEMMA": "update"}, {"LEMMA": "note"}],
        [{"LEMMA": "edit"}, {"LEMMA": "note"}],
        [{"LEMMA": "modify"}, {"LEMMA": "note"}],
        [{"LEMMA": "change"}, {"LEMMA": "note"}],
    ],

    "DELETE_NOTE": [
        [{"LEMMA": "delete"}, {"LEMMA": "note"}],
        [{"LEMMA": "remove"}, {"LEMMA": "note"}],
        [{"LEMMA": "erase"}, {"LEMMA": "note"}],
    ],
}


# Reminder Module

REMINDER_PATTERNS = {
    "CREATE_REMINDER": [
        [{"LEMMA": "remind"}],
        [{"LEMMA": "create"}, {"LEMMA": "reminder"}],
        [{"LEMMA": "add"}, {"LEMMA": "reminder"}],
    ],

    "DELETE_REMINDER": [
        [{"LEMMA": "delete"}, {"LEMMA": "reminder"}],
        [{"LEMMA": "remove"}, {"LEMMA": "reminder"}],
    ],

    "READ_REMINDER": [
        [{"LEMMA": "show"}, {"LEMMA": "reminder"}],
        [{"LEMMA": "list"}, {"LEMMA": "reminder"}],
        [{"LEMMA": "view"}, {"LEMMA": "reminder"}],
    ],
}


# Memory Module

MEMORY_PATTERNS = {
    "SAVE_MEMORY": [
        [{"LEMMA": "remember"}],
        [{"LOWER": "don't"}, {"LEMMA": "forget"}],
        [{"LEMMA": "save"}, {"LEMMA": "memory"}],
        [{"LEMMA": "store"}, {"LEMMA": "memory"}],
    ]
}
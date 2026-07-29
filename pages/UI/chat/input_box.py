import streamlit as st


def get_user_prompt():
    """
    Display the chat input box and return the user's message.

    Returns:
        str | None: The user's message if submitted, otherwise None.
    """

    return st.chat_input("Ask JARVIS something...")
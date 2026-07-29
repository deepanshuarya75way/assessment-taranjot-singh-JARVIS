import streamlit as st

from pages.UI.chat.message_renderer import render_message


def render_chat_history(chat_history):
    """
    Render all chat messages.

    Args:
        chat_history (list): List of chat message dictionaries.
    """

    if not chat_history:
        st.info("Start a conversation with JARVIS.")
        return

    for message in chat_history:
        render_message(message)
import streamlit as st


def render_message(message):
    """
    Render a single chat message.

    Expected message format:
    {
        "role": "user" | "assistant",
        "content": "Message text",
        "source": "service" | "gemini"   # Optional
    }
    """

    role = message.get("role", "assistant")
    content = message.get("content", "")

    with st.chat_message(role):
        st.markdown(content)
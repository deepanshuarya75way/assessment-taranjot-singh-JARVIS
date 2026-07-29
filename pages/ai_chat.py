import streamlit as st

from AI.controllers.chat_controller import ChatController
from pages.UI.chat.header import render_header
from pages.UI.chat.history import render_chat_history
from pages.UI.chat.input_box import get_user_prompt


def initialize_chat():
    """Initialize chat session state."""

    if "chat_controller" not in st.session_state:
        st.session_state.chat_controller = ChatController()

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []


def app():
    """Render the AI chat page."""

    initialize_chat()

    render_header()

    render_chat_history(st.session_state.chat_history)

    prompt = get_user_prompt()

    if not prompt:
        return

    st.session_state.chat_history.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    with st.spinner("JARVIS is thinking..."):
        result = st.session_state.chat_controller.process_prompt(prompt)

    response = result.get("response", "No response generated.")

    data = result.get("data")

    if isinstance(data, dict):
        title = data.get("title")
        content = data.get("content")

        if title and content:
            response = f"# {title}\n\n{content}"

    elif isinstance(data, tuple) and len(data) >= 4:
        # SQLite row format:
        # (id, user_id, title, content, category, created_at, updated_at)
        title = data[2]
        content = data[3]

        response = f"# {title}\n\n{content}"

    st.session_state.chat_history.append(
        {
            "role": "assistant",
            "content": response,
        }
    )

    st.rerun()
import streamlit as st


def render_header():
    """Render the AI chat page header."""

    col1, col2 = st.columns([6, 1])

    with col1:
        st.title("JARVIS")
        st.caption("Personal AI Assistant")

    with col2:
        if st.button("Clear Chat", use_container_width=True):
            st.session_state.chat_history = []
            st.rerun()

    st.divider()
import streamlit as st
from streamlit_option_menu import option_menu
import pages.ai_chat as ai_chat

def initialize_session():
    """Initialize Streamlit session state."""

    if "user_id" not in st.session_state:
        st.session_state.user_id = None

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    if "current_conversation" not in st.session_state:
        st.session_state.current_conversation = None

PAGES = {
    "AI Chat": ai_chat.app,
}

def main():
    """Launch the Streamlit application."""
    initialize_session()
    selected_page = option_menu(
        menu_title="JARVIS",
        options=list(PAGES.keys()),
        default_index=0,
    )
    PAGES[selected_page]()

if __name__ == "__main__":
    main()

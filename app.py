import streamlit as st
from streamlit_option_menu import option_menu
import pages.home as home
import pages.users as users
import pages.notes as notes
import pages.reminders as reminders
import pages.conversations as conversations
import pages.memories as memories
import pages.ai_chat as ai_chat

st.set_page_config(page_title="JARVIS", layout="wide")

PAGES = {
    "Home": home.app,
    "Users": users.app,
    "Notes": notes.app,
    "Reminders": reminders.app,
    "Conversations": conversations.app,
    "Memories": memories.app,
    "AI Chat": ai_chat.app,
}

def main():
    selected_page = option_menu(
        menu_title="JARVIS",
        options=list(PAGES.keys()),
        default_index=0,
    )
    PAGES[selected_page]()

if __name__ == "__main__":
    main()

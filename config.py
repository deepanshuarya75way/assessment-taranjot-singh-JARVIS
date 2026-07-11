from pathlib import Path

# Project Root
BASE_DIR = Path(__file__).resolve().parent

# Data Directory
DATA_DIR = BASE_DIR / "DATA"
DATA_DIR.mkdir(exist_ok=True)

# SQLite Database
DATABASE_PATH = DATA_DIR / "assistant.db"

# App Information
APP_NAME = "JARVIS"
import os

API_ID    = os.environ.get("API_ID", "33836080")
API_HASH  = os.environ.get("API_HASH", "a5a02f0324ef4a8c767c6831aae67526")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8512379184:AAHVoF20cWSHBkYpne3yJyQ9_RTnRG5ZHcQ") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8870))  # Default to 8000 if not set

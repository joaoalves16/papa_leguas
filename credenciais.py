import os

# Set environment variables
os.environ["API_USER"] = ""
os.environ["API_PASSWORD"] = ""
os.environ["API_KEY"] = ""

USER = os.getenv("API_USER")
PASSWORD = os.environ.get("API_PASSWORD")
KEY = os.environ.get("API_KEY")

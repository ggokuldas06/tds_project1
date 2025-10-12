from dotenv import load_dotenv
import os

# Load environment variables from .env in the current directory
load_dotenv()

# Debug print — remove later
print("STUDENT_EMAIL:", os.getenv("STUDENT_EMAIL"))
print("STUDENT_SECRET:", os.getenv("STUDENT_SECRET"))

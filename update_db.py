import sys
import os

# Add project root to sys.path to allow importing main
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

try:
    from src.main import app, db
    print("App and db imported successfully.")

    with app.app_context():
        print("Dropping all tables...")
        db.drop_all()
        print("Creating all tables...")
        db.create_all()
        print("Database schema updated successfully.")

except ImportError as e:
    print(f"Error importing app or db: {e}")
    print("Please ensure src/main.py exists and is correctly structured.")
except Exception as e:
    print(f"An error occurred during database update: {e}")


import os
import sys

# Get the directory of the current script
current_script_path = os.path.dirname(os.path.abspath(__file__))

# Navigate up one level to the 'shepherd_app' directory and add it to the system path.
# This makes the 'src' directory discoverable.
project_root = os.path.abspath(os.path.join(current_script_path, ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
    print(f"Added {project_root} to the system path.")

try:
    from src.services.firebase_manager import initialize_firebase
except ModuleNotFoundError as e:
    import pytest

    pytest.skip(f"Skipping firebase connection tests - missing module: {e}")


def run_test():
    """
    Runs a simple test to check if the Firebase Admin SDK can be initialized.
    """
    print("--- Running Firebase Connection Test ---")

    db = initialize_firebase()

    if db:
        print("✅ Success: Firebase connection test passed!")
    else:
        print("❌ Failure: Firebase connection test failed.")


if __name__ == "__main__":
    run_test()

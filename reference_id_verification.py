import hashlib
import re

# Function to validate the Reference ID
def is_valid_reference_id(ref_id):
    # Check if the reference ID is exactly 12 characters long and contains only alphanumeric characters
    if len(ref_id) == 12 and re.match("^[a-zA-Z0-9]*$", ref_id):
        return True
    return False

# Function to encrypt the Reference ID using SHA-256
def encrypt_reference_id(ref_id):
    # Encrypt the reference ID using SHA-256 hash
    encrypted_id = hashlib.sha256(ref_id.encode()).hexdigest()
    return encrypted_id

# Main function to run the system
def main():
    # Step 1: Read input from command line
    ref_id = input("Enter the Reference ID (12 alphanumeric characters): ")

    # Step 2: Validate the Reference ID
    if is_valid_reference_id(ref_id):
        # Step 3: Encrypt the Reference ID
        encrypted_id = encrypt_reference_id(ref_id)
        print(f"Encrypted Reference ID: {encrypted_id}")
    else:
        print("Invalid Reference ID. It must be 12 alphanumeric characters.")

if __name__ == "__main__":
    main()
import os
import subprocess
import configparser

def get_git_root_path():
    # Get the root directory of the current Git repository
    return subprocess.check_output(['git', 'rev-parse', '--show-toplevel']).strip().decode()

def read_key_from_file(filename="license_key.txt"):
    try:
        # Construct the full path to the file
        git_root = get_git_root_path()
        file_path = os.path.join(git_root, filename)

        # Read the license key from the file
        with open(file_path, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        # Handle the case where the file does not exist
        print("Error: License key file not found.")
        exit(1)
    except Exception as e:
        # Handle any other exceptions
        print(f"Error: {e}")
        exit(1)

def verify_license_key(user_key, valid_key):
    # Compare the provided key with the valid key
    return user_key == valid_key

# Predefined valid license key 
config = configparser.ConfigParser()
config.read('config.cfg')
VALID_LICENSE_KEY = config.get('license', 'key', fallback='default-fallback-key')


# Read the license key from the file
license_key_from_file = read_key_from_file()

# Verify the license key
if verify_license_key(license_key_from_file, VALID_LICENSE_KEY):
    print("Success: License key is valid.")
else:
    print("Error: Invalid license key.")
    exit(1)

import uuid
import os
import subprocess

def get_git_root_path():
    # Execute a Git command to find the root directory of the current Git repository
    # The command 'git rev-parse --show-toplevel' returns the absolute path of the top-level directory
    # 'subprocess.check_output' runs the command and captures its output
    # 'strip().decode()' converts the output from bytes to a string and removes any trailing whitespace
    return subprocess.check_output(['git', 'rev-parse', '--show-toplevel']).strip().decode()

def generate_license_key():
    # Generate a unique license key using UUID4
    # UUID4 generates random UUIDs, which are highly unlikely to repeat
    return str(uuid.uuid4())

def write_key_to_file(key, filename="license_key.txt"):
    # Get the root path of the current Git repository
    # This ensures the file is saved in the top directory of the Git repository
    git_root = get_git_root_path()

    # Create the full path for the file by joining the Git root directory and the filename
    file_path = os.path.join(git_root, filename)

    # Open the file for writing and write the generated key to it
    # 'with open' is used for safe file handling (automatically closes the file)
    with open(file_path, 'w') as file:
        file.write(key)

# Generate a new license key using the function defined above
license_key = generate_license_key()

# Write the generated license key to a file
# The file will be saved in the top directory of the Git repository
write_key_to_file(license_key)

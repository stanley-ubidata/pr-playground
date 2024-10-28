import sys
import os

def bump_version(version):
    # Split the version into version part and build number
    version_parts = version.split('+')
    version_part = version_parts[0]
    build_number = int(version_parts[1])

    # Split version part into major, minor, patch
    version_numbers = version_part.split('.')
    major = int(version_numbers[0])
    minor = int(version_numbers[1])
    patch = int(version_numbers[2])

    # Increment the patch and build numbers
    patch += 1
    build_number += 1

    # Form the new version string
    new_version = f"{major}.{minor}.{patch}+{build_number}"

    # Navigate to the folder on top
    folder_path = "../../apps"

    # Assign the new version value to file called VERSION
    version_file_path = os.path.join(folder_path, "VERSION")
    with open(version_file_path, 'w') as version_file:
        version_file.write(new_version)

    # Read the value from the file and print it
    with open(version_file_path, 'r') as version_file:
        print(version_file.read())

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a version number as a command line argument.")
    else:
        bump_version(sys.argv[1])

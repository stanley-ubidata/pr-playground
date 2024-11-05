import sys
import os

def bump_version(version,  environment="DEV", override_major="-", override_minor="-", override_patch="-"):
    # Split the version into version part and build number
    version_parts = version.split('+')
    version_part = version_parts[0]
    build_number = int(version_parts[1])
    # Split version part into major, minor, patch
    version_numbers = version_part.split('.')
    major = int(version_numbers[0])
    minor = int(version_numbers[1])
    patch = int(version_numbers[2])

    build_number += 1    

    if override_major != "-":
        major = override_major
        minor = override_minor != "-" and override_minor or 0
        patch = override_patch != "-" and override_patch or 0
    elif override_minor != "-":
        minor = override_minor
        patch = override_patch != "-" and override_patch or 0
    else:
        if override_patch != "-":
            patch = override_patch
        elif environment == "QA":
            patch = patch + 1

    new_version = f"{major}.{minor}.{patch}+{build_number}"

    # Navigate to the folder on top
    folder_path = "./"

    # Assign the new version value to file called VERSION
    version_file_path = os.path.join(folder_path, "VERSION")
    with open(version_file_path, 'w') as version_file:
        version_file.write(new_version)

    # Read the value from the file and print it
    with open(version_file_path, 'r') as version_file:
        print(version_file.read())

if __name__ == "__main__":
    if len(sys.argv) < 1:
        print("Please provide a version number as a command line argument.")
    elif len(sys.argv) == 2:
        bump_version(sys.argv[1])
    elif len(sys.argv) == 3:
        bump_version(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 4:
        bump_version(sys.argv[1], sys.argv[2], sys.argv[3])
    elif len(sys.argv) == 5:
        bump_version(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    elif len(sys.argv) == 6:
        bump_version(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
    else:
        print("Too many arguments provided.")

# Run the script
# python bump_version.py 1.0.0+1


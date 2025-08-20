#!/usr/bin/env python3
import sys
import plistlib
from packaging.version import Version

def increment_version(version: str, part: str) -> str:
    """Increment the semantic version based on the specified part (major, minor, patch)."""
    v = Version(version)
    major, minor, patch = v.major, v.minor, v.micro

    if part == 'major':
        major += 1
        minor = 0
        patch = 0
    elif part == 'minor':
        minor += 1
        patch = 0
    elif part == 'patch':
        patch += 1
    else:
        raise ValueError("Invalid part specified. Use 'major', 'minor', or 'patch'.")

    return f"{major}.{minor}.{patch}"

def update_ios_version(plist_path: str, part: str):
    """Update the CFBundleShortVersionString in Info.plist."""
    with open(plist_path, 'rb') as plist_file:
        plist_data = plistlib.load(plist_file)
        current_version = plist_data['CFBundleShortVersionString']
        new_version = increment_version(current_version, part)
        plist_data['CFBundleShortVersionString'] = new_version

    with open(plist_path, 'wb') as plist_file:
        plistlib.dump(plist_data, plist_file)

    print(f"Updated iOS version to {new_version} in {plist_path}")

def update_android_version(gradle_path: str, part: str):
    """Update the versionName in build.gradle."""
    with open(gradle_path, 'r') as gradle_file:
        gradle_content = gradle_file.readlines()

    new_gradle_content = []
    found = False
    for line in gradle_content:
        if 'versionName' in line:
            parts = line.split('"')
            if len(parts) >= 3:
                current_version = parts[1]
                new_version = increment_version(current_version, part)
                line = line.replace(current_version, new_version)
                found = True
        new_gradle_content.append(line)

    if not found:
        raise ValueError("versionName not found in build.gradle")

    with open(gradle_path, 'w') as gradle_file:
        gradle_file.writelines(new_gradle_content)

    print(f"Updated Android version to {new_version} in {gradle_path}")

def main():
    if len(sys.argv) != 2:
        print("Usage: increment_app_version.py <part>")
        print("<part>: 'major', 'minor', or 'patch'")
        sys.exit(1)

    part = sys.argv[1]
    plist_path = "./ios/App/App/Info.plist"
    gradle_path = "./android/app/build.gradle"

    try:
        update_ios_version(plist_path, part)
        update_android_version(gradle_path, part)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

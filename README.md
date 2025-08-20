# App Version Incrementer

 A Python script to automatically increment the version number for both iOS and Android apps.

## Features

- Increments semantic version (major, minor, patch) in:
- iOS `Info.plist` (`CFBundleShortVersionString`)
- Android `build.gradle` (`versionName`)
- Uses the `packaging` library for robust version parsing.

## Project Structure

```text
app-version-incrementer
├── src
│   ├── increment_app_version.py
├── tests
│   ├── test_increment_app_version.py
├── package.json
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.7+
- `packaging` library

## Installation

1. Clone the repository to your local machine:

```bash
git clone <repository-url>
cd build-number-incrementer
```

1. Install the required Python dependencies:

```bash
pip install -r requirements.txt
```

1. Set up the project as a global npm package using `npm link`:

```bash
npm link
```

This will make the `increment-app-version` command globally available on your system.

## Usage

Run the script from the `src` directory:

```bash
python increment_app_version.py <part>
```

Where `<part>` is one of:

- `major`
- `minor`
- `patch`

### Example

```bash
python increment_app_version.py minor
```

This will increment the minor version in both iOS and Android project files.

## File Paths

- iOS: `./ios/App/App/Info.plist`
- Android: `./android/app/build.gradle`

## Error Handling

If the script encounters an error (e.g., missing version string), it will print an error message and exit with code 1.

## License

MIT

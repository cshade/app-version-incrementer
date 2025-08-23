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

In general, the script can be run as follows:

```bash
python increment_app_version.py <part>
```

Where `<part>` is one of:

- `major`
- `minor`
- `patch`

This will increment the minor version in both iOS and Android project files.

More ideally, add an npm script to your project's `package.json`:

```json
{
  "scripts": {
    "increment-version": "increment-app-version"
  }
}
```

And then run the script:

```bash
npm run increment-version -- <part>
```

Where `<part>` is one of:

- `major`
- `minor`
- `patch`

For example, the following will update the `minor` version number in the local project:

```bash
npm run increment-version -- minor
```

This script will:

- Read the current build number from `Info.plist` and `build.gradle`.
- Increment the build number by 1.
- Write the updated build number back to both files.

## File Paths

- iOS: `./ios/App/App/Info.plist`
- Android: `./android/app/build.gradle`

## Error Handling

If the script encounters an error (e.g., missing version string), it will print an error message and exit with code 1.

## License

MIT

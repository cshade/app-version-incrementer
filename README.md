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
│   ├── test_increment_version.py
├── package.json
├── pyproject.toml
└── README.md
```

## Requirements

- Python 3.8+
- `packaging` library

## Installation

1. Clone the repository to your local machine:

```bash
git clone <repository-url>
cd app-version-incrementer
```

1. Install the project:

```bash
python -m pip install .
```

If you want the test dependencies as well, install the development extra:

```bash
python -m pip install -e ".[dev]"
```

To enable the git hooks for linting and formatting, then run:

```bash
pre-commit install
```

1. Optionally, set up the project as a global npm package using `npm link`:

```bash
npm link
```

This will make the `increment-app-version` command globally available on your system.

## Usage

In general, the script can be run as follows:

```bash
increment-app-version <part>
```

Where `<part>` is one of:

- `major`
- `minor`
- `patch`

This will increment the selected semantic version component in both iOS and Android project files.

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

- Read the current version from `Info.plist` and `build.gradle`.
- Increment the requested semantic version component.
- Write the updated version back to both files.

## File Paths

- iOS: `./ios/App/App/Info.plist`
- Android: `./android/app/build.gradle`

## Error Handling

If the script encounters an error (e.g., missing version string), it will print an error message and exit with code 1.

## Running Tests

This project uses [pytest](https://pytest.org/) for unit testing. All tests are located in the `tests/` folder.

To run all tests, use:

```bash
pytest
```

If you need to install pytest, run:

```bash
python -m pip install -e ".[dev]"
```

## Code Quality

This project uses `pre-commit` with local `ruff` hooks for linting and formatting.

To run the hooks manually:

```bash
pre-commit run --all-files
```

Test files are named with the pattern `test_*.py` and cover the main functionality of the scripts in `src/`.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements for the project.

## License

MIT

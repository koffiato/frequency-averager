# Frequency Averager

A simple Python tool to average the frequency response of left and right audio channels, making it easier to target EQ adjustments.

## Requirements

- Python 3.7 or newer
- No external packages required for CLI mode
- For GUI mode: `tkinter`

## Features

- Reads two plain text files containing frequency response data (frequency and response per line).
- Checks for frequency alignment between files.
- Outputs a new file with the averaged response.
- Provides clear error messages for mismatched frequencies or invalid input.
- Supports both GUI (file picker) and CLI usage.
- Accepts files with either space or comma as separator.

## Usage

### GUI Mode

1. Run the script without arguments:

    ```sh
    python averager.py
    ```

2. Select the two files when prompted.
3. Choose where to save the averaged output.

### CLI Mode

You can also run the script with file paths as arguments:

```sh
python averager.py left.txt right.txt output.txt
```

If you do not have `tkinter` installed, use CLI mode.

## Example

Input files:
```
20 104.2
21 104.1
...
```

Output file:
```
20 104.15
21 104.05
...
```

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.


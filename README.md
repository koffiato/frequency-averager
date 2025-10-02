# Frequency Averager

A simple Python tool to average the frequency response of left and right audio channels, making it easier to target EQ adjustments.

## Requirements

- Python 3.7 or newer
- No external packages required for CLI mode
- For GUI mode: `tkinter`

## Features

- Reads two or more plain text files containing frequency response data (frequency and response per line).
- Checks for frequency alignment and line count between files.
- Outputs a new file with the averaged response.
- Provides clear error messages for mismatched frequencies, line count, or invalid input.
- Supports both GUI (file picker) and CLI usage.
- Accepts files with either space or comma as separator.

## Usage

### GUI Mode

1a. Run the script in GUI mode (file picker):

```sh
python averager.py --gui
```

1b. Or simply run without arguments (GUI will launch if no CLI args are provided):

```sh
python averager.py
```

2.  Select the number of input files (minimum 2).
3.  Pick the files to average.
4.  Choose where to save the output.

### CLI Mode

1a. Run the script with arguments:

```sh
python averager.py left.txt right.txt -o output.txt
```

1b. Or specify more files:

```sh
python averager.py -m 3 file1.txt file2.txt file3.txt -o averaged.txt
```

If you do not have `tkinter` installed, use CLI mode.

#### Arguments

- `-m` : Number of input files (default: 2)
- `inputs` : Paths to input files (must match `-m`)
- `-o`, `--output` : Path to output file
- `--gui` : Run in GUI mode

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


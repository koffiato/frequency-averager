# Frequency Averager

A simple Python tool to average the frequency response of left and right audio channels, making it easier to target EQ adjustments.

## Features

- Reads two plain text files containing frequency response data (frequency and response per line).
- Checks for frequency alignment between files.
- Outputs a new file with the averaged response.

## Usage

1. Place your two frequency response files (e.g., `Dunu Glacier [1].txt` and `Dunu Glacier [2].txt`) in the same directory as `averager.py`.
2. Run the script:

    ```sh
    python averager.py
    ```

3. Enter the names of your two files when prompted.
4. The script will create a new file named `<file1>_<file2>_Averaged.txt` containing the averaged data.

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


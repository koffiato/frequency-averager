# Frequency Averager

A simple Python tool to average the frequency response of left and right audio channels, making it easier to target EQ adjustments.

## Features

- Reads two plain text files containing frequency response data (frequency and response per line).
- Checks for frequency alignment between files.
- Outputs a new file with the averaged response.
- Provides clear error messages for mismatched frequencies or invalid input.

## Usage

1. Run the script:

    ```sh
    python averager.py
    ```

3. Select the files when prompted.
4. Save anywhere you desire.

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


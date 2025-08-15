import os
import sys
import argparse

def average_files(file1, file2, output_file):
    with open(file1, "r") as f1, open(file2, "r") as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    with open(output_file, "w") as out:
        for line1, line2 in zip(lines1, lines2):
            if not line1.strip() or not line2.strip():
                continue

            sep1 = ',' if ',' in line1 else None
            sep2 = ',' if ',' in line2 else None

            parts1 = line1.strip().split(sep1)
            parts2 = line2.strip().split(sep2)

            if len(parts1) != 2 or len(parts2) != 2:
                raise ValueError(f"Line format error:\n{line1}\n{line2}")

            freq1, resp1 = parts1
            freq2, resp2 = parts2

            if freq1 != freq2:
                raise ValueError(f"Frequency mismatch: {freq1} vs {freq2}")

            avg_response = (float(resp1) + float(resp2)) / 2
            out.write(f"{freq1} {avg_response:.14f}\n")

    print(f"Averaged file saved as: {output_file}")

def gui_mode():
    import tkinter as tk
    from tkinter import filedialog

    root = tk.Tk()
    root.withdraw()

    file1 = filedialog.askopenfilename(title="Select the first file", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    file2 = filedialog.askopenfilename(title="Select the second file", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])

    if not file1 or not file2:
        print("File selection cancelled.")
        return

    base1 = os.path.splitext(os.path.basename(file1))[0]
    base2 = os.path.splitext(os.path.basename(file2))[0]
    default_output = f"{base1}_{base2}_Averaged.txt"

    output_file = filedialog.asksaveasfilename(
        title="Save Averaged File As",
        defaultextension=".txt",
        initialfile=default_output,
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )

    if not output_file:
        print("Save cancelled.")
        return

    average_files(file1, file2, output_file)

def cli_mode(args):
    if not os.path.exists(args.file1):
        print(f"Error: File not found: {args.file1}")
        sys.exit(1)
    if not os.path.exists(args.file2):
        print(f"Error: File not found: {args.file2}")
        sys.exit(1)

    average_files(args.file1, args.file2, args.output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Average two frequency response files.")
    parser.add_argument("file1", nargs="?", help="Path to the first input file")
    parser.add_argument("file2", nargs="?", help="Path to the second input file")
    parser.add_argument("output", nargs="?", help="Path to the output file")

    args = parser.parse_args()

    if args.file1 and args.file2 and args.output:
        cli_mode(args)
    else:
        try:
            gui_mode()
        except ImportError:
            print("Error: tkinter is not available. Use CLI mode to run the script.")


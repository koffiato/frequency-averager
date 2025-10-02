import os
import sys
import argparse

def average_files(input_files, output_file):
    all_lines = []
    for fname in input_files:
        with open(fname, "r") as f:
            lines = [line for line in f.readlines() if line.strip()]
            all_lines.append(lines)

    line_counts = [len(lines) for lines in all_lines]
    if len(set(line_counts)) != 1:
        raise ValueError(f"Input files have different number of lines: {line_counts}")

    with open(output_file, "w") as out:
        for lines in zip(*all_lines):
            freqs = []
            resps = []
            for line in lines:
                sep = ',' if ',' in line else None
                parts = line.strip().split(sep)
                if len(parts) != 2:
                    raise ValueError(f"Line format error: {line}")
                freq, resp = parts
                freqs.append(freq)
                resps.append(float(resp))
            if len(set(freqs)) != 1:
                raise ValueError(f"Frequency mismatch in line: {freqs}")
            avg_response = sum(resps) / len(resps)
            out.write(f"{freqs[0]} {avg_response:.14f}\n")
    print(f"Averaged file saved as: {output_file}")

def gui_mode(m=2):
    import tkinter as tk
    from tkinter import filedialog, simpledialog

    root = tk.Tk()
    root.withdraw()

    if m is None or m < 2:
        m = simpledialog.askinteger("Number of Inputs", "How many input files? (min 2)", minvalue=2)
        if not m:
            print("Cancelled.")
            return

    input_files = []
    for i in range(m):
        fname = filedialog.askopenfilename(title=f"Select input file #{i+1}", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if not fname:
            print("File selection cancelled.")
            return
        input_files.append(fname)

    bases = [os.path.splitext(os.path.basename(f))[0] for f in input_files]
    default_output = f"{'_'.join(bases)}_Averaged.txt"

    output_file = filedialog.asksaveasfilename(
        title="Save Averaged File As",
        defaultextension=".txt",
        initialfile=default_output,
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )

    if not output_file:
        print("Save cancelled.")
        return

    average_files(input_files, output_file)

def cli_mode(args):
    if args.m is None:
        m = 2
    else:
        m = args.m
    if not args.inputs or len(args.inputs) != m:
        print(f"Error: Expected {m} input files, got {len(args.inputs) if args.inputs else 0}.")
        sys.exit(1)
    for fname in args.inputs:
        if not os.path.exists(fname):
            print(f"Error: File not found: {fname}")
            sys.exit(1)
    if not args.output:
        print("Error: Output file not specified.")
        sys.exit(1)
    average_files(args.inputs, args.output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Average multiple frequency response files.")
    parser.add_argument("-m", type=int, default=None, help="Number of input files (default: 2)")
    parser.add_argument("inputs", nargs="*", help="Paths to input files")
    parser.add_argument("-o", "--output", type=str, help="Path to the output file")
    parser.add_argument("--gui", action="store_true", help="Run in GUI mode")

    args = parser.parse_args()

    if args.gui or (not args.inputs or not args.output):
        try:
            gui_mode(args.m)
        except ImportError:
            print("Error: tkinter is not available. Use CLI mode to run the script.")
    else:
        cli_mode(args)


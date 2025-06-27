import os
import tkinter as tk
from tkinter import filedialog

# Hide the main tkinter window
root = tk.Tk()
root.withdraw()

# Ask for input files using file picker
file1 = filedialog.askopenfilename(title="Select the first file", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
file2 = filedialog.askopenfilename(title="Select the second file", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])

if not file1 or not file2:
    print("File selection cancelled.")
    exit()

base1 = os.path.splitext(os.path.basename(file1))[0]
base2 = os.path.splitext(os.path.basename(file2))[0]
default_output = f"{base1}_{base2}_Averaged.txt"

# Ask for output file location using file picker
output_file = filedialog.asksaveasfilename(
    title="Save Averaged File As",
    defaultextension=".txt",
    initialfile=default_output,
    filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
)

if not output_file:
    print("Save cancelled.")
    exit()

# Read both files
with open(file1, "r") as f1, open(file2, "r") as f2:
    lines1 = f1.readlines()
    lines2 = f2.readlines()

# Write the output
with open(output_file, "w") as out:
    for line1, line2 in zip(lines1, lines2):
        freq1, resp1 = line1.strip().split()
        freq2, resp2 = line2.strip().split()

        if freq1 != freq2:
            raise ValueError(f"Frequency mismatch: {freq1} vs {freq2}")

        avg_response = (float(resp1) + float(resp2)) / 2
        out.write(f"{freq1} {avg_response:.14f}\n")

print(f"Averaged file saved as: {output_file}")

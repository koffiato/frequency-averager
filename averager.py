# Ask for input file names
file1 = input("Enter the name of the first file (e.g. Dunu Glacier [1].txt): ").strip()
file2 = input("Enter the name of the second file (e.g. Dunu Glacier [2].txt): ").strip()

# Output file name
import os

base1 = os.path.splitext(os.path.basename(file1))[0]
base2 = os.path.splitext(os.path.basename(file2))[0]
output_file = f"{base1}_{base2}_Averaged.txt"

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
        out.write(f"{freq1} {avg_response:.6f}\n")

print(f"Averaged file saved as: {output_file}")

from Bio import SeqIO

fasta_file = "Dengue_all.fasta"
output_file = "Dengue_all_trimmed.fasta"

# Find the length of the shortest sequence
min_length = min(len(record.seq) for record in SeqIO.parse(fasta_file, "fasta"))

# Trim all sequences to the same length
with open(output_file, "w") as out_handle:
    for record in SeqIO.parse(fasta_file, "fasta"):
        record.seq = record.seq[:min_length]
        SeqIO.write(record, out_handle, "fasta")

print(f"All sequences have been trimmed to {min_length} bases and saved to {output_file}")

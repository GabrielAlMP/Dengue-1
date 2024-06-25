from Bio import SeqIO

fasta_file = "Dengue_all_trimmed.fasta"
sequence_lengths = []

for record in SeqIO.parse(fasta_file, "fasta"):
    sequence_lengths.append(len(record.seq))

# Check if all sequences have the same length
if len(set(sequence_lengths)) == 1:
    print("All sequences are of the same length.")
else:
    print("Sequences have different lengths:")
    for i, length in enumerate(sequence_lengths):
        print(f"Sequence {i+1}: {length} bases")


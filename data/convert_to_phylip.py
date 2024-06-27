from Bio import AlignIO
from Bio.Align import MultipleSeqAlignment

# Lee el alineamiento en formato FASTA
alignment = AlignIO.read("results/Dengue_Zika_aligned.fasta", "fasta")

# Acorta los nombres de las secuencias y añade un índice único
for i, seq in enumerate(alignment):
    seq.id = f"{seq.id[:6]}_{i:03d}"

# Escribe el alineamiento en formato PHYLIP
AlignIO.write(alignment, "results/Dengue_Zika_aligned.phy", "phylip")
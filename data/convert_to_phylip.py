from Bio import AlignIO

# Leer el archivo de alineamiento en formato FASTA
alignment = AlignIO.read("Dengue_all_trimmed.fasta", "fasta")

# Ajustar los nombres de las secuencias para asegurar que sean únicos y adecuados para PHYLIP
max_name_length = 10  # Definir la longitud máxima del nombre
unique_names = {}

for i, record in enumerate(alignment):
    name = f"Seq{i+1}"[:max_name_length]  # Generar un nombre único limitado a max_name_length caracteres
    record.id = name
    record.name = ""
    record.description = ""

# Escribir el alineamiento en formato PHYLIP
AlignIO.write(alignment, "Dengue_aligned.phy", "phylip")


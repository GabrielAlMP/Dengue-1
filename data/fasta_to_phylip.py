from Bio import SeqIO

# Archivos de entrada y salida
input_file = "Dengue_all.fasta"
output_file = "Dengue_all.phy"

# Leer secuencias del archivo FASTA
records = list(SeqIO.parse(input_file, "fasta"))

# Asegurarse de que todas las secuencias tienen la misma longitud
max_len = max(len(record.seq) for record in records)
for record in records:
    if len(record.seq) < max_len:
        raise ValueError(f"Las secuencias deben tener la misma longitud. Secuencia '{record.id}' es más corta.")

# Escribir en formato PHYLIP
SeqIO.write(records, output_file, "phylip")
print(f"Archivo convertido exitosamente a {output_file}")


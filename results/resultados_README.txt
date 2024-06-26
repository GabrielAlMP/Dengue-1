# Configuración de Python y Biopython en el PATH

Para ejecutar los scripts de Python y usar Biopython, asegúrate de tener Python instalado y añadido al PATH de tu sistema. Puedes verificar la instalación de Python ejecutando `python --version` en la línea de comandos.

Si necesitas instalar Biopython, puedes hacerlo usando pip: "pip install biophyton"


# Alineamiento de secuencias con Muscle

Asegúrate de tener Muscle instalado y añadido al PATH de tu sistema. Puedes verificar la instalación de Muscle ejecutando `muscle -version` en la línea de comandos.

Para alinear las secuencias de Dengue y Zika, ejecuta el siguiente comando:


"muscle -in data/Dengue_Zika_all.fasta -out results/Dengue_Zika_aligned.fasta"


Este comando toma el archivo "data/Dengue_Zika_all.fasta" que contiene las secuencias de Dengue y Zika, las alinea usando Muscle y guarda el alineamiento resultante en "results/Dengue_Zika_aligned.fasta".

# Conversión de FASTA a PHYLIP con Biopython

Asegúrate de tener Python y Biopython instalados y configurados correctamente en tu sistema.

Crea un script de Python llamado `fasta_to_phylip.py` con el siguiente contenido:

```python
from Bio import AlignIO
from Bio.Align import MultipleSeqAlignment

# Leer el alineamiento en formato FASTA
alignment = AlignIO.read("results/Dengue_Zika_aligned.fasta", "fasta")

# Acortar los nombres de las secuencias y añadir un índice único
for i, seq in enumerate(alignment):
    seq.id = f"{seq.id[:6]}_{i:03d}"

# Escribir el alineamiento en formato PHYLIP
AlignIO.write(alignment, "results/Dengue_Zika_aligned.phy", "phylip")



# Para ejecutar el script
"python fasta_to_phylip.py"



# Construcción del árbol filogenético con IQ-TREE

iqtree2 -s results/Dengue_Zika_aligned.phy -m GTR+G+I -B 1000 -alrt 1000 -pre results/Dengue_Zika_iqtree


# Extracción de datos de Dengue y Zika del NCBI

Los datos de las secuencias de Dengue y Zika se obtuvieron del NCBI (National Center for Biotechnology Information) utilizando los siguientes accesos:

- Dengue virus 1: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=11053
- Dengue virus 2: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=11060
- Dengue virus 3: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=11069
- Dengue virus 4: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=11070
- Zika virus: https://www.ncbi.nlm.nih.gov/nuccore/1245709111

Los archivos de secuencia se descargaron en formato GenBank (.txt) para Dengue y en formato FASTA (.fasta) para Zika.

# Conversión de formato GenBank a FASTA

	#Para convertir los archivos de Dengue del formato GenBank (.txt) a formato FASTA, se utilizó el siguiente comando para cada archivo:

seqkit genbank -p <archivo.txt> > <archivo.fasta>


Reemplaza `<archivo.txt>` con el nombre del archivo de Dengue en formato GenBank y `<archivo.fasta>` con el nombre deseado para el archivo FASTA resultante.

# Combinación de archivos FASTA

	#Para combinar todos los archivos FASTA de Dengue y Zika en un solo archivo llamado `Dengue_Zika_all.fasta`, se utilizó el siguiente comando:

cat Dengue_virus_1.fasta Dengue_virus_2.fasta Dengue_virus_3.fasta Dengue_virus_4.fasta Zika_virus.fasta > Dengue_Zika_all.fasta


# Recorte de secuencias (trimming)

	#Para recortar las secuencias de Dengue y crear el archivo `Dengue_all_trimmed.fasta`, se utilizó el siguiente comando:
seqkit subseq -r <inicio>:<fin> Dengue_Zika_all.fasta > Dengue_all_trimmed.fasta




# Análisis Filogenético de Virus del Dengue y Zika
#### Gabriel Alejandro Moreno Pérez (gamorales@puce.edu.ec) </br> 27 de Junio, 2023

Este proyecto tiene como objetivo analizar las relaciones evolutivas entre distintos serotipos del virus del Dengue y el virus Zika utilizando sus secuencias genómicas completas. 
El análisis incluye la obtención de datos del NCBI, el procesamiento y alineamiento de secuencias, la construcción de árboles filogenéticos y la interpretación de los resultados.

### Flujo de Trabajo del Programa

1. **Obtención de Datos**: 
Las secuencias genómicas de los virus del Dengue (serotipos 1-4) y Zika se obtuvieron del NCBI. Los detalles de este proceso se encuentran en el archivo `data/data_README.txt`.


2. **Procesamiento de Datos**: 
Las secuencias descargadas se convirtieron de formato GenBank a FASTA y se combinaron en un solo archivo FASTA (`data/Dengue_Zika_all.fasta`). Además, se realizó un recorte de las secuencias de Dengue (`data/Dengue_all_trimmed.fasta`).


3. **Alineamiento de Secuencias**: 
Las secuencias combinadas de Dengue y Zika se alinearon utilizando Muscle (`results/Dengue_Zika_aligned.fasta`).


4. **Conversión de Formato**: 
El alineamiento se convirtió de formato FASTA a PHYLIP utilizando un script de Biopython (`results/Dengue_Zika_aligned.phy`).


5. **Construcción del Árbol Filogenético**: 
Se construyó un árbol filogenético utilizando IQ-TREE con el modelo GTR+G+I, 1000 réplicas de bootstrap ultrarrápido y 1000 réplicas de SH-aLRT (`results/Dengue_Zika_iqtree`).


6. **Visualización y Interpretación**: 
El árbol filogenético resultante se visualizó y se interpretaron las relaciones evolutivas entre los virus del Dengue y Zika.


Los detalles de los comandos utilizados en cada paso se encuentran en el archivo `scripts/scripts_README.txt`.

<img src="ruta/a/tu/imagen.jpg" alt="Descripción de la imagen" width="50%">

<video src="ruta/a/tu/video.mp4" width="50%" controls>

  Video.

</video>

### Uso del Programa

#### Dependencias
- Muscle
- IQ-TREE
- Biopython
- R packages: deldir, rgeos, PairViz, TSP, graph

#### Instrucciones de Uso
1. Clona este repositorio.
2. Asegúrate de tener todas las dependencias instaladas.
3. Ejecuta los scripts en el orden descrito en `scripts/scripts_README.txt`.

### Autor
- Gabriel Alejandro Morales Pérez
    - Estudiante de [Bioinformática - PUCE]
    - contacto: gamorales@puce.edu.ec

### Agradecimientos
- [A Jorge Drexler porque la vida está en la luna de Rasquí]

### Referencias
- [Añadir referencias]



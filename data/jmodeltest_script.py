import os

# Navegar al directorio de Apache Ant
os.chdir(r"D:\Downloads\apache-ant-1.10.14-bin\apache-ant-1.10.14\bin")

# Añadir el directorio actual a PATH
os.environ["PATH"] += os.pathsep + os.getcwd()

# Navegar al directorio de jModelTest
os.chdir(r"D:\Downloads\apache-ant-1.10.14-bin\jmodeltest-2.1.10\jmodeltest-2.1.10")

# Compilar jModelTest
os.system("ant")

# Navegar al directorio del proyecto
os.chdir(r"C:\Users\Usuario\OneDrive\Escritorio\Bioinformática\ProyectoFinalBio24\data")

# Ejecutar jModelTest
os.system("java -jar D:\\Downloads\\apache-ant-1.10.14-bin\\jmodeltest-2.1.10\\jmodeltest-2.1.10\\dist\\jmodeltest.jar -d Dengue_aligned.phy -g 4 -i -f -AIC -BIC -a -o jmodeltest_output")
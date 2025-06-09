import pandas as pd
from scipy import stats

# URL del dataset en GitHub
url = "https://raw.githubusercontent.com/joshuagonzalezcampos/Dataset-Parcial2/refs/heads/main/dataset_procesos_memoria.csv"

# Leer el CSV desde GitHub
df = pd.read_csv(url)

# Convertir columnas a numéricas si es necesario
df["Uso_RAM_MB"] = pd.to_numeric(df["Uso_RAM_MB"], errors='coerce')
df["Porcentaje_RAM"] = pd.to_numeric(df["Porcentaje_RAM"], errors='coerce')

# Estadísticas básicas
media = df[["Uso_RAM_MB", "Porcentaje_RAM"]].mean()
mediana = df[["Uso_RAM_MB", "Porcentaje_RAM"]].median()
moda = df[["Uso_RAM_MB", "Porcentaje_RAM"]].mode().iloc[0]
desviacion = df[["Uso_RAM_MB", "Porcentaje_RAM"]].std()

# Correlación
correlacion = df[["Uso_RAM_MB", "Porcentaje_RAM"]].corr()

# Resultados
print("\n ESTADÍSTICAS BÁSICAS")
print("------------------------")
print("Media:\n", media)
print("\nMediana:\n", mediana)
print("\nModa:\n", moda)
print("\nDesviación estándar:\n", desviacion)

print("\n MATRIZ DE CORRELACIÓN")
print("-------------------------")
print(correlacion)

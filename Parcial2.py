# generar_dataset.py
import psutil
import pandas as pd
from datetime import datetime

# Lista para almacenar la información
procesos = []

# Recolectar información de procesos activos
for proc in psutil.process_iter(['pid', 'name', 'memory_info', 'username']):
    try:
        mem_mb = proc.info['memory_info'].rss / (1024 * 1024)  # Convertir a MB
        procesos.append({
            'Timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'Nombre_Proceso': proc.info['name'],
            'PID': proc.info['pid'],
            'Uso_RAM_MB': round(mem_mb, 2),
            'Usuario': proc.info['username'] if proc.info['username'] else 'Desconocido'
        })
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass

# Crear DataFrame
df = pd.DataFrame(procesos)

# Simular "Porcentaje_RAM" (opcional) y otras columnas para análisis
total_ram = psutil.virtual_memory().total / (1024 * 1024)
df['Porcentaje_RAM'] = round(df['Uso_RAM_MB'] / total_ram * 100, 2)
df['Firma_Digital'] = 'Desconocido'  # No se puede determinar desde psutil
df['Nivel_Prioridad'] = 'Normal'     # Valor por defecto
df['Etiqueta'] = 'Desconocida'       # Etiqueta para análisis posterior

# Guardar CSV
nombre_archivo = "dataset_procesos_memoria.csv"
df.to_csv(nombre_archivo, index=False)
print(f" Dataset generado: {nombre_archivo}")


import pandas as pd
import matplotlib.pyplot as plt

# 1. Crear diccionario con datos de servicio de empresa 
servidores_empresa = {
    'id_servidor': ['SRV-01', 'SRV-02', 'SRV-03', 'SRV-04', 'SRV-05', 'SRV-06'],
    'nombre_host': ['web-prod-01', 'db-prod-01', 'app-test-01', 'file-server', 'backup-01', 'mail-server'],
    'sistema_operativo': ['Ubuntu 22.04', 'Windows Server 2022', 'CentOS 8', 'Ubuntu 20.04', 'Debian 11', 'Windows Server 2019'],
    'ram_gb': [32, 128, 16, 64, 32, 32],
    'almacenamiento_tb': [2, 10, 1, 20, 50, 4],
    'ip_address': ['192.168.1.10', '192.168.1.11', '192.168.2.10', '192.168.1.20', '192.168.3.10', '192.168.1.15'],
    'estado': ['Activo', 'Activo', 'Inactivo', 'Activo', 'Activo', 'Activo'],
    'uptime_dias': [120, 365, 0, 200, 400, 150],
    'responsable': ['Carlos', 'Ana', 'Luis', 'Pedro', 'Ana', 'Carlos'],
    'fecha_ultima_parche': ['2024-01-05', '2024-01-05', 'N/A', '2023-12-20', '2024-01-01', '2023-12-15']
}

print("El estudiante aprenderá a realizar un **Análisis Exploratorio de Datos EDA por Emily Barraza NC = 0025")
print("Exploratory Data Analysis por Emily Barraza NC = 0025")
print("5. Crear el diccionario con 10 listas y 6 elementos")

# 2. Convertir diccionario en DataFrame
df = pd.DataFrame(servidores_empresa)
print("\n--- TABLA ORIGINAL DE SERVIDORES ---")
print(df)

# 3. Exportar los datos a CSV
print("+-+-+-+-+-+-Convertir el DataFrame en archivo CSV +-+-+-+-")
df.to_csv(
    'servidores_empresa_0025.csv',
    index=False,
    encoding='utf-8-sig'
)
print("\n✅ Archivo CSV creado correctamente")
print("+-+-+-+-+-+-+- leer los datos desde archivo +-+-+-+-+-+--+-")
print("servidores_empresa_0025.csv")
print("Leer el archivo CSV")

# 4. Leer el archivo CSV
df = pd.read_csv('servidores_empresa_0025.csv')
print("\n--- DATOS LEÍDOS DESDE CSV ---")
print(df)

print("+-+-+-+-+-+-+-Análisis Exploratorio de Datos (EDA)+-+-+-+-+-+-+-+-")
# 5. Primeros y últimos registros
print("+-+-+-+-+-+-+-+ \n1. PRIMEROS REGISTROS (Head): +-+-+-+-+-+-+-+-+")
print(df.head(3))  # Muestra los primeros 3
print("+-+-+-+-+-+-+-+-+ \n2. ÚLTIMOS REGISTROS (Tail): +-+-+-+-+-+-+-+-+")
print(df.tail(2))  # Muestra los últimos 2

# 6. Dimensiones y estructura
print("+-+-+-+-+-+-+ Dimensiones y estructura +-+-+-+-+-+-")
print(df)  # Mostrar tabla o matriz
print("\n3. DIMENSIONES (Filas, Columnas):", df.shape)
print("\n4. NOMBRES DE COLUMNAS:\n", df.columns)
print("\n5. TIPOS DE DATOS:\n", df.dtypes)
print("\n6. INFORMACIÓN GENERAL:")
df.info()

# 7. Estadísticas y limpieza
print("+-+-+-+-+-+-+-+-+- \n7. ESTADÍSTICAS DESCRIPTIVAS: +-+-+-+-+-+-+-+-+-+")
print(df.describe())
print("\n8. VALORES FALTANTES (Nulls):")
print(df.isnull().sum())
print("\n9. REGISTROS DUPLICADOS:")
print(df.duplicated().sum())
print("\n10. VALORES ÚNICOS POR COLUMNA:")
print(df.nunique())
print("Sistemas operativos únicos:", df['sistema_operativo'].unique())

# 8. Análisis específico
print(df)
print("----------------------------------------------------------------------------")
print("+-+-+-+-+-+-+-Análisis específico-+-+-+-+-+-+-")
print("+-+-+-+-+-+-+-\n11. SERVIDORES POR RESPONSABLE:+-+-+-+-+-+-+-+-")
print(df['responsable'].value_counts())
print("\n12. PROMEDIO DE RAM (GB):", df['ram_gb'].mean())
print("13. RAM MÁXIMA (GB):", df['ram_gb'].max())
print("14. RAM MÍNIMA (GB):", df['ram_gb'].min())

# 9. Ordenamiento, filtrado y agrupación
print("+-+-+-+-+-+-+-Ordenamiento, filtrado y agrupación-+-+-+-+-+-+-")

print("+-+-+-+-+-+-\n15. SERVIDORES ORDENADOS POR RAM (Mayor a menor):+-+-+-+-+-+-+-")
print(df.sort_values(by='ram_gb', ascending=False))

print("\n16. SERVIDORES CON RAM MAYOR A 32 GB:")
filtro = df[df['ram_gb'] > 32]
print(filtro)

print("\n17. RESUMEN POR RESPONSABLE:")
resumen = df.groupby('responsable').agg(
    servidores=('id_servidor', 'count'),
    ram_promedio=('ram_gb', 'mean'),
    ram_maxima=('ram_gb', 'max')
)
print(resumen)

# 18. Gráfica de barras: Servidores por responsable
print("18. Gráfica de barras: Servidores por responsable")
conteo = df['responsable'].value_counts()
plt.figure(figsize=(8, 5))
plt.bar(conteo.index, conteo.values, color='skyblue')
plt.title('Servidores por responsable Emily 0025')
plt.xlabel('Responsable')
plt.ylabel('Cantidad de servidores')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 19. Gráfica de barras: Memoria RAM por servidor
print("19. Gráfica de barras: Memoria RAM por servidor")
plt.figure(figsize=(8, 5))
plt.bar(df['nombre_host'], df['ram_gb'], color='lightgreen')
plt.title('Memoria RAM (GB) por servidor EDA por Emily 0025')
plt.xlabel('Servidor (Host)')
plt.ylabel('RAM en GB')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 20. Histograma: Distribución de almacenamiento
plt.figure(figsize=(8, 5))
plt.hist(df['almacenamiento_tb'], bins=5, color='orange', edgecolor='black')
plt.title('Distribución de almacenamiento (TB) EDA Emily 0025')
plt.xlabel('Almacenamiento (TB)')
plt.ylabel('Frecuencia')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 21. Gráfica de dispersión: RAM vs Uptime (días activo)
plt.figure(figsize=(8, 5))
plt.scatter(df['ram_gb'], df['uptime_dias'], color='red', s=100)
plt.title('Relación entre RAM (GB) y Uptime (días) EDA por Emily 0025')
plt.xlabel('RAM (GB)')
plt.ylabel('Días activo (Uptime)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 22. Diagrama de caja: Distribución de Memoria RAM
plt.figure(figsize=(7, 5))
plt.boxplot(df['ram_gb'], patch_artist=True, boxprops=dict(facecolor='lightblue'))
plt.title('Distribución de RAM en GB (Boxplot) EDA Emily 0025')
plt.ylabel('RAM (GB)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 23. Matriz de correlación
correlacion = df.corr(numeric_only=True)
print("\n--- MATRIZ DE CORRELACIÓN ---")
print(correlacion)

plt.figure(figsize=(9, 6))
plt.imshow(correlacion, cmap='coolwarm', vmin=-1, vmax=1)
plt.colorbar()
plt.xticks(range(len(correlacion.columns)), correlacion.columns, rotation=45)
plt.yticks(range(len(correlacion.columns)), correlacion.columns)
plt.title('Matriz de correlación de variables numéricas EDA Emily 0025')
plt.tight_layout()
plt.show()
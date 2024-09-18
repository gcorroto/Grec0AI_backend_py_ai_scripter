# Usar una imagen base ligera de Python
FROM python:3.9-slim

# Instalar las librerías más comunes para la IA
RUN pip install --no-cache-dir matplotlib pillow requests numpy pandas scikit-learn

# Directorio de trabajo para los scripts
WORKDIR /scripts

# Comando por defecto para ejecutar los scripts (puede ser sobrescrito)
CMD ["python", "/scripts/temp_script.py"]

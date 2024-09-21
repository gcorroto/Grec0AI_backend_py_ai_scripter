# Usar una imagen base ligera de Python
FROM python:3.9-slim

# Instalar las librerías más comunes para la IA
RUN pip install --no-cache-dir numpy pandas matplotlib requests pillow opencv-python-headless scikit-image seaborn plotly bokeh scikit-learn tensorflow xgboost lightgbm nltk spacy transformers beautifulsoup4 scrapy networkx scipy statsmodels tqdm

# Directorio de trabajo para los scripts
WORKDIR /scripts

# Comando por defecto para ejecutar los scripts (puede ser sobrescrito)
CMD ["python", "/scripts/temp_script.py"]

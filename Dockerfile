# Dockerfile Mono: todas las dependencias en una sola imagen para procesamiento de video
FROM python:3.9-slim

# Actualizar repositorios e instalar FFmpeg
RUN apt-get update && \
    apt-get install -y ffmpeg && \
    rm -rf /var/lib/apt/lists/*

# Instalar librerías de Python necesarias para las tareas de video (y otras)
RUN pip install --no-cache-dir \
    numpy \
    pandas \
    matplotlib \
    requests \
    pillow \
    opencv-python-headless \
    scikit-image \
    seaborn \
    plotly \
    bokeh \
    scikit-learn \
    tensorflow \
    xgboost \
    lightgbm \
    nltk \
    spacy \
    transformers \
    beautifulsoup4 \
    scrapy \
    networkx \
    scipy \
    statsmodels \
    tqdm \
    moviepy \
    scenedetect

# Establecer el directorio de trabajo para los scripts y archivos
WORKDIR /scripts

# Comando por defecto para ejecutar un script (se puede sobrescribir en tiempo de ejecución)
CMD ["python"]

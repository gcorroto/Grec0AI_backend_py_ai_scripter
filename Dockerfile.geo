# Dockerfile para análisis geoespacial y mapas
FROM python:3.9-slim

# Instalar GDAL y dependencias geoespaciales
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gdal-bin \
    libgdal-dev \
    libspatialindex-dev \
    && rm -rf /var/lib/apt/lists/*

# Variables de entorno para GDAL
ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

# Librerías para análisis geoespacial
RUN pip install --no-cache-dir \
    geopandas \
    shapely \
    folium \
    geopy \
    pyproj \
    rtree \
    contextily \
    mapclassify \
    osmnx \
    matplotlib \
    seaborn \
    plotly \
    geojson \
    h3 \
    s2sphere

WORKDIR /scripts
CMD ["python"]

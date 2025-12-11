#!/bin/bash
# Script para construir todas las imágenes Docker del KPU

REGISTRY="localhost:5000"

echo "🏗️  Construyendo imágenes Docker del KPU GREC0AI..."
echo ""

# Definir todas las imágenes
declare -A IMAGES=(
    ["py-graph"]="Dockerfile.graph"
    ["py-audio"]="Dockerfile.audio"
    ["py-nlp"]="Dockerfile.nlp"
    ["py-ocr"]="Dockerfile.ocr"
    ["py-geo"]="Dockerfile.geo"
    ["py-timeseries"]="Dockerfile.timeseries"
    ["py-web"]="Dockerfile.web"
    ["py-image"]="Dockerfile.image"
    ["py-crypto"]="Dockerfile.crypto"
    ["py-bio"]="Dockerfile.bio"
    ["py-network"]="Dockerfile.network"
    ["py-3d"]="Dockerfile.3d"
    ["py-music"]="Dockerfile.music"
    ["py-mono"]="Dockerfile"
)

# Construir cada imagen
for image_name in "${!IMAGES[@]}"; do
    dockerfile="${IMAGES[$image_name]}"
    echo "📦 Construyendo $image_name desde $dockerfile..."
    docker build -t "$REGISTRY/$image_name:latest" -f "$dockerfile" .
    
    if [ $? -eq 0 ]; then
        echo "✅ $image_name construida exitosamente"
        docker push "$REGISTRY/$image_name:latest"
        echo "✅ $image_name pusheada al registro"
    else
        echo "❌ Error construyendo $image_name"
    fi
    echo ""
done

echo "🎉 Proceso de construcción completado"
echo ""
echo "📋 Listado de imágenes disponibles:"
docker images | grep "$REGISTRY/py-"

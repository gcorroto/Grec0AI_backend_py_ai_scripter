# 🚀 KPU Quick Reference - Cheat Sheet

## 🎯 Selección Rápida de Contenedor

| Tarea | Contenedor | Comando Clave |
|-------|-----------|---------------|
| Hacer gráficos estadísticos | `py-graph` | matplotlib, seaborn |
| Extraer audio de video | `py-audio` | moviepy |
| Análisis de sentimientos | `py-nlp` | transformers |
| OCR en PDF | `py-ocr` | pytesseract |
| Crear mapas | `py-geo` | folium |
| Predecir serie temporal | `py-timeseries` | prophet |
| Scraping web | `py-web` | selenium |
| Detectar rostros | `py-image` | face_recognition |
| Trading crypto | `py-crypto` | ccxt |
| Análisis DNA | `py-bio` | biopython |
| Escanear red | `py-network` | nmap, scapy |
| Analizar modelo 3D | `py-3d` | trimesh |
| Análisis de música | `py-music` | librosa |

---

## 📦 Top Librerías por Contenedor

### py-nlp 💬
```python
transformers      # Modelos BERT, GPT, etc.
spacy            # NLP production-ready
nltk             # Toolkit clásico
gensim           # Topic modeling
textblob         # Sentiment análisis simple
wordcloud        # Nubes de palabras
```

### py-ocr 📄
```python
pytesseract      # OCR Tesseract
pdfplumber       # Extraer PDFs
easyocr          # OCR moderno
openpyxl         # Excel
python-docx      # Word
```

### py-geo 🗺️
```python
folium           # Mapas interactivos
geopandas        # GIS con pandas
geopy            # Geocodificación
osmnx            # OpenStreetMap
```

### py-timeseries 📈
```python
prophet          # Forecasting FB
statsmodels      # ARIMA clásico
tsfresh          # Feature extraction
darts            # Forecasting moderno
```

### py-web 🌐
```python
selenium         # Browser automation
playwright       # Navegación moderna
beautifulsoup4   # HTML parsing
scrapy           # Framework scraping
trafilatura      # Extracción texto
```

### py-image 🖼️
```python
face_recognition # Detección facial
rembg            # Quitar fondo
mediapipe        # Pose detection
qrcode           # Generar QR
albumentations   # Augmentation
```

### py-crypto 💰
```python
ccxt             # 100+ exchanges
yfinance         # Yahoo Finance
pandas_ta        # Indicadores técnicos
web3             # Ethereum
backtrader       # Backtesting
```

### py-music 🎼
```python
librosa          # Análisis audio
music21          # Teoría musical
pretty_midi      # MIDI processing
mido             # MIDI I/O
```

### py-3d 🎲
```python
trimesh          # Mesh processing
pyvista          # 3D plotting
open3d           # 3D data processing
```

### py-network 🔐
```python
scapy            # Packet manipulation
nmap             # Port scanning
paramiko         # SSH
impacket         # Network protocols
```

---

## 💡 Patrones Comunes de Uso

### Pattern 1: Generar y Guardar Imagen
```python
import matplotlib.pyplot as plt

# Tu código de gráfico
plt.plot([1,2,3], [4,5,6])
plt.title('Mi Gráfico')

# SIEMPRE guardar en /scripts/
plt.savefig('/scripts/output.png', dpi=300, bbox_inches='tight')
```

### Pattern 2: Procesar y Retornar Datos
```python
import json

# Procesar datos
results = {"status": "success", "data": [1,2,3]}

# Guardar resultado
with open('/scripts/results.json', 'w') as f:
    json.dump(results, f, indent=2)

# Imprimir para debug
print("Proceso completado")
```

### Pattern 3: Cargar Archivo de Entrada
```python
from PIL import Image

# Cargar desde /scripts/ (volumen compartido)
img = Image.open('/scripts/input_image.jpg')

# Procesar
processed = img.rotate(90)

# Guardar resultado
processed.save('/scripts/output_image.jpg')
```

---

## 🔧 Casos de Uso Avanzados

### Workflow: Análisis Multimedia Completo
1. **py-audio**: Video → Audio
2. **py-music**: Audio → Features
3. **py-nlp**: Transcripción → Análisis
4. **py-graph**: Visualizar resultados

### Workflow: Inteligencia de Negocio
1. **py-web**: Scraping competencia
2. **py-nlp**: Análisis sentimientos
3. **py-timeseries**: Predicción ventas
4. **py-graph**: Dashboard ejecutivo

### Workflow: Procesamiento Documental
1. **py-ocr**: PDF → Texto
2. **py-nlp**: Clasificación documentos
3. **py-graph**: Visualización categorías

---

## ⚡ Tips de Performance

### ✅ DO:
- Guardar SIEMPRE en `/scripts/`
- Usar rutas absolutas
- Especificar encoding UTF-8
- Limpiar recursos (close files)
- Usar `dpi=300` para imágenes

### ❌ DON'T:
- No escribir fuera de `/scripts/`
- No usar rutas relativas
- No instalar librerías en runtime
- No hacer operaciones interactivas
- No usar `plt.show()` (headless)

---

## 🐛 Debugging

### Problema: "Module not found"
**Solución**: Verificar que la librería esté en el Dockerfile correcto

### Problema: "Permission denied"
**Solución**: Usar `/scripts/` como directorio de trabajo

### Problema: "Timeout"
**Solución**: Optimizar código, proceso < 5 minutos

### Problema: "No output file"
**Solución**: Verificar rutas con `/scripts/` prefix

---

## 📊 Tamaños y Tiempos

| Contenedor | Tamaño | Build | Startup |
|------------|--------|-------|---------|
| py-graph | 800MB | 3min | 2s |
| py-audio | 600MB | 2min | 2s |
| py-nlp | 2GB | 8min | 5s |
| py-ocr | 1.5GB | 6min | 3s |
| py-geo | 1GB | 5min | 3s |
| py-timeseries | 900MB | 4min | 3s |
| py-web | 1.2GB | 6min | 4s |
| py-image | 1.5GB | 7min | 3s |
| py-crypto | 700MB | 3min | 2s |
| py-bio | 600MB | 3min | 2s |
| py-network | 800MB | 4min | 2s |
| py-3d | 900MB | 4min | 3s |
| py-music | 1GB | 5min | 3s |

---

## 🎓 Ejemplos Mínimos

### NLP - Sentiment
```python
from transformers import pipeline
s = pipeline('sentiment-analysis')
print(s("I love this!"))
```

### OCR - PDF
```python
import pdfplumber
with pdfplumber.open('/scripts/doc.pdf') as pdf:
    print(pdf.pages[0].extract_text())
```

### GEO - Mapa
```python
import folium
m = folium.Map(location=[40.4168, -3.7038])
m.save('/scripts/map.html')
```

### Crypto - Precio
```python
import ccxt
ex = ccxt.binance()
print(ex.fetch_ticker('BTC/USDT'))
```

### Image - Remover Fondo
```python
from rembg import remove
from PIL import Image
img = Image.open('/scripts/in.jpg')
remove(img).save('/scripts/out.png')
```

---

## 🚀 Build All Images - One Liner

```bash
cd Grec0AI_backend_py_ai_scripter && ./build-all-images.sh
```

---

## 📞 Selector Automático

```python
from container_selector import ContainerSelector

code = "from transformers import pipeline"
container, scores = ContainerSelector.select_container(code)
print(f"Usar: {container}")  # Output: py-nlp
```

---

## 🎯 Decisión Rápida

**¿Texto/Lenguaje?** → py-nlp  
**¿Documento/PDF?** → py-ocr  
**¿Ubicaciones/Mapas?** → py-geo  
**¿Predicción/Tiempo?** → py-timeseries  
**¿Scraping/Web?** → py-web  
**¿Imagen/Foto?** → py-image  
**¿Trading/Finanzas?** → py-crypto  
**¿DNA/Biología?** → py-bio  
**¿Red/Seguridad?** → py-network  
**¿3D/Modelos?** → py-3d  
**¿Música/Audio?** → py-music  
**¿Video/Multimedia?** → py-audio  
**¿Gráficos/Viz?** → py-graph  

---

**Última actualización**: 2025-11-29
**Versión KPU**: 2.0

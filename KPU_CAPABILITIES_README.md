# 🧠 KPU (Knowledge Processing Unit) - Sistema de Capacidades Computacionales

## 📋 Resumen
El KPU de GREC0AI permite al agente de IA ejecutar código Python especializado en contenedores Docker aislados, desgranando cualquier tarea compleja en pequeñas operaciones atómicas altamente especializadas.

---

## 🎯 IMÁGENES DOCKER DISPONIBLES

### **1. py-graph** 📊
**Propósito:** Visualización de datos y gráficos estadísticos

**Capacidades:**
- Gráficos matplotlib, seaborn, plotly, bokeh
- Análisis de redes con networkx
- Diagramas con graphviz
- Estadísticas avanzadas

**Casos de uso:**
```python
# Análisis de correlaciones
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('/scripts/data.csv')
sns.heatmap(df.corr(), annot=True)
plt.savefig('/scripts/correlation_matrix.png')
```

---

### **2. py-audio** 🎵
**Propósito:** Procesamiento de audio y video

**Capacidades:**
- Extracción de audio de videos (FFmpeg)
- Conversión de formatos
- Análisis básico de audio
- MoviePy para edición

**Casos de uso:**
```python
# Extraer audio de video
from moviepy.editor import VideoFileClip
video = VideoFileClip('/scripts/video.mp4')
video.audio.write_audiofile('/scripts/audio.mp3')
```

---

### **3. py-nlp** 💬 ⭐ NUEVA
**Propósito:** Procesamiento avanzado de lenguaje natural

**Capacidades:**
- Modelos transformer (BERT, GPT)
- spaCy (NER, POS tagging)
- Análisis de sentimientos
- Traducción automática
- Generación de embeddings
- Word clouds
- Detección de idiomas

**Casos de uso:**
```python
# Análisis de sentimientos
from transformers import pipeline
sentiment = pipeline('sentiment-analysis', model='nlptown/bert-base-multilingual-uncased-sentiment')
result = sentiment("Este producto es excelente")
print(result)

# NER con spaCy
import spacy
nlp = spacy.load('es_core_news_sm')
doc = nlp("Juan vive en Madrid")
for ent in doc.ents:
    print(ent.text, ent.label_)
```

---

### **4. py-ocr** 📄 ⭐ NUEVA
**Propósito:** OCR y procesamiento de documentos

**Capacidades:**
- Tesseract OCR (español/inglés)
- EasyOCR
- Extracción de texto de PDFs
- Procesamiento de Excel/Word
- Extracción de tablas
- Conversión de documentos

**Casos de uso:**
```python
# OCR en imagen
import pytesseract
from PIL import Image
text = pytesseract.image_to_string(Image.open('/scripts/document.png'), lang='spa')

# Extraer tablas de PDF
import pdfplumber
with pdfplumber.open('/scripts/report.pdf') as pdf:
    table = pdf.pages[0].extract_table()
```

---

### **5. py-geo** 🗺️ ⭐ NUEVA
**Propósito:** Análisis geoespacial y cartografía

**Capacidades:**
- Mapas interactivos con Folium
- Análisis de shapefiles
- Geocodificación
- Cálculos de distancias
- Rutas óptimas
- OpenStreetMap

**Casos de uso:**
```python
# Crear mapa interactivo
import folium
m = folium.Map(location=[40.4168, -3.7038], zoom_start=13)
folium.Marker([40.4168, -3.7038], popup='Madrid').add_to(m)
m.save('/scripts/map.html')

# Geocodificación
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="grec0ai")
location = geolocator.geocode("Gran Vía, Madrid")
print(location.latitude, location.longitude)
```

---

### **6. py-timeseries** 📈 ⭐ NUEVA
**Propósito:** Análisis de series temporales y forecasting

**Capacidades:**
- Prophet (Facebook)
- ARIMA/SARIMA
- Detección de anomalías
- Descomposición de series
- Predicciones automáticas
- Análisis de estacionalidad

**Casos de uso:**
```python
# Predicción con Prophet
from prophet import Prophet
import pandas as pd

df = pd.read_csv('/scripts/sales.csv')
model = Prophet()
model.fit(df)
future = model.make_future_dataframe(periods=30)
forecast = model.predict(future)
```

---

### **7. py-web** 🌐 ⭐ NUEVA
**Propósito:** Web scraping y automatización web

**Capacidades:**
- Selenium + Chromium
- Playwright (navegación headless)
- BeautifulSoup + Scrapy
- Extracción de noticias
- Bypass de Cloudflare
- Automatización de formularios

**Casos de uso:**
```python
# Scraping con Selenium
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.get('https://example.com')
content = driver.page_source

# Extracción de noticias
import trafilatura
downloaded = trafilatura.fetch_url('https://news.com/article')
text = trafilatura.extract(downloaded)
```

---

### **8. py-image** 🖼️ ⭐ NUEVA
**Propósito:** Procesamiento avanzado de imágenes

**Capacidades:**
- Detección de rostros
- Remoción de fondo (rembg)
- QR codes
- Augmentation de imágenes
- Reconocimiento facial
- MediaPipe (pose detection)
- Filtros avanzados

**Casos de uso:**
```python
# Remover fondo
from rembg import remove
from PIL import Image
input_img = Image.open('/scripts/photo.jpg')
output = remove(input_img)
output.save('/scripts/no_background.png')

# Detección facial
import face_recognition
image = face_recognition.load_image_file('/scripts/people.jpg')
face_locations = face_recognition.face_locations(image)
```

---

### **9. py-crypto** 💰 ⭐ NUEVA
**Propósito:** Análisis de criptomonedas y trading

**Capacidades:**
- CCXT (100+ exchanges)
- Análisis técnico (TA-Lib)
- Backtesting
- Web3 (Ethereum)
- Indicadores financieros
- Datos históricos

**Casos de uso:**
```python
# Obtener precio de Bitcoin
import ccxt
exchange = ccxt.binance()
ticker = exchange.fetch_ticker('BTC/USDT')
print(f"Bitcoin: ${ticker['last']}")

# Análisis técnico
import pandas_ta as ta
df['RSI'] = ta.rsi(df['close'], length=14)
df['MACD'] = ta.macd(df['close'])
```

---

### **10. py-bio** 🧬 ⭐ NUEVA
**Propósito:** Bioinformática y análisis de secuencias

**Capacidades:**
- Análisis de secuencias DNA/RNA
- Alineamiento de secuencias
- Árboles filogenéticos
- Parseo de formatos biológicos
- Análisis de variantes

**Casos de uso:**
```python
# Análisis de secuencia DNA
from Bio.Seq import Seq
dna_seq = Seq("AGTACACTGGT")
print(f"RNA: {dna_seq.transcribe()}")
print(f"Protein: {dna_seq.translate()}")

# Análisis de secuencias
from Bio import SeqIO
for record in SeqIO.parse('/scripts/genome.fasta', 'fasta'):
    print(record.id, len(record))
```

---

### **11. py-network** 🔐 ⭐ NUEVA
**Propósito:** Análisis de redes y seguridad

**Capacidades:**
- Escaneo de puertos (nmap)
- Análisis de paquetes (Scapy)
- Sniffing de red
- Criptografía
- SSH automation
- Análisis de tráfico

**Casos de uso:**
```python
# Escaneo de puertos
import nmap
nm = nmap.PortScanner()
nm.scan('192.168.1.1', '22-443')

# Análisis de paquetes
from scapy.all import *
packets = sniff(count=10)
packets.summary()
```

---

### **12. py-3d** 🎲 ⭐ NUEVA
**Propósito:** Modelado 3D y geometría computacional

**Capacidades:**
- Manipulación de meshes
- Visualización 3D
- Conversión de formatos 3D
- Geometría computacional
- Análisis de modelos STL

**Casos de uso:**
```python
# Cargar y analizar modelo 3D
import trimesh
mesh = trimesh.load('/scripts/model.stl')
print(f"Volumen: {mesh.volume}")
print(f"Área: {mesh.area}")
mesh.export('/scripts/output.obj')
```

---

### **13. py-music** 🎼 ⭐ NUEVA
**Propósito:** Análisis y generación de música

**Capacidades:**
- Análisis de audio (librosa)
- Extracción de features musicales
- Detección de tempo/ritmo
- Separación de stems
- Procesamiento MIDI
- Teoría musical

**Casos de uso:**
```python
# Análisis de audio
import librosa
y, sr = librosa.load('/scripts/song.mp3')
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
print(f"Tempo: {tempo} BPM")

# Separación de fuentes
chroma = librosa.feature.chroma_stft(y=y, sr=sr)
```

---

### **14. py-mono** 🎯
**Propósito:** Contenedor todoterreno (legacy)

**Capacidades:** Combinación de múltiples librerías para tareas generales.

---

## 🚀 CÓMO CONSTRUIR LAS IMÁGENES

```bash
cd Grec0AI_backend_py_ai_scripter
chmod +x build-all-images.sh
./build-all-images.sh
```

O construir individualmente:
```bash
docker build -t localhost:5000/py-nlp -f Dockerfile.nlp .
docker push localhost:5000/py-nlp
```

---

## 📊 MATRIZ DE CAPACIDADES

| Contenedor | Tamaño | Build Time | Casos de Uso Principales |
|------------|--------|------------|--------------------------|
| py-graph | ~800MB | 3min | Visualización, estadística |
| py-audio | ~600MB | 2min | Procesamiento multimedia |
| py-nlp | ~2GB | 8min | NLP, transformers, text mining |
| py-ocr | ~1.5GB | 6min | OCR, documentos, PDFs |
| py-geo | ~1GB | 5min | Mapas, geolocalización |
| py-timeseries | ~900MB | 4min | Forecasting, anomalías |
| py-web | ~1.2GB | 6min | Scraping, automation |
| py-image | ~1.5GB | 7min | Computer vision, rostros |
| py-crypto | ~700MB | 3min | Trading, blockchain |
| py-bio | ~600MB | 3min | Bioinformática, DNA |
| py-network | ~800MB | 4min | Pentesting, análisis red |
| py-3d | ~900MB | 4min | Modelado 3D, CAD |
| py-music | ~1GB | 5min | Audio analysis, MIDI |

---

## 🎯 EJEMPLOS DE WORKFLOWS COMPLEJOS

### **Workflow 1: Análisis Multimedia Completo**
1. **py-audio**: Extraer audio de video
2. **py-music**: Analizar tempo y características
3. **py-nlp**: Transcribir y analizar texto
4. **py-graph**: Visualizar resultados

### **Workflow 2: Inteligencia de Mercado**
1. **py-web**: Scraping de noticias financieras
2. **py-nlp**: Análisis de sentimiento
3. **py-crypto**: Obtener datos de mercado
4. **py-timeseries**: Predecir tendencias
5. **py-graph**: Dashboard final

### **Workflow 3: Documentación Inteligente**
1. **py-ocr**: Extraer texto de PDFs escaneados
2. **py-nlp**: Clasificar y resumir
3. **py-graph**: Generar visualizaciones
4. **py-web**: Publicar resultados

---

## 🔮 FUTURAS EXPANSIONES POSIBLES

- **py-quantum**: Computación cuántica (Qiskit)
- **py-robotics**: ROS, control de robots
- **py-medical**: Análisis de imágenes médicas (DICOM)
- **py-gaming**: Desarrollo de juegos (Pygame, Unity ML)
- **py-iot**: IoT, Arduino, sensores
- **py-social**: Análisis de redes sociales
- **py-legal**: Procesamiento de documentos legales
- **py-voice**: Síntesis y reconocimiento de voz

---

## 📝 NOTAS DE IMPLEMENTACIÓN

### Ventajas del Sistema:
✅ **Aislamiento**: Cada contenedor es independiente
✅ **Especialización**: Librerías optimizadas por dominio
✅ **Escalabilidad**: Fácil añadir nuevas capacidades
✅ **Seguridad**: Ejecución en sandbox
✅ **Modularidad**: Combinar contenedores según necesidad

### Consideraciones:
⚠️ Tamaño total: ~13GB de imágenes
⚠️ Tiempo de build inicial: ~1 hora
⚠️ Consumo de RAM: 200-500MB por ejecución
⚠️ Cache de Docker recomendado: >50GB

---

## 🎓 CONCLUSIÓN

El KPU de GREC0AI transforma al agente en un **sistema computacional universal** capaz de:
- 📊 Analizar cualquier tipo de dato
- 🎨 Generar visualizaciones complejas
- 🤖 Aplicar IA/ML especializada
- 🌐 Interactuar con la web
- 💾 Procesar documentos
- 🔒 Análisis de seguridad
- 🧬 Bioinformática
- 💰 Trading automático

**Capacidades actuales: 14 dominios especializados**
**Posibilidades futuras: Infinitas** 🚀

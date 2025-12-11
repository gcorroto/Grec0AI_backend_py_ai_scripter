# -*- coding: utf-8 -*-
"""
Ejemplos de uso del KPU con diferentes contenedores especializados
"""

# ============================================
# 1. PY-NLP: Análisis de Sentimientos
# ============================================
nlp_sentiment = """
from transformers import pipeline
import matplotlib.pyplot as plt

# Analizar sentimientos de reseñas
reviews = [
    "Este producto es excelente, lo recomiendo totalmente",
    "Muy mala calidad, no vale la pena",
    "Está bien, cumple su función pero nada especial"
]

sentiment_pipeline = pipeline("sentiment-analysis", 
                              model="nlptown/bert-base-multilingual-uncased-sentiment")

results = []
for review in reviews:
    result = sentiment_pipeline(review)[0]
    results.append(result)
    print(f"Review: {review[:50]}...")
    print(f"Score: {result['label']} - Confidence: {result['score']:.2f}\\n")

# Guardar resultados
with open('/scripts/sentiment_results.txt', 'w') as f:
    for i, (review, result) in enumerate(zip(reviews, results)):
        f.write(f"Review {i+1}: {result['label']} ({result['score']:.2f})\\n")
"""

# ============================================
# 2. PY-OCR: Extraer Texto de PDF
# ============================================
ocr_pdf = """
import pdfplumber
import pytesseract
from PIL import Image
import json

# Extraer texto de PDF con tablas
pdf_path = '/scripts/document.pdf'
results = {
    'text': [],
    'tables': []
}

with pdfplumber.open(pdf_path) as pdf:
    for i, page in enumerate(pdf.pages):
        # Extraer texto
        text = page.extract_text()
        results['text'].append(f"--- Página {i+1} ---\\n{text}")
        
        # Extraer tablas
        tables = page.extract_tables()
        if tables:
            results['tables'].append({
                'page': i+1,
                'count': len(tables),
                'data': tables
            })

# Guardar resultados
with open('/scripts/extracted_data.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"Extraídas {len(results['text'])} páginas")
print(f"Encontradas {sum(t['count'] for t in results['tables'])} tablas")
"""

# ============================================
# 3. PY-GEO: Mapa de Tiendas
# ============================================
geo_map = """
import folium
import pandas as pd
from geopy.distance import geodesic

# Coordenadas de tiendas
stores = pd.DataFrame({
    'name': ['Tienda Centro', 'Tienda Norte', 'Tienda Sur'],
    'lat': [40.4168, 40.4500, 40.3900],
    'lon': [-3.7038, -3.7000, -3.7100]
})

# Crear mapa centrado en Madrid
m = folium.Map(location=[40.4168, -3.7038], zoom_start=12)

# Añadir marcadores
for idx, store in stores.iterrows():
    folium.Marker(
        [store['lat'], store['lon']],
        popup=store['name'],
        tooltip=store['name'],
        icon=folium.Icon(color='red', icon='shopping-cart', prefix='fa')
    ).add_to(m)

# Calcular distancias entre tiendas
center = (stores.iloc[0]['lat'], stores.iloc[0]['lon'])
for idx, store in stores.iterrows():
    point = (store['lat'], store['lon'])
    distance = geodesic(center, point).kilometers
    print(f"{store['name']}: {distance:.2f} km del centro")

# Guardar mapa
m.save('/scripts/stores_map.html')
print("Mapa guardado en stores_map.html")
"""

# ============================================
# 4. PY-TIMESERIES: Predicción de Ventas
# ============================================
timeseries_forecast = """
from prophet import Prophet
import pandas as pd
import matplotlib.pyplot as plt

# Datos de ejemplo de ventas diarias
dates = pd.date_range('2023-01-01', periods=365, freq='D')
sales = pd.DataFrame({
    'ds': dates,
    'y': [100 + i*0.5 + (i%30)*2 for i in range(365)]  # Tendencia + estacionalidad
})

# Entrenar modelo Prophet
model = Prophet(yearly_seasonality=True, weekly_seasonality=True)
model.fit(sales)

# Predecir próximos 90 días
future = model.make_future_dataframe(periods=90)
forecast = model.predict(future)

# Visualizar
fig = model.plot(forecast)
plt.title('Predicción de Ventas - Próximos 90 días')
plt.savefig('/scripts/sales_forecast.png', dpi=300, bbox_inches='tight')

# Guardar predicciones
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(90).to_csv(
    '/scripts/predictions.csv', index=False
)

print("Predicción completada. Archivos generados:")
print("- sales_forecast.png")
print("- predictions.csv")
"""

# ============================================
# 5. PY-WEB: Scraping de Noticias
# ============================================
web_scraping = """
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import json
import time

# Configurar navegador headless
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)

# Scraping de ejemplo
url = 'https://news.ycombinator.com'
driver.get(url)
time.sleep(2)

# Extraer títulos
titles = driver.find_elements(By.CLASS_NAME, 'titleline')
news = []

for i, title in enumerate(titles[:10]):
    try:
        link = title.find_element(By.TAG_NAME, 'a')
        news.append({
            'position': i+1,
            'title': link.text,
            'url': link.get_attribute('href')
        })
    except:
        pass

driver.quit()

# Guardar resultados
with open('/scripts/scraped_news.json', 'w', encoding='utf-8') as f:
    json.dump(news, f, ensure_ascii=False, indent=2)

print(f"Extraídas {len(news)} noticias")
"""

# ============================================
# 6. PY-IMAGE: Detección de Rostros
# ============================================
image_face_detection = """
import face_recognition
import cv2
import numpy as np
from PIL import Image

# Cargar imagen
image_path = '/scripts/group_photo.jpg'
image = face_recognition.load_image_file(image_path)

# Detectar rostros
face_locations = face_recognition.face_locations(image)
face_encodings = face_recognition.face_encodings(image, face_locations)

print(f"Encontrados {len(face_locations)} rostros")

# Dibujar rectángulos en los rostros
image_cv2 = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
for (top, right, bottom, left) in face_locations:
    cv2.rectangle(image_cv2, (left, top), (right, bottom), (0, 255, 0), 2)

# Guardar imagen con detecciones
cv2.imwrite('/scripts/faces_detected.jpg', image_cv2)

# Metadata
with open('/scripts/face_detection_report.txt', 'w') as f:
    f.write(f"Total de rostros detectados: {len(face_locations)}\\n")
    for i, loc in enumerate(face_locations):
        f.write(f"Rostro {i+1}: {loc}\\n")
"""

# ============================================
# 7. PY-CRYPTO: Análisis de Mercado
# ============================================
crypto_analysis = """
import ccxt
import pandas as pd
import matplotlib.pyplot as plt
import pandas_ta as ta

# Conectar a Binance
exchange = ccxt.binance()

# Obtener datos históricos de Bitcoin
ohlcv = exchange.fetch_ohlcv('BTC/USDT', '1h', limit=168)  # 1 semana
df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

# Calcular indicadores técnicos
df['RSI'] = ta.rsi(df['close'], length=14)
macd = ta.macd(df['close'])
df['MACD'] = macd['MACD_12_26_9']
df['Signal'] = macd['MACDs_12_26_9']

# Visualizar
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 10))

# Precio
ax1.plot(df['timestamp'], df['close'], label='BTC/USDT')
ax1.set_title('Bitcoin Price (Last 7 Days)')
ax1.legend()

# RSI
ax2.plot(df['timestamp'], df['RSI'], label='RSI', color='orange')
ax2.axhline(70, color='red', linestyle='--', alpha=0.5)
ax2.axhline(30, color='green', linestyle='--', alpha=0.5)
ax2.set_title('RSI')
ax2.legend()

# MACD
ax3.plot(df['timestamp'], df['MACD'], label='MACD')
ax3.plot(df['timestamp'], df['Signal'], label='Signal')
ax3.set_title('MACD')
ax3.legend()

plt.tight_layout()
plt.savefig('/scripts/crypto_analysis.png', dpi=300)

# Resumen
print(f"Precio actual: ${df['close'].iloc[-1]:.2f}")
print(f"RSI: {df['RSI'].iloc[-1]:.2f}")
print(f"MACD: {df['MACD'].iloc[-1]:.2f}")
"""

# ============================================
# 8. PY-MUSIC: Análisis de Audio
# ============================================
music_analysis = """
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# Cargar audio
audio_path = '/scripts/song.mp3'
y, sr = librosa.load(audio_path, duration=30)  # Primeros 30 segundos

# Análisis básico
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
beat_times = librosa.frames_to_time(beat_frames, sr=sr)

# Extraer características
chroma = librosa.feature.chroma_stft(y=y, sr=sr)
spectral_centroids = librosa.feature.spectral_centroid(y=y, sr=sr)

# Visualizar
fig, ax = plt.subplots(3, 1, figsize=(12, 10))

# Forma de onda
librosa.display.waveshow(y, sr=sr, ax=ax[0])
ax[0].set_title('Waveform')
ax[0].vlines(beat_times, -1, 1, color='r', alpha=0.3, label='Beats')

# Chroma
img = librosa.display.specshow(chroma, y_axis='chroma', x_axis='time', ax=ax[1])
ax[1].set_title('Chromagram')
fig.colorbar(img, ax=ax[1])

# Spectral Centroid
frames = range(len(spectral_centroids[0]))
t = librosa.frames_to_time(frames, sr=sr)
ax[2].plot(t, spectral_centroids[0])
ax[2].set_title('Spectral Centroid')
ax[2].set_xlabel('Time (s)')

plt.tight_layout()
plt.savefig('/scripts/audio_analysis.png', dpi=300)

# Resumen
print(f"Tempo: {tempo:.2f} BPM")
print(f"Total beats detectados: {len(beat_times)}")
print(f"Duración analizada: {len(y)/sr:.2f} segundos")
"""

# ============================================
# 9. PY-3D: Análisis de Modelo STL
# ============================================
model_3d_analysis = """
import trimesh
import numpy as np

# Cargar modelo 3D
mesh = trimesh.load('/scripts/model.stl')

# Análisis geométrico
print("=== Análisis de Modelo 3D ===")
print(f"Volumen: {mesh.volume:.2f} unidades³")
print(f"Área superficial: {mesh.area:.2f} unidades²")
print(f"Centro de masa: {mesh.center_mass}")
print(f"Número de vértices: {len(mesh.vertices)}")
print(f"Número de caras: {len(mesh.faces)}")

# Verificar si el modelo es sólido
print(f"¿Es estanco?: {mesh.is_watertight}")
print(f"¿Es convexo?: {mesh.is_convex}")

# Exportar a diferentes formatos
mesh.export('/scripts/model.obj')
mesh.export('/scripts/model.ply')

# Generar reporte
with open('/scripts/3d_analysis_report.txt', 'w') as f:
    f.write("REPORTE DE ANÁLISIS 3D\\n")
    f.write("="*50 + "\\n")
    f.write(f"Volumen: {mesh.volume:.2f}\\n")
    f.write(f"Área: {mesh.area:.2f}\\n")
    f.write(f"Vértices: {len(mesh.vertices)}\\n")
    f.write(f"Caras: {len(mesh.faces)}\\n")
    f.write(f"Bounds: {mesh.bounds}\\n")

print("Análisis completado")
"""

# ============================================
# 10. PY-GRAPH: Dashboard Completo
# ============================================
graph_dashboard = """
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Datos de ejemplo
np.random.seed(42)
data = pd.DataFrame({
    'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'] * 3,
    'category': ['A']*6 + ['B']*6 + ['C']*6,
    'sales': np.random.randint(100, 500, 18),
    'profit': np.random.randint(20, 100, 18)
})

# Crear dashboard con múltiples gráficos
fig = plt.figure(figsize=(16, 10))
gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)

# 1. Ventas por categoría (Bar)
ax1 = fig.add_subplot(gs[0, :2])
sales_by_cat = data.groupby('category')['sales'].sum()
sales_by_cat.plot(kind='bar', ax=ax1, color=['#FF6B6B', '#4ECDC4', '#45B7D1'])
ax1.set_title('Ventas Totales por Categoría', fontsize=14, fontweight='bold')
ax1.set_xlabel('Categoría')
ax1.set_ylabel('Ventas')

# 2. KPI Card
ax2 = fig.add_subplot(gs[0, 2])
ax2.axis('off')
total_sales = data['sales'].sum()
avg_profit = data['profit'].mean()
ax2.text(0.5, 0.7, f'${total_sales:,}', ha='center', va='center', 
         fontsize=24, fontweight='bold', color='#2C3E50')
ax2.text(0.5, 0.4, 'Ventas Totales', ha='center', va='center', 
         fontsize=12, color='#7F8C8D')
ax2.text(0.5, 0.1, f'{avg_profit:.1f}% Profit Avg', ha='center', va='center',
         fontsize=10, color='#27AE60')

# 3. Tendencia temporal (Line)
ax3 = fig.add_subplot(gs[1, :])
for cat in data['category'].unique():
    cat_data = data[data['category'] == cat]
    ax3.plot(cat_data['month'], cat_data['sales'], marker='o', label=cat)
ax3.set_title('Tendencia de Ventas por Mes', fontsize=14, fontweight='bold')
ax3.legend()
ax3.grid(alpha=0.3)

# 4. Correlación (Heatmap)
ax4 = fig.add_subplot(gs[2, 0])
corr_data = data[['sales', 'profit']].corr()
sns.heatmap(corr_data, annot=True, cmap='coolwarm', center=0, ax=ax4)
ax4.set_title('Correlación', fontsize=12, fontweight='bold')

# 5. Distribución (Histogram)
ax5 = fig.add_subplot(gs[2, 1])
ax5.hist(data['sales'], bins=15, color='#3498DB', alpha=0.7, edgecolor='black')
ax5.set_title('Distribución de Ventas', fontsize=12, fontweight='bold')
ax5.set_xlabel('Ventas')
ax5.set_ylabel('Frecuencia')

# 6. Scatter
ax6 = fig.add_subplot(gs[2, 2])
colors = {'A': '#FF6B6B', 'B': '#4ECDC4', 'C': '#45B7D1'}
for cat in data['category'].unique():
    cat_data = data[data['category'] == cat]
    ax6.scatter(cat_data['sales'], cat_data['profit'], 
                label=cat, color=colors[cat], s=100, alpha=0.6)
ax6.set_title('Ventas vs Profit', fontsize=12, fontweight='bold')
ax6.set_xlabel('Ventas')
ax6.set_ylabel('Profit')
ax6.legend()

plt.suptitle('Dashboard de Análisis de Negocio', 
             fontsize=18, fontweight='bold', y=0.98)

plt.savefig('/scripts/business_dashboard.png', dpi=300, bbox_inches='tight')
print("Dashboard generado exitosamente")
"""


# Mapeo de ejemplos a contenedores
EXAMPLES = {
    'py-nlp': nlp_sentiment,
    'py-ocr': ocr_pdf,
    'py-geo': geo_map,
    'py-timeseries': timeseries_forecast,
    'py-web': web_scraping,
    'py-image': image_face_detection,
    'py-crypto': crypto_analysis,
    'py-music': music_analysis,
    'py-3d': model_3d_analysis,
    'py-graph': graph_dashboard,
}

if __name__ == "__main__":
    print("=== EJEMPLOS DE USO DEL KPU ===\n")
    for container, code in EXAMPLES.items():
        print(f"🐳 {container.upper()}")
        print(f"Código: {len(code)} caracteres")
        print(f"Líneas: {len(code.split(chr(10)))} líneas")
        print("-" * 50)

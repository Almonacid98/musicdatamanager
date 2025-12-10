# 🎵 musicdatamanager

**musicdatamanager** es una aplicación de línea de comandos diseñada para gestionar, consultar y actualizar información proveniente del archivo `spotify_and_youtube 2024.csv`.  
Incluye búsqueda avanzada, inserción de registros con validaciones, estadísticas por artista y álbum, y herramientas para visualizar información ordenada de manera clara.

---

## 🚀 Funcionalidades principales

### 🔍 Buscar por título o artista
- Permite buscar canciones por nombre del tema o nombre del artista.  
- Búsqueda **case-insensitive** y por coincidencia parcial.  
- Resultados ordenados por cantidad de reproducciones (descendente).  
- Cada resultado muestra:
  - Artista  
  - Canción  
  - Duración (formato **HH:MM:SS**)

---

### ⭐ Top 10 canciones de un artista
Dado un artista, el programa muestra sus **10 temas más reproducidos**, incluyendo:
- Nombre del artista  
- Nombre del tema  
- Duración (HH:MM:SS)  
- Reproducciones (en millones)

---

### ➕ Inserción de registros
Se pueden agregar nuevos registros de dos formas:

#### 1️⃣ Inserción manual  
Desde la terminal ingresando:
- Artista  
- Track  
- Álbum  
- URI de Spotify  
- Duración (convertida automáticamente a milisegundos)  
- URL de Spotify  
- URL de YouTube  
- Likes  
- Views (validando que *likes ≤ views*)

#### 2️⃣ Inserción masiva (batch)  
Mediante un archivo `.csv` con múltiples registros.

Todos los campos son validados mediante **expresiones regulares** para asegurar consistencia y formato correcto.

---

### 💿 Mostrar álbumes de un artista
Al seleccionar un artista se muestra:
- Cantidad total de álbumes  
- Para cada álbum:
  - Nombre del álbum  
  - Cantidad de canciones  
  - Duración total del álbum (formato HH:MM:SS)

---

## 🛠️ Tecnologías y herramientas
- Python
- Manejo de archivos `.csv`
- Expresiones regulares (Regex)
- Conversión y formateo de tiempos
- Estructuras de datos y ordenamiento
  
---

## 👥 Integrante

| Integrante |
|-----------|
| [<img src="https://avatars.githubusercontent.com/u/49103419?v=4" width="115"><br><sub>Almonacid Gabriel</sub>](https://github.com/Almonacid98) |

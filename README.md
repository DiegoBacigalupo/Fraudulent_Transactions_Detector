
# FraudGuard AI - Deteccion de transacciones Fraudulentas

**Versiones:**
*
## Versión 1:
   **Descripción:** Implementa la funcionalidad base para ingresar datos de una transacción y obtener una predicción de fraude utilizando un modelo de Machine Learning y un análisis de OpenAI.
  
*   
## Versión 2 :
     FraudGuard AI - Detección de Fraudes (Versión 2)

## Descripción General

Esta aplicación combina el poder del Machine Learning (ML) y la Inteligencia Artificial (IA) para detectar transacciones fraudulentas.

Permite a los usuarios cargar sus propios datasets, entrenar modelos de ML y obtener análisis detallados de transacciones de alto riesgo utilizando la API de OpenAI.

## Funcionalidades

* **Carga de Datasets:**
    * Los usuarios pueden cargar archivos CSV que contienen datos de transacciones.
* **Entrenamiento del Modelo de Machine Learning:**
    * Los usuarios pueden cargar un dataset con la columna objetivo (que indica si una transacción es fraudulenta) para entrenar un modelo de ML personalizado.
    * Opción para reentrenar un modelo existente con nuevos datos o entrenar un modelo desde cero.
* **Predicción de Fraudes:**
    * Los usuarios pueden cargar un dataset sin la columna objetivo para que el modelo de ML prediga qué transacciones son fraudulentas.
    * La aplicación muestra una lista de las transacciones clasificadas como fraudulentas.
* **Análisis Detallado con IA:**
    * Para las transacciones de alta probabilidad de fraude, la aplicación utiliza la API de OpenAI para generar un análisis detallado.
    * La respuesta de OpenAI incluye una evaluación de la probabilidad de fraude (baja, media o alta) y una explicación de los factores que contribuyen a la evaluación.
    * Botón para expandir la explicación generada por la IA.
## Optimización de Recursos

* El modelo de ML se utiliza para realizar una predicción inicial y filtrar las transacciones de alto riesgo.
* La API de OpenAI se utiliza solo para analizar las transacciones de alto riesgo, lo que reduce el consumo de tokens y los costos.

* 

* **Versión 3 (Próximamente):**
    * [Aquí se describirá la Versión 3 cuando esté lista]

**Instalación:**

1.  Clona el repositorio: `git clone <URL_DE_TU_REPOSITORIO>`
2.  Navega al directorio del proyecto: `cd FraudGuard-AI`
3.  Crea y activa el entorno virtual (recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Linux/macOS
    venv\Scripts\activate    # En Windows
    ```
4.  Instala las dependencias: `pip install -r requirements.txt` (si tienes un archivo `requirements.txt`) o `pip install pandas scikit-learn openai streamlit`
5.  Ejecuta la aplicación: `streamlit run main.py`

**Dependencias:**

* pandas
* scikit-learn
* openai

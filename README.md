
# FraudGuard AI - Deteccion de transacciones Fraudulentas


## Versión 1:
  FraudGuard AI - Detección de Fraudes (Versión 1) - Prototipo 

## Descripción General:

La versión 1 de FraudGuard AI es un prototipo básico para la detección de fraudes. Su funcionalidad es muy limitada y se utiliza principalmente para demostrar el concepto de detección de fraudes utilizando un modelo de Machine Learning pre-entrenado y la API de OpenAI en un entorno controlado.

## Funcionalidades Limitadas:

* **Entrada de Datos Estática:**
    * El usuario solo puede seleccionar valores de un conjunto de datos predefinido a través de una interfaz simple en Streamlit.
    * No existe la posibilidad de cargar datos externos o personalizados.
* **Predicción Binaria con Modelo Pre-entrenado:**
    * Un modelo de Machine Learning (RandomForestClassifier) ya entrenado realiza una predicción binaria: "Fraude" o "No fraude".
    * El usuario no tiene control sobre el modelo ni puede modificarlo.
* **Análisis Textual Limitado con OpenAI:**
    * La API de OpenAI (gpt-3.5-turbo) proporciona un análisis textual básico de la transacción.
    * Este análisis está limitado por las capacidades del modelo y la información proporcionada.

## Limitaciones Críticas:

* **Conjunto de Datos Fijo:**
    * El análisis se restringe completamente al conjunto de datos predefinido en el código.
    * Esto limita drásticamente la aplicabilidad y utilidad de la aplicación.
* **Modelo de Machine Learning Inalterable:**
    * El modelo de Machine Learning no se puede ajustar, reentrenar ni personalizar.
    * Esto significa que la precisión y el rendimiento son fijos y potencialmente bajos.
* **Recursos:**
    * No tiene ninguna optimización a nivel de recursos.
* **Falsos positivos:**
    * Por las limitaciones del modelo, tiene una alta posibilidad de generar falsos positivos.

  
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

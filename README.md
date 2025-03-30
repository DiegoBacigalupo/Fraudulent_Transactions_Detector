# FraudGuard AI 
# Detección de Transacciones Fraudulentas
---
---

## Versión 1: FraudGuard AI - Detección de Fraudes (Versión 1) - Prototipo

### Descripción General:

La versión 1 de FraudGuard AI es un prototipo básico para la detección de fraudes. Su funcionalidad es limitada y se utiliza principalmente para demostrar el concepto de detección de fraudes.

### Funcionalidades:

* **Entrada de Datos Estática:** El usuario puede seleccionar valores de un conjunto de datos predefinido.
* **Predicción Binaria:** Un modelo de Machine Learning pre-entrenado realiza una predicción binaria: "Fraude" o "No fraude".
* **Análisis Textual Limitado:** La API de OpenAI proporciona un análisis textual básico de la transacción.

---
---

## Versión 2: FraudGuard AI - Detección de Fraudes (Versión 2)

**Descripción General**

Esta aplicación combina el poder del Machine Learning (ML) y la Inteligencia Artificial (IA) para detectar transacciones fraudulentas. Permite a los usuarios cargar sus propios datasets, entrenar modelos de ML y obtener análisis detallados de transacciones de alto riesgo utilizando la API de OpenAI.

### Optimización de Recursos

El modelo de ML se utiliza para realizar una predicción inicial y filtrar las transacciones de alto riesgo. La API de OpenAI se utiliza solo para analizar las transacciones de alto riesgo, lo que reduce el consumo de tokens y los costos.

### Funcionalidades

* **Carga de Datasets:** Los usuarios pueden cargar archivos CSV que contienen datos de transacciones.
* **Entrenamiento del Modelo de Machine Learning:** Los usuarios pueden cargar un dataset con la columna objetivo (que indica si una transacción es fraudulenta) para entrenar un modelo de ML personalizado. Opción para reentrenar un modelo existente con nuevos datos o entrenar un modelo desde cero.
* **Predicción de Fraudes:** Los usuarios pueden cargar un dataset sin la columna objetivo para que el modelo de ML prediga qué transacciones son fraudulentas. La aplicación muestra una lista de las transacciones clasificadas como fraudulentas.
* **Análisis Detallado con IA:** Para las transacciones de alta probabilidad de fraude, la aplicación utiliza la API de OpenAI para generar un análisis detallado.
    * La respuesta de OpenAI incluye una evaluación de la probabilidad de fraude (Alta) y una explicación de los factores que contribuyen a la evaluación.
    * Botón para expandir la explicación generada por la IA.

### Comunicación entre el Modelo de ML y OpenAI para Análisis Detallado

Para proporcionar explicaciones más precisas sobre las transacciones de alto riesgo, la aplicación utiliza una combinación de un modelo de Machine Learning (Random Forest) y la API de OpenAI. El proceso es el siguiente:

1.  **Entrenamiento del Modelo de ML:**

    * El modelo de Random Forest se entrena con un dataset proporcionado por el usuario, que incluye ejemplos de transacciones fraudulentas y no fraudulentas.
    * Durante este proceso, el modelo aprende a identificar patrones en los datos que son indicativos de fraude.
    * Además, se calcula la importancia de cada característica (columna) en el dataset, lo que indica cuánto contribuye cada una a las predicciones del modelo.
2.  **Predicción de Fraudes:**

    * Una vez entrenado, el modelo de ML se utiliza para predecir qué transacciones en un nuevo dataset son de alto riesgo.
3.  **Análisis Detallado con OpenAI:**

    * Para cada transacción que el modelo de ML clasifica como de alto riesgo, se realiza una solicitud a la API de OpenAI para obtener un análisis más detallado.
    * Esta solicitud incluye:
        * Los detalles de la transacción específica.
        * Los nombres de las columnas (características) en el dataset.
        * La importancia de cada característica, calculada durante el entrenamiento del modelo de ML.
4.  **Análisis de OpenAI:**

    * OpenAI utiliza esta información para generar una explicación en lenguaje natural, centrándose en los factores más relevantes que contribuyeron a la clasificación de la transacción como de alto riesgo por parte del modelo de ML.
    * Opcionalmente, se puede incluir información sobre las reglas de decisión del modelo de ML para proporcionar un contexto adicional a la explicación de OpenAI.

Al combinar la capacidad del modelo de ML para identificar patrones con la capacidad de OpenAI para generar explicaciones en lenguaje natural, la aplicación proporciona un análisis más completo y comprensible de las transacciones de alto riesgo.

---
---

## Versión 3: FraudGuard AI - Detección de Fraudes (Versión 3)

## Descripción

FraudGuard AI es una aplicación de Streamlit diseñada para detectar transacciones fraudulentas utilizando modelos de Machine Learning e Inteligencia Artificial. La aplicación permite a los usuarios entrenar modelos personalizados a partir de sus propios datos y analizar nuevas transacciones para identificar posibles fraudes.

## Funcionalidades

* **Entrenamiento de Modelos Personalizados:** Los usuarios pueden subir sus propios datasets para entrenar modelos de Machine Learning. Se admiten archivos CSV.
* **Selección de Características y Objetivo:** Los usuarios pueden seleccionar qué columnas de sus datos se utilizarán como características y cuál será la columna objetivo.
* **Recomendación de Modelo:** La aplicación puede recomendar el modelo de Machine Learning más adecuado para los datos del usuario, utilizando la API de OpenAI.
* **Soporte para Múltiples Modelos:** Los usuarios pueden elegir entre varios modelos de Machine Learning populares, incluyendo Random Forest, Gradient Boosting, Regresión Logística, y más.
* **Análisis de Transacciones:** Los usuarios pueden subir un dataset de transacciones para ser analizado por el modelo entrenado. La aplicación marcará las transacciones que se consideren fraudulentas.
* **Explicaciones Detalladas:** Para cada transacción marcada como fraudulenta, la aplicación proporciona una explicación detallada de los factores que contribuyeron a la decisión, utilizando la API de OpenAI.
* **Métricas de Rendimiento:** Se muestran métricas de rendimiento del modelo, como accuracy, precision, recall, F1-score y AUC-ROC.
* **Matriz de Confusión:** Se visualiza la matriz de confusión para evaluar el rendimiento del modelo.

## Cómo Funciona

1.  **Entrenamiento del Modelo:**
    * El usuario sube un dataset en formato CSV.
    * El usuario selecciona la columna objetivo y las columnas de características.
    * Opcionalmente, la aplicación recomienda un modelo de Machine Learning.
    * El usuario selecciona un modelo y lo entrena.
2.  **Análisis de Transacciones:**
    * El usuario sube un dataset de transacciones en formato CSV.
    * La aplicación utiliza el modelo entrenado para predecir qué transacciones son fraudulentas.
    * Se muestran las transacciones fraudulentas detectadas.
    * El usuario puede solicitar una explicación detallada para cada transacción fraudulenta.

## Requisitos

* Python 3.6 o superior
* Streamlit
* OpenAI Python library
* Pandas
* Scikit-learn
* Matplotlib
* Seaborn

## Instalación

1.  Clona este repositorio:

    ```bash
    git clone [https://github.com/tu-usuario/nombre-del-repo.git](https://github.com/tu-usuario/nombre-del-repo.git)
    cd nombre-del-repo
    ```

2.  Crea un entorno virtual (recomendado):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # En Linux/macOS
    venv\Scripts\activate  # En Windows
    ```

3.  Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

4.  Obtén una API Key de OpenAI desde [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys).

## Uso

1.  Ejecuta la aplicación:

    ```bash
    streamlit run app.py
    ```

2.  Sigue las instrucciones en la aplicación web.



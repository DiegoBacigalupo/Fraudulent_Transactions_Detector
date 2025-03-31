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
El modelo de ML actúa como un sistema de detección, identificando transacciones sospechosas y notificando al Agente de IA. El Agente de IA sirve como intermediario, presentando esta información a los usuarios y permitiéndoles tomar decisiones informadas. El Agente de IA entonces ejecuta estas decisiones, interactuando con otros sistemas según sea necesario.

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


  ### Comunicación con el Agente de IA

**1. Comunicación del Modelo ML con el Agente de IA**

* **Detección de Transacciones Sospechosas:** El modelo de ML es el componente principal responsable de analizar las transacciones y determinar su nivel de riesgo. Cuando el modelo detecta una transacción que supera un umbral de riesgo predefinido, se activa una alerta.
* **Envío de Alertas al Agente de IA:** En lugar de tomar acción directa (como bloquear la transacción), el modelo de ML se comunica con el Agente de IA. Envía los detalles de la transacción sospechosa, incluyendo:
    * Identificador de la transacción
    * Usuario involucrado
    * Monto de la transacción
    * Características extraídas por el modelo
    * Puntaje de riesgo calculado
* **Formato de los Datos:** La comunicación entre el modelo de ML y el Agente de IA se realiza mediante un formato de datos estandarizado (por ejemplo, JSON). Esto asegura que ambos componentes puedan entender e interpretar la información correctamente.
* **API de Comunicación:** El modelo de ML utiliza una API (Interfaz de Programación de Aplicaciones) para enviar las alertas al Agente de IA. Esta API define los puntos finales (endpoints), los métodos de solicitud (por ejemplo, POST), y el formato de los datos.

**2. Comunicación del Usuario con el Agente de IA**

* **Interfaz de Usuario (UI):** Los usuarios interactúan con el Agente de IA a través de una interfaz de usuario, que puede ser una aplicación web, una aplicación móvil, o un sistema de mensajería.
* **Recepción de Alertas:** El Agente de IA presenta las alertas de transacciones sospechosas a los usuarios a través de la UI. La información mostrada incluye los detalles proporcionados por el modelo de ML.
* **Acciones del Usuario:** Los usuarios pueden realizar varias acciones en respuesta a una alerta, tales como:
    * **Aprobar la transacción:** Si el usuario determina que la transacción es legítima.
    * **Rechazar la transacción:** Si el usuario confirma que la transacción es fraudulenta.
    * **Solicitar más información:** Si el usuario necesita más detalles para tomar una decisión.
    * **Investigar al usuario:** Si el usuario considera que el usuario involucrado es sospechoso.
* **Envío de Acciones al Agente de IA:** Las acciones que el usuario realiza en la UI se envían al Agente de IA.
* **Lógica del Agente de IA:** El Agente de IA procesa las acciones del usuario y toma las medidas necesarias. Por ejemplo, si el usuario rechaza una transacción, el Agente de IA puede bloquear la transacción, notificar al sistema de procesamiento de pagos, y registrar la acción para fines de auditoría.
* **Confirmación al Usuario:** El Agente de IA envía una confirmación al usuario a través de la UI para indicar que su acción ha sido procesada.





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
    git clone https://github.com/DiegoBacigalupo/Fraudulent_Transactions_Detector.git
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
    streamlit run DFT_version_03.py
    ```

2.  Sigue las instrucciones en la aplicación web.



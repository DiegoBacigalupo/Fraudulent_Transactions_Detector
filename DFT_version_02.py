# Datasets de prueba (archivos con y sin columna objetivo): https://drive.google.com/drive/folders/1gPFAfwKYNmjR2GNBR_uQGogiW9twF4q3?usp=sharing

import streamlit as st
import openai
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import export_text  


openai.api_key = "KEY"  
if not openai.api_key:
    st.warning("Advertencia: La variable de entorno OPENAI_API_KEY no está configurada.")


if 'modelo_ml' not in st.session_state:
    st.session_state['modelo_ml'] = None
if 'feature_columns_entrenamiento' not in st.session_state:
    st.session_state['feature_columns_entrenamiento'] = []
if 'transacciones_fraudulentas' not in st.session_state:
    st.session_state['transacciones_fraudulentas'] = {}
if 'explicaciones' not in st.session_state:  
    st.session_state['explicaciones'] = {}
if 'mostrar_transacciones' not in st.session_state:
    st.session_state['mostrar_transacciones'] = False
if 'importancia_caracteristicas' not in st.session_state:
    st.session_state['importancia_caracteristicas'] = {}


st.title("FraudGuard AI - Detección de Fraudes")

st.subheader("Entrenar modelo desde cero")
uploaded_file_entrenamiento = st.file_uploader("Sube el dataset para entrenar el modelo (debe incluir la columna objetivo)", type=["csv"])

if uploaded_file_entrenamiento is not None:
    try:
        df_entrenamiento = pd.read_csv(uploaded_file_entrenamiento)
       
        target_column_entrenamiento = st.selectbox("Selecciona la columna objetivo", df_entrenamiento.columns.tolist())
       
        feature_columns_entrenamiento = st.multiselect("Selecciona las columnas de características",
                                                       df_entrenamiento.columns.tolist())

        if st.button("Entrenar modelo"):
            if target_column_entrenamiento and feature_columns_entrenamiento:
                X_entrenamiento = df_entrenamiento[feature_columns_entrenamiento]
                y_entrenamiento = df_entrenamiento[target_column_entrenamiento].astype(int)
                try:
                    modelo_ml = RandomForestClassifier(random_state=42) 
                    modelo_ml.fit(X_entrenamiento, y_entrenamiento)
                    st.session_state['modelo_ml'] = modelo_ml
                    st.session_state['feature_columns_entrenamiento'] = feature_columns_entrenamiento
                    
                    st.session_state['importancia_caracteristicas'] = dict(
                        zip(feature_columns_entrenamiento, modelo_ml.feature_importances_))
                    st.success("Modelo entrenado con éxito.")
                except Exception as e:
                    st.error(f"Error al entrenar el modelo: {e}")
            else:
                st.warning("Por favor, selecciona la columna objetivo y las columnas de características.")

        st.subheader("Analizar transferencias con modelo entrenado")
        uploaded_file_prediccion = st.file_uploader("Sube el dataset para predecir fraudes (sin la columna objetivo)",
                                                   type=["csv"])

        if uploaded_file_prediccion is not None:
            try:
                df_prediccion = pd.read_csv(uploaded_file_prediccion)
                if st.button("Analizar transferencias"):
                    if st.session_state['modelo_ml'] is not None:
                        try:
                            X_prediccion = df_prediccion[st.session_state['feature_columns_entrenamiento']]
                            predicciones = st.session_state['modelo_ml'].predict(X_prediccion)
                            df_prediccion["prediccion_fraude"] = predicciones
                            st.session_state['transacciones_fraudulentas'] = df_prediccion[
                                df_prediccion["prediccion_fraude"] == 1].to_dict(orient='index')
                            st.session_state['mostrar_transacciones'] = True  
                        except Exception as e:
                            st.error(f"Error al predecir fraudes: {e}")
                    else:
                        st.warning("Por favor, reentrena el modelo primero.")
            except Exception as e:
                st.error(f"Error al cargar el dataset de predicción: {e}")

    except Exception as e:
        st.error(f"Error al cargar el dataset de entrenamiento: {e}")



if st.session_state['mostrar_transacciones']:
    if not st.session_state['transacciones_fraudulentas']:
        st.write("No se detectaron transacciones fraudulentas.")
    else:
        st.write("Transacciones fraudulentas detectadas:")
        for index, row in st.session_state['transacciones_fraudulentas'].items():
            
            if row['prediccion_fraude'] == 1:
                st.write(f"Transacción {index}: Probabilidad de Fraude: ", end="")
                probabilidad_fraude = "Alta"  
                st.write(probabilidad_fraude)

                
                if st.button("Ver Explicación", key=f"explicacion_{index}"):
                    if index not in st.session_state['explicaciones']:
                        
                        importancia_transaccion = {k: st.session_state['importancia_caracteristicas'][k] for k in
                                                    st.session_state['feature_columns_entrenamiento']}
                        
                        explicacion_arbol = ""
                        if hasattr(st.session_state['modelo_ml'], 'estimators_'):
                            
                            primer_arbol = st.session_state['modelo_ml'].estimators_[0]
                            explicacion_arbol = export_text(primer_arbol,
                                                           feature_names=st.session_state['feature_columns_entrenamiento'])
                        
                        prompt_openai = f"Analiza en detalle la siguiente transacción. Indica la probabilidad de fraude (baja, media o alta) y explica los factores que contribuyen a tu conclusión.  Especificamente, considera y explica la relevancia de los siguientes campos y sus valores: {', '.join(st.session_state['feature_columns_entrenamiento'])}.  Aquí está la importancia de cada característica: {importancia_transaccion}. Aquí está la explicación de un árbol de decisión para esta transacción: {explicacion_arbol}. Proporciona una justificación detallada.: {row}"
                        respuesta = openai.chat.completions.create(
                            model="gpt-3.5-turbo",
                            messages=[
                                {
                                    "role": "system",
                                    "content": "Eres un experto en detección de fraudes con un profundo conocimiento de los indicadores de riesgo, el análisis de datos transaccionales, la importancia de las características en modelos de machine learning y la lógica de los árboles de decisión.",
                                },
                                {"role": "user", "content": prompt_openai},
                            ],
                            max_tokens=300,  
                        )
                        st.session_state['explicaciones'][index] = respuesta.choices[0].message.content.strip()
                    st.write(st.session_state['explicaciones'][index])

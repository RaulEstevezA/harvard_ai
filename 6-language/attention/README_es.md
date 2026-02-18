# Attention

Este proyecto forma parte del curso **CS50's Introduction to Artificial Intelligence with Python**, dentro de la unidad de **Language** (Procesamiento del Lenguaje Natural).

El objetivo de este ejercicio es inspeccionar y visualizar el **mecanismo de self-attention** utilizado por los modelos de lenguaje basados en transformadores.

## Descripción del Proyecto

Los modelos transformadores como BERT utilizan self-attention para evaluar las relaciones entre tokens dentro de una frase. Cada token puede asignar dinámicamente importancia a otros tokens, lo que permite al modelo capturar dependencias contextuales sin depender únicamente del procesamiento secuencial.

En este proyecto, los pesos de atención se extraen de un modelo BERT pretrained de tipo masked language model y se representan como diagramas en escala de grises. Estas visualizaciones permiten entender cómo el modelo distribuye la atención entre tokens en distintas capas y cabezas.

## Cómo Funciona

El programa opera en varias fases:

1. **Procesamiento de Entrada**
   - El usuario proporciona una frase que contiene un token `[MASK]`.
   - La frase se tokeniza usando un tokenizer pretrained.

2. **Inferencia del Modelo**
   - Se carga un modelo BERT pretrained de tipo masked language model.
   - El modelo genera matrices de atención para cada capa y cabeza.

3. **Visualización de la Atención**
   - Las puntuaciones de atención se convierten en valores en escala de grises.
   - Se genera un diagrama por cada capa y cabeza de atención.

## Cómo Ejecutarlo

Se **recomienda utilizar un entorno virtual de Python** para evitar conflictos de dependencias.

Crear y activar un entorno virtual:

```bash
python3 -m venv venv
source venv/bin/activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Si trabajas en macOS y aparecen problemas de compatibilidad con TensorFlow/Keras:

```bash
export TF_USE_LEGACY_KERAS=1
```

### Ejecución

Ejecuta el programa e introduce una frase cuando se solicite:

```bash
python mask.py
```

Ejemplo de entrada:

```text
Text: The capital of France is [MASK].
```

## Salida

El programa genera múltiples archivos PNG que representan los patrones de atención:

- `Attention_LayerX_HeadY.png`

Cada diagrama corresponde a una capa del transformador y a una cabeza de atención. Las celdas más claras representan mayores puntuaciones de atención, mientras que las más oscuras indican menor atención.

![Result](../../images/attention.png)

## Conceptos Clave Implementados

- Mecanismo de self-attention
- Arquitectura de transformadores
- Capas y cabezas de atención
- Relaciones entre tokens en modelos de lenguaje
- Interpretación visual de matrices de atención

## Archivos

- **`mask.py`** → Programa principal. Carga el modelo, extrae las atenciones y genera los diagramas.
- **`requirements.txt`** → Dependencias de Python.

## Acceso Directo

- [Ver el código fuente](./mask.py)  
- [Volver al README principal](../../README_es.md)

## Autor

Este proyecto fue completado por [**Raul Estevez**](https://raulesteveza.github.io) como parte del coursework de CS50 AI.

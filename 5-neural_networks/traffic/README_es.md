# Traffic

Este proyecto forma parte del curso **CS50's Introduction to Artificial Intelligence with Python**, dentro de la unidad de **Redes Neuronales (Neural Networks)**.  
El objetivo de este ejercicio es construir y entrenar una **red neuronal convolucional (CNN)** capaz de clasificar señales de tráfico a partir de imágenes.

## Descripción del proyecto

El reconocimiento de señales de tráfico es un problema clásico de **visión por computador** en inteligencia artificial. En este proyecto, se entrena una red neuronal para identificar señales de tráfico utilizando el conjunto de datos **German Traffic Sign Recognition Benchmark (GTSRB)**.

Cada imagen representa una señal de tráfico y pertenece a una de **43 categorías diferentes**. El objetivo es clasificar correctamente cada imagen basándose en sus características visuales, como formas, colores y patrones.

El proyecto se centra en el diseño, entrenamiento y evaluación de una red neuronal convolucional utilizando **TensorFlow y Keras**, así como en la experimentación con distintas configuraciones del modelo para mejorar su rendimiento.

## Funcionamiento

El programa consta de tres fases principales:

1. **Carga y preprocesamiento de datos**
   - Las imágenes se cargan desde directorios organizados por categoría.
   - Cada imagen se redimensiona a **30 × 30 píxeles**.
   - Las etiquetas se asignan en función del nombre del directorio.
   - El conjunto de datos se divide en datos de entrenamiento y de prueba.

2. **Arquitectura del modelo**
   - Red neuronal convolucional con varias capas convolucionales y de *pooling*.
   - Una capa totalmente conectada para combinar las características aprendidas.
   - Una capa *Dropout* para reducir el sobreajuste.
   - Una capa de salida *softmax* con una neurona por cada categoría de señal.

3. **Entrenamiento y evaluación**
   - El modelo se entrena durante un número fijo de épocas.
   - Se monitorizan la precisión (*accuracy*) y la pérdida (*loss*) durante el entrenamiento.
   - El rendimiento final se evalúa utilizando un conjunto de prueba independiente.

## Proceso de experimentación

Se realizaron varios experimentos para mejorar el modelo:

- Se aumentó el número de épocas de entrenamiento de 10 a 20, lo que mejoró notablemente la precisión en el conjunto de prueba.
- Se añadió una capa *Dropout* para reducir el sobreajuste y mejorar la capacidad de generalización.
- Se ajustó el tamaño de la capa totalmente conectada para evaluar su impacto en el rendimiento.
- Se probó una capa convolucional adicional para aumentar la profundidad del modelo.

Tras comparar los resultados de varias ejecuciones, el modelo final alcanzó una **precisión estable cercana al 98%**, logrando un buen equilibrio entre rendimiento, complejidad y estabilidad.

## Cómo ejecutar el proyecto

Se **recomienda utilizar un entorno virtual de Python** para evitar conflictos de dependencias.

Una vez creado y activado el entorno virtual, instala los paquetes necesarios usando el archivo `requirements.txt` incluido en el proyecto:

```bash
pip install -r requirements.txt
```

### Preparación del conjunto de datos

1. Descarga el conjunto de datos GTSRB desde el siguiente enlace:

```
https://cdn.cs50.net/ai/2023/x/projects/5/gtsrb.zip
```

2. Descomprime el archivo y coloca la carpeta **`gtsrb`** resultante dentro del directorio del proyecto.

Si el enlace anterior no funciona, el conjunto de datos también puede encontrarse en la sección **Getting Started** de la página oficial del proyecto:

```
https://cs50.harvard.edu/ai/projects/5/traffic/
```

### Ejecución

Una vez preparado el conjunto de datos, ejecuta el programa con:

```bash
python traffic.py gtsrb
```

## Ejemplo de salida

A continuación se muestra un ejemplo del resultado del entrenamiento (los valores pueden variar ligeramente):

```text
Epoch 20/20
accuracy: 0.9645
loss: 0.1292

Test accuracy: 0.9813
Test loss: 0.0850
```

![Resultado del entrenamiento](../../images/traffic.png)

## Conceptos clave implementados

- Redes neuronales convolucionales (CNN)
- Preprocesamiento y redimensionado de imágenes
- Aprendizaje supervisado con datos etiquetados
- Regularización del modelo mediante *Dropout*
- Evaluación del rendimiento mediante precisión y pérdida

## Archivos

- **`traffic.py`** → Programa principal. Carga los datos, define la red neuronal, entrena el modelo y evalúa su rendimiento.

## Acceso directo

- [**Ver el código fuente completo**](./traffic.py)  
- [Volver al README principal](../../README_en.md)

## Autor

Este proyecto fue realizado por **Raul Estevez** como parte de los ejercicios del curso CS50 AI.

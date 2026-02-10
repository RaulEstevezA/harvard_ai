# Heredity

Este proyecto forma parte del curso **CS50's Introduction to Artificial Intelligence with Python**, ofrecido por la Universidad de Harvard.  
El ejercicio se encuentra dentro de la unidad de **Incertidumbre (Uncertainty)** y su objetivo es calcular las probabilidades de que las personas posean un determinado gen y manifiesten un rasgo, basándose en la herencia genética y en las probabilidades de mutación.

## Descripción del proyecto

En este proyecto se modela cómo los genes se transmiten de padres a hijos, teniendo en cuenta tanto:

- **Probabilidades de herencia**:  
  - Los padres pueden transmitir 0, 1 o 2 copias de un gen a sus hijos.  
  - La probabilidad depende del número de copias del gen que tenga cada progenitor.

- **Probabilidades de mutación**:  
  - Un gen puede mutar con una probabilidad dada (1%), lo que implica que:
    - Un padre con 2 copias del gen podría no transmitirlo.
    - Un padre con 0 copias del gen podría transmitirlo de forma inesperada.

Estas probabilidades se combinan con las probabilidades del rasgo (la probabilidad de manifestar un rasgo dado un número concreto de copias del gen) para calcular la **probabilidad conjunta** de cualquier configuración familiar.  
Finalmente, los resultados se **normalizan** para obtener distribuciones de probabilidad válidas para cada individuo.

## Cómo ejecutar el programa

Para ejecutar el proyecto, asegúrate de tener **Python 3** instalado.  
Ejecuta el programa utilizando uno de los conjuntos de datos CSV proporcionados:

```bash
python heredity.py family0.csv
python heredity.py family1.csv
python heredity.py family2.csv
```

El archivo CSV especifica las personas, sus padres (si se conocen) y la evidencia sobre si manifiestan o no el rasgo.

## Ejemplo de salida

Por ejemplo, al ejecutar el programa con `family0.csv`, se puede obtener una salida similar a la siguiente:

```
Harry
  Gene:
    2: 0.0000
    1: 0.0000
    0: 1.0000
  Trait:
    True: 0.0000
    False: 1.0000

James
  Gene:
    2: 0.0100
    1: 0.0300
    0: 0.9600
  Trait:
    True: 0.0100
    False: 0.9900

Lily
  Gene:
    2: 0.1976
    1: 0.5030
    0: 0.2994
  Trait:
    True: 0.6976
    False: 0.3024
```

*(Los valores pueden variar ligeramente debido a la precisión de los cálculos en coma flotante.)*

![Salida del programa](../../images/heredity.png)

## Archivos incluidos
- **`heredity.py`** → Programa principal que implementa el algoritmo.
- **`family0.csv`**, **`family1.csv`**, **`family2.csv`** → Conjuntos de datos de ejemplo para probar el programa.
- **`README_es.md`** → Este archivo de explicación.

## Conceptos trabajados
- Representación de probabilidades utilizando diccionarios en Python.
- Cálculo de **distribuciones de probabilidad conjuntas**.
- Actualización de probabilidades entre múltiples hipótesis.
- **Normalización** de distribuciones de probabilidad.
- Iteración sobre todas las combinaciones posibles usando `powerset`.

## Acceso directo

- [**Ver el código fuente completo**](./heredity.py)
- [Volver al README principal](../../README_es.md)

## Autor

Este proyecto fue realizado por [**Raul Estevez**](https://raulesteveza.github.io) como parte de los ejercicios del curso CS50 AI.

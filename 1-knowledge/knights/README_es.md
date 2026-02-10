# Knights

Este proyecto forma parte del curso **CS50's Introduction to Artificial Intelligence with Python**, ofrecido por la Universidad de Harvard. El ejercicio se encuentra dentro de la unidad de **Lógica Proposicional**, y su objetivo es aplicar razonamiento lógico para determinar la identidad de distintos personajes (Caballeros o Mentirosos).

## Descripción del proyecto

En este ejercicio se trabaja con agentes lógicos en un entorno ficticio. Cada personaje es o bien un **Caballero**, que siempre dice la verdad, o un **Mentiroso**, que siempre miente.

Se presentan cuatro escenarios distintos, cada uno con declaraciones realizadas por algunos de los personajes. Utilizando lógica proposicional e inferencia, se modelan estas situaciones con el fin de determinar el rol de cada personaje en cada acertijo.

## Cómo ejecutar el programa

Para ejecutar el proyecto, asegúrate de tener Python 3 instalado. A continuación, ejecuta el siguiente comando en la terminal:

```bash
python puzzle.py
```

El programa mostrará por pantalla las identidades deducidas de los personajes en cada uno de los cuatro acertijos, basándose en el conocimiento lógico definido.

## Ejemplo de salida

```text
Puzzle 0
    AKnave
Puzzle 1
    AKnave
    BKnight
Puzzle 2
    AKnave
    BKnight
Puzzle 3
    AKnight
    BKnave
    CKnight
```

![Salida del programa](../../images/knights.png)

## Archivos

- `logic.py`: Archivo proporcionado por CS50 que contiene las clases y métodos para símbolos lógicos, conectores y comprobación de modelos.
- `puzzle.py`: Archivo principal donde se construye la base de conocimiento de cada acertijo y se evalúan los modelos.
- `README_es.md`: Este archivo.

## Acceso directo

- [**Ver el código fuente completo**](./puzzle.py)
- [Volver al README principal](../../README_es.md)

## Autor

Este proyecto fue realizado por [**Raul Estevez**](https://raulesteveza.github.io) como parte de los ejercicios del curso CS50 AI.

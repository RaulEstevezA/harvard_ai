# Crossword

Este proyecto forma parte del curso **CS50's Introduction to Artificial Intelligence with Python**, ofrecido por la Universidad de Harvard.  
El ejercicio se encuentra dentro de la unidad de **Optimización (Optimization)** y su objetivo es generar crucigramas modelándolos como un **Problema de Satisfacción de Restricciones (CSP)**.

## Descripción del proyecto

El objetivo de este proyecto es rellenar una cuadrícula de crucigrama utilizando una lista de palabras dada, asegurando que se cumplan todas las restricciones impuestas por la estructura. El problema se modela como un CSP con los siguientes componentes:

1. **Variables**
   - Cada espacio horizontal o vertical del crucigrama es una variable.
   - Cada variable tiene asociada una restricción de longitud.

2. **Dominios**
   - Los valores posibles para cada variable son las palabras de la lista que coinciden con su longitud.
   - Los dominios se reducen aplicando consistencia de nodo y de arco.

3. **Restricciones**
   - Restricción unaria: la longitud de la palabra debe coincidir con la longitud del espacio.
   - Restricciones binarias: las variables que se cruzan deben compartir el mismo carácter en la posición de cruce.
   - Ninguna palabra puede reutilizarse más de una vez.

Para resolver el problema de forma eficiente, el programa utiliza:
- **AC-3** para imponer consistencia de arco y podar dominios.  
- **Heurísticas**:
  - *Minimum Remaining Values (MRV)* para seleccionar la variable.  
  - *Degree heuristic* para desempatar según el número de restricciones.  
  - *Least Constraining Value (LCV)* para ordenar las palabras candidatas.  
- **Búsqueda con backtracking** para explorar asignaciones hasta encontrar una solución válida o agotar todas las opciones.

El programa genera una cuadrícula de crucigrama completa si existe una solución, o informa cuando no es posible encontrarla.

## Cómo ejecutar el programa

Asegúrate de tener **Python 3** instalado.  
Ejecuta el proyecto con el siguiente comando:

```bash
python generate.py data/structure1.txt data/words1.txt output.png
```

- `structure1.txt` → Define la estructura del crucigrama (con `█` para las celdas bloqueadas).  
- `words1.txt` → Contiene la lista de palabras que se utilizarán.  
- `output.png` → El crucigrama resultante se guardará como una imagen.  

También puedes mostrar el crucigrama directamente por consola modificando la función `main` en `generate.py`.

## Ejemplo de salida

```
██████████████
███████M████R█
█INTELLIGENCE█
█N█████N████S█
█F██LOGIC███O█
█E█████M████L█
█R███SEARCH█V█
███████X████E█
██████████████
```

![Vista del editor](../../images/crossword1.png)

![Resultado del crucigrama](../../images/crossword2.png)

## Archivos

- **`crossword.py`** → Contiene la definición de la clase `Crossword` y métodos auxiliares.  
- **`generate.py`** → Implementa el solucionador CSP, las heurísticas y la búsqueda con backtracking.  
- **`data/structure*.txt`** → Archivos de estructura del crucigrama.  
- **`data/words*.txt`** → Listas de palabras para las pruebas.  

## Acceso directo

- [**Ver el código fuente completo**](./generate.py)  
- [Volver al README principal](../../README_es.md)  

## Autor

Este proyecto fue realizado por [**Raul Estevez**](https://raulesteveza.github.io) como parte de los ejercicios del curso CS50 AI.

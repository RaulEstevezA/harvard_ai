# Degrees

Este proyecto es el primer ejercicio de la primera lección, **"0 - Search"**, del curso *CS50’s Introduction to Artificial Intelligence with Python*.

En este ejercicio se implementa un algoritmo de búsqueda en grafos para determinar la conexión más corta entre dos actores a partir de las películas en las que han participado. Inspirado en el juego *Six Degrees of Kevin Bacon*, el programa explora cuán estrechamente relacionados están dos actores dentro de la industria cinematográfica.

## Cómo funciona

El programa modela a los actores y las películas como un grafo:

- Cada **actor** es un nodo.
- Cada **película** es una arista que conecta a los actores que han aparecido juntos.
- Utilizando **búsqueda en anchura (Breadth-First Search, BFS)**, se encuentra el camino más corto entre un actor y otro.

Ejemplo de uso:

```
python3 degrees.py small
```

Se te pedirá que introduzcas los nombres de dos actores. El programa mostrará entonces los grados de separación y la lista de películas y coprotagonistas que los conectan.

## Ejemplo de salida

![Salida del programa](../../images/degrees.png)

## Archivos

- `degrees.py`: Programa principal.
- `util.py`: Clases auxiliares (`Node`, `QueueFrontier`) utilizadas para la búsqueda.
- `small/` y `large/`: Conjuntos de datos con información de actores y películas en formato CSV.

## Acceso directo

- [**Ver el código fuente completo**](./degrees.py)
- [Volver al README principal](../../README_es.md)

## Estado

Completado y probado con los conjuntos de datos pequeño y grande.

## Autor

Este proyecto fue realizado por [**Raul Estevez**](https://raulesteveza.github.io) como parte de los ejercicios del curso CS50 AI.

# Introducción a la Inteligencia Artificial con Python (CS50 AI)

Este repositorio contiene mi progreso personal y mis soluciones del curso **[CS50’s Introduction to Artificial Intelligence with Python](https://www.edx.org/learn/artificial-intelligence/harvard-university-cs50-s-introduction-to-artificial-intelligence-with-python)**, ofrecido por la Universidad de Harvard.

El curso explora los conceptos fundamentales de la inteligencia artificial, con un enfoque práctico mediante la implementación de algoritmos en Python. A lo largo del curso se trabajan temas como algoritmos de búsqueda, representación del conocimiento, lógica, planificación, aprendizaje automático y procesamiento del lenguaje natural.

## Objetivos del curso

- Comprender los conceptos clave de la inteligencia artificial y su aplicación en escenarios reales.
- Implementar algoritmos fundamentales de IA utilizando Python.
- Obtener experiencia práctica en búsqueda, optimización, inferencia lógica y aprendizaje automático.

## Contenidos del curso y ejercicios

Cada carpeta del repositorio corresponde a una unidad principal del curso. Dentro de cada una se incluyen uno o más ejercicios prácticos.

**[0 - Búsqueda](./0-search)**

Esta unidad introduce los algoritmos fundamentales de búsqueda y las estrategias de resolución de problemas utilizadas en inteligencia artificial:

- **Definición de problemas de búsqueda**: estado inicial, estado objetivo, función sucesora y métricas de coste.
- **Búsqueda no informada (ciega)**:
  - **Búsqueda en profundidad (DFS)**: explora completamente una rama usando una pila (LIFO); no garantiza optimalidad ni completitud en grafos infinitos.
  - **Búsqueda en anchura (BFS)**: explora nivel por nivel usando una cola (FIFO); garantiza encontrar el camino más corto y es completa en grafos finitos.
- **Búsqueda informada (heurística)**:
  - **Greedy Best‑First Search**: utiliza una función heurística `h(n)` para estimar la cercanía al objetivo.
  - **A\***: combina el coste del camino y la heurística (`f(n) = g(n) + h(n)`), garantizando optimalidad con heurísticas admisibles y consistentes.
- **Otras estrategias introducidas**:
  - **Búsqueda en profundidad iterativa (IDDFS)**.
  - Visión general de **búsqueda bidireccional**, **búsqueda de coste uniforme** y **poda alfa‑beta**.

**Ejercicios:**
- [Degrees](./0-search/degrees/README_es.md)  
  Implementa BFS para encontrar el grado mínimo de separación entre dos actores a partir de películas compartidas.

- [Tic Tac Toe](./0-search/tictactoe/README_es.md)  
  Implementa una IA invencible usando el algoritmo Minimax para jugar al tres en raya.

**[1 - Knowledge](./1-knowledge)**  

Esta unidad introduce la **lógica proposicional** como una herramienta para representar conocimiento y realizar **inferencias** en inteligencia artificial. Se centra en cómo un agente puede deducir hechos a partir de reglas y hechos conocidos usando razonamiento lógico, en lugar de recurrir a una búsqueda por fuerza bruta.

- **Lógica proposicional**:
  - Símbolos lógicos y conectores: `∧` (y), `∨` (o), `¬` (no), `→` (implicación) y `↔` (bicondicional).
  - Tablas de verdad y modelos: determinar cuándo una proposición lógica se cumple en un “mundo” concreto.
  - Reglas de inferencia: incluyendo **Modus Ponens**, **Modus Tollens** y transformaciones de equivalencia como las **Leyes de De Morgan** y las **propiedades distributivas**.
- **Bases de conocimiento (KB)**:
  - Un conjunto de oraciones lógicas que representan hechos y reglas sobre el mundo.
  - Uso de la función `model_check` para determinar si una conclusión se deriva lógicamente de la KB.
- **IA simbólica**:
  - Da importancia a la lógica formal y al razonamiento estructurado, en lugar de usar heurísticas numéricas.
  - Es la base de muchos sistemas expertos y motores de razonamiento.

Estos conceptos son fundamentales para construir agentes que razonan con certeza y pueden deducir verdades sobre el entorno a partir de información limitada.

**Ejercicios:**
- [Knights](./1-knowledge/knights/README_es.md)  
  Utiliza lógica proposicional para determinar la identidad (Caballero o Mentiroso) de los personajes en acertijos lógicos basados en sus declaraciones. Implementa una base de conocimiento para cada puzzle y aplica reglas de inferencia para llegar a conclusiones.

- [Minesweeper](./1-knowledge/minesweeper/README_es.md)  
  Construye un agente de IA que juega al Buscaminas usando deducción lógica. La IA mantiene una base de conocimiento con celdas seguras y peligrosas, y deduce nueva información a medida que descubre el tablero.

**[2 - Uncertainty](./2-uncertainty)**  

Esta unidad introduce el **razonamiento probabilístico** como una herramienta fundamental en inteligencia artificial. A diferencia de la lógica proposicional, que trabaja con verdades absolutas, los modelos probabilísticos permiten representar la **incertidumbre** y ayudan a los agentes a tomar decisiones informadas en situaciones donde los resultados no son deterministas.

- **Fundamentos de probabilidad**:
  - Variables aleatorias y distribuciones de probabilidad.  
  - Probabilidad condicional: `P(A|B)` y su papel en el razonamiento bajo incertidumbre.  
  - Regla de Bayes como método para actualizar creencias a partir de nueva evidencia.  

- **Inferencia con probabilidades**:
  - El concepto de *distribuciones de probabilidad conjuntas* y la marginalización.  
  - Representación de la incertidumbre sobre causas y efectos en entornos complejos.  

- **Aplicaciones en IA**:
  - Modelos probabilísticos para razonar con información incompleta.  
  - Fundamentos de algoritmos utilizados en procesamiento del lenguaje natural, visión por computador y toma de decisiones bajo riesgo.  

Estos conceptos son fundamentales para construir agentes capaces de desenvolverse de forma eficaz en entornos reales, donde la incertidumbre es inevitable.

**Ejercicios:**
- [PageRank](./2-uncertainty/pagerank/README_es.md)  
  Implementa el algoritmo PageRank de Google usando dos enfoques: muestreo (simulando un “navegante aleatorio”) e iteración (redistribuyendo probabilidades repetidamente hasta alcanzar la convergencia). El proyecto muestra cómo las distribuciones de probabilidad pueden representar la importancia de las páginas web.  

- [Heredity](./2-uncertainty/heredity/README_es.md)  
  Modela la herencia genética y la expresión de rasgos en familias. El programa calcula probabilidades conjuntas de que las personas tengan 0, 1 o 2 copias de un gen, y de que presenten un rasgo determinado, teniendo en cuenta la herencia de los padres, las tasas de mutación y las probabilidades condicionales. Los resultados se normalizan para obtener distribuciones de probabilidad válidas.

**[3 - Optimization](./3-optimization)**  

Esta unidad introduce la **optimización** como una forma de resolver problemas complejos encontrando la mejor asignación posible de valores bajo un conjunto de restricciones. A diferencia de los algoritmos de búsqueda que exploran caminos en un grafo, los métodos de optimización suelen trabajar directamente con variables y dominios, aplicando heurísticas y comprobaciones de consistencia para reducir el espacio de búsqueda.

- **Búsqueda local**:  
  - Hill climbing y sus variantes (ascenso más pronunciado, estocástico, reinicios aleatorios).  
  - Equilibrio entre exploración y explotación al recorrer espacios de estados grandes.  

- **Problemas de satisfacción de restricciones (CSP)**:  
  - Problemas definidos por variables, sus dominios y las restricciones entre ellas.  
  - Restricciones unarias y binarias, y técnicas para imponer consistencia de nodos y de arcos.  
  - El algoritmo **AC-3** para eliminar valores inconsistentes de los dominios.  

- **Heurísticas para mejorar la eficiencia**:  
  - Heurística de **Minimum Remaining Values (MRV)** para seleccionar variables.  
  - Heurística de **grado** como criterio de desempate.  
  - Heurística de **Least Constraining Value (LCV)** para ordenar los valores del dominio.  

Estos métodos proporcionan un marco eficaz para resolver problemas en los que una búsqueda por fuerza bruta sería inviable, convirtiendo la optimización en una herramienta central de la inteligencia artificial.

**Ejercicios:**
- [Crossword](./3-optimization/crossword/README_es.md)  
  Genera crucigramas modelándolos como un problema de satisfacción de restricciones. Cada espacio del tablero se representa como una variable con palabras como dominio. El solucionador impone consistencia de nodos y de arcos, aplica heurísticas (MRV, grado y LCV) y utiliza búsqueda con backtracking para asignar palabras de forma que se satisfagan todos los solapamientos. El programa muestra un crucigrama completo o indica cuando no existe solución.

**[4 - Learning](./4-learning)**  

Esta unidad introduce el **aprendizaje automático (machine learning)**, donde los sistemas mejoran su rendimiento en una tarea a partir de la experiencia, en lugar de ser programados explícitamente. El aprendizaje permite a la IA **generalizar a partir de ejemplos** y realizar predicciones sobre datos no vistos previamente.

- **Aprendizaje supervisado**:  
  - Entrenamiento de un modelo con datos etiquetados para predecir resultados en nuevas entradas.  
  - Conceptos de entrenamiento, prueba, sobreajuste (*overfitting*) y generalización.  
  - Métricas de evaluación como la sensibilidad (tasa de verdaderos positivos) y la especificidad (tasa de verdaderos negativos).  

- **Clasificadores por vecinos más cercanos**:  
  - Predicción de etiquetas basada en la similitud con ejemplos de entrenamiento.  
  - Algoritmo *k-nearest neighbors (k-NN)* y el efecto de diferentes valores de *k*.  

- **Aprendizaje por refuerzo**:  
  - Los agentes aprenden estrategias interactuando con un entorno.  
  - Conceptos de estados, acciones, recompensas y políticas.  
  - **Q-learning** como método para aproximar funciones de valor acción-estado óptimas.  

Estos enfoques constituyen la base de muchos sistemas modernos de inteligencia artificial, desde motores de recomendación hasta agentes que juegan a videojuegos, al permitirles adaptarse y mejorar a partir de datos o interacción.

**Ejercicios:**
- [Shopping](./4-learning/shopping/README_es.md)  
  Implementa un modelo de aprendizaje supervisado utilizando **k-nearest neighbors (k=1)** para predecir si un usuario generará ingresos en un sitio web de comercio electrónico a partir de datos de sesión. El programa carga y procesa características categóricas y numéricas, entrena el clasificador y lo evalúa en términos de sensibilidad y especificidad.  

- [Nim](./4-learning/nim/README_es.md)  
  Implementa un agente de aprendizaje por refuerzo que aprende a jugar al juego de Nim mediante autoaprendizaje. El agente utiliza **Q-learning** para actualizar su estrategia, mejorando progresivamente su rendimiento y aproximándose al juego óptimo sin estar programado explícitamente con la solución del juego.

**[5 - Neural Networks](./5-neural_networks)**  

Esta unidad introduce las **redes neuronales artificiales**, una potente clase de modelos de aprendizaje automático inspirados en la estructura del cerebro humano. Las redes neuronales aprenden ajustando pesos en respuesta a los errores, lo que les permite reconocer patrones complejos en datos como imágenes, texto o estados de un juego.

- **Estructura de una red neuronal**:  
  - Capa de entrada, capas ocultas y capa de salida.  
  - Las neuronas combinan entradas ponderadas con un sesgo y aplican una función de activación.  

- **Funciones de activación**:  
  - Funciones no lineales (como sigmoid, ReLU o tanh) que permiten a las redes modelar relaciones complejas.  

- **Propagación hacia adelante (forward propagation)**:  
  - Cálculo de predicciones pasando las entradas por la red capa a capa.  

- **Funciones de pérdida (loss functions)**:  
  - Medición de la distancia entre las predicciones y los valores correctos, proporcionando una señal para el aprendizaje.  

- **Retropropagación y descenso por gradiente**:  
  - Uso de derivadas para determinar cómo cada peso contribuye al error.  
  - Actualización de los pesos en la dirección que minimiza la pérdida, controlada por una tasa de aprendizaje.  

- **Aprendizaje profundo (deep learning)**:  
  - Redes neuronales con múltiples capas ocultas capaces de aprender representaciones de alto nivel a partir de datos en bruto.  

En conjunto, estos conceptos muestran cómo las redes neuronales pueden aprender automáticamente características a partir de los datos y mejorar mediante entrenamiento repetido, formando la base de muchas aplicaciones modernas de la inteligencia artificial, como la visión por computador y el reconocimiento de patrones.

**Ejercicios:**
- [Traffic](./5-neural_networks/traffic/README_es.md)  
  Implementa una red neuronal convolucional para clasificar imágenes de señales de tráfico. El modelo se entrena con datos de imágenes etiquetadas y se evalúa sobre ejemplos no vistos, demostrando cómo las redes neuronales pueden aprender características visuales directamente a partir de los píxeles.

**[6 - Language](./6-language)**  

Esta unidad introduce el **procesamiento del lenguaje natural (NLP)**, el área de la inteligencia artificial centrada en permitir que las máquinas comprendan, interpreten y generen lenguaje humano. El lenguaje presenta desafíos únicos para la IA, ya que el texto es inherentemente secuencial, ambiguo y altamente dependiente del contexto.

En esta unidad se exploran distintos enfoques para modelar la estructura y el significado del lenguaje, desde sistemas basados en reglas hasta técnicas modernas basadas en redes neuronales.

- **Estructura del lenguaje y gramática**  
  - Representación de oraciones mediante reglas gramaticales y árboles de análisis sintáctico (*parse trees*).  
  - Comprensión de cómo las palabras se combinan para formar estructuras sintácticas válidas.

- **Contexto y ambigüedad**  
  - Las palabras y las oraciones pueden tener múltiples significados según el contexto.  
  - Los modelos deben considerar las palabras circundantes para interpretar correctamente el significado.

- **Modelado de secuencias**  
  - Tratamiento del lenguaje como una secuencia de tokens procesados en orden.  
  - Captura de dependencias entre partes tempranas y posteriores de una oración.

- **Enfoques neuronales para el lenguaje**  
  - Uso de redes neuronales para aprender patrones a partir de datos textuales.  
  - Superación de las reglas fijas mediante representaciones del lenguaje basadas en datos.

- **Mecanismos de atención**  
  - Permiten que los modelos se centren en las partes más relevantes de una oración.  
  - Mejoran el rendimiento en tareas que requieren comprender dependencias a largo alcance.

En conjunto, estas ideas muestran cómo los sistemas de IA pueden procesar y razonar sobre el lenguaje, formando la base de aplicaciones como la traducción automática, el resumen de textos y los sistemas de preguntas y respuestas.

### Ejercicios

- [Parser](./6-language/parser/README_es.md)  
  Implementa un analizador sintáctico basado en **gramáticas libres de contexto**, que analiza la estructura de las oraciones y genera árboles de análisis, demostrando un enfoque basado en reglas para comprender la sintaxis del lenguaje.

- [Attention](./6-language/attention/README_es.md)  
  Utiliza redes neuronales con **mecanismos de atención** para procesar datos lingüísticos, mostrando cómo los modelos pueden centrarse dinámicamente en las partes más relevantes de una secuencia de entrada para mejorar la comprensión.

---

Cada ejercicio incluye:
- Un archivo README explicativo
- El código fuente completo
- Los datos o archivos necesarios
- (Opcionalmente) capturas o ejemplos en la carpeta `/images`

[← Volver al README principal](./README.md)

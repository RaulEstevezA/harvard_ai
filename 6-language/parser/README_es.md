# Parser

Este proyecto forma parte del curso **CS50's Introduction to Artificial Intelligence with Python**, dentro de la unidad de **Language** (Procesamiento del Lenguaje Natural).  
El objetivo de este ejercicio es implementar un parser basado en una gramática libre de contexto (CFG) capaz de analizar la estructura sintáctica de frases simples en inglés.

## Descripción del Proyecto

El parsing es un problema fundamental en el procesamiento del lenguaje natural. Un parser intenta determinar cómo se relacionan las palabras dentro de una frase identificando su estructura gramatical.

En este proyecto, el parser se construye utilizando una **gramática libre de contexto (CFG)** y el `ChartParser` de NLTK. La gramática define:

- El vocabulario válido del lenguaje (símbolos terminales)
- Las estructuras sintácticas permitidas (reglas no terminales)

Dada una frase de entrada, el programa genera uno o más árboles sintácticos que representan posibles interpretaciones gramaticales.

## Cómo Funciona

El programa opera en varias etapas:

1. **Preprocesamiento**
   - La frase de entrada se tokeniza utilizando NLTK.
   - Todos los tokens se convierten a minúsculas.
   - Se eliminan los tokens que no contienen caracteres alfabéticos.

2. **Definición de la Gramática**
   - Los símbolos terminales definen las palabras permitidas.
   - Las reglas no terminales definen cómo se forman frases y estructuras.

3. **Parsing**
   - La frase se analiza utilizando el `ChartParser` de NLTK.
   - Se generan árboles sintácticos válidos según la gramática.

4. **Extracción de Sintagmas Nominales (NP)**
   - El árbol sintáctico se analiza para extraer los sintagmas nominales.
   - Solo se devuelven los sintagmas nominales mínimos (sin NP anidados).

## Cómo Ejecutarlo

Se **recomienda utilizar un entorno virtual de Python** para evitar conflictos de dependencias.

Crea y activa un entorno virtual, luego instala las dependencias:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Si NLTK muestra un error de recursos del tokenizer, descarga los datos necesarios una sola vez:

```bash
python3
```

```python
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
exit()
```

### Ejecución

Ejecuta el parser e introduce una frase cuando se solicite:

```bash
python3 parser.py
```

También puedes proporcionar un archivo con una frase:

```bash
python3 parser.py sentences/1.txt
```

## Ejemplo de Salida

Entrada de ejemplo:

```text
Sentence: holmes sat in the armchair
```

Resultado de ejemplo (simplificado):

```text
(S
  (NP holmes)
  (VP sat
    (PP in
      (NP the armchair))))
```

Sintagmas Nominales Detectados:

```text
holmes
the armchair
```

![Resultado](../../images/parser.png)

## Conceptos Clave Implementados

- Gramáticas Libres de Contexto (CFG)
- Parsing sintáctico
- Procesamiento del Lenguaje Natural (NLP)
- Estructuras de árbol y recorrido
- Extracción de sintagmas nominales (NP)

## Archivos

- **`parser.py`** → Programa principal. Define la gramática, preprocesa la entrada, analiza frases y extrae sintagmas nominales.

## Acceso Directo

- [**Ver el código fuente**](./parser.py)  
- [Volver al README principal](../../README_es.md)

## Autor

Este proyecto fue realizado por **Raul Estevez** como parte de los ejercicios del curso CS50 AI.

# Traductor de Emojis - README.md

## Introducción

Bienvenido al repositorio del "Traductor de Emojis", un programa desarrollado en Python que te permite traducir abreviaturas de emojis a emojis reales. Este proyecto se enfoca en la utilización de expresiones regulares y el manejo de diccionarios para lograr una traducción eficiente y precisa. A continuación, encontrarás una guía detallada sobre la estructura del código, los módulos utilizados y cómo funciona cada parte del programa.

## Índice

1. [**Diccionario de Emojis (`diccionario.py`)**](#diccionario-de-emojis)
2. [**Verificación de Palabras en Español (`palabrasRAE.py`)**](#verificación-de-palabras-en-español)
3. [**Traductor con Expresiones Regulares (`traductor.py`)**](#traductor-con-expresiones-regulares)
4. [**Interfaz Gráfica (`interfas.py`)**](#interfaz-gráfica)
5. [**Conclusion**](#conclusion)
6. [**Video Explicativo Codigo (#Video-Explicativo-Codigo)**](#video-explicativo-codigo)

## Diccionario de Emojis (`diccionario.py`)

En este módulo, se define un diccionario llamado `diccionario_de_emojis`, que asocia abreviaturas con emojis correspondientes. Este diccionario es esencial para la traducción de abreviaturas a emojis en el programa principal.

```python
# diccionario.py
diccionario_de_emojis = { ... }

```

### Verificación de Palabras en Español (`palabrasRAE.py`)

Este módulo se encarga de leer archivos en un directorio específico, normalizar palabras eliminando tildes y construir un conjunto (`diccionarioRAE`) de palabras en español para su verificación. Esta verificación se utiliza para asegurar que las palabras ingresadas en la interfaz de usuario estén en español.

```python
# palabrasRAE.py
import os
import unicodedata

# ...

def normalizar(palabra):
    """Normaliza una palabra eliminando tildes y caracteres especiales."""
    palabra = palabra.lower()
    palabra = ''.join(
        c for c in unicodedata.normalize('NFD', palabra)
        if unicodedata.category(c) != 'Mn'
    )
    palabra = palabra.replace('ñ', 'n')
    palabra = palabra.replace(' ', '')
    return palabra

# ...

def construir_diccionario():
    """Construye un conjunto de palabras en español."""
    diccionario = set()
    for archivo in os.listdir('palabras'):
        with open(f'palabras/{archivo}', 'r', encoding='utf-8') as f:
            for linea in f:
                diccionario.add(normalizar(linea))
    return diccionario

# ...

diccionarioRAE = construir_diccionario()

```

## Traductor con Expresiones Regulares (`traductor.py`)

Este módulo se encarga de traducir abreviaturas de emojis a emojis reales utilizando expresiones regulares. Para lograr esto, se define una expresión regular que busca coincidencias con abreviaturas de emojis en una cadena de texto. Luego, se utiliza el método `sub` de la clase `re` para reemplazar cada coincidencia con su respectivo emoji.

```python

# traductor.py
import re

# ...


def traducir(texto):
    """Traduce abreviaturas de emojis a emojis reales."""
    return re.sub(r':([a-z0-9_]+):', lambda match: diccionario_de_emojis[match.group(1)], texto)

```

## Interfaz Gráfica (`interfas.py`)

Este módulo se encarga de crear una interfaz gráfica para el programa utilizando la biblioteca `tkinter`. La interfaz gráfica consiste en una ventana con un campo de texto para ingresar texto y un botón para traducir el texto ingresado. Además, se utiliza el módulo `traductor` para traducir el texto ingresado y se utiliza el módulo `palabrasRAE` para verificar que el texto ingresado esté en español.

```python

# interfas.py
import tkinter as tk
from tkinter import messagebox
from traductor import traducir
from palabrasRAE import diccionarioRAE

# ...

def traducir_texto():
    """Traduce el texto ingresado en el campo de texto."""
    texto = campo_texto.get('1.0', 'end-1c')
    if texto == '':
        messagebox.showerror('Error', 'No se ingresó texto.')
    elif not texto.isalpha():
        messagebox.showerror('Error', 'El texto ingresado debe contener solo letras.')
    elif not texto in diccionarioRAE:
        messagebox.showerror('Error', 'El texto ingresado no está en español.')
    else:
        texto_traducido = traducir(texto)
        messagebox.showinfo('Traducción', texto_traducido)

# ...

ventana = tk.Tk()

# ...

campo_texto = tk.Text(ventana, height=10, width=50)

# ...

boton_traducir = tk.Button(ventana, text='Traducir', command=traducir_texto)

# ...

ventana.mainloop()

```

## Conclusion

Este es un programa sencillo para leer cadenas de texto y definir si esta o no cada palabra en un diccionario o en forma de emojis
Este trabajo fue desarrollado por
Luis Miguel Giraldo D //
Leidy Gallo Vargas


## Video Explicativo Codigo

https://youtu.be/O-1lrGAm8PE



import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
from diccionario import dicconario_de_emojis
from traductor import Traductor

class InterfazTraductor:
    def __init__(self, master):
        self.master = master
        self.master.title("Traductor de Texto")
        self.master.geometry("400x400")

        self.diccionario = dicconario_de_emojis
        self.traductor = Traductor(self.diccionario)

        self.label_instrucciones = tk.Label(master, text="Ingresa el texto:")
        self.label_instrucciones.pack(pady=5)

        self.texto_entrada = scrolledtext.ScrolledText(master, width=40, height=5, wrap=tk.WORD)
        self.texto_entrada.pack(pady=5)

        self.boton_traducir = tk.Button(master, text="Traducir", command=self.traducir_texto)
        self.boton_traducir.pack(pady=5)

        self.label_resultado = tk.Label(master, text="")
        self.label_resultado.pack(pady=5)

    def traducir_texto(self):
        texto = self.texto_entrada.get("1.0", tk.END).strip()

        if not texto:
            messagebox.showwarning("Advertencia", "Ingresa un texto antes de traducir.")
            return

        texto_traducido = self.traductor.traducir(texto)
        cantidad_coincidencias = self.traductor.contador_de_coincidencias(texto)
        cantidad_palabras = self.traductor.contador_de_palabras(texto)

        resultado = f"Texto traducido: {texto_traducido}\nEmojis Encontrados: {cantidad_coincidencias}\nPalabras Encontradas: {cantidad_palabras}"

        self.label_resultado.config(text=resultado, font=("Arial", 12))
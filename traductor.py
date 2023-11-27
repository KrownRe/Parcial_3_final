import re
from palabrasRAE import verificador


class Traductor:
    def __init__(self, diccionario):
        self.diccionario = diccionario
        self.expresion_regular = re.compile('|'.join(re.escape(key) for key in self.diccionario.keys()),
                                            flags=re.IGNORECASE)

    def traducir(self, texto):
        return self.expresion_regular.sub(lambda x: self.diccionario[x.group().lower()], texto)

    def contador_de_coincidencias(self, texto):
        return len(self.expresion_regular.findall(texto))

    def contador_de_palabras(self, texto):
        oracion_emojis = re.sub(r'[^a-zA-Z]', ' ',self.traducir(texto))
        return len([palabra for palabra in oracion_emojis.split() if palabra and verificador(palabra)])

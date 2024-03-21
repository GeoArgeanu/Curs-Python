import csv
import json

'''
Factory Pattern
Acest pattern ne permite sa creăm un obiect dintr-o clasa
folosind o alta clasa (fabrica). Fabrica are posibilitatea de
a crea obiecte din mai multe clase (de obicei aceste clase
sunt siblings, adica mostenesc de la acelasi parinte).


Vom implementa următoarele clase:
English/French/Spanish Translator – clase care știu sa
traduca cuvinte din română în limba specificata
translations va fi un dicționar cu acele cuvinte, exemplu
`{ “masina”: “car” }` – se poate hardcoda în clasa
localize va fi o funcție care pentru un parametru de intrare,
ne va da traducerea lui în acea limba (exemplu
`input(“masina”)` returneaza “car”)

TranslatorFactory – clasa care are o singura metoda
 (preferabil statica sau de clasa) numita get_translator(language)
 – in functie de parametrul language, returnează un translator object.


factory = TranslatorFactory()

english_trans = factory.get_translator('en')
spanish_trans = factory.get_translator('es')

print(f'In engleza zicem {english_trans.localize("masina")}')
print(f'In spaniola zicem {spanish_trans.localize("masina")}')
'''


class Translator:
    translations = {}

    def localize(self, text):
        return self.translations.get(text)


class EnglishTranslator(Translator):
    def __init__(self):
        self.translations = {
            # EN
            "salut": "hello",
            "lume": "world",
            "pisica": "cat",
            "caine": "dog",
            "soare": "sun",
            "carte": "book",
            "puteri": "powers",
            "apa": "water",
            "munte": "mountain",
            "oras": "city",
            "floare": "flower",
            "masa": "table",
            "telefon": "phone",
            "tara": "country",
            "ploaie": "rain",
            "fericit": "happy",
            "fermecat": "enchanted",
            "cafea": "coffee",
            "calatorie": "journey",
            "muzica": "music"
        }


class SpanishTranslator(Translator):
    def __init__(self):
        self.translations = {
            # ES
            "salut": "hola",
            "lume": "mundo",
            "pisica": "gato",
            "caine": "perro",
            "soare": "sol",
            "carte": "libro",
            "puteri": "poderes",
            "apa": "agua",
            "munte": "montaña",
            "oras": "ciudad",
            "floare": "flor",
            "masa": "mesa",
            "telefon": "telefono",
            "tara": "pais",
            "ploaie": "lluvia",
            "fericit": "feliz",
            "fermecat": "encantado",
            "cafea": "cafe",
            "calatorie": "viaje",
            "muzica": "música"
        }


class FrenchTranslator(Translator):
    def __init__(self):
        self.translations = {
            # FR
            "salut": "salut",
            "lume": "monde",
            "pisica": "chat",
            "caine": "chien",
            "soare": "soleil",
            "carte": "livre",
            "puteri": "pouvoirs",
            "apa": "eau",
            "munte": "montagne",
            "oras": "ville",
            "floare": "fleur",
            "masa": "table",
            "telefon": "telephone",
            "tara": "pays",
            "ploaie": "pluie",
            "fericit": "heureux",
            "fermecat": "ensorcele",
            "cafea": "cafe",
            "calatorie": "voyage",
            "muzica": "musique"
        }


class TranslatorFactory:
    __TRANSLATORS_MAPPING = {
        'EN': EnglishTranslator,
        'ES': SpanishTranslator,
        'FR': FrenchTranslator
    }

    def get_translator(self, language):
        translator_class = self.__TRANSLATORS_MAPPING.get(language)
        return translator_class()


factory = TranslatorFactory()
english_trans = factory.get_translator('EN')
french_trans = factory.get_translator('FR')
print(f'In engleza zicem {english_trans.localize("masina")}')
print(f'In franceza zicem {french_trans.localize("masina")}')


class FileTranslator:
    def __init__(self, filename):
        self.filename = filename

    def read_words(self):
        with open(self.filename, 'r') as f:
            reader = csv.DictReader(f)
            return list(reader)

    def translate(self):
        words = self.read_words()
        translated_words = []
        factory = TranslatorFactory()
        for word in words:
            translator = factory.get_translator(word['limba_destinatie'].upper())
            translated_words.append({
                'cuvant_initial': word['cuvant'],
                'limba_de_traducere': word['limba_destinatie'],
                'traducere': translator.localize(word['cuvant'])
            })
        self.write_translations(translated_words)

    def write_translations(self, translated_words):
        with open('translations.json', 'w') as f:
            json.dump(translated_words, f, indent=4)


file_translator = FileTranslator('de_tradus.csv')
file_translator.translate()

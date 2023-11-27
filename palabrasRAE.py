import os
import unicodedata

dics_path = "./diccionarioRAE"

# Read all files in the 'dics' directory
files = os.listdir(dics_path)

diccionarioRAE = set()


def quitar_tildes(cadena):
    return unicodedata.normalize('NFD', cadena).encode('ascii', 'ignore').decode('utf-8')


for file in files:
    file_path = os.path.join(dics_path, file)

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            words = f.read().split('\n')

            for word in words:
                cleaned_word = quitar_tildes(word.replace('[0-9]', '').strip().lower())

                if ',' in cleaned_word:
                    parts = [quitar_tildes(w.strip()) for w in cleaned_word.split(",")]
                    diccionarioRAE.add(parts[0])
                    diccionarioRAE.add(parts[0][:-len(parts[1])] + parts[1])
                else:
                    diccionarioRAE.add(cleaned_word)

    except Exception as error:
        print(f"Error reading file {file_path}: {error}")


# Now 'dic' contains the unique words without tildes

def verificador(word):
    return word.strip().lower() in diccionarioRAE

# Example usage:
# result = validate_word("example")
# print(result)

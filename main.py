def main():
   
    path_to_file = "books/frankenstein.txt"
    

    print(f"--- Begin report of {path_to_file} ---")

    text = get_text_from_file(path_to_file)
    palabras = get_words(text)
    contador_palabras = count_words(palabras)

    print(f"{contador_palabras} words found in document\n")

    diccionario_ocurrencias = count_letters_in_text(palabras)
    imprime_ocurrencias(diccionario_ocurrencias)


    


def get_text_from_file(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def get_words(text):
    return text.split()

def count_words(palabras):
    return len(palabras)

def count_letters_in_text(palabras):

    diccionario = {}
    abc = "abcdefghijklmnopqrstuvwxyz"
    abc_no_deseados ="0123456789!#$%&'()*+,-./:;<=>?@[\\]^_{|}~`)"+'"'

    # abc_list = list(abc)
    for c in abc:
        diccionario[c] = 0

    for palabra in palabras:
        #quitando signos raros
        palabra_limpia = ""
        for letra in palabra:
            if letra in abc_no_deseados:
                palabra_limpia+=""
            else:
                palabra_limpia+=letra
        
        # Pasando a lower case
        lower_palabra = palabra_limpia.lower()
        for letra in lower_palabra:
            diccionario[letra] += 1

    # ordenando el diccionario
    diccionario_sorted = {}
    while len(diccionario) > 0:
        max = float("-inf")
        ubi = ''        

        for letra in diccionario:
            if diccionario[letra] > max:
                max = diccionario[letra]
                ubi = letra

        diccionario_sorted[ubi] = max
        
        del diccionario[ubi]

    return diccionario_sorted

def imprime_ocurrencias(diccionario):

    for letra in diccionario:
        print(f"The '{letra}' character was found {diccionario[letra]} times")

    return None
    
main()
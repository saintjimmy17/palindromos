def palindromo(palabra):
    palabra = palabra.lower()
    palabra = palabra.replace(" ", "")
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run():
    palabra = str(input("Escribe una palabra: "))
    es_palindromo = palindromo(palabra)
    if es_palindromo:
        print("Es un palindromo")
    else:
        print("No es un palindromo")




if __name__ == '__main__':
    run()
    


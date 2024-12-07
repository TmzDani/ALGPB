def texto_para_leet(texto):
    subs = {
        'a': '4', 'b': '8', 'c': '(', 'd': '|)', 'e': '3',
        'f': '|=', 'g': '6', 'h': '#', 'i': '1', 'j': '_|',
        'k': '|<', 'l': '1', 'm': '/\\/', 'n': '|\\|', 'o': '0',
        'p': '|*', 'q': '0_', 'r': '|2', 's': '5', 't': '7',
        'u': '|_|', 'v': '\\/', 'w': '\\/\\/', 'x': '><', 'y': '`/',
        'z': '2'
    }
    return ''.join(subs.get(char.lower(), char) for char in texto)     

text_user = input("Digite um texto: ")
print("Leet speak:", text_for_leet(tex_user))
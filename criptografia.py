def cifra_de_substituicao(texto, deslocamento):
    texto_cifrado = ""
    for char in texto:
        if char.isalpha():  # Verifica se o caractere é uma letra
            maiuscula = char.isupper()  # Verifica se o caractere é maiúsculo
            char = char.lower()  # Converte para minúsculas para facilitar a cifragem
            char_cifrado = chr(((ord(char) - ord('a') + deslocamento) % 26) + ord('a')) 
            if maiuscula:  # Converte de volta para maiúsculas se necessário
                char_cifrado = char_cifrado.upper()
            texto_cifrado += char_cifrado
        else:
            texto_cifrado += char  # Mantém caracteres não-alfabéticos inalterados
    return texto_cifrado

def cifra_arquivo(nome_arquivo_entrada, nome_arquivo_saida, deslocamento):
    with open(nome_arquivo_entrada, 'r') as arquivo_entrada:
        texto_original = arquivo_entrada.read()
    
    texto_cifrado = cifra_de_substituicao(texto_original, deslocamento)
    
    with open(nome_arquivo_saida, 'w') as arquivo_saida:
        arquivo_saida.write(texto_cifrado)

nome_arquivo_entrada = "ebnf.txt"
nome_arquivo_saida = "ebnf.txt"
deslocamento = 15

cifra_arquivo(nome_arquivo_entrada, nome_arquivo_saida, deslocamento)

import os

def substituir_caractere_invalido(nome_arquivo):
    caracteres_invalidos = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']
    substituto = '-'

    for c in caracteres_invalidos:
        nome_arquivo = nome_arquivo.replace(c, substituto)

    return nome_arquivo

def adicionar_numero_se_existir(arquivo):
    nome_arquivo, extensao = os.path.splitext(arquivo)
    contador = 1
    novo_arquivo = arquivo

    while os.path.exists(novo_arquivo):
        novo_arquivo = f"{nome_arquivo}_{contador}{extensao}"
        contador += 1

    return novo_arquivo
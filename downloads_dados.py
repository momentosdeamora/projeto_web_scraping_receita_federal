import csv
import json
from renomeia_download import substituir_caractere_invalido, adicionar_numero_se_existir

def salvar_txt(dados, arquivo):
    nome_arquivo = substituir_caractere_invalido(arquivo) + '.txt'
    novo_arquivo = adicionar_numero_se_existir(nome_arquivo)

    with open(novo_arquivo, 'w', encoding='latin-1') as file:
        for linha in dados:
            file.write('\t'.join(linha) + '\n')


def salvar_csv(dados, arquivo):
    nome_arquivo = substituir_caractere_invalido(arquivo) + '.csv'
    novo_arquivo = adicionar_numero_se_existir(nome_arquivo)

    with open(novo_arquivo, 'w', newline='', encoding='latin-1') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(dados)


def salvar_json(dados, arquivo):
    nome_arquivo = substituir_caractere_invalido(arquivo) + '.json'
    novo_arquivo = adicionar_numero_se_existir(nome_arquivo)

    with open(novo_arquivo, 'w', encoding='latin-1') as file:
        json.dump(dados, file, indent=4)
        
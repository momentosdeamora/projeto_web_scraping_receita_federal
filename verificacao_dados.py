import os

def verifica_download_txt(arquivo):
    arquivo_txt = arquivo + '.txt'
    if os.path.exists(arquivo_txt):
        print(f'\n\033[32mO arquivo foi baixado.\033[m')
    else:
        print(f'\n\033[31mO arquivo não foi encontrado.\033[m')


def verifica_download_csv(arquivo):
        arquivo_csv = arquivo + '.csv'
        if os.path.exists(arquivo_csv):
            print(f'\n\033[32mO arquivo foi baixado.\033[m')
        else:
            print(f'\n\033[31mO arquivo não foi encontrado.\033[m')


def verifica_download_json(arquivo):
        arquivo_json = arquivo + '.json'
        if os.path.exists(arquivo_json):
            print(f'\n\033[32mO arquivo foi baixado.\033[m')
        else:
            print(f'\n\033[31mO arquivo não foi encontrado.\033[m')
            
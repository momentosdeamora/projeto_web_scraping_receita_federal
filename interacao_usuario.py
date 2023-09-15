from downloads_dados import salvar_txt
from downloads_dados import salvar_csv
from downloads_dados import salvar_json
from verificacao_dados import verifica_download_txt
from verificacao_dados import verifica_download_csv
from verificacao_dados import verifica_download_json
from formatacao import formatar_linha

def escolha_tipo_de_download():
    opcoes_validas = [1, 2, 3, 4, 5]
    while True:
        try:
            opcao = input('\nDigite o número correspondente ao formato que você deseja salvar o arquivo: \n'
                          '[ 1 ] - txt\n'
                          '[ 2 ] - csv\n'
                          '[ 3 ] - json\n'
                          '[ 4 ] - Todos os anteriores\n'
                          '[ 5 ] - Sair do sistema\n').strip()
            if opcao and opcao.isnumeric():
                numero_inteiro = int(opcao)
                if numero_inteiro in opcoes_validas:
                    return numero_inteiro
            else:
                print('\033[31mERRO! Por favor, digite uma opção válida.\n\033[m')
        except  (ValueError, NameError):
                print("\n\033[31mEntrada inválida. Digite um número entre 1 e 4 de acordo com o formato de arquivo desejado.\n\033[m")

def download_arquivos(dados, escolha_do_usuario):
        print(f'\nVocê escolheu a opção {escolha_do_usuario}.')

        if escolha_do_usuario == 1 or escolha_do_usuario == 4:
            print(f'\nVou baixar os arquivos... Por favor, aguarde.')
            arquivo_txt = input('Digite o nome do arquivo txt: ')
            salvar_txt(dados, arquivo_txt)
            verifica_download_txt(arquivo_txt)

        if escolha_do_usuario == 2 or escolha_do_usuario == 4:
            print(f'\nVou baixar os arquivos... Por favor, aguarde.')
            arquivo_csv = input('Digite o nome do arquivo csv: ')
            salvar_csv(dados, arquivo_csv)
            verifica_download_csv(arquivo_csv)

        if escolha_do_usuario == 3 or escolha_do_usuario == 4:
            print(f'\nVou baixar os arquivos... Por favor, aguarde.')
            arquivo_json = input('Digite o nome do arquivo json: ')
            salvar_json(dados, arquivo_json)
            verifica_download_json(arquivo_json)

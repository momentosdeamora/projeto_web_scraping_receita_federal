from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from conexao_internet import check_internet
from conexao_internet import recarregar_pagina
from navegacao import navegue
from dados import ler_tabela
from formatacao import formatar_linha
from interacao_usuario import escolha_tipo_de_download
from interacao_usuario import download_arquivos
import time

selenium_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=selenium_service)


# Programa Principal
programa_principal = True

while programa_principal:
    if check_internet():
        formatar_linha('\033[34mSOFTWARE SELIC\033[m')
        print('Realizando o processamento...')

        navegue(driver)

        xpath_tabela_1 = '//*[@id="parent-fieldname-text"]/table[2]/tbody'
        dados_tabela_1 = ler_tabela(driver, xpath_tabela_1)

        xpath_tabela_2 = '//*[@id="parent-fieldname-text"]/table[3]/tbody'
        dados_tabela_2 = ler_tabela(driver, xpath_tabela_2)

        programa_secundario = True

        while programa_secundario:
            escolha_do_usuario = escolha_tipo_de_download()

            if escolha_do_usuario == 5:
                print(f'\nVocê escolheu a opção {escolha_do_usuario}.')
                print('Vou encerrar o programa!')
                formatar_linha('\033[33m<< PROGRAMA ENCERRADO >>\033[m')
                driver.quit()
                programa_principal = False
                break
            else:
                download_arquivos(dados_tabela_1, escolha_do_usuario)
            while True:
                try:
                    opcao_novo_download = input('\nDeseja baixar outros formatos?\n'
                                                'Digite a letra "S" para voltar ao menu de opções ou a letra "N" para encerrar o programa:\n').strip()
                    if opcao_novo_download.upper() == 'S':
                        ...
                        break
                    elif opcao_novo_download.upper() == 'N':
                        formatar_linha('\033[33m<< PROGRAMA ENCERRADO >>\033[m')
                        driver.quit()
                        programa_secundario = False
                        break
                    else:
                        print('\n\033[31mERRO! Por favor, digite apena a letra "S" ou a letra "N".\n\033[m')
                except (ValueError, NameError):
                    print(
                        "\n\033[31mEntrada inválida. Digite .\n\033[m")

        programa_principal = False
    else:
        recarregar_pagina(driver)
        print('Vou tentar conectar novamente daqui 5 minutos.')
        time.sleep(15)
        continue

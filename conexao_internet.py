from selenium.common.exceptions import WebDriverException
import requests

def check_internet():
    url = 'https://www.gov.br/receitafederal/pt-br'
    try:
        resposta = requests.get(url, timeout=5)
        if resposta.status_code == 200:
            print('\n\033[32mConectado à internet!\033[m')
            return True

    except requests.ConnectionError:
        print('\n\033[31mSem conexão com a internet!\033[m')
        return False

def recarregar_pagina(driver):
    max_tentativas = 3
    for tentativa in range(1, max_tentativas + 1):
        try:
            driver.get('https://www.gov.br/receitafederal/pt-br')
            if check_internet():
                print('\nConexão restabelecida na tentativa', tentativa)
                break
            else:
                print('\n\033[31mTentativa', tentativa, 'falhou.\033[m')
        except WebDriverException as excecao:
            if "net::ERR_INTERNET_DISCONNECTED" in str(excecao):
                print('\n\033[31mVerifique sua conexão com a internet!\033[m')
            else:
                print('\n\033[31mErro no WebDriver!\033[m', str(excecao))
    if not check_internet():
        print('\n\033[31mFalha ao restabelecer a conexão após', max_tentativas, 'tentativas.\033[m')
        
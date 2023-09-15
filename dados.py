from selenium.webdriver.common.by import By

def ler_tabela(driver, xpath_tabela):
    tabela = driver.find_element(By.XPATH, xpath_tabela)
    linhas = tabela.find_elements(By.TAG_NAME, 'tr')
    lista = []
    for linha in linhas:
        colunas = linha.find_elements(By.TAG_NAME, 'td')
        linha_lista = [coluna.text for coluna in colunas]
        lista.append(linha_lista)
    return lista
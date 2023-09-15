from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from dados import ler_tabela


url = 'https://www.gov.br/receitafederal/pt-br'

def navegue(driver):
    driver.get(url)
    fecha_pop_up(driver)
    aceita_cookies(driver)
    abre_menu_hambuguer(driver)
    abre_menus(driver)
    abre_pag_selic(driver)



def fecha_pop_up(driver):
    # Executa um script JavaScript para fechar o pop-up e liberar a tela inicial
    driver.execute_script('''
        var element = document.querySelector('#barra-sso');
        var shadowRoot = element.shadowRoot;
        var aside = shadowRoot.querySelector('#sso-status-bar');
        var popup = aside.querySelector('#sso-status-bar > div.popup-login-overlay.msg-signed-out');
        if (popup) {
            popup.parentNode.removeChild(popup);
        }
        var closeButton = shadowRoot.querySelector('#govbr-login-overlay-wrapper');
        if (closeButton) {
            closeButton.click();
        }
        var menuButton = shadowRoot.querySelector('#site-header > div.main > div > div.site-name-wrapper > a');
        if (menuButton) {
            menuButton.click();
        }
    ''')


def aceita_cookies(driver):
    # Aceita os Cookies na Página Inicial
    accept_button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.dsgov > div > div > div > div > div.br-modal-footer.actions > button.br-button.secondary.small.btn-accept')))
    accept_button.click()


def abre_menu_hambuguer(driver):
    # Abre o Menu Hamburguer
    menu_hamburguer = driver.find_element(By.TAG_NAME, 'header')
    link_menu_hamburguer = menu_hamburguer.find_element(By.XPATH, '//*[@id="site-header"]/div[2]/div/div[1]/a')
    link_menu_hamburguer.click()


def abre_menus(driver):
    # Localização do Menu Parte 1
    li1 = driver.find_element(By.CSS_SELECTOR, '#main-navigation > ul > li:nth-child(2)')
    a_href = li1.find_element(By.CSS_SELECTOR, 'a')
    actions = ActionChains(driver)
    actions.move_to_element(li1)

    # Localização do Menu Parte 2
    li2 = driver.find_element(By.CSS_SELECTOR, '#main-navigation > ul > li:nth-child(2) > ul > li:nth-child(10)')
    a_href = li2.find_element(By.CSS_SELECTOR, 'a')
    actions.move_to_element(li2)

    # Localização do Menu Parte 3
    li3 = driver.find_element(By.CSS_SELECTOR, '#main-navigation > ul > li:nth-child(2) > ul > li:nth-child(10) > ul > li:nth-child(8)')
    a_href = li3.find_element(By.CSS_SELECTOR, 'a')
    actions.move_to_element(li3).click()
    actions.perform()


def abre_pag_selic(driver):
    #Abrir Taxa de Juros Selic
    liselic_element = driver.find_element(By.CSS_SELECTOR, '#e090f1f84b2b4e4880332f232fe4d33e > div > ul > li:nth-child(2)')
    element_to_click = liselic_element.find_element(By.XPATH, '//*[@id="e090f1f84b2b4e4880332f232fe4d33e"]/div/ul/li[2]/a')
    actions = ActionChains(driver)
    actions.move_to_element(liselic_element).click()
    actions.perform()

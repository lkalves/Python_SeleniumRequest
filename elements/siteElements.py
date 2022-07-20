from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class GoogleElements:
    def __init__(self, browser):
        self.resultadoPesquisa = None
        self.campoPesquisa = None
        self.url = 'http://www.google.com.br'
        self.driver = browser

    def elementos_pagina(self):
        self.campoPesquisa = self.driver.find_element(By.XPATH, '//*[@title="Pesquisar"]')

    def pesquisa_google(self):
        lst = []
        self.resultadoPesquisa = self.driver.find_elements(By.XPATH, '//*[@id="rso"]//*/div[1]/a')

        for link in self.resultadoPesquisa:
            try:
                a = link.find_element(By.XPATH, './/div/cite')
                if a.text:
                    href = link.get_attribute('href')
                    lst.append(href)
            except NoSuchElementException:
                continue
        return lst

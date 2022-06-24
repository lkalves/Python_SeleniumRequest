import time
import requests

from behave import given, when, then
from selenium.webdriver.common.keys import Keys

from elements.siteElements import GoogleElements


@given('que estou no google')
def acessa_site(context):
    starting_url = context.browser.current_url
    context.googleElements = GoogleElements(context.browser)
    context.browser.get(context.googleElements.url)
    context.googleElements.elementos_pagina()
    assert starting_url != context.browser.current_url
    time.sleep(2)


@when('pesquiso por github')
def pesquisa_google(context):
    context.googleElements.elementos_pagina()
    context.googleElements.campoPesquisa.send_keys('Github')
    context.googleElements.campoPesquisa.send_keys(Keys.RETURN)
    time.sleep(3)
    context.retorna_lista = context.googleElements.pesquisa_google()


@then('então devo visualizar os 5 primeiros resultados da pesquisa')
def visualiza_tela(context):
    for count, linha in enumerate(context.retorna_lista):
        if count + 1 == 1:
            print(f'\n{count + 1}: {linha}')
        else:
            print(f'{count + 1}: {linha}')
    assert context.retorna_lista is not None

@given('que estou usando request')
def requisition_request(context):
    context.res = requests.get('https://api.github.com/users/lkalves/repos')
    assert context.res.status_code == 200


@when('devo pegar todos repositorios de LKALVES')
def repositories_github(context):
    context.var = context.res.json()
    context.gravar = []
    for linha in context.var:
        context.gravar.append(linha['html_url'])


@then('então devo apresentar os 5 primeiros resultados')
def resultado_requisition(context):
    for i in range(5):
        if i == 0:
            print(f'\n{i + 1}: {context.gravar[i]}')
        else:
            print(f'{i + 1}: {context.gravar[i]}')
    assert len(context.gravar) >= 5

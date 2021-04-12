# Importo librerias a usar
from behave import *
from selenium import webdriver
from nose.tools import assert_equal, assert_true
# importo pages a usar
from Pages.googleIndex import *
from Pages.googleResults import *
from Pages.results import *


@step('Me encuentro en la página principal de Google')
def step_impl(context):
    context.browser = webdriver.Chrome('webdriver/chromedriver.exe')
    context.browser.get('https://www.google.com/')


@step('Tipero “The name of the wind” dentro del campo de búsqueda')
def step_impl(context):
    index = googleIndex(context.browser)
    index.google_search('The name of the wind')


@step('Clickeo en el botón “Google Search”')
def step_impl(context):
    index = googleIndex(context.browser)
    index.google_search_click()


@step('Me dirige a la página de resultados')
def step_impl(context):
    google_results = GoogleResults(context.browser)
    try:
        assert_true('https://www.google.com/search?q=The+name+of+the+wind' in google_results.google_results())
    except AssertionError:
        print('La pagina de resultados no es la correcta')


@step('El primer resultado es “The Name of the Wind - Patrick Rothfuss”')
def step_impl(context):
    google_results = GoogleResults(context.browser)
    try:
        assert_true('The Name of the Wind - Patrick Rothfuss' in google_results.google_first_results())
    except AssertionError:
        print('El primer resultado no es el correcto')


@step('Clickeo en el primer resultado')
def step_impl(context):
    google_results = GoogleResults(context.browser)
    google_results.google_first_results_click()


@step('Me dirige a la página de “Patrick Rothfuss - The Books”')
def step_impl(context):
    results = Results(context.browser)
    try:
        assert_equal(results.google_results(), 'Patrick Rothfuss - The Books')
    except AssertionError:
        print('Nos dirigimos a la pagina incorrecta')


# pasos extras para el scenario: Usuario puede buscar mediante sugerencias
@step('Tipeo “The name of the w” dentro del campo de búsqueda')
def step_impl(context):
    index = googleIndex(context.browser)
    index.google_search('The name of the w')


@step('Las lista de sugerencia es desplegada')
def step_impl(context):
    index = googleIndex(context.browser)
    try:
        assert_true(index.google_dropdowm_sugestion())
    except AssertionError:
        print('No se han desplegado las sugerencias de google')


@step('Clickeo en la primer opción sugerida')
def step_impl(context):
    index = googleIndex(context.browser)
    index.google_sugestion()

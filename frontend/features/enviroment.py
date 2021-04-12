# Cierro el browser despues de cada escenario
def after_scenario(context, scenario):
    context.browser.close()
    context.browser.quit()

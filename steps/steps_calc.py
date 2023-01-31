
from behave import given, when, then


@given(u'eu digito o número dez')
def digitando_dez(context):
    context.app.pages_calc.digita_dez()


@when(u'digito o botão de somar')
def sinal_add(context):
    context.app.pages_calc.sinal_add()
  

@when(u'digito o número vinte')
def digitando_vinte(context):
    context.app.pages_calc.digita_vinte()


@when(u'digito o botão de igual')
def sinal_igual(context):
    context.app.pages_calc.sinal_igual()


@then(u'eu verifico se o resultado da operação é trinta')
def recebe_resultado(context):
    context.app.pages_calc.recebe_resultado()

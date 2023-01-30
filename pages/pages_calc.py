from selenium.webdriver.common.by import By
from pages.base_page import Page


# Organização dos elementos que serão utilizados

class CalculadoraPage(Page):
    CLICA_UM = (By.ID, "com.google.android.calculator:id/digit_1")
    CLICA_ZERO = (By.ID, "com.google.android.calculator:id/digit_0")
    SINAL_PLUS = (By.ID, "com.google.android.calculator:id/op_add")
    CLICA_DOIS = (By.ID, "com.google.android.calculator:id/digit_2")
    CLICA_ZERO = (By.ID, "com.google.android.calculator:id/digit_0")
    CLICA_IGUAL = (By.ID, "com.google.android.calculator:id/eq")    
    VERIFICA_RESULT = (By.ID, "com.google.android.calculator:id/result_final")


    def digita_dez(self):      
        self.click_on_element(self.CLICA_UM)
        self.click_on_element(self.CLICA_ZERO)

    def sinal_add(self): 
        self.click_on_element(self.SINAL_PLUS)

    def digita_vinte(self): 
        self.click_on_element(self.CLICA_DOIS)
        self.click_on_element(self.CLICA_ZERO)

    def sinal_igual(self): 
        self.click_on_element(self.CLICA_IGUAL)

    def recebe_resultado(self): 
        self.assert_on_element (self.VERIFICA_RESULT)

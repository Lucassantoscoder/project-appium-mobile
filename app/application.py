from pages.pages_calc import CalculadoraPage


class Application:
    def __init__(self, driver):
        self.pages_calc = CalculadoraPage(driver)
     
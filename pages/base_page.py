# função para segregar os elementos

class Page:
    def __init__(self, driver):
        self.driver = driver

    def find_elements(self, locator):
        return self.driver.find_elements(by=locator[0],
                                         value=locator[1])
    #seleciona elemento
    def find_element(self, locator):
        return self.driver.find_element(by=locator[0],
                                        value=locator[1])

    #clica no elemento
    def click_on_element(self, locator):
        element = self.driver.find_element(by=locator[0],
                                           value=locator[1])
        element.click()

    #verifica se o elemento tem no display
    def assert_on_element(self, locator):
        element = self.driver.find_element(by=locator[0],
                                           value=locator[1])
        expected_text = "30"
        assert element.is_displayed(), "O elemento não existe!"
        actual_text = element.text
        assert actual_text == expected_text, f"Expected text '{expected_text}' but got '{actual_text}'"  
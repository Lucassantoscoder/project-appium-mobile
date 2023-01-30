from appium import webdriver
from app.application import Application

# configuração de  acordo com o ADV (Emulador instalado) 
# dispositivo fisico usa outro modelo de  desired capabilities.

def before_scenario(context, scenario):
    context.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",
                                      desired_capabilities={"platformName":"Android",
                                                            "automationName":"UiAutomator2",
                                                            'platformVersion': '11.0',
                                                            "deviceName":"Nexus 6 API 30",
                                                            "appPackage":"com.google.android.calculator",
                                                            "appActivity":"com.android.calculator2.Calculator"
                                                            })

    context.driver.implicitly_wait(15)

    context.app = Application(context.driver)

    # executa após o teste, fecha a aplicação.
def after_scenario(context, scenario):
    context.driver.quit()
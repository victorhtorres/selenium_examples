import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver


class HelloWorld(unittest.TestCase):

    # Ejecutar todo lo necesario antes de hacer la prueba
    # El decorador classmethod y el objeto cls permite abrir las páginas web, en una sola instancia de navegador
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
        driver = cls.driver
        driver.implicitly_wait(10) # esperar 10 segundos antes de realizar la siguiente acción (casos de prueba)

    # Caso de prueba: una serie de acciones para que el navegador lo automatice
    def test_hello_world(self):
        driver = self.driver
        driver.get('https://www.platzi.com')

    def test_visit_wikipedia(self):
        self.driver.get('https://www.wikipedia.org')

    # Ejecutar acciones después de finalizar las pruebas
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit() # Cerrar la ventana del navegador


if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reports', report_name='hello-world-report'))

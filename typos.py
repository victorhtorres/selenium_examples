import unittest
from selenium import webdriver


class Typos(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
        driver = self.driver
        driver.get('https://the-internet.herokuapp.com/')
        driver.find_element_by_link_text('Typos').click()

    def test_find_typo(self):
        driver = self.driver

        paragraph_to_check = driver.find_element_by_xpath('//*[@id="content"]/div/p[2]')
        text_to_check = paragraph_to_check.text

        tries = 1
        correct_text = "Sometimes you'll see a typo, other times you won't."

        while text_to_check != correct_text:
            driver.refresh()
            tries += 1
            paragraph_to_check = driver.find_element_by_xpath('//*[@id="content"]/div/p[2]')
            text_to_check = paragraph_to_check.text

        print(f"It took {tries} tries to find the typo")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)

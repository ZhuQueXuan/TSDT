from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUP(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('To_Do', self.browser.title), "browser title was:" + self.browser.title
        self.fail("Finish the test!")


if __name__ == 'main':
    unittest.main()

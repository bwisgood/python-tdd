from selenium import webdriver
import unittest


# browser = webdriver.Chrome()
# browser.get('http://localhost:8000')
#
# assert 'To-do' in browser.title
#
# browser.quit()

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')

        self.assertIn('To-do', self.browser.title)
        self.fail("Finish test!")


if __name__ == '__main__':
    unittest.main()

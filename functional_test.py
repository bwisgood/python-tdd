from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time


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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn("To-Do", header_text)

        # 邀请她写一个待办事项
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            input_box.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # 然后她在文本框中输入了"Buy peacock feathers"
        input_box.send_keys("Buy peacock feathers")

        # 她按下回车后，待办事项更新了
        # 待办事项的表格中显示了"1:Buy peacock feathers"
        input_box.send_keys(Keys.ENTER)
        time.sleep(2)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1:Buy peacock feathers to make a fly' for row in rows)
        )

        self.fail("Finish test!")


if __name__ == '__main__':
    unittest.main()

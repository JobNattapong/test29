from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
       self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # เป็นหน้าแรกเข้า app quiz
        self.browser.get('http://localhost:8000/quiz')

        # มี page title ที่ชื่อวว่า Quiz และมี header web-app ชื่อ Question
        self.assertIn('Quiz', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Question', header_text)
        time.sleep(2)

        # เจอคำถามและเข้าไปดูรายละเอียดของคำถาม
        self.browser.find_element_by_id('detail_question').click()
        time.sleep(2)

        # เจอช้อยให้เลือก True และ False ถ้ายังไม่เลือกและคลิก
        # จะขึ้นเป็นข้อความบอกให้เลือกคำถามก่อน
        self.browser.find_element_by_id('Answer').click()
        time.sleep(2)

        #ตอบ True
        self.browser.find_element_by_id('choice1').click()
        time.sleep(2)

        #เมื่อคลิกจะเห็นผลลัพธ์ว่ามีคนเลือกคำถามนี้ไปเท่าไหร่
        self.browser.find_element_by_id('Answer').click()
        time.sleep(2)

        #สามารถกลับเพิ่อตอบช้อยอื่น
        self.browser.find_element_by_id('back_to_datail').click()
        time.sleep(2)

        #สามารถกลับไปเลือกคำถามใหม่
        self.browser.find_element_by_id('back_to_index').click()
        time.sleep(2)



if __name__ == '__main__':
    unittest.main(warnings='ignore')

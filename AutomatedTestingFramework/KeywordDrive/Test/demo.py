from ddt import ddt, file_data

from AutomatedTestingFramework.KeywordDrive.Keyword_UI.web_ui import WebDemo
from time import sleep
import unittest

# demo = WebDemo('Chrome')
# demo.visit('http://www.baidu.com')
# demo.input_text('id', 'kw', 'OKC')
# demo.click('id', 'su')
# sleep(3)
# demo.quit()

@ddt
class CaseDemo(unittest.TestCase):
    @file_data('../Data/test_data.yaml')
    def test_1(self, **kwargs):
        demo = WebDemo(kwargs['type'])
        demo.visit(kwargs['url'])
        demo.input_text(kwargs['input']['name'], kwargs['input']['value'], kwargs['input']['txt'])
        demo.click(kwargs['click']['name'], kwargs['click']['value'])
        sleep(3)
        demo.quit()

if __name__ == '__main__':
    unittest.main()
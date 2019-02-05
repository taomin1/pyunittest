import unittest
import requests
import case_listener

test = case_listener.caseListener()


class test_case_suite(unittest.TestCase):
    def setUp(self):
        self.url = "http://www.baidu.com"

    @test.method_automation(dict(classname="test_case1"))
    def test_case1(self):
        response = requests.get(self.url)
        self.assertEqual(response.status_code,200)

if __name__=="__main__":
    # suite1 = unittest.TestLoader().loadTestsFromTestCase(test_baidu)
    # suite = unittest.TestSuite([suite1])
    # unittest.TextTestRunner(verbosity=2).run(suite)

    pass
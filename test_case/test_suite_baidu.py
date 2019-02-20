import unittest
import requests
import case_listener
from ddt import file_data,ddt

test = case_listener.caseListener()



@ddt
class test_case_suite(unittest.TestCase):
    def setUp(self):
        self.url = "http://www.baidu.com"

    @file_data("./test_baidu_dict.json")
    @test.method_automation(dict(classname="test_case1"))
    def test_case1(self,**kwargs):
        print("##")
        response = requests.get(self.url,params=kwargs["key"])
        self.assertEqual(response.status_code,kwargs["status_code"])

if __name__=="__main__":
    # suite1 = unittest.TestLoader().loadTestsFromTestCase("test_Case_suite")
    # suite = unittest.TestSuite([suite1])
    # unittest.TextTestRunner(verbosity=2).run(suite)
    unittest.main()
    # pass
import sys
import getopt
import unittest

opts, args = getopt.getopt(sys.argv[1:],"p:")
pattern = opts[0][1]
# discover = unittest.defaultTestLoader.discover("./",pattern='test_case_**.py')
discover = unittest.defaultTestLoader.discover("./test_case/",pattern=pattern)
runner = unittest.TextTestRunner()
runner.run(discover)
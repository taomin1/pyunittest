安装依赖包
1.pip3 install getopt
2.pip3 install unittest
3.pip3 install requests

用例存放路径为test_case
程序主入口 test_runner.py

实例：
pull代码后使用命令
python3 test_runner.py -p test_suite_**.py 执行用例

扩展：
用例编写必须以test_suit_**.py为目录格式，比如test_suite_baidu.py

jenkins集成
后续补充
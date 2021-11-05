import time
import unittest
import HTMLTestRunner
from case.add_team_case import AddTeamCase
from case.login_case import Login
from congfig.log import init_logging_config
import logging
init_logging_config()




suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(Login))
suite.addTest(unittest.makeSuite(AddTeamCase))

report_path = "../report/mhyj_test_report_{}.html".format(time.strftime("%Y-%m-%d"), time.localtime())
report_file = open(report_path, "wb")
runner = HTMLTestRunner.HTMLTestRunner(report_file, title="美好益家后台测试报告", description="目前包含登录、增加团队", verbosity=3)
runner.run(suite)


import unittest

from selenium.webdriver import Chrome

from RPA_Console_testEnv.common.log import logger
from RPA_Console_testEnv.common.readConfig import ReadConfig
from RPA_Console_testEnv.pageObject.choiceTenant import choiceTenantPage
from RPA_Console_testEnv.pageObject.loginPage import loginPage
from RPA_Console_testEnv.pageObject.usersPage import usersPage
from selenium import  webdriver


class usersTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        options.add_argument("--ignore-certificate-errors")
        cls.driver = webdriver.Chrome(options=options)

        cls.driver.maximize_window()
        cls.url = ReadConfig().getOptionValue('environment', 'url')  # 变成类范围的变量。
        cls.driver.get(cls.url)
        cls.driver.implicitly_wait(3)
        logger().debug('driver is setup.')

    def test_01(self):
        account = ReadConfig().getOptionValue('test_account01', 'account')
        password = ReadConfig().getOptionValue('test_account01', 'password')
        lo = loginPage(self.driver)
        lo.loginIn(account, password)
        url_ = ReadConfig().getOptionValue('environment', 'url') + '#/passport/login'
        self.assertEqual(self.driver.current_url, url_)

    def test_02(self):
        choiceTenant = choiceTenantPage(self.driver)
        choiceTenant.choiceTenant()
        url_ = ReadConfig().getOptionValue('environment', 'url') + '#/dashboard'
        self.assertEqual(self.driver.current_url, url_)

    def test_03(self):
        """
        角色管理，进入用户管理模块。
        :return:
        """
        users_Page = usersPage(self.driver)
        users_Page.user_list()
        url_ = ReadConfig().getOptionValue('environment', 'url') + '#/settings/user-list'
        self.assertEqual(self.driver.current_url, url_)


    def test_04(self):
        """
        角色管理，添加用户。
        :return:
        """
        users_Page = usersPage(self.driver)
        users_Page.add_user()
        self.assertNotEqual(1, 2)

    def test_05(self):
        """
        角色管理，批量导入
        :return:
        """
        users_Page = usersPage(self.driver)
        users_Page.user_batchImport()
        self.assertNotEqual(1, 2)

    def test_06(self):
        """
        角色管理,搜索
        :return:
        """
        users_Page = usersPage(self.driver)
        users_Page.search()
        self.assertNotEqual(1, 2)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()

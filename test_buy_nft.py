# This is a test automation script in python
# Application name:qamarket.moiverse.io
# Programmer name : Niyog v
# Date of programming : 24 feb 2022
#
# Test scenario : Buying an NFT and checking whether it comes under my bought items

import time
import pytest
from selenium import webdriver
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

class Test_qamarket:

    # This is a predefined step before buying the NFT
    @pytest.fixture()
    def test_invoke(self):
        self.driver=webdriver.Chrome(executable_path='/Applications/chromedriver')
        self.driver.get('https://www.example.com/')
        self.driver.maximize_window()
        self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div[2]/div').click()
        user=self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div[10]/div/div[2]/div/div/div/div[2]/div/div/input')
        user.send_keys('')# username who is part of the marketplace
        password=self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div[10]/div/div[2]/div/div/div/div[3]/div/div/input')
        password.send_keys('')# password for the username
        self.driver.find_element_by_xpath("//button[@class='MuiButtonBase-root MuiButton-root MuiButton-contained']").click()
        time.sleep(10)
        self.driver.find_element_by_link_text("Explore").click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[1]/div/div[2]/div/div').click()
        self.driver.find_element_by_xpath('//*[@id="menu-"]/div[3]/ul/li[2]').click()
        time.sleep(10)
        self.driver.find_element_by_xpath("//div[@class='styles_exploreAll__1FXSE']/div[4]/div[1]").click()
        time.sleep(10)
        self.driver.find_element_by_xpath("//div[@class='styles_listing__wKd-O']/div[5]").click()
        time.sleep(2)

    # This is the main function which clicks on buy and selenium switches to cashfree and performs function
    # Again after performing function under cashfree it again switch back moiverse
    # After switching back it clicks on profile and checks whether the NFT is appeared in my bought items
    def test_Buy_nft(self,test_invoke):
        self.driver.find_element_by_xpath("//button[@type='button']").click()
        time.sleep(10)
        handles = self.driver.window_handles
        size = len(handles)
        parent_handle = self.driver.current_window_handle # swtiches to child window (cash free) and performs the action to buy the NFT 
        for x in range(size):
            if handles[x] != parent_handle:
                self.driver.switch_to.window(handles[x])
                self.driver.find_element_by_xpath("//div[@class='row vpdlr bg-cf'][2]/div[1]/div[1]").click()
                time.sleep(2)
                self.driver.find_element_by_xpath("//div[@class='row social-icons']/div[2]/form").click()
                break
        time.sleep(30)
        self.driver.switch_to.window(parent_handle)# switches back to the parent window from the child window and verifies whether the NFT bought is under the user profile
        self.driver.find_element_by_xpath("//div[@class='styles_account__3MgT6 styles_menuLink__17kgw']").click()
        self.driver.find_element_by_xpath("//ul[@class='MuiList-root MuiMenu-list styles_menuList__33Jfh MuiList-padding']/div[1]").click()
        time.sleep(2)
        print(self.driver.find_element_by_xpath("//div[@class='styles_history__1Gi3X'][2]/div[1]").text)
        print(self.driver.find_element_by_xpath("//div[@class='styles_history__1Gi3X'][2]/div[3]").text)
        print(self.driver.find_element_by_xpath("//div[@class='styles_history__1Gi3X'][2]/div[5]").text)
        self.driver.find_element_by_xpath("//div[@class='styles_tabsGroup__EOg-L'][1]/div[5]").click()







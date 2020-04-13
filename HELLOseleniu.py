#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-04-01 10:41
# @Author  : dd
from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.get("https://www.baidu.com")
sleep(3)
driver.quit()
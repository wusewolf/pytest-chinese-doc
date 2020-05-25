#!/usr/bin/env python3

'''
    open a browser
'''

import pytest

@pytest.fixture(scope="session")
def browser_instance():
    from selenium import webdriver
    browser = webdriver.Chrome()
    return browser
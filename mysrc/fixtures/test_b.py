#!/usr/bin/env python3

'''
    open a browser
'''

import pytest

'''
def test_func(tmpdir):
    print(tmpdir)
    assert 1==3
'''

def test_maximize_window(browser_instance):
    browser_instance.maximize_window()
    browser_instance.implicitly_wait(5)
    browser_instance.quit()
    assert 1
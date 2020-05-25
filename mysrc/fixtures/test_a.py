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
    



def test_open_browser(browser_instance):
    browser_instance.get('http://www.baidu.com/')
    assert 1
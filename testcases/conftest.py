"""
 #!/usr/bin/env python
 # -*- coding:utf-8 -*-
 @Author: Little Seven
 @FileName: conftest.py
 @DateTime: 2023/4/6 15:19
 @SoftWare: PyCharm
"""
import pytest

@pytest.fixture(scope='class')
def init_class():
    print('这是类方法，只会在开头执行一次')

@pytest.fixture(scope='module')
def demo_module():
    print('这是模块级别的初始化')



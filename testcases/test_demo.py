"""
 #!/usr/bin/env python
 # -*- coding:utf-8 -*-
 @Author: Little Seven
 @FileName: test_demo.py
 @DateTime: 2023/4/4 14:19
 @SoftWare: PyCharm
"""
import pytest,requests
import allure


@allure.feature('feature装饰器')
class Test_Demo:

    @allure.story('story装饰器')
    def test_demo1(self):
        assert 1,1


if __name__ == '__main__':
    # 执行pytest单元测试，生成 Allure 报告需要的数据存在 /temp 目录
    pytest.main(['--alluredir', '../reports/2'])
    # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
    os.system('allure generate ../reports/2 -o ./reports/2/reports_html --clean')

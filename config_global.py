#!/usr/bin/env python
# encoding: utf-8

"""
@author: xuchu
@software: PyCharm
@file: config_global.py
@time: 2017/6/20 上午11:53
"""

data = {
    "headers": "url",
    "postData": ""
}

jmeter_path = "sh /Users/xuchu/xctools/apache-jmeter-3.2/bin/jmeter"
jmx_path = "/Users/xuchu/xcpy/bsbApi/autoJmeter/jmxs/"
jmeter_log = "/Users/xuchu/xcpy/bsbApi/autoJmeter/logs/%s.csv"
# 用户参数
j_Vars = ["count=101010", "data1=22222", "loopV1=v1", "loopV2=v2"]
# 系统参数
d_Vars = ["url=10.1.2.231"]

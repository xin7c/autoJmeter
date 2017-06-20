#!/usr/bin/env python
# encoding: utf-8

"""
@author: xuchu
@software: PyCharm
@file: dafei001.py
@time: 2017/6/20 下午5:32
"""
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
from utils.jmeterRunner import Action
import config_global as cg

dafei001 = Action()
dafei001.runJmeter(jmx_path=dafei001.jmx("dafei001.jmx"),
                var=dafei001.j_var(cg.vars))

dafei001.runJmeter(jmx_path=dafei001.jmx("dafei001.jmx"),
                var=dafei001.j_var(cg.vars))
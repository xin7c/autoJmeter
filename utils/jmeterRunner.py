#!/usr/bin/env python
# encoding: utf-8

"""
@author: xuchu
@software: PyCharm
@file: jmeterRunner.py
@time: 2017/6/20 上午10:03
"""
import subprocess
import time
import config_global as cg


class Action(object):
    def __init__(self):
        self.jmeter_path = cg.jmeter_path
        self.jmx_path = cg.jmx_path
        self.jmeter_log = cg.jmeter_log % self.logger_time()

    def jmx(self, jmx_name):
        """指定jmx文件"""
        return self.jmx_path + jmx_name

    @staticmethod
    def j_var(vars):
        """
            @J参数生成
            @usage:["key1=11111", "key2=22222"]
        """
        _j_var = ""
        for i in vars:
            _j_var += (" -J" + i)
        return _j_var

    @staticmethod
    def d_var(vars):
        """D参数生成"""
        _d_var = ""
        for i in vars:
            _d_var += (" -D" + i)
        return _d_var

    def logger_time(self):
        """执行时间"""
        lt = time.strftime("%Y%m%d-%H%M%S", time.localtime())
        return lt

    def make_cmd(self, var, *args):
        """命令行生成"""
        if var == 0:
            cmd = "%s -n -t %s -l %s %s" % (args[0], args[1], args[2], "")
            return cmd
        else:
            cmd = "%s -n -t %s -l %s %s" % (args[0], args[1], args[2], var)
            return cmd

    def runJmeter(self, jmx_path, var=None):
        """
            @jmeter_path, jmx_path, var=None
            @jmeter_log(目前使用时间戳)
            @var=0: 无jmx属性参数
            @var=var: 按需调整属性参数
        """
        # 提示执行时间
        print("=" * 10 + "执行时间:%s" % self.logger_time() + "=" * 10)
        # 提示执行脚本
        print("脚本名称:%s" % (jmx_path))
        # 提示执行参数
        print("执行参数:%s" % (var))
        p = subprocess.Popen(self.make_cmd(var, self.jmeter_path, jmx_path, self.jmeter_log),
                             shell=True, stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT)
        for line in p.stdout.readlines():
            print(line.strip("\n"))
        # 提示日志路径
        print(self.jmeter_log)


if __name__ == "__main__":
    a = Action()
    # print(a.logger_time())
    a.runJmeter(jmx_path=a.jmx("dafei001.jmx"),
                var=a.j_var(cg.vars))

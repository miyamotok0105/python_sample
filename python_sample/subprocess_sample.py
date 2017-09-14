# -*- coding: utf-8 -*-
import subprocess

command = "ls -la | sort -r"
proc = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout_data, stderr_data = proc.communicate()

# print stdout_data  #標準出力の確認
# print stderr_data  #標準エラーの確認

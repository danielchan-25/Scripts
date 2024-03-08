@echo off
:: 用于Windows下，开机启动 ChatGLM2-6B 模型
E:
cd github\ChatGLM2-6B
E:\conda_files\envs\ChatGLM2-6B\python.exe web_demo.py
cmd /k

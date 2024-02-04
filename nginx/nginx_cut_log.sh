#!/bin/bash
# ---------------------- #
# 日期：2023年3月7日
# 作者：陈某
# 功能：此脚本用于自动分割Nginx的日志，包括 access.log 和 error.log
# ---------------------- #

# Nginx日志文件所在目录
LOG_PATH=/data/nginx/logs

# 获取昨天的日期
YESTERDAY=$(date -d "yesterday" +%Y-%m-%d)

# 获取pid文件路径
PID=/data/nginx/logs/nginx.pid

# 分割日志
mv ${LOG_PATH}/access.log ${LOG_PATH}/access-${YESTERDAY}.log
mv ${LOG_PATH}/error.log ${LOG_PATH}/error-${YESTERDAY}.log

# 向Nginx主进程发送USR1信号，重新打开日志文件
kill -USR1 `cat ${PID}`

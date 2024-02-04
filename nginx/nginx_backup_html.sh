#!/bin/bash
# ---------------------- #
# 日期：2023年3月7日
# 作者：陈某
# 功能：用于备份 nginx 的 html 目录
# ---------------------- #

# nginx路径
NGINX_PATH=/data/nginx

# 获取昨天的日期
YESTERDAY=$(date -d "yesterday" +%Y-%m-%d)

# 备份html目录
tar -cvf /data/backup/html-{$YESTERDAY}.tar.gz /data/nginx/html

# 移动备份文件到/data/backup
#mv /data/nginx/html-{$YESTERDAY}.tar.gz /data/backup/

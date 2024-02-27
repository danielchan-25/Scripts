#!/bin/sh
# ------------------------------------ #
# Date: 2024-02-27
# Author: AlexChan
# Function: Install MySQL Server
# OS: CentOS 7.6
# ------------------------------------ #


yum install -y cmake make gcc gcc-c++ bison ncurses ncurses-devel libaio libaio-devel wget

groupadd mysql
useradd -M -s /sbin/nologin -r -g mysql mysql

wget http://xxxxxxxxxxxx/mysql-5.7.43-el7-x86_64.tar  # MySQLServer的下载地址
tar -xvf mysql-5.7.43-el7-x86_64.tar
tar -xvf mysql-5.7.43-el7-x86_64.tar.gz

mv mysql-5.7.43-el7-x86_64/ /usr/local/mysql
/usr/local/mysql/bin/mysqld --initialize --user=mysql --datadir=/usr/local/mysql/data --basedir=/usr/local/mysql
# Remember Password

cat /etc/my.cnf < EOF
[mysqld]
character_set_server=utf8
init_connect='SET NAMES utf8'
basedir=/usr/local/mysql
datadir=/usr/local/mysql/data
socket=/tmp/mysql.sock
log-error=/var/log/mysqld.log
pid-file=/var/run/mysqld/mysqld.pid
EOF

mkdir -p /usr/local/mysql/data
touch /var/log/mysqld.log
mkdir -p /var/run/mysqld
touch /var/run/mysqld/mysqld.pid
chown -R mysql.mysql /usr/local/mysql
chown -R mysql.mysql /var/run/mysqld
chown -R mysql.mysql /var/log/mysqld.log
chmod 777 /var/log/mysqld.log
chmod 777 /var/run/mysqld/mysqld.pid

/usr/local/mysql/support-files/mysql.server start

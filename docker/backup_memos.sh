#!/bin/sh
# ---------------------------- #
# Date: 2023-05-03
# Author: AlexChing
# Function: Backup Memos Data
# Timed tasks: 59 23 * * *
# ---------------------------- #

memos_dir="/data/docker-data/memos"
backup_dir="/data/cc-NAS/Public/backup/docker-data/memos"

function backup(){
  cd ${memos_dir}
  tar -zcvf memos_`date "+%F"`.tar.gz *
  mv ${memos_dir}/memos_`date "+%F"`.tar.gz ${backup_dir}/.
}

backup

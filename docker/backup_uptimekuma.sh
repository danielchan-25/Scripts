#!/bin/sh
# --------------------------------- #
# Date: 2023-05-04
# Author: AlexChing
# Function: Backup UptimeKuma Data
# Timed tasks: 59 23 * * * 
# --------------------------------- #

uptimekuma_dir="/data/docker-data/uptimekuma/data"
backup_dir="/data/cc-NAS/Public/backup/docker-data/uptimekuma"

function backup(){
  cd ${uptimekuma_dir}
  tar -zcvf uptimekuma_`date "+%F".tar.gz` *
  mv uptimekuma_`date "+%F".tar.gz` ${backup_dir}/.
}

backup

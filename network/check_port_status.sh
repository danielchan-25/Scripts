#!/bin/sh
# ---------------------------- #
# Date: 2023-02-02
# Author: AlexChing
# Function: Check Port Status
# ---------------------------- #

check_port(){
  local port="$1"
  if netstat -tnlp | grep -q ${port}; then
    echo "${port} is Open"
  else
    echo "${port} is NOT Open"
  fi
}

read -p "Please enter the port number you want to query: " port
check_port "${port}"

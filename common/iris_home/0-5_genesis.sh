#!/usr/bin/env bash

#普通irishub
if [ $1 == "irishub" ]
  then
  echo "Init irishub genesis.json"

  sed -i '' 's/stake/uiris/g' /Users/sherlock/.iris/config/genesis.json
  sed -i '' 's/"supers": \[\]/"supers": \[{"description":"test","account_type":0,"address":"iaa1cdq70u5cpczvyt2py80savz7gasgdzx9hc0xw0","added_by":"iaa1cdq70u5cpczvyt2py80savz7gasgdzx9hc0xw0"}\]/g' /Users/sherlock/.iris/config/genesis.json


#irishub自动化测试
  elif [ $1 == "irishub_autotest" ]
  then
  echo "Init irishub_autotest genesis.json"

  sed -i '' 's/stake/uiris/g' /Users/sherlock/.iris/config/genesis.json
  sed -i '' 's/"supers": \[\]/"supers": \[{"description":"test","account_type":0,"address":"iaa1cdq70u5cpczvyt2py80savz7gasgdzx9hc0xw0","added_by":"iaa1cdq70u5cpczvyt2py80savz7gasgdzx9hc0xw0"}\]/g' /Users/sherlock/.iris/config/genesis.json



fi






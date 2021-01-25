#!/usr/bin/env bash

#普通irishub
if [ $1 == "irishub" ]
  then
  echo "Init irishub genesis.json"

  sed -i '' 's/stake/uiris/g' /Users/sherlock/.iris/config/genesis.json
  sed -i '' 's/"supers": \[\]/"supers": \[{"description":"test","account_type":0,"address":"iaa1x8nwtz579zth0dzghkrazpeyp0ua8hqu332xm0","added_by":"iaa1x8nwtz579zth0dzghkrazpeyp0ua8hqu332xm0"}\]/g' /Users/sherlock/.iris/config/genesis.json
  sed -i '' 's/\"voting_period\": \"172800s\"/\"voting_period\": \"90s\"/g' /Users/sherlock/.iris/config/genesis.json

#slash相关
  sed -i '' 's/"signed_blocks_window": "100"/"signed_blocks_window": "20"/g' /Users/sherlock/.iris/config/genesis.json
  sed -i '' 's/"downtime_jail_duration": "600s"/"downtime_jail_duration": "5s"/g' /Users/sherlock/.iris/config/genesis.json


  sed -i '' 's/swagger = false/swagger = true/g'  /Users/sherlock/.iris/config/app.toml
  sed -i '' 's/enable = false/enable = true/g'  /Users/sherlock/.iris/config/app.toml

#irishub自动化测试
  elif [ $1 == "irishub_autotest" ]
  then
  echo "Init irishub_autotest genesis.json"

fi






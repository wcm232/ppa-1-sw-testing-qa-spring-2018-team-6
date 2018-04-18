#!/bin/bash

basePath=$("pwd")
pidFile="${basePath}/pids.pid"

if [ -f $pidFile ];
then
  echo "$pidFile already exists. Stop the process before attempting to start."
else
  echo -n "" > $pidFile
  cd ${basePath}
  echo "Starting Ditto"
  python3 main.py host 2>&1 > /dev/null &
  echo -n "$! " >> $pidFile
fi
#!/bin/bash

basePath=$("pwd")
pidFile="${basePath}/pids.pid"

if [ -f $pidFile ];
then
  echo "$pidFile already exists. Stop the process before attempting to start."
else
  echo -n "" > $pidFile
  cd ${basePath}
  echo "Starting..."
  python3 main.py host &
  echo -n "$! " >> $pidFile
fi
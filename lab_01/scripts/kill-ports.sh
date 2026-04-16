#!/usr/bin/env bash

PID=$(ps aux | grep socat | grep -v grep | awk '{print $2}')
kill $PID
echo "killed PID: $PID"
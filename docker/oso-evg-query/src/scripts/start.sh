#!/bin/bash -e

# This is useful so we can debug containers running inside of OpenShift that are
# failing to start properly.

if [ "$OO_PAUSE_ON_START" = "true" ] ; then
  echo
  echo "This container's startup has been paused indefinitely because OO_PAUSE_ON_START has been set."
  echo
  while true; do
    sleep 10    
  done
fi

echo This container hosts the following applications:
echo
echo '/usr/local/bin/mysql_query'
echo
echo '/usr/local/bin/weekly_duplicate_accounts_report.sh'
echo
echo '/usr/local/bin/check_reporting.sh'
echo
echo 'checking on reporting functionality once a week' 
/usr/local/bin/ops-run-in-loop 36288000 /usr/local/bin/check_reporting.sh &>/dev/null 

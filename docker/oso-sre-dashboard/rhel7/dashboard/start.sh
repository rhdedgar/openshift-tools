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
echo '/usr/local/bin/sre-dashboard'

if [ "$LEGO_CERT" = "true" ] ; then
  echo "running Lego to check if our certificates need to be renewed"
  /usr/local/bin/lego --tls=true --tls.port=":8443" --email="dedgar@redhat.com" --domains="sre-dashboard.openshift.com" --path="/cert/lego" --filename="dashboard" --accept-tos run
  sleep 10
fi

echo
echo '---------------'
echo 'Starting sre-dashboard'
echo '---------------'
exec /usr/local/bin/sre-dashboard

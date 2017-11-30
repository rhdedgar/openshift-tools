#!/bin/bash

PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

for line in $(chroot /host /usr/bin/docker ps | grep -v 'host-monitoring\|logging-fluentd\|image-inspector\|CONTAINER ID' | awk '{print $1}'); do echo "$line" && image-inspector -scan-type=clamav -clam-socket=/host/run/clamd.scan/clamd.sock -container="$line" -post-results-url http://localhost:8080; done

/usr/local/bin/upload_scanlogs

#!/bin/bash

PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

chroot /host /usr/local/bin/scanpod-inmem | awk '$4~/!None/' >> /var/log/clam/in-memory-scan.log

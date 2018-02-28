#!/bin/bash

/usr/local/bin/mysql_query -b -r -s $(date -d -7days +%Y-%m-%d) -e $(date -d +1days +%Y-%m-%d) 2>&1 /var/log/reports/weekly_duplicate_accounts_report_$(date +%Y%m%d)

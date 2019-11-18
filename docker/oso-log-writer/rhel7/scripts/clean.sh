#!/bin/bash

find /logs/$(date +%Y)/ -type d -mtime +30 -delete

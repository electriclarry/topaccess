#!/bin/bash

python /path/to/topaccess.py > /tmp/topaccess.log;
cat /tmp/topaccess.log | mail -s "[APACHE] MTA statistics for YOURHOSTNAME" -r sender@email.address recipient@email.address
rm /tmp/topaccess.log

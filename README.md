# pcsensorplot
Read/store/graph readings from TEMPer USB Thermometer

cronjobs - entries to add to scheduler to take readings and to update graph images

readings.sql - table structure

hr/day/month/allgraph.py -  scripts to read db and creat png images to save in /var/www/html/

readtemp.py - executes precompiled pcsensor application and inserts into db while saving reading to a log file

www/index.html - simple html file to load precreated images for users
